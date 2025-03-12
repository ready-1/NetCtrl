# Project Brief: 

**Project Name: CMS with RBAC**

**Project Goal: Create a working CMS with Role-Based Access Control (RBAC).**

**Core Requirements:**
We are developing a Content Management System (CMS) with Role-Based Access Control (RBAC), deployed using Docker containers. The project will utilize the following technology stack:

- **Backend**: FastAPI with FastAPI Users for authentication and API development.
- **Database**: Postgres for persistent storage.
- **Reverse Proxy/Static File Server**: NGINX to handle routing and serve static assets.
- **Frontend**: React with Material UI for UI components and a responsive, mobile-first design.
- **Logging**: A syslog container for centralized logging.
- **Air-Gapped Operation**: The system must function in environments without internet access.

The project will be delivered in four Minimum Viable Product (MVP) phases:

1. **MVP1**: A working Docker environment with a simple login screen and registration process.
2. **MVP2**: A fully functional CMS API with support for large file uploads (up to 2GB binary files).
3. **MVP3**: A fully functional CMS front end.
4. **MVP4**: A static page for GitHub issue creation and submission.

## Objectives
- Build a CMS that enables users to manage content based on their roles.
- Implement secure authentication and RBAC to control access to CMS features.
- Ensure seamless deployment using Docker containers.
- Deliver a responsive, user-friendly interface optimized for mobile devices using Material UI.
- Support the upload and management of large binary files (up to 2GB) within the CMS.
- Provide a static page for authenticated users to create and submit GitHub issues.
- Support operation in air-gapped environments with no external internet access.

## Scope

### Included
- **Dockerized Environment**: Containers for backend, database, NGINX, syslog, and frontend.
- **Backend**: FastAPI-based API with endpoints for authentication, CMS functionality, and user management.
- **Database**: Postgres schema with tables for users, roles, and content.
- **Deployment Initialization**: Automatic creation of a superuser account and default roles (superuser, admin, editor, viewer) on deployment.
- **RBAC**: Role-based access control to restrict CMS features based on user roles.
- **User Registration**: Process including:
  - An "approved" flag (boolean, default `false`), set to `true` by an admin to enable the account.
  - An "inactive" flag (boolean, default `false`), toggled by an admin for security concerns, vacations, etc.
- **Authentication Logic**: Login checks for valid credentials, "approved" = `true`, and "inactive" = `false`.
- **API Endpoints**:
  - User registration and login.
  - User management for admins to approve users and toggle the "inactive" flag.
  - CMS content management (CRUD operations).
  - GitHub issue creation.
- **Frontend**:
  - Material UI components for consistent, responsive design.
  - Login and registration screens (MVP1).
  - CMS interfaces for content management (MVP3).
  - User management interfaces for admins (MVP3).
  - Static page for GitHub issue submission (MVP4).
- **NGINX**: Configured for large file uploads (up to 2GB).
- **File Storage**: Local storage for uploaded files (up to 2GB, no type validation).
- **API Documentation**: OpenAPI YAML specification (OpenAPI 3.1.0 compliant) for the backend API.
- **Fully Local Resources**: All dependencies, frameworks, and libraries must be served locally to support air-gapped environments.
- **Testing Strategy**:
  - Unit, integration, end-to-end, and security testing.
  - User Acceptance Testing (UAT).
- **Documentation**: Deployment instructions, API reference, user guides, and developer documentation.
- **Error Handling**: Clear error messages (e.g., "Account not approved," "Account is inactive").

### Excluded
- Advanced CMS features (e.g., content versioning).
- Scalability measures (e.g., caching, rate limiting).
- File type validation for uploads.
- Internationalization (i18n).
- Backup and disaster recovery (handled at the server level).
- CDN integration or external API dependencies.

## Deliverables
- **Source Code**: Backend (FastAPI), frontend (React with Material UI), and database schema.
- **Docker Compose Files**: For deployment, including syslog.
- **NGINX Configuration**: For reverse proxy and large file uploads.
- **OpenAPI YAML**: Updated with authentication, user management, CMS, and GitHub issue endpoints.
- **Vendor Packages**: All required libraries and frameworks packaged for local deployment.
- **Documentation**:
  - Deployment instructions.
  - API reference.
  - User guides (including admin instructions for user management).
  - Developer documentation.
  - Air-gapped deployment guide.

## Timeline
- **MVP1: Working Docker Environment with Login, Registration, and Basic User Management API (Weeks 1-2)**:
  - Set up Docker containers (backend, Postgres, NGINX, syslog).
  - Implement FastAPI backend with:
    - `/auth/register`: Creates user with "approved" = `false`, "inactive" = `false`.
    - `/auth/login`: Verifies credentials, "approved" = `true`, "inactive" = `false`.
    - Basic user management endpoints (e.g., `/users`, `/users/{user_id}`) for superuser to list users and update "approved" flag.
  - Develop React login and registration screens with Material UI components.
  - Create initial OpenAPI YAML for authentication and user management.
  - Configure project for offline/air-gapped operation.
  - Test deployment and authentication logic.

- **MVP2: Fully Functional CMS API (Weeks 3-4)**:
  - Implement CMS API endpoints for content management (CRUD).
  - Enhance user management endpoints for admins to update "approved" and "inactive" flags.
  - Configure NGINX and FastAPI for 2GB file uploads.
  - Update OpenAPI YAML with CMS and enhanced user management endpoints.
  - Conduct testing (unit, integration, security).

- **MVP3: Fully Functional CMS Front End (Weeks 5-6)**:
  - Develop React interfaces with Material UI for:
    - Content management (list, create, edit, delete).
    - User management (admin ability to approve users and toggle "inactive" flag).
  - Integrate frontend with backend API.
  - Perform end-to-end testing and UAT.

- **MVP4: Static Page for GitHub Issue Submission (Weeks 7-8)**:
  - Implement backend endpoint (e.g., `/issues`) to create GitHub issues using a secure token.
  - Develop frontend page with Material UI for authenticated users to submit issues via the backend endpoint.
  - Test and refine functionality.

**Total Duration**: 8 weeks.

## Assumptions
- Low-volume use case; scalability not prioritized.
- Local file storage sufficient for 2GB uploads.
- No caching or rate limiting required.
- GitHub issue submission restricted to authenticated users.
- Superuser uses API directly (e.g., Postman) for approvals in MVP1 until MVP3 provides a frontend.
- Air-gapped deployment will require all dependencies to be pre-packaged.

## Constraints
- Tech stack: Postgres, FastAPI with FastAPI Users, NGINX, React with Material UI, Docker.
- Responsive, mobile-first frontend design using Material UI components.
- Automatic creation of superuser and default roles on deployment.
- Air-gapped operation with no external network dependencies.
- All frameworks and dependencies must be served locally.

## Risks and Mitigations
- **Risk**: Incorrect implementation of "approved" and "inactive" flags in login logic.
  - **Mitigation**: Test login with various user states (approved/not approved, active/inactive).
- **Risk**: Large file upload performance issues.
  - **Mitigation**: Use streaming, configure NGINX appropriately, test with 2GB files.
- **Risk**: Security flaws in authentication or user management.
  - **Mitigation**: Apply best practices (JWT validation, role checks) and security testing.
- **Risk**: Air-gapped environment missing critical dependencies.
  - **Mitigation**: Comprehensive dependency bundling, offline package repository, and thorough testing in a simulated air-gapped environment.
- **Risk**: Updates to Material UI or other libraries might be difficult in air-gapped environments.
  - **Mitigation**: Document the process for safely updating libraries in air-gapped environments.

## Team and Resources
- **Backend Developer**: Python, FastAPI, SQLAlchemy expertise.
- **Frontend Developer**: React, Material UI, JavaScript, responsive design skills.
- **DevOps Engineer**: Docker, NGINX, deployment knowledge, air-gapped operations experience.
- **Tools**: Git, pytest (backend), Jest (frontend).

## Testing Strategy
- **Unit Testing**: Backend and frontend components.
- **Integration Testing**: API, database, frontend interactions.
- **End-to-End Testing**: Key workflows (login, content creation, issue submission).
- **Security Testing**: Verify RBAC, authentication (including "approved"/"inactive" checks), and file uploads.
- **Air-Gapped Testing**: Verify system works correctly with no external network access.
- **UAT**: Stakeholder validation of functionality.

## Documentation
- **Deployment Instructions**: Docker setup guide, including air-gapped deployment procedures.
- **API Reference**: From OpenAPI YAML.
- **User Guides**: CMS usage, admin user management, GitHub issue submission.
- **Developer Documentation**: For maintenance and extension, including offline development guidance.

## User Acceptance Testing (UAT)
- Define acceptance criteria per MVP.
- Engage stakeholders for testing and feedback.

## Error Handling and User Feedback
- Clear error messages (e.g., "Account not approved" for "approved" = `false`, "Account is inactive" for "inactive" = `true`).
- Feedback via GitHub issue submission page.

**Source of Truth:** This document serves as the source of truth for the project's scope, core requirements, and overall vision. All other documentation and development efforts should align with the principles and goals outlined here.
