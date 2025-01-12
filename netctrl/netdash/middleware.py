"""
Custom middleware for user approval checks.
"""
from django.shortcuts import redirect
from django.urls import resolve, reverse
from django.conf import settings


class UserApprovalMiddleware:
    """Middleware to check if user is approved."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            return self.get_response(request)

        current_url = resolve(request.path_info).url_name
        exempt_urls = getattr(settings, 'APPROVAL_EXEMPT_URLS', [])

        # Allow access to exempt URLs and admin users
        if current_url in exempt_urls or request.user.is_staff:
            return self.get_response(request)

        # If user is not approved and trying to access a protected URL,
        # redirect to a pending approval page
        if not request.user.is_approved:
            if current_url != 'pending_approval':
                return redirect('netdash:pending_approval')

        return self.get_response(request)
