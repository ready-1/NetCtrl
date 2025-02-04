# Technical Context

## Development Environment
- Python 3.12
- Django 5.1
- PostgreSQL 15
- Redis (latest)
- Docker & Docker Compose
- Nginx (Alpine)

## Deployment Configuration

### Environment Variables
```bash
# Database
POSTGRES_DB=netctrl
POSTGRES_USER=netctrl
POSTGRES_PASSWORD=[generated]
POSTGRES_HOST=db
POSTGRES_PORT=5432

# Django
DJANGO_SETTINGS_MODULE=config.settings
DJANGO_SECRET_KEY=[generated]
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=[configured]

# Paths
STATIC_ROOT=/opt/static
MEDIA_ROOT=/opt/media
LOG_DIR=/opt/logs
```

### Docker Services
1. Web (Django):
   - Custom Python image
   - Poetry for dependencies
   - Gunicorn with uvicorn workers
   - Volume mounts for static/media

2. Database (PostgreSQL):
   - Version 15 Alpine
   - Persistent volume
   - Health checks
   - Environment from .env

3. Redis:
   - Alpine image
   - Persistent volume
   - Health checks

4. Nginx:
   - Alpine image
   - Reverse proxy
   - Static file serving
   - URL prefix handling

### Authentication
1. Superuser:
   ```python
   Username: admin
   Email: admin@example.com
   Password: FuseFuse123!
   ```

2. Creation:
   - During deployment
   - After migrations
   - Idempotent operation
   - Fixed credentials

### URL Configuration
1. Django:
   ```python
   FORCE_SCRIPT_NAME = '/netctrl'
   STATIC_URL = '/netctrl/static/'
   MEDIA_URL = '/netctrl/media/'
   ```

2. Nginx:
   ```nginx
   location /netctrl/ {
       proxy_pass http://web:8000/;
   }
   ```

## Development Setup
1. Initial Setup:
   ```bash
   ./setup.sh
   # Creates directories
   # Installs dependencies
   # Sets permissions
   ```

2. Deployment:
   ```bash
   ./deploy.sh
   # Updates environment
   # Starts containers
   # Runs migrations
   # Creates superuser
   # Collects static
   ```
