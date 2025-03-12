#!/bin/bash
set -e

# Environment variables that can be overridden
DB_HOST=${POSTGRES_HOST:-database}
DB_PORT=${POSTGRES_PORT:-5432}
APP_PORT=${API_PORT:-8000}
APP_HOST=${API_HOST:-0.0.0.0}
LOG_LEVEL=${LOG_LEVEL:-info}

# Function to check if the database is ready
wait_for_db() {
  echo "Waiting for database at ${DB_HOST}:${DB_PORT} to become available..."
  
  while ! nc -z ${DB_HOST} ${DB_PORT}; do
    echo "Database is unavailable - sleeping"
    sleep 2
  done
  
  echo "Database is up - executing migrations and starting application"
}

# Function to run database migrations
run_migrations() {
  echo "Running database migrations..."
  alembic upgrade head
  echo "Migrations completed successfully."
}

# Function to initialize superuser if it doesn't exist
init_superuser() {
  echo "Checking if superuser needs to be created..."
  python -m app.initial_setup
  echo "Superuser check completed."
}

# Main execution
echo "Starting backend service in $(hostname) container..."
echo "Environment: $NODE_ENV"

# Wait for database to be ready
wait_for_db

# Create database tables (on first run)
run_migrations

# Initialize superuser (if needed)
init_superuser

# Start the FastAPI application with Uvicorn
echo "Starting FastAPI application on ${APP_HOST}:${APP_PORT}"
exec uvicorn app.main:app --host ${APP_HOST} --port ${APP_PORT} --log-level ${LOG_LEVEL}
