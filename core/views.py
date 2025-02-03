from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .models import AuditLog, Notification

# Create your views here.


class DashboardView(LoginRequiredMixin, TemplateView):
    """
    Main dashboard view for authenticated users.
    """

    template_name = "core/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Dashboard")
        return context


class AuditLogListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    View for listing audit log entries.
    Only accessible by privileged users.
    """

    model = AuditLog
    template_name = "core/audit_log_list.html"
    context_object_name = "audit_logs"
    paginate_by = 50
    ordering = ["-timestamp"]

    def test_func(self):
        """Only allow privileged users to view audit logs"""
        return self.request.user.is_privileged

    def get_queryset(self):
        """Filter audit logs based on query parameters"""
        queryset = super().get_queryset()

        # Apply filters
        filters = {}

        # Filter by user
        user_id = self.request.GET.get("user")
        if user_id:
            filters["user_id"] = user_id

        # Filter by action type
        action = self.request.GET.get("action")
        if action:
            filters["action"] = action

        # Filter by date range
        start_date = self.request.GET.get("start_date")
        if start_date:
            filters["timestamp__gte"] = start_date

        end_date = self.request.GET.get("end_date")
        if end_date:
            filters["timestamp__lte"] = end_date

        # Apply all filters
        return queryset.filter(**filters)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Audit Logs")
        context["action_choices"] = AuditLog.ACTION_CHOICES
        return context


@login_required
def mark_notification_read(request, notification_id):
    """Mark a notification as read."""
    notification = get_object_or_404(
        Notification, id=notification_id, user=request.user
    )
    notification.mark_as_read()
    return JsonResponse({"status": "success"})


@login_required
def mark_all_notifications_read(request):
    """Mark all notifications as read."""
    Notification.objects.filter(user=request.user, read_at__isnull=True).update(
        read_at=timezone.now()
    )
    return JsonResponse({"status": "success"})


@login_required
def get_notifications(request):
    """Get recent notifications for the current user."""
    notifications = Notification.objects.filter(user=request.user).order_by(
        "-created_at"
    )[:5]
    return JsonResponse(
        {
            "notifications": [
                {
                    "id": n.id,
                    "message": n.message,
                    "url": n.url,
                    "type": n.type,
                    "read": n.read_at is not None,
                    "created_at": n.created_at.isoformat(),
                }
                for n in notifications
            ]
        }
    )


@login_required
def profile(request):
    """User profile view."""
    if request.method == "POST":
        # Handle profile update
        pass
    return render(
        request, "core/profile.html", {"title": _("Profile"), "user": request.user}
    )


@login_required
def preferences(request):
    """User preferences view."""
    if request.method == "POST":
        # Handle preferences update
        pass
    return render(
        request,
        "core/preferences.html",
        {"title": _("Preferences"), "user": request.user},
    )
