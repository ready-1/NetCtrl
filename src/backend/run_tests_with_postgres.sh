#!/bin/bash
# Run tests with PostgreSQL

# Start PostgreSQL container for testing
echo "Starting PostgreSQL container for testing..."
docker compose -f docker-compose.test.yml up test_db -d

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL to be ready..."
sleep 5

# Set environment variables
export TEST_WITH_POSTGRES=1
export POSTGRES_SERVER=localhost
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=postgres
export POSTGRES_DB=test_netctrl
export POSTGRES_PORT=5433

# Run tests
echo "Running tests with PostgreSQL..."
python -m pytest app/tests/ -v

# Clean up
echo "Cleaning up test containers..."
docker compose -f docker-compose.test.yml down
