"""
CMS application models.

This package contains all models related to the Content Management System.
Models are split into separate modules for better organization:

- users.py: User-related models (profiles, preferences)
- documents.py: Document models, categories, and tags
- files.py: File storage and file upload models
"""

from cms.models.users import UserProfile
from cms.models.documents import Category, Tag, Document
from cms.models.files import FileCategory, FileTag, File, FileChunkedUpload

__all__ = [
    'UserProfile',
    'Category',
    'Tag', 
    'Document',
    'FileCategory',
    'FileTag',
    'File',
    'FileChunkedUpload',
]
