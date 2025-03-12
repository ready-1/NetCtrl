FROM nginx:alpine

# Create necessary directories
RUN mkdir -p /usr/share/nginx/html/static/assets/css \
             /usr/share/nginx/html/static/assets/js \
             /usr/share/nginx/html/static/error

# Configure NGINX
COPY standalone/nginx.conf /etc/nginx/conf.d/default.conf

# Copy static files
COPY static/index.html /usr/share/nginx/html/static/
COPY static/assets/css/custom.css /usr/share/nginx/html/static/assets/css/
COPY static/assets/js/app.js /usr/share/nginx/html/static/assets/js/
COPY static/error/*.html /usr/share/nginx/html/static/error/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
