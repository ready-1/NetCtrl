# System Patterns

## Architecture
The application follows a containerized microservices architecture with four primary Docker containers:

1. **Flask App Container**
   - Core backend services
   - API endpoints
   - Business logic
   - Worker processes for switch polling

2. **PostgreSQL Container**
   - Persistent data storage
   - Stores user information
   - CMS content
   - Switch configuration data

3. **Redis Container**
   - Near-realtime SNMP metrics storage
   - Caching layer
   - Worker task queue

4. **Nginx Container**
   - Reverse proxy
   - Static file serving
   - API request forwarding

## Data Flow
```
User → Nginx → Flask → PostgreSQL/Redis
                ↓
         Worker Processes
                ↓
            Switches
```

## Key Technical Decisions
1. **Worker Processes**
   - Celery workers for switch polling
   - Managed task queue for distributed processing
   - Configured to balance load across switches

2. **API Design**
   - RESTful API endpoints
   - OpenAPI integration for M4300 switches
   - SNMP integration for near-realtime metrics

3. **Authentication**
   - JWT-based authentication
   - Role-based access control
   - Air-gapped registration workflow

4. **Database Schema**
   - Users and roles tables
   - CMS content storage
   - Switch configuration JSON storage
   - File metadata tracking

5. **SSL Handling**
   - Temporary workaround for self-signed certificates
   - Suppression of insecure connection warnings

## Deployment Strategy
- Docker Compose for container orchestration
- Environment variables for configuration
- Shared volumes for file storage
- Self-contained dependencies for air-gapped operation
