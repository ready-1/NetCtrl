"""
Helper function for retrieving Link Aggregation Group (LAG) settings from the switch.

This function interacts with the `/sw_lag_cfg` endpoint of the network switch API
to fetch LAG configuration details. The API allows querying specific LAG group
details or all LAG groups if `lag_group` is set to `ALL`.

Author: Bob King (Ready-1 LLC)
Date: 2025-01-02
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger
logger = logging.getLogger("app")

def get_lag_config(switch_ip: str, token: str, lag_group: str = "ALL") -> dict:
    """
    Retrieve Link Aggregation Group (LAG) settings from the switch.

    Parameters:
        switch_ip (str): The IP address of the target switch.
        token (str): Authentication token for API access.
        lag_group (str): LAG group ID (or "ALL" to fetch all groups). Example: "1", "ALL".

    Returns:
        dict: Parsed JSON response containing LAG settings.

    Raises:
        ValueError: If `lag_group` is invalid.
        InvalidResponse: If the response format is unexpected.
        Exception: For unexpected errors during the API call.

    Example Usage:
        response = get_lag_config("192.168.1.1", "token_string", lag_group="1")

    Example Response:
        {
            "resp": {
                "status": "success",
                "respCode": 0,
                "respMsg": "Operation successful"
            },
            "switchConfigLagGroup": {
                "lag_group": 1,
                "name": "LAG1",
                "groupId": 1,
                "adminMode": true,
                "type": 0,
                "members": [1, 2, 3]
            }
        }

    JSON Response Structure:
        - resp (object):
            - status (string): "success" or "failure".
            - respCode (integer): Response code.
            - respMsg (string): Response message.
        - switchConfigLagGroup (object):
            - lag_group (integer): LAG group ID (0 to 128).
            - name (string): LAG description.
            - groupId (integer): LAG group ID.
            - adminMode (boolean): LAG enabled state.
            - type (integer): LAG type (0: Dynamic/Static, 1: Static).
            - members (list): List of member port IDs.

    """
    endpoint = "/sw_lag_cfg"
    params = {"lag_group": lag_group}

    if not isinstance(lag_group, str) or not (lag_group.isdigit() or lag_group == "ALL"):
        raise ValueError("Invalid lag_group. Must be a numeric string or 'ALL'.")

    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = make_api_request(
            switch_ip=switch_ip,
            endpoint=endpoint,
            method="GET",
            headers=headers,
            params=params
        )

        if "resp" not in response or response["resp"].get("status") != "success":
            logger.error(f"Unexpected API response: {response}")
            raise InvalidResponse("Invalid API response.")

        return response

    except Exception as e:
        logger.exception("Error retrieving LAG configuration.")
        raise