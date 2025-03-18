#!/bin/bash
set -e

# Create uploads directory if it doesn't exist
mkdir -p /app/uploads
echo "Ensuring uploads directory exists at /app/uploads"
# Do not attempt chmod as it will fail with non-root user

# Apply database migrations
echo "Applying database migrations..."
alembic upgrade head

# Start the FastAPI application
echo "Starting FastAPI application..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
