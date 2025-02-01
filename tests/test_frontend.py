"""Tests for frontend infrastructure."""

from django.test import TestCase, Client
from django.urls import reverse
from django.middleware.csrf import get_token


class FrontendInfrastructureTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_htmx_csrf_token(self):
        """Test that HTMX requests include CSRF token."""
        response = self.client.get(reverse("netctrl:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "csrf-token")
        self.assertContains(response, "htmx.org")

    def test_dark_theme_css_variables(self):
        """Test that dark theme CSS variables are properly defined."""
        response = self.client.get("/static/css/base/variables.css")
        content = b"".join(response.streaming_content).decode()

        # Check for essential CSS variables
        required_variables = [
            "--nc-bg-primary",
            "--nc-bg-secondary",
            "--nc-text-primary",
            "--nc-text-secondary",
            "--nc-border-color",
            "--nc-primary",
            "--nc-success",
            "--nc-warning",
            "--nc-danger",
        ]

        for variable in required_variables:
            self.assertIn(variable, content, f"Missing CSS variable: {variable}")

    def test_utility_classes(self):
        """Test that utility classes are properly defined."""
        response = self.client.get("/static/css/base/utilities.css")
        content = b"".join(response.streaming_content).decode()

        # Check for essential utility classes
        required_classes = [
            ".nc-m-0",
            ".nc-p-0",
            ".nc-text-primary",
            ".nc-bg-primary",
            ".nc-border",
            ".nc-d-flex",
        ]

        for class_name in required_classes:
            self.assertIn(class_name, content, f"Missing utility class: {class_name}")

    def test_component_styles(self):
        """Test that component styles are properly defined."""
        # Test button styles
        response = self.client.get("/static/css/components/buttons.css")
        content = b"".join(response.streaming_content).decode()
        required_button_classes = [
            ".nc-btn",
            ".nc-btn-primary",
            ".nc-btn-success",
            ".nc-btn-warning",
            ".nc-btn-danger",
        ]
        for class_name in required_button_classes:
            self.assertIn(class_name, content, f"Missing button class: {class_name}")

        # Test card styles
        response = self.client.get("/static/css/components/cards.css")
        content = b"".join(response.streaming_content).decode()
        required_card_classes = [
            ".nc-card",
            ".nc-card-body",
            ".nc-card-header",
            ".nc-card-footer",
            ".nc-card-title",
        ]
        for class_name in required_card_classes:
            self.assertIn(class_name, content, f"Missing card class: {class_name}")

    def test_javascript_utilities(self):
        """Test that JavaScript utilities are properly defined."""
        # Test Chart.js utilities
        response = self.client.get("/static/js/utils/charts.js")
        content = b"".join(response.streaming_content).decode()
        required_chart_functions = [
            "createTimeSeriesChart",
            "createBarChart",
            "updateChartData",
            "defaultChartConfig",
        ]
        for function_name in required_chart_functions:
            self.assertIn(
                function_name, content, f"Missing chart function: {function_name}"
            )

        # Test WebSocket utilities
        response = self.client.get("/static/js/utils/websocket.js")
        content = b"".join(response.streaming_content).decode()
        required_websocket_methods = [
            "connect",
            "handleReconnect",
            "handleMessage",
            "addEventListener",
            "removeEventListener",
            "send",
            "disconnect",
        ]
        for method_name in required_websocket_methods:
            self.assertIn(
                method_name, content, f"Missing WebSocket method: {method_name}"
            )

        # Test HTMX configuration
        response = self.client.get("/static/js/utils/htmx-config.js")
        content = b"".join(response.streaming_content).decode()
        required_htmx_events = [
            "htmx:configRequest",
            "htmx:responseError",
        ]
        for event_name in required_htmx_events:
            self.assertIn(event_name, content, f"Missing HTMX event: {event_name}")

    def test_htmx_events(self):
        """Test HTMX event handling."""
        response = self.client.get("/static/js/utils/htmx-config.js")
        content = b"".join(response.streaming_content).decode()

        # Check for HTMX event handlers
        required_event_handlers = [
            "htmx:beforeRequest",  # For loading indicators
            "htmx:afterRequest",  # For loading indicators
            "htmx:responseError",  # For error handling
            "htmx:sendError",  # For network error handling
            "htmx:timeout",  # For timeout handling
        ]
        for handler in required_event_handlers:
            self.assertIn(handler, content, f"Missing HTMX event handler: {handler}")

    def test_responsive_design(self):
        """Test responsive design breakpoints."""
        response = self.client.get("/static/css/base/utilities.css")
        content = b"".join(response.streaming_content).decode()

        # Check for responsive breakpoints
        required_breakpoints = [
            "@media (min-width: 576px)",  # Small devices
            "@media (min-width: 768px)",  # Medium devices
            "@media (min-width: 992px)",  # Large devices
            "@media (min-width: 1200px)",  # Extra large devices
        ]
        for breakpoint in required_breakpoints:
            self.assertIn(
                breakpoint, content, f"Missing responsive breakpoint: {breakpoint}"
            )

    def test_dark_theme_toggle(self):
        """Test dark theme toggle functionality."""
        response = self.client.get("/static/js/utils/theme.js")
        content = b"".join(response.streaming_content).decode()

        # Check for theme toggle functions
        required_functions = [
            "toggleDarkTheme",
            "setThemePreference",
            "getThemePreference",
            "applyTheme",
        ]
        for function in required_functions:
            self.assertIn(function, content, f"Missing theme function: {function}")

    def test_websocket_events(self):
        """Test WebSocket event handling."""
        response = self.client.get("/static/js/utils/websocket.js")
        content = b"".join(response.streaming_content).decode()

        # Check for WebSocket event handling
        required_event_handlers = [
            "onopen",
            "onclose",
            "onerror",
            "onmessage",
            "handleSwitchUpdate",
            "handlePortUpdate",
            "handleConfigUpdate",
        ]
        for handler in required_event_handlers:
            self.assertIn(
                handler, content, f"Missing WebSocket event handler: {handler}"
            )

    def test_chart_rendering(self):
        """Test Chart.js rendering configuration."""
        response = self.client.get("/static/js/utils/charts.js")
        content = b"".join(response.streaming_content).decode()

        # Check for chart configuration
        required_chart_config = [
            "darkMode: true",  # Dark theme support
            "responsive: true",  # Responsive charts
            "maintainAspectRatio",  # Aspect ratio handling
            "interaction: {",  # Interaction settings
            "animation: {",  # Animation settings
            "plugins: {",  # Plugin configuration
            "scales: {",  # Axis configuration
        ]
        for config in required_chart_config:
            self.assertIn(config, content, f"Missing chart configuration: {config}")
