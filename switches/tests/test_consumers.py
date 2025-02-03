"""Test cases for WebSocket consumers."""

import json
import pytest
from channels.testing import WebsocketCommunicator
from channels.routing import URLRouter
from django.urls import re_path
from switches.consumers import SwitchStatusConsumer
from switches.models import Switch
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def user(db):
    """Create a test superuser."""
    return User.objects.create_superuser(
        username="testuser",
        email="test@example.com",
        password="password123",
        role=User.ROLE_SUPERUSER,
    )


@pytest.fixture
def switch(db):
    """Create a test switch."""
    return Switch.objects.create(
        name="Test Switch",
        ip_address="192.168.1.1",
        username="admin",
        password="password123",
    )


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
class TestSwitchStatusConsumer:
    """Test cases for the SwitchStatusConsumer."""

    async def test_connect(self):
        """Test WebSocket connection."""
        application = URLRouter(
            [
                re_path(r"ws/switches/status/$", SwitchStatusConsumer.as_asgi()),
            ]
        )
        communicator = WebsocketCommunicator(application, "/ws/switches/status/")
        connected, _ = await communicator.connect()
        assert connected
        await communicator.disconnect()

    async def test_switch_status_update(self, switch):
        """Test switch status update message handling."""
        application = URLRouter(
            [
                re_path(r"ws/switches/status/$", SwitchStatusConsumer.as_asgi()),
            ]
        )
        communicator = WebsocketCommunicator(application, "/ws/switches/status/")
        await communicator.connect()

        # Send status update
        await communicator.send_json_to(
            {"type": "switch_status", "payload": {"id": switch.id, "status": "down"}}
        )

        # Receive response
        response = await communicator.receive_json_from()
        assert response["type"] == "switch_update"
        assert response["payload"]["id"] == switch.id
        assert response["payload"]["status"] == "down"

        # Check database update
        switch.refresh_from_db()
        assert switch.status == "down"
        assert switch.last_seen is not None

        await communicator.disconnect()

    async def test_invalid_message(self):
        """Test handling of invalid messages."""
        application = URLRouter(
            [
                re_path(r"ws/switches/status/$", SwitchStatusConsumer.as_asgi()),
            ]
        )
        communicator = WebsocketCommunicator(application, "/ws/switches/status/")
        await communicator.connect()

        # Send invalid JSON
        await communicator.send_to("invalid json")

        # Should receive error response
        response = await communicator.receive_json_from()
        assert response["type"] == "error"
        assert "Invalid JSON format" in response["message"]

        await communicator.disconnect()

    async def test_missing_fields(self, switch):
        """Test handling of messages with missing required fields."""
        application = URLRouter(
            [
                re_path(r"ws/switches/status/$", SwitchStatusConsumer.as_asgi()),
            ]
        )
        communicator = WebsocketCommunicator(application, "/ws/switches/status/")
        await communicator.connect()

        # Send message without status
        await communicator.send_json_to(
            {"type": "switch_status", "payload": {"id": switch.id}}
        )

        # No update should be broadcast
        assert await communicator.receive_nothing()

        await communicator.disconnect()

    async def test_nonexistent_switch(self):
        """Test handling of updates for non-existent switches."""
        application = URLRouter(
            [
                re_path(r"ws/switches/status/$", SwitchStatusConsumer.as_asgi()),
            ]
        )
        communicator = WebsocketCommunicator(application, "/ws/switches/status/")
        await communicator.connect()

        # Send status update for non-existent switch
        await communicator.send_json_to(
            {"type": "switch_status", "payload": {"id": 9999, "status": "down"}}
        )

        # No update should be broadcast
        assert await communicator.receive_nothing()

        await communicator.disconnect()
