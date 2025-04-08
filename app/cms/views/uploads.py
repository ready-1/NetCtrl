"""
File upload views for the CMS application.

This module defines views for handling file uploads, including chunked uploads 
for large files (up to 5GB). These views handle all stages of the file upload process:
- Presenting the upload form
- Handling chunked uploads via AJAX
- Finalizing the upload and creating File records
"""

import os
import logging
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.db import transaction
from django.conf import settings
from django.contrib import messages

from chunked_upload.views import ChunkedUploadView, ChunkedUploadCompleteView
from chunked_upload.exceptions import ChunkedUploadError
from chunked_upload.constants import http_status, UPLOADING, COMPLETE

from ..models.files import FileChunkedUpload, File, FileCategory, FileTag

logger = logging.getLogger(__name__)

# Default max file size: 5GB
MAX_FILE_SIZE = getattr(settings, 'CMS_MAX_UPLOAD_SIZE', 5 * 1024 * 1024 * 1024)
# Default chunk size: 5MB
CHUNK_SIZE = getattr(settings, 'CMS_CHUNK_SIZE', 5 * 1024 * 1024)


class FileUploadView(LoginRequiredMixin, TemplateView):
    """
    View for file upload page with chunked upload capability.
    
    Displays the form for uploading files with metadata and manages
    the client-side chunked upload process.
    """
    template_name = 'cms/file_upload.html'
    
    def get_context_data(self, **kwargs):
        """Add categories, tags, and configuration values to context."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Upload File'
        context['categories'] = FileCategory.objects.all()
        context['tags'] = FileTag.objects.all()
        context['max_file_size'] = MAX_FILE_SIZE
        context['chunk_size'] = CHUNK_SIZE
        return context


class SimpleFileUploadView(LoginRequiredMixin, TemplateView):
    """
    Simple file upload view that doesn't require JavaScript.
    
    This view provides a traditional file upload form that processes
    the upload in a single request rather than using chunked uploads.
    It's simpler but less suitable for very large files.
    """
    template_name = 'cms/file_upload_simple.html'
    
    def get_context_data(self, **kwargs):
        """Add categories, tags, and configuration values to context."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Upload File (Simple)'
        context['categories'] = FileCategory.objects.all()
        context['tags'] = FileTag.objects.all()
        context['max_file_size'] = MAX_FILE_SIZE
        return context
    
    def post(self, request, *args, **kwargs):
        """Handle file upload form submission."""
        context = self.get_context_data(**kwargs)
        
        # Get the uploaded file
        uploaded_file = request.FILES.get('file')
        if not uploaded_file:
            context['error'] = 'No file was uploaded'
            return self.render_to_response(context)
        
        # Check file size
        if uploaded_file.size > MAX_FILE_SIZE:
            context['error'] = f'File size exceeds the maximum allowed size of {MAX_FILE_SIZE} bytes'
            return self.render_to_response(context)
        
        try:
            with transaction.atomic():
                # Create a new File object
                name = request.POST.get('name') or uploaded_file.name
                file_obj = File(
                    name=name,
                    original_filename=uploaded_file.name,
                    file_size=uploaded_file.size,
                    uploaded_by=request.user,
                )
                
                # Save the file
                file_obj.file.save(uploaded_file.name, uploaded_file, save=False)
                
                # Determine MIME type and save
                file_obj.detect_mime_type()
                file_obj.save()
                
                # Add category if provided
                category_id = request.POST.get('category_id')
                if category_id:
                    try:
                        category = FileCategory.objects.get(id=category_id)
                        file_obj.category = category
                        file_obj.save(update_fields=['category'])
                    except FileCategory.DoesNotExist:
                        logger.warning(f"Category ID {category_id} does not exist")
                
                # Add description if provided
                description = request.POST.get('description')
                if description:
                    file_obj.description = description
                    file_obj.save(update_fields=['description'])
                
                # Add tags if provided
                tags = request.POST.getlist('tags')
                if tags:
                    try:
                        tag_ids = [int(tag_id) for tag_id in tags]
                        tags = FileTag.objects.filter(id__in=tag_ids)
                        file_obj.tags.add(*tags)
                    except (ValueError, TypeError) as e:
                        logger.warning(f"Error adding tags: {e}")
                
                logger.info(f"File uploaded via simple form: {file_obj.name} ({file_obj.file_size} bytes)")
                
                # Set success message
                messages.success(request, f'File "{file_obj.name}" uploaded successfully')
                
                # Redirect to file detail page
                return redirect('cms:file_detail', uuid=file_obj.uuid)
                
        except Exception as e:
            logger.exception("Error uploading file")
            context['error'] = f'An error occurred while uploading the file: {str(e)}'
            return self.render_to_response(context)


class FileUploadDebugView(LoginRequiredMixin, TemplateView):
    """
    Debug view for file uploads.
    
    This view provides additional debugging tools and information
    to help troubleshoot upload issues.
    """
    template_name = 'cms/file_upload_debug.html'
    
    def get_context_data(self, **kwargs):
        """Add categories, tags, and configuration values to context."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Upload File (Debug Mode)'
        context['categories'] = FileCategory.objects.all()
        context['tags'] = FileTag.objects.all()
        context['max_file_size'] = MAX_FILE_SIZE
        context['chunk_size'] = CHUNK_SIZE
        return context
    
    def post(self, request, *args, **kwargs):
        """Handle file upload form submission."""
        context = self.get_context_data(**kwargs)
        
        # Get the uploaded file
        uploaded_file = request.FILES.get('file')
        if not uploaded_file:
            context['error'] = 'No file was uploaded'
            return self.render_to_response(context)
        
        # Check file size
        if uploaded_file.size > MAX_FILE_SIZE:
            context['error'] = f'File size exceeds the maximum allowed size of {MAX_FILE_SIZE} bytes'
            return self.render_to_response(context)
        
        try:
            with transaction.atomic():
                # Create a new File object
                name = request.POST.get('name') or uploaded_file.name
                file_obj = File(
                    name=name,
                    original_filename=uploaded_file.name,
                    file_size=uploaded_file.size,
                    uploaded_by=request.user,
                )
                
                # Save the file
                file_obj.file.save(uploaded_file.name, uploaded_file, save=False)
                
                # Determine MIME type and save
                file_obj.detect_mime_type()
                file_obj.save()
                
                # Add category if provided
                category_id = request.POST.get('category_id')
                if category_id:
                    try:
                        category = FileCategory.objects.get(id=category_id)
                        file_obj.category = category
                        file_obj.save(update_fields=['category'])
                    except FileCategory.DoesNotExist:
                        logger.warning(f"Category ID {category_id} does not exist")
                
                # Add description if provided
                description = request.POST.get('description')
                if description:
                    file_obj.description = description
                    file_obj.save(update_fields=['description'])
                
                # Add tags if provided
                tags_str = request.POST.get('tags')
                if tags_str:
                    try:
                        # Handle multiple select tags
                        if isinstance(tags_str, list):
                            tag_ids = [int(tag_id) for tag_id in tags_str]
                        else:
                            tag_ids = [int(tag_id) for tag_id in request.POST.getlist('tags')]
                        
                        tags = FileTag.objects.filter(id__in=tag_ids)
                        file_obj.tags.add(*tags)
                    except (ValueError, TypeError) as e:
                        logger.warning(f"Error adding tags: {e}")
                
                logger.info(f"File uploaded via simple form: {file_obj.name} ({file_obj.file_size} bytes)")
                
                # Set success message
                context['success'] = f'File "{file_obj.name}" uploaded successfully'
                
                # Redirect to file detail page
                return redirect('cms:file_detail', uuid=file_obj.uuid)
                
        except Exception as e:
            logger.exception("Error uploading file")
            context['error'] = f'An error occurred while uploading the file: {str(e)}'
            return self.render_to_response(context)


@method_decorator(csrf_exempt, name='dispatch')
class FileChunkedUploadView(ChunkedUploadView):
    """
    View for handling chunked upload API requests.
    
    This view receives chunks of a file upload and manages the chunked
    upload process. It extends Django Chunked Upload's ChunkedUploadView.
    """
    model = FileChunkedUpload
    field_name = 'file'
    
    def check_permissions(self, request):
        """
        Check if the user is authenticated.
        
        Raises:
            ChunkedUploadError: If the user is not authenticated.
        """
        if not request.user.is_authenticated:
            raise ChunkedUploadError(
                status=http_status.HTTP_403_FORBIDDEN,
                detail='Authentication required'
            )
    
    def create_chunked_upload(self, save=False, **attrs):
        """
        Create and save a chunked upload with additional metadata.
        
        Args:
            save (bool): Whether to save the upload.
            **attrs: Additional attributes for the upload.
            
        Returns:
            FileChunkedUpload: The created upload instance.
        """
        chunked_upload = super().create_chunked_upload(save=False, **attrs)
        chunked_upload.user = self.request.user
        
        # Add any category, description, or tags passed in request.POST
        if self.request.POST.get('category_id'):
            try:
                category_id = int(self.request.POST.get('category_id'))
                # Verify category exists
                if FileCategory.objects.filter(id=category_id).exists():
                    chunked_upload.category_id = category_id
            except (ValueError, TypeError):
                logger.warning(f"Invalid category_id: {self.request.POST.get('category_id')}")
        
        if self.request.POST.get('description'):
            chunked_upload.description = self.request.POST.get('description')
        
        if self.request.POST.get('tags'):
            # Store as comma-separated list of IDs
            chunked_upload.tags = self.request.POST.get('tags')
        
        if save:
            chunked_upload.save()
        
        return chunked_upload
    
    def get_response_data(self, chunked_upload, request):
        """
        Return upload progress data as JSON.
        
        Args:
            chunked_upload (FileChunkedUpload): The chunked upload instance.
            request (HttpRequest): The HTTP request.
            
        Returns:
            dict: Upload progress data.
        """
        return {
            'upload_id': chunked_upload.upload_id,
            'offset': chunked_upload.offset,
            'expires_at': chunked_upload.expires_on.timestamp()
        }
    
    def _post(self, request, *args, **kwargs):
        """
        Handle POST requests for chunk uploads with better error handling.
        
        Args:
            request (HttpRequest): The HTTP request.
            
        Returns:
            HttpResponse: The JSON response.
        """
        try:
            # Log the request details for debugging
            logger.info(f"Chunked upload request: {request.method} {request.path}")
            logger.info(f"Request headers: {dict(request.headers)}")
            logger.info(f"Request POST data: {dict(request.POST)}")
            logger.info(f"Request FILES: {request.FILES.keys()}")
            
            # Check if the file field is present
            if self.field_name not in request.FILES:
                missing_fields = []
                if self.field_name not in request.FILES:
                    missing_fields.append(self.field_name)
                
                logger.error(f"Missing required fields in upload request: {missing_fields}")
                
                return JsonResponse({
                    'error': 'Missing required fields',
                    'details': f"Required field '{self.field_name}' not found in request. Available fields: {list(request.FILES.keys())}",
                    'message': f"Required field '{self.field_name}' is missing from the upload."
                }, status=http_status.HTTP_400_BAD_REQUEST)
            
            # If we got here, try to process the request
            return super()._post(request, *args, **kwargs)
            
        except Exception as e:
            logger.exception("Error processing chunked upload")
            
            # Provide more detailed error information
            error_details = {
                'error': str(e),
                'error_type': type(e).__name__,
                'message': 'An error occurred while processing your upload.'
            }
            
            # Add traceback information in debug mode
            if settings.DEBUG:
                import traceback
                error_details['traceback'] = traceback.format_exc()
            
            return JsonResponse(error_details, status=http_status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class FileChunkedUploadCompleteView(ChunkedUploadCompleteView):
    """
    View for completing a chunked upload.
    
    This view finalizes the chunked upload process and creates a File object
    from the uploaded chunks.
    """
    model = FileChunkedUpload
    
    def check_permissions(self, request):
        """
        Check if the user is authenticated.
        
        Raises:
            ChunkedUploadError: If the user is not authenticated.
        """
        if not request.user.is_authenticated:
            raise ChunkedUploadError(
                status=http_status.HTTP_403_FORBIDDEN,
                detail='Authentication required'
            )
    
    @transaction.atomic
    def on_completion(self, chunked_upload, request):
        """
        Process the completed upload and create a File object.
        
        This method is called when all chunks have been uploaded. It creates
        a File object from the uploaded chunks and sets its metadata.
        
        Args:
            chunked_upload (FileChunkedUpload): The chunked upload instance.
            request (HttpRequest): The HTTP request.
            
        Returns:
            File: The created file object.
            
        Raises:
            Exception: If an error occurs while creating the file.
        """
        try:
            # Get the uploaded file
            uploaded_file = chunked_upload.get_uploaded_file()
            
            # Create a new File object
            name = request.POST.get('name') or chunked_upload.filename
            file_obj = File(
                name=name,
                original_filename=chunked_upload.filename,
                file_size=chunked_upload.offset,
                uploaded_by=request.user,
            )
            
            # Set file field to the uploaded file
            file_obj.file.save(chunked_upload.filename, uploaded_file, save=False)
            
            # Determine MIME type and set other attributes
            file_obj.detect_mime_type()
            file_obj.save()
            
            # Add category if provided
            if chunked_upload.category_id:
                try:
                    category = FileCategory.objects.get(id=chunked_upload.category_id)
                    file_obj.category = category
                    file_obj.save(update_fields=['category'])
                except FileCategory.DoesNotExist:
                    logger.warning(f"Category ID {chunked_upload.category_id} does not exist")
                except Exception as e:
                    logger.exception(f"Error setting category: {e}")
            
            # Add description if provided
            if chunked_upload.description:
                file_obj.description = chunked_upload.description
                file_obj.save(update_fields=['description'])
            
            # Add tags if provided
            if chunked_upload.tags:
                try:
                    tag_ids = [int(id.strip()) for id in chunked_upload.tags.split(',') if id.strip()]
                    tags = FileTag.objects.filter(id__in=tag_ids)
                    file_obj.tags.add(*tags)
                except (ValueError, TypeError) as e:
                    logger.warning(f"Error adding tags: {e}")
                except Exception as e:
                    logger.exception(f"Error setting tags: {e}")
            
            # Mark chunked upload as complete
            chunked_upload.status = COMPLETE
            chunked_upload.completed_on = timezone.now()
            chunked_upload.save()
            
            logger.info(f"File upload completed: {file_obj.name} ({file_obj.file_size} bytes)")
            return file_obj
            
        except Exception as e:
            # Log the error and re-raise for the view to handle
            logger.exception("Error completing chunked upload")
            raise
        finally:
            # Ensure file is closed properly
            if 'uploaded_file' in locals():
                if hasattr(uploaded_file, 'close'):
                    uploaded_file.close()
    
    def get_response_data(self, chunked_upload, request):
        """
        Return data on successful upload completion.
        
        Args:
            chunked_upload (FileChunkedUpload): The chunked upload instance.
            request (HttpRequest): The HTTP request.
            
        Returns:
            dict: Upload completion data with file details.
        """
        try:
            file_obj = self.on_completion(chunked_upload, request)
            return {
                'success': True,
                'file_id': str(file_obj.uuid),
                'name': file_obj.name,
                'redirect_url': reverse('cms:file_detail', kwargs={'uuid': file_obj.uuid})
            }
        except Exception as e:
            logger.exception("Error in get_response_data")
            return {
                'success': False,
                'error': str(e),
                'message': 'An error occurred while completing your upload.'
            }
