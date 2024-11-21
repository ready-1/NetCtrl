import os
from io import BytesIO
from django.db import models
from tinymce.models import HTMLField
from django.core.files.base import ContentFile
from taggit.managers import TaggableManager
from PIL import Image


class WikiPage(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class FileUpload(models.Model):
    file = models.FileField(upload_to="uploads/")
    thumbnail = models.ImageField(upload_to="thumbnails/", blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    tags = TaggableManager()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Generate thumbnail for images
        if self.file and not self.thumbnail and self.is_image():
            self.thumbnail = self.create_thumbnail(self.file)
        super().save(*args, **kwargs)

    def create_thumbnail(self, file):
        # Open the uploaded image
        with Image.open(file) as img:
            img.thumbnail((150, 150))  # Set thumbnail size
            thumb_io = BytesIO()
            img.save(thumb_io, format=img.format)
            thumbnail_name = f"thumb_{file.name.split('/')[-1]}"
            return ContentFile(thumb_io.getvalue(), name=thumbnail_name)

    def is_image(self):
        # Check if the file is an image based on its extension
        return self.file.name.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))

    def delete(self, *args, **kwargs):
        # Delete associated file and thumbnail from the filesystem
        if self.file and os.path.isfile(self.file.path):
            os.remove(self.file.path)
        if self.thumbnail and os.path.isfile(self.thumbnail.path):
            os.remove(self.thumbnail.path)
        super().delete(*args, **kwargs)
