#!/bin/bash
# Environment Initialization Script
# Copies .env.example files to .env files for each service

set -e

# Text colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

# Root directory
ROOT_DIR=$(cd "$(dirname "$0")/../.." && pwd)
ENV_CONFIG_DIR="${ROOT_DIR}/env-config"

echo -e "${GREEN}CMS with RBAC - Environment Initialization${NC}"
echo "This script will create .env files from .env.example templates."
echo "Working directory: ${ROOT_DIR}"

# Create main .env file if it doesn't exist
if [ ! -f "${ENV_CONFIG_DIR}/.env" ]; then
  echo -e "\n${YELLOW}Creating main .env file...${NC}"
  cp "${ENV_CONFIG_DIR}/.env.example" "${ENV_CONFIG_DIR}/.env"
  echo -e "${GREEN}Created ${ENV_CONFIG_DIR}/.env${NC}"
else
  echo -e "\n${YELLOW}Main .env file already exists. Skipping.${NC}"
  echo "If you want to reset it, please delete the file and run this script again."
fi

# Services to initialize
services=("backend" "database" "frontend" "nginx" "syslog")

# Create service-specific .env files
for service in "${services[@]}"; do
  service_dir="${ENV_CONFIG_DIR}/services/${service}"
  
  if [ ! -f "${service_dir}/.env" ]; then
    echo -e "\n${YELLOW}Creating ${service} .env file...${NC}"
    cp "${service_dir}/.env.example" "${service_dir}/.env"
    echo -e "${GREEN}Created ${service_dir}/.env${NC}"
  else
    echo -e "\n${YELLOW}${service} .env file already exists. Skipping.${NC}"
  fi
done

# Create gitignore for env files if it doesn't exist
if [ ! -f "${ENV_CONFIG_DIR}/.gitignore" ]; then
  echo -e "\n${YELLOW}Creating .gitignore for environment files...${NC}"
  cat > "${ENV_CONFIG_DIR}/.gitignore" << EOF
# Ignore all .env files (contain sensitive information)
.env
services/*/.env
EOF
  echo -e "${GREEN}Created ${ENV_CONFIG_DIR}/.gitignore${NC}"
fi

echo -e "\n${GREEN}Environment initialization complete!${NC}"
echo -e "Next steps:"
echo -e "1. Edit the .env files with your specific configuration values"
echo -e "2. Run ${YELLOW}env-config/scripts/validate-env.sh${NC} to verify your configuration"
echo -e "3. Start the containers with ${YELLOW}docker-compose up -d${NC}"
