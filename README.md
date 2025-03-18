# NetCtrl: CMS with RBAC

A Content Management System with Role-Based Access Control (RBAC) deployed using Docker containers.

## Features

- **User Authentication**: Username-based JWT authentication system
- **Role-Based Access Control**: Admin, Editor, and User roles with granular permissions
- **Content Management**: Create, read, update, and delete content with versioning
- **File Management**: Upload, download, and manage files with content associations
- **Permission System**: Fine-grained permission controls for content and files

## Backend Implementation

The system uses a FastAPI backend with the following components:

- **Authentication System**: Custom JWT implementation with username-based login
- **User Management**: Complete CRUD operations with role-based permissions
- **Content API**: RESTful API for content management with filtering and search
- **File API**: File upload, download, and management API
- **Testing Framework**: Comprehensive test suite for all functionality

Documentation for the backend APIs can be found in the `src/backend/` directory:
- [CMS API Guide](src/backend/CMS_API_GUIDE.md)
- [Authentication Guide](src/backend/AUTHENTICATION_GUIDE.md)
- [User Management Guide](src/backend/USER_MANAGEMENT_GUIDE.md)

## Docker Environment Setup

This project uses Docker Compose to orchestrate containers for the following services:
- FastAPI Backend
- Postgres Database
- React Frontend with Material UI
- NGINX Reverse Proxy
- Syslog for Centralized Logging
- Local Package Repositories for Air-gapped Operation

## Environment Variables

Environment variables are managed through a structured system:

```
env-config/
├── .env.example            # Master template with all variables
├── .env                    # Local development variables (gitignored)
├── services/
│   ├── backend/            # FastAPI-specific variables
│   ├── database/           # Postgres-specific variables
│   ├── frontend/           # React-specific variables
│   ├── nginx/              # NGINX-specific variables
│   └── syslog/             # Syslog-specific variables
└── scripts/
    └── validate-env.sh     # Script to verify all required env vars
    └── init-env.sh         # Script to initialize .env files from templates
```

## Getting Started

1. Initialize environment variables:
   ```bash
   chmod +x env-config/scripts/init-env.sh
   ./env-config/scripts/init-env.sh
   ```

2. Edit the generated `.env` files with your specific configuration values.

3. Validate environment variables:
   ```bash
   cd env-config/scripts
   ./validate-env.sh
   ```

4. Start the containers:
   ```bash
   docker compose up -d
   ```

5. Access the application at http://localhost

## Air-gapped Operation

This project is designed to work in air-gapped environments with no internet access:

- Local PyPI mirror (devpi) for Python dependencies
- Local NPM registry (verdaccio) for JavaScript dependencies
- All Material UI components served locally
- No CDN dependencies

## Development

For development you can use the following commands:

- Start individual services:
  ```bash
  docker compose up backend database -d
  ```

- View logs:
  ```bash
  docker compose logs -f
  ```

- Access specific container:
  ```bash
  docker compose exec backend bash
  ```

- Run the test suite:
  ```bash
  docker compose -f docker-compose.test.yml run --rm test_backend pytest
  ```

## Configuration

See the `.env.example` file for all available configuration options.
