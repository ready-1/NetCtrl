"""
Content-focused views for the CMS application.

This module defines views for a user-friendly, content-focused browsing experience:
- ContentListView: A wiki-like content library for browsing published documents
- ContentDetailView: A reader-optimized view that puts content front and center
"""

import logging
from django.views.generic import ListView, DetailView
from django.db.models import Q, Count
from django.shortcuts import get_object_or_404
from django.http import Http404

from ..models.documents import Document, Category, Tag

logger = logging.getLogger(__name__)

class ContentListView(ListView):
    """Content-focused view of published documents."""
    model = Document
    template_name = 'cms/content_list.html'
    context_object_name = 'documents'
    paginate_by = 12  # More documents per page for content browsing
    
    def get_queryset(self):
        """Filter for published documents only."""
        # Base queryset - only published documents
        queryset = Document.objects.filter(status='published')
        
        # Select related fields to reduce database queries
        queryset = queryset.select_related('author', 'category')
        
        # Category filtering
        category_id = self.request.GET.get('category')
        if category_id:
            try:
                queryset = queryset.filter(category_id=int(category_id))
            except (ValueError, TypeError):
                logger.warning(f"Invalid category_id filter: {category_id}")
        
        # Tag filtering
        tag_id = self.request.GET.get('tag')
        if tag_id:
            try:
                queryset = queryset.filter(tags__id=int(tag_id))
            except (ValueError, TypeError):
                logger.warning(f"Invalid tag_id filter: {tag_id}")
        
        # Search functionality with sanitized inputs
        query = self.request.GET.get('q', '').strip()
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | 
                Q(excerpt__icontains=query)
            ).distinct()
        
        return queryset
    
    def get_context_data(self, **kwargs):
        """Add categories, tags, and search context."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Content Library'
        
        # Get categories with document counts
        context['categories'] = Category.objects.annotate(
            doc_count=Count('documents', filter=Q(documents__status='published'))
        ).filter(doc_count__gt=0)
        
        # Get most used tags
        context['tags'] = Tag.objects.annotate(
            doc_count=Count('documents', filter=Q(documents__status='published'))
        ).filter(doc_count__gt=0).order_by('-doc_count')[:20]
        
        # Add search and filter context
        context['search_query'] = self.request.GET.get('q', '')
        
        # Add category context if filtering by category
        category_id = self.request.GET.get('category')
        if category_id:
            try:
                context['current_category'] = get_object_or_404(
                    Category, 
                    id=int(category_id)
                )
            except (ValueError, Http404):
                # Handle invalid category ID gracefully
                pass
                
        # Add current tag if filtering by tag
        tag_id = self.request.GET.get('tag')
        if tag_id:
            try:
                context['current_tag'] = get_object_or_404(
                    Tag,
                    id=int(tag_id)
                )
            except (ValueError, Http404):
                # Handle invalid tag ID gracefully
                pass
                
        return context


class ContentDetailView(DetailView):
    """Content-focused document reader view."""
    model = Document
    template_name = 'cms/content_detail.html'
    context_object_name = 'document'
    
    def get_queryset(self):
        """Only show published documents with optimized queries."""
        return Document.objects.filter(
            status='published'
        ).select_related(
            'author', 'category'
        ).prefetch_related(
            'tags', 
            'document_files__file'
        )
    
    def get_object(self, queryset=None):
        """Get the document with additional error handling."""
        obj = super().get_object(queryset)
        
        # Check if document is published
        if obj.status != 'published':
            logger.warning(f"Attempt to access unpublished document: {obj.slug}")
            raise Http404("Document not found")
            
        return obj
    
    def get_context_data(self, **kwargs):
        """Add related documents and metadata."""
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        
        # Get files attached to this document
        context['files'] = self.object.document_files.select_related('file').order_by('order')
        
        # Find related documents
        self._add_related_documents(context)
        
        # Add reading time estimate
        word_count = len(self.object.content.split())
        reading_time = max(1, round(word_count / 200))  # Assume 200 words per minute
        context['reading_time'] = reading_time
        
        return context
    
    def _add_related_documents(self, context):
        """Helper method to find related documents efficiently."""
        if not self.object:
            return
            
        # Start with base queryset of published documents
        related_base = Document.objects.filter(
            status='published'
        ).exclude(
            id=self.object.id
        ).select_related(
            'author', 'category'
        )
        
        # Try category-based related docs first
        if self.object.category:
            category_related = related_base.filter(
                category=self.object.category
            )[:3]
            
            if category_related.exists():
                context['related_documents'] = category_related
                context['relation_type'] = 'category'
                return
        
        # If no category or no related docs found, try tag-based
        if self.object.tags.exists():
            # Get tag IDs for efficient querying
            tag_ids = self.object.tags.values_list('id', flat=True)
            
            tag_related = related_base.filter(
                tags__id__in=tag_ids
            ).distinct()[:3]
            
            if tag_related.exists():
                context['related_documents'] = tag_related
                context['relation_type'] = 'tags'
                return
        
        # If still no related docs, get recent docs
        context['related_documents'] = related_base.order_by('-published_at')[:3]
        context['relation_type'] = 'recent'
