# Changelog

## March 16, 2025 - Fixed Authentication System

- Implemented custom JWT strategy for proper authentication:
  - Created a custom JWT strategy implementation to handle token generation and validation
  - Fixed type conversion between database integers and JWT string IDs
  - Added proper error handling for authentication flows
  - Made email field optional in user schemas to support username-only authentication
  - Updated authentication documentation with comprehensive examples
  - Added tested curl examples for all authentication endpoints
  - Fixed token processing in read_token and write_token functions

- Technical improvements:
  - Consolidated authentication documentation into a single comprehensive guide
  - Added explicit type conversions to prevent database query errors
  - Improved error logging during authentication flows
  - Enhanced authentication route with better exception handling
  - Verified the complete authentication flow with proper testing

## March 16, 2025 - Authentication System Aggressive Optimization

- Ruthlessly simplified and optimized authentication system:
  - Removed all custom authentication implementations in favor of the standard FastAPI-Users library
  - Deleted 10+ redundant debugging scripts and consolidated into a single auth_diagnostics.py tool
  - Streamlined auth-related utilities with proper error handling and logging
  - Optimized database queries using SQL text() for better performance
  - Simplified NGINX configuration by removing all special case handling
  - Eliminated code duplication and redundant documentation

- Technical improvements:
  - Replaced print statements with proper logging
  - Optimized SQL queries for better performance
  - Added more efficient error handling
  - Reduced script file sizes by up to 60%
  - Cleaned up API endpoint routing

## March 16, 2025 - Authentication System Refactoring

- Simplified authentication system by removing duplicate router registrations:
  - Eliminated custom_auth router to prevent route conflicts
  - Standardized on FastAPI-Users implementation as single source of truth
  - Removed custom_auth import from main.py

- Streamlined NGINX configuration:
  - Removed special case handling for login endpoint
  - Eliminated request mirroring and debug-specific configuration
  - Unified API request handling for more consistent behavior

- Consolidated authentication tooling and documentation:
  - Created comprehensive AUTHENTICATION_GUIDE.md that covers all scenarios
  - Developed unified auth_diagnostics.py tool that replaces multiple specialized scripts
  - Made auth_diagnostics.py executable

- The new authentication system is more maintainable follows standard patterns and eliminates potential conflicts that were causing login issues

## March 12, 2025 - Fixed Database Migration and Import Errors

- Updated FastAPI-Users import path
- Fixed duplicate enum creation
- Configured Alembic properly
- Resolved table name mismatch
- Added missing columns to migrations
- Fixed superuser creation with proper Pydantic model

## March 11, 2025 - Implemented FastAPI Backend

- Implemented role-based authentication system
- Created comprehensive test suite
- Created comprehensive authentication implementation plan for FastAPI backend with RBAC

## March 10, 2025 - Docker Modernization

- Standardized on "docker compose" command syntax (without hyphen) for all operations
- Updated project to use modern Docker Compose standards (removing deprecated "version" key)
- Updated Docker configuration to operate with direct internet connection while being resilient to temporary outages
- Removed local PyPI and NPM mirrors as system will be online for installation and updates

## March 9, 2025 - Docker Configuration Fixes

- Fixed Docker container DNS resolution issue by simplifying network architecture and using explicit hostname/container_name
- Fixed Docker container logging issues by switching from syslog to JSON file logging
- Fixed Docker frontend container build hanging issue by configuring docker-compose.yml to use host network during build
- Improved Docker frontend build by adding npm retry logic and network timeout settings to prevent hanging
- Updated docker-compose.yml to properly establish service dependencies with health checks
- Fixed Docker backend container build issue by configuring it to use the public PyPI repository during initial build

## March 8, 2025 - Project Initialization

- Initialized CRCT system
- Created core files for CMS with RBAC project
- Set up main dependency tracker (cline_docs/dependency_tracker.md) and doc tracker (docs/doc_tracker.md)
- Generated embeddings for dependency trackers
- Updated .gitignore to properly reflect the CMS with RBAC project architecture
- Refined .gitignore to specifically exclude the python directory with 30k+ virtual environment files
- Added requirements for air-gapped operation (all dependencies to be served locally)
- Added Material UI as the CSS framework for the frontend
- Created strategy for Docker environment setup with environment variable management (first step for MVP1)
- Identified need for comprehensive env file structure to support air-gapped operation
