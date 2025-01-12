"""
Models for the dashboard app.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model with approval status."""
    
    is_approved = models.BooleanField(default=False)
    approval_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'netctrl_user'
        
    def save(self, *args, **kwargs):
        """Override save to handle group assignment on approval."""
        if self.is_approved and not self.approval_date:
            from django.utils import timezone
            from django.contrib.auth.models import Group
            
            self.approval_date = timezone.now()
            
            # Add user to operators group if approved
            try:
                operators_group = Group.objects.get(name='operators')
                self.groups.add(operators_group)
            except Group.DoesNotExist:
                pass  # Group will be created in migrations
            
        super().save(*args, **kwargs)
