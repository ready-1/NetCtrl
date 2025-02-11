# Technologies & Dependencies

## Core Framework
- Python 3.11
- Django 4.2.10
- Django REST Framework

## Data Storage
- PostgreSQL 15
- Redis 7.0.12
- HashiCorp Vault 1.15.4

## Infrastructure
- Docker & Docker Compose
- Nginx
- TFTP Server
- CA Manager (custom Python service)

## Development Tools
- Pre-commit hooks
- Black code formatter
- Flake8 linter
- MyPy type checker

## Security
- cryptography (Fernet encryption)
- python-environ
- django-environ

## Environment Variables
- ENCRYPTION_KEY: For Fernet encryption
- SWITCH_DEFAULT_USERNAME: Default switch admin username
- SWITCH_DEFAULT_PASSWORD: Default switch admin password
- VAULT_ROOT_TOKEN: For HashiCorp Vault access
- Database configuration (POSTGRES_*)
- Redis configuration (REDIS_URL)
- Django settings (DEBUG, SECRET_KEY)

## Planned Integrations
- Certificate Authority system
- TFTP configuration deployment
- CLI command execution system
