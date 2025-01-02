"""
Helper function for POST /system_config.

This module provides a helper to set the system configuration on the switch using the POST /system_config API endpoint.
It ensures consistent error handling, response validation, and alignment with the API documentation.

Author: Bob King (Ready-1 LLC)
Date: 2025-01-01
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app")

def set_system_config(switch_ip: str, token: str, access_line: str, system_config: dict) -> dict:
    """
    Sets the system configuration for a switch.

    This function interacts with the POST /system_config endpoint to configure system settings for a specific
    access line type (console, telnet, or ssh).

    Parameters:
        switch_ip (str): The IP address of the target switch.
        token (str): Authentication token for the API.
        access_line (str): Access type for the system ("console", "telnet", or "ssh").
        system_config (dict): Dictionary containing system configuration fields as required by the API.

            Required Fields (from API documentation):
                - sysLineTerminalDefaultLen (int): Terminal default length.
                - sysLineTerminalLen (int): Terminal length.
                - sysSerialTimeOutDefault (int): Serial timeout default value.
                - sysSerialTimeOut (int): Serial timeout value.
                - sysTelnetServerAdminMode (str): Telnet server admin mode ("enabled" or "disabled").
                - sysTransferBytesCompleted (int): Number of bytes transferred.

    Returns:
        dict: Parsed and validated response from the API.

    Raises:
        ValueError: If inputs are invalid or required fields are missing.
        InvalidResponse: If the API response is unexpected or indicates an error.

    Example Usage:
        ```python
        response = set_system_config(
            switch_ip="192.168.1.1",
            token="abc123",
            access_line="console",
            system_config={
                "sysLineTerminalDefaultLen": 12,
                "sysLineTerminalLen": 24,
                "sysSerialTimeOutDefault": 0,
                "sysSerialTimeOut": 60,
                "sysTelnetServerAdminMode": "disabled",
                "sysTransferBytesCompleted": 1000
            }
        )
        print(response)
        ```

    Example Response:
        {
            "resp": {
                "respCode": 0,
                "respMsg": "Success"
            }
        }
    """
    # Validation rules based on the API documentation
    required_fields = [
        "sysLineTerminalDefaultLen",
        "sysLineTerminalLen",
        "sysSerialTimeOutDefault",
        "sysSerialTimeOut",
        "sysTelnetServerAdminMode",
        "sysTransferBytesCompleted",
    ]

    # Validate required fields
    missing_fields = [field for field in required_fields if field not in system_config]
    if missing_fields:
        raise ValueError(f"Missing required fields for '{access_line}': {missing_fields}")

    # Prepare request
    endpoint = "system_config"  # Correct endpoint to avoid duplication
    params = {"access_line": access_line}
    headers = {"Authorization": f"Bearer {token}"}
    data = {"system_config": system_config}

    # Make API request
    response = make_api_request(
        switch_ip=switch_ip,
        endpoint=endpoint,
        method="POST",
        headers=headers,
        params=params,
        data=data
    )

    # Validate response
    if "resp" not in response:
        logger.error("Missing 'resp' in API response")
        raise InvalidResponse("API response is missing 'resp' field.")
    
    resp = response["resp"]
    if resp.get("respCode") != 0:
        error_msg = f"API Error: {resp.get('respMsg', 'Unknown error')}"
        logger.error(error_msg)
        raise InvalidResponse(error_msg)

    return response