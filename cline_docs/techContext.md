# Technical Context

## Technologies

### Backend
- **Framework**: Flask (latest stable version)
- **Language**: Python 3.x
- **Database ORM**: SQLAlchemy
- **Authentication**: Flask-JWT-Extended or Flask-Login
- **Worker Process Management**: Celery
- **SNMP Library**: pysnmp (or similar)
- **API Client**: OpenAPI-generated client for M4300 REST API

### Frontend
- **Framework**: React
- **Styling**: Bootstrap 5 with Bootstrap Icons
- **Build Tools**: Node.js/npm

### Data Storage
- **Primary Database**: PostgreSQL
  - Users, roles, and permissions
  - CMS content
  - File metadata
  - Switch JSON data
- **Cache/Metrics**: Redis
  - SNMP metrics and traps
  - Optional persistence for airgapped recovery

### Infrastructure
- **Containerization**: Docker and Docker Compose
- **Deployment Platform**: Debian Bookworm
- **Web Server**: Nginx (reverse proxy)
- **SSL**: Workaround for self-signed certificates

## Development Environment Setup
- Python virtual environment for backend development
- Node.js/npm for frontend development
- Docker and Docker Compose for container orchestration
- External tools:
  - OpenAPI generator for API client updates
  - SNMP monitoring tools for testing

## Technical Constraints
1. **Airgapped Operation**
   - All dependencies must be pre-installed in images
   - No external network connections during operation
   - Self-contained development environment

2. **Security Considerations**
   - SSL verification disabled (temporary solution)
   - Internal security prioritized
   - Input validation required for all endpoints

3. **Performance Requirements**
   - Support for up to 50 switches
   - Workers distributed to handle polling load
   - Redis for fast SNMP data access

4. **Integration Points**
   - OpenAPI client for M4300 REST API (v2.0.0.59)
   - SNMP for near-realtime metrics
   - JWT token handling for authentication

## API Integration
The application integrates with the Netgear M4300 REST API (v2.0.0.59) using the pre-generated OpenAPI client in the `openapi_client` directory. This client provides:

- Authentication endpoints
- Device settings management
- Port configuration
- VLAN management
- Diagnostics tools
- And many other switch management features

## Testing Strategy
- 100% test coverage goal
- Backend: pytest for unit and integration tests
- Frontend: Jest for React component testing
- Live test switch for OpenAPI/SNMP validation

## Documentation Resources

### Container Infrastructure
- [Docker Documentation](https://docs.docker.com/reference/)

### Frontend Technologies
- [React Documentation](https://react.dev/reference/react)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

### Operating Systems
- [Debian Documentation](https://www.debian.org/doc/)

### Flask Ecosystem
- [Flask Documentation](https://flask.palletsprojects.com/en/2.2.x/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/)

### Database and Storage
- [PostgreSQL Documentation](https://www.postgresql.org/docs/current/index.html)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/2.0/)
- [Psycopg (PostgreSQL driver)](https://www.psycopg.org/docs/)
- [Redis-py](https://redis-py.readthedocs.io/en/stable/)

### Task Processing
- [Celery](https://docs.celeryproject.org/en/stable/)
- [Flower (Celery monitoring)](https://flower.readthedocs.io/en/latest/)

### Networking and Security
- [PySNMP](https://pysnmp.readthedocs.io/en/latest/)
- [PyCryptodome](https://pycryptodome.readthedocs.io/en/latest/)
- [Requests](https://requests.readthedocs.io/en/latest/)
- [Urllib3](https://urllib3.readthedocs.io/en/latest/)

### Testing
- [Pytest](https://docs.pytest.org/en/7.3.x/)
- [Pytest-Flask](https://pytest-flask.readthedocs.io/en/latest/)
- [Pytest-Cov](https://pytest-cov.readthedocs.io/en/latest/)

### Utilities and Configuration
- [Python-dotenv](https://github.com/theskumar/python-dotenv)
- [Marshmallow](https://marshmallow.readthedocs.io/en/stable/)
- [Gunicorn](https://docs.gunicorn.org/en/stable/)
