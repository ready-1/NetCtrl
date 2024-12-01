from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    display_name = models.CharField(max_length=50, blank=True, null=True)
    notify_on_approval = models.BooleanField(default=False)