#!/bin/bash
# Reset database script for NetCtrl CMS
# This wrapper script detects the environment and runs the appropriate command

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${YELLOW}NetCtrl CMS Database Reset Tool${NC}"
echo "=================================="

# Function to check if we're running inside a Docker container
in_docker() {
    [ -f /.dockerenv ] || grep -q 'docker\|lxc' /proc/1/cgroup
}

# Function to check if Docker is available
has_docker() {
    command -v docker &> /dev/null
}

# Function to check if Docker Compose is available
has_docker_compose() {
    command -v docker compose &> /dev/null
}

# First, check where we're running from
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Ensure we're in the correct directory context
cd "$SCRIPT_DIR/.." || { echo -e "${RED}Error: Could not navigate to backend directory${NC}"; exit 1; }

if in_docker; then
    echo -e "${GREEN}Running inside Docker container${NC}"
    echo "Executing reset script directly..."
    python scripts/reset_db.py
elif has_docker_compose && [ -f "../docker-compose.yml" ]; then
    echo -e "${GREEN}Docker Compose detected${NC}"
    echo "Executing reset script via Docker Compose..."
    # Check if backend container is running
    if docker compose ps | grep -q backend; then
        docker compose exec backend python scripts/reset_db.py
    else
        echo -e "${YELLOW}Backend container is not running. Starting it temporarily...${NC}"
        docker compose run --rm backend python scripts/reset_db.py
    fi
elif has_docker && [ -f "Dockerfile" ]; then
    echo -e "${GREEN}Docker detected${NC}"
    echo "Executing reset script via Docker..."
    CONTAINER_NAME=$(docker ps --filter "name=backend" --format "{{.Names}}" | head -n1)
    if [ -n "$CONTAINER_NAME" ]; then
        docker exec -it "$CONTAINER_NAME" python scripts/reset_db.py
    else
        echo -e "${RED}Error: Backend container not found running${NC}"
        echo "Please start the containers first or use the local execution method"
        exit 1
    fi
else
    echo -e "${GREEN}Running locally${NC}"
    echo "Executing reset script directly..."
    echo -e "${YELLOW}Note: Make sure your database connection settings are correct${NC}"
    echo "You may need to set POSTGRES_SERVER=localhost if connecting to a Docker database"
    
    # Check if Python is available
    if command -v python3 &> /dev/null; then
        python3 scripts/reset_db.py
    elif command -v python &> /dev/null; then
        python scripts/reset_db.py
    else
        echo -e "${RED}Error: Python not found${NC}"
        exit 1
    fi
fi

echo "=================================="
echo -e "${GREEN}Database reset operation completed${NC}"
echo "You should now be able to log in with:"
echo "  Username: admin"
echo "  Password: admin"
