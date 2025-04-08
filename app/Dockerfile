FROM python:3.9-slim

WORKDIR /srv/NetCtrl

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories for static/media files
RUN mkdir -p /srv/NetCtrl/static /srv/NetCtrl/media

# Configure logging to syslog
ENV PYTHONUNBUFFERED=1

# Command to run
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
