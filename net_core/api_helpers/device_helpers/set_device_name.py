"""
Helper functions for device name and location management.

This module provides functions to interact with the `/device_name` endpoint
of the network switch API. The function allows setting the device name and optionally the location.

Author: Bob King (Ready-1 LLC)
Date: 2024-12-28
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app.device_helpers.set_device_name")

def set_device_name(
    switch_ip: str, token: str, device_name: str, device_location: str = None
) -> dict:
    """
    Set the device name and optionally the location on the switch using the `/device_name` endpoint.

    Purpose:
        This function sends a POST request to set the device name and optionally
        the location of the target switch.

    Inputs:
        - switch_ip (str): The IP address of the target switch.
        - token (str): The authentication token for the switch.
        - device_name (str): The new name for the device.
        - device_location (str, optional): The location of the device.

    Returns:
        dict: Parsed response with relevant details.

    Raises:
        ValueError: If input parameters are invalid.
        InvalidResponse: If the API response is unexpected.
        Exception: For general errors during the request.

    Example Usage:
        ```
        response = set_device_name(
            switch_ip="192.168.1.1",
            token="abc123",
            device_name="NewSwitchName",
            device_location="Server Room"
        )
        print(response)
        ```

    Example Response:
        ```
        {
            "resp": {
                "respCode": 0,
                "respMsg": "Success"
            }
        }
        ```

    JSON Response Structure:
        - resp (dict):
            - respCode (int): Status code (e.g., 0 for success).
            - respMsg (str): Message describing the response (e.g., "Success").
    """
    # Input validation
    if not switch_ip or not isinstance(switch_ip, str):
        raise ValueError("Invalid switch_ip parameter.")
    if not token or not isinstance(token, str):
        raise ValueError("Invalid token parameter.")
    if not device_name or not isinstance(device_name, str):
        raise ValueError("Invalid device_name parameter.")
    if device_location and not isinstance(device_location, str):
        raise ValueError("Invalid device_location parameter.")

    # Prepare API request details
    endpoint = "/device_name"
    headers = {"Authorization": f"Bearer {token}"}
    data = {"deviceName": {"name": device_name}}
    if device_location:
        data["deviceName"]["location"] = device_location

    try:
        # Make the API request
        response = make_api_request(
            switch_ip=switch_ip,
            endpoint=endpoint,
            method="POST",
            data=data,
            headers=headers
        )

        # Validate API response
        if "resp" not in response or not isinstance(response["resp"], dict):
            logger.error("Invalid response format: %s", response)
            raise InvalidResponse("Missing or malformed 'resp' in response.")

        resp_code = response["resp"].get("respCode")
        if resp_code != 0:
            logger.error("API error: %s", response["resp"].get("respMsg"))
            raise InvalidResponse(f"API returned error code {resp_code}.")

        return response

    except Exception as e:
        logger.exception("Failed to set device name and location.")
        raise e