"""Tests for frontend components."""

from django.test import TestCase, Client
from django.urls import reverse


class ComponentTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_alert_rendering(self):
        """Test alert component rendering."""
        response = self.client.get("/tests/alert/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "check-circle-fill")
        self.assertContains(response, "alert-success")
        self.assertContains(response, "nc-alert")

    def test_button_states(self):
        """Test button component states."""
        response = self.client.get("/tests/buttons/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "nc-btn")
        self.assertContains(response, "nc-btn-primary")
        self.assertContains(response, "nc-btn-secondary")
        self.assertContains(response, "nc-btn-success")
        self.assertContains(response, "nc-btn-danger")
        self.assertContains(response, "nc-btn-loading")

    def test_card_rendering(self):
        """Test card component rendering."""
        response = self.client.get("/tests/card/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "nc-card")
        self.assertContains(response, "nc-card-header")
        self.assertContains(response, "nc-card-body")
        self.assertContains(response, "nc-card-title")
        self.assertContains(response, "nc-card-text")

    def test_loading_indicator(self):
        """Test loading indicator rendering."""
        response = self.client.get("/tests/loading/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "loading-spinner")
        self.assertContains(response, "loading-indicator")
        self.assertContains(response, "nc-loading")

    def test_form_validation(self):
        """Test form validation rendering."""
        response = self.client.get("/tests/form/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "required")
        self.assertContains(response, "invalid-feedback")
        self.assertContains(response, "nc-btn-primary")

    def test_dark_theme_components(self):
        """Test components in dark theme."""
        response = self.client.get("/tests/components/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "nc-dark-theme")
        self.assertContains(response, "nc-card")
        self.assertContains(response, "nc-card-body")
        self.assertContains(response, "nc-btn-primary")

    def test_responsive_components(self):
        """Test component responsive behavior."""
        response = self.client.get("/tests/components/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "nc-d-sm-none")
        self.assertContains(response, "nc-d-md-block")
        self.assertContains(response, "nc-d-lg-flex")
