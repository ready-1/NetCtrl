# NetCtrl CMS Active Context

## Current State

The NetCtrl CMS is a content management system with document and file management capabilities. The system is in active development with the following components currently implemented:

- **User Authentication**: Login/logout functionality with profile management
- **Document Management**: CRUD operations for documents with rich text editing
- **File Management**: Chunked file upload supporting large files (up to 5GB)
- **Taxonomy System**: Categories and tags for organizing content
- **Dashboard**: System statistics and activity tracking
- **Search**: Advanced search functionality across documents and files

## Recent Changes (Last 24 Hours)

- Enhanced environment variables management and security:
  - Fixed placeholder detection to prevent false positives for common values (True/False, environment names)
  - Added robust CSS sanitizer support to fix warnings in Markdown rendering
  - Improved GitHub API integration with graceful degradation when token is missing
  - Added proper HTTP status code handling in API views
  - Created `verify_env.py` script for environment configuration validation
  - Added comprehensive placeholder detection with regex patterns
  - Improved environment validation with robust type conversion and error handling
  
- Implemented comprehensive environment variables management:
  - Created centralized environment variable module (`env_config.py`) with type validation
  - Moved all secrets and configuration values from hardcoded settings to `.env` file
  - Removed exposed GitHub token from settings.py
  - Added detailed documentation for environment setup in README.md and dedicated guide
  - Created `.env.example` template with placeholder values and clear documentation
  - Implemented environment-specific configurations for development, testing, and production
  - Added validation and proper error handling for missing critical variables

- Added TODO management system with structured format in `cline_docs/todos.md`
  - Added configuration to `.clinerules` with categories and priority levels
  - Created streamlined workflow for managing future tasks

## Current Focus

- Document management system enhancements
- Administrative tools for user and content management
- UI/UX improvements for content editing
- Permission system refinement

## Next Steps

- Plan and implement the deployment workflow for air-gapped Debian environment
- Implement administrative dashboard for user management
- Add bulk operations for document and file management
- Improve taxonomy management interface
- Enhance search functionality with filters and saved searches
- Address any remaining UI issues in the document editor

## Technical Notes

- The TinyMCE integration requires properly handling the editor's initialization to prevent read-only mode
- Document content supports both HTML (via TinyMCE) and Markdown (via SimpleMDE) formats
- Large file uploads are handled via chunking using the django-chunked-upload package

## TODO Management System

A TODO tracking system has been implemented to manage future tasks, bugs, features, and improvements. The system uses a dedicated `cline_docs/todos.md` file with configuration in `.clinerules`.

### Usage Instructions

- **Adding TODOs**: Use the syntax `#TODO: [description]` with optional priority (!-!!!!)
- **Categories**: TODOs are automatically categorized as Feature, Fix, Improve, or Document
- **Priorities**: ! (Low), !! (Normal), !!! (High), !!!! (Critical)
- **Corrections**: Use `#Category` and/or priority markers (e.g., `#Feature !!!`) to modify suggestions
- **Working on TODOs**: Use the syntax `Work on TODO: [description]` to begin implementation

See `cline_docs/todos.md` for the current list of tasks and full explanation of the system.
