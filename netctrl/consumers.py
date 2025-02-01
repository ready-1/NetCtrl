"""WebSocket consumers."""

from channels.generic.websocket import AsyncJsonWebsocketConsumer
import asyncio
import random
from django.utils import timezone


class DashboardConsumer(AsyncJsonWebsocketConsumer):
    """Consumer for dashboard updates."""

    async def connect(self):
        """Handle WebSocket connection."""
        await self.accept()
        self.update_task = asyncio.create_task(self.send_updates())

    async def disconnect(self, close_code):
        """Handle WebSocket disconnection."""
        self.update_task.cancel()

    async def send_updates(self):
        """Send periodic updates."""
        while True:
            await asyncio.sleep(5)  # Update every 5 seconds
            await self.send_json(
                {
                    "type": "stats_update",
                    "total_switches": random.randint(10, 20),
                    "active_switches": random.randint(5, 15),
                    "total_ports": random.randint(100, 500),
                }
            )
            await self.send_json(
                {
                    "type": "traffic_update",
                    "timestamp": timezone.now().strftime("%H:%M:%S"),
                    "inbound": random.randint(100, 1000),
                    "outbound": random.randint(100, 1000),
                }
            )


class SwitchStatsConsumer(AsyncJsonWebsocketConsumer):
    """Consumer for switch statistics updates."""

    async def connect(self):
        """Handle WebSocket connection."""
        self.switch_id = self.scope["url_route"]["kwargs"]["switch_id"]
        await self.accept()
        self.update_task = asyncio.create_task(self.send_updates())

    async def disconnect(self, close_code):
        """Handle WebSocket disconnection."""
        self.update_task.cancel()

    async def send_updates(self):
        """Send periodic updates."""
        while True:
            await asyncio.sleep(5)  # Update every 5 seconds
            await self.send_json(
                {
                    "type": "port_stats",
                    "connections": [random.randint(0, 10) for _ in range(48)],
                }
            )
            await self.send_json(
                {
                    "type": "traffic",
                    "timestamp": timezone.now().strftime("%H:%M:%S"),
                    "inbound": random.randint(100, 1000),
                    "outbound": random.randint(100, 1000),
                }
            )
