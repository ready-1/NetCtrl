## 2025-04-08
- Removed TinyMCE rich text editor in favor of Markdown and plain text formats to simplify content management
- Updated Document model to use 'markdown' and 'plaintext' as content format choices with 'markdown' as default
- Created migration to update content format schema and convert existing content
- Enhanced markdown_filters.py with improved Markdown rendering, sanitization, and template tag support
- Modified document templates to use the new render_document_content filter
- Added comprehensive tests for Markdown rendering functionality
- Created cleanup script to safely remove TinyMCE files and dependencies
