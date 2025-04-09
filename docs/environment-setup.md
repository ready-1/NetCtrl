# Environment Configuration Guide

## Overview

NetCtrl uses environment variables for all configuration, especially for sensitive information like API keys and database credentials. This approach:

- Keeps secrets out of version control
- Enables different configurations for development, testing, and production
- Follows security best practices

## Quick Start

1. **Set up the development environment**:
   ```bash
   # Run the automated setup script
   python scripts/setup_env.py
   
   # Activate the virtual environment
   source python/bin/activate  # Linux/macOS
   # OR
   .\python\Scripts\activate   # Windows
   ```

   The setup script will:
   - Create or validate the Python virtual environment
   - Install all required dependencies
   - Verify your environment configuration

2. **Create your environment file** (if it doesn't exist):
   ```bash
   cp .env.example .env
   ```

3. **Generate a secure Django secret key**:
   ```bash
   python -c "from django.core.management.utils.get_random_secret_key import get_random_secret_key; print(get_random_secret_key())"
   ```

4. **Edit your `.env` file** with the generated key and other required values.

5. **Verify your environment**:
   ```bash
   python scripts/verify_env.py
   ```

## Security Best Practices

- **Never commit `.env` to version control**
- Keep different environment files for development, staging, and production
- Rotate secrets periodically (especially API tokens)
- Use strong, randomly generated values
- Limit access to production environment variables
- Validate critical environment variables at startup

## Environment Variables Reference

| Variable | Description | Default | Required | Example |
|----------|-------------|---------|----------|---------|
| **Core Django Settings** |
| `DJANGO_SECRET_KEY` | Django encryption key | Auto-generated (insecure) | ✅ Production | `j8e3fk*87p_mv=#dc2tf(r7y4!x6g5j=u8=3cjs5pt4l0!81h+` |
| `DJANGO_DEBUG` | Debug mode | `True` | ❌ | `False` |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated list of allowed hosts | `localhost,127.0.0.1` | ❌ | `mysite.com,www.mysite.com` |
| `ENVIRONMENT` | Environment type | `development` | ❌ | `production` |
| **Database Configuration** |
| `USE_POSTGRES` | Use PostgreSQL instead of SQLite | `False` | ❌ | `True` |
| `POSTGRES_DB` | PostgreSQL database name | `netctrl_db` | ✅ if using PostgreSQL | `netctrl_production` |
| `POSTGRES_USER` | PostgreSQL username | `netctrl_user` | ✅ if using PostgreSQL | `netctrl_prod_user` |
| `POSTGRES_PASSWORD` | PostgreSQL password | `netctrl_password` | ✅ if using PostgreSQL | `highly-secure-password` |
| `POSTGRES_HOST` | PostgreSQL host | `postgres` | ✅ if using PostgreSQL | `db.example.com` |
| `POSTGRES_PORT` | PostgreSQL port | `5432` | ✅ if using PostgreSQL | `5432` |
| **GitHub Integration** |
| `GITHUB_TOKEN` | GitHub Personal Access Token | None | ✅ for GitHub features | `github_pat_123456abcdef...` |
| `GITHUB_REPOSITORY` | GitHub repository name | `ready-1/NetCtrl` | ❌ | `myorg/myproject` |
| **Logging Configuration** |
| `LOG_LEVEL` | Log level | `INFO` | ❌ | `WARNING` |
| `SYSLOG_HOST` | Syslog server host | None | ❌ | `logs.example.com` |
| `SYSLOG_PORT` | Syslog server port | `5140` | ❌ | `514` |
| **File Storage** |
| `MEDIA_ROOT` | Media storage path | `BASE_DIR/media` | ❌ | `/var/www/media` |
| `STATIC_ROOT` | Static files path | `BASE_DIR/staticfiles` | ❌ | `/var/www/static` |

## Setup by Environment

### Development Environment

For local development, the defaults are usually sufficient:

```
DJANGO_SECRET_KEY=your-dev-key-here
DJANGO_DEBUG=True
ENVIRONMENT=development
# GitHub token for issue tracking (if needed)
GITHUB_TOKEN=your-github-token
```

### Testing Environment

Testing should mimic production config but with settings that allow for testing:

```
DJANGO_SECRET_KEY=your-test-key-here
DJANGO_DEBUG=False
ENVIRONMENT=testing
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,testserver
# Use SQLite for tests by default
USE_POSTGRES=False
```

### Production Environment

Production must use secure settings:

```
DJANGO_SECRET_KEY=your-very-secure-production-key
DJANGO_DEBUG=False
ENVIRONMENT=production
DJANGO_ALLOWED_HOSTS=yoursite.com,www.yoursite.com
USE_POSTGRES=True
POSTGRES_DB=netctrl_production
POSTGRES_USER=secure_db_user
POSTGRES_PASSWORD=very-secure-password
POSTGRES_HOST=your-db-host
POSTGRES_PORT=5432
# GitHub credentials if using GitHub integration
GITHUB_TOKEN=your-github-token
GITHUB_REPOSITORY=yourorg/yourrepo
# Logging to syslog in production
LOG_LEVEL=WARNING
SYSLOG_HOST=logs.yoursite.com
SYSLOG_PORT=514
```

## Docker and Kubernetes

### Docker Compose

```yaml
version: '3'
services:
  web:
    build: .
    environment:
      - DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}
      - DJANGO_DEBUG=False
      - ENVIRONMENT=production
      - DJANGO_ALLOWED_HOSTS=website.com
      - USE_POSTGRES=True
      - POSTGRES_DB=netctrl
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=${DB_PASSWORD}
      - POSTGRES_HOST=db
    depends_on:
      - db
  db:
    image: postgres:13
    environment:
      - POSTGRES_DB=netctrl
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
volumes:
  postgres_data:
```

### Kubernetes Secrets

Example of setting up Kubernetes secrets:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: netctrl-secrets
type: Opaque
data:
  django_secret_key: base64_encoded_secret_key_here
  postgres_password: base64_encoded_password_here
  github_token: base64_encoded_token_here
```

Then reference in deployment:

```yaml
env:
  - name: DJANGO_SECRET_KEY
    valueFrom:
      secretKeyRef:
        name: netctrl-secrets
        key: django_secret_key
```

## Troubleshooting

### Common Issues

1. **Environment variables not being loaded**
   - Ensure the `.env` file is in the project root
   - Verify that python-dotenv is installed
   - Check that `load_dotenv()` is called before variables are used

2. **"Missing required environment variable" errors**
   - Check if all required variables are defined in your `.env` file
   - Verify spelling and case sensitivity of variable names

3. **ValueError when converting environment variables**
   - Ensure variables have the correct format (e.g. `True`/`False` for booleans)
   - Check for trailing whitespace in your `.env` values

### Debugging

To debug environment variable loading:

```python
import os
from dotenv import load_dotenv

load_dotenv()
print(os.environ.get('VARIABLE_NAME', 'Not found'))
```

## References

- [Django Settings Best Practices](https://docs.djangoproject.com/en/stable/topics/settings/)
- [12-Factor App: Config](https://12factor.net/config)
- [python-dotenv Documentation](https://pypi.org/project/python-dotenv/)
