FROM alpine:3.18

# Install rsyslog and other dependencies
RUN apk add --no-cache \
    rsyslog \
    curl \
    tzdata \
    bash \
    logrotate

# Set working directory
WORKDIR /etc/rsyslog.d

# Copy rsyslog configuration
COPY rsyslog.conf /etc/rsyslog.conf
COPY logrotate.conf /etc/logrotate.d/cms-logs

# Create log directories with proper permissions
RUN mkdir -p /var/log/cms /var/spool/rsyslog \
    && chown -R root:root /var/log/cms \
    && chmod -R 755 /var/log/cms

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expose syslog port
EXPOSE 514/udp 514/tcp

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD ps aux | grep rsyslog | grep -v grep || exit 1

# Start rsyslog
ENTRYPOINT ["/entrypoint.sh"]
