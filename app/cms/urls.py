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

# File upload URLs
file_upload_urls = [
    # Upload form views - advanced, simple, and debug
    path('new/', views.uploads.FileUploadView.as_view(), name='file_upload'),
    path('simple/', views.uploads.SimpleFileUploadView.as_view(), name='file_upload_simple'),
    path('debug/', views.uploads.FileUploadDebugView.as_view(), name='file_upload_debug'),
    
    # API endpoints for chunked upload
    path('api/chunked_upload/', views.uploads.FileChunkedUploadView.as_view(), 
         name='api_chunked_upload'),
    path('api/chunked_upload_complete/', views.uploads.FileChunkedUploadCompleteView.as_view(), 
         name='api_chunked_upload_complete'),
]

# File management URLs
file_urls = [
    # File list with search and filtering
    path('', views.files.FileListView.as_view(), name='file_list'),
    
    # File detail, download, edit and delete
    path('<uuid:uuid>/', views.files.FileDetailView.as_view(), name='file_detail'),
    path('<uuid:uuid>/download/', views.files.FileDownloadView.as_view(), name='file_download'),
    path('<uuid:uuid>/edit/', views.files.FileEditView.as_view(), name='file_edit'),
    path('<uuid:uuid>/delete/', views.files.FileDeleteView.as_view(), name='file_delete'),
    
    # File upload (includes chunked upload)
    path('upload/', include(file_upload_urls)),
]

urlpatterns = [
    # Dashboard view
    path('dashboard/', login_required(TemplateView.as_view(
        template_name='cms/dashboard.html',
        extra_context={'title': 'Dashboard'}
    )), name='dashboard'),
    
    # Document URLs (will be implemented in next phase)
    path('documents/', login_required(TemplateView.as_view(
        template_name='cms/document_list.html',
        extra_context={'title': 'Documents'}
    )), name='document_list'),
    
    # File management URLs
    path('files/', include(file_urls)),
    
    # User profile (will be implemented in next phase)
    path('profile/', login_required(TemplateView.as_view(
        template_name='cms/profile.html',
        extra_context={'title': 'User Profile'}
    )), name='user_profile'),
    
    # Landing page
    path('', TemplateView.as_view(
        template_name='cms/landing.html',
        extra_context={'title': 'Welcome to NetCtrl CMS'}
    ), name='landing'),
]
