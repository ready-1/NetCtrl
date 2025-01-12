"""
Application configuration for netdash app.
"""
from django.apps import AppConfig


class NetdashConfig(AppConfig):
    """Configuration for netdash app."""
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'netdash'
    verbose_name = 'Network Dashboard'
