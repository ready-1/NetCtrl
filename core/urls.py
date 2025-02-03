from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("audit-logs/", views.AuditLogListView.as_view(), name="audit_logs"),
    path("notifications/", views.get_notifications, name="notifications"),
    path(
        "notifications/mark-read/<int:notification_id>/",
        views.mark_notification_read,
        name="mark-notification-read",
    ),
    path(
        "notifications/mark-all-read/",
        views.mark_all_notifications_read,
        name="mark-all-notifications-read",
    ),
]
