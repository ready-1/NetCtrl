# NetCtrl CMS Backend

Backend API for the NetCtrl CMS with Role-Based Access Control.

## Features

- FastAPI-based RESTful API
- JWT Authentication with username/password
- Role-Based Access Control (Admin, Manager, User)
- PostgreSQL database
- Comprehensive testing suite
- Docker support

## Development Setup

### Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

3. Access the API documentation:
   - OpenAPI UI: http://localhost:8000/api/v1/docs
   - ReDoc: http://localhost:8000/api/v1/redoc

### Running Tests

#### Option 1: Run with SQLite (Quick Tests)

```bash
cd src/backend
python -m pytest app/tests/
```

#### Option 2: Run with PostgreSQL (Production-like Tests)

```bash
cd src/backend
chmod +x run_tests_with_postgres.sh
./run_tests_with_postgres.sh
```

#### Option 3: Run with Docker Compose

```bash
cd src/backend
docker compose -f docker-compose.test.yml up --build
```

## API Endpoints

### Authentication

- `POST /api/v1/jwt/login` - Login and get JWT token
- `POST /api/v1/register` - Register a new user
- `GET /api/v1/users/me` - Get current user profile

### User Management

- `GET /api/v1/users` - List all users (admin/manager)
- `GET /api/v1/users/{id}` - Get user by ID
- `POST /api/v1/users` - Create a new user (admin only)
- `PATCH /api/v1/users/{id}` - Update a user
- `DELETE /api/v1/users/{id}` - Delete a user (admin only)

### Roles

- `GET /api/v1/roles` - List all available roles
- `GET /api/v1/roles/{role}/users` - List users with a specific role (admin only)

## Environment Variables

- `SECRET_KEY` - Secret key for JWT token generation
- `POSTGRES_SERVER` - PostgreSQL server hostname
- `POSTGRES_USER` - PostgreSQL username
- `POSTGRES_PASSWORD` - PostgreSQL password
- `POSTGRES_DB` - PostgreSQL database name
- `FIRST_SUPERUSER_USERNAME` - Initial admin username (default: admin)
- `FIRST_SUPERUSER_PASSWORD` - Initial admin password

## Docker Deployment

The application is designed to run in a Docker container and is configured to work with the project's Docker Compose setup.

```bash
# Start the entire application stack
docker compose up -d
