# Changelog

## 2025-03-12
- **Added**: Docker helper script with standardized functions for modern Docker command syntax
- **Updated**: Project documentation and scripts to use "docker compose" instead of "docker-compose"
- **Standardized**: Docker Compose format to follow modern specification (without version key)
- **Fixed**: Docker container DNS resolution issue by simplifying network architecture and using explicit hostname/container_name
- **Fixed**: Docker container logging issues by switching from syslog to JSON file logging
- **Updated**: Docker configuration to operate with direct internet connection while being resilient to temporary outages
- **Removed**: Local PyPI and NPM mirrors as system will be online for installation and updates
- **Fixed**: Frontend Docker build loop issue by removing circular dependency and using official npm registry
- **Improved**: NPM package installation in frontend Dockerfile with multiple fallback options and better timeout settings
- **Fixed**: Frontend container build hanging issue by configuring docker-compose.yml to use host network during build
- **Improved**: Frontend container build process by adding npm retry logic and network timeout settings to prevent hanging
- **Updated**: docker-compose.yml to properly establish service dependencies with health checks
- **Fixed**: Backend container build issue by configuring it to use the public PyPI repository during initial build
- **Added**: Docker environment implementation with Docker Compose, Dockerfiles for all services, and scripts
- **Added**: Comprehensive environment variable management system with templates and validation script
- **Added**: Service configurations for backend (FastAPI), frontend (React with Material UI), NGINX, database, and syslog
- **Added**: Docker_Environment_Setup_Instructions.md in strategy_tasks directory
- **Updated**: activeContext.md to reflect focus on Docker environment setup for MVP1
- **Updated**: progress.md to prioritize Docker environment implementation
- **Added**: Material UI as the CSS framework requirement for the frontend
- **Added**: Initial CRCT system setup with core files and dependency trackers
- **Updated**: .gitignore file to reflect project architecture for CMS with RBAC
