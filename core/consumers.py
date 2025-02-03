"""WebSocket consumers for the core app."""

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from django.core.serializers.json import DjangoJSONEncoder


class BaseConsumer(AsyncJsonWebsocketConsumer):
    """Base WebSocket consumer with common functionality."""

    async def connect(self):
        """Handle WebSocket connection."""
        if self.scope["user"].is_anonymous:
            await self.close()
            return

        await self.channel_layer.group_add(
            f"user_{self.scope['user'].id}", self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        """Handle WebSocket disconnection."""
        if not self.scope["user"].is_anonymous:
            await self.channel_layer.group_discard(
                f"user_{self.scope['user'].id}", self.channel_name
            )

    async def send_json(self, content, close=False):
        """Send JSON message with Django JSON encoder."""
        await super().send_json(content, close=close, encoder=DjangoJSONEncoder)

    async def notify(self, event):
        """Send notification to client."""
        await self.send_json(
            {
                "type": event["type"],
                "message": event["message"],
                "data": event.get("data", {}),
            }
        )


class NotificationConsumer(BaseConsumer):
    """Consumer for handling real-time notifications."""

    async def connect(self):
        """Handle WebSocket connection."""
        await super().connect()
        if not self.scope["user"].is_anonymous:
            await self.channel_layer.group_add("notifications", self.channel_name)

    async def disconnect(self, close_code):
        """Handle WebSocket disconnection."""
        if not self.scope["user"].is_anonymous:
            await self.channel_layer.group_discard("notifications", self.channel_name)
        await super().disconnect(close_code)
