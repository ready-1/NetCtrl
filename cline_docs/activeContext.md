# Active Context

This document tracks the current state, decisions, and priorities for the NetCtrl project.

## Current State

- Project defined with comprehensive requirements for both Phase 1 (CMS) and Phase 2 (Network Management)
- CRCT system initialized with core documentation structure
- Currently in Strategy phase, with detailed implementation instructions created
- Project technical stack defined: Django, PostgreSQL, Docker, Nginx, Bootstrap 5.3
- Phase 1 requirements solidified: CMS with file management up to 5GB
- Phase 2 requirements outlined: Network management for Netgear M4300 switches
- Docker infrastructure details finalized, with focus on Syslog implementation first

## Decisions

- Implementing a containerized architecture with four primary services: syslog, PostgreSQL, Nginx, Django app
- Starting with Syslog implementation to enable better debugging during development
- Using syslog-ng with log categorization by service (nginx, django, postgres)
- Implementing a web-based log viewer using Dozzle, accessible via Nginx at /logs/
- Configuring log rotation with appropriate retention periods (7-30 days)
- Using Alpine-based images where possible to reduce container size
- Using modern Docker Compose syntax (compose.yaml, docker compose command)
- Using Django with `django-chunked-upload` for handling large files
- Mobile-first design approach with dark mode toggle support
- Local authentication only (no external auth systems)
- OpenAPI client will be generated from provided specification for Phase 2
- Air-gapped deployment targeting Debian environment

## Priorities

1. **Current Focus**: Implement Syslog server with log categorization and viewer
2. **Next Steps**: Complete remaining Docker infrastructure and begin Django implementation
3. **Short-term**: 
   - Create syslog-ng configuration with service-specific log files
   - Set up Dozzle log viewer with Nginx proxy configuration
   - Complete Docker infrastructure (compose.yaml, Dockerfiles, config files)
   - Implement Django project structure
4. **Medium-term**:
   - Implement large file upload functionality
   - Set up comprehensive testing
   - Document deployment process
5. **Long-term**:
   - Plan and implement Phase 2 (Network Management)
   - Prepare air-gapped deployment package
