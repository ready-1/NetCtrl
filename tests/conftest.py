"""Test fixtures for the NetCtrl application."""

import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from .factories import UserFactory, SwitchFactory, PortFactory


@pytest.fixture
def api_client():
    """Return an API client."""
    return APIClient()


@pytest.fixture
def user():
    """Create a test user."""
    return UserFactory(username="testuser", password="testpass123")


@pytest.fixture
def authenticated_client(api_client, user):
    """Return an authenticated API client."""
    refresh = RefreshToken.for_user(user)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    return api_client


@pytest.fixture
def switch_data():
    """Return test data for a switch."""
    return {
        "name": "Test Switch",
        "ip_address": "192.168.1.1",
        "username": "admin",
        "password": "admin123",
        "description": "Test switch for API tests",
    }


@pytest.fixture
def port_data():
    """Return test data for a port."""
    return {
        "name": "1/0/1",
        "description": "Test port",
        "admin_status": "up",
        "vlan": 1,
        "speed": "1G",
        "duplex": "full",
    }
