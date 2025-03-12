# Progress:

## What's Left to Build:

### MVP1: Working Docker Environment with Login, Registration, and Basic User Management API
- [ ] Docker environment setup (backend, Postgres, NGINX, syslog)
- [ ] Offline package repository for air-gapped operation
- [ ] FastAPI backend with authentication endpoints
- [ ] User registration and login functionality
- [ ] Basic RBAC implementation
- [ ] Initial React login/registration screens with Material UI

### MVP2: Fully Functional CMS API
- [ ] CMS API endpoints for content management
- [ ] Enhanced user management 
- [ ] NGINX configuration for large file uploads
- [ ] OpenAPI documentation updates
- [ ] Local serving of all API documentation

### MVP3: Fully Functional CMS Front End
- [ ] React interface with Material UI components for content management
- [ ] User management interface
- [ ] Frontend-backend integration
- [ ] All frontend dependencies bundled for offline use

### MVP4: Static Page for GitHub Issue Submission
- [ ] GitHub issue creation API
- [ ] Frontend page for issue submission with Material UI
- [ ] Offline issue queue for air-gapped environments

## Immediate Priorities:
1. Complete CRCT system initialization
2. Set up dependency tracking structure
3. Prepare Docker environment architecture for air-gapped operation
4. Design database schema for users and roles
5. Plan approach for bundling Material UI and all dependencies locally

## Known Issues:
- Need to determine best approach for handling 2GB file uploads in air-gapped environments
- RBAC implementation details with FastAPI Users to be finalized
- Strategy for updating dependencies in air-gapped environments needs to be established
- Material UI component bundling for offline use needs research
- GitHub issue submission workflow in air-gapped environments requires special consideration
