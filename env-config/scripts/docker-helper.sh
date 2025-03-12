#!/bin/bash
# Docker Helper Functions
# Provides standardized Docker command functions using modern syntax

# Text colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

# Root directory
ROOT_DIR=$(cd "$(dirname "$0")/../.." && pwd)

# Helper function for standard docker compose commands
# Usage: docker_cmd up -d
docker_cmd() {
    echo -e "${YELLOW}Executing: docker compose $*${NC}"
    docker compose "$@"
}

# Helper function to start containers
# Usage: docker_start
docker_start() {
    echo -e "${GREEN}Starting containers...${NC}"
    docker_cmd up -d
    echo -e "${GREEN}Containers started successfully${NC}"
}

# Helper function to stop containers
# Usage: docker_stop
docker_stop() {
    echo -e "${YELLOW}Stopping containers...${NC}"
    docker_cmd down
    echo -e "${GREEN}Containers stopped successfully${NC}"
}

# Helper function to stop containers and remove orphans
# Usage: docker_clean
docker_clean() {
    echo -e "${YELLOW}Stopping containers and removing orphans...${NC}"
    docker_cmd down --remove-orphans
    echo -e "${GREEN}Containers stopped and orphans removed successfully${NC}"
}

# Helper function to view container logs
# Usage: docker_logs [service_name]
docker_logs() {
    local service=$1
    if [ -z "$service" ]; then
        echo -e "${YELLOW}Viewing logs for all services...${NC}"
        docker_cmd logs
    else
        echo -e "${YELLOW}Viewing logs for ${service}...${NC}"
        docker_cmd logs "$service"
    fi
}

# Helper function to check container status
# Usage: docker_status
docker_status() {
    echo -e "${YELLOW}Checking container status...${NC}"
    docker_cmd ps
}

# Helper function to rebuild a service
# Usage: docker_rebuild [service_name]
docker_rebuild() {
    local service=$1
    if [ -z "$service" ]; then
        echo -e "${RED}Error: Service name required${NC}"
        echo -e "Usage: docker_rebuild [service_name]"
        return 1
    fi
    
    echo -e "${YELLOW}Rebuilding ${service}...${NC}"
    docker_cmd build --no-cache "$service"
    echo -e "${GREEN}${service} rebuilt successfully${NC}"
}

# Display available commands
echo -e "${GREEN}Docker Helper Functions Available:${NC}"
echo -e "  ${YELLOW}docker_cmd${NC} - Run any docker compose command"
echo -e "  ${YELLOW}docker_start${NC} - Start all containers"
echo -e "  ${YELLOW}docker_stop${NC} - Stop all containers"
echo -e "  ${YELLOW}docker_clean${NC} - Stop all containers and remove orphans"
echo -e "  ${YELLOW}docker_logs${NC} - View container logs"
echo -e "  ${YELLOW}docker_status${NC} - Check container status"
echo -e "  ${YELLOW}docker_rebuild${NC} - Rebuild a specific service"
echo -e "\nExamples:"
echo -e "  ${YELLOW}source env-config/scripts/docker-helper.sh${NC}"
echo -e "  ${YELLOW}docker_start${NC}"
echo -e "  ${YELLOW}docker_logs backend${NC}"
