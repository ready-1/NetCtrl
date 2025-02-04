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

# Ensure we're in the app directory
APP_DIR="/opt/netctrl/app"
if [ ! -d "${APP_DIR}" ]; then
    echo "Error: ${APP_DIR} not found. Please run setup.sh first."
    exit 1
fi
cd "${APP_DIR}"

# Check for required files
for file in ".env" "docker-compose.prod.yml"; do
    if [ ! -f "${file}" ]; then
        echo "Error: ${file} not found in ${APP_DIR}"
        echo "Please run setup.sh to properly initialize the application"
        exit 1
    fi
done

# Load environment variables
echo "Loading environment variables..."
set -a  # automatically export all variables
source .env
set +a

# Verify required variables
echo "Verifying environment variables..."
required_vars=(
    "POSTGRES_DB" "POSTGRES_USER" "POSTGRES_PASSWORD" "POSTGRES_HOST" "POSTGRES_PORT"
    "DJANGO_SECRET_KEY" "DJANGO_DEBUG" "DJANGO_ALLOWED_HOSTS"
    "STATIC_ROOT" "MEDIA_ROOT" "LOG_DIR"
)
for var in "${required_vars[@]}"; do
    if [ -z "${!var}" ]; then
        echo "Error: ${var} is not set in .env file"
        exit 1
    fi
done

# Update repository
echo "Updating application..."
git pull origin main


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
until docker compose -f docker-compose.prod.yml exec -T db pg_isready -U "${POSTGRES_USER}" -d "${POSTGRES_DB}"; do
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
