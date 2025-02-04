#!/bin/bash

# Exit on error
set -e

echo "Starting deployment..."

# Check if setup.sh has been run
if [ ! -d "/opt/netctrl/app" ]; then
    echo "Error: /opt/netctrl/app directory not found."
    echo "Please run setup.sh first to prepare the system."
    exit 1
fi

# Change to app directory and update
echo "Updating application..."
cd /opt/netctrl/app
git pull origin main

# Copy .env.example if needed
if [ ! -f .env.example ]; then
    echo "Error: .env.example not found in current directory"
    exit 1
fi

# Create .env file if not exists
if [ ! -f /opt/netctrl/app/.env ]; then
    echo "Creating .env file..."
    cp .env.example /opt/netctrl/app/.env

    # Generate secure passwords
    db_password=$(openssl rand -base64 32)
    secret_key=$(openssl rand -base64 64)

    # Convert any old DB_ prefixes to POSTGRES_
    sed -i "s/DB_\([A-Z]*\)=/POSTGRES_\1=/g" /opt/netctrl/app/.env

    # Update .env file with secure defaults
    sed -i "s/POSTGRES_DB=.*/POSTGRES_DB=netctrl/" /opt/netctrl/app/.env
    sed -i "s/POSTGRES_USER=.*/POSTGRES_USER=netctrl/" /opt/netctrl/app/.env
    sed -i "s/POSTGRES_PASSWORD=.*/POSTGRES_PASSWORD=$db_password/" /opt/netctrl/app/.env
    sed -i "s/POSTGRES_HOST=.*/POSTGRES_HOST=db/" /opt/netctrl/app/.env
    sed -i "s/POSTGRES_PORT=.*/POSTGRES_PORT=5432/" /opt/netctrl/app/.env
    sed -i "s/DJANGO_SECRET_KEY=.*/DJANGO_SECRET_KEY=$secret_key/" /opt/netctrl/app/.env
    sed -i "s/DJANGO_DEBUG=.*/DJANGO_DEBUG=False/" /opt/netctrl/app/.env
    sed -i "s|DJANGO_ALLOWED_HOSTS=.*|DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0,172.29.10.99,172.16.0.0,172.17.0.0,172.18.0.0,172.19.0.0,172.20.0.0,172.21.0.0,172.22.0.0,172.23.0.0,172.24.0.0,172.25.0.0,172.26.0.0,172.27.0.0,172.28.0.0,172.29.0.0,172.30.0.0,172.31.0.0,192.168.0.0|" /opt/netctrl/app/.env
    sed -i "s|STATIC_ROOT=.*|STATIC_ROOT=/opt/static|" /opt/netctrl/app/.env
    sed -i "s|MEDIA_ROOT=.*|MEDIA_ROOT=/opt/media|" /opt/netctrl/app/.env
    sed -i "s|LOG_DIR=.*|LOG_DIR=/opt/logs|" /opt/netctrl/app/.env

    # Verify environment variables
    echo "Verifying environment variables..."
    required_vars=("POSTGRES_DB" "POSTGRES_USER" "POSTGRES_PASSWORD" "POSTGRES_HOST" "DJANGO_SECRET_KEY" "DJANGO_ALLOWED_HOSTS" "STATIC_ROOT" "MEDIA_ROOT" "LOG_DIR")
    for var in "${required_vars[@]}"; do
        if ! grep -q "^$var=" /opt/netctrl/app/.env; then
            echo "Error: $var is not set in .env file"
            exit 1
        fi
    done

    echo "Environment file created with secure defaults"
    echo "Database password: $db_password"
    echo "Please save these credentials securely"
fi

# Ensure directories exist and have correct permissions
echo "Setting up directories..."
mkdir -p /opt/netctrl/{static,media,logs}
chmod 777 /opt/netctrl/{static,media,logs}

# Copy and configure Nginx
echo "Setting up Nginx configuration..."
cp nginx.conf.example /opt/netctrl/app/nginx.conf

# Stop system Nginx if running
echo "Checking system Nginx..."
if systemctl is-active --quiet nginx; then
    echo "Stopping system Nginx..."
    sudo systemctl stop nginx
fi

# Stop and remove all project containers
echo "Stopping and removing project containers..."
project_containers=$(docker ps -a --filter name=netctrl -q)
if [ ! -z "$project_containers" ]; then
    echo "Found existing project containers, removing..."
    docker stop $project_containers
    docker rm $project_containers
fi

# Remove project networks
echo "Removing project networks..."
project_networks=$(docker network ls --filter name=netctrl -q)
if [ ! -z "$project_networks" ]; then
    echo "Found project networks, removing..."
    docker network rm $project_networks || true
fi

# Remove project volumes (optional, comment out to preserve data)
# echo "Removing project volumes..."
# project_volumes=$(docker volume ls --filter name=netctrl -q)
# if [ ! -z "$project_volumes" ]; then
#     echo "Found project volumes, removing..."
#     docker volume rm $project_volumes || true
# fi

# Stop any running containers
echo "Stopping existing containers..."
docker compose -f docker-compose.prod.yml down --remove-orphans || true

# Build and start containers
echo "Building and starting containers..."
docker compose -f docker-compose.prod.yml up --build -d

# Wait for database to be ready
echo "Waiting for database to be ready..."
until docker compose -f docker-compose.prod.yml exec -T db pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}; do
    echo "Database is unavailable - sleeping"
    sleep 1
done

# Run migrations
echo "Running database migrations..."
docker compose -f docker-compose.prod.yml exec -T web poetry run python manage.py migrate

# Collect static files
echo "Collecting static files..."
docker compose -f docker-compose.prod.yml exec -T web poetry run python manage.py collectstatic --noinput

echo "Deployment completed successfully!"
echo "Your application should now be available at:"
for host in ${DJANGO_ALLOWED_HOSTS//,/ }; do
    echo "  http://${host}/netctrl"
    echo "  https://${host}/netctrl"
done
