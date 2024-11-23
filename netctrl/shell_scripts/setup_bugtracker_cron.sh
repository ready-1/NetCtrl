#!/bin/bash

# Constants
CRON_LOG="/var/log/bugtracker_cron.log"
SCRIPT_PATH="/srv/NetCtrl/netctrl/shell_scripts/process_bug_queue.py"
PYTHON_PATH="/usr/bin/python3"
LOGROTATE_CONF="/etc/logrotate.d/bugtracker_cron"

# Check if the Python script exists
if [ ! -f "$SCRIPT_PATH" ]; then
    echo "Error: Python script not found at $SCRIPT_PATH"
    exit 1
fi

# Ensure the cron log file exists
if [ ! -f "$CRON_LOG" ]; then
    sudo touch "$CRON_LOG"
    sudo chmod 664 "$CRON_LOG"
    echo "Created log file at $CRON_LOG"
fi

# Create or update the logrotate configuration
if [ ! -f "$LOGROTATE_CONF" ]; then
    echo "Creating logrotate configuration at $LOGROTATE_CONF"
    sudo bash -c "cat > $LOGROTATE_CONF" <<EOL
$CRON_LOG {
    daily
    rotate 7
    compress
    missingok
    notifempty
    create 664 root root
    postrotate
        systemctl reload cron > /dev/null 2>&1 || true
    endscript
}
EOL
    echo "Logrotate configuration created."
else
    echo "Logrotate configuration already exists."
fi

# Create a temporary file for the crontab
TMP_CRON=$(mktemp)
crontab -l > "$TMP_CRON" 2>/dev/null || true

# Add the cron job if it doesn't already exist
if ! grep -q "$SCRIPT_PATH" "$TMP_CRON"; then
    echo "Adding cron job to process the bug queue..."
    echo "*/5 * * * * $PYTHON_PATH $SCRIPT_PATH >> $CRON_LOG 2>&1" >> "$TMP_CRON"
    crontab "$TMP_CRON"
    echo "Cron job added."
else
    echo "Cron job already exists."
fi

# Clean up temporary file
rm -f "$TMP_CRON"

# Verify the crontab
echo "Current crontab:"
crontab -l

echo "Setup complete. Logs will be written to $CRON_LOG and rotated daily."
