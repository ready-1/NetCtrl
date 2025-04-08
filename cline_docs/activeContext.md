# Active Context

This document tracks the current state, decisions, and priorities for the NetCtrl project.

## Current State

- Project defined with comprehensive requirements for both Phase 1 (CMS) and Phase 2 (Network Management)
- CRCT system initialized with core documentation structure
- Transitioned to Execution phase, implementing components according to strategic plan
- Project technical stack defined: Django, PostgreSQL, Docker, Nginx, Bootstrap 5.3
- Phase 1 requirements solidified: CMS with file management up to 5GB
- Phase 2 requirements outlined: Network management for Netgear M4300 switches
- Docker infrastructure implementation started with Syslog server
- Syslog server implemented with log categorization by service and Graylog web viewer
- Completed Docker setup for syslog-ng (balabit/syslog-ng) and log viewer (graylog/graylog)
- Implemented log rotation with retention periods (7-30 days)
- Created testing script for verifying syslog functionality
- Nginx configured to proxy the log viewer at /logs/ path
- Fixed container logging configuration using json-file driver instead of syslog
- Removed non-existent python-logging-handler package from requirements.txt
- Removed unnecessary logshipper container since logs are now managed via json-file driver
- Configured syslog-ng to forward logs to Graylog in GELF format with proper host field
- Exposed GELF UDP port (12201) in Graylog container to receive logs directly
- Converted syslog test script from Bash to Python for better project compatibility
- Implemented Python logging facility with syslog integration for standardized application logging
- Created example Django views demonstrating proper logging usage with different log levels
- Fixed TCP logging by implementing a custom TCP handler for reliable syslog communication
- Created detailed Django implementation plan for the CMS with file management up to 5GB
- Implemented file metadata editing functionality allowing users to update file details post-upload
- Fixed file upload functionality to reliably handle files up to 5GB in size
- Created user-friendly file detail page with download, edit, and delete capabilities
- Integrated file categorization and tagging system for better organization
- Implemented document management system with version tracking and file attachments
- Created document versioning functionality to maintain history of document changes
- Added ability to associate multiple files with documents for better content organization
- Implemented document CRUD operations with proper permission handling
- Set up admin interfaces for document and version management
- Implemented dashboard with system statistics and activity tracking
- Created advanced search functionality with multi-model search and filtering
- Implemented user profile management with profile editing and activity tracking

## Decisions

- Implementing a containerized architecture with four primary services: syslog, PostgreSQL, Nginx, Django app
- Starting with Syslog implementation to enable better debugging during development
- Using syslog-ng with log categorization by service (nginx, django, postgres)
- Implementing a web-based log viewer using Graylog, accessible via Nginx at /logs/
- Configuring log rotation with appropriate retention periods (7-30 days)
- Using Alpine-based images where possible to reduce container size
- Using modern Docker Compose syntax (compose.yaml, docker compose command)
- Using Django with `django-chunked-upload` for handling large files
- Mobile-first design approach with dark mode toggle support
- Local authentication only (no external auth systems)
- OpenAPI client will be generated from provided specification for Phase 2
- Air-gapped deployment targeting Debian environment

## Priorities

1. **Current Focus**: Implement user profile management and reporting features
2. **Next Steps**: Enhance administrative tools for user and content management
3. **Short-term**: 
   - Create syslog-ng configuration with service-specific log files
   - Set up Graylog log viewer with Nginx proxy configuration
   - Complete Docker infrastructure (compose.yaml, Dockerfiles, config files)
   - Implement Django project structure
4. **Medium-term**:
   - Implement large file upload functionality
   - Set up comprehensive testing
   - Document deployment process
5. **Long-term**:
   - Plan and implement Phase 2 (Network Management)
   - Prepare air-gapped deployment package
