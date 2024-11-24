from .base import *  # Import all settings from base.py
import os

# Development-specific settings
DEBUG = True
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',') or ['localhost', '127.0.0.1']

# Example: Enable Django's built-in server to serve static files during development
STATICFILES_DIRS = [BASE_DIR / "static"]