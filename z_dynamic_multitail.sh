#!/bin/bash

# Name of the container to monitor
CONTAINER="db"

# Function to handle cleanup
cleanup() {
  echo "Cleaning up..."
  pkill -f "docker logs -f $CONTAINER" 2>/dev/null
  exit 0
}
trap cleanup SIGINT SIGTERM

# Ensure the container is running
if ! docker ps --format '{{.Names}}' | grep -q "^$CONTAINER$"; then
  echo "Container $CONTAINER is not running."
  exit 1
fi

# Stream logs from the container with improved formatting
echo "Starting log stream for container: $CONTAINER"
docker logs -f "$CONTAINER" 2>&1 | awk -v container="$CONTAINER" '
{
  gsub(/\r/, "");                   # Remove carriage returns
  printf "[%-10s] %s\n", container, $0
  fflush()
}' | fold -s -w 80                 # Wrap long lines to fit the terminal width