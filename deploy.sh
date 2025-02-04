#!/bin/bash

# Exit on error
set -e

echo "Starting deployment..."

# Check if setup.sh has been run
if [ ! -d "/opt/netctrl" ]; then
    echo "Error: /opt/netctrl directory not found."
    echo "Please run setup.sh first to prepare the system."
    exit 1
fi

# Pull latest changes
echo "Pulling latest changes..."
git pull origin main

# Create .env file if not exists
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cp .env.example .env

    # Prompt for environment variables
    read -p "Database Name (default: netctrl): " db_name
    db_name=${db_name:-netctrl}

    read -p "Database User (default: netctrl): " db_user
    db_user=${db_user:-netctrl}

    read -sp "Database Password: " db_password
    echo

    read -p "Domain Name (or IP address): " domain_name
    domain_name=${domain_name:-localhost}

    # Generate a secure secret key
    secret_key=$(python3 -c 'from secrets import token_urlsafe; print(token_urlsafe(50))')

    # Update .env file
    sed -i "s/DB_NAME=.*/DB_NAME=$db_name/" .env
    sed -i "s/DB_USER=.*/DB_USER=$db_user/" .env
    sed -i "s/DB_PASSWORD=.*/DB_PASSWORD=$db_password/" .env
    sed -i "s/DJANGO_SECRET_KEY=.*/DJANGO_SECRET_KEY=$secret_key/" .env
    sed -i "s/DJANGO_ALLOWED_HOSTS=.*/DJANGO_ALLOWED_HOSTS=$domain_name,localhost/" .env
fi

# Copy Nginx configuration
echo "Setting up Nginx configuration..."
cp nginx.conf.example nginx.conf

# Stop any running containers
echo "Stopping existing containers..."
docker compose -f docker-compose.prod.yml down || true

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
