FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY flask_app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir flask flask-sqlalchemy flask-migrate flask-jwt-extended flask-cors celery psycopg2

# Copy application code
COPY . .

# Copy openapi_client directory
COPY openapi_client/ /app/openapi_client/

# Create shared files directory with appropriate permissions
RUN mkdir -p /app/shared_files && chmod 777 /app/shared_files

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
