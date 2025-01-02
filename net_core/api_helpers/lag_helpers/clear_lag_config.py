"""
Helper function for clearing a Link Aggregation Group (LAG) configuration.

This module provides a convenience function to clear an existing LAG group by disabling it
and removing all members. It retrieves the current LAG configuration and modifies it as needed.

Author: Bob King (Ready-1 LLC)
Date: 2025-01-02
"""

import logging
from net_core.api_helpers.lag_helpers.get_lag_config import get_lag_config
from net_core.api_helpers.lag_helpers.set_lag_config import set_lag_config

logger = logging.getLogger("app")

def clear_lag_config(switch_ip: str, token: str, lag_group: int) -> dict:
    """
    Clears a Link Aggregation Group (LAG) configuration on a network switch.

    **Purpose**:
    - Retrieves the current LAG configuration.
    - Disables the LAG group (admin mode set to False).
    - Removes all member ports.

    Parameters:
        switch_ip (str): IP address of the target switch.
        token (str): Authorization token for the switch.
        lag_group (int): LAG group ID to clear.

    Returns:
        dict: Processed response from the `set_lag_config` call.

    Raises:
        ValueError: If the `lag_group` does not exist or cannot be retrieved.
        Exception: For unexpected errors during the API calls.

    Example Usage:
        ```python
        response = clear_lag_config(
            switch_ip="192.168.1.1",
            token="abc123",
            lag_group=3
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
    """
    try:
        # Retrieve current configuration
        current_config = get_lag_config(switch_ip, token, lag_group)['switchConfigLagGroup']
        if not current_config:
            raise ValueError(f"LAG group {lag_group} does not exist or could not be retrieved.")
        
        # Clear configuration
        response = set_lag_config(
            switch_ip=switch_ip,
            token=token,
            lag_group=current_config.get('groupId'),
            name=f"ch{current_config.get('groupId')}",
            group_id=current_config.get('groupId'),
            admin_mode=False,
            lag_type=current_config.get('type', 0),
            members=[]
        )
        logger.info(f"LAG group {lag_group} cleared successfully.")
        return response
    except Exception as e:
        logger.error(f"Failed to clear LAG group {lag_group}: {e}")
        raise