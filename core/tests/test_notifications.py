"""Test cases for the notification system."""

import pytest
from django.utils import timezone
from django.contrib.auth import get_user_model
from core.models import Notification
from core.utils.notifications import (
    notify_switch_status_change,
    notify_config_change,
    notify_backup_failure,
    notify_port_profile_change,
    notify_system_error,
)
from switches.models import Switch

User = get_user_model()


@pytest.fixture
def users(db):
    """Create test users with different roles."""
    superuser = User.objects.create_superuser(
        username="superuser",
        email="super@example.com",
        password="password123",
        role=User.ROLE_SUPERUSER,
    )
    privileged = User.objects.create_user(
        username="privileged",
        email="privileged@example.com",
        password="password123",
        role=User.ROLE_PRIVILEGED,
    )
    non_privileged = User.objects.create_user(
        username="non_privileged",
        email="non@example.com",
        password="password123",
        role=User.ROLE_NON_PRIVILEGED,
    )
    return {
        "superuser": superuser,
        "privileged": privileged,
        "non_privileged": non_privileged,
    }


@pytest.fixture
def switch(db):
    """Create a test switch."""
    return Switch.objects.create(
        name="Test Switch",
        ip_address="192.168.1.1",
        username="admin",
        password="password123",
    )


@pytest.mark.django_db
class TestNotificationModel:
    """Test cases for the Notification model."""

    def test_notification_creation(self, users):
        """Test creating a notification."""
        notification = Notification.create_for_user(
            user=users["superuser"],
            message="Test notification",
            notification_type="info",
            url="/test/",
        )
        assert notification.pk is not None
        assert notification.message == "Test notification"
        assert notification.type == "info"
        assert notification.url == "/test/"
        assert notification.read_at is None

    def test_mark_as_read(self, users):
        """Test marking a notification as read."""
        notification = Notification.create_for_user(
            user=users["superuser"], message="Test notification"
        )
        assert notification.read_at is None
        notification.mark_as_read()
        assert notification.read_at is not None


@pytest.mark.django_db
class TestNotificationUtils:
    """Test cases for notification utility functions."""

    def test_notify_switch_status_change(self, users, switch):
        """Test switch status change notifications."""
        old_status = "up"
        new_status = "down"
        notify_switch_status_change(switch, old_status, new_status)

        # Check that superuser and privileged users got notifications
        assert Notification.objects.filter(user=users["superuser"]).exists()
        assert Notification.objects.filter(user=users["privileged"]).exists()
        assert not Notification.objects.filter(user=users["non_privileged"]).exists()

        # Check notification content
        notification = Notification.objects.get(user=users["superuser"])
        assert switch.name in notification.message
        assert old_status in notification.message
        assert new_status in notification.message
        assert notification.type == "warning"

    def test_notify_system_error(self, users):
        """Test system error notifications."""
        error_message = "Test error message"
        notify_system_error(error_message)

        # Only superusers should get system error notifications
        assert Notification.objects.filter(user=users["superuser"]).exists()
        assert not Notification.objects.filter(user=users["privileged"]).exists()
        assert not Notification.objects.filter(user=users["non_privileged"]).exists()

        # Check notification content
        notification = Notification.objects.get(user=users["superuser"])
        assert error_message in notification.message
        assert notification.type == "error"

    def test_notify_backup_failure(self, users, switch):
        """Test backup failure notifications."""
        error_message = "Backup failed"
        notify_backup_failure(switch, error_message)

        # Only superusers should get backup failure notifications
        assert Notification.objects.filter(user=users["superuser"]).exists()
        assert not Notification.objects.filter(user=users["privileged"]).exists()
        assert not Notification.objects.filter(user=users["non_privileged"]).exists()

        # Check notification content
        notification = Notification.objects.get(user=users["superuser"])
        assert switch.name in notification.message
        assert error_message in notification.message
        assert notification.type == "error"
        assert f"/switches/{switch.id}/backups/" in notification.url
