"""
Helper functions for retrieving the device name.

This module provides a function to interact with the `/device_name` endpoint
of the network switch API. It retrieves the name and location of the device.

Author: Bob King (Ready-1 LLC)
Date: 2024-12-28
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app")

# Constants specific to this module
TIMEOUT = 10  # Default timeout for API requests

def get_device_name(switch_ip: str, token: str) -> dict:
    """
    Retrieve the device name and location from the `/device_name` endpoint.

    Purpose:
        Fetches the device name and location for the specified switch.

    Inputs:
        switch_ip (str): The IP address of the target switch.
        token (str): The authentication token for the API.

    Returns:
        dict: A dictionary containing the device name and location.

    Raises:
        ValueError: If inputs are invalid (e.g., missing or malformed).
        InvalidResponse: If the API response is not as expected.

    Example Usage:
        >>> get_device_name("192.168.1.1", "your_auth_token")
        {
            "name": "NGTR_SW",
            "location": "TBD"
        }

    Example Response:
        {
            "resp": {
                "status": "success",
                "respCode": 0,
                "respMsg": "Device name retrieved successfully"
            },
            "deviceName": {
                "name": "NGTR_SW",
                "location": "TBD"
            }
        }

    JSON Response Structure:
        - resp (dict):
            - status (str): Response status, e.g., "success".
            - respCode (int): Response code (0 indicates success).
            - respMsg (str): Response message.
        - deviceName (dict):
            - name (str): The device's name.
            - location (str): The device's location.

    """
    # Validate inputs
    if not switch_ip or not isinstance(switch_ip, str):
        raise ValueError("Invalid switch_ip: must be a non-empty string.")
    if not token or not isinstance(token, str):
        raise ValueError("Invalid token: must be a non-empty string.")

    # Endpoint for the API call
    endpoint = "/device_name"
    headers = {"Authorization": f"Bearer {token}"}

    try:
        # Make the API request
        response = make_api_request(
            switch_ip=switch_ip,
            endpoint=endpoint,
            method="GET",
            headers=headers,
            timeout=TIMEOUT
        )

        # Validate the response
        if not response.get("resp") or response["resp"].get("respCode") != 0:
            raise InvalidResponse(
                f"Error from API: {response['resp'].get('respMsg', 'Unknown error')}"
            )
        
        if "deviceName" not in response:
            raise InvalidResponse("Missing 'deviceName' in API response.")

        # Return relevant data
        return response["deviceName"]

    except Exception as e:
        logger.error(f"Failed to retrieve device name: {e}")
        raise