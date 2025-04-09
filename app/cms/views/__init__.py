"""
Views package for the CMS application.

This package contains all view modules for the CMS application:
- uploads.py: Views for handling file uploads and chunked uploads
- files.py: Views for file management (list, detail, delete)
- documents.py: Views for document management, versioning, and file attachments
- dashboard.py: Views for dashboard with system statistics
- search.py: Views for advanced search functionality
- users.py: Views for user profile management and activity tracking
- taxonomy.py: Views for tag and category management
- content.py: Views for content-focused document browsing (wiki-like experience)
"""

from . import uploads
from . import files
from . import documents
from . import dashboard
from . import search
from . import users
from . import taxonomy
from . import content
