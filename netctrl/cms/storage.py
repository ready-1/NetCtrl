import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.text import slugify
from datetime import datetime
import hashlib

class SecureCMSStorage(FileSystemStorage):
    """
    Custom storage backend for CMS files with enhanced security and organization.
    Implements path generation and file validation.
    """

    def __init__(self, *args, **kwargs):
        """Initialize storage with CMS-specific configuration."""
        if not kwargs.get('location'):
            kwargs['location'] = os.path.join(settings.MEDIA_ROOT, 'cms_files')
        super().__init__(*args, **kwargs)

    def get_valid_name(self, name):
        """
        Return a filename suitable for use with the underlying storage system.
        Ensures security and consistency in filenames.
        """
        name = str(name).strip().replace(' ', '_')
        name = slugify(os.path.splitext(name)[0]) + os.path.splitext(name)[1]
        return name

    def get_available_name(self, name, max_length=None):
        """
        Return a filename that's free on the target storage system.
        Adds timestamp to ensure uniqueness.
        """
        dir_name, file_name = os.path.split(name)
        file_root, file_ext = os.path.splitext(file_name)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        new_name = f"{file_root}_{timestamp}{file_ext}"
        
        if dir_name:
            new_name = os.path.join(dir_name, new_name)
            
        return super().get_available_name(new_name, max_length)

    def generate_path(self, instance, filename):
        """
        Generate a unique path for storing the file based on its type and metadata.
        Creates organized directory structure.
        
        Args:
            instance: File model instance
            filename: Original filename
            
        Returns:
            str: Generated storage path
        """
        # Get file type directory
        type_dir = instance.type.lower()
        
        # Generate date-based path
        date_path = datetime.now().strftime('%Y/%m')
        
        # Create category path if available
        category_path = ''
        if instance.category:
            category_path = slugify(instance.category.get_full_path())
        
        # Generate unique filename
        file_root, file_ext = os.path.splitext(self.get_valid_name(filename))
        unique_id = hashlib.sha256(
            f"{file_root}{datetime.now().timestamp()}".encode()
        ).hexdigest()[:8]
        
        final_name = f"{file_root}_{unique_id}{file_ext}"
        
        # Combine all path components
        path_components = [
            'cms_files',
            type_dir,
            date_path
        ]
        
        if category_path:
            path_components.append(category_path)
            
        path_components.append(final_name)
        
        return os.path.join(*path_components)

    def validate_file(self, file_obj):
        """
        Validate file before storage.
        Implement security checks and constraints.
        
        Args:
            file_obj: File object to validate
            
        Raises:
            ValidationError: If file validation fails
        """
        # Implement security validation as needed
        # Example: virus scanning, file type validation, etc.
        pass

def get_storage():
    """
    Factory function to create storage instance with proper configuration.
    Allows for future storage backend changes.
    
    Returns:
        SecureCMSStorage: Configured storage instance
    """
    return SecureCMSStorage()

# Path generation helpers
def get_firmware_path(instance, filename):
    """Generate path for firmware files."""
    storage = get_storage()
    instance.type = 'FIRMWARE'
    return storage.generate_path(instance, filename)

def get_document_path(instance, filename):
    """Generate path for documentation files."""
    storage = get_storage()
    instance.type = 'DOC'
    return storage.generate_path(instance, filename)

def get_config_path(instance, filename):
    """Generate path for configuration files."""
    storage = get_storage()
    instance.type = 'CONFIG'
    return storage.generate_path(instance, filename)
