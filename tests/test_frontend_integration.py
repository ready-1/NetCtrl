"""Integration tests for frontend components."""

from django.test import TestCase, Client, override_settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from channels.testing import WebsocketCommunicator
from channels.auth import AuthMiddlewareStack
from asgiref.sync import sync_to_async
import json

from netctrl.routing import websocket_urlpatterns
from netctrl.models import Switch
from config.asgi import application


class FrontendIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpass123"
        )
        self.client.login(username="testuser", password="testpass123")

    async def test_websocket_switch_updates(self):
        """Test that WebSocket updates are reflected in the UI."""
        communicator = WebsocketCommunicator(application, "/ws/switches/")
        connected, _ = await communicator.connect()
        self.assertTrue(connected)

        # Send a switch update
        await communicator.send_json_to(
            {"type": "switch.update", "switch_id": 1, "status": "active"}
        )

        # Verify the response
        response = await communicator.receive_json_from()
        self.assertEqual(response["type"], "switch.update")
        self.assertEqual(response["switch_id"], 1)
        self.assertEqual(response["status"], "active")

        await communicator.disconnect()

    def test_form_submission_with_validation(self):
        """Test form submission with validation."""
        # Test empty form submission
        response = self.client.post(reverse("tests:test-form"), {})
        self.assertEqual(response.status_code, 400)

        # Test valid form submission
        response = self.client.post(reverse("tests:test-form"), {"name": "Test User"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "success")

    def test_loading_indicators(self):
        """Test that loading indicators show during HTMX requests."""
        response = self.client.get(reverse("tests:test-loading"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "loading-indicator")

    def test_network_failure_handling(self):
        """Test network failure handling."""
        url = "/tests/network-failure/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "network-error")

    def test_alert_component(self):
        """Test alert component functionality."""
        # Test success alert
        response = self.client.get(reverse("tests:test-alert-success"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "alert-success")

        # Test error alert
        response = self.client.get(reverse("tests:test-alert-error"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "alert-danger")

    def test_network_failure(self):
        """Test handling of network failures."""
        url = "/tests/network-failure/"
        response = self.client.post(url, {"name": "x" * 2000})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content.decode(), "Request too large")

    def test_chart_updates(self):
        """Test that charts update with new data."""
        response = self.client.get(
            reverse("tests:test-chart"),
            HTTP_HX_REQUEST="true",
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "chart.js")
        self.assertContains(response, "data-chart")

    def test_mobile_responsive_layout(self):
        """Test that the layout is responsive on mobile devices."""
        response = self.client.get(
            reverse("tests:test-components"),
            HTTP_USER_AGENT="Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "viewport")
        self.assertContains(response, "width=device-width")

    def test_form_validation(self):
        """Test form validation."""
        url = "/tests/form/"
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content.decode(), "Name is required")
