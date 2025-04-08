"""
Dashboard views for the CMS application.

This module defines views for the dashboard, including:
- Main dashboard with system statistics
- Activity tracking
- Storage usage information
"""

import logging
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Sum, Q
from django.utils import timezone
from datetime import timedelta

from ..models.documents import Document, DocumentVersion, DocumentFile
from ..models.files import File
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


class DashboardView(LoginRequiredMixin, TemplateView):
    """Main dashboard view with system statistics."""
    template_name = 'cms/dashboard.html'
    
    def get_context_data(self, **kwargs):
        """Add statistics to context."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dashboard'
        
        # Current user's statistics
        user = self.request.user
        context['user_documents'] = Document.objects.filter(author=user).count()
        context['user_files'] = File.objects.filter(uploaded_by=user).count()
        
        # Calculate user's storage usage
        user_file_size = File.objects.filter(uploaded_by=user).aggregate(
            total=Sum('file_size')
        )['total'] or 0
        context['user_storage'] = self._format_file_size(user_file_size)
        
        # Get total counts
        context['total_documents'] = Document.objects.count()
        context['total_files'] = File.objects.count()
        context['total_users'] = User.objects.filter(is_active=True).count()
        
        # Calculate total storage usage
        total_size = File.objects.aggregate(total=Sum('file_size'))['total'] or 0
        context['total_storage'] = self._format_file_size(total_size)
        
        # Get recent activity
        recent_date = timezone.now() - timedelta(days=7)
        context['recent_documents'] = Document.objects.filter(
            created_at__gte=recent_date
        ).order_by('-created_at')[:5]
        
        context['recent_files'] = File.objects.filter(
            uploaded_at__gte=recent_date
        ).order_by('-uploaded_at')[:5]
        
        # Get most viewed files
        context['popular_files'] = File.objects.order_by('-download_count')[:5]
        
        # Get file type distribution
        file_types = File.objects.values('mime_type').annotate(
            count=Count('id')
        ).order_by('-count')[:5]
        
        # Prettify mime types for display
        for ft in file_types:
            mime = ft['mime_type']
            if '/' in mime:
                ft['type_name'] = mime.split('/')[1].upper()
            else:
                ft['type_name'] = mime.upper()
        
        context['file_types'] = file_types
        
        # Get document statistics
        context['published_documents'] = Document.objects.filter(
            status='published'
        ).count()
        
        context['draft_documents'] = Document.objects.filter(
            status='draft'
        ).count()
        
        # Get activity over time (last 30 days)
        thirty_days_ago = timezone.now() - timedelta(days=30)
        daily_file_uploads = File.objects.filter(
            uploaded_at__gte=thirty_days_ago
        ).extra({
            'day': "date(uploaded_at)"
        }).values('day').annotate(count=Count('id')).order_by('day')
        
        context['daily_uploads'] = daily_file_uploads
        
        return context
    
    def _format_file_size(self, size_bytes):
        """Format file size in human-readable format."""
        if size_bytes < 1024:
            return f"{size_bytes} bytes"
        elif size_bytes < 1024 ** 2:
            return f"{size_bytes / 1024:.1f} KB"
        elif size_bytes < 1024 ** 3:
            return f"{size_bytes / (1024 ** 2):.1f} MB"
        else:
            return f"{size_bytes / (1024 ** 3):.2f} GB"
