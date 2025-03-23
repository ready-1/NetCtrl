# Changelog

This document tracks significant changes to the NetCtrl CMS with RBAC system.

## 2025-03-19: Fixed Docker Container and Database Issues

### NGINX Configuration and Frontend Access
- Fixed NGINX configuration to properly handle frontend routes with `/app/` prefix
- Implemented proper URL structure with status page accessible via `/status`
- Added direct static endpoints for testing and debugging (`/frontendtest`, `/app/test`)
- Fixed route prioritization using NGINX location block modifiers (`=`, `^~`)

### Database Initialization and Retry Logic
- Documented database initialization retry logic in DATABASE_TROUBLESHOOTING.md
- Identified that "relation 'user' does not exist" errors during startup are transient and handled by retry logic
- Confirmed superuser creation works after migrations complete

### Documentation
- Created comprehensive troubleshooting guide in DATABASE_TROUBLESHOOTING.md
- Added detailed instructions for NGINX configuration and debugging
- Documented the system access URLs and structure
- Added schema reference for main database tables

## 2025-03-18: Implemented CMS Frontend Components

### Content Management UI
- Added content list view with filtering, sorting, search, and role-based access control for viewing/editing/deleting
- Created rich text editor for content creation and editing using React-Quill with proper sanitization
- Implemented detailed content view with metadata display and HTML/Markdown rendering
- Added responsive design with both desktop and mobile layouts for all components

### Frontend Architecture
- Created React Query hooks for efficient data fetching, caching, and state management
- Implemented component structure following Material UI best practices
- Added type definitions for content and related entities

## 2025-03-17: Fixed Critical Docker Container Issues

### Backend Permissions
- Removed chmod operations when running as non-root user
- Fixed frontend dependency issues by explicitly installing missing ajv module
- Fixed Alembic migration chain problems
- Aligned database configuration across the application

## 2025-03-16: Created Frontend Implementation Plan

### Component Architecture
- Designed detailed component architecture for CMS using React and Material UI
- Created technical considerations document
- Defined implementation phases for frontend development

## 2025-03-15: Implemented CMS Backend Testing Framework

### Test Infrastructure
- Created async-aware fixtures
- Implemented proper test isolation
- Added complete test coverage for all planned CMS functionality
- Documented testing approach in CMS_TESTING_GUIDE.md

## 2025-03-14: Enhanced API Documentation

### API Examples and Testing
- Created CURL_API_EXAMPLES.md with detailed API examples
- Added comprehensive test_user_management.py with tests for login and RBAC
- Updated OpenAPI specification with detailed descriptions

## 2025-03-13: Implemented User CRUD Operations with RBAC

### Authentication System
- Added password complexity validation
- Implemented role-based permissions
- Added comprehensive test suite
- Fixed authentication system by implementing custom JWT strategy with proper username-based login
- Made email field optional in user schemas to support username-only authentication

## 2025-03-12: System Initialization

### Project Setup
- Initialized CRCT system
- Created core files for CMS with RBAC project
- Set up dependency trackers
- Updated .gitignore to reflect project architecture
- Added requirements for air-gapped operation

### Docker Environment
- Implemented Docker environment structure with docker-compose.yml
- Created comprehensive environment variable management system
- Configured NGINX for reverse proxy and handling large file uploads
- Established centralized logging with syslog container
