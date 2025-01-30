"""Global pytest fixtures and configuration."""

import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

@pytest.fixture
def api_client():
    """Return an authenticated API client."""
    return APIClient()

@pytest.fixture
def authenticated_client(api_client, user):
    """Return an authenticated API client."""
    api_client.force_authenticate(user=user)
    return api_client

@pytest.fixture
def user():
    """Create and return a regular user."""
    return User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123'
    )

@pytest.fixture
def admin_user():
    """Create and return an admin user."""
    return User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='adminpass123'
    )

@pytest.fixture
def switch_data():
    """Return test data for a switch."""
    return {
        'name': 'Test Switch',
        'ip_address': '192.168.1.1',
        'username': 'admin',
        'password': 'password123',
        'description': 'Test switch for unit tests'
    }

@pytest.fixture
def port_data():
    """Return test data for a port."""
    return {
        'name': '1/0/1',
        'description': 'Test Port',
        'admin_status': 'up',
        'vlan': 1,
        'speed': 'auto',
        'duplex': 'full'
    }
