"""Utility functions for the core app."""

import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.core.serializers.json import DjangoJSONEncoder


def send_notification(user_id, message, notification_type="info", data=None):
    """Send a real-time notification to a specific user.

    Args:
        user_id (int): ID of the user to send the notification to
        message (str): Notification message
        notification_type (str): Type of notification (info, success, warning, error)
        data (dict, optional): Additional data to send with the notification
    """
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"user_{user_id}",
        {
            "type": "notify",
            "message": message,
            "notification_type": notification_type,
            "data": json.loads(json.dumps(data or {}, cls=DjangoJSONEncoder)),
        },
    )


def broadcast_notification(message, notification_type="info", data=None):
    """Send a real-time notification to all connected users.

    Args:
        message (str): Notification message
        notification_type (str): Type of notification (info, success, warning, error)
        data (dict, optional): Additional data to send with the notification
    """
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notifications",
        {
            "type": "notify",
            "message": message,
            "notification_type": notification_type,
            "data": json.loads(json.dumps(data or {}, cls=DjangoJSONEncoder)),
        },
    )
