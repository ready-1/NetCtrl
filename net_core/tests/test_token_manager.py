import os
from django.test import TestCase
from unittest.mock import patch, MagicMock
from net_core.api_helpers.token_manager import TokenManager
from net_core.api_helpers.utils import make_api_request
from django.core.cache import cache


class TokenManagerTests(TestCase):

    def setUp(self):
        # Read environment variables
        self.switch_ip = os.getenv("SWITCH_IP", "192.168.1.1")
        self.username = os.getenv("SWITCH_USERNAME", "admin")
        self.password = os.getenv("SWITCH_PASSWORD", "password123")
        self.token = "mock_token"

    @patch("net_core.api_helpers.token_manager.cache.get")
    def test_get_token_from_cache(self, mock_cache_get):
        """Test retrieving token from cache."""
        mock_cache_get.return_value = self.token
        retrieved_token = TokenManager.get_token(self.switch_ip, self.username, self.password)
        self.assertEqual(retrieved_token, self.token)
        mock_cache_get.assert_called_with(f"switch_token_{self.switch_ip}")

    @patch("net_core.api_helpers.token_manager.requests.post")
    @patch("net_core.api_helpers.token_manager.cache.set")
    def test_fetch_token_and_cache(self, mock_cache_set, mock_requests_post):
        """Test fetching a new token and caching it."""
        # Simulate API response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "resp": {"status": "success", "respCode": 0, "respMsg": "Login successful"},
            "login": {"token": self.token, "expire": 3600}
        }
        mock_requests_post.return_value = mock_response

        # Call fetch token
        retrieved_token = TokenManager._fetch_token(self.switch_ip, self.username, self.password)
        self.assertEqual(retrieved_token, self.token)
        mock_requests_post.assert_called_once()
        mock_cache_set.assert_called_with(
            f"switch_token_{self.switch_ip}",
            self.token,
            timeout=3590  # 3600 seconds minus 10 for safety
        )

    @patch("net_core.api_helpers.token_manager.requests.post")
    def test_fetch_token_invalid_response(self, mock_requests_post):
        """Test handling an invalid response structure."""
        # Simulate invalid API response
        mock_response = MagicMock()
        mock_response.json.return_value = {"unexpected_key": "unexpected_value"}
        mock_requests_post.return_value = mock_response

        with self.assertRaises(ValueError) as context:
            TokenManager._fetch_token(self.switch_ip, self.username, self.password)

        self.assertIn("Invalid response structure", str(context.exception))

    @patch("net_core.api_helpers.token_manager.cache.get")
    @patch("net_core.api_helpers.utils.requests.request")
    def test_make_api_request_with_cached_token(self, mock_request, mock_cache_get):
        """Test making an API request with a cached token."""
        mock_cache_get.return_value = self.token

        # Simulate API response
        mock_response = MagicMock()
        mock_response.json.return_value = {"result": "success"}
        mock_request.return_value = mock_response

        response = make_api_request(self.switch_ip, "endpoint", "GET")
        self.assertEqual(response, {"result": "success"})
        mock_request.assert_called_once_with(
            method="GET",
            url=f"https://{self.switch_ip}:8443/api/v1/endpoint",
            headers={"Authorization": f"Bearer {self.token}", "Accept": "application/json"},
            json=None,
            params=None,
            timeout=10,
            verify=False
        )

    @patch("net_core.api_helpers.token_manager.cache.get")
    @patch("net_core.api_helpers.token_manager.TokenManager._fetch_token")
    @patch("net_core.api_helpers.utils.requests.request")
    def test_make_api_request_token_expired(self, mock_request, mock_fetch_token, mock_cache_get):
        """Test making an API request with an expired token."""
        mock_cache_get.return_value = None  # Simulate token expired
        mock_fetch_token.return_value = self.token

        # Simulate API response
        mock_response = MagicMock()
        mock_response.json.return_value = {"result": "success"}
        mock_request.return_value = mock_response

        response = make_api_request(self.switch_ip, "endpoint", "GET")
        self.assertEqual(response, {"result": "success"})
        mock_fetch_token.assert_called_once_with(self.switch_ip, self.username, self.password)
        mock_request.assert_called_once_with(
            method="GET",
            url=f"https://{self.switch_ip}:8443/api/v1/endpoint",
            headers={"Authorization": f"Bearer {self.token}", "Accept": "application/json"},
            json=None,
            params=None,
            timeout=10,
            verify=False
        )