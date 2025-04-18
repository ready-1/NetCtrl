# NetCtrl CMS

A Django-based Content Management System with file management capabilities and network control features.

## Project Overview

NetCtrl CMS is a comprehensive Django web application that combines content management functionality with network management capabilities. The system allows users to manage documents and files (supporting uploads up to 5GB), along with monitoring and controlling network infrastructure.

### Key Features

- **Content Management System**
  - Document management with categories and tags
  - File management supporting files up to 5GB
  - Chunked file upload for large files
  - Rich text editing

- **Network Control**
  - Network monitoring and visualization
  - Device management
  - Performance metrics
  - Alert system

## Implementation Status

This implementation represents Phase 1 of the project, focusing on:

- Core Django project setup
- Database models for CMS functionality
- User authentication system
- Admin interface
- Placeholder UI with Bootstrap 5
- Responsive design with dark mode support

The following features are currently implemented as placeholders and will be fully implemented in subsequent phases:
- Chunked file upload for large files
- Document/file content views and management
- Network monitoring and control

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL (optional, SQLite is used for development)

### Installation

1. Clone the repository
```bash
git clone <repository-url>
cd NetCtrl
```

2. Create and activate a virtual environment
```bash
python -m venv python
source python/bin/activate  # On Windows: python\Scripts\activate
```

3. Install dependencies
```bash
pip install -r app/requirements.txt
```

4. Apply database migrations
```bash
cd app
python manage.py migrate
```

5. Create a superuser (admin account)
```bash
python manage.py createsuperuser
```

6. Run the development server
```bash
python manage.py runserver
```

7. Access the application at `http://localhost:8000`

### Environment Configuration

NetCtrl uses environment variables for configuration, especially for sensitive information like API keys and credentials. These are managed through a `.env` file in the project root.

#### Setting Up Your Environment

1. Copy the example environment file to create your own:
   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file and set the appropriate values for your environment:
   ```bash
   # Open in your favorite editor
   nano .env  # or vim .env, code .env, etc.
   ```

3. Generate a secure Django secret key (if needed):
   ```bash
   python -c "from django.core.management.utils.get_random_secret_key import get_random_secret_key; print(get_random_secret_key())"
   ```

#### Available Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| **Core Django Settings** |
| `DJANGO_SECRET_KEY` | Django encryption key | Auto-generated (insecure) | Yes for production |
| `DJANGO_DEBUG` | Debug mode | `True` | No |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated list of allowed hosts | `localhost,127.0.0.1` | No |
| `ENVIRONMENT` | Environment type (development, testing, production) | `development` | No |
| **Database Configuration** |
| `USE_POSTGRES` | Use PostgreSQL instead of SQLite | `False` | No |
| `POSTGRES_DB` | PostgreSQL database name | `netctrl_db` | Yes if using PostgreSQL |
| `POSTGRES_USER` | PostgreSQL username | `netctrl_user` | Yes if using PostgreSQL |
| `POSTGRES_PASSWORD` | PostgreSQL password | `netctrl_password` | Yes if using PostgreSQL |
| `POSTGRES_HOST` | PostgreSQL host | `postgres` | Yes if using PostgreSQL |
| `POSTGRES_PORT` | PostgreSQL port | `5432` | Yes if using PostgreSQL |
| **GitHub Integration** |
| `GITHUB_TOKEN` | GitHub Personal Access Token | None | Yes for GitHub features |
| `GITHUB_REPOSITORY` | GitHub repository name (format: owner/repo) | `ready-1/NetCtrl` | No |
| **Logging Configuration** |
| `LOG_LEVEL` | Log level (INFO, WARNING, ERROR, DEBUG) | `INFO` | No |
| `SYSLOG_HOST` | Syslog server host | None | No |
| `SYSLOG_PORT` | Syslog server port | `5140` | No |
| **File Storage** |
| `MEDIA_ROOT` | Absolute path to media storage | `BASE_DIR/media` | No |
| `STATIC_ROOT` | Absolute path to static files storage | `BASE_DIR/staticfiles` | No |

#### Using Environment Variables in Different Contexts

**Development**:
- Use the `.env` file in the project root
- Set `ENVIRONMENT=development` and `DJANGO_DEBUG=True`

**Production**:
- Set `ENVIRONMENT=production` and `DJANGO_DEBUG=False`
- Ensure a secure `DJANGO_SECRET_KEY` is set
- Configure appropriate database settings

**Docker**:
- Environment variables can be passed to Docker using the `-e` flag or in `docker-compose.yml`
- Example `docker-compose.yml` excerpt:
  ```yaml
  services:
    web:
      build: .
      environment:
        - DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}
        - DJANGO_DEBUG=False
        - ENVIRONMENT=production
  ```

## Project Structure

```
NetCtrl/
├── app/                  # Django application
│   ├── cms/              # CMS application
│   │   ├── models/       # CMS models
│   │   └── templates/    # CMS templates
│   ├── network/          # Network application
│   ├── netctrl/          # Django project settings
│   ├── static/           # Static files (CSS, JS)
│   │   ├── css/          # CSS files
│   │   └── js/           # JavaScript files
│   ├── templates/        # Base templates
│   ├── manage.py         # Django management script
│   └── requirements.txt  # Python dependencies
├── syslog/               # Syslog configuration
├── scripts/              # Utility scripts
└── docs/                 # Documentation
```

## Authentication

The system uses Django's built-in authentication system with extended user profiles. Key URLs:

- Login: `/accounts/login/`
- Logout: `/accounts/logout/`
- Admin: `/admin/`

Default credentials for development:
- Username: admin
- Email: admin@example.com
- Password: (set during `createsuperuser`)

## Development

### Running with SQLite (Development)

By default, the application uses SQLite for development:

```bash
cd app
python manage.py runserver
```

### Running with PostgreSQL (Production-like)

To use PostgreSQL:

1. Ensure PostgreSQL is running
2. Set environment variables:
```bash
export USE_POSTGRES=True
export POSTGRES_DB=netctrl_db
export POSTGRES_USER=netctrl_user
export POSTGRES_PASSWORD=netctrl_password
export POSTGRES_HOST=localhost
export POSTGRES_PORT=5432
```
3. Run the server:
```bash
python manage.py runserver
```

## Logging

The application uses a custom logging configuration that integrates with syslog:

- Console logging for development
- Syslog integration for production
- Custom TCP syslog handler for reliable delivery

## Contributing

1. Create a feature branch
2. Implement your changes
3. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
