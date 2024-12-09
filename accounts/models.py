from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    notify_on_approval = models.BooleanField(default=False)
    objects = UserManager()

    def save(self, *args, **kwargs):
        # Capitalize first and last names
        if self.first_name:
            self.first_name = self.first_name.capitalize()
        if self.last_name:
            self.last_name = self.last_name.capitalize()
        super().save(*args, **kwargs)

    @property
    def display_name(self):
        # Generate display name as "First L." or just "First" if last_name is missing
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name[0].upper()}."
        elif self.first_name:
            return self.first_name
        return self.username  # Fallback to username if names are missing

    def __str__(self):
        return self.username

# Example of a related model using AUTH_USER_MODEL
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Profile for {self.user.username}"