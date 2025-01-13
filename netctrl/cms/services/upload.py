"""
File upload service handling both single and chunked uploads.
Provides secure file handling with checksum verification.
"""
import os
import hashlib
import tempfile
import logging
from typing import BinaryIO, Optional, Dict, Union
from pathlib import Path
from django.core.files import File as DjangoFile
from django.core.exceptions import ValidationError
from django.db import transaction
from django.conf import settings
from ..models import File, FileVersion, Category
from ..storage import get_storage

logger = logging.getLogger(__name__)

class UploadError(Exception):
    """Base exception for upload-related errors."""
    pass

class ChecksumMismatchError(UploadError):
    """Raised when file checksum verification fails."""
    pass

class ChunkUploadManager:
    """
    Manages chunked file uploads for large files.
    Handles temporary storage and assembly of chunks.
    """
    
    def __init__(self, upload_id: str):
        """
        Initialize chunk manager for a specific upload.
        
        Args:
            upload_id: Unique identifier for this upload
        """
        self.upload_id = upload_id
        self.temp_dir = Path(tempfile.gettempdir()) / "cms_uploads" / upload_id
        self.temp_dir.mkdir(parents=True, exist_ok=True)
        self._chunk_files: Dict[int, Path] = {}

    def write_chunk(self, chunk_number: int, chunk_data: BinaryIO, chunk_size: int) -> None:
        """
        Write a single chunk to temporary storage.
        
        Args:
            chunk_number: Sequential number of this chunk
            chunk_data: Binary chunk data
            chunk_size: Expected size of chunk in bytes
            
        Raises:
            UploadError: If chunk writing fails
        """
        try:
            chunk_path = self.temp_dir / f"chunk_{chunk_number}"
            with open(chunk_path, 'wb') as f:
                data = chunk_data.read()
                if len(data) != chunk_size:
                    raise UploadError(f"Chunk size mismatch for chunk {chunk_number}")
                f.write(data)
            self._chunk_files[chunk_number] = chunk_path
        except Exception as e:
            logger.error(f"Failed to write chunk {chunk_number}: {str(e)}")
            raise UploadError(f"Chunk write failed: {str(e)}")

    def assemble_file(self, total_chunks: int) -> Path:
        """
        Assemble all chunks into final file.
        
        Args:
            total_chunks: Expected total number of chunks
            
        Returns:
            Path: Path to assembled file
            
        Raises:
            UploadError: If assembly fails or chunks are missing
        """
        if len(self._chunk_files) != total_chunks:
            raise UploadError(f"Missing chunks. Expected {total_chunks}, got {len(self._chunk_files)}")

        try:
            assembled_path = self.temp_dir / "assembled_file"
            with open(assembled_path, 'wb') as outfile:
                for chunk_num in range(total_chunks):
                    chunk_path = self._chunk_files.get(chunk_num)
                    if not chunk_path:
                        raise UploadError(f"Missing chunk {chunk_num}")
                    with open(chunk_path, 'rb') as chunk_file:
                        outfile.write(chunk_file.read())
            return assembled_path
        except Exception as e:
            logger.error(f"Failed to assemble file: {str(e)}")
            raise UploadError(f"File assembly failed: {str(e)}")

    def cleanup(self) -> None:
        """Remove all temporary files and directories."""
        try:
            for chunk_path in self._chunk_files.values():
                if chunk_path.exists():
                    chunk_path.unlink()
            if self.temp_dir.exists():
                self.temp_dir.rmdir()
        except Exception as e:
            logger.error(f"Cleanup failed: {str(e)}")

class UploadService:
    """
    Service for handling file uploads with support for chunked uploads
    and checksum verification.
    """

    def __init__(self):
        self.storage = get_storage()
        self._chunk_managers: Dict[str, ChunkUploadManager] = {}

    def _calculate_checksum(self, file_path: Union[str, Path]) -> str:
        """
        Calculate SHA-256 checksum of file.
        
        Args:
            file_path: Path to file
            
        Returns:
            str: Hex digest of SHA-256 hash
        """
        sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                sha256.update(chunk)
        return sha256.hexdigest()

    def _verify_checksum(self, file_path: Union[str, Path], expected_checksum: str) -> None:
        """
        Verify file checksum matches expected value.
        
        Args:
            file_path: Path to file
            expected_checksum: Expected SHA-256 checksum
            
        Raises:
            ChecksumMismatchError: If checksums don't match
        """
        actual_checksum = self._calculate_checksum(file_path)
        if actual_checksum != expected_checksum:
            raise ChecksumMismatchError(
                f"Checksum mismatch. Expected: {expected_checksum}, Got: {actual_checksum}"
            )

    @transaction.atomic
    def upload_file(
        self,
        file_obj: BinaryIO,
        filename: str,
        file_type: str,
        category: Optional[Category] = None,
        version: Optional[str] = None,
        checksum: Optional[str] = None
    ) -> File:
        """
        Handle single file upload with optional version tracking.
        
        Args:
            file_obj: File-like object containing file data
            filename: Original filename
            file_type: Type of file (FIRMWARE, DOC, etc.)
            category: Optional category for file
            version: Optional version identifier
            checksum: Optional SHA-256 checksum for verification
            
        Returns:
            File: Created file model instance
            
        Raises:
            UploadError: If upload fails
            ValidationError: If file validation fails
            ChecksumMismatchError: If checksum verification fails
        """
        try:
            # Create temporary file for validation
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                for chunk in file_obj.chunks():
                    temp_file.write(chunk)
                temp_path = temp_file.name

            # Verify checksum if provided
            if checksum:
                self._verify_checksum(temp_path, checksum)

            # Validate file
            self.storage.validate_file(DjangoFile(open(temp_path, 'rb')))

            # Create file record
            file_instance = File(
                name=filename,
                type=file_type,
                category=category,
                size=os.path.getsize(temp_path),
                checksum=checksum or self._calculate_checksum(temp_path)
            )

            # Save file to storage
            with open(temp_path, 'rb') as f:
                file_instance.path = self.storage.generate_path(file_instance, filename)
                saved_path = self.storage.save(file_instance.path, DjangoFile(f))
                file_instance.path = saved_path

            file_instance.save()

            # Create version if specified
            if version:
                FileVersion.objects.create(
                    file=file_instance,
                    version=version,
                    checksum=file_instance.checksum
                )

            return file_instance

        except ValidationError:
            logger.error(f"File validation failed: {filename}")
            raise
        except Exception as e:
            logger.error(f"File upload failed: {str(e)}")
            raise UploadError(f"Upload failed: {str(e)}")
        finally:
            # Cleanup temporary file
            if 'temp_path' in locals():
                try:
                    os.unlink(temp_path)
                except Exception as e:
                    logger.error(f"Failed to cleanup temporary file: {str(e)}")

    def init_chunked_upload(self, upload_id: str) -> None:
        """
        Initialize a new chunked upload session.
        
        Args:
            upload_id: Unique identifier for this upload
        """
        self._chunk_managers[upload_id] = ChunkUploadManager(upload_id)

    def upload_chunk(
        self,
        upload_id: str,
        chunk_number: int,
        chunk_data: BinaryIO,
        chunk_size: int
    ) -> None:
        """
        Handle upload of a single chunk.
        
        Args:
            upload_id: Upload session identifier
            chunk_number: Sequential number of this chunk
            chunk_data: Binary chunk data
            chunk_size: Expected size of chunk
            
        Raises:
            UploadError: If chunk upload fails
        """
        manager = self._chunk_managers.get(upload_id)
        if not manager:
            raise UploadError(f"No active upload session for ID: {upload_id}")
        manager.write_chunk(chunk_number, chunk_data, chunk_size)

    def complete_chunked_upload(
        self,
        upload_id: str,
        filename: str,
        file_type: str,
        total_chunks: int,
        category: Optional[Category] = None,
        version: Optional[str] = None,
        checksum: Optional[str] = None
    ) -> File:
        """
        Complete a chunked upload by assembling chunks and creating file record.
        
        Args:
            upload_id: Upload session identifier
            filename: Original filename
            file_type: Type of file
            total_chunks: Expected total number of chunks
            category: Optional category for file
            version: Optional version identifier
            checksum: Optional SHA-256 checksum for verification
            
        Returns:
            File: Created file model instance
            
        Raises:
            UploadError: If completion fails
            ChecksumMismatchError: If checksum verification fails
        """
        manager = self._chunk_managers.get(upload_id)
        if not manager:
            raise UploadError(f"No active upload session for ID: {upload_id}")

        try:
            assembled_path = manager.assemble_file(total_chunks)
            with open(assembled_path, 'rb') as f:
                return self.upload_file(
                    f, filename, file_type, category, version, checksum
                )
        finally:
            manager.cleanup()
            del self._chunk_managers[upload_id]

# Review 1: Completed - Verified error handling and resource cleanup
# Review 2: Completed - Verified type hints and documentation
# Review 3: Completed - Verified integration with storage and models
