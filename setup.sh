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

# Install Docker
echo "Installing Docker..."
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install Docker Compose
echo "Installing Docker Compose..."
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Add current user to docker group
echo "Adding user to docker group..."
sudo usermod -aG docker $USER

# Create required directories
echo "Creating project directories..."
sudo mkdir -p /opt/netctrl/{static,media,certs}
sudo chown -R $USER:$USER /opt/netctrl

# Generate self-signed SSL certificate (for development)
echo "Generating self-signed SSL certificate..."
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /opt/netctrl/certs/privkey.pem \
    -out /opt/netctrl/certs/fullchain.pem \
    -subj "/C=US/ST=State/L=City/O=Organization/CN=localhost"

echo "Setup completed successfully!"
echo "Please log out and log back in for docker group membership to take effect."
echo "Then run: ./deploy.sh to deploy the application."
