"""
Helper function for managing active images on a switch.

This module provides the helper function to set the active flash image of a switch via the /active_image POST API endpoint. 

Author: Bob King (Ready-1 LLC)
Date: 2024-12-31
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app")

def set_active_image(switch_ip: str, token: str, image_label: str) -> dict:
    """
    Sets the active flash image on the switch.

    Summary:
        Use the /active_image POST endpoint to set the active flash image on a switch.

    Purpose:
        This function helps configure the active image for a network switch, enabling seamless image management.

    Parameters:
        switch_ip (str): IP address of the target switch.
        token (str): Bearer token for authentication.
        image_label (str): The image label to activate. Must be 'image1' or 'image2'.

    Returns:
        dict: A dictionary with the API response details.

    Raises:
        ValueError: If inputs are invalid or image_label is not 'image1' or 'image2'.
        InvalidResponse: If the API response is not in the expected format.
        Exception: For other unexpected errors.

    Example Usage:
        >>> response = set_active_image("192.168.1.1", "abcdef123456", "image1")
        >>> print(response)

    Example Response:
        {
            "resp": {
                "status": "ok",
                "respCode": 0,
                "respMsg": "Active image set successfully"
            }
        }

    JSON Response Structure:
        {
            "resp": {
                "status": str,
                "respCode": int,
                "respMsg": str
            }
        }
        - resp.status: (str) Overall status of the operation ('ok' or 'error').
        - resp.respCode: (int) Response code (0 indicates success).
        - resp.respMsg: (str) Descriptive message of the operation.

    Note:
    Changing the active image on the switch may cause the API interface to lock up
    for approximately 30 seconds. During this time, other API calls may fail.
    This operation is primarily intended for troubleshooting and is often better
    performed through the switch's native web interface.

    """
    if not switch_ip or not token:
        raise ValueError("Both switch_ip and token must be provided.")
    if image_label not in {"image1", "image2"}:
        raise ValueError("Invalid image_label. Must be 'image1' or 'image2'.")

    endpoint = "/active_image"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    data = {
        "active_image": {"label": image_label}
    }

    try:
        response = make_api_request(
            switch_ip=switch_ip,
            endpoint=endpoint,
            method="POST",
            headers=headers,
            data=data
        )

        # Validate the response structure
        if "resp" not in response or not isinstance(response["resp"], dict):
            raise InvalidResponse("Response structure is invalid.")
        if response["resp"].get("respCode") != 0:
            logger.error(f"API Error: {response['resp'].get('respMsg')}")
            raise InvalidResponse(response["resp"].get("respMsg"))

        return response

    except Exception as e:
        logger.error(f"Failed to set active image: {e}")
        raise