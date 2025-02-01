"""Tests for frontend components."""

from django.test import TestCase, Client
from django.urls import reverse


class ComponentTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_alert_rendering(self):
        """Test alert component rendering."""
        # Test success alert
        response = self.client.get(reverse("test-alert", kwargs={"type": "success"}))
        self.assertContains(response, "alert-success")
        self.assertContains(response, "check-circle-fill")
        self.assertContains(response, 'role="alert"')

        # Test error alert
        response = self.client.get(reverse("test-alert", kwargs={"type": "error"}))
        self.assertContains(response, "alert-danger")
        self.assertContains(response, "exclamation-triangle-fill")

        # Test warning alert
        response = self.client.get(reverse("test-alert", kwargs={"type": "warning"}))
        self.assertContains(response, "alert-warning")
        self.assertContains(response, "exclamation-triangle-fill")

        # Test info alert
        response = self.client.get(reverse("test-alert", kwargs={"type": "info"}))
        self.assertContains(response, "alert-info")
        self.assertContains(response, "info-circle-fill")

    def test_loading_indicator_rendering(self):
        """Test loading indicator component rendering."""
        response = self.client.get(reverse("test-loading"))
        self.assertContains(response, "loading-spinner")
        self.assertContains(response, 'role="status"')
        self.assertContains(response, "visually-hidden")

    def test_card_rendering(self):
        """Test card component rendering."""
        response = self.client.get(reverse("test-card"))
        self.assertContains(response, "nc-card")
        self.assertContains(response, "nc-card-header")
        self.assertContains(response, "nc-card-body")
        self.assertContains(response, "nc-card-footer")

    def test_button_states(self):
        """Test button component states."""
        response = self.client.get(reverse("test-buttons"))

        # Test regular buttons
        self.assertContains(response, "nc-btn-primary")
        self.assertContains(response, "nc-btn-secondary")
        self.assertContains(response, "nc-btn-success")
        self.assertContains(response, "nc-btn-danger")

        # Test disabled state
        self.assertContains(response, "disabled")
        self.assertContains(response, 'aria-disabled="true"')

        # Test loading state
        self.assertContains(response, "nc-btn-loading")
        self.assertContains(response, "loading-spinner")

    def test_form_validation(self):
        """Test form validation rendering."""
        response = self.client.get(reverse("test-form"))

        # Test required fields
        self.assertContains(response, "required")
        self.assertContains(response, 'aria-required="true"')

        # Test validation messages
        self.assertContains(response, "invalid-feedback")
        self.assertContains(response, "valid-feedback")

    def test_dark_theme_components(self):
        """Test components in dark theme."""
        response = self.client.get(reverse("test-components"), HTTP_COOKIE="theme=dark")

        # Test dark theme classes
        self.assertContains(response, "nc-dark-theme")

        # Test dark theme colors
        self.assertContains(response, "--nc-bg-primary")
        self.assertContains(response, "--nc-text-primary")

    def test_responsive_components(self):
        """Test component responsive behavior."""
        response = self.client.get(reverse("test-components"))

        # Test responsive classes
        self.assertContains(response, "nc-d-sm-none")
        self.assertContains(response, "nc-d-md-block")
        self.assertContains(response, "nc-d-lg-flex")

        # Test responsive margins/padding
        self.assertContains(response, "nc-m-sm-0")
        self.assertContains(response, "nc-p-md-0")
