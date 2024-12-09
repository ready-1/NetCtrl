from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib import messages
from django.urls import reverse
from .models import CustomUser

@receiver(user_logged_in)
def admin_login_notification(sender, request, user, **kwargs):
    # Check if the user is an admin and should be notified
    if user.is_staff and user.notify_on_approval:
        pending_users = CustomUser.objects.filter(is_active=False)
        if pending_users.exists():
            user_list = ', '.join([pending_user.username for pending_user in pending_users])
            link = reverse('admin:accounts_customuser_changelist')
            messages.info(
                request,
                f"The following users are pending approval: {', '.join([u.display_name for u in pending_users])}. "
                f"<a href='{link}'>Review now</a>",
                extra_tags='safe',
            )