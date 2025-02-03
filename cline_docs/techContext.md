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
   - Docker for containerization
   - Docker Compose for orchestration
   - Nginx for reverse proxy
   - Gunicorn for WSGI server

2. Environment Configuration
   - Environment variables
   - Django settings modules
   - Production configurations

3. Monitoring
   - Django logging
   - System metrics
   - Error tracking

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
