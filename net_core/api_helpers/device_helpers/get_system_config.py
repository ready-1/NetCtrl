"""
Helper function for retrieving system configuration.

This module provides a function to interact with the `GET /system_config` endpoint
of the network switch API. It fetches console, telnet, and related settings.

Author: Bob King (Ready-1 LLC)
Date: 2024-12-31
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app.device_helpers.get_system_config")

def get_system_config(switch_ip: str, token: str, access_line: str = "console") -> dict:
    """
    Retrieves system configuration from the switch.

    Purpose:
        Interacts with the `GET /system_config` endpoint to fetch settings
        such as console, telnet, and SSH access configurations.

    Parameters:
        switch_ip (str): The IP address of the target switch.
        token (str): The authentication token for the API request.
        access_line (str): The system access type. Must be one of:
            - `console`
            - `telnet`
            - `ssh`
            Defaults to "console".

    Returns:
        dict: A dictionary containing system configuration details.

    Raises:
        ValueError: If `switch_ip`, `token`, or `access_line` is invalid.
        InvalidResponse: If the API response is not as expected or respCode != 0.
        Exception: For any unexpected errors during the API call.

    Example Usage:
        ```python
        config = get_system_config("192.168.1.1", "Bearer abc123", "console")
        print(config)
        ```

    Example Response:
        ```json
        {
            "sysAccessLine": "console",
            "sysLineTerminalLen": 48,
            "sysSerialTimeOut": 120,
            "sysTelnetServerAdminMode": "enabled"
        }
        ```

    JSON Response Structure:
        - sysAccessLine (str): System access type setting. Possible values:
            * `console`
            * `telnet`
            * `ssh`
        - sysLineTerminalLen (int): Terminal length of an access line.
        - sysSerialTimeOut (int): Serial timeout.
        - sysTelnetServerAdminMode (str): Telnet server admin mode. Possible values:
            * `enabled`
            * `disabled`
    """
    # Validate inputs
    if not switch_ip or not isinstance(switch_ip, str):
        raise ValueError("Invalid switch IP address provided.")
    if not token or not isinstance(token, str):
        raise ValueError("Invalid token provided.")
    if access_line not in {"console", "telnet", "ssh"}:
        raise ValueError("Invalid access_line value. Must be one of ['console', 'telnet', 'ssh'].")

    endpoint = "/system_config"
    headers = {"Authorization": token}
    params = {"access_line": access_line}

    try:
        response = make_api_request(
            switch_ip=switch_ip,
            endpoint=endpoint,
            method="GET",
            headers=headers,
            params=params
        )
        # Check for API-specific errors
        if "resp" not in response or response["resp"].get("respCode") != 0:
            raise InvalidResponse(f"API returned an error: {response.get('resp', {}).get('respMsg', 'Unknown error')}")

        # Extract and return relevant data
        return response.get("system_config", {})
    except Exception as e:
        logger.error(f"Failed to fetch system configuration: {e}")
        raise