from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
import json
from django.utils import timezone


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
        help_text=_("User's role in the system"),
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


class AuditLog(models.Model):
    """
    Audit log for tracking all system actions.
    Uses generic foreign keys to link to any model instance.
    """

    # Action types
    ACTION_CREATE = "create"
    ACTION_UPDATE = "update"
    ACTION_DELETE = "delete"
    ACTION_VIEW = "view"
    ACTION_LOGIN = "login"
    ACTION_LOGOUT = "logout"
    ACTION_API = "api"
    ACTION_OTHER = "other"

    ACTION_CHOICES = [
        (ACTION_CREATE, _("Create")),
        (ACTION_UPDATE, _("Update")),
        (ACTION_DELETE, _("Delete")),
        (ACTION_VIEW, _("View")),
        (ACTION_LOGIN, _("Login")),
        (ACTION_LOGOUT, _("Logout")),
        (ACTION_API, _("API Access")),
        (ACTION_OTHER, _("Other")),
    ]

    # Core fields
    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Timestamp"),
        help_text=_("When the action occurred"),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="audit_logs",
        verbose_name=_("User"),
        help_text=_("User who performed the action"),
    )
    action = models.CharField(
        max_length=20,
        choices=ACTION_CHOICES,
        verbose_name=_("Action"),
        help_text=_("Type of action performed"),
    )
    description = models.TextField(
        verbose_name=_("Description"), help_text=_("Description of the action")
    )
    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True,
        verbose_name=_("IP Address"),
        help_text=_("IP address of the user"),
    )

    # Target object fields (using generic foreign key)
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Content Type"),
        help_text=_("Type of the target object"),
    )
    object_id = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Object ID"),
        help_text=_("ID of the target object"),
    )
    target = GenericForeignKey("content_type", "object_id")

    # Additional data
    changes = models.JSONField(
        null=True,
        blank=True,
        verbose_name=_("Changes"),
        help_text=_("JSON representation of the changes made"),
    )
    metadata = models.JSONField(
        null=True,
        blank=True,
        verbose_name=_("Metadata"),
        help_text=_("Additional metadata about the action"),
    )

    class Meta:
        verbose_name = _("Audit Log")
        verbose_name_plural = _("Audit Logs")
        ordering = ["-timestamp"]
        indexes = [
            models.Index(fields=["-timestamp"]),
            models.Index(fields=["user"]),
            models.Index(fields=["action"]),
            models.Index(fields=["content_type", "object_id"]),
        ]

    def __str__(self):
        return f"{self.get_action_display()} by {self.user} at {self.timestamp}"

    def set_changes(self, old_data, new_data):
        """
        Compare old and new data to generate a changes dictionary
        """
        if not old_data or not new_data:
            self.changes = {"old": old_data, "new": new_data}
            return

        changes = {"modified": {}}
        for key in set(old_data) | set(new_data):
            old_value = old_data.get(key)
            new_value = new_data.get(key)
            if old_value != new_value:
                changes["modified"][key] = {"old": old_value, "new": new_value}
        self.changes = changes

    def add_metadata(self, **kwargs):
        """
        Add additional metadata to the audit log
        """
        if not self.metadata:
            self.metadata = {}
        self.metadata.update(kwargs)


class Notification(models.Model):
    """Model for system notifications."""

    TYPE_CHOICES = [
        ("success", "Success"),
        ("warning", "Warning"),
        ("error", "Error"),
        ("info", "Information"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications"
    )
    message = models.TextField()
    url = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default="info")

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["user", "-created_at"]),
            models.Index(fields=["user", "read_at"]),
        ]

    def __str__(self):
        return f"{self.user} - {self.message[:50]}"

    def mark_as_read(self):
        """Mark the notification as read."""
        if not self.read_at:
            self.read_at = timezone.now()
            self.save(update_fields=["read_at"])

    @classmethod
    def create_for_user(cls, user, message, notification_type="info", url=""):
        """Create a notification for a specific user."""
        return cls.objects.create(
            user=user, message=message, type=notification_type, url=url
        )
