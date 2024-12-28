import logging
import requests
import urllib3
from requests.exceptions import HTTPError
from datetime import datetime, timedelta
from django.conf import settings

from net_core.api_helpers.utils import make_api_request
from net_core.api_helpers.token_manager import TokenManager

# Suppress only the specific SSL warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Get the logger defined in settings.py
logger = logging.getLogger('app')

# Define valid HTTP methods for validation
VALID_HTTP_METHODS = {"GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "HEAD"}


class InvalidResponse(Exception):
    """Custom exception for invalid API responses."""
    pass


def login_to_device(switch_ip: str, username: str, password: str) -> dict:
    """
    Logs into the device and retrieves an authentication token.

    Parameters:
        switch_ip (str): The IP address of the target switch.
        username (str): Admin username for the switch.
        password (str): Admin user's password.

    Returns:
        dict: A dictionary containing the token and expiration time.
            Example:
                {
                    "token": "abc123",
                    "expires": 3600
                }

    Raises:
        ValueError: If any input parameter is invalid.
        InvalidResponse: If the API response structure or data is unexpected.
        HTTPError: If an HTTP error occurs during the API call.

    Example Usage:
        try:
            response = login_to_device("192.168.1.1", "admin", "password123")
            print(f"Token: {response['token']}, Expires in: {response['expires']} seconds")
        except Exception as e:
            print(f"Login failed: {e}")

    Example Response:
        {
            "resp": {
                "status": "success",
                "respCode": 0,
                "respMsg": "Login successful"
            },
            "login": {
                "token": "abc123",
                "expires": 3600
            }
        }
    """
    # Validate inputs
    if not isinstance(switch_ip, str) or not switch_ip.strip():
        raise ValueError("Invalid switch_ip: Must be a non-empty string.")
    if not isinstance(username, str) or not username.strip():
        raise ValueError("Invalid username: Must be a non-empty string.")
    if not isinstance(password, str) or not password.strip():
        raise ValueError("Invalid password: Must be a non-empty string.")

    # API request details
    endpoint = "login"
    method = "POST"
    data = {
        "login": {
            "username": username,
            "password": password
        }
    }

    try:
        # Make the API request
        response = make_api_request(switch_ip, endpoint, method=method, data=data)

        # Validate response structure
        if not isinstance(response, dict) or "resp" not in response or "login" not in response:
            raise InvalidResponse("Invalid response structure.")

        # Validate response status
        resp = response["resp"]
        if resp.get("status") != "success" or resp.get("respCode") != 0:
            raise InvalidResponse(f"API Error: {resp.get('respMsg', 'Unknown error')}")

        # Extract and return login data
        login_data = response["login"]
        token = login_data.get("token")
        expires = login_data.get("expires")
        if not token or not isinstance(expires, int):
            raise InvalidResponse("Missing or invalid token data in response.")
        
        return {"token": token, "expires": expires}

    except HTTPError as http_err:
        logger.error(f"HTTP error during login: {http_err}")
        raise
    except InvalidResponse as ir:
        logger.error(f"Invalid response: {ir}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during login: {e}")
        raise