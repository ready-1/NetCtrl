"""
File models for the NetCtrl CMS.

This module defines models for file management:
- FileCategory: For organizing files
- FileTag: For tagging and filtering files
- File: The main file storage model
- FileChunkedUpload: For handling large file uploads in chunks
"""

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from chunked_upload.models import ChunkedUpload
import uuid
import os
import mimetypes
import logging

logger = logging.getLogger(__name__)

class FileCategory(models.Model):
    """
    Category model for organizing files.
    
    Attributes:
        name (CharField): The category name
        slug (SlugField): URL-friendly version of the name
        description (TextField): Optional description of the category
    """
    name = models.CharField("Name", max_length=100)
    slug = models.SlugField("Slug", max_length=100, unique=True)
    description = models.TextField("Description", blank=True)
    
    class Meta:
        verbose_name = "File Category"
        verbose_name_plural = "File Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """Auto-generate slug if not provided."""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        logger.info(f"File category saved: {self.name}")
    
    def get_absolute_url(self):
        """Get URL for file category detail page."""
        return reverse('cms:file_category_detail', kwargs={'slug': self.slug})


class FileTag(models.Model):
    """
    Tags for files to enable filtering and organization.
    
    Attributes:
        name (CharField): The tag name
        slug (SlugField): URL-friendly version of the name
    """
    name = models.CharField("Name", max_length=50)
    slug = models.SlugField("Slug", max_length=50, unique=True)
    
    class Meta:
        verbose_name = "File Tag"
        verbose_name_plural = "File Tags"
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """Auto-generate slug if not provided."""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        logger.info(f"File tag saved: {self.name}")
    
    def get_absolute_url(self):
        """Get URL for file tag detail page."""
        return reverse('cms:file_tag_detail', kwargs={'slug': self.slug})


class File(models.Model):
    """
    File model for storing uploaded files.
    
    Attributes:
        name (CharField): Name of the file (user-provided)
        file (FileField): The actual file
        original_filename (CharField): Original name of the uploaded file
        file_size (BigIntegerField): Size in bytes
        mime_type (CharField): MIME type of the file
        description (TextField): Optional description
        category (ForeignKey): File category for organization
        tags (ManyToManyField): Tags for filtering
        uploaded_by (ForeignKey): User who uploaded the file
        uploaded_at (DateTimeField): When the file was uploaded
        last_accessed (DateTimeField): When the file was last accessed
        download_count (PositiveIntegerField): Number of times downloaded
        uuid (UUIDField): Unique identifier for the file
    """
    name = models.CharField("Name", max_length=255)
    file = models.FileField("File", upload_to='uploads/%Y/%m/%d/')
    original_filename = models.CharField("Original filename", max_length=255)
    file_size = models.BigIntegerField("File size", help_text="Size in bytes")
    mime_type = models.CharField("MIME type", max_length=255)
    description = models.TextField("Description", blank=True)
    category = models.ForeignKey(
        FileCategory, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='files',
        verbose_name="Category"
    )
    tags = models.ManyToManyField(
        FileTag, 
        blank=True, 
        related_name='files',
        verbose_name="Tags"
    )
    uploaded_by = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='uploaded_files',
        verbose_name="Uploaded by"
    )
    uploaded_at = models.DateTimeField("Uploaded at", auto_now_add=True)
    last_accessed = models.DateTimeField("Last accessed", null=True, blank=True)
    download_count = models.PositiveIntegerField("Download count", default=0)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
    
    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """Determine MIME type and file size if not already set."""
        # Only do this for new files, not when updating existing records
        if not self.pk and self.file:
            # Set original filename if not already set
            if not self.original_filename:
                self.original_filename = os.path.basename(self.file.name)
            
            # Set file size if not already set
            if not self.file_size:
                self.file_size = self.file.size
            
            # Set MIME type if not already set
            if not self.mime_type:
                self.detect_mime_type()
        
        super().save(*args, **kwargs)
        logger.info(f"File saved: {self.name} ({self.file_size} bytes)")
    
    def detect_mime_type(self):
        """
        Detect MIME type using python-magic or mimetypes.
        
        This method tries to use python-magic first (more accurate),
        and falls back to mimetypes module if python-magic is not available.
        """
        if not self.file:
            return
        
        # Try to detect using python-magic
        try:
            import magic
            self.mime_type = magic.from_buffer(self.file.read(2048), mime=True)
            self.file.seek(0)  # Reset file pointer
        except (ImportError, Exception) as e:
            logger.warning(f"MIME type detection with python-magic failed: {e}")
            # Fallback to mimetypes module
            mime_type, encoding = mimetypes.guess_type(self.file.name)
            self.mime_type = mime_type or 'application/octet-stream'
    
    def get_absolute_url(self):
        """Get URL for file detail page."""
        return reverse('cms:file_detail', kwargs={'uuid': self.uuid})
    
    def record_download(self):
        """Record a file download, incrementing the counter."""
        from django.utils import timezone
        self.download_count += 1
        self.last_accessed = timezone.now()
        self.save(update_fields=['download_count', 'last_accessed'])
        logger.info(f"File downloaded: {self.name} by user ID {self.uploaded_by.id}")
    
    def file_extension(self):
        """Get the file extension."""
        return os.path.splitext(self.file.name)[1].lstrip('.')
    
    def is_image(self):
        """Check if the file is an image."""
        return self.mime_type.startswith('image/')
    
    def get_icon_class(self):
        """
        Return the appropriate icon class based on MIME type.
        
        This method returns a Bootstrap icon class for use in templates.
        """
        if self.mime_type.startswith('image/'):
            return 'bi-file-image'
        elif self.mime_type.startswith('video/'):
            return 'bi-file-play'
        elif self.mime_type.startswith('audio/'):
            return 'bi-file-music'
        elif 'pdf' in self.mime_type:
            return 'bi-file-pdf'
        elif 'word' in self.mime_type or 'document' in self.mime_type:
            return 'bi-file-word'
        elif 'excel' in self.mime_type or 'spreadsheet' in self.mime_type:
            return 'bi-file-excel'
        elif 'powerpoint' in self.mime_type or 'presentation' in self.mime_type:
            return 'bi-file-ppt'
        elif 'zip' in self.mime_type or 'archive' in self.mime_type or 'compressed' in self.mime_type:
            return 'bi-file-zip'
        elif 'text' in self.mime_type:
            return 'bi-file-text'
        else:
            return 'bi-file'


class FileChunkedUpload(ChunkedUpload):
    """
    Custom chunked upload model for handling large file uploads.
    
    Extends the base ChunkedUpload model with additional fields.
    
    Attributes:
        Inherits all attributes from ChunkedUpload
        category_id (PositiveIntegerField): Optional category ID for the file
        description (TextField): Optional description for the file
        tags (CharField): Optional comma-separated list of tag IDs
    """
    category_id = models.PositiveIntegerField("Category ID", null=True, blank=True)
    description = models.TextField("Description", blank=True)
    tags = models.CharField(
        "Tags",
        max_length=255, 
        blank=True, 
        help_text="Comma-separated tag IDs to apply to file"
    )
    
    class Meta(ChunkedUpload.Meta):
        abstract = False
        verbose_name = "File Chunked Upload"
        verbose_name_plural = "File Chunked Uploads"
    
    def delete(self, delete_file=True, *args, **kwargs):
        """Override delete to ensure proper logging."""
        if self.file and self.filename:
            logger.info(f"Chunked upload deleted: {self.filename} ({self.offset} bytes)")
        return super().delete(delete_file, *args, **kwargs)
