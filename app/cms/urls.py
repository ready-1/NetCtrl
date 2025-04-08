"""
URL patterns for the CMS application.

This module defines all URL patterns for the CMS application, including:
- Dashboard views
- Document views (list, detail, create, edit, delete)
- File management views (upload, download, list, delete)
- User profile views
- Category and tag views
"""

from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'cms'

# URLs for the chunked upload functionality - will implement in the next phase
chunked_upload_urls = [
    # Custom URLs for chunked upload will be defined here
    path('chunked_upload/', TemplateView.as_view(
        template_name='cms/placeholder.html',
        extra_context={'title': 'File Upload'}
    ), name='chunked_upload'),
]

urlpatterns = [
    # Dashboard (temporary placeholder views)
    path('dashboard/', login_required(TemplateView.as_view(
        template_name='cms/dashboard.html',
        extra_context={'title': 'Dashboard'}
    )), name='dashboard'),
    
    # Placeholder for document URLs (will be implemented in next phase)
    path('documents/', login_required(TemplateView.as_view(
        template_name='cms/document_list.html',
        extra_context={'title': 'Documents'}
    )), name='document_list'),
    
    # Placeholder for file management URLs (will be implemented in next phase)
    path('files/', login_required(TemplateView.as_view(
        template_name='cms/file_list.html',
        extra_context={'title': 'Files'}
    )), name='file_list'),
    
    # Placeholder for user profile URLs (will be implemented in next phase)
    path('profile/', login_required(TemplateView.as_view(
        template_name='cms/profile.html',
        extra_context={'title': 'User Profile'}
    )), name='user_profile'),
    
    # Chunked upload URLs
    path('uploads/', include(chunked_upload_urls)),
    
    # Landing page (will redirect to dashboard if logged in)
    path('', TemplateView.as_view(
        template_name='cms/landing.html',
        extra_context={'title': 'Welcome to NetCtrl CMS'}
    ), name='landing'),
]
