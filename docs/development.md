# NetCtrl Development Guide

## Development Environment Setup

### Prerequisites

1. **Python 3.12+**
   - Download from [python.org](https://www.python.org/downloads/)
   - Verify installation: `python --version`

2. **Poetry**
   - Install: `curl -sSL https://install.python-poetry.org | python3 -`
   - Verify installation: `poetry --version`

3. **Docker and Docker Compose**
   - Install Docker Desktop from [docker.com](https://www.docker.com/products/docker-desktop)
   - Verify installation:
     ```bash
     docker --version
     docker compose version
     ```

### Initial Setup

1. **Clone Repository**
   ```bash
   git clone <repository-url>
   cd netctrl
   ```

2. **Install Dependencies**
   ```bash
   poetry install
   ```

3. **Start Development Environment**
   ```bash
   docker compose up -d
   ```

4. **Database Setup**
   ```bash
   # Create database
   docker compose exec db psql -U postgres -c "CREATE DATABASE netctrl;"

   # Apply migrations
   docker compose exec web python manage.py migrate

   # Create superuser
   docker compose exec web python manage.py createsuperuser
   ```

5. **Collect Static Files**
   ```bash
   docker compose exec web python manage.py collectstatic --noinput
   ```

### Development Workflow

1. **Running Tests**
   ```bash
   poetry run pytest
   ```

2. **Code Formatting**
   ```bash
   poetry run black .
   ```

3. **Linting**
   ```bash
   poetry run flake8
   ```

4. **Database Management**
   - Access Adminer: http://localhost:8080
   - Credentials:
     - System: PostgreSQL
     - Server: db
     - Username: postgres
     - Password: postgres
     - Database: netctrl

### Development URLs

- Django Admin: http://localhost:8000/admin
- API Documentation: http://localhost:8000/api/docs/
- Database Admin: http://localhost:8080

### Common Tasks

1. **Creating Database Migrations**
   ```bash
   docker compose exec web python manage.py makemigrations
   ```

2. **Applying Migrations**
   ```bash
   docker compose exec web python manage.py migrate
   ```

3. **Creating a Superuser**
   ```bash
   docker compose exec web python manage.py createsuperuser
   ```

4. **Viewing Logs**
   ```bash
   docker compose logs -f web
   ```

### Best Practices

1. **Code Style**
   - Follow PEP 8 guidelines
   - Use type hints
   - Write docstrings for all public functions and classes
   - Keep functions small and focused
   - Use meaningful variable names

2. **Testing**
   - Write tests for all new features
   - Maintain minimum 80% test coverage
   - Test both success and failure cases
   - Use pytest fixtures for common test setup

3. **Git Workflow**
   - Create feature branches from `main`
   - Keep commits small and focused
   - Write clear commit messages
   - Update documentation as needed

4. **Security**
   - Never commit sensitive data
   - Use environment variables for secrets
   - Validate all user input
   - Follow security best practices

### Troubleshooting

1. **Database Connection Issues**
   - Verify PostgreSQL container is running
   - Check database credentials
   - Ensure migrations are applied

2. **Static Files Not Loading**
   - Run `collectstatic`
   - Check STATIC_ROOT and STATIC_URL settings
   - Verify file permissions

3. **Docker Issues**
   - Check container logs
   - Verify port mappings
   - Ensure all services are healthy
