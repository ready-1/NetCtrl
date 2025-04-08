"""
User-related models for the NetCtrl CMS.

This module defines models extending Django's User model with additional functionality:
- UserProfile: Extends User with profile picture, bio, and user preferences
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import logging

logger = logging.getLogger(__name__)

class UserProfile(models.Model):
    """
    User profile model extending Django's User model.
    
    Contains additional user information and preferences.
    
    Attributes:
        user (User): One-to-one relationship with Django User model
        profile_picture (ImageField): User's profile picture
        bio (TextField): User's biography or description
        dark_mode (BooleanField): User's preference for dark mode
        date_joined (property): Access to User's date_joined field
        last_login (property): Access to User's last_login field
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(blank=True)
    dark_mode = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    @property
    def date_joined(self):
        """Get the date the user joined from the User model."""
        return self.user.date_joined
    
    @property
    def last_login(self):
        """Get the last login date from the User model."""
        return self.user.last_login

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a UserProfile when a new User is created.
    
    This signal handler is called whenever a User is saved.
    If the User was just created, a new UserProfile is created as well.
    
    Args:
        sender: The model class (User)
        instance: The User instance that was saved
        created: Boolean indicating if this is a new record
        **kwargs: Additional arguments
    """
    if created:
        UserProfile.objects.create(user=instance)
        logger.info(f"Created user profile for {instance.username}")

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Save the UserProfile when a User is saved.
    
    This signal handler ensures the UserProfile is saved whenever 
    the associated User is saved.
    
    Args:
        sender: The model class (User)
        instance: The User instance that was saved
        **kwargs: Additional arguments
    """
    try:
        instance.profile.save()
        logger.info(f"Updated user profile for {instance.username}")
    except UserProfile.DoesNotExist:
        logger.warning(f"UserProfile does not exist for {instance.username}, creating one")
        UserProfile.objects.create(user=instance)
