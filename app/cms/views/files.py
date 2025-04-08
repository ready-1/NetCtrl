"""
File management views for the CMS application.

This module defines views for working with files in the CMS:
- Listing files
- Viewing file details
- Downloading files
- Deleting files
- Editing file metadata
"""

import logging
from django.views.generic import DetailView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404, FileResponse
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.db import transaction
from django.contrib import messages

from ..models.files import File, FileCategory, FileTag

logger = logging.getLogger(__name__)


class FileListView(LoginRequiredMixin, ListView):
    """
    View for listing files with filtering capabilities.
    
    Displays a list of files with options to filter by category,
    tag, and search terms.
    """
    model = File
    template_name = 'cms/file_list.html'
    context_object_name = 'files'
    paginate_by = 20
    
    def get_queryset(self):
        """
        Filter queryset based on request GET parameters.
        
        Supports filtering by:
        - category_id: Filter by category
        - tag_id: Filter by tag
        - q: Search in name and description
        """
        queryset = super().get_queryset()
        
        # Filter by category
        category_id = self.request.GET.get('category_id')
        if category_id:
            try:
                queryset = queryset.filter(category_id=int(category_id))
            except (ValueError, TypeError):
                logger.warning(f"Invalid category_id filter: {category_id}")
        
        # Filter by tag
        tag_id = self.request.GET.get('tag_id')
        if tag_id:
            try:
                queryset = queryset.filter(tags__id=int(tag_id))
            except (ValueError, TypeError):
                logger.warning(f"Invalid tag_id filter: {tag_id}")
        
        # Search in name and description
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | 
                Q(description__icontains=query) |
                Q(original_filename__icontains=query)
            )
        
        return queryset
    
    def get_context_data(self, **kwargs):
        """Add categories and tags to context for filtering."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Files'
        context['categories'] = FileCategory.objects.all()
        context['tags'] = FileTag.objects.all()
        
        # Add filter values to context for form persistence
        context['category_id'] = self.request.GET.get('category_id', '')
        context['tag_id'] = self.request.GET.get('tag_id', '')
        context['query'] = self.request.GET.get('q', '')
        
        return context


class FileDetailView(LoginRequiredMixin, DetailView):
    """
    View for displaying file details.
    
    Shows metadata about a file and provides options for
    downloading or deleting it.
    """
    model = File
    template_name = 'cms/file_detail.html'
    context_object_name = 'file'
    
    def get_object(self, queryset=None):
        """
        Get file by UUID instead of pk/slug.
        
        Args:
            queryset: Optional queryset to use.
            
        Returns:
            File: The file object.
            
        Raises:
            Http404: If the file does not exist.
        """
        if queryset is None:
            queryset = self.get_queryset()
        
        uuid = self.kwargs.get('uuid')
        try:
            obj = queryset.get(uuid=uuid)
            return obj
        except queryset.model.DoesNotExist:
            raise Http404("File does not exist")
    
    def get_context_data(self, **kwargs):
        """Add title to context."""
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context


class FileDownloadView(LoginRequiredMixin, DetailView):
    """
    View for downloading a file.
    
    Serves the file for download and records the download in
    the file's statistics.
    """
    model = File
    
    def get_object(self, queryset=None):
        """Get file by UUID."""
        if queryset is None:
            queryset = self.get_queryset()
        
        uuid = self.kwargs.get('uuid')
        return get_object_or_404(queryset, uuid=uuid)
    
    def get(self, request, *args, **kwargs):
        """
        Serve the file for download and record the download.
        
        Args:
            request: The HTTP request.
            
        Returns:
            FileResponse: The file response for download.
        """
        file_obj = self.get_object()
        
        # Record the download
        file_obj.record_download()
        logger.info(f"File downloaded: {file_obj.name} by {request.user.username}")
        
        # Prepare the response
        response = FileResponse(
            file_obj.file,
            content_type=file_obj.mime_type or 'application/octet-stream',
            as_attachment=True,
            filename=file_obj.original_filename
        )
        
        # Add Content-Length header
        response['Content-Length'] = file_obj.file_size
        
        return response


class FileDeleteView(LoginRequiredMixin, DeleteView):
    """
    View for deleting a file.
    
    Allows users to delete files they have permission to delete.
    """
    model = File
    template_name = 'cms/file_confirm_delete.html'
    success_url = reverse_lazy('cms:file_list')
    
    def get_object(self, queryset=None):
        """Get file by UUID."""
        if queryset is None:
            queryset = self.get_queryset()
        
        uuid = self.kwargs.get('uuid')
        return get_object_or_404(queryset, uuid=uuid)
    
    def delete(self, request, *args, **kwargs):
        """
        Delete the file and record the action.
        
        Args:
            request: The HTTP request.
            
        Returns:
            HttpResponse: Redirect to success URL.
        """
        file_obj = self.get_object()
        filename = file_obj.name
        
        # Only allow deletion by uploaders or staff
        if not (request.user == file_obj.uploaded_by or request.user.is_staff):
            messages.error(request, "You don't have permission to delete this file.")
            return redirect('cms:file_detail', uuid=file_obj.uuid)
        
        try:
            with transaction.atomic():
                file_obj.delete()
            
            messages.success(request, f"File '{filename}' was successfully deleted.")
            logger.info(f"File deleted: {filename} by {request.user.username}")
            
        except Exception as e:
            messages.error(request, f"An error occurred while deleting the file: {str(e)}")
            logger.exception(f"Error deleting file {file_obj.uuid}")
            return redirect('cms:file_detail', uuid=file_obj.uuid)
        
        return redirect(self.success_url)
    
    def get_context_data(self, **kwargs):
        """Add title to context."""
        context = super().get_context_data(**kwargs)
        context['title'] = f"Delete {self.object.name}"
        return context


class FileEditView(LoginRequiredMixin, UpdateView):
    """
    View for editing file metadata.
    
    Allows users to update file name, category, tags, and description.
    """
    model = File
    template_name = 'cms/file_edit.html'
    fields = ['name', 'description']
    
    def get_object(self, queryset=None):
        """Get file by UUID."""
        if queryset is None:
            queryset = self.get_queryset()
        
        uuid = self.kwargs.get('uuid')
        return get_object_or_404(queryset, uuid=uuid)
    
    def get_success_url(self):
        """Return to file detail page after successful update."""
        return reverse('cms:file_detail', kwargs={'uuid': self.object.uuid})
    
    def get_context_data(self, **kwargs):
        """Add categories and tags to context."""
        context = super().get_context_data(**kwargs)
        context['title'] = f"Edit {self.object.name}"
        context['categories'] = FileCategory.objects.all()
        context['tags'] = FileTag.objects.all()
        return context
    
    def form_valid(self, form):
        """Process form and handle category and tags."""
        # Save the basic form fields
        response = super().form_valid(form)
        
        # Handle category
        category_id = self.request.POST.get('category')
        if category_id:
            try:
                category = FileCategory.objects.get(id=category_id)
                self.object.category = category
            except (FileCategory.DoesNotExist, ValueError):
                pass
        else:
            # Remove category if empty selection
            self.object.category = None
        
        # Handle tags
        tag_ids = self.request.POST.getlist('tags')
        self.object.tags.clear()
        if tag_ids:
            try:
                tags = FileTag.objects.filter(id__in=tag_ids)
                self.object.tags.add(*tags)
            except Exception as e:
                logger.warning(f"Error adding tags: {str(e)}")
        
        # Save the object with all changes
        self.object.save()
        
        # Add success message
        messages.success(self.request, f"File '{self.object.name}' updated successfully.")
        logger.info(f"File updated: {self.object.name} by {self.request.user.username}")
        
        return response
