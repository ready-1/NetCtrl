"""File management service layer"""
from typing import Optional, List, Dict, Any, Tuple
from datetime import datetime
import os
import shutil
import logging
from fastapi import HTTPException, UploadFile, status
from sqlalchemy import select, or_, and_, desc, delete
from sqlalchemy.orm import Session, joinedload

from app.core.config import settings
from app.models.content import ContentFile, ContentPermission
from app.models.role import UserRole
from app.services.content import ContentService

class FileService:
    """Service for managing files"""
    
    @staticmethod
    def get_file_path(file_id: str) -> str:
        """Get the file storage path based on ID"""
        # Create uploads directory if it doesn't exist
        uploads_dir = os.path.join(settings.UPLOAD_DIR)
        os.makedirs(uploads_dir, exist_ok=True)
        
        # Create a nested directory structure based on file ID
        # This helps prevent too many files in a single directory
        if file_id:
            id_str = str(file_id)
            # Use first few characters for directory structure
            if len(id_str) >= 4:
                nested_dir = os.path.join(uploads_dir, id_str[:2], id_str[2:4])
                os.makedirs(nested_dir, exist_ok=True)
                return nested_dir
        
        return uploads_dir
    
    @staticmethod
    async def save_uploaded_file(
        file: UploadFile,
        file_id: str
    ) -> str:
        """Save an uploaded file to disk"""
        # Get destination directory
        dest_dir = FileService.get_file_path(file_id)
        
        # Create full path with filename
        file_path = os.path.join(dest_dir, file.filename)
        
        # Save the file
        try:
            # Create a temporary file
            with open(file_path, "wb") as buffer:
                # Copy from upload file to destination
                shutil.copyfileobj(file.file, buffer)
            
            return file_path
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error saving file: {str(e)}"
            )
        finally:
            # Close the file
            await file.close()

    @staticmethod
    async def create_file(
        db: Session,
        file: UploadFile,
        content_id: Optional[int] = None,
        user_id: int = None
    ) -> ContentFile:
        """Create a new file in the database"""
        # Validate file size
        try:
            file.file.seek(0, 2)  # Move to end
            file_size = file.file.tell()  # Get size
            file.file.seek(0)  # Reset position
            
            # Check if file is too large
            max_size = settings.MAX_UPLOAD_SIZE
            if file_size > max_size:
                raise HTTPException(
                    status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                    detail=f"File too large. Maximum size is {max_size / (1024 * 1024)}MB"
                )
        except Exception as e:
            if isinstance(e, HTTPException):
                raise e
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error processing file: {str(e)}"
            )
        
        # Create file record
        file_record = ContentFile(
            filename=file.filename,
            file_size=file_size,
            mime_type=file.content_type or "application/octet-stream",
            content_id=content_id,
            uploaded_by=user_id,
            uploaded_at=datetime.now()
        )
        
        # Add to database to get ID
        db.add(file_record)
        await db.commit()
        await db.refresh(file_record)
        
        # Now save file to disk using ID for path organization
        file_path = await FileService.save_uploaded_file(file, str(file_record.id))
        
        # Update file record with path
        file_record.file_path = file_path
        await db.commit()
        await db.refresh(file_record)
        
        return file_record

    @staticmethod
    async def get_file_by_id(
        db: Session,
        file_id: int,
        user_id: int,
        user_role: UserRole
    ) -> Optional[ContentFile]:
        """Get a file by ID"""
        # Get file
        query = select(ContentFile).where(ContentFile.id == file_id)
        result = await db.execute(query)
        file = result.scalar_one_or_none()
        
        if file is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"File with id {file_id} not found"
            )
        
        # Check permissions if file is associated with content
        if file.content_id:
            can_view = await ContentService.check_permission(
                db, file.content_id, user_id, user_role, "view"
            )
            
            if not can_view:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="You don't have permission to access this file"
                )
        
        return file

    @staticmethod
    async def list_files(
        db: Session,
        user_id: int,
        user_role: UserRole,
        content_id: Optional[int] = None,
        skip: int = 0,
        limit: int = 100
    ) -> Tuple[List[ContentFile], int]:
        """List files with optional filtering by content ID"""
        # Base query
        query = select(ContentFile)
        count_query = select(ContentFile)
        
        # Apply content_id filter if provided
        if content_id:
            # Check if user has permission to view the content
            can_view = await ContentService.check_permission(
                db, content_id, user_id, user_role, "view"
            )
            
            if not can_view:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="You don't have permission to access files for this content"
                )
            
            query = query.where(ContentFile.content_id == content_id)
            count_query = count_query.where(ContentFile.content_id == content_id)
        else:
            # If not filtering by content_id, only show files:
            # 1. That the user uploaded
            # 2. That are associated with content the user can view
            # 3. Admin can see all files
            if user_role != UserRole.ADMIN:
                # Get content IDs where user has view permission
                subquery = (
                    select(ContentFile.id)
                    .join(
                        ContentPermission,
                        ContentFile.content_id == ContentPermission.content_id
                    )
                    .where(
                        and_(
                            ContentPermission.role == user_role,
                            ContentPermission.can_view == True
                        )
                    )
                )
                
                result = await db.execute(subquery)
                viewable_content_files = [r[0] for r in result]
                
                # Filter query
                filter_condition = or_(
                    ContentFile.uploaded_by == user_id,
                    ContentFile.id.in_(viewable_content_files),
                    ContentFile.content_id.is_(None)  # Unassociated files
                )
                
                query = query.where(filter_condition)
                count_query = count_query.where(filter_condition)
        
        # Get total count
        count_result = await db.execute(count_query)
        total_count = len(count_result.all())
        
        # Apply pagination and get results
        query = query.order_by(desc(ContentFile.uploaded_at)).offset(skip).limit(limit)
        result = await db.execute(query)
        files = result.scalars().all()
        
        return files, total_count

    @staticmethod
    async def delete_file(
        db: Session,
        file_id: int,
        user_id: int,
        user_role: UserRole
    ) -> bool:
        """Delete a file"""
        # Get file
        query = select(ContentFile).where(ContentFile.id == file_id)
        result = await db.execute(query)
        file = result.scalar_one_or_none()
        
        if file is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"File with id {file_id} not found"
            )
        
        # Check permissions
        if file.content_id:
            # If associated with content, check content permissions
            can_delete = await ContentService.check_permission(
                db, file.content_id, user_id, user_role, "delete"
            )
            
            if not can_delete and file.uploaded_by != user_id and user_role != UserRole.ADMIN:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="You don't have permission to delete this file"
                )
        elif file.uploaded_by != user_id and user_role != UserRole.ADMIN:
            # If not associated with content, only uploader or admin can delete
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You don't have permission to delete this file"
            )
        
        # Delete file from disk
        try:
            if os.path.exists(file.file_path):
                os.remove(file.file_path)
        except Exception as e:
            # Log error but continue
            logging.error(f"Error deleting file from disk: {str(e)}")
        
        # Delete file record
        delete_stmt = delete(ContentFile).where(ContentFile.id == file_id)
        await db.execute(delete_stmt)
        await db.commit()
        
        return True

    @staticmethod
    async def update_file_metadata(
        db: Session,
        file_id: int,
        metadata: Dict[str, Any],
        user_id: int,
        user_role: UserRole
    ) -> ContentFile:
        """Update file metadata"""
        # Get file
        query = select(ContentFile).where(ContentFile.id == file_id)
        result = await db.execute(query)
        file = result.scalar_one_or_none()
        
        if file is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"File with id {file_id} not found"
            )
        
        # Check permissions
        if file.content_id:
            # If associated with content, check content permissions
            can_edit = await ContentService.check_permission(
                db, file.content_id, user_id, user_role, "edit"
            )
            
            if not can_edit and file.uploaded_by != user_id and user_role != UserRole.ADMIN:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="You don't have permission to update this file"
                )
        elif file.uploaded_by != user_id and user_role != UserRole.ADMIN:
            # If not associated with content, only uploader or admin can update
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You don't have permission to update this file"
            )
        
        # Update metadata fields
        # Only allow updating filename and content_id
        if "filename" in metadata:
            file.filename = metadata["filename"]
        
        if "content_id" in metadata:
            # If changing content association, check permission for new content
            if metadata["content_id"] and metadata["content_id"] != file.content_id:
                can_edit_new = await ContentService.check_permission(
                    db, metadata["content_id"], user_id, user_role, "edit"
                )
                
                if not can_edit_new and user_role != UserRole.ADMIN:
                    raise HTTPException(
                        status_code=status.HTTP_403_FORBIDDEN,
                        detail="You don't have permission to associate this file with the specified content"
                    )
            
            file.content_id = metadata["content_id"]
        
        await db.commit()
        await db.refresh(file)
        
        return file
