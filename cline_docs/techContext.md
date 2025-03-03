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
