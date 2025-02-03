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

1. Install Git and clone the repository:
```bash
sudo apt-get update
sudo apt-get install -y git
git clone <repository-url>
cd netctrl
```

2. Make scripts executable and run setup:
```bash
chmod +x setup.sh deploy.sh
./setup.sh
```
The setup script will:
- Update system packages
- Install Docker and Docker Compose
- Create required directories
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
cd netctrl
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
docker-compose -f docker-compose.prod.yml logs
```

2. Check container status:
```bash
docker-compose -f docker-compose.prod.yml ps
```

3. Restart services:
```bash
docker-compose -f docker-compose.prod.yml restart
```

4. View application logs:
```bash
docker-compose -f docker-compose.prod.yml logs web
```
