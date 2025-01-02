"""
Helper function for configuring Link Aggregation Group (LAG) settings.

This module provides a function to interact with the `/sw_lag_cfg` endpoint
of the network switch API. The endpoint is used to set Link Aggregation Group settings.

Author: Bob King (Ready-1 LLC)
Date: 2025-01-02
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

logger = logging.getLogger("app")

def set_lag_config(switch_ip: str, token: str, lag_group: int, name: str, group_id: int, 
                   admin_mode: bool, lag_type: int, members: list[int]) -> dict:
    """
    Sets Link Aggregation Group (LAG) settings on a network switch.

    **Endpoint**: POST /sw_lag_cfg

    **Purpose**: Configure or modify LAG group settings on a switch.

    Parameters:
        switch_ip (str): IP address of the target switch.
        token (str): Authorization token for the switch.
        lag_group (int): LAG group ID (0 to create a new group, non-zero to modify).
        name (str): Description for the LAG group.
        group_id (int): Unique identifier for the LAG group.
        admin_mode (bool): Enable or disable the LAG group.
        lag_type (int): Type of LAG (0 for Dynamic/Static, 1 for Static).
        members (list[int]): List of member port IDs for the LAG.

    Returns:
        dict: Processed response from the API.

    Raises:
        ValueError: If input parameters are invalid.
        InvalidResponse: If the API response format is unexpected.
        Exception: For other unexpected errors during the API call.

    Example Usage:
        ```python
        response = set_lag_config(
            switch_ip="192.168.1.1",
            token="abc123",
            lag_group=3,
            name="LAG3",
            group_id=3,
            admin_mode=True,
            lag_type=0,
            members=[2, 3, 4, 5]
        )
        print(response)
        ```

    Example Response:
        {
            "resp": {
                "status": "success",
                "respCode": 0,
                "respMsg": "LAG configuration updated successfully."
            }
        }

    JSON Response Structure:
        resp (dict): API response status.
            - status (str): Indicates success or failure. Allowed values: "success", "failure".
            - respCode (int): Response code. `0` indicates success.
            - respMsg (str): Message describing the response.
    """
    # Validate inputs
    if not (0 <= lag_group <= 128):
        raise ValueError("lag_group must be between 0 and 128.")
    if not isinstance(name, str) or not name.strip():
        raise ValueError("name must be a non-empty string.")
    if not (0 <= lag_type <= 1):
        raise ValueError("lag_type must be 0 (Dynamic/Static) or 1 (Static).")
    if not isinstance(members, list) or not all(isinstance(port, int) for port in members):
        raise ValueError("members must be a list of integers.")

    # Prepare API request
    endpoint = "/sw_lag_cfg"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "switchConfigLagGroup": {
            "name": name,
            "groupId": group_id,
            "adminMode": admin_mode,
            "type": lag_type,
            "members": members,
            "lag_group": lag_group  # Redundant but included as part of the API design
        }
    }
    query_params = {"lag_group": lag_group}

    # Make API request
    try:
        response = make_api_request(
            switch_ip=switch_ip,
            endpoint=endpoint,
            method="POST",
            headers=headers,
            data=payload,
            params=query_params,  # Add query parameters for lag_group
        )
        # Validate response
        if not response.get("resp"):
            raise InvalidResponse("Response is missing the 'resp' field.")
        if response["resp"].get("respCode") != 0:
            raise InvalidResponse(f"API Error: {response['resp'].get('respMsg')}")
        return response
    except Exception as e:
        logger.error(f"Failed to set LAG configuration: {e}")
        raise