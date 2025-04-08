"""
URL patterns for the Network application.

This module defines all URL patterns for the Network application.
Currently these are placeholders that will be implemented in future phases.
"""

from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

app_name = 'network'

urlpatterns = [
    # Main network dashboard (placeholder)
    path('', login_required(TemplateView.as_view(
        template_name='network/index.html',
        extra_context={'title': 'Network Management'}
    )), name='index'),
    
    # Placeholder for network monitoring
    path('monitoring/', login_required(TemplateView.as_view(
        template_name='network/monitoring.html',
        extra_context={'title': 'Network Monitoring'}
    )), name='monitoring'),
    
    # Placeholder for device management
    path('devices/', login_required(TemplateView.as_view(
        template_name='network/devices.html',
        extra_context={'title': 'Network Devices'}
    )), name='devices'),
]
