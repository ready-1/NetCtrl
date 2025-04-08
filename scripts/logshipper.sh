#!/bin/sh

# Log shipper script that tails log files and outputs them to stdout
# This makes the logs visible to Dozzle as container logs

# Set up continuous loop to tail all log files
while true; do
  echo "Starting log shipping..."
  
  # Tail all available log files
  tail -f /var/log/all.log /var/log/nginx.log /var/log/django.log /var/log/postgres.log /var/log/errors.log 2>/dev/null
  
  # If tail exits for some reason, wait a bit and restart
  echo "Log tail exited, restarting in 5 seconds..."
  sleep 5
done
