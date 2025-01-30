"""Tests for authentication functionality."""

import pytest
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db


def test_user_can_login(api_client, user):
    """Test that a user can login with valid credentials."""
    url = reverse("api:token_obtain_pair")
    response = api_client.post(url, {"username": "testuser", "password": "testpass123"})
    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data
    assert "refresh" in response.data


def test_user_cannot_login_with_wrong_password(api_client, user):
    """Test that a user cannot login with invalid credentials."""
    url = reverse("api:token_obtain_pair")
    response = api_client.post(url, {"username": "testuser", "password": "wrongpass"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_user_can_refresh_token(api_client, user):
    """Test that a user can refresh their token."""
    # First get tokens
    url = reverse("api:token_obtain_pair")
    response = api_client.post(url, {"username": "testuser", "password": "testpass123"})
    refresh_token = response.data["refresh"]

    # Then try to refresh
    url = reverse("api:token_refresh")
    response = api_client.post(url, {"refresh": refresh_token})
    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data


@pytest.mark.api
def test_protected_view_with_token(authenticated_client):
    """Test that a protected view can be accessed with valid token."""
    url = reverse("api:user-detail")
    response = authenticated_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.api
def test_protected_view_without_token(api_client):
    """Test that a protected view cannot be accessed without token."""
    url = reverse("api:user-detail")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
