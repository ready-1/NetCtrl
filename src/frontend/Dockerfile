FROM node:18-alpine

# Build arguments for local package repository (air-gapped operation)
ARG NPM_REGISTRY=http://localhost:4873
ARG NODE_ENV=development

# Set environment variables
ENV NODE_ENV=${NODE_ENV} \
    NPM_CONFIG_REGISTRY=${NPM_REGISTRY} \
    REACT_APP_API_URL=http://localhost/api

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apk add --no-cache curl

# Copy package files
COPY package.json package-lock.json* ./

# Configure npm to use local registry and install dependencies
RUN echo "registry=${NPM_REGISTRY}" > .npmrc && \
    npm ci

# Copy application code
COPY . .

# Create directory for Material UI local files
RUN mkdir -p /app/public/static/material-ui

# Build the application for production
RUN if [ "$NODE_ENV" = "production" ]; then \
      npm run build; \
    fi

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:3000/health || exit 1

# Start application
CMD ["npm", "start"]
