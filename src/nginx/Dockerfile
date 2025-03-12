FROM nginx:1.25-alpine

# Install dependencies
RUN apk add --no-cache bash curl envsubst

# Copy default configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
    CMD curl -f http://localhost/health || exit 1

# Copy entrypoint script
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Create directories for static files and uploads
RUN mkdir -p /var/www/html/static /var/www/html/uploads \
    && chmod -R 755 /var/www/html

# Expose port
EXPOSE 80

# Use custom entrypoint to substitute environment variables
ENTRYPOINT ["/entrypoint.sh"]

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
