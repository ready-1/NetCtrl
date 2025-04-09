"""
Document management views for the CMS application.

This module defines views for working with documents in the CMS:
- Listing documents with filtering
- Creating and editing documents
- Managing document versions
- Attaching and managing files within documents
"""

import logging
import json
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView,
    FormView, View, TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.db.models import Q, Max
from django.forms import modelform_factory
from django.db import transaction
from django.utils import timezone
from django.core.exceptions import PermissionDenied

from ..models.documents import Document, DocumentVersion, DocumentFile, Category, Tag
from ..models.files import File
from ..forms import DocumentVersionForm, DocumentFileForm, DocumentFilterForm

logger = logging.getLogger(__name__)


class DocumentListView(LoginRequiredMixin, ListView):
    """View for listing documents with filtering."""
    model = Document
    template_name = 'cms/document_list.html'
    context_object_name = 'documents'
    paginate_by = 10
    
    def get_queryset(self):
        """Filter queryset based on search parameters."""
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
        
        # Filter by status
        status = self.request.GET.get('status')
        if status in ['draft', 'published']:
            queryset = queryset.filter(status=status)
        
        # Search in title, content, and excerpt
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | 
                Q(content__icontains=query) |
                Q(excerpt__icontains=query)
            )
        
        return queryset
    
    def get_context_data(self, **kwargs):
        """Add categories, tags, and filter form to context."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Documents'
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        
        # Create filter form with initial values from request
        initial = {
            'q': self.request.GET.get('q', ''),
            'category_id': self.request.GET.get('category_id', ''),
            'tag_id': self.request.GET.get('tag_id', ''),
            'status': self.request.GET.get('status', '')
        }
        context['filter_form'] = DocumentFilterForm(initial=initial)
        
        return context


class DocumentDetailView(LoginRequiredMixin, DetailView):
    """View for displaying document details."""
    model = Document
    template_name = 'cms/document_detail.html'
    context_object_name = 'document'
    
    def get_context_data(self, **kwargs):
        """Add related data to context."""
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        
        # Add associated files
        context['files'] = self.object.document_files.select_related('file').order_by('order')
        
        # Add latest versions (limited to 5)
        context['versions'] = self.object.versions.select_related('created_by').order_by('-version_number')[:5]
        
        # Determine if user can edit
        context['can_edit'] = self.request.user == self.object.author or self.request.user.is_staff
        
        return context


class DocumentCreateView(LoginRequiredMixin, CreateView):
    """View for creating a new document."""
    model = Document
    template_name = 'cms/document_form.html'
    fields = ['title', 'content', 'excerpt', 'category', 'tags', 'featured_image', 'content_format']
    
    def get_context_data(self, **kwargs):
        """Add form context."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Document'
        context['is_new'] = True
        return context
    
    def form_valid(self, form):
        """Set author and handle the form submission."""
        form.instance.author = self.request.user
        response = super().form_valid(form)
        
        # Log the creation
        logger.info(f"Document created: {self.object.title} by {self.request.user.username}")
        messages.success(self.request, f'Document "{self.object.title}" created successfully.')
        
        return response


class DocumentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """View for updating an existing document."""
    model = Document
    template_name = 'cms/document_form.html'
    fields = ['title', 'content', 'content_format', 'excerpt', 'category', 'tags', 'featured_image', 'status']
    
    def test_func(self):
        """Check if user can edit this document."""
        obj = self.get_object()
        return self.request.user == obj.author or self.request.user.is_staff
    
    def get_context_data(self, **kwargs):
        """Add form context."""
        context = super().get_context_data(**kwargs)
        context['title'] = f'Edit {self.object.title}'
        context['is_new'] = False
        return context
    
    def form_valid(self, form):
        """Create a version before saving."""
        # Create a version of the document before changes
        old_version = self.object
        changelog = f"Edited by {self.request.user.username} on {timezone.now().strftime('%Y-%m-%d %H:%M')}"
        
        # Save the form to update the document
        response = super().form_valid(form)
        
        # Create a new version record
        self.object.create_version(
            created_by=self.request.user,
            changelog=changelog
        )
        
        # Log the update
        logger.info(f"Document updated: {self.object.title} by {self.request.user.username}")
        messages.success(self.request, f'Document "{self.object.title}" updated successfully.')
        
        return response


class DocumentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """View for deleting a document."""
    model = Document
    template_name = 'cms/document_confirm_delete.html'
    success_url = reverse_lazy('cms:document_list')
    
    def test_func(self):
        """Check if user can delete this document."""
        obj = self.get_object()
        return self.request.user == obj.author or self.request.user.is_staff
    
    def get_context_data(self, **kwargs):
        """Add context data."""
        context = super().get_context_data(**kwargs)
        context['title'] = f'Delete {self.object.title}'
        return context
    
    def delete(self, request, *args, **kwargs):
        """Handle document deletion."""
        document = self.get_object()
        title = document.title
        
        # Perform the deletion
        result = super().delete(request, *args, **kwargs)
        
        # Log the deletion
        logger.info(f"Document deleted: {title} by {request.user.username}")
        messages.success(request, f'Document "{title}" deleted successfully.')
        
        return result


class DocumentVersionListView(LoginRequiredMixin, DetailView):
    """View for listing all versions of a document."""
    model = Document
    template_name = 'cms/document_versions.html'
    context_object_name = 'document'
    
    def get_context_data(self, **kwargs):
        """Add versions to context."""
        context = super().get_context_data(**kwargs)
        context['title'] = f'{self.object.title} - Versions'
        context['versions'] = self.object.versions.select_related('created_by').order_by('-version_number')
        
        # Determine if user can restore versions
        context['can_restore'] = self.request.user == self.object.author or self.request.user.is_staff
        
        return context


class DocumentVersionDetailView(LoginRequiredMixin, DetailView):
    """View for viewing a specific document version."""
    model = DocumentVersion
    template_name = 'cms/document_version_detail.html'
    context_object_name = 'version'
    
    def get_object(self, queryset=None):
        """Get version by document slug and version number."""
        if queryset is None:
            queryset = self.get_queryset()
        
        document_slug = self.kwargs.get('slug')
        version_number = self.kwargs.get('version')
        
        document = get_object_or_404(Document, slug=document_slug)
        return get_object_or_404(
            queryset.filter(document=document), 
            version_number=version_number
        )
    
    def get_context_data(self, **kwargs):
        """Add context data."""
        context = super().get_context_data(**kwargs)
        context['title'] = f'{self.object.document.title} - Version {self.object.version_number}'
        context['document'] = self.object.document
        
        # Determine if user can restore this version
        context['can_restore'] = (
            self.request.user == self.object.document.author or 
            self.request.user.is_staff
        )
        
        return context


class DocumentVersionCreateView(LoginRequiredMixin, UserPassesTestMixin, FormView):
    """View for manually creating a document version."""
    template_name = 'cms/document_version_form.html'
    form_class = DocumentVersionForm
    
    def test_func(self):
        """Check if user can create versions for this document."""
        document = get_object_or_404(Document, slug=self.kwargs.get('slug'))
        return self.request.user == document.author or self.request.user.is_staff
    
    def get_document(self):
        """Get the document object."""
        return get_object_or_404(Document, slug=self.kwargs.get('slug'))
    
    def get_context_data(self, **kwargs):
        """Add document to context."""
        context = super().get_context_data(**kwargs)
        document = self.get_document()
        context['document'] = document
        context['title'] = f'Create Version - {document.title}'
        return context
    
    def form_valid(self, form):
        """Process the form and create a new version."""
        document = self.get_document()
        
        # Create the new version
        version = document.create_version(
            created_by=self.request.user,
            changelog=form.cleaned_data.get('changelog', '')
        )
        
        messages.success(self.request, f'Version {version.version_number} created for "{document.title}".')
        return redirect('cms:document_versions', slug=document.slug)


class DocumentVersionPromoteView(LoginRequiredMixin, UserPassesTestMixin, View):
    """View for promoting a version to be the current document."""
    
    def test_func(self):
        """Check if user can promote versions for this document."""
        document = get_object_or_404(Document, slug=self.kwargs.get('slug'))
        return self.request.user == document.author or self.request.user.is_staff
    
    def post(self, request, *args, **kwargs):
        """Handle the promotion request."""
        document_slug = self.kwargs.get('slug')
        version_number = self.kwargs.get('version')
        
        document = get_object_or_404(Document, slug=document_slug)
        version = get_object_or_404(
            DocumentVersion.objects.filter(document=document),
            version_number=version_number
        )
        
        # Promote the version
        version.promote_to_current()
        
        messages.success(
            request, 
            f'Version {version.version_number} promoted to current for "{document.title}".'
        )
        return redirect('cms:document_detail', slug=document.slug)


class DocumentFileListView(LoginRequiredMixin, DetailView):
    """View for managing files attached to a document."""
    model = Document
    template_name = 'cms/document_files.html'
    context_object_name = 'document'
    
    def get_context_data(self, **kwargs):
        """Add files and available files to context."""
        context = super().get_context_data(**kwargs)
        context['title'] = f'{self.object.title} - Files'
        
        # Get attached files
        context['document_files'] = self.object.document_files.select_related('file').order_by('order')
        
        # Determine if user can manage files
        context['can_manage_files'] = (
            self.request.user == self.object.author or 
            self.request.user.is_staff
        )
        
        if context['can_manage_files']:
            # Get files that could be attached
            attached_file_ids = self.object.document_files.values_list('file_id', flat=True)
            context['available_files'] = File.objects.exclude(id__in=attached_file_ids)
        
        return context


class DocumentFileAddView(LoginRequiredMixin, UserPassesTestMixin, FormView):
    """View for adding files to a document."""
    template_name = 'cms/document_file_add.html'
    form_class = DocumentFileForm
    
    def test_func(self):
        """Check if user can add files to this document."""
        document = get_object_or_404(Document, slug=self.kwargs.get('slug'))
        return self.request.user == document.author or self.request.user.is_staff
    
    def get_document(self):
        """Get the document object."""
        return get_object_or_404(Document, slug=self.kwargs.get('slug'))
    
    def get_form_kwargs(self):
        """Pass available files to form."""
        kwargs = super().get_form_kwargs()
        document = self.get_document()
        
        # Get files that aren't already attached
        attached_file_ids = document.document_files.values_list('file_id', flat=True)
        available_files = File.objects.exclude(id__in=attached_file_ids)
        
        kwargs['available_files'] = available_files
        return kwargs
    
    def get_context_data(self, **kwargs):
        """Add document to context."""
        context = super().get_context_data(**kwargs)
        document = self.get_document()
        context['document'] = document
        context['title'] = f'Add Files - {document.title}'
        return context
    
    def form_valid(self, form):
        """Process the form and add selected files."""
        document = self.get_document()
        file_ids = form.cleaned_data.get('files', [])
        
        count = 0
        for file_id in file_ids:
            try:
                # Get the file
                file_obj = File.objects.get(id=file_id)
                
                # Determine next order position
                max_order = document.document_files.aggregate(Max('order'))['order__max'] or 0
                next_order = max_order + 1
                
                # Create the document-file association
                DocumentFile.objects.create(
                    document=document,
                    file=file_obj,
                    order=next_order,
                    added_by=self.request.user
                )
                count += 1
                
            except Exception as e:
                logger.warning(f"Error adding file {file_id} to document {document.id}: {str(e)}")
        
        if count > 0:
            messages.success(self.request, f'Added {count} files to document "{document.title}".')
        else:
            messages.warning(self.request, 'No files were added to the document.')
        
        return redirect('cms:document_files', slug=document.slug)


class DocumentFileRemoveView(LoginRequiredMixin, UserPassesTestMixin, View):
    """View for removing a file from a document."""
    
    def test_func(self):
        """Check if user can remove files from this document."""
        document = get_object_or_404(Document, slug=self.kwargs.get('slug'))
        return self.request.user == document.author or self.request.user.is_staff
    
    def post(self, request, *args, **kwargs):
        """Handle the removal request."""
        document_slug = self.kwargs.get('slug')
        file_uuid = self.kwargs.get('file_uuid')
        
        document = get_object_or_404(Document, slug=document_slug)
        file_obj = get_object_or_404(File, uuid=file_uuid)
        
        try:
            # Find and delete the document-file association
            doc_file = get_object_or_404(
                DocumentFile,
                document=document,
                file=file_obj
            )
            doc_file.delete()
            
            messages.success(
                request, 
                f'File "{file_obj.name}" removed from document "{document.title}".'
            )
            logger.info(f"File {file_obj.id} removed from document {document.id} by {request.user.username}")
            
        except Exception as e:
            messages.error(
                request,
                f'Error removing file: {str(e)}'
            )
            logger.error(f"Error removing file {file_obj.id} from document {document.id}: {str(e)}")
        
        return redirect('cms:document_files', slug=document.slug)


class DocumentFileReorderView(LoginRequiredMixin, UserPassesTestMixin, View):
    """View for reordering files within a document."""
    
    def test_func(self):
        """Check if user can reorder files in this document."""
        document = get_object_or_404(Document, slug=self.kwargs.get('slug'))
        return self.request.user == document.author or self.request.user.is_staff
    
    def post(self, request, *args, **kwargs):
        """Handle the reordering request."""
        document_slug = self.kwargs.get('slug')
        document = get_object_or_404(Document, slug=document_slug)
        
        try:
            # Get the new order from the request
            new_order = json.loads(request.body)
            
            with transaction.atomic():
                for item in new_order:
                    file_id = item.get('id')
                    position = item.get('position')
                    
                    if file_id and position is not None:
                        doc_file = get_object_or_404(
                            DocumentFile,
                            document=document,
                            file_id=file_id
                        )
                        doc_file.order = position
                        doc_file.save(update_fields=['order'])
            
            logger.info(f"Files reordered for document {document.id} by {request.user.username}")
            return JsonResponse({'status': 'success'})
            
        except Exception as e:
            logger.error(f"Error reordering files for document {document.id}: {str(e)}")
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
