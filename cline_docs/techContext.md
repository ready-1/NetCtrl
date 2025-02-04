# Technical Context

## Development Environment
1. Package Management
   - Poetry for dependency management
   - pyproject.toml for project configuration
   - poetry.lock for dependency locking

2. Python Environment
   - Python 3.12+
   - Virtual environment managed by Poetry
   - Development packages installed via poetry install

3. Development Tools
   - VSCode as primary IDE
   - Black for code formatting
   - Flake8 for linting
   - Pre-commit hooks for code quality

## Technologies Used
1. Backend
   - Django 5.0+
   - Django REST Framework
   - Django Channels
   - PostgreSQL/SQLite
   - Redis (for caching/async)

2. Frontend
   - Bootstrap 5 (locally served)
   - Chart.js for metrics
   - HTMX for dynamic updates
   - Font Awesome icons

3. Testing
   - Pytest for testing framework
   - Factory Boy for test data
   - Coverage.py for test coverage
   - Django test client

## Technical Constraints
1. Airgapped Environment
   - No internet connectivity
   - All assets must be served locally
   - No CDN dependencies
   - Self-contained deployment

2. Browser Support
   - Chrome-based browsers
   - Safari
   - Mobile browsers (iOS Safari, Android Chrome)
   - Minimum resolution: iPhone viewport

3. Network Constraints
   - HTTP access to switches on port 49151
   - In-band and out-band management
   - Local network connectivity only

## Development Setup
1. Local Development
   ```bash
   # Clone repository
   git clone [repository]
   cd NetCtrl

   # Install dependencies
   poetry install

   # Run migrations
   poetry run python manage.py migrate

   # Start development server
   poetry run python manage.py runserver
   ```

2. Database
   - Development: SQLite
   - Production: PostgreSQL
   - Migrations managed by Django

3. Asset Management
   - Static files in static/
   - Media files in media/
   - Whitenoise for static serving

## Deployment
1. Container Setup
   - Docker Engine 24.0+ with Compose V2:
     * Web application (Django + Gunicorn)
     * PostgreSQL 15 database
     * Redis Alpine for caching/async
     * Nginx Alpine reverse proxy
   - Docker Compose orchestration
   - Self-signed SSL certificates
   - Volume management for persistence

2. Environment Configuration
   - Automated setup script (setup.sh)
   - Deployment script (deploy.sh)
   - Environment variables via .env
   - Docker-based configuration

3. System Requirements
   - Debian 11+ or Ubuntu 22.04+
   - Docker Engine 24.0+ with Compose V2
   - 2GB RAM minimum
   - 20GB disk space recommended
   - Git (latest version)

4. Monitoring & Health
   - Container health checks
   - Nginx status monitoring
   - Database connection monitoring
   - Application error logging

## Security Requirements
1. Authentication
   - Role-based access
   - JWT for API authentication
   - Session-based web auth

2. Network Security
   - CSRF protection
   - XSS prevention
   - SQL injection protection

3. Data Protection
   - Encrypted credentials
   - Secure configuration storage
   - Audit logging
