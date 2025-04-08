# NetCtrl Project

## Centralized Logging System with Syslog and Graylog

This repository contains the implementation for the NetCtrl project's centralized logging system with the following components:

### Syslog Server

The Syslog server is implemented using syslog-ng and provides:
- Centralized log collection over TCP (port 601) and UDP (port 514)
- Log categorization by service (nginx, django, postgres)
- Structured logging template
- Integration with Graylog via GELF format
- Log rotation with configurable retention periods (7-30 days)
- Error log aggregation

### Log Viewer (Graylog)

A web-based log viewer is available at http://localhost:8080/logs/ providing:
- Comprehensive log management and searching
- Advanced filtering and analysis capabilities
- Service-specific log views
- Dashboard creation
- Alert configuration
- GELF input support (UDP port 12201)
- Direct access to syslog log files

### Python Logging Integration

A standardized Python logging facility with:
- Centralized configuration in `src/netctrl/logging_config.py`
- Custom TCP handler for reliable syslog communication
- Automatic integration with the centralized logging system
- Structured log formatting
- Console and syslog outputs
- Service tag support for proper log categorization
- Example Django views demonstrating proper usage

### Docker Infrastructure

The system uses Docker Compose with:
- Modern compose.yaml syntax
- Bridge networking
- Volume management for persistent logs
- Health checks
- Proper service dependencies
- JSON-file logging driver with rotation for container logs

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.12 for running the test script and using the logging facility

### Starting the Services

```bash
# Start all services
docker compose up -d

# Start only the logging components
docker compose up -d syslog elasticsearch mongodb logviewer
```

### Testing

A Python test script is provided to verify the logging functionality:

```bash
python scripts/syslog_test.py
```

This script sends test log entries to all configured log streams for validation using both TCP and UDP connections.

### Viewing Logs

1. Open http://localhost:8080/logs/ in your browser
2. Login with username: `admin` and password: `admin`
3. Navigate to the "Search" tab to view incoming logs
4. Create custom dashboards and views as needed

## Project Structure

```
├── app/                      # Django application
│   ├── Dockerfile            # Django app container configuration
│   └── requirements.txt      # Python dependencies
├── compose.yaml              # Docker Compose configuration
├── nginx/                    # Nginx configuration
│   └── nginx.conf            # Main Nginx configuration file
├── scripts/
│   └── syslog_test.py        # Python test script for syslog verification
├── src/
│   └── netctrl/
│       ├── logging_config.py # Python logging facility configuration
│       └── views_example.py  # Example Django views with logging
└── syslog/
    └── syslog-ng.conf        # Syslog-ng configuration
```

## Logs Location

- Container logs: Managed by Docker using json-file driver with rotation
- Syslog log files (inside the syslog container):
  - `/var/log/all.log` - All logs
  - `/var/log/nginx.log` - Nginx-specific logs
  - `/var/log/django.log` - Django-specific logs
  - `/var/log/postgres.log` - PostgreSQL-specific logs
  - `/var/log/errors.log` - Error logs from all services
- Graylog logs: Stored in Elasticsearch and accessible via the web interface

## Using the Python Logging Facility

To use the logging facility in your application code:

```python
from netctrl.logging_config import get_logger

# Create a logger with an optional service tag
logger = get_logger(__name__, 'django')

# Use standard logging methods
logger.debug("Debug message")
logger.info("Information message")
logger.warning("Warning message")
logger.error("Error message", exc_info=True)  # Include exception info
```

The logs will be sent to both the console and the syslog server, then aggregated and viewable in Graylog.

## Future Development

The next steps for this project include:
- Implementing the Django project structure
- Developing CMS core functionality with file management up to 5GB
- Creating a user interface with mobile-first design and dark mode support
- Implementing comprehensive testing
- Preparing for air-gapped deployment
- Phase 2: Implementing network management for Netgear M4300 switches
