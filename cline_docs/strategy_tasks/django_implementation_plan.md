# NetCtrl Django Implementation Plan (MVP)

This plan outlines the step-by-step approach for implementing the NetCtrl Django application, focusing on delivering a solid MVP (Minimum Viable Product) with proper file management capabilities.

## Implementation Principles

- **Simplicity First**: Focus on core features that work reliably
- **Iterative Development**: Build in small, testable increments
- **Proper Documentation**: Include clear docstrings and comments
- **Regular Commits**: Make atomic commits for easier tracking and potential rollbacks
- **Security Awareness**: Apply security best practices without overengineering
- **Testing**: Include basic tests for critical functionality

## 1. Project Setup (Day 1-2)

### 1.1 Project Directory Structure
```
app/
├── manage.py
├── netctrl/              # Main project settings
│   ├── __init__.py
│   ├── settings.py       # Unified settings with env var support
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── cms/                  # CMS application
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models/           # Split models for organization
│   │   ├── __init__.py
│   │   ├── documents.py
│   │   ├── files.py
│   │   └── users.py
│   ├── views/            # Split views for organization
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── documents.py
│   │   └── files.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       └── cms/
├── network/              # Network application (minimal for Phase 1)
├── templates/            # Project-wide templates
│   ├── base.html
│   └── authentication/
├── static/               # Static files
└── media/                # User uploaded files
```

### 1.2 Initial Setup Commands
```bash
# Install required packages
pip install django==3.2.* psycopg2-binary python-magic django-chunked-upload

# Create main project
django-admin startproject netctrl .

# Create applications
python manage.py startapp cms
python manage.py startapp network
```

### 1.3 Settings Configuration
```python
# netctrl/settings.py (key sections)

import os
from pathlib import Path

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# Environment-based settings
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'insecure-development-key-change-in-production')
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'chunked_upload',
    
    # Local apps
    'cms.apps.CmsConfig',
    'network.apps.NetworkConfig',
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'netctrl_db'),
        'USER': os.environ.get('POSTGRES_USER', 'netctrl_user'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'netctrl_password'),
        'HOST': os.environ.get('POSTGRES_HOST', 'postgres'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}

# Static/Media Files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Chunked Upload Settings
CHUNKED_UPLOAD_PATH = 'uploads/chunks/'
CHUNKED_UPLOAD_MAX_BYTES = 5 * 1024 * 1024 * 1024  # 5GB
CHUNKED_UPLOAD_STORAGE_CLASS = 'django.core.files.storage.FileSystemStorage'
CHUNKED_UPLOAD_ABSTRACT_MODEL = False
CHUNKED_UPLOAD_COMPLETE_EXT = '.done'

# Authentication
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'

# Logging - Integrate with our custom TCPSysLogHandler
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'syslog': {
            'level': 'INFO',
            'class': 'netctrl.logging_config.TCPSysLogHandler',
            'formatter': 'verbose',
            'facility': 'local1',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'syslog'],
            'level': 'INFO',
            'propagate': True,
        },
        'cms': {
            'handlers': ['console', 'syslog'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

## 2. Core Models (Day 3-4)

### 2.1 User Profile Model
```python
# cms/models/users.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from netctrl.logging_config import get_logger
logger = get_logger(__name__, 'django')

class UserProfile(models.Model):
    """
    User profile model extending Django's User model.
    
    Contains additional user information and preferences.
    
    Attributes:
        user (User): One-to-one relationship with Django User model
        profile_picture (ImageField): User's profile picture
        bio (TextField): User's biography or description
        dark_mode (BooleanField): User's preference for dark mode
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(blank=True)
    dark_mode = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a UserProfile when a new User is created."""
    if created:
        UserProfile.objects.create(user=instance)
        logger.info(f"User profile created for {instance.username}")

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save the UserProfile when a User is saved."""
    instance.profile.save()
```

### 2.2 Document Models
```python
# cms/models/documents.py
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid

from netctrl.logging_config import get_logger
logger = get_logger(__name__, 'django')

class Category(models.Model):
    """
    Category model for organizing documents.
    
    Attributes:
        name (CharField): The category name
        slug (SlugField): URL-friendly version of the name
        description (TextField): Optional description of the category
        parent (ForeignKey): Optional parent category creating a hierarchy
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """Auto-generate slug if not provided."""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        logger.info(f"Category saved: {self.name}")
    
    def get_absolute_url(self):
        """Get URL for category detail page."""
        return reverse('cms:category_detail', kwargs={'slug': self.slug})

class Tag(models.Model):
    """
    Tag model for categorizing documents.
    
    Attributes:
        name (CharField): The tag name
        slug (SlugField): URL-friendly version of the name
    """
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """Auto-generate slug if not provided."""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        logger.info(f"Tag saved: {self.name}")

class Document(models.Model):
    """
    Document model - the primary content type for the CMS.
    
    Documents have a publishing workflow with draft and published states.
    
    Attributes:
        title (CharField): The document title
        slug (SlugField): URL-friendly version of the title
        content (TextField): The main document content (HTML)
        excerpt (TextField): Short summary or teaser
        author (ForeignKey): User who created the document
        category (ForeignKey): Primary category for the document
        tags (ManyToManyField): Associated tags
        featured_image (ImageField): Main image for the document
        status (CharField): Document status (draft or published)
        created_at (DateTimeField): When the document was created
        updated_at (DateTimeField): When the document was last updated
        published_at (DateTimeField): When the document was published
        uuid (UUIDField): Unique identifier for the document
    """
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='documents')
    tags = models.ManyToManyField(Tag, blank=True, related_name='documents')
    featured_image = models.ImageField(upload_to='documents/featured_images/%Y/%m/', null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        """Auto-generate slug if not provided."""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        logger.info(f"Document saved: {self.title} by {self.author.username}")
    
    def get_absolute_url(self):
        """Get URL for document detail page."""
        return reverse('cms:document_detail', kwargs={'slug': self.slug})
    
    @property
    def is_published(self):
        """Check if document is published."""
        return self.status == 'published'
    
    def publish(self):
        """Publish the document."""
        from django.utils import timezone
        self.status = 'published'
        self.published_at = timezone.now()
        self.save()
        logger.info(f"Document published: {self.title} by {self.author.username}")
```

### 2.3 File Models
```python
# cms/models/files.py
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from chunked_upload.models import ChunkedUpload
import uuid
import os
import mimetypes

from netctrl.logging_config import get_logger
logger = get_logger(__name__, 'django')

class FileCategory(models.Model):
    """
    Category model for organizing files.
    
    Attributes:
        name (CharField): The category name
        slug (SlugField): URL-friendly version of the name
        description (TextField): Optional description of the category
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "File Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """Auto-generate slug if not provided."""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        logger.info(f"File category saved: {self.name}")

class FileTag(models.Model):
    """
    Tags for files to enable filtering and organization.
    
    Attributes:
        name (CharField): The tag name
        slug (SlugField): URL-friendly version of the name
    """
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """Auto-generate slug if not provided."""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        logger.info(f"File tag saved: {self.name}")

class File(models.Model):
    """
    File model for storing uploaded files.
    
    Attributes:
        name (CharField): Name of the file (user-provided)
        file (FileField): The actual file
        original_filename (CharField): Original name of the uploaded file
        file_size (BigIntegerField): Size in bytes
        mime_type (CharField): MIME type of the file
        description (TextField): Optional description
        category (ForeignKey): File category for organization
        tags (ManyToManyField): Tags for filtering
        uploaded_by (ForeignKey): User who uploaded the file
        uploaded_at (DateTimeField): When the file was uploaded
        download_count (PositiveIntegerField): Number of times downloaded
        uuid (UUIDField): Unique identifier for the file
    """
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    original_filename = models.CharField(max_length=255)
    file_size = models.BigIntegerField()
    mime_type = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(FileCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='files')
    tags = models.ManyToManyField(FileTag, blank=True, related_name='files')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_files')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    download_count = models.PositiveIntegerField(default=0)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """Determine MIME type and file size if not already set."""
        # Only do this for new files, not when updating existing records
        if not self.pk and self.file:
            # Set original filename if not already set
            if not self.original_filename:
                self.original_filename = os.path.basename(self.file.name)
            
            # Set file size if not already set
            if not self.file_size:
                self.file_size = self.file.size
            
            # Set MIME type if not already set
            if not self.mime_type:
                self.detect_mime_type()
        
        super().save(*args, **kwargs)
        logger.info(f"File saved: {self.name} ({self.file_size} bytes)")
    
    def detect_mime_type(self):
        """Detect MIME type using python-magic or mimetypes."""
        if not self.file:
            return
        
        # Try to detect using python-magic
        try:
            import magic
            self.mime_type = magic.from_buffer(self.file.read(2048), mime=True)
            self.file.seek(0)  # Reset file pointer
        except (ImportError, Exception):
            # Fallback to mimetypes module
            mime_type, encoding = mimetypes.guess_type(self.file.name)
            self.mime_type = mime_type or 'application/octet-stream'
    
    def get_absolute_url(self):
        """Get URL for file detail page."""
        return reverse('cms:file_detail', kwargs={'uuid': self.uuid})
    
    def record_download(self):
        """Record a file download, incrementing the counter."""
        self.download_count += 1
        self.save(update_fields=['download_count'])
        logger.info(f"File downloaded: {self.name} by user ID {self.uploaded_by.id}")
    
    def file_extension(self):
        """Get the file extension."""
        return os.path.splitext(self.file.name)[1].lstrip('.')
    
    def is_image(self):
        """Check if the file is an image."""
        return self.mime_type.startswith('image/')

class FileChunkedUpload(ChunkedUpload):
    """
    Custom chunked upload model for handling large file uploads.
    
    Extends the base ChunkedUpload model with additional fields.
    
    Attributes:
        Inherits all attributes from ChunkedUpload
        category_id (PositiveIntegerField): Optional category ID for the file
        description (TextField): Optional description for the file
    """
    category_id = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    
    class Meta:
        abstract = False
```

## 3. Authentication & Basic Views (Day 5-6)

### 3.1 Authentication Forms
```python
# cms/forms.py (Authentication section)
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class BootstrapFormMixin:
    """Add Bootstrap 5 classes to form fields."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.__class__.__name__ != 'CheckboxInput':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-check-input'

class UserRegistrationForm(BootstrapFormMixin, UserCreationForm):
    """Form for user registration with Bootstrap styling."""
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        """Validate that the email is unique."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already in use.")
        return email

class LoginForm(BootstrapFormMixin, AuthenticationForm):
    """Custom login form with Bootstrap styling and remember-me option."""
    remember_me = forms.BooleanField(required=False, initial=True)
```

### 3.2 Authentication Views
```python
# cms/views/auth.py
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from ..forms import UserRegistrationForm, UserProfileForm

from netctrl.logging_config import get_logger
logger = get_logger(__name__, 'django')

class RegisterView(CreateView):
    """View for user registration."""
    template_name = 'cms/auth/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('cms:dashboard')
    
    def form_valid(self, form):
        """Log user in after successful registration."""
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        logger.info(f"New user registered: {username}")
        return response

@login_required
def profile_view(request):
    """View for displaying and editing user profile."""
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            logger.info(f"User {request.user.username} updated their profile")
            return redirect('cms:profile')
    else:
        form = UserProfileForm(instance=request.user.profile)
    
    return render(request, 'cms/auth/profile.html', {'form': form})

@login_required
def dashboard_view(request):
    """Dashboard view showing user's documents and files."""
    user_documents = request.user.documents.all()[:5]
    user_files = request.user.uploaded_files.all()[:5]
    
    return render(request, 'cms/dashboard.html', {
        'user_documents': user_documents,
        'user_files': user_files,
    })
```

## 4. File Upload Implementation (Day 7-10)

### 4.1 File Upload Forms
```python
# cms/forms.py (File section)
from django import forms
from .models import File, FileCategory, FileTag

class FileUploadForm(BootstrapFormMixin, forms.ModelForm):
    """Form for file uploading with chunked upload support."""
    class Meta:
        model = File
        fields = ['name', 'description', 'category', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

class FileFilterForm(forms.Form):
    """Form for filtering files."""
    search = forms.CharField(required=False)
    category = forms.ModelChoiceField(
        queryset=FileCategory.objects.all(),
        required=False,
        empty_label="All Categories"
    )
    tag = forms.ModelChoiceField(
        queryset=FileTag.objects.all(),
        required=False,
        empty_label="All Tags"
    )
    sort = forms.ChoiceField(
        choices=[
            ('-uploaded_at', 'Newest First'),
            ('uploaded_at', 'Oldest First'),
            ('name', 'Name (A-Z)'),
            ('-name', 'Name (Z-A)'),
            ('-download_count', 'Most Downloaded'),
        ],
        required=False,
        initial='-uploaded_at'
    )
```

### 4.2 File Upload Views
```python
# cms/views/files.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse, HttpResponse, FileResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from chunked_upload.views import ChunkedUploadView, ChunkedUploadCompleteView

from ..models import File, FileCategory, FileTag, FileChunkedUpload
from ..forms import FileUploadForm, FileFilterForm

from netctrl.logging_config import get_logger
logger = get_logger(__name__, 'django')

class FileListView(ListView):
    """View for listing files with filtering and pagination."""
    model = File
    template_name = 'cms/files/list.html'
    context_object_name = 'files'
    paginate_by = 20
    
    def get_queryset(self):
        """Get filtered queryset based on form data."""
        queryset = File.objects.all()
        
        # Apply search filter
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | 
                Q(description__icontains=search_query)
            )
        
        # Apply category filter
        category_id = self.request.GET.get('category')
        if category_id and category_id.isdigit():
            queryset = queryset.filter(category_id=category_id)
        
        # Apply tag filter
        tag_id = self.request.GET.get('tag')
        if tag_id and tag_id.isdigit():
            queryset = queryset.filter(tags__id=tag_id)
        
        # Apply sorting
        sort_by = self.request.GET.get('sort', '-uploaded_at')
        queryset = queryset.order_by(sort_by)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        """Add filter form to context."""
        context = super().get_context_data(**kwargs)
        context['filter_form'] = FileFilterForm(self.request.GET)
        return context

class FileDetailView(DetailView):
    """View for displaying file details."""
    model = File
    template_name = 'cms/files/detail.html'
    context_object_name = 'file'
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

@login_required
def file_download_view(request, uuid):
    """View for downloading a file and tracking download count."""
    file_obj = get_object_or_404(File, uuid=uuid)
    
    # Record download
    file_obj.record_download()
    
    # Serve the file
    response = FileResponse(file_obj.file, as_attachment=True, filename=file_obj.original_filename)
    return response

@login_required
def file_upload_view(request):
    """View for the file upload form (not the actual upload)."""
    if request.method == 'POST':
        form = FileUploadForm(request.POST)
        if form.is_valid():
            # The actual file processing is done in the ChunkedUploadCompleteView
            return redirect('cms:file_list')
    else:
        form = FileUploadForm()
    
    # Get lists for the frontend
    categories = FileCategory.objects.all()
    tags = FileTag.objects.all()
    
    return render(request, 'cms/files/upload.html', {
        'form': form,
        'categories': categories,
        'tags': tags,
    })

class FileChunkedUploadView(LoginRequiredMixin, ChunkedUploadView):
    """View for handling chunked file uploads."""
    model = FileChunkedUpload
    
    def check_permissions(self, request):
        """Check if user has permission to upload files."""
        # All authenticated users can upload
        return request.user.is_authenticated

class FileChunkedUploadCompleteView(LoginRequiredMixin, ChunkedUploadCompleteView):
    """View for completing chunked uploads and creating File objects."""
    model = FileChunkedUpload
    
    def check_permissions(self, request):
        """Check permissions and ownership."""
        if not request.user.is_authenticated:
            raise PermissionDenied()
            
        # Check ownership of the upload
        upload_id = request.POST.get('upload_id')
        if upload_id:
            chunked_upload = self.get_queryset(request).filter(id=upload_id).first()
            if chunked_upload and chunked_upload.user != request.user:
                raise PermissionDenied()
                
        return True
    
    def on_completion(self, uploaded_file, request):
        """Process the completed upload and create a File object."""
        # Create the file object
        name = request.POST.get('name') or uploaded_file.name
        
        # First detect MIME type (outside model save)
        from ..models.files import File
        file_obj = File(
            name=name,
            file=uploaded_file,
            original_filename=uploaded_file.name,
            file_size=uploaded_file.size,
            uploaded_by=request.user,
            description=request.POST.get('description', '')
        )
        
        # Detect MIME type
        file_obj.detect_mime_type()
        
        # Save the file
        file_obj.save()
        logger.info(f"File upload completed: {file_obj.name} ({file_obj.file_size} bytes)")
        
        # Set category if provided
        category_id = request.POST.get('category')
        if category_id and category_id.isdigit():
            category = FileCategory.objects.filter(pk=int(category_id)).first()
            if category:
                file_obj.category = category
                file_obj.save(update_fields=['category'])
        
        # Add tags if provided
        tag_ids = request.POST.get
