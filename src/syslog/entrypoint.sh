#!/bin/bash
set -e

# Default environment variables
: ${SYSLOG_PORT:=514}
: ${LOG_LEVEL:=info}
: ${LOG_FORMAT:=json}
: ${RETENTION_DAYS:=30}
: ${LOG_STORAGE_PATH:=/var/log/cms}

echo "Starting syslog service with the following configuration:"
echo "  Port: $SYSLOG_PORT"
echo "  Log Level: $LOG_LEVEL"
echo "  Log Format: $LOG_FORMAT"
echo "  Retention Days: $RETENTION_DAYS"
echo "  Storage Path: $LOG_STORAGE_PATH"

# Ensure log directory exists with proper permissions
mkdir -p ${LOG_STORAGE_PATH}
chmod -R 755 ${LOG_STORAGE_PATH}

# Update logrotate configuration with environment variables
sed -i "s/rotate 30/rotate ${RETENTION_DAYS}/g" /etc/logrotate.d/cms-logs

# Set up a cron job for log rotation
echo "0 0 * * * /usr/sbin/logrotate /etc/logrotate.d/cms-logs" > /var/spool/cron/crontabs/root
chmod 600 /var/spool/cron/crontabs/root

# Start cron daemon
crond -b -L /var/log/cron.log

# Run rsyslogd in the foreground
echo "Starting rsyslogd..."
exec /usr/sbin/rsyslogd -n
