# Active Context

This document tracks the current state, decisions, and priorities for the NetCtrl project.

## Current State

- Project defined with comprehensive requirements for both Phase 1 (CMS) and Phase 2 (Network Management)
- CRCT system initialized with core documentation structure
- Currently in Set-up/Maintenance phase, preparing for transition to Strategy phase
- Project technical stack defined: Django, PostgreSQL, Docker, Nginx, Bootstrap 5.3
- Phase 1 requirements solidified: CMS with file management up to 5GB
- Phase 2 requirements outlined: Network management for Netgear M4300 switches

## Decisions

- Implementing a containerized architecture with four primary services: syslog, PostgreSQL, Nginx, Django app
- Using Django with `django-chunked-upload` for handling large files
- Mobile-first design approach with dark mode toggle support
- Local authentication only (no external auth systems)
- OpenAPI client will be generated from provided specification for Phase 2
- Air-gapped deployment targeting Debian environment

## Priorities

1. **Current Focus**: Complete Set-up/Maintenance phase by updating CRCT documentation and generating dependency trackers
2. **Next Steps**: Transition to Strategy phase and develop detailed implementation plan for Phase 1
3. **Short-term**: 
   - Develop Docker infrastructure (compose.yaml, Dockerfiles, config files)
   - Implement Django project structure
   - Create CMS with Bootstrap 5.3 UI (mobile-first, dark mode)
4. **Medium-term**:
   - Implement large file upload functionality
   - Set up comprehensive testing
   - Document deployment process
5. **Long-term**:
   - Plan and implement Phase 2 (Network Management)
   - Prepare air-gapped deployment package
