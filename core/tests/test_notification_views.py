"""Test cases for notification views."""

import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from core.models import Notification

User = get_user_model()


@pytest.fixture
def user(db):
    """Create a test user."""
    return User.objects.create_user(
        username="testuser", email="test@example.com", password="password123"
    )


@pytest.fixture
def notification(user):
    """Create a test notification."""
    return Notification.create_for_user(
        user=user, message="Test notification", notification_type="info", url="/test/"
    )


@pytest.mark.django_db
class TestNotificationViews:
    """Test notification views."""

    def test_mark_notification_as_read(self, client, user, notification):
        """Test marking a notification as read."""
        client.force_login(user)
        response = client.post(
            reverse("core:mark_notification_read", args=[notification.id])
        )
        assert response.status_code == 200
        notification.refresh_from_db()
        assert notification.read_at is not None

    def test_mark_all_notifications_as_read(self, client, user):
        """Test marking all notifications as read."""
        # Create multiple notifications
        notifications = [
            Notification.create_for_user(
                user=user, message=f"Test notification {i}", notification_type="info"
            )
            for i in range(3)
        ]

        client.force_login(user)
        response = client.post(reverse("core:mark_all_notifications_read"))
        assert response.status_code == 200

        # Check all notifications are marked as read
        for notification in notifications:
            notification.refresh_from_db()
            assert notification.read_at is not None

    def test_get_recent_notifications(self, client, user):
        """Test getting recent notifications."""
        # Create multiple notifications
        notifications = [
            Notification.create_for_user(
                user=user, message=f"Test notification {i}", notification_type="info"
            )
            for i in range(5)
        ]

        client.force_login(user)
        response = client.get(reverse("core:recent_notifications"))
        assert response.status_code == 200
        data = response.json()
        assert len(data["notifications"]) == len(notifications)
        assert data["unread_count"] == len(notifications)

    def test_unauthorized_access(self, client, notification):
        """Test unauthorized access to notification endpoints."""
        # Test without login
        response = client.post(
            reverse("core:mark_notification_read", args=[notification.id])
        )
        assert response.status_code == 302  # Redirect to login

        response = client.post(reverse("core:mark_all_notifications_read"))
        assert response.status_code == 302  # Redirect to login

        response = client.get(reverse("core:recent_notifications"))
        assert response.status_code == 302  # Redirect to login

    def test_mark_other_user_notification(self, client, user, notification):
        """Test marking another user's notification as read."""
        other_user = User.objects.create_user(
            username="otheruser", email="other@example.com", password="password123"
        )
        client.force_login(other_user)
        response = client.post(
            reverse("core:mark_notification_read", args=[notification.id])
        )
        assert response.status_code == 404
        notification.refresh_from_db()
        assert notification.read_at is None
