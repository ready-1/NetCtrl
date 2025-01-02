"""
Helper functions for Port Mirroring Configuration.

This module provides a function to interact with the `/sw_portmirroring` endpoint
of the network switch API. It handles setting port mirroring configurations with
detailed error handling and response validation.

Author: Bob King (Ready-1 LLC)
Date: 2025-01-02
"""

import json
import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app")


def set_port_mirroring(switch_ip: str, token: str, session_num: int, admin_mode: str, dest_port: int, src_ports: list):
    """
    Configure port mirroring on the switch using Token Authentication.

    Adjusted to match the correct payload structure and data types based on the working payload.

    Summary:
        Configures port mirroring settings for the specified session.

    Purpose:
        This function sends a request to the `/sw_portmirroring` endpoint
        to configure port mirroring on the specified session of a network switch.

    Inputs:
        - switch_ip (str): IP address of the switch.
        - token (str): Authentication token for the switch API.
        - session_num (int): Port mirroring session number (1-4).
        - admin_mode (str): Port mirroring admin mode configuration (`"true"` or `"false"`).
        - dest_port (int): Destination or probe port ID. No ports selected when set to `0`.
        - src_ports (list of dict): List of source port objects with the following keys:
            * `intfType` (int): Source port capture type. Enum values:
                - `0`: INTF_TYPE_PHY
                - `1`: INTF_TYPE_CPU
                - `2`: INTF_TYPE_LAG
                - `3`: INTF_TYPE_VLAN
                - `4`: INTF_TYPE_LOOPBACK
                - `5`: INTF_TYPE_TUNNEL
                - `6`: INTF_TYPE_SERVICE_PORT
                - `7`: INTF_TYPE_OTHER
                - `8`: INTF_TYPE_ANY
            * `intfNum` (int): Source port interface number.
            * `direction` (int): Source port capture direction. Enum values:
                - `1`: BIDIRECTIONAL
                - `2`: INGRESS
                - `3`: EGRESS
                - `4`: SFLOW

    Returns:
        dict: Parsed API response containing:
            - `resp` (dict):
                * `status` (str): Operation status. Enum values:
                    - `success`
                    - `failure`
                * `respCode` (int): Response code.
                * `respMsg` (str): Response message.

    Raises:
        - ValueError: If invalid input parameters are provided.
        - InvalidResponse: If the API response format is unexpected or indicates failure.

    Example Usage:
        ```python
        response = set_port_mirroring(
            switch_ip="192.168.1.1",
            token="abc123",
            session_num=2,
            admin_mode="true",
            dest_port=21,
            src_ports=[
                {"intfType": 0, "intfNum": 22, "direction": 1},
                {"intfType": 0, "intfNum": 23, "direction": 2}
            ]
        )
        print(response)
        ```

    Example Response:
        ```json
        {
            "resp": {
                "status": "success",
                "respCode": 0,
                "respMsg": "Operation success"
            }
        }
        ```

    JSON Response Structure:
        - `resp` (dict): Top-level response object.
            * `status` (str): Operation status. Enum values:
                - `success`
                - `failure`
            * `respCode` (int): Response code.
            * `respMsg` (str): Response message.
    """
    # Validate inputs
    if not isinstance(session_num, int) or session_num not in range(1, 5):
        raise ValueError("Invalid session number. Must be an integer between 1 and 4.")
    if admin_mode not in ["true", "false"]:
        raise ValueError("Invalid admin_mode. Must be 'true' or 'false'.")
    if not isinstance(dest_port, int) or dest_port < 0:
        raise ValueError("Invalid dest_port. Must be a non-negative integer.")
    if not isinstance(src_ports, list) or not all(
        isinstance(port, dict) and
        port.get("intfType") in range(0, 9) and
        isinstance(port.get("intfNum"), int) and
        port.get("direction") in range(1, 5)
        for port in src_ports
    ):
        raise ValueError("Invalid src_ports. Must be a list of valid port dictionaries.")

    # Prepare Authorization header with Bearer token
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # Prepare endpoint and request data
    endpoint = f"/sw_portmirroring?sessionNum={session_num}"  # Query parameter included in the URL
    data = {
        "devicePortMirroring": {  # Corrected field name
            "sessionNum": session_num,  # Integer as observed
            "sessionMode": admin_mode,  # String as observed
            "destPort": dest_port,      # Integer as observed
            "srcPort": src_ports        # List of objects as observed
        }
    }

    # Use make_api_request
    try:
        response = make_api_request(
            switch_ip=switch_ip,
            endpoint=endpoint,
            method="POST",
            headers=headers,
            data=data
        )
    except Exception as e:
        logger.error(f"Failed to set port mirroring: {e}")
        raise InvalidResponse("Failed to communicate with the switch API.")

    # Validate and process response
    if not isinstance(response, dict) or "resp" not in response:
        raise InvalidResponse("Invalid API response format.")

    resp = response["resp"]
    if resp.get("status") != "success":
        logger.error(f"API error: {resp.get('respMsg')}")
        raise InvalidResponse(f"API error: {resp.get('respMsg')}")

    return resp