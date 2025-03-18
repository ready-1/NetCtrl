# NetCtrl CMS Backend

This is the backend for the NetCtrl Content Management System with Role-Based Access Control.

## Features

- **Authentication**: Username-based JWT authentication system
- **Role-Based Access Control**: Admin, Editor, and User roles with appropriate permissions
- **User Management**: CRUD operations for users with proper permission checks
- **Content Management**: Complete CMS functionality for creating, managing, and publishing content
- **File Management**: File upload, download, and management with content associations
- **Permission System**: Granular permission controls for content and files

## API Documentation

- [Authentication Guide](./AUTHENTICATION_GUIDE.md) - Details on the authentication system
- [User Management Guide](./USER_MANAGEMENT_GUIDE.md) - User CRUD operations and RBAC
- [CMS API Guide](./CMS_API_GUIDE.md) - Content Management API documentation
- [Testing Guide](./CMS_TESTING_GUIDE.md) - Testing the CMS functionality
- [curl Examples](./CURL_API_EXAMPLES.md) - Example API calls with curl

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.11+

### Running the Backend

```bash
# Start all services
docker compose up -d

# Run database migrations
docker compose exec backend alembic upgrade head

# Create initial superuser if needed
docker compose exec backend python -m app.initial_setup
```

### Configuration

Modify the .env files in the env-config/ directory to configure the system. See the env-config/.env.example files for available options.

### Testing

```bash
# Run the test suite
docker compose -f docker-compose.test.yml run --rm test_backend pytest
```

## Endpoints

Main API endpoints:

- **Authentication**: `/api/v1/jwt/login`, `/api/v1/users/me`
- **User Management**: `/api/v1/users/`, `/api/v1/roles/`
- **Content Management**: `/api/v1/content/`
- **File Management**: `/api/v1/files/`
