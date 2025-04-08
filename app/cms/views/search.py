"""
Search views for the CMS application.

This module defines views for searching across the CMS:
- Global search across files and documents
- Advanced search with filtering
"""

import logging
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render

from ..models.documents import Document, Category, Tag
from ..models.files import File, FileCategory, FileTag

logger = logging.getLogger(__name__)


class SearchView(LoginRequiredMixin, ListView):
    """View for searching across files and documents."""
    template_name = 'cms/search_results.html'
    context_object_name = 'results'
    paginate_by = 20
    
    def get_queryset(self):
        """Get search results based on query parameters."""
        # Get search parameters from request
        query = self.request.GET.get('q', '').strip()
        search_type = self.request.GET.get('type', 'all')
        category = self.request.GET.get('category', '')
        tag = self.request.GET.get('tag', '')
        date_from = self.request.GET.get('date_from', '')
        date_to = self.request.GET.get('date_to', '')
        
        # Log search query
        logger.info(f"Search query: '{query}' (type: {search_type}) by user {self.request.user.username}")
        
        # Return empty queryset if no query
        if not query and not category and not tag and not date_from and not date_to:
            return []
        
        # Initialize querysets
        document_results = Document.objects.all()
        file_results = File.objects.all()
        
        # Apply text search if query exists
        if query:
            # Document search
            document_results = document_results.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(excerpt__icontains=query)
            )
            
            # File search
            file_results = file_results.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(original_filename__icontains=query)
            )
        
        # Filter by category
        if category:
            try:
                category_id = int(category)
                if search_type in ['all', 'documents']:
                    document_results = document_results.filter(category_id=category_id)
                if search_type in ['all', 'files']:
                    file_results = file_results.filter(category_id=category_id)
            except (ValueError, TypeError):
                logger.warning(f"Invalid category ID in search: {category}")
        
        # Filter by tag
        if tag:
            try:
                tag_id = int(tag)
                if search_type in ['all', 'documents']:
                    document_results = document_results.filter(tags__id=tag_id)
                if search_type in ['all', 'files']:
                    file_results = file_results.filter(tags__id=tag_id)
            except (ValueError, TypeError):
                logger.warning(f"Invalid tag ID in search: {tag}")
        
        # Filter by date range
        if date_from:
            if search_type in ['all', 'documents']:
                document_results = document_results.filter(created_at__gte=date_from)
            if search_type in ['all', 'files']:
                file_results = file_results.filter(uploaded_at__gte=date_from)
        
        if date_to:
            if search_type in ['all', 'documents']:
                document_results = document_results.filter(created_at__lte=date_to)
            if search_type in ['all', 'files']:
                file_results = file_results.filter(uploaded_at__lte=date_to)
        
        # Combine results based on search type
        if search_type == 'documents':
            # Add type flag for template rendering
            for doc in document_results:
                doc.result_type = 'document'
            return document_results
            
        elif search_type == 'files':
            # Add type flag for template rendering
            for file in file_results:
                file.result_type = 'file'
            return file_results
            
        else:  # 'all'
            # Add type flags for combined results
            for doc in document_results:
                doc.result_type = 'document'
            for file in file_results:
                file.result_type = 'file'
            
            # Combine querysets - this returns a list, not a queryset
            combined_results = list(document_results) + list(file_results)
            
            # Sort combined results by date (newest first)
            # This is a simple approach; for more complex sorting we'd use a different method
            combined_results.sort(
                key=lambda x: x.created_at if hasattr(x, 'created_at') else x.uploaded_at, 
                reverse=True
            )
            
            return combined_results
    
    def get_context_data(self, **kwargs):
        """Add search filters to context."""
        context = super().get_context_data(**kwargs)
        
        # Add search parameters to context
        context['query'] = self.request.GET.get('q', '')
        context['search_type'] = self.request.GET.get('type', 'all')
        context['selected_category'] = self.request.GET.get('category', '')
        context['selected_tag'] = self.request.GET.get('tag', '')
        context['date_from'] = self.request.GET.get('date_from', '')
        context['date_to'] = self.request.GET.get('date_to', '')
        
        # Add filter options
        context['document_categories'] = Category.objects.all()
        context['file_categories'] = FileCategory.objects.all()
        context['document_tags'] = Tag.objects.all()
        context['file_tags'] = FileTag.objects.all()
        
        # Add title
        context['title'] = 'Search Results'
        
        return context
