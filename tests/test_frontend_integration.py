"""Integration tests for frontend components."""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from channels.testing import WebsocketCommunicator
from channels.routing import URLRouter
from channels.auth import AuthMiddlewareStack
import json

from netctrl.routing import websocket_urlpatterns
from netctrl.models import Switch


class FrontendIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpass123"
        )
        self.client.login(username="testuser", password="testpass123")

    async def test_websocket_switch_updates(self):
        """Test that WebSocket updates are reflected in the UI."""
        application = AuthMiddlewareStack(URLRouter(websocket_urlpatterns))

        # Create a test switch
        switch = Switch.objects.create(name="Test Switch", ip_address="192.168.1.1")

        # Connect to WebSocket
        communicator = WebsocketCommunicator(
            application=application, path=f"/ws/switch/{switch.id}/stats/"
        )
        connected, _ = communicator.connect()
        self.assertTrue(connected)

        # Check that we receive updates
        response = await communicator.receive_json_from()
        self.assertIn("type", response)
        self.assertEqual(response["type"], "port_stats")
        self.assertIn("connections", response)

        # Close
        await communicator.disconnect()

    def test_form_submission_with_validation(self):
        """Test form submission with client and server validation."""
        # Test empty form submission
        response = self.client.post(
            reverse("netctrl:switch-add"), data={}, HTTP_HX_REQUEST="true"
        )
        self.assertEqual(response.status_code, 400)
        self.assertContains(response, "This field is required", status_code=400)

        # Test valid form submission
        response = self.client.post(
            reverse("netctrl:switch-add"),
            data={"name": "Test Switch", "ip_address": "192.168.1.1"},
            HTTP_HX_REQUEST="true",
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "success")

    def test_loading_indicators(self):
        """Test that loading indicators show during HTMX requests."""
        response = self.client.get(
            reverse("netctrl:switch-list"), HTTP_HX_REQUEST="true"
        )
        self.assertContains(response, "loading-spinner")
        self.assertContains(response, "nc-loading")

    def test_alert_component(self):
        """Test alert component functionality."""
        # Test success alert
        response = self.client.post(
            reverse("netctrl:switch-add"),
            data={
                "name": "test-switch",
                "ip_address": "192.168.1.1",
                "username": "admin",
                "password": "secret123",
            },
            HTTP_HX_REQUEST="true",
        )
        self.assertContains(response, "alert-success")
        self.assertContains(response, 'data-bs-dismiss="alert"')

        # Test error alert
        response = self.client.post(
            reverse("netctrl:switch-add"), data={"name": ""}, HTTP_HX_REQUEST="true"
        )
        self.assertContains(response, "alert-danger", status_code=400)

    def test_network_failure(self):
        """Test handling of network failures."""
        # Test with a large request that should be rejected
        large_data = {
            "name": "x" * (2 * 1024 * 1024),  # 2MB of data
            "ip_address": "192.168.1.1",
        }
        response = self.client.post(
            reverse("netctrl:switch-add"), data=large_data, HTTP_HX_REQUEST="true"
        )
        self.assertEqual(response.status_code, 400)
        self.assertContains(response, "Request too large", status_code=400)

    def test_chart_updates(self):
        """Test that charts update with new data."""
        switch = Switch.objects.create(name="Test Switch", ip_address="192.168.1.1")

        response = self.client.get(
            reverse("netctrl:switch-stats", kwargs={"switch_id": switch.id}),
            HTTP_HX_REQUEST="true",
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "chart.js")
        self.assertContains(response, "data-chart")

    def test_mobile_responsive_layout(self):
        """Test that the layout is responsive on mobile devices."""
        response = self.client.get(
            reverse("netctrl:dashboard"),
            HTTP_USER_AGENT="Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "viewport")
        self.assertContains(response, "width=device-width")
