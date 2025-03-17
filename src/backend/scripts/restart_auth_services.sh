#!/bin/bash
# Restart script for authentication-related services

echo "Restarting backend and nginx services to apply authentication system changes..."

# Make a backup of current configuration
echo "Creating backup of current configuration..."
mkdir -p src/backend/backups/auth_refactor
cp src/backend/app/main.py src/backend/backups/auth_refactor/
cp src/nginx/conf/default.conf src/backend/backups/auth_refactor/

# Restart services
echo "Restarting backend and nginx services..."
docker compose restart backend nginx

# Check service status
echo "Checking service status..."
docker compose ps backend nginx

echo "Waiting for services to be ready..."
sleep 5

# Test authentication endpoint
echo "Testing authentication endpoint..."
STATUS=$(curl -s -o /dev/null -w "%{http_code}" -X POST "http://localhost/api/v1/jwt/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=admin&grant_type=password")

if [ $STATUS -eq 200 ]; then
  echo "✅ Authentication endpoint working correctly (HTTP 200)"
elif [ $STATUS -eq 400 ]; then
  echo "⚠️ Authentication endpoint returned HTTP 400 - possibly incorrect credentials but endpoint is accessible"
  echo "Try running: docker compose exec backend python scripts/reset_admin_password.py admin"
else
  echo "❌ Authentication endpoint error (HTTP $STATUS)"
  echo "For troubleshooting, run: docker compose exec backend python scripts/auth_diagnostics.py health-check"
fi

echo "For comprehensive authentication testing, use the new diagnostics tool:"
echo "docker compose exec backend python scripts/auth_diagnostics.py health-check"

echo ""
echo "Restart completed."
