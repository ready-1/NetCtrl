from django.db.models import Q
from django.utils import timezone
from datetime import timedelta
from .models import Notification


def notifications(request):
    """
    Context processor that provides notification data for the current user.
    """
    if not request.user.is_authenticated:
        return {"notifications": [], "unread_notifications_count": 0}

    # Get recent notifications (last 30 days)
    thirty_days_ago = timezone.now() - timedelta(days=30)
    notifications = Notification.objects.filter(
        user=request.user, created_at__gte=thirty_days_ago
    ).order_by("-created_at")[
        :5
    ]  # Show only 5 most recent

    # Count unread notifications
    unread_count = Notification.objects.filter(
        user=request.user, read_at__isnull=True
    ).count()

    return {"notifications": notifications, "unread_notifications_count": unread_count}


def dark_mode(request):
    """Context processor that provides dark mode state."""
    return {"dark_mode": False}
