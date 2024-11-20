from django.db import models
from tinymce.models import HTMLField

class WikiPage(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title