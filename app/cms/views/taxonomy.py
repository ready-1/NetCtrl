"""
Views for taxonomy management (tags and categories).

This module defines views for creating, reading, updating, and deleting taxonomy entities:
- TagListView: For listing and searching tags
- TagCreateView: For creating new tags
- TagUpdateView: For editing existing tags
- TagDeleteView: For deleting tags
- TagDetailView: For viewing tag details
- Equivalent views for categories
"""

import logging
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import Count, Q

from ..models.documents import Tag, Category, Document
from ..forms.taxonomy_forms import TagForm, CategoryForm

logger = logging.getLogger(__name__)


class StaffRequiredMixin(UserPassesTestMixin):
    """
    Mixin that requires the user to be staff.
    
    Ensures that only staff members can access the view.
    """
    
    def test_func(self):
        """Test if the user is staff."""
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        """Handle non-staff users."""
        messages.error(self.request, "You don't have permission to access this page.")
        return super().handle_no_permission()


# Base views for common functionality

class TaxonomyListView(LoginRequiredMixin, ListView):
    """
    Base list view for taxonomy models with search functionality.
    
    This is a base class for TagListView and CategoryListView.
    """
    paginate_by = 20
    search_fields = ['name']
    
    def get_queryset(self):
        """Get filtered queryset based on search query."""
        queryset = super().get_queryset()
        
        # Apply search filter
        search_query = self.request.GET.get('q')
        if search_query:
            query = Q()
            for field in self.search_fields:
                query |= Q(**{f"{field}__icontains": search_query})
            queryset = queryset.filter(query)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        """Add search query to context."""
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context


# Tag views

class TagListView(TaxonomyListView):
    """View for listing and searching tags."""
    model = Tag
    template_name = 'cms/taxonomy/tag_list.html'
    context_object_name = 'tags'
    
    def get_queryset(self):
        """Get tags with document count annotation."""
        queryset = super().get_queryset()
        # Annotate with document count
        return queryset.annotate(document_count=Count('documents'))
    
    def get_context_data(self, **kwargs):
        """Add title to context."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tags'
        context['total_count'] = self.get_queryset().count()
        return context


class TagCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    """View for creating new tags."""
    model = Tag
    form_class = TagForm
    template_name = 'cms/taxonomy/tag_form.html'
    success_url = reverse_lazy('cms:tag_list')
    
    def form_valid(self, form):
        """Handle successful form submission."""
        response = super().form_valid(form)
        messages.success(self.request, f'Tag "{self.object.name}" created successfully.')
        logger.info(f'Tag created: {self.object.name} by {self.request.user.username}')
        return response
    
    def get_context_data(self, **kwargs):
        """Add title to context."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Tag'
        return context


class TagUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    """View for editing existing tags."""
    model = Tag
    form_class = TagForm
    template_name = 'cms/taxonomy/tag_form.html'
    success_url = reverse_lazy('cms:tag_list')
    
    def form_valid(self, form):
        """Handle successful form submission."""
        response = super().form_valid(form)
        messages.success(self.request, f'Tag "{self.object.name}" updated successfully.')
        logger.info(f'Tag updated: {self.object.name} by {self.request.user.username}')
        return response
    
    def get_context_data(self, **kwargs):
        """Add title to context."""
        context = super().get_context_data(**kwargs)
        context['title'] = f'Edit Tag: {self.object.name}'
        return context


class TagDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    """View for deleting tags."""
    model = Tag
    template_name = 'cms/taxonomy/tag_confirm_delete.html'
    success_url = reverse_lazy('cms:tag_list')
    context_object_name = 'tag'
    
    def get_context_data(self, **kwargs):
        """Add title and document count to context."""
        context = super().get_context_data(**kwargs)
        context['title'] = f'Delete Tag: {self.object.name}'
        context['document_count'] = Document.objects.filter(tags=self.object).count()
        return context
    
    def delete(self, request, *args, **kwargs):
        """Handle tag deletion with confirmation and validation."""
        tag = self.get_object()
        document_count = Document.objects.filter(tags=tag).count()
        
        # Check if tag is in use and abort if it is
        if document_count > 0:
            messages.error(request, f'Cannot delete tag "{tag.name}" because it is used by {document_count} documents.')
            return redirect('cms:tag_list')
        
        # Proceed with deletion if not in use
        response = super().delete(request, *args, **kwargs)
        messages.success(request, f'Tag "{tag.name}" deleted successfully.')
        logger.info(f'Tag deleted: {tag.name} by {request.user.username}')
        return response


class TagDetailView(LoginRequiredMixin, DetailView):
    """View for viewing tag details and associated documents."""
    model = Tag
    template_name = 'cms/taxonomy/tag_detail.html'
    context_object_name = 'tag'
    
    def get_context_data(self, **kwargs):
        """Add title and associated documents to context."""
        context = super().get_context_data(**kwargs)
        context['title'] = f'Tag: {self.object.name}'
        
        # Get associated documents
        documents = Document.objects.filter(tags=self.object).order_by('-created_at')
        context['documents'] = documents
        context['document_count'] = documents.count()
        return context


# Category views

class CategoryListView(TaxonomyListView):
    """View for listing and searching categories."""
    model = Category
    template_name = 'cms/taxonomy/category_list.html'
    context_object_name = 'categories'
    search_fields = ['name', 'description']
    
    def get_queryset(self):
        """Get categories with document count annotation."""
        queryset = super().get_queryset()
        # Annotate with document count
        return queryset.annotate(document_count=Count('documents'))
    
    def get_context_data(self, **kwargs):
        """Add title to context."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Categories'
        context['total_count'] = self.get_queryset().count()
        
        # Get top-level categories (no parent) for hierarchical display
        context['top_level_categories'] = self.get_queryset().filter(parent__isnull=True)
        return context


class CategoryCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    """View for creating new categories."""
    model = Category
    form_class = CategoryForm
    template_name = 'cms/taxonomy/category_form.html'
    success_url = reverse_lazy('cms:category_list')
    
    def form_valid(self, form):
        """Handle successful form submission."""
        response = super().form_valid(form)
        messages.success(self.request, f'Category "{self.object.name}" created successfully.')
        logger.info(f'Category created: {self.object.name} by {self.request.user.username}')
        return response
    
    def get_context_data(self, **kwargs):
        """Add title to context."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Category'
        return context


class CategoryUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    """View for editing existing categories."""
    model = Category
    form_class = CategoryForm
    template_name = 'cms/taxonomy/category_form.html'
    success_url = reverse_lazy('cms:category_list')
    
    def form_valid(self, form):
        """Handle successful form submission."""
        response = super().form_valid(form)
        messages.success(self.request, f'Category "{self.object.name}" updated successfully.')
        logger.info(f'Category updated: {self.object.name} by {self.request.user.username}')
        return response
    
    def get_context_data(self, **kwargs):
        """Add title to context."""
        context = super().get_context_data(**kwargs)
        context['title'] = f'Edit Category: {self.object.name}'
        return context


class CategoryDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    """View for deleting categories."""
    model = Category
    template_name = 'cms/taxonomy/category_confirm_delete.html'
    success_url = reverse_lazy('cms:category_list')
    context_object_name = 'category'
    
    def get_context_data(self, **kwargs):
        """Add title, document count, and children count to context."""
        context = super().get_context_data(**kwargs)
        context['title'] = f'Delete Category: {self.object.name}'
        context['document_count'] = Document.objects.filter(category=self.object).count()
        context['children_count'] = Category.objects.filter(parent=self.object).count()
        return context
    
    def delete(self, request, *args, **kwargs):
        """Handle category deletion with confirmation and validation."""
        category = self.get_object()
        document_count = Document.objects.filter(category=category).count()
        children_count = Category.objects.filter(parent=category).count()
        
        # Check if category is in use and abort if it is
        if document_count > 0:
            messages.error(request, f'Cannot delete category "{category.name}" because it is used by {document_count} documents.')
            return redirect('cms:category_list')
        
        # Check if category has children and abort if it does
        if children_count > 0:
            messages.error(request, f'Cannot delete category "{category.name}" because it has {children_count} subcategories.')
            return redirect('cms:category_list')
        
        # Proceed with deletion if not in use and has no children
        response = super().delete(request, *args, **kwargs)
        messages.success(request, f'Category "{category.name}" deleted successfully.')
        logger.info(f'Category deleted: {category.name} by {request.user.username}')
        return response


class CategoryDetailView(LoginRequiredMixin, DetailView):
    """View for viewing category details and associated documents."""
    model = Category
    template_name = 'cms/taxonomy/category_detail.html'
    context_object_name = 'category'
    
    def get_context_data(self, **kwargs):
        """Add title, associated documents, and subcategories to context."""
        context = super().get_context_data(**kwargs)
        context['title'] = f'Category: {self.object.name}'
        
        # Get associated documents
        documents = Document.objects.filter(category=self.object).order_by('-created_at')
        context['documents'] = documents
        context['document_count'] = documents.count()
        
        # Get subcategories
        subcategories = Category.objects.filter(parent=self.object)
        context['subcategories'] = subcategories
        context['subcategory_count'] = subcategories.count()
        
        return context
