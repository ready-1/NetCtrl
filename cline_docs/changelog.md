# NetCtrl CMS Changelog

This file tracks significant changes to the codebase.

## 2025-04-09
- Implemented TODO management system with structured format in `cline_docs/todos.md`
- Added TODO system configuration to `.clinerules` with categories, priority levels, and workflow rules
- Updated `activeContext.md` with TODO system usage instructions
- Created streamlined workflow for adding, categorizing, and managing future tasks
- Added deployment workflow task to the TODO list with detailed implementation steps
- Updated `activeContext.md` to include deployment workflow planning as a next step

## 2025-04-08
- Fixed TinyMCE editor read-only issue by adding initialization code to prevent read-only mode. Modified `editor-switcher.js` to set global TinyMCE settings with `readonly: false` and verify editor mode.
- Resolved TinyMCE initialization issues by implementing a comprehensive approach to self-hosted mode configuration. Created a new `tinymce-core.js` module that provides robust initialization handling with proper path detection, warning suppression, and error management to ensure the editor reliably loads and displays correctly.
- Fixed TinyMCE resource loading issues by adding explicit path mappings for plugins, themes, models, and skins to ensure all editor components load correctly from the proper locations.
- Completely rewrote TinyMCE initialization with hardcoded paths, multi-level read-only prevention, and comprehensive error handling to resolve persistent loading and API key warning issues.
- Fixed circular import in CMS document forms by directly defining form classes in forms/__init__.py module.
- Fixed URL name mismatch for user profile in base.html template.

## 2025-04-07
- Implemented user profile management system with profile editing capabilities.
- Created password change functionality with enhanced security features.
- Added user activity tracking to display documents and files created by the user.
- Implemented responsive UI for profile management with dark mode support.

## 2025-04-06
- Implemented dashboard with system statistics and activity tracking.
- Created advanced search functionality with multi-model search and filtering.
- Added dashboard template with responsive UI and data visualization.
- Enhanced navigation with integrated search functionality across documents and files.

## 2025-04-05
- Implemented document management system with version tracking and file associations.
- Created document versioning functionality to maintain history of document changes.
- Added ability to associate multiple files with documents for better content organization.
- Implemented document CRUD operations with proper permission handling.

## 2025-04-04
- Implemented file metadata editing functionality allowing users to update file details after upload.
- Fixed file upload functionality to reliably handle files up to 5GB in size.
- Created user-friendly file detail page with download, edit, and delete capabilities.
- Integrated file categorization and tagging system for better organization.

## 2025-04-03
- Created detailed Django implementation plan for CMS with file management supporting files up to 5GB.
- Implemented Python logging facility with syslog integration for standardized application logging.
- Created example Django views demonstrating proper logging with different log levels.
- Fixed TCP logging by implementing a custom TCP handler for reliable syslog communication.

## 2025-04-02
- Fixed Docker infrastructure logging configuration by changing container logging driver from syslog to json-file.
- Removed non-existent python-logging-handler package from requirements.txt.
- Removed unnecessary logshipper container since logs are now managed via json-file driver.
- Configured syslog-ng to forward logs to Graylog in GELF format with proper host field.
- Exposed GELF UDP port (12201) in Graylog container to receive logs directly.

## 2025-04-01
- Changed log viewer from Dozzle to Graylog for improved log viewing capabilities.
- Implemented Syslog server with log categorization and web viewer.
- Used balabit/syslog-ng for the syslog server and replaced Dozzle with Graylog.
- Created Docker Compose configuration for centralized logging.
- Set up log rotation with categorization by service.

## 2025-03-31
- Initial setup completed.
- Created detailed strategic plan for Phase 1 (CMS with file management).
- Created implementation instructions for all major Phase 1 components.
