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
- Build and start Docker containers
- Initialize database
- Set up Nginx proxy
- Deploy the application

The application will be available at:
- http://your-domain/netctrl
- https://your-domain/netctrl

### Environment Configuration

The deployment script will prompt for:
- Database name (default: netctrl)
- Database user (default: netctrl)
- Database password
- Domain name or IP address

### Updating the Application

To update to the latest version:
```bash
cd netctrl
git pull
./deploy.sh
```

### Troubleshooting

1. View container logs:
```bash
docker compose -f docker-compose.prod.yml logs
```

2. Check container status:
```bash
docker compose -f docker-compose.prod.yml ps
```

3. Restart services:
```bash
docker compose -f docker-compose.prod.yml restart
```

4. View application logs:
```bash
docker compose -f docker-compose.prod.yml logs web
```

### System Requirements

- Debian 11+ or Ubuntu 22.04+
- 2GB RAM minimum
- 20GB disk space recommended
- Git (installed automatically)
- Docker Engine 24.0+ (installed automatically)

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
```
