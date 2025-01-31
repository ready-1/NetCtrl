from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractUser):
    """
    Custom user model for NetCtrl.
    Extends Django's AbstractUser to add role-based permissions and additional fields.
    """

    # Constants for user roles
    ROLE_NON_PRIVILEGED = "non_privileged"
    ROLE_PRIVILEGED = "privileged"
    ROLE_SUPERUSER = "superuser"

    ROLE_CHOICES = [
        (ROLE_NON_PRIVILEGED, _("Non-Privileged")),
        (ROLE_PRIVILEGED, _("Privileged")),
        (ROLE_SUPERUSER, _("Superuser")),
    ]

    # Additional fields
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=ROLE_NON_PRIVILEGED,
        verbose_name=_("Role"),
        help_text=_("User role determines access permissions"),
    )
    last_activity = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Last Activity"),
        help_text=_("Last time the user performed an action"),
    )
    api_access = models.BooleanField(
        default=False,
        verbose_name=_("API Access"),
        help_text=_("Whether the user can access the API"),
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    def save(self, *args, **kwargs):
        # Automatically set role based on permissions
        if self.is_superuser:
            self.role = self.ROLE_SUPERUSER
        elif self.is_staff:
            self.role = self.ROLE_PRIVILEGED
        super().save(*args, **kwargs)

    @property
    def is_privileged(self):
        """Check if user has privileged access"""
        return self.is_staff or self.is_superuser

    @property
    def role_display(self):
        """Get the display name of the user's role"""
        return dict(self.ROLE_CHOICES).get(self.role, self.role)
