from django.db import models

from tinymce.models import HTMLField

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField()
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.title