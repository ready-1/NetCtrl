"""Tests for Whitenoise configuration."""

from django.test import TestCase, Client
from django.conf import settings
import os


class WhitenoiseConfigTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_whitenoise_caching(self):
        """Test that Whitenoise sets appropriate cache headers."""
        # Get a CSS file
        css_file = "css/base/utilities.css"
        response = self.client.get(f"/static/{css_file}")

        # Check for cache headers
        self.assertIn("Cache-Control", response.headers)
        self.assertIn("max-age=31536000", response.headers["Cache-Control"])
        self.assertIn("public", response.headers["Cache-Control"])

    def test_whitenoise_static_root(self):
        """Test that Whitenoise uses the correct static root."""
        # Verify STATIC_ROOT is set
        self.assertTrue(hasattr(settings, "STATIC_ROOT"))
        self.assertTrue(os.path.exists(settings.STATIC_ROOT))

        # Verify staticfiles directory contains collected files
        css_dir = os.path.join(settings.STATIC_ROOT, "css")
        js_dir = os.path.join(settings.STATIC_ROOT, "js")
        vendor_dir = os.path.join(settings.STATIC_ROOT, "vendor")

        self.assertTrue(os.path.exists(css_dir))
        self.assertTrue(os.path.exists(js_dir))
        self.assertTrue(os.path.exists(vendor_dir))
