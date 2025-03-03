# Project Specification: Netgear Switch Management Application

## Overview
This document provides a high-level design specification for a web application to manage Netgear switches (up to 50 on the network). The application leverages Python with Flask for the backend, React for the frontend, and PostgreSQL for persistent data storage, with Redis added for near-realtime SNMP data. It will be deployed on a Debian Bookworm server using Docker containers for modularity and portability. The system must operate in an airgapped environment at times, requiring self-contained dependencies. The UI will be modern and responsive, styled with Bootstrap, and include role-based authentication, a wiki-style CMS, switch management via OpenAPI and SNMP, and worker processes for polling switches.

## Architecture
The application consists of four primary Docker containers, orchestrated with Docker Compose:

1. **Flask App Container**
   - Runs the Flask backend with Python 3.x.
   - Handles API requests, business logic, database interactions, and OpenAPI/SNMP communication.
   - Uses a virtual environment for dependency management.

2. **PostgreSQL Container**
   - Manages persistent data (users, CMS content, switch info).
   - Configured with a persistent volume.

3. **Nginx Container**
   - Reverse proxy for static file serving and API request forwarding.
   - Enhances performance and security.

4. **Redis Container**
   - Stores near-realtime SNMP metrics and traps from switches.
   - Lightweight, in-memory storage with optional persistence.

### Worker Processes
- **Purpose**: Poll up to 50 switches for status and metrics via OpenAPI and SNMP.
- **Implementation**: Celery workers (or similar) running in the Flask container, managed by a task queue.
- **Scaling**: Configurable worker pool (e.g., 5-10 workers) to handle concurrent polling efficiently.

### Deployment
- **Platform**: Debian Bookworm server.
- **Containerization**: Docker and Docker Compose.
- **Airgapped Operation**: All images include dependencies (Python packages, Node.js modules, SNMP libraries) for offline functionality.

## Key Features

### Role-Based Authentication
- **Description**: Secure system with configurable roles (e.g., admin, user) and permissions.
- **Default Superuser**: "admin" with full privileges.
- **Onboarding**: 
  - Airgapped registration with "pending" status; admin approval workflow via UI.

### Wiki-Style Content Management System (CMS)
- **Description**: Create, edit, and view wiki pages.
- **File Handling**: 
  - Large file uploads/downloads stored in a shared volume.
  - Accessible to Flask and Nginx.
- **Media Display**: Inline images/videos using HTML5 or compatible libraries.

### Switch Management
- **Description**: Manage up to 50 switches using OpenAPI and SNMP.
- **OpenAPI Integration**: 
  - Uses an OpenAPI client for the M4300 REST API (v2.0.0.59).
  - Fetches/stores switch data as JSON in PostgreSQL.
- **SNMP Integration**: 
  - Retrieves near-realtime metrics and traps (e.g., port status, traffic).
  - Data stored in Redis with a TTL for freshness.
  - Uses `pysnmp` or similar library.
- **Polling**: 
  - Worker processes poll switches periodically (e.g., every 30s-1min).
  - Balanced across workers to avoid overload (e.g., 10 switches per worker with 5 workers).
- **Dashboard**: 
  - Displays switch status (OpenAPI data from PostgreSQL, SNMP metrics from Redis).
  - Visual elements (tables, charts) updated dynamically.

### User Interface
- **Responsive Design**: 
  - React with Bootstrap 5, collapsible layout for phones/tablets/laptops.
- **Styling**: 
  - Latest Bootstrap and Bootstrap Icons.
- **Dark Mode**: 
  - Toggleable themes using Bootstrap or custom CSS.

## Technical Requirements

### Backend
- **Framework**: Flask (latest stable).
- **Dependencies**: Managed via `requirements.txt` in a virtual environment.
- **Database Interaction**: SQLAlchemy for PostgreSQL; Redis-py for Redis.
- **Authentication**: Flask-JWT-Extended or Flask-Login.
- **Worker Processes**: Celery (with Redis as broker) for polling tasks.
- **SSL Handling**: 
  - Mitigates missing SSL certificate errors with `requests`:
    - Configure a `Session` with `verify=False`.
    - Suppress `urllib3` warnings via `urllib3.disable_warnings(InsecureRequestWarning)`.
  - Temporary solution; full SSL cert management deferred to a future phase.

### Frontend
- **Framework**: React (latest stable).
- **Styling**: Bootstrap 5 with Bootstrap Icons.
- **Build Tools**: Node.js/npm, bundled in Docker.

### Database
- **PostgreSQL**: 
  - Stores users, roles, permissions, CMS content, files metadata, switch JSON data.
- **Redis**: 
  - Stores SNMP metrics/traps (e.g., key-value pairs with switch ID and timestamp).
  - Optional persistence for airgapped recovery.

### Containerization
- **Tools**: Docker and Docker Compose.
- **Configuration**: `.env` files for secrets (e.g., DB credentials, Redis settings).

### Security
- **Practices**: Input validation, secure uploads, error handling.
- **SSL Workaround**: Disabled verification flagged as temporary with clear documentation.
- **Airgapped Focus**: Internal security prioritized.

### Testing
- **Goal**: 100% test coverage.
- **Tools**: 
  - Backend: pytest (unit/integration tests for Flask, workers, SNMP).
  - Frontend: Jest for React.
- **Test Environment**: Live test switch for OpenAPI/SNMP validation.

## Development Environment
- **Backend**: Python virtual environment.
- **Frontend**: Node.js/npm, bundled in Docker.
- **Dependencies**: `requirements.txt` (Python), `package.json` (Node.js), installable offline.

## Deployment
- **Server**: Debian Bookworm.
- **Orchestration**: Docker Compose defines container networking and volumes.
- **File Storage**: Shared volume for CMS uploads.
- **Secrets**: Managed via `.env` files.

## Additional Considerations
- **Airgapped Operation**: 
  - Dependencies pre-installed in images.
  - OpenAPI/SNMP clients cached or mocked if switches are unavailable.
- **Switch Integration**: 
  - OpenAPI: Handles endpoints like `/device_info`, `/sw_portstats`.
  - SNMP: Retrieves OID-based metrics (e.g., ifInOctets, ifOutOctets) and traps.
- **Performance**: 
  - Nginx optimizes static files.
  - Workers distribute polling load.
  - Redis ensures fast SNMP data access.
- **User Experience**: 
  - Collapsible design with Bootstrap.
  - Dark mode preference stored locally or in profiles.

## Conclusion
This updated specification defines a robust application for managing up to 50 Netgear switches in an airgapped environment. It integrates Flask, React, PostgreSQL, Redis, and Docker, with worker processes for polling, a temporary SSL workaround, and SNMP for near-realtime data. The design is scalable and maintainable, with detailed implementations to be refined during development.