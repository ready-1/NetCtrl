from django.utils import timezone
from django.http import HttpResponse
from .models import User, AuditLog


class AuditLogMiddleware:
    """
    Middleware to automatically log requests and update user activity.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process the request
        response = self.get_response(request)
        if not isinstance(response, HttpResponse):
            response = HttpResponse()

        # Skip logging for static and media files
        if any(path in request.path for path in ["/static/", "/media/"]):
            return response

        # Get user
        user = request.user if request.user.is_authenticated else None

        # Update user's last activity
        if user:
            User.objects.filter(pk=user.pk).update(last_activity=timezone.now())

        # Determine action type
        action = (
            AuditLog.ACTION_API
            if request.path.startswith("/api/")
            else AuditLog.ACTION_VIEW
        )
        if request.path.startswith("/auth/"):
            if request.path.endswith("/login/"):
                action = AuditLog.ACTION_LOGIN
            elif request.path.endswith("/logout/"):
                action = AuditLog.ACTION_LOGOUT

        # Create audit log entry
        AuditLog.objects.create(
            user=user,
            action=action,
            description=f"{request.method} {request.path}",
            ip_address=self.get_client_ip(request),
            metadata={
                "method": request.method,
                "path": request.path,
                "status_code": response.status_code,
                "user_agent": request.META.get("HTTP_USER_AGENT", ""),
            },
        )

        return response

    def get_client_ip(self, request):
        """
        Get the client's IP address from the request.
        Handles cases where the request might be coming through a proxy.
        """
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0].strip()
        return request.META.get("REMOTE_ADDR")
