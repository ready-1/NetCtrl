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

- Ubuntu server with:
  - Docker and Docker Compose installed
  - Nginx installed and running
  - Existing PostgreSQL database
  - Git installed

### Deployment Files

- `docker-compose.prod.yml` - Production Docker Compose configuration
- `.env.example` - Template for environment variables
- `deploy.sh` - Deployment script
- `nginx.conf.example` - Example Nginx configuration

### Deployment Steps

1. Clone the repository on your server:
```bash
git clone <repository-url>
cd netctrl
```

2. Make the deployment script executable:
```bash
chmod +x deploy.sh
```

3. Run the deployment script:
```bash
./deploy.sh
```
The script will:
- Pull the latest changes
- Set up environment variables (first run only)
- Build and start Docker containers
- Run database migrations
- Collect static files

4. Configure Nginx:
```bash
# Copy and modify the Nginx configuration
sudo cp nginx.conf.example /etc/nginx/sites-available/netctrl
sudo nano /etc/nginx/sites-available/netctrl

# Create symlink and test configuration
sudo ln -s /etc/nginx/sites-available/netctrl /etc/nginx/sites-enabled/
sudo nginx -t

# Reload Nginx
sudo systemctl reload nginx
```

### Environment Variables

Required environment variables in `.env`:
- `DB_NAME` - PostgreSQL database name
- `DB_USER` - Database username
- `DB_PASSWORD` - Database password
- `DB_HOST` - Database host
- `DJANGO_SECRET_KEY` - Django secret key
- `DJANGO_ALLOWED_HOSTS` - Comma-separated list of allowed hosts

### Updating the Application

To update to the latest version:
```bash
./deploy.sh
```

### Troubleshooting

1. Check container logs:
```bash
docker-compose -f docker-compose.prod.yml logs web
```

2. Check Nginx logs:
```bash
sudo tail -f /var/log/nginx/netctrl_error.log
```

3. Check container status:
```bash
docker-compose -f docker-compose.prod.yml ps
```
