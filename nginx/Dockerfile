FROM nginx:stable-alpine

# Remove default Nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom Nginx configuration
COPY conf/ /etc/nginx/conf.d/

# Create directory for SSL certificates (for production)
RUN mkdir -p /etc/nginx/ssl

# Create directory for frontend static files
RUN mkdir -p /usr/share/nginx/html

# Expose ports
EXPOSE 80
EXPOSE 443

# Start Nginx when the container launches
CMD ["nginx", "-g", "daemon off;"]
