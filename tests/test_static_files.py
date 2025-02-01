"""Tests for static file serving configuration."""

from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings
import os


class StaticFileServingTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_static_files_exist(self):
        """Test that critical static files exist in the staticfiles directory."""
        static_files = [
            "js/utils/htmx-config.js",
            "js/utils/charts.js",
            "js/utils/websocket.js",
            "css/base/variables.css",
            "css/base/utilities.css",
            "css/components/buttons.css",
            "css/components/cards.css",
            "vendor/bootstrap/bootstrap-5.3.2-dist/css/bootstrap.min.css",
            "vendor/fontawesome/fontawesome-free-6.0.0-web/css/all.min.css",
        ]

        for file_path in static_files:
            full_path = os.path.join(settings.STATIC_ROOT, file_path)
            self.assertTrue(
                os.path.exists(full_path), f"Static file {file_path} not found"
            )

    def test_base_template_loads(self):
        """Test that the base template loads with all required static files."""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

        # Check for static file references in template
        content = response.content.decode()
        expected_files = [
            "bootstrap.bundle.min.js",
            "htmx.org",
            "chart.js",
            "htmx-config.js",
            "charts.js",
            "websocket.js",
            "variables.css",
            "utilities.css",
            "buttons.css",
            "cards.css",
        ]

        for file in expected_files:
            self.assertIn(file, content, f"Missing {file} in base template")
