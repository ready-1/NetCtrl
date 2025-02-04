#!/bin/bash

# Exit on error
set -e

echo "Starting system cleanup..."

# Remove Kubernetes repositories if they exist
echo "Removing Kubernetes repositories..."
sudo rm -f /etc/apt/sources.list.d/kubernetes.list
sudo rm -f /etc/apt/sources.list.d/kubernetes.list.save

# Clean apt lists and cache
echo "Cleaning package manager cache..."
sudo rm -rf /var/lib/apt/lists/*
sudo apt-get clean

# Update package lists
echo "Updating package lists..."
sudo apt-get update

# Clean up any failed Docker installations
echo "Cleaning up Docker (if exists)..."
if command -v docker &> /dev/null; then
    echo "Stopping Docker containers..."
    docker stop $(docker ps -aq) 2>/dev/null || true
    echo "Removing Docker containers..."
    docker rm $(docker ps -aq) 2>/dev/null || true
    echo "Removing Docker volumes..."
    docker volume rm $(docker volume ls -q) 2>/dev/null || true
fi

# Clean up old installation directories
echo "Cleaning up old installation directories..."
if [ -d "/opt/netctrl" ]; then
    echo "Removing old /opt/netctrl directory..."
    sudo rm -rf /opt/netctrl
fi

echo "System cleanup completed successfully!"
echo "You can now run setup.sh to install the application."
