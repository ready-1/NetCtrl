# Project Brief

This document defines the mission, objectives, and constraints for the NetCtrl project.

## Mission

NetCtrl is a web application with two development phases:
1. **Phase 1**: A lightweight Content Management System (CMS) with file management capabilities supporting files up to 5GB.
2. **Phase 2**: A network management platform specifically for Netgear M4300 switches via an OpenAPI client.

## Objectives

- Develop a containerized solution using Docker and Docker Compose
- Deploy services in this specific order: syslog, PostgreSQL, Nginx, Django app
- Support 30 user accounts with basic authentication (no RBAC)
- Prioritize simplicity, reliability, and detailed documentation
- Use a monolithic Django architecture
- Implement mobile-first design with dark mode toggle
- Support local authentication only

## Constraints

### Development Environment
- **OS**: macOS (MacBook Pro)
- **Root Directory**: `/Users/bob/dev/NetCtrl`
- **Tools**: Docker, Docker Compose (latest syntax with `docker compose`)

### Deployment Environment
- **OS**: Debian
- **Root Directory**: `/srv/NetCtrl`
- **Environment**: Air-gapped (no internet access after initial setup)

### Technical Constraints
- **Backend**: Django (Python 3.9)
- **Database**: PostgreSQL 14
- **Frontend**: Bootstrap 5.3 (local copy)
- **Web Server**: Gunicorn (inside app container) + Nginx 1.21 (reverse proxy)
- **File Handling**: Django with `django-chunked-upload` for large files
- **Logging**: Syslog-ng (centralized logging)
- **Containerization**: Docker Compose (version 3.8)
