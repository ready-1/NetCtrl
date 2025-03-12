FROM python:3.11-slim

# Build arguments for local package repository (air-gapped operation)
ARG PIP_INDEX_URL=http://localhost:3141/simple
ARG PIP_TRUSTED_HOST=localhost

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_INDEX_URL=${PIP_INDEX_URL} \
    PIP_TRUSTED_HOST=${PIP_TRUSTED_HOST}

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    netcat-openbsd \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt /app/

# Install Python dependencies
# For initial builds, use the public PyPI repository to ensure successful installation
# In production, the containers will use the local mirror as configured in docker-compose.yml
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --index-url https://pypi.org/simple -r requirements.txt

# Copy application code
COPY . /app/

# Create directories for uploads and data
RUN mkdir -p /app/uploads /app/data

# Script to wait for database before starting app
COPY ./scripts/start.sh /app/scripts/
RUN chmod +x /app/scripts/start.sh

# Set proper permissions
RUN chown -R www-data:www-data /app

# Run as non-root user
USER www-data

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Start application
CMD ["/app/scripts/start.sh"]
