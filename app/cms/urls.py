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
    path('dashboard/', views.dashboard.DashboardView.as_view(), name='dashboard'),
    
    # Search view
    path('search/', views.search.SearchView.as_view(), name='search'),
    
    # Document management URLs
    path('documents/', include([
        # Document list with search and filtering
        path('', views.documents.DocumentListView.as_view(), name='document_list'),
        
        # Document CRUD operations
        path('create/', views.documents.DocumentCreateView.as_view(), name='document_create'),
        path('<slug:slug>/', views.documents.DocumentDetailView.as_view(), name='document_detail'),
        path('<slug:slug>/edit/', views.documents.DocumentUpdateView.as_view(), name='document_update'),
        path('<slug:slug>/delete/', views.documents.DocumentDeleteView.as_view(), name='document_delete'),
        
        # Document version management
        path('<slug:slug>/versions/', views.documents.DocumentVersionListView.as_view(), name='document_versions'),
        path('<slug:slug>/versions/create/', views.documents.DocumentVersionCreateView.as_view(), name='document_version_create'),
        path('<slug:slug>/versions/<int:version>/', views.documents.DocumentVersionDetailView.as_view(), name='document_version_detail'),
        path('<slug:slug>/versions/<int:version>/promote/', views.documents.DocumentVersionPromoteView.as_view(), name='document_version_promote'),
        
        # Document file management
        path('<slug:slug>/files/', views.documents.DocumentFileListView.as_view(), name='document_files'),
        path('<slug:slug>/files/add/', views.documents.DocumentFileAddView.as_view(), name='document_file_add'),
        path('<slug:slug>/files/<uuid:file_uuid>/remove/', views.documents.DocumentFileRemoveView.as_view(), name='document_file_remove'),
        path('<slug:slug>/files/reorder/', views.documents.DocumentFileReorderView.as_view(), name='document_file_reorder'),
    ])),
    
    # File management URLs
    path('files/', include(file_urls)),
    
    # Tag management URLs
    path('tags/', include([
        path('', views.taxonomy.TagListView.as_view(), name='tag_list'),
        path('create/', views.taxonomy.TagCreateView.as_view(), name='tag_create'),
        path('<slug:slug>/', views.taxonomy.TagDetailView.as_view(), name='tag_detail'),
        path('<slug:slug>/edit/', views.taxonomy.TagUpdateView.as_view(), name='tag_update'),
        path('<slug:slug>/delete/', views.taxonomy.TagDeleteView.as_view(), name='tag_delete'),
    ])),
    
    # Category management URLs
    path('categories/', include([
        path('', views.taxonomy.CategoryListView.as_view(), name='category_list'),
        path('create/', views.taxonomy.CategoryCreateView.as_view(), name='category_create'),
        path('<slug:slug>/', views.taxonomy.CategoryDetailView.as_view(), name='category_detail'),
        path('<slug:slug>/edit/', views.taxonomy.CategoryUpdateView.as_view(), name='category_update'),
        path('<slug:slug>/delete/', views.taxonomy.CategoryDeleteView.as_view(), name='category_delete'),
    ])),
    
    # User profile management
    path('profile/', views.users.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.users.ProfileUpdateView.as_view(), name='profile_edit'),
    path('profile/activity/', views.users.UserActivityView.as_view(), name='user_activity'),
    path('profile/password/', views.users.EnhancedPasswordChangeView.as_view(), name='password_change'),
    
    # Landing page
    path('', TemplateView.as_view(
        template_name='cms/landing.html',
        extra_context={'title': 'Welcome to NetCtrl CMS'}
    ), name='landing'),
]
