"""WebSocket consumers for switch status updates."""

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.utils import timezone
from .models import Switch
from core.models import Notification
from core.utils.notifications import notify_switch_status_change


class SwitchStatusConsumer(AsyncWebsocketConsumer):
    """Consumer for handling switch status updates."""

    async def connect(self):
        """Handle WebSocket connection."""
        # Add to switch status group
        await self.channel_layer.group_add("switch_status", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        """Handle WebSocket disconnection."""
        # Remove from switch status group
        await self.channel_layer.group_discard("switch_status", self.channel_name)

    async def receive(self, text_data):
        """Handle incoming WebSocket messages."""
        try:
            data = json.loads(text_data)
            message_type = data.get("type")
            payload = data.get("payload", {})

            if message_type == "switch_status":
                await self.handle_switch_status(payload)
            elif message_type == "port_status":
                await self.handle_port_status(payload)

        except json.JSONDecodeError:
            await self.send(
                text_data=json.dumps(
                    {"type": "error", "message": "Invalid JSON format"}
                )
            )
        except Exception as e:
            await self.send(text_data=json.dumps({"type": "error", "message": str(e)}))

    async def handle_switch_status(self, payload):
        """Handle switch status updates."""
        switch_id = payload.get("id")
        new_status = payload.get("status")

        if not all([switch_id, new_status]):
            return

        # Update switch status in database
        switch, old_status = await self.update_switch_status(switch_id, new_status)

        if switch and old_status != new_status:
            # Create notification for status change
            await database_sync_to_async(notify_switch_status_change)(
                switch=switch, old_status=old_status, new_status=new_status
            )

            # Broadcast status change to all connected clients
            await self.channel_layer.group_send(
                "switch_status",
                {
                    "type": "switch_update",
                    "payload": {
                        "id": switch_id,
                        "status": new_status,
                        "lastSeen": timezone.now().isoformat(),
                    },
                },
            )

    async def handle_port_status(self, payload):
        """Handle port status updates."""
        switch_id = payload.get("switch_id")
        port_id = payload.get("port_id")
        status = payload.get("status")

        if not all([switch_id, port_id, status]):
            return

        # Broadcast port status to all connected clients
        await self.channel_layer.group_send(
            "switch_status", {"type": "port_update", "payload": payload}
        )

    @database_sync_to_async
    def update_switch_status(self, switch_id, new_status):
        """Update switch status in database."""
        try:
            switch = Switch.objects.get(id=switch_id)
            old_status = switch.status
            switch.status = new_status
            switch.last_seen = timezone.now()
            switch.save(update_fields=["status", "last_seen"])
            return switch, old_status
        except Switch.DoesNotExist:
            return None, None

    async def switch_update(self, event):
        """Handle switch update messages."""
        await self.send(
            text_data=json.dumps({"type": "switch_update", "payload": event["payload"]})
        )

    async def port_update(self, event):
        """Handle port update messages."""
        await self.send(
            text_data=json.dumps({"type": "port_update", "payload": event["payload"]})
        )
