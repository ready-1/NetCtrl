#!/bin/bash

# Exit on error
set -e

echo "Starting deployment..."

# Pull latest changes
echo "Pulling latest changes..."
git pull origin main

# Create .env file if not exists
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cp .env.example .env

    # Prompt for environment variables
    read -p "Database Name: " db_name
    read -p "Database User: " db_user
    read -sp "Database Password: " db_password
    echo
    read -p "Database Host: " db_host
    read -p "Allowed Hosts (comma-separated): " allowed_hosts

    # Generate a secure secret key
    secret_key=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')

    # Update .env file
    sed -i "s/DB_NAME=.*/DB_NAME=$db_name/" .env
    sed -i "s/DB_USER=.*/DB_USER=$db_user/" .env
    sed -i "s/DB_PASSWORD=.*/DB_PASSWORD=$db_password/" .env
    sed -i "s/DB_HOST=.*/DB_HOST=$db_host/" .env
    sed -i "s/DJANGO_SECRET_KEY=.*/DJANGO_SECRET_KEY=$secret_key/" .env
    sed -i "s/DJANGO_ALLOWED_HOSTS=.*/DJANGO_ALLOWED_HOSTS=$allowed_hosts/" .env
fi

# Build and start containers
echo "Building and starting containers..."
docker-compose -f docker-compose.prod.yml up --build -d

# Wait for web container to be ready
echo "Waiting for web container to be ready..."
sleep 10

# Run migrations
echo "Running database migrations..."
docker-compose -f docker-compose.prod.yml exec -T web poetry run python manage.py migrate

# Collect static files
echo "Collecting static files..."
docker-compose -f docker-compose.prod.yml exec -T web poetry run python manage.py collectstatic --noinput

echo "Deployment completed successfully!"
echo "Please ensure your Nginx configuration is properly set up to proxy requests to the application."
