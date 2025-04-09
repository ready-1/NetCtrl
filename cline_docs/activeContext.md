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

- Fixed TinyMCE editor read-only issue by modifying `editor-switcher.js` to:
  - Set global TinyMCE settings with `readonly: false`
  - Add verification and correction of editor mode after initialization
  - Improve error handling for TinyMCE initialization
- Fixed TinyMCE editor initialization and resource loading issues:
  - Completely rewrote `tinymce-core.js` with hardcoded paths instead of dynamic detection
  - Implemented multi-layered read-only prevention with four separate strategies
  - Added comprehensive resource validation and error handling
  - Applied aggressive API key warning suppression
  - Improved plugin resolution with explicit external_plugins mapping
  - Configured direct resource paths for all components (themes, plugins, models, skins)
- These changes resolved the issues where the rich text editor would initialize in read-only mode and display API key warnings, providing a seamless editing experience

## Current Focus

- Document management system enhancements
- Administrative tools for user and content management
- UI/UX improvements for content editing
- Permission system refinement

## Next Steps

- Implement administrative dashboard for user management
- Add bulk operations for document and file management
- Improve taxonomy management interface
- Enhance search functionality with filters and saved searches
- Address any remaining UI issues in the document editor

## Technical Notes

- The TinyMCE integration requires properly handling the editor's initialization to prevent read-only mode
- Document content supports both HTML (via TinyMCE) and Markdown (via SimpleMDE) formats
- Large file uploads are handled via chunking using the django-chunked-upload package
