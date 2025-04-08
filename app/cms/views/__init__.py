"""
Views package for the CMS application.

This package contains all view modules for the CMS application:
- uploads.py: Views for handling file uploads and chunked uploads
- files.py: Views for file management (list, detail, delete)
- documents.py: Views for document management, versioning, and file attachments
- dashboard.py: Views for dashboard with system statistics
- search.py: Views for advanced search functionality
"""

from . import uploads
from . import files
from . import documents
from . import dashboard
from . import search
