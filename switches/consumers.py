"""WebSocket consumers for the switches app."""

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Switch


class SwitchStatusConsumer(AsyncWebsocketConsumer):
    """Consumer for switch status updates."""

    async def connect(self):
        """Handle WebSocket connection."""
        # Add to the switch_status group
        await self.channel_layer.group_add("switch_status", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        """Handle WebSocket disconnection."""
        # Remove from the switch_status group
        await self.channel_layer.group_discard("switch_status", self.channel_name)

    async def receive(self, text_data):
        """Handle incoming WebSocket data."""
        # Currently we don't expect to receive any data
        pass

    async def switch_status_update(self, event):
        """Handle switch status updates."""
        # Send status update to WebSocket
        await self.send(
            text_data=json.dumps(
                {
                    "type": "switch.status_update",
                    "switch_id": event["switch_id"],
                    "data": event["data"],
                }
            )
        )

    @database_sync_to_async
    def get_switch_status(self, switch_id):
        """Get current status for a switch."""
        try:
            switch = Switch.objects.get(pk=switch_id)
            return {
                "overall_status": switch.status,
                "in_band": {
                    "status": switch.in_band_status,
                    "last_seen": (
                        switch.in_band_last_seen.isoformat()
                        if switch.in_band_last_seen
                        else None
                    ),
                },
                "out_band": {
                    "status": switch.out_band_status,
                    "last_seen": (
                        switch.out_band_last_seen.isoformat()
                        if switch.out_band_last_seen
                        else None
                    ),
                },
            }
        except Switch.DoesNotExist:
            return None
