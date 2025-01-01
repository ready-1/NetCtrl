"""
Helper function for the 3.5 GET /sw_portmirroring endpoint.

This module provides a function to retrieve port mirroring configuration
from a network switch using the REST API. The function ensures robust error
handling, response validation, and retry logic for seamless API interaction.

Author: Bob King (Ready-1 LLC)
Date: 2025-01-01
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app.device_helpers.get_port_mirroring")

# Constants specific to this module
TIMEOUT = 10
RETRIES = 3

def get_port_mirroring(switch_ip: str, token: str, session_num: int) -> dict:
    """
    Fetches the port mirroring configuration for a specified session from the switch.

    Purpose:
        Retrieve detailed configuration of port mirroring, including session number,
        destination port, source ports, and capture settings.

    Parameters:
        switch_ip (str): The IP address of the target switch.
        token (str): Bearer token for authentication.
        session_num (int): Port mirroring session number (1-4).

    Returns:
        dict: A dictionary containing the processed port mirroring configuration.
            {
                "session_number": int,
                "admin_mode": bool,
                "destination_port": int,
                "source_ports": [
                    {
                        "interface_type": str,
                        "interface_number": int,
                        "direction": str
                    }
                ]
            }

    Raises:
        ValueError: If the input parameters are invalid.
        InvalidResponse: If the API response is unexpected or indicates failure.
        requests.RequestException: If the API request fails after retries.

    Example Usage:
        >>> from net_core.api_helpers.device_helpers.get_port_mirroring import get_port_mirroring
        >>> config = get_port_mirroring("192.168.1.1", "your_token", 1)
        >>> print(config)

    Example Response:
        {
            "session_number": 1,
            "admin_mode": True,
            "destination_port": 5,
            "source_ports": [
                {
                    "interface_type": "Physical",
                    "interface_number": 10,
                    "direction": "Bidirectional"
                }
            ]
        }

    JSON Response Structure:
        {
            "resp": {
                "status": "success",
                "respCode": 0,
                "respMsg": "Operation successful"
            },
            "switchRstpPortConfig": {
                "sessionNum": 1,
                "sessionMode": true,
                "destPort": 5,
                "srcPort": [
                    {
                        "intfType": 0,
                        "intfNum": 10,
                        "direction": 1
                    }
                ]
            }
        }
        - resp: Top-level response object.
            - status (enum): "success" or "failure".
            - respCode (int): Response code (0 indicates success).
            - respMsg (str): Response message.
        - switchRstpPortConfig: Port mirroring configuration object.
            - sessionNum (int): Port mirroring session number (1-4).
            - sessionMode (bool): Port mirroring admin mode.
            - destPort (int): Destination port.
            - srcPort (list): List of source port configurations.
                - intfType (enum): Interface type (0-8; see `make_api_request` for mapping).
                - intfNum (int): Interface number.
                - direction (enum): Direction (1: Bidirectional, 2: Ingress, 3: Egress, 4: sFlow).
    """
    if not (1 <= session_num <= 4):
        raise ValueError("session_num must be between 1 and 4.")

    endpoint = f"/sw_portmirroring"
    params = {"sessionNum": session_num}
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = make_api_request(
            switch_ip=switch_ip,
            endpoint=endpoint,
            method="GET",
            headers=headers,
            params=params,
            timeout=TIMEOUT,
            retries=RETRIES,
        )

        # Validate top-level response
        resp = response.get("resp", {})
        if resp.get("status") != "success" or resp.get("respCode") != 0:
            raise InvalidResponse(f"API Error: {resp.get('respMsg', 'Unknown error')}")

        # Extract and process data
        config = response.get("switchRstpPortConfig", {})
        return {
            "session_number": config.get("sessionNum"),
            "admin_mode": config.get("sessionMode", False),
            "destination_port": config.get("destPort", 0),
            "source_ports": [
                {
                    "interface_type": ["Physical", "CPU", "LAG", "VLAN", "Loopback", "Tunnel", "Service Port", "Other", "Any"][port.get("intfType", 0)],
                    "interface_number": port.get("intfNum"),
                    "direction": ["Bidirectional", "Ingress", "Egress", "sFlow"][port.get("direction", 1) - 1],
                }
                for port in config.get("srcPort", [])
            ],
        }

    except Exception as e:
        logger.error(f"Failed to fetch port mirroring config: {e}")
        raise