"""
Helper function for adding a new multicast group.

This function interacts with the multicast group addition endpoint
of the network switch API. It adheres to a consistent format with detailed
error handling and response validation.

Author: Bob King (Ready-1 LLC) 
Date: [Today's date]
"""

import logging
import json
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app")

def add_multicast_group(switch_ip: str, token: str, group_id: str, config: dict) -> dict:
    logger.debug(f"Entering add_multicast_group with parameters: {json.dumps(locals(), indent=2)}")
    """
    Adds a new multicast group to the network switch.

    Purpose:
        This function calls the '/add_multicast_group' endpoint to create
        a new multicast group with the specified configuration.

    Inputs:
        switch_ip (str): The IP address of the target switch.
        token (str): The bearer token to use for authentication.
        group_id (str): The ID of the multicast group to add.
        config (dict): The configuration settings for the new multicast group.

    Returns:
        dict: Parsed JSON response confirming the multicast group was added.

    Raises:
        ValueError: If the input parameters are invalid.
        InvalidResponse: If the API response format is unexpected.
        Exception: For any other errors during the API call.

    Example Usage:
        config = {"status": "active"}
        response = add_multicast_group("192.168.1.1", "your_token_here", "239.255.0.1", config)

    Example Response:
        {
            "resp": {
                "status": "success",
                "respCode": 0,
                "respMsg": "Multicast group added successfully"
            }
        }

    JSON Response Structure:
        - resp: object
            - status: string (e.g., "success", "error")
            - respCode: integer (0 for success, other values for errors)
            - respMsg: string (message describing the response)
    """
    if not isinstance(switch_ip, str) or not isinstance(token, str) or not isinstance(group_id, str) or not isinstance(config, dict):
        raise ValueError("Invalid input parameters: switch_ip, token, and group_id must be strings, config must be a dictionary.")

    endpoint = "/add_multicast_group"
    logger.debug(f"API endpoint: {endpoint}, data: {json.dumps(data, indent=2)}")
