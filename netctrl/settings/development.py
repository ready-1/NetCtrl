from .base import *  # Import all settings from base.py

# Development-specific settings
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'devsrvr']

# Example: Enable Django's built-in server to serve static files during development
STATICFILES_DIRS = [BASE_DIR / "static"]