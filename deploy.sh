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

# Create .env file if not exists
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cp .env.example .env

    # Generate secure passwords
    db_password=$(openssl rand -base64 32)
    secret_key=$(openssl rand -base64 64)

    # Update .env file with secure defaults
    sed -i "s/DB_NAME=.*/DB_NAME=netctrl/" .env
    sed -i "s/DB_USER=.*/DB_USER=netctrl/" .env
    sed -i "s/DB_PASSWORD=.*/DB_PASSWORD=$db_password/" .env
    sed -i "s/DB_HOST=.*/DB_HOST=db/" .env
    sed -i "s/DJANGO_SECRET_KEY=.*/DJANGO_SECRET_KEY=$secret_key/" .env
    sed -i "s/DJANGO_DEBUG=.*/DJANGO_DEBUG=False/" .env
    sed -i "s/DJANGO_ALLOWED_HOSTS=.*/DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1/" .env
    sed -i "s|STATIC_ROOT=.*|STATIC_ROOT=/opt/static|" .env
    sed -i "s|MEDIA_ROOT=.*|MEDIA_ROOT=/opt/media|" .env
    sed -i "s|LOG_DIR=.*|LOG_DIR=/opt/logs|" .env

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

# Stop any running containers
echo "Stopping existing containers..."
docker compose -f docker-compose.prod.yml down || true

# Clean up any stale containers
echo "Cleaning up containers..."
docker rm -f $(docker ps -aq) 2>/dev/null || true

# Build and start containers
echo "Building and starting containers..."
docker compose -f docker-compose.prod.yml up --build -d

# Wait for database to be ready
echo "Waiting for database to be ready..."
until docker compose -f docker-compose.prod.yml exec -T db pg_isready -U ${db_user} -d ${db_name}; do
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
echo "  http://${domain_name}/netctrl"
echo "  https://${domain_name}/netctrl"
