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

# Get absolute path to source directory
SOURCE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
APP_DIR="/opt/netctrl/app"

echo "Setting up application in ${APP_DIR}..."

# Clone repository if not exists
if [ ! -d "${APP_DIR}/.git" ]; then
    echo "Cloning repository..."
    git clone "${SOURCE_DIR}" "${APP_DIR}"
    cd "${APP_DIR}"

    # Copy deployment files
    echo "Setting up deployment files..."
    cp "${SOURCE_DIR}/deploy.sh" .
    chmod +x deploy.sh
fi

echo "Setup completed successfully!"
echo "Please log out and log back in for docker group membership to take effect."
echo "Then run: ./deploy.sh to deploy the application."
