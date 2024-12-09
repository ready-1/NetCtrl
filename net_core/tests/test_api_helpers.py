import requests
from django.test import TestCase
from unittest.mock import patch
from net_core.api_helpers import make_api_request


class MakeApiRequestTests(TestCase):
    """
    Test suite for the make_api_request function.

    These tests ensure that the make_api_request function handles various scenarios correctly,
    including successful requests, error handling, and edge cases.
    """

    @patch('net_core.api_helpers.requests.request')
    def test_get_request_success(self, mock_request):
        """
        Test a successful GET request.

        Ensures that the function correctly returns the JSON response
        when a GET request succeeds with a 200 status code.
        """
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = {"message": "success"}
        
        url = "https://example.com/api/resource"
        response = make_api_request(url, method="GET")
        
        self.assertEqual(response, {"message": "success"})
        mock_request.assert_called_once_with(
            method="GET",
            url=url,
            headers=None,
            json=None,
            params=None,
            timeout=10
        )

    @patch('net_core.api_helpers.requests.request')
    def test_post_request_success(self, mock_request):
        """
        Test a successful POST request.

        Verifies that the function correctly handles POST requests
        and returns the expected JSON response when successful.
        """
        mock_request.return_value.status_code = 201
        mock_request.return_value.json.return_value = {"id": 1, "message": "created"}
        
        url = "https://example.com/api/resource"
        data = {"name": "test"}
        headers = {"Content-Type": "application/json"}
        response = make_api_request(url, method="POST", headers=headers, data=data)
        
        self.assertEqual(response, {"id": 1, "message": "created"})
        mock_request.assert_called_once_with(
            method="POST",
            url=url,
            headers=headers,
            json=data,
            params=None,
            timeout=10
        )

    @patch('net_core.api_helpers.requests.request')
    def test_timeout_error(self, mock_request):
        """
        Test handling of a timeout error.

        Ensures that a TimeoutError is raised when the request times out.
        """
        mock_request.side_effect = requests.Timeout
        
        url = "https://example.com/api/resource"
        with self.assertRaises(TimeoutError):
            make_api_request(url, method="GET")
        mock_request.assert_called_once()

    @patch('net_core.api_helpers.requests.request')
    def test_connection_error(self, mock_request):
        """
        Test handling of a connection error.

        Verifies that a generic Exception is raised with the appropriate message
        when a connection error occurs.
        """
        mock_request.side_effect = requests.ConnectionError
        
        url = "https://example.com/api/resource"
        with self.assertRaises(Exception) as context:
            make_api_request(url, method="GET")
        self.assertIn("Connection error", str(context.exception))
        mock_request.assert_called_once()

    @patch('net_core.api_helpers.requests.request')
    def test_http_error(self, mock_request):
        """
        Test handling of HTTP errors.

        Ensures that a requests.HTTPError is raised and contains the appropriate
        status and error message when the server returns a 4xx or 5xx error.
        """
        mock_request.return_value.status_code = 404
        mock_request.return_value.raise_for_status.side_effect = requests.HTTPError("404 Not Found")
        
        url = "https://example.com/api/resource"
        with self.assertRaises(requests.HTTPError) as context:
            make_api_request(url, method="GET")
        
        self.assertIn("404 Not Found", str(context.exception))

    @patch('net_core.api_helpers.requests.request')
    def test_invalid_json_response(self, mock_request):
        """
        Test handling of a response that is not valid JSON.

        Ensures that a ValueError is raised when the server's response cannot be parsed as JSON.
        """
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.side_effect = ValueError  # Simulate invalid JSON
        
        url = "https://example.com/api/resource"
        with self.assertRaises(ValueError):
            make_api_request(url, method="GET")
        mock_request.assert_called_once()

    @patch('net_core.api_helpers.requests.request')
    def test_custom_headers_and_params(self, mock_request):
        """
        Test sending custom headers and query parameters.

        Ensures that custom headers and query parameters are correctly sent in the request.
        """
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = {"result": "success"}
        
        url = "https://example.com/api/resource"
        headers = {"Authorization": "Bearer token"}
        params = {"query": "test"}
        response = make_api_request(url, method="GET", headers=headers, params=params)
        
        self.assertEqual(response, {"result": "success"})
        mock_request.assert_called_once_with(
            method="GET",
            url=url,
            headers=headers,
            json=None,
            params=params,
            timeout=10
        )

    @patch('net_core.api_helpers.requests.request')
    def test_edge_case_empty_url(self, mock_request):
        """
        Test handling of an empty URL.

        Ensures that a ValueError is raised when the URL is empty or invalid.
        """
        url = ""
        with self.assertRaises(ValueError) as context:
            make_api_request(url, method="GET")
        
        self.assertIn("The URL provided is empty or invalid", str(context.exception))
        mock_request.assert_not_called()

    @patch('net_core.api_helpers.requests.request')
    def test_edge_case_invalid_method(self, mock_request):
        """
        Test handling of an invalid HTTP method.

        Verifies that a ValueError is raised when an unsupported HTTP method is provided.
        """
        url = "https://example.com/api/resource"
        with self.assertRaises(ValueError) as context:
            make_api_request(url, method="INVALID")
        
        self.assertIn("Invalid HTTP method", str(context.exception))
        mock_request.assert_not_called()