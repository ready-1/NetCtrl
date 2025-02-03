"""Test views for NetCtrl components."""

import pytest
from django.test import TestCase, Client
from django.urls import reverse
from core.models import User
from .views import TestView, TestFormView, TestAllView


@pytest.fixture
def client():
    """Create a test client."""
    return Client()


@pytest.mark.django_db
class TestComponentViews:
    """Test component views."""

    def test_dark_theme_components(self, client):
        """Test dark theme components view."""
        url = reverse("tests:test-dark-theme")
        response = client.get(url)
        assert response.status_code == 200
        assert "dark_theme" in response.context
        assert response.context["dark_theme"] is True

    def test_alert_component(self, client):
        """Test alert component view."""
        url = reverse("tests:test-alert")
        response = client.get(url)
        assert response.status_code == 200
        assert "alert_type" in response.context
        assert "message" in response.context

        # Test with custom alert type
        response = client.get(f"{url}?type=error")
        assert response.status_code == 200
        assert response.context["alert_type"] == "error"

    def test_loading_component(self, client):
        """Test loading component view."""
        url = reverse("tests:test-loading")
        response = client.get(url)
        assert response.status_code == 200

    def test_mobile_responsive(self, client):
        """Test mobile responsive view."""
        url = reverse("tests:test-mobile")
        response = client.get(url)
        assert response.status_code == 200

    def test_button_component(self, client):
        """Test button component view."""
        url = reverse("tests:test-button")
        response = client.get(url)
        assert response.status_code == 200

    def test_card_component(self, client):
        """Test card component view."""
        url = reverse("tests:test-card")
        response = client.get(url)
        assert response.status_code == 200

    def test_form_component(self, client):
        """Test form component view."""
        url = reverse("tests:test-form")
        response = client.get(url)
        assert response.status_code == 200

    def test_all_components(self, client):
        """Test all components view."""
        url = reverse("tests:test-all")
        response = client.get(url)
        assert response.status_code == 200
        assert "dark_theme" in response.context
        assert "alert_type" in response.context
        assert "message" in response.context
