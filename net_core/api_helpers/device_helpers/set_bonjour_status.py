"""
Helper function for managing Bonjour settings on the switch.

This module provides a function to interact with the `/bonjour` endpoint
of the network switch API. It allows enabling or disabling the Bonjour service
on the device.

Author: Bob King (Ready-1 LLC)
Date: 2024-12-30
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app")

# Constants
TIMEOUT = 10  # Default timeout for API requests

def set_bonjour_status(switch_ip: str, token: str, status: str) -> dict:
    """
    Set the Bonjour status on a network switch.

    This function calls the `/bonjour` POST endpoint to set the Bonjour service
    status on the target switch.

    Args:
        switch_ip (str): The IP address of the target switch.
        token (str): Bearer token for authentication.
        status (str): Desired Bonjour status, either 'enabled' or 'disabled'.

    Returns:
        dict: Parsed JSON response from the API containing the result of the operation.

    Raises:
        ValueError: If any input parameters are invalid.
        InvalidResponse: If the API response format is unexpected or indicates failure.
        requests.HTTPError: If an HTTP error occurs during the request.
    """
    # Input validation
    if status not in ["enabled", "disabled"]:
        raise ValueError(f"Invalid Bonjour status: {status}. Must be 'enabled' or 'disabled'.")

    # Prepare API request
    endpoint = "/bonjour"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"bonjour": {"status": status}}

    # Make API request
    try:
        response = make_api_request(
            switch_ip=switch_ip,
            endpoint=endpoint,
            method="POST",
            data=payload,
            headers=headers,
            timeout=TIMEOUT,
        )
    except Exception as e:
        logger.error(f"Error making API request to {endpoint}: {e}")
        raise

    # Validate API response
    if "resp" not in response or "respCode" not in response["resp"]:
        raise InvalidResponse("Missing 'resp' or 'respCode' in API response.")

    resp_code = response["resp"]["respCode"]
    resp_msg = response["resp"].get("respMsg", "No message provided.")

    if resp_code != 0:
        logger.error(f"API error for {endpoint}: {resp_msg}")
        raise InvalidResponse(f"API error {resp_code}: {resp_msg}")

    logger.info(f"Successfully set Bonjour status to '{status}' on switch {switch_ip}.")
    return response

"""
Example Usage:
---------------
try:
    result = set_bonjour_status("192.168.1.1", "your_token", "enabled")
    print("Response:", result)
except Exception as e:
    print("Error:", str(e))
"""