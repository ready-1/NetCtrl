#!/bin/bash
set -e

# Default environment variables
: ${NGINX_HOST:=localhost}
: ${NGINX_PORT:=80}
: ${API_HOST:=backend}
: ${API_PORT:=8000}
: ${FRONTEND_HOST:=frontend}
: ${FRONTEND_PORT:=3000}
: ${NGINX_MAX_BODY_SIZE:=2048M}

# Process templates
echo "Processing NGINX configuration templates..."

# Replace environment variables in all .template files and output to .conf
for template in /etc/nginx/templates/*.template; do
  if [ -f "$template" ]; then
    output_path="/etc/nginx/conf.d/$(basename ${template%.template}.conf)"
    echo "Generating $output_path from template $template..."
    envsubst '${NGINX_HOST},${NGINX_PORT},${API_HOST},${API_PORT},${FRONTEND_HOST},${FRONTEND_PORT},${NGINX_MAX_BODY_SIZE}' < "$template" > "$output_path"
  fi
done

# Create health check endpoint
cat > /etc/nginx/conf.d/health.conf << EOF
server {
    listen 80;
    server_name localhost;
    
    location /health {
        access_log off;
        add_header Content-Type text/plain;
        return 200 'NGINX is healthy';
    }
}
EOF

echo "NGINX configuration complete. Starting server..."

# Start NGINX
exec "$@"
