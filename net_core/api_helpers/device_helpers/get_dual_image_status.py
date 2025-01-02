"""
Helper function for the /dual_image_status endpoint.

This module provides a function to retrieve information about the dual firmware images
on a network switch using the /dual_image_status API endpoint.

Author: Bob King (Ready-1 LLC)
Date: 2024-12-30
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger
logger = logging.getLogger("app")

# Constants
ENDPOINT = "dual_image_status"
TIMEOUT = 10  # Timeout for API requests

def get_dual_image_status(switch_ip: str, token: str) -> dict:
    """
    Retrieves the dual image status from the network switch.

    Summary:
        Retrieve firmware image status, including active and inactive images.

    Purpose:
        This function queries the switch for details about the two firmware images
        and identifies which one is currently active.

    Inputs:
        - switch_ip (str): The IP address of the target switch.
        - token (str): Bearer token for API authentication.

    Returns:
        dict: Parsed response containing dual image status.

    Raises:
        - ValueError: If inputs are invalid.
        - InvalidResponse: If the API response is unexpected.

    Example Usage:
        response = get_dual_image_status("192.168.99.92", "your_token_here")
        print(response)

    Example Response:
        {
            "image1Label": "image1",
            "image1Descr": "",
            "image1Version": "3.28.0.1",
            "image2Label": "image2",
            "image2Descr": "",
            "image2Version": "3.30.11.1",
            "activatedImgLabel": "image2"
        }

    JSON Response Structure:
        - image1Label (str): Label of the first image.
        - image1Descr (str): Description of the first image.
        - image1Version (str): Version of the first image.
        - image2Label (str): Label of the second image.
        - image2Descr (str): Description of the second image.
        - image2Version (str): Version of the second image.
        - activatedImgLabel (str): Label of the currently active image.
    """
    # Input validation
    if not isinstance(switch_ip, str) or not switch_ip:
        raise ValueError("Invalid switch_ip.")
    if not isinstance(token, str) or not token:
        raise ValueError("Invalid token.")

    # Request headers
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}",
    }

    try:
        # Make the API request
        response = make_api_request(
            switch_ip=switch_ip,
            endpoint=ENDPOINT,
            method="GET",
            headers=headers,
            timeout=TIMEOUT,
        )

        # Validate the response
        if not isinstance(response, dict) or "resp" not in response or "dualImageStatus" not in response:
            raise InvalidResponse("Unexpected response structure.")

        # Extract the respCode and validate it
        resp_code = response["resp"].get("respCode")
        if resp_code != 0:
            raise InvalidResponse(f"API responded with error code: {resp_code}")

        # Return the dualImageStatus data
        return response["dualImageStatus"]

    except Exception as e:
        logger.error(f"Error fetching dual image status: {e}")
        raise