"""Utility functions for creating notifications."""

from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from core.models import Notification

User = get_user_model()


def notify_switch_status_change(switch, old_status, new_status):
    """Create notifications for switch status changes."""
    # Notify all privileged users and superusers
    users = User.objects.filter(role__in=[User.ROLE_PRIVILEGED, User.ROLE_SUPERUSER])
    message = _(
        f"Switch {switch.name} status changed from {old_status} to {new_status}"
    )

    for user in users:
        Notification.create_for_user(
            user=user,
            message=message,
            notification_type="warning" if new_status == "down" else "info",
            url=f"/switches/{switch.id}/",
        )


def notify_config_change(config, user):
    """Create notifications for configuration changes."""
    # Notify all privileged users and superusers except the user who made the change
    users = User.objects.filter(
        role__in=[User.ROLE_PRIVILEGED, User.ROLE_SUPERUSER]
    ).exclude(id=user.id)

    message = _(
        f"Configuration updated for switch {config.switch.name} by {user.username}"
    )

    for recipient in users:
        Notification.create_for_user(
            user=recipient,
            message=message,
            notification_type="info",
            url=f"/switches/{config.switch.id}/config/",
        )


def notify_backup_failure(switch, error_message):
    """Create notifications for backup failures."""
    # Notify all superusers
    users = User.objects.filter(role=User.ROLE_SUPERUSER)
    message = _(f"Backup failed for switch {switch.name}: {error_message}")

    for user in users:
        Notification.create_for_user(
            user=user,
            message=message,
            notification_type="error",
            url=f"/switches/{switch.id}/backups/",
        )


def notify_port_profile_change(port_profile, switch, user):
    """Create notifications for port profile changes."""
    # Notify all privileged users and superusers except the user who made the change
    users = User.objects.filter(
        role__in=[User.ROLE_PRIVILEGED, User.ROLE_SUPERUSER]
    ).exclude(id=user.id)

    message = _(
        f"Port profile '{port_profile.name}' applied to switch {switch.name} by {user.username}"
    )

    for recipient in users:
        Notification.create_for_user(
            user=recipient,
            message=message,
            notification_type="info",
            url=f"/switches/{switch.id}/ports/",
        )


def notify_system_error(error_message):
    """Create notifications for system-level errors."""
    # Notify all superusers
    users = User.objects.filter(role=User.ROLE_SUPERUSER)
    message = _(f"System Error: {error_message}")

    for user in users:
        Notification.create_for_user(
            user=user, message=message, notification_type="error"
        )
