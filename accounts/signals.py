from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import CustomUser
from django.conf import settings

@receiver(post_save, sender=CustomUser)
def notify_approvers(sender, instance, created, **kwargs):
    if created and not instance.is_active:
        approvers = CustomUser.objects.filter(notify_on_approval=True)
        for approver in approvers:
            # Send email notification
            send_mail(
                subject="New User Pending Approval",
                message=f"A new user '{instance.username}' is awaiting approval.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[approver.email],
                fail_silently=False,
            )