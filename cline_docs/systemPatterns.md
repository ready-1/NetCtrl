# System Patterns

## Architecture Overview

### Container Architecture
1. Web Service (Django)
   - Python 3.12
   - Django 5.1.5
   - Poetry for dependency management
   - Gunicorn with Uvicorn workers
   - Mounted volumes for static/media/logs

2. Database Service (PostgreSQL)
   - PostgreSQL 15
   - Persistent volume storage
   - Health checks
   - Automated initialization
   - Environment-based configuration

3. Cache Service (Redis)
   - Redis Alpine
   - Persistent volume storage
   - Health monitoring
   - Used for Django channels

4. Proxy Service (Nginx)
   - Nginx Alpine
   - SSL/TLS termination
   - Static file serving
   - Load balancing
   - Health checks

### Directory Structure
```
/opt/netctrl/
├── app/              # Application code
├── static/           # Static files
├── media/           # Media files
├── logs/            # Application logs
└── certs/           # SSL certificates
```

### Environment Configuration
1. Database Settings
   - POSTGRES_DB: Database name
   - POSTGRES_USER: Database user
   - POSTGRES_PASSWORD: Auto-generated password
   - POSTGRES_HOST: Container hostname
   - POSTGRES_PORT: Database port

2. Django Settings
   - DJANGO_SETTINGS_MODULE: Config module
   - DJANGO_SECRET_KEY: Auto-generated key
   - DJANGO_DEBUG: Debug mode flag
   - DJANGO_ALLOWED_HOSTS: Host whitelist

3. File Paths
   - STATIC_ROOT: Static file directory
   - MEDIA_ROOT: Media file directory
   - LOG_DIR: Log file directory

### Network Configuration
1. Host Access
   - localhost/127.0.0.1: Local access
   - Docker network IPs: Container access
   - Production domains: External access
   - Wildcard support for development

2. Port Mapping
   - 80: HTTP traffic
   - 443: HTTPS traffic
   - 5432: PostgreSQL (internal)
   - 6379: Redis (internal)

### Security Patterns
1. SSL/TLS
   - Self-signed certificates for development
   - Proper SSL support planned for production
   - Certificate volume mounting

2. Environment Security
   - Auto-generated secure passwords
   - Auto-generated secret keys
   - Environment-based configuration
   - No hardcoded credentials

3. File Permissions
   - Read-only application code
   - Writable logs directory
   - Writable media directory
   - Writable static directory

### Deployment Patterns
1. System Preparation
   - Package updates
   - Docker installation
   - Directory creation
   - Permission setup
   - SSL certificate generation

2. Container Management
   - Container cleanup before deploy
   - Network cleanup
   - Volume preservation
   - Health check verification
   - Dependency ordering

3. Database Management
   - Automatic initialization
   - Migration handling
   - Health monitoring
   - Connection verification

4. Static File Handling
   - Automatic collection
   - Nginx serving
   - Compression
   - Cache control

### Monitoring Patterns
1. Health Checks
   - Database connectivity
   - Redis connectivity
   - Web service status
   - Static file access
   - Regular interval checks

2. Logging
   - Application logs
   - Container logs
   - Nginx access logs
   - Error tracking
   - Structured logging

### Development Patterns
1. Local Development
   - SQLite for development
   - Debug mode support
   - Local static serving
   - Auto-reload capability

2. Production Deployment
   - PostgreSQL database
   - Redis caching
   - Nginx proxy
   - SSL termination
   - Health monitoring
