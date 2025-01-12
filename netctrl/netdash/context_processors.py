"""
Context processors for netdash app.
"""
from django.contrib.auth import get_user_model

User = get_user_model()

def pending_approvals(request):
    """Add pending approvals count to context for admin users."""
    if request.user.is_authenticated and request.user.is_staff:
        pending_count = User.objects.filter(is_approved=False).count()
        return {'pending_approvals_count': pending_count}
    return {'pending_approvals_count': 0}
