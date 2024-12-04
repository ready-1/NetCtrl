from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    notify_on_approval = models.BooleanField(default=False)
    objects = UserManager()

    def __str__(self):
        return self.username

# Example of a related model using AUTH_USER_MODEL
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Profile for {self.user.username}"