from functools import wraps
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from .models import AuditLog


def audit_log(action=None, description=None):
    """
    Decorator to log changes to model instances.
    Can be used on views or model methods.

    Usage:
        @audit_log(action='update', description='Updated switch configuration')
        def update_config(self, request, *args, **kwargs):
            ...

    Args:
        action: The type of action being performed (create, update, delete, etc.)
        description: Description of the action (can be a string or a callable)
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Get request object (could be first or second argument)
            request = args[0] if hasattr(args[0], "user") else args[1]
            instance = None
            old_data = None

            # If this is a model method, get the instance
            if len(args) > 0 and hasattr(args[0], "_meta"):
                instance = args[0]
                if action in [AuditLog.ACTION_UPDATE, AuditLog.ACTION_DELETE]:
                    old_data = {
                        field.name: getattr(instance, field.name)
                        for field in instance._meta.fields
                        if not field.is_relation
                    }

            # Execute the wrapped function
            with transaction.atomic():
                result = func(*args, **kwargs)

                # Get the action type
                action_type = action or AuditLog.ACTION_OTHER

                # Get the description
                if callable(description):
                    desc = description(result)
                else:
                    desc = description or f"{action_type.title()} operation"

                # If we have an instance, get its updated data
                new_data = None
                if instance and action in [
                    AuditLog.ACTION_UPDATE,
                    AuditLog.ACTION_CREATE,
                ]:
                    instance.refresh_from_db()
                    new_data = {
                        field.name: getattr(instance, field.name)
                        for field in instance._meta.fields
                        if not field.is_relation
                    }

                # Create the audit log entry
                log_entry = AuditLog.objects.create(
                    user=request.user if request.user.is_authenticated else None,
                    action=action_type,
                    description=desc,
                    ip_address=request.META.get("REMOTE_ADDR"),
                    content_type=(
                        ContentType.objects.get_for_model(instance)
                        if instance
                        else None
                    ),
                    object_id=str(instance.pk) if instance else None,
                )

                # Set changes if we have both old and new data
                if old_data or new_data:
                    log_entry.set_changes(old_data, new_data)
                    log_entry.save()

            return result

        return wrapper

    return decorator
