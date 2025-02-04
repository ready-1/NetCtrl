#!/bin/bash

# Exit on error
set -e

echo "Starting system setup..."

# Update system
echo "Updating system packages..."
sudo apt-get update
sudo apt-get upgrade -y

# Install required packages
echo "Installing required packages..."
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    git

# Stop and disable system Nginx if installed
echo "Checking system Nginx..."
if dpkg -l | grep -q nginx; then
    echo "Stopping and disabling system Nginx..."
    sudo systemctl stop nginx
    sudo systemctl disable nginx
fi

# Install Docker
echo "Installing Docker..."
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Docker Compose is now included with Docker Engine
echo "Docker Compose is included with Docker Engine..."

# Add current user to docker group
echo "Adding user to docker group..."
sudo usermod -aG docker $USER

# Create required directories with proper permissions
echo "Creating project directories..."
sudo mkdir -p /opt/netctrl/{app,static,media,certs,logs}
sudo chown -R $USER:$USER /opt/netctrl
sudo chmod 755 /opt/netctrl
sudo chmod 777 /opt/netctrl/{static,media,logs}

# Generate self-signed SSL certificate (for development)
echo "Generating self-signed SSL certificate..."
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /opt/netctrl/certs/privkey.pem \
    -out /opt/netctrl/certs/fullchain.pem \
    -subj "/C=US/ST=State/L=City/O=Organization/CN=localhost"

# Clone repository if not exists
if [ ! -d "/opt/netctrl/app/.git" ]; then
    echo "Cloning repository..."
    git clone "$PWD" /opt/netctrl/app
    cd /opt/netctrl/app

    # Copy environment file
    cp .env.example .env

    # Generate secure passwords
    db_password=$(openssl rand -base64 32)
    secret_key=$(openssl rand -base64 64)

    # Update .env file with secure defaults
    sed -i "s/POSTGRES_DB=.*/POSTGRES_DB=netctrl/" .env
    sed -i "s/POSTGRES_USER=.*/POSTGRES_USER=netctrl/" .env
    sed -i "s/POSTGRES_PASSWORD=.*/POSTGRES_PASSWORD=$db_password/" .env
    sed -i "s/POSTGRES_HOST=.*/POSTGRES_HOST=db/" .env
    sed -i "s/POSTGRES_PORT=.*/POSTGRES_PORT=5432/" .env
    sed -i "s/DJANGO_SECRET_KEY=.*/DJANGO_SECRET_KEY=$secret_key/" .env
    sed -i "s/DJANGO_DEBUG=.*/DJANGO_DEBUG=False/" .env
    sed -i "s/DJANGO_ALLOWED_HOSTS=.*/DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0,172.16.0.0\/12,192.168.0.0\/16/" .env
    sed -i "s|STATIC_ROOT=.*|STATIC_ROOT=/opt/static|" .env
    sed -i "s|MEDIA_ROOT=.*|MEDIA_ROOT=/opt/media|" .env
    sed -i "s|LOG_DIR=.*|LOG_DIR=/opt/logs|" .env

    echo "Environment file created with secure defaults"
    echo "Database password: $db_password"
    echo "Please save these credentials securely"
fi

echo "Setup completed successfully!"
echo "Please log out and log back in for docker group membership to take effect."
echo "Then run: ./deploy.sh to deploy the application."
