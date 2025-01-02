"""
Helper functions for managing Bonjour status on network switches.

This module provides functions to retrieve the Bonjour status of a network switch
via the REST API. Each function adheres to a consistent format with detailed error
handling and response validation.

Author: Bob King (Ready-1 LLC)
Date: 2024-12-30
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app")

def get_bonjour_status(switch_ip: str, token: str) -> dict:
    """
    Retrieves the Bonjour status of a network switch.

    Purpose:
        This function calls the /bonjour GET endpoint of the switch REST API
        to retrieve the current Bonjour status.

    Inputs:
        switch_ip (str): The IP address of the target switch.
        token (str): The authentication token for the API.

    Returns:
        dict: A dictionary containing the Bonjour status.

    Raises:
        ValueError: If the inputs are invalid.
        InvalidResponse: If the API response format is unexpected or missing fields.
        Exception: For other errors during the API call.

    Example Usage:
        >>> status = get_bonjour_status("192.168.1.1", "token123")
        >>> print(status)

    Example Response:
        {
            "bonjour": {
                "status": "enabled"
            }
        }

    JSON Response Structure:
        {
            "bonjour": {
                "status": str (enabled/disabled),
                "description": "Set the Bonjour status."
            }
        }

    """
    if not switch_ip or not isinstance(switch_ip, str):
        raise ValueError("Invalid switch_ip. It must be a non-empty string.")
    if not token or not isinstance(token, str):
        raise ValueError("Invalid token. It must be a non-empty string.")

    endpoint = "/bonjour"
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = make_api_request(
            switch_ip=switch_ip,
            endpoint=endpoint,
            method="GET",
            headers=headers,
            timeout=10
        )
    except Exception as e:
        logger.error(f"Failed to call {endpoint} for switch {switch_ip}: {e}")
        raise

    if "bonjour" not in response:
        logger.error(f"Unexpected response format: {response}")
        raise InvalidResponse("Missing 'bonjour' field in the API response.")

    return response["bonjour"]