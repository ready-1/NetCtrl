# Django Implementation Plan (Continued)

*This is a continuation of the django_implementation_plan.md file*

## 4. File Upload Implementation (continued)

### 4.2 File Upload Views (continued)
```python
# Continuing from the on_completion method
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
        tag_ids = request.POST.getlist('tags')
        if tag_ids:
            # Batch fetch tags to avoid N+1 query issue
            tags = FileTag.objects.filter(pk__in=tag_ids)
            file_obj.tags.add(*tags)
        
        return JsonResponse({
            'success': True,
            'file_id': file_obj.id,
            'file_uuid': str(file_obj.uuid),
            'url': file_obj.get_absolute_url()
        })
```

### 4.3 Frontend JavaScript for Chunked Upload
```javascript
// static/js/chunked-upload.js
document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('file-upload-form');
    const fileInput = document.getElementById('id_file');
    const progressContainer = document.getElementById('progress-container');
    const progressBar = document.getElementById('progress-bar');
    const progressText = document.getElementById('progress-text');
    const uploadButton = document.getElementById('upload-button');
    
    // If upload form doesn't exist on this page, exit
    if (!uploadForm) return;
    
    // Constants
    const CHUNK_SIZE = 2 * 1024 * 1024; // 2MB chunks
    let file = null;
    let uploadId = null;
    let fileName = '';
    let offset = 0;
    let totalChunks = 0;
    let currentChunk = 0;
    
    fileInput.addEventListener('change', function(e) {
        file = e.target.files[0];
        if (file) {
            fileName = file.name;
            document.getElementById('file-name').textContent = fileName;
            document.getElementById('file-size').textContent = formatFileSize(file.size);
            document.getElementById('file-type').textContent = file.type || 'Unknown';
            
            // Enable upload button
            uploadButton.disabled = false;
        }
    });
    
    uploadForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        if (!file) {
            alert('Please select a file first');
            return;
        }
        
        // Initialize upload
        resetUpload();
        startUpload();
    });
    
    function resetUpload() {
        offset = 0;
        uploadId = null;
        currentChunk = 0;
        totalChunks = Math.ceil(file.size / CHUNK_SIZE);
        
        // Show progress bar
        progressContainer.style.display = 'block';
        progressBar.style.width = '0%';
        progressText.textContent = '0%';
    }
    
    async function startUpload() {
        // Disable form during upload
        uploadButton.disabled = true;
        
        try {
            // Upload all chunks sequentially
            for (let i = 0; i < totalChunks; i++) {
                const start = i * CHUNK_SIZE;
                const end = Math.min(file.size, start + CHUNK_SIZE);
                const chunk = file.slice(start, end);
                
                // Upload this chunk
                await uploadChunk(chunk, start);
                
                // Update progress
                currentChunk++;
                const progress = Math.round((currentChunk / totalChunks) * 100);
                progressBar.style.width = progress + '%';
                progressText.textContent = progress + '%';
            }
            
            // Complete the upload
            await completeUpload();
            
        } catch (error) {
            console.error('Upload failed:', error);
            alert('Upload failed: ' + error.message);
            uploadButton.disabled = false;
        }
    }
    
    async function uploadChunk(chunk, start) {
        const formData = new FormData();
        
        // Add CSRF token
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        formData.append('csrfmiddlewaretoken', csrfToken);
        
        // Add the file information
        formData.append('file', chunk, fileName);
        formData.append('filename', fileName);
        
        // If we already have an upload ID, include it
        if (uploadId) {
            formData.append('upload_id', uploadId);
        }
        
        // Include the offset
        formData.append('offset', start);
        
        // Send the request
        const response = await fetch('/cms/uploads/chunked/', {
            method: 'POST',
            body: formData,
            credentials: 'same-origin'
        });
        
        if (!response.ok) {
            throw new Error('Failed to upload chunk');
        }
        
        const data = await response.json();
        
        // Store the upload ID for subsequent chunks
        if (data.upload_id) {
            uploadId = data.upload_id;
        }
    }
    
    async function completeUpload() {
        if (!uploadId) {
            throw new Error('No upload ID available');
        }
        
        const formData = new FormData();
        
        // Add CSRF token
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        formData.append('csrfmiddlewaretoken', csrfToken);
        
        // Add the upload ID
        formData.append('upload_id', uploadId);
        
        // Add form data
        formData.append('name', document.getElementById('id_name').value);
        formData.append('description', document.getElementById('id_description').value);
        
        // Add category if selected
        const categorySelect = document.getElementById('id_category');
        if (categorySelect && categorySelect.value) {
            formData.append('category', categorySelect.value);
        }
        
        // Add tags if selected
        const selectedTags = [];
        document.querySelectorAll('input[name="tags"]:checked').forEach(tag => {
            selectedTags.push(tag.value);
        });
        if (selectedTags.length > 0) {
            formData.append('tags', selectedTags.join(','));
        }
        
        // Send the request
        const response = await fetch('/cms/uploads/chunked/complete/', {
            method: 'POST',
            body: formData,
            credentials: 'same-origin'
        });
        
        if (!response.ok) {
            throw new Error('Failed to complete upload');
        }
        
        const data = await response.json();
        
        if (data.success) {
            // Show success message
            progressContainer.innerHTML = '<div class="alert alert-success">Upload complete!</div>';
            
            // Redirect to the file detail page after a short delay
            setTimeout(() => {
                window.location.href = data.url;
            }, 1500);
        } else {
            throw new Error(data.error || 'Unknown error');
        }
    }
    
    function formatFileSize(bytes) {
        if (bytes === 0) return '0 Bytes';
        
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    }
});
```

## 5. Templates and Frontend (Day 11-14)

### 5.1 Base Template
```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en" data-bs-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}NetCtrl{% endblock %}</title>
    <!-- Bootstrap 5.3 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Bootstrap Icons -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css" rel="stylesheet">
    <!-- Custom CSS -->
    <link href="{% static 'css/style.css' %}" rel="stylesheet">
    {% block extra_css %}{% endblock %}
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="{% url 'cms:dashboard' %}">NetCtrl</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarMain">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarMain">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'cms:dashboard' %}">Dashboard</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'cms:document_list' %}">Documents</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'cms:file_list' %}">Files</a>
                    </li>
                </ul>
                <ul class="navbar-nav">
                    {% if user.is_authenticated %}
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" id="userDropdown" role="button" data-bs-toggle="dropdown">
                                {{ user.username }}
                            </a>
                            <ul class="dropdown-menu dropdown-menu-end">
                                <li><a class="dropdown-item" href="{% url 'cms:profile' %}">Profile</a></li>
                                {% if user.is_staff %}
                                    <li><a class="dropdown-item" href="{% url 'admin:index' %}">Admin</a></li>
                                {% endif %}
                                <li><hr class="dropdown-divider"></li>
                                <li>
                                    <form method="post" action="{% url 'logout' %}">
                                        {% csrf_token %}
                                        <button type="submit" class="dropdown-item">Logout</button>
                                    </form>
                                </li>
                            </ul>
                        </li>
                        <li class="nav-item">
                            <button class="btn btn-outline-light ms-2" id="darkModeToggle">
                                <i class="bi bi-moon"></i>
                            </button>
                        </li>
                    {% else %}
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'login' %}">Login</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'cms:register' %}">Register</a>
                        </li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="container mt-4 mb-5">
        {% if messages %}
            <div class="messages">
                {% for message in messages %}
                    <div class="alert alert-{{ message.tags }} alert-dismissible fade show">
                        {{ message }}
                        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                    </div>
                {% endfor %}
            </div>
        {% endif %}
        
        {% block content %}{% endblock %}
    </main>

    <!-- Footer -->
    <footer class="bg-light py-4 mt-auto">
        <div class="container">
            <div class="row">
                <div class="col-md-6">
                    <p class="mb-0">&copy; 2025 NetCtrl. All rights reserved.</p>
                </div>
                <div class="col-md-6 text-md-end">
                    <p class="mb-0">Version 1.0.0</p>
                </div>
            </div>
        </div>
    </footer>

    <!-- Bootstrap JS Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    
    <!-- Dark Mode Script -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const darkModeToggle = document.getElementById('darkModeToggle');
            const htmlElement = document.documentElement;
            const isDarkMode = localStorage.getItem('darkMode') === 'true';
            
            // Set initial state
            if (isDarkMode) {
                htmlElement.setAttribute('data-bs-theme', 'dark');
                darkModeToggle.innerHTML = '<i class="bi bi-sun"></i>';
            }
            
            // Toggle dark mode
            darkModeToggle.addEventListener('click', function() {
                const currentTheme = htmlElement.getAttribute('data-bs-theme');
                const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                
                htmlElement.setAttribute('data-bs-theme', newTheme);
                localStorage.setItem('darkMode', newTheme === 'dark');
                
                // Update the icon
                darkModeToggle.innerHTML = newTheme === 'dark' 
                    ? '<i class="bi bi-sun"></i>' 
                    : '<i class="bi bi-moon"></i>';
                
                // If user is logged in, save preference to profile
                {% if user.is_authenticated %}
                fetch('{% url "cms:update_dark_mode" %}', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': '{{ csrf_token }}'
                    },
                    body: JSON.stringify({ dark_mode: newTheme === 'dark' })
                });
                {% endif %}
            });
        });
    </script>
    
    {% block extra_js %}{% endblock %}
</body>
</html>
```

### 5.2 File Upload Template
```html
<!-- templates/cms/files/upload.html -->
{% extends "base.html" %}
{% load static %}

{% block title %}Upload File - NetCtrl{% endblock %}

{% block extra_css %}
<style>
    .drop-zone {
        border: 2px dashed #ccc;
        border-radius: 5px;
        padding: 40px;
        text-align: center;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .drop-zone:hover {
        background-color: #f8f9fa;
    }
    .drop-zone.active {
        background-color: #e9ecef;
        border-color: #6c757d;
    }
    .file-info {
        margin-top: 20px;
        display: none;
    }
    #progress-container {
        margin-top: 20px;
        display: none;
    }
</style>
{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-8 offset-md-2">
        <div class="card">
            <div class="card-header">
                <h4>Upload File</h4>
            </div>
            <div class="card-body">
                <form id="file-upload-form" method="post" enctype="multipart/form-data">
                    {% csrf_token %}
                    
                    <div class="drop-zone" id="drop-zone">
                        <p>Drag and drop a file here or click to select</p>
                        <input type="file" id="id_file" name="file" hidden>
                        <button type="button" class="btn btn-primary" id="browse-button">Browse Files</button>
                    </div>
                    
                    <div class="file-info" id="file-info">
                        <div class="card bg-light">
                            <div class="card-body">
                                <h5 class="card-title">File Information</h5>
                                <p><strong>Name:</strong> <span id="file-name"></span></p>
                                <p><strong>Size:</strong> <span id="file-size"></span></p>
                                <p><strong>Type:</strong> <span id="file-type"></span></p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="mb-3 mt-4">
                        <label for="id_name" class="form-label">Display Name</label>
                        <input type="text" class="form-control" id="id_name" name="name" required>
                    </div>
                    
                    <div class="mb-3">
                        <label for="id_description" class="form-label">Description</label>
                        <textarea class="form-control" id="id_description" name="description" rows="3"></textarea>
                    </div>
                    
                    <div class="mb-3">
                        <label for="id_category" class="form-label">Category</label>
                        <select class="form-select" id="id_category" name="category">
                            <option value="">Select a category</option>
                            {% for category in categories %}
                                <option value="{{ category.id }}">{{ category.name }}</option>
                            {% endfor %}
                        </select>
                    </div>
                    
                    <div class="mb-3">
                        <label class="form-label">Tags</label>
                        <div class="row">
                            {% for tag in tags %}
                                <div class="col-md-4">
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" value="{{ tag.id }}" id="tag_{{ tag.id }}" name="tags">
                                        <label class="form-check-label" for="tag_{{ tag.id }}">
                                            {{ tag.name }}
                                        </label>
                                    </div>
                                </div>
                            {% endfor %}
                        </div>
                    </div>
                    
                    <div id="progress-container">
                        <div class="progress">
                            <div id="progress-bar" class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" style="width: 0%"></div>
                        </div>
                        <p class="text-center mt-2"><span id="progress-text">0%</span></p>
                    </div>
                    
                    <div class="mt-4">
                        <button type="submit" class="btn btn-success" id="upload-button" disabled>Upload File</button>
                        <a href="{% url 'cms:file_list' %}" class="btn btn-secondary">Cancel</a>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}

{% block extra_js %}
<script src="{% static 'js/chunked-upload.js' %}"></script>
<script>
    // Handle drag and drop functionality
    document.addEventListener('DOMContentLoaded', function() {
        const dropZone = document.getElementById('drop-zone');
        const fileInput = document.getElementById('id_file');
        const browseButton = document.getElementById('browse-button');
        const fileInfo = document.getElementById('file-info');
        
        browseButton.addEventListener('click', function() {
            fileInput.click();
        });
        
        dropZone.addEventListener('dragover', function(e) {
            e.preventDefault();
            dropZone.classList.add('active');
        });
        
        dropZone.addEventListener('dragleave', function() {
            dropZone.classList.remove('active');
        });
        
        dropZone.addEventListener('drop', function(e) {
            e.preventDefault();
            dropZone.classList.remove('active');
            
            if (e.dataTransfer.files.length) {
                fileInput.files = e.dataTransfer.files;
                // Trigger change event
                const event = new Event('change', { bubbles: true });
                fileInput.dispatchEvent(event);
            }
        });
        
        fileInput.addEventListener('change', function() {
            if (fileInput.files.length > 0) {
                fileInfo.style.display = 'block';
            } else {
                fileInfo.style.display = 'none';
            }
        });
    });
</script>
{% endblock %}
```

## 6. Basic Testing (Day 15)

### 6.1 Model Tests
```python
# cms/tests/test_models.py
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from ..models import Document, Category, Tag, File, FileCategory, FileTag
import tempfile
import os

class DocumentModelTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123'
        )
        
        # Create a test category
        self.category = Category.objects.create(
            name='Test Category',
            slug='test-category'
        )
        
        # Create a test tag
        self.tag = Tag.objects.create(
            name='Test Tag',
            slug='test-tag'
        )
    
    def test_document_creation(self):
        # Create a document
        document = Document.objects.create(
            title='Test Document',
            content='This is a test document.',
            author=self.user,
            category=self.category
        )
        document.tags.add(self.tag)
        
        # Check attributes
        self.assertEqual(document.title, 'Test Document')
        self.assertEqual(document.content, 'This is a test document.')
        self.assertEqual(document.author, self.user)
        self.assertEqual(document.category, self.category)
        self.assertEqual(document.tags.count(), 1)
        self.assertEqual(document.tags.first(), self.tag)
        
        # Check slug generation
        self.assertEqual(document.slug, 'test-document')
        
        # Check status
        self.assertEqual(document.status, 'draft')
        self.assertFalse(document.is_published)
        
        # Test the publish method
        document.publish()
        self.assertEqual(document.status, 'published')
        self.assertTrue(document.is_published)
        self.assertIsNotNone(document.published_at)

class FileModelTests(TestCase):
    def setUp(self):
        # Create temporary directory for test files
        self.temp_dir = tempfile.mkdtemp()
        
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123'
        )
        
        # Create a test category
        self.category = FileCategory.objects.create(
            name='Test Category',
            slug='test-category'
        )
        
        # Create a test tag
        self.tag = FileTag.objects.create(
            name='Test Tag',
            slug='test-tag'
        )
        
        # Create a test file
        self.test_file_content = b'Test file content'
        self.test_file = SimpleUploadedFile(
            'test_file.txt',
            self.test_file_content,
            content_type='text/plain'
        )
    
    def tearDown(self):
        # Clean up any test files
        for file_obj in File.objects.all():
            if file_obj.file and os.path.exists(file_obj.file.path):
                os.unlink(file_obj.file.path)
    
    def test_file_creation(self):
        # Create a file
        file_obj = File.objects.create(
            name='Test File',
            file=self.test_file,
            original_filename='test_file.txt',
            file_size=len(self.test_file_content),
            mime_type='text/plain',
            uploaded_by=self.user
        )
        file_obj.tags.add(self.tag)
        
        # Check attributes
        self.assertEqual(file_obj.name, 'Test File')
        self.assertEqual(file_obj.original_filename, 'test_file.txt')
        self.assertEqual(file_obj.file_size, len(self.test_file_content))
        self.assertEqual(file_obj.mime_type, 'text/plain')
        self.assertEqual(file_obj.uploaded_by, self.user)
        self.assertEqual(file_obj.tags.count(), 1)
        self.assertEqual(file_obj.tags.first(), self.tag)
        
        # Test download count
        self.assertEqual(file_obj.download_count, 0)
        file_obj.record_download()
        self.assertEqual(file_obj.download_count, 1)
        
        # Test helper methods
        self.assertEqual(file_obj.file_extension(), 'txt')
        self.assertFalse(file_obj.is_image())
```

### 6.2 View Tests
```python
# cms/tests/test_views.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from ..models import File, FileCategory, FileTag, FileChunkedUpload
import tempfile
import os

class FileViewsTests(TestCase):
    def setUp(self):
        # Create temporary directory for test files
        self.temp_dir = tempfile.mkdtemp()
        
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123'
        )
        
        # Create an admin user
        self.admin = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )
        
        # Create a test category
        self.category = FileCategory.objects.create(
            name='Test Category',
            slug='test-category'
        )
        
        # Create a test tag
        self.tag = FileTag.objects.create(
            name='Test Tag',
            slug='test-tag'
        )
        
        # Create a test file
        self.test_file_content = b'Test file content'
        self.test_file = SimpleUploadedFile(
            'test_file.txt',
            self.test_file_content,
            content_type='text/plain'
        )
        
        # Create a test file in the database
        self.file = File.objects.create(
            name='Test File',
            file=self.test_file,
            original_filename='test_file.txt',
            file_size=len(self.test_file_content),
            mime_type='text/plain',
            uploaded_by=self.user
        )
        
        # Set up client
        self.client = Client()
    
    def tearDown(self):
        # Clean up any test files
        for file_obj in File.objects.all():
            if file_obj.file and os.path.exists(file_obj.file.path):
                os.unlink(file_obj.file.path)
    
    def test_file_list_view(self):
        # Test unauthenticated access
        response = self.client.get(reverse('cms:file_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test File')
        
        # Test authenticated access
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('cms:file_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test File')
    
    def test_file_detail_view(self):
        # Test unauthenticated access
        response = self.client.get(reverse('cms:file_detail', kwargs={'uuid': self.file.uuid}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test File')
        
        # Test authenticated access
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('cms:file_detail', kwargs={'uuid': self.file.uuid}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test File')
    
    def test_file_download_view(self):
        # Test unauthenticated access (should redirect to login)
        response = self.client.get(reverse('cms:file_download', kwargs={'uuid': self.file.uuid}))
        self.assertEqual(response.status_code, 302)
        
        # Test authenticated access
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('cms:file_download', kwargs={'uuid': self.file.uuid}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get('Content-Disposition'), f'attachment; filename=test_file.txt')
        
        # Check that download count was incremented
        self.file.refresh_from_db()
        self.assertEqual(self.file.download_count, 1)
    
    def test_file_upload_view(self):
        # Test unauthenticated access (should redirect to login)
        response = self.client.get(reverse('cms:file_upload'))
        self.assertEqual(response.status_code, 302)
        
        # Test authenticated access
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('cms:file_upload'))
        self.assertEqual
