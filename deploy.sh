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

# Handle local changes
echo "Checking for local changes..."
if git status --porcelain | grep -q '^.M \(deploy\.sh\|docker-compose\.prod\.yml\|\.env\.example\)$'; then
    echo "Found local changes in deployment files..."
    echo "Stashing changes before update..."
    git stash push -m "pre-deployment-stash" -- deploy.sh docker-compose.prod.yml .env.example
fi

# Update repository
echo "Updating application..."
if ! git pull origin main; then
    echo "Error: Failed to update from repository"
    if [ -n "$(git stash list | grep pre-deployment-stash)" ]; then
        echo "Restoring local changes..."
        git stash pop
    fi
    exit 1
fi

# Restore local changes if any were stashed
if [ -n "$(git stash list | grep pre-deployment-stash)" ]; then
    echo "Restoring local changes..."
    if ! git stash pop; then
        echo "Warning: Failed to restore local changes. Please check git stash list"
        exit 1
    fi
fi

# Check for .env.example
if [ ! -f .env.example ]; then
    echo "Error: .env.example not found"
    exit 1
fi

# Create/update environment file
echo "Setting up environment..."

# Generate new secrets
db_password=$(openssl rand -base64 32)
secret_key=$(openssl rand -base64 64)

if [ ! -f .env ]; then
    echo "Creating new .env file..."
    cp .env.example .env
else
    echo "Updating existing .env file..."
    # Backup existing passwords
    old_db_password=$(grep "^POSTGRES_PASSWORD=" .env | cut -d'=' -f2-)
    old_secret_key=$(grep "^DJANGO_SECRET_KEY=" .env | cut -d'=' -f2-)

    # Use existing passwords if they exist
    if [ ! -z "$old_db_password" ]; then
        db_password=$old_db_password
    fi
    if [ ! -z "$old_secret_key" ]; then
        secret_key=$old_secret_key
    fi
fi

# Update .env file
echo "Configuring environment variables..."
sed -i "s/POSTGRES_DB=.*/POSTGRES_DB=netctrl/" .env
sed -i "s/POSTGRES_USER=.*/POSTGRES_USER=netctrl/" .env
sed -i "s/POSTGRES_PASSWORD=.*/POSTGRES_PASSWORD=$db_password/" .env
sed -i "s/POSTGRES_HOST=.*/POSTGRES_HOST=db/" .env
sed -i "s/POSTGRES_PORT=.*/POSTGRES_PORT=5432/" .env
sed -i "s/DJANGO_SECRET_KEY=.*/DJANGO_SECRET_KEY=$secret_key/" .env
sed -i "s/DJANGO_DEBUG=.*/DJANGO_DEBUG=False/" .env
sed -i "s|DJANGO_ALLOWED_HOSTS=.*|DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0,172.29.10.99,172.16.0.0,172.17.0.0,172.18.0.0,172.19.0.0,172.20.0.0,172.21.0.0,172.22.0.0,172.23.0.0,172.24.0.0,172.25.0.0,172.26.0.0,172.27.0.0,172.28.0.0,172.29.0.0,172.30.0.0,172.31.0.0,192.168.0.0|" .env
sed -i "s|STATIC_ROOT=.*|STATIC_ROOT=/opt/static|" .env
sed -i "s|MEDIA_ROOT=.*|MEDIA_ROOT=/opt/media|" .env
sed -i "s|LOG_DIR=.*|LOG_DIR=/opt/logs|" .env

# Convert any old DB_ prefixes to POSTGRES_
sed -i "s/DB_\([A-Z]*\)=/POSTGRES_\1=/g" .env

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

if [ ! -f docker-compose.prod.yml ]; then
    echo "Error: docker-compose.prod.yml not found"
    exit 1
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
