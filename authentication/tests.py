"""Test views for authentication."""

import pytest
from django.test import Client
from django.urls import reverse
from core.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def client():
    """Create a test client."""
    return Client()


@pytest.fixture
def api_client():
    """Create a test API client."""
    return APIClient()


@pytest.fixture
def user():
    """Create a test user."""
    user = User.objects.create_user(
        username="testuser",
        password="testpass123",
        email="test@example.com",
    )
    return user


@pytest.fixture
def privileged_user():
    """Create a test privileged user."""
    user = User.objects.create_user(
        username="privileged",
        password="testpass123",
        email="privileged@example.com",
        is_staff=True,
    )
    return user


@pytest.fixture
def superuser():
    """Create a test superuser."""
    user = User.objects.create_superuser(
        username="admin",
        password="testpass123",
        email="admin@example.com",
    )
    return user


@pytest.fixture
def refresh_token(user):
    """Create a refresh token for the test user."""
    refresh = RefreshToken.for_user(user)
    return str(refresh)


@pytest.mark.django_db
class TestAuthenticationViews:
    """Test authentication views."""

    def test_login_view_get(self, client):
        """Test GET request to login view."""
        url = reverse("authentication:login")
        response = client.get(url)
        assert response.status_code == 200
        assert "form" in response.context

    def test_login_view_post_success(self, client, user):
        """Test successful POST request to login view."""
        url = reverse("authentication:login")
        data = {
            "username": "testuser",
            "password": "testpass123",
        }
        response = client.post(url, data)
        assert response.status_code == 302
        assert response.url == reverse("core:dashboard")

    def test_login_view_post_failure(self, client):
        """Test failed POST request to login view."""
        url = reverse("authentication:login")
        data = {
            "username": "wronguser",
            "password": "wrongpass",
        }
        response = client.post(url, data)
        assert response.status_code == 200
        assert "form" in response.context
        assert response.context["form"].errors

    def test_login_view_authenticated_user(self, client, user):
        """Test GET request to login view when already authenticated."""
        client.force_login(user)
        url = reverse("authentication:login")
        response = client.get(url)
        assert response.status_code == 302
        assert response.url == reverse("core:dashboard")

    def test_logout_view(self, client, user):
        """Test logout view."""
        client.force_login(user)
        url = reverse("authentication:logout")
        response = client.get(url)
        assert response.status_code == 302
        assert response.url == reverse("authentication:login")

    def test_token_obtain_view_non_privileged(self, api_client, user):
        """Test token obtain view for non-privileged user."""
        url = reverse("authentication:token_obtain")
        data = {
            "username": "testuser",
            "password": "testpass123",
        }
        response = api_client.post(url, data)
        assert response.status_code == 200
        assert "access" in response.data
        assert "refresh" in response.data
        assert response.data["user_role"] == "non_privileged"

    def test_token_obtain_view_privileged(self, api_client, privileged_user):
        """Test token obtain view for privileged user."""
        url = reverse("authentication:token_obtain")
        data = {
            "username": "privileged",
            "password": "testpass123",
        }
        response = api_client.post(url, data)
        assert response.status_code == 200
        assert "access" in response.data
        assert "refresh" in response.data
        assert response.data["user_role"] == "privileged"

    def test_token_obtain_view_superuser(self, api_client, superuser):
        """Test token obtain view for superuser."""
        url = reverse("authentication:token_obtain")
        data = {
            "username": "admin",
            "password": "testpass123",
        }
        response = api_client.post(url, data)
        assert response.status_code == 200
        assert "access" in response.data
        assert "refresh" in response.data
        assert response.data["user_role"] == "superuser"

    def test_token_obtain_view_invalid_credentials(self, api_client):
        """Test token obtain view with invalid credentials."""
        url = reverse("authentication:token_obtain")
        data = {
            "username": "wronguser",
            "password": "wrongpass",
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_token_revoke_view_success(self, api_client, user, refresh_token):
        """Test successful token revocation."""
        api_client.force_authenticate(user=user)
        url = reverse("authentication:token_revoke")
        data = {
            "refresh": refresh_token,
        }
        response = api_client.post(url, data)
        assert response.status_code == 200
        assert response.data["detail"] == "Token has been revoked"

    def test_token_revoke_view_invalid_token(self, api_client, user):
        """Test token revocation with invalid token."""
        api_client.force_authenticate(user=user)
        url = reverse("authentication:token_revoke")
        data = {
            "refresh": "invalid_token",
        }
        response = api_client.post(url, data)
        assert response.status_code == 400
        assert response.data["detail"] == "Invalid token"

    def test_token_revoke_view_unauthenticated(self, api_client, refresh_token):
        """Test token revocation when not authenticated."""
        url = reverse("authentication:token_revoke")
        data = {
            "refresh": refresh_token,
        }
        response = api_client.post(url, data)
        assert response.status_code == 401
