"""
Helper functions for managing device name.

This module provides a function to fetch the device name from the
network switch API. The function adheres to a consistent format with
detailed error handling and response validation.

Author: Bob King (Ready-1 LLC)
Date: 2024-12-28
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app")

# Constants
API_VERSION = "v1"
TIMEOUT = 10  # Default timeout for API requests

def get_device_name(switch_ip, token):
    """
    Fetches the device name using the NetCtrl REST API.

    Purpose:
        Retrieves the current device name from the network switch.

    Inputs:
        token (str): Bearer token for API authentication.

    Returns:
        dict: Dictionary containing the device name.
            Example: {"name": "NGTR_SW", "location": "TBD"}

    Raises:
        ValueError: If the token is invalid.
        InvalidResponse: If the API response is not as expected.

    Example Usage:
        token = "Bearer abc123"
        device_name = get_device_name(token)
        print(device_name)

    Example Response:
        {
            "name": "NGTR_SW",
            "location": "TBD"
        }

    JSON Response Structure:
        - `resp` (dict):
            - `status` (str): Response status.
            - `respCode` (int): Response code (0 for success).
            - `respMsg` (str): Response message.
        - `deviceName` (dict):
            - `name` (str): Device name.
            - `location` (str): Device location.

    """
    if not isinstance(token, str) or not token.strip():
        raise ValueError("Invalid token provided.")

    url = f"https://127.0.0.1:8443/api/{API_VERSION}/device_name"
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = make_api_request("GET", url, headers=headers, timeout=TIMEOUT)

        if "resp" not in response or "deviceName" not in response:
            raise InvalidResponse("Missing 'resp' or 'deviceName' in response.")

        resp = response["resp"]
        if resp.get("respCode") != 0:
            raise InvalidResponse(f"API Error: {resp.get('respMsg')}")

        device_name = response["deviceName"]
        return {
            "name": device_name.get("name"),
            "location": device_name.get("location"),
        }

    except InvalidResponse as e:
        logger.error(f"Invalid API response: {e}")
        raise
    except Exception as e:
        logger.error(f"Error fetching device name: {e}")
        raise