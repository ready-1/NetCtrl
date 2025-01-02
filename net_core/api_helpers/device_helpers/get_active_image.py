"""
Helper function to interact with the /active_image GET endpoint.

This function retrieves the active flash image details of the switch.

Author: Bob King (Ready-1 LLC)
Date: [Today's date]
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app.device_helpers")

def get_active_image(switch_ip: str, token: str) -> dict:
    """
    Retrieves the active flash image details from the switch.

    Purpose:
        Fetches information about the currently active flash image on the device.

    Parameters:
        switch_ip (str): The IP address of the target switch.
        token (str): Authorization token for the API.

    Returns:
        dict: Processed response containing the active image details.

    Raises:
        ValueError: If input parameters are invalid.
        InvalidResponse: If the API response is invalid or the respCode is not '0'.
        Exception: For unexpected errors.

    Example Usage:
        active_image = get_active_image("192.168.1.1", "Bearer <token>")
        print(active_image)

    Example Response:
        {
            "label": "image1",
            "imageDescr": "Test Img"
        }

    JSON Response Structure:
        {
            "resp": {
                "respCode": 0,
                "respMsg": "Success"
            },
            "active_image": {
                "label": str,  # Active image label, e.g., 'image1'
                "imageDescr": str  # Description of the active image, e.g., 'Test Img'
            }
        }
    """
    if not isinstance(switch_ip, str) or not switch_ip:
        raise ValueError("Invalid switch IP address.")
    if not isinstance(token, str) or not token:
        raise ValueError("Invalid token.")

    endpoint = "/active_image"
    headers = {"Authorization": token}
    try:
        # Make API request
        response = make_api_request(
            switch_ip=switch_ip,
            endpoint=endpoint,
            method="GET",
            headers=headers,
        )
        # Validate response
        if not response or "resp" not in response or "active_image" not in response:
            raise InvalidResponse(f"Unexpected response format: {response}")
        if response["resp"].get("respCode") != 0:
            raise InvalidResponse(
                f"API error {response['resp'].get('respCode')}: {response['resp'].get('respMsg')}"
            )

        # Process and return relevant data
        return response["active_image"]

    except Exception as e:
        logger.error(f"Error fetching active image: {e}")
        raise