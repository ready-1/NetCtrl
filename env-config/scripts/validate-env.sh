#!/bin/bash
# Environment Variable Validation Script
# Checks if all required environment variables are set correctly

set -e

# Text colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

# Main .env file location (parent directory)
MAIN_ENV_FILE="../.env"

# Function to check if a variable is set in the .env file
check_var() {
  local var_name=$1
  local env_file=$2
  local required=$3
  
  if grep -q "^${var_name}=" "$env_file"; then
    local var_value=$(grep "^${var_name}=" "$env_file" | cut -d '=' -f2-)
    if [[ -z "$var_value" ]]; then
      if [[ "$required" == "true" ]]; then
        echo -e "${RED}ERROR: ${var_name} is empty in ${env_file}${NC}"
        return 1
      else
        echo -e "${YELLOW}WARNING: ${var_name} is empty in ${env_file}${NC}"
        return 0
      fi
    else
      # Variable is set and has a value
      echo -e "${GREEN}OK: ${var_name} is set in ${env_file}${NC}"
      return 0
    fi
  else
    if [[ "$required" == "true" ]]; then
      echo -e "${RED}ERROR: ${var_name} is missing from ${env_file}${NC}"
      return 1
    else
      echo -e "${YELLOW}WARNING: ${var_name} is missing from ${env_file}${NC}"
      return 0
    fi
  fi
}

# Function to check service-specific env files
check_service_env() {
  local service=$1
  local env_file="../services/${service}/.env"
  
  if [[ ! -f "$env_file" ]]; then
    echo -e "${RED}ERROR: $env_file does not exist${NC}"
    return 1
  fi
  
  echo -e "\nChecking ${service} environment variables..."
  
  case "$service" in
    backend)
      # Required backend variables
      check_var "API_HOST" "$env_file" "true"
      check_var "API_PORT" "$env_file" "true"
      check_var "SECRET_KEY" "$env_file" "true"
      check_var "ALGORITHM" "$env_file" "true"
      check_var "ACCESS_TOKEN_EXPIRE_MINUTES" "$env_file" "true"
      check_var "DATABASE_URL" "$env_file" "true"
      # Optional variables
      check_var "PIP_INDEX_URL" "$env_file" "false"
      ;;
    database)
      # Required database variables
      check_var "POSTGRES_USER" "$env_file" "true"
      check_var "POSTGRES_PASSWORD" "$env_file" "true"
      check_var "POSTGRES_DB" "$env_file" "true"
      # Optional variables
      check_var "POSTGRES_MAX_CONNECTIONS" "$env_file" "false"
      ;;
    frontend)
      # Required frontend variables
      check_var "REACT_APP_API_URL" "$env_file" "true"
      check_var "NODE_ENV" "$env_file" "true"
      check_var "PORT" "$env_file" "true"
      # Optional variables
      check_var "NPM_REGISTRY" "$env_file" "false"
      ;;
    nginx)
      # Required nginx variables
      check_var "NGINX_PORT" "$env_file" "true"
      check_var "NGINX_MAX_BODY_SIZE" "$env_file" "true"
      check_var "API_HOST" "$env_file" "true"
      check_var "API_PORT" "$env_file" "true"
      check_var "FRONTEND_HOST" "$env_file" "true"
      check_var "FRONTEND_PORT" "$env_file" "true"
      ;;
    syslog)
      # Required syslog variables
      check_var "SYSLOG_HOST" "$env_file" "true"
      check_var "SYSLOG_PORT" "$env_file" "true"
      check_var "LOG_LEVEL" "$env_file" "true"
      ;;
    *)
      echo -e "${RED}ERROR: Unknown service: ${service}${NC}"
      return 1
      ;;
  esac
}

# Check if main .env file exists
if [[ ! -f "$MAIN_ENV_FILE" ]]; then
  echo -e "${RED}ERROR: Main .env file does not exist: $MAIN_ENV_FILE${NC}"
  echo -e "${YELLOW}Please copy .env.example to .env and fill in the values.${NC}"
  exit 1
fi

# Check main .env file variables
echo "Checking main environment variables..."
check_var "COMPOSE_PROJECT_NAME" "$MAIN_ENV_FILE" "true"
check_var "POSTGRES_USER" "$MAIN_ENV_FILE" "true"
check_var "POSTGRES_PASSWORD" "$MAIN_ENV_FILE" "true"
check_var "POSTGRES_DB" "$MAIN_ENV_FILE" "true"
check_var "SECRET_KEY" "$MAIN_ENV_FILE" "true"

# Check service-specific env files
for service in backend database frontend nginx syslog; do
  check_service_env "$service"
done

echo -e "\n${GREEN}Environment validation completed successfully!${NC}"

# Check for air-gapped operation settings
if grep -q "PIP_INDEX_URL" "$MAIN_ENV_FILE" && grep -q "NPM_REGISTRY" "$MAIN_ENV_FILE"; then
  echo -e "${GREEN}Air-gapped operation settings detected.${NC}"
else
  echo -e "${YELLOW}WARNING: Air-gapped operation settings incomplete.${NC}"
  echo -e "${YELLOW}Please ensure PIP_INDEX_URL and NPM_REGISTRY are properly configured for air-gapped operation.${NC}"
fi

exit 0
