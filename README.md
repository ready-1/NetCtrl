# NetCtrl

Network switch management system for M4300 switches.

## Development Setup

### Prerequisites

- Python 3.12+
- Poetry for dependency management
- PostgreSQL database (via Docker)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd netctrl
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Activate the virtual environment:
```bash
poetry shell
```

### Database Setup

The application uses PostgreSQL with the following development configuration:
- Host: localhost
- Port: 5432
- Database: netctrl
- Username: postgres
- Password: postgres

### Running Tests

```bash
poetry run pytest
```

### Code Formatting

```bash
poetry run black .
```

### Linting

```bash
poetry run flake8
```

## Project Structure

- `docs/` - Project documentation
- `openapi_client/` - Generated M4300 API client

## Production Deployment

### Prerequisites

- Fresh Debian installation (Debian 11+ or Ubuntu 22.04+)
- Root or sudo access
- Git installed (`apt-get install git`)

### Deployment Files

- `setup.sh` - System preparation script
- `deploy.sh` - Application deployment script
- `docker-compose.prod.yml` - Production Docker configuration
- `.env.example` - Environment variables template
- `nginx.conf.example` - Nginx configuration template

### Initial Server Setup

1. Clone the repository:
```bash
git clone <repository-url> netctrl
cd netctrl
```

2. Make scripts executable:
```bash
chmod +x cleanup.sh setup.sh deploy.sh
```

3. Clean up system (if needed):
```bash
./cleanup.sh
```
The cleanup script will:
- Remove any conflicting repositories
- Clean package manager cache
- Remove old Docker containers and volumes
- Clean up old installation directories

4. Run system setup:
```bash
./setup.sh
```
The setup script will:
- Update system packages
- Install Docker Engine with Compose
- Create required directories in /opt/netctrl
- Clone repository to /opt/netctrl/app
- Generate SSL certificate
- Configure system permissions
- Set up environment variables
- Generate secure passwords
- Display initial credentials
- Stop and disable system Nginx (if installed)

IMPORTANT: Save the displayed database password and other credentials securely after setup.

3. Log out and back in for Docker permissions to take effect:
```bash
exit
# Log back in
```

### Application Deployment

1. Run the deployment script:
```bash
cd /opt/netctrl/app
./deploy.sh
```
The script will:
- Configure environment variables
- Stop and remove existing project containers
- Clean up project networks
- Build and start fresh Docker containers
- Initialize database
- Set up Nginx proxy
- Deploy the application

Note: By default, the script preserves database volumes. To perform a complete cleanup including volumes, uncomment the volume removal section in deploy.sh.

The application will be available at:
- http://your-domain/netctrl
- https://your-domain/netctrl

### Environment Configuration

The environment is automatically configured with secure defaults:
- Database name: netctrl
- Database user: netctrl
- Database password: auto-generated (displayed during setup)
- Debug mode: disabled
- Secret key: auto-generated
- Static/Media paths: configured for production

#### Host Configuration

The application is configured to accept requests from:
- localhost
- 127.0.0.1
- Docker network IPs
- All hosts (*) for development

For production, you should update DJANGO_ALLOWED_HOSTS in .env to list your specific domains:
```bash
# Example for production
DJANGO_ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

#### Docker Network Access

The application can be accessed through:
- Host machine: http://localhost/netctrl
- Docker network: http://<container-ip>/netctrl
- Production domain: https://yourdomain.com/netctrl

To modify these settings:
```bash
# Edit environment variables
nano /opt/netctrl/app/.env

# Restart services after changes
docker compose -f docker-compose.prod.yml restart
```

### Port Requirements

The application requires the following ports:
- 80 (HTTP): Must be free for Nginx container
- 443 (HTTPS): Must be free for Nginx container
- 6379 (Redis): Internal use only
- 5432 (PostgreSQL): Internal use only

Note: The setup script will automatically stop and disable any existing Nginx service to prevent port conflicts. If you have other services using ports 80 or 443, please stop them before deployment.

### Updating the Application

To update to the latest version:
```bash
cd netctrl
git pull
./deploy.sh
```

### Troubleshooting

1. Port Conflicts:
```bash
# Check if ports are in use
sudo lsof -i :80
sudo lsof -i :443

# Stop system Nginx if running
sudo systemctl stop nginx
sudo systemctl disable nginx
```

2. View container logs:
```bash
docker compose -f docker-compose.prod.yml logs
```

3. Check container status and health:
```bash
docker compose -f docker-compose.prod.yml ps
```

4. Check service health details:
```bash
# Database health
docker compose -f docker-compose.prod.yml exec db pg_isready -U ${DB_USER} -d ${DB_NAME}

# Redis health
docker compose -f docker-compose.prod.yml exec redis redis-cli ping
```

5. Restart services:
```bash
docker compose -f docker-compose.prod.yml restart
```

6. View application logs:
```bash
# All container logs
docker compose -f docker-compose.prod.yml logs

# Specific service logs
docker compose -f docker-compose.prod.yml logs web
docker compose -f docker-compose.prod.yml logs db
docker compose -f docker-compose.prod.yml logs nginx

# Application log file
tail -f /opt/netctrl/logs/netctrl.log
```

### Service Health Monitoring

The deployment includes built-in health checks for:
- Database: Checks PostgreSQL readiness
- Redis: Verifies Redis connection
- Web: Monitored through Nginx
- Static/Media files: Served through Nginx

Health check configurations:
- Interval: 5 seconds
- Timeout: 5 seconds
- Retries: 5
- Start period: 10 seconds

### System Requirements

- Debian 11+ or Ubuntu 22.04+
- 2GB RAM minimum
- 20GB disk space recommended
- Git (installed automatically)
- Docker Engine 24.0+ (installed automatically)
- Ports 80 and 443 must be available

### Directory Structure

```
/opt/netctrl/
├── app/              # Application code (Git repository)
├── static/           # Static files served by Nginx
├── media/           # Media files served by Nginx
├── logs/            # Application and server logs
└── certs/           # SSL certificates
```

### Log Files

The application logs are stored in `/opt/netctrl/logs/netctrl.log`. You can view them using:
```bash
tail -f /opt/netctrl/logs/netctrl.log
```

For container logs, use:
```bash
docker compose -f docker-compose.prod.yml logs -f
