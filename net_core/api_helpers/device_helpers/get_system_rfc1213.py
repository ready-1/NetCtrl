"""
Helper functions for retrieving system RFC1213 information.

This module provides functions to interact with the /system_rfc1213 endpoint
of the network switch API. Each function adheres to a consistent format with detailed
error handling and response validation.

Author: Bob King (Ready-1 LLC)
Date: 2025-01-01
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app")

def get_system_rfc1213(switch_ip: str, token: str):
    """
    Retrieve system RFC1213 information, including device name, description, location, and contact.

    Purpose:
        Interacts with the /system_rfc1213 GET endpoint to fetch system information
        compliant with RFC1213 standards.

    Parameters:
        switch_ip (str): IP address of the target switch.
        token (str): Bearer token for API authentication.

    Returns:
        dict: Parsed JSON response containing system RFC1213 information.

    Raises:
        ValueError: If the switch_ip or token is invalid.
        InvalidResponse: If the API response is malformed or respCode is not 0.

    Example Usage:
        >>> from net_core.api_helpers.device_helpers.get_system_rfc1213 import get_system_rfc1213
        >>> response = get_system_rfc1213("192.168.1.1", "Bearer abc123")
        >>> print(response)

    Example Response:
        {
            "sysDescr": "M4300-24X ProSAFE 20-port 10GBASE-T and 4-port 10G combo, 20.36.53.1, B1.0.0.15",
            "sysName": "M4324X",
            "sysLocation": "San Jose",
            "sysContact": ""
        }

    JSON Response Structure:
        - resp (dict):
            - respCode (int): 0 if the request was successful, otherwise error code.
            - respMsg (str): Descriptive message of the response.
        - system_rfc1213 (dict):
            - sysDescr (str): Description of the system.
            - sysName (str): Name of the system.
            - sysLocation (str): Physical location of the system.
            - sysContact (str): System administrator contact information.
    """
    endpoint = "/system_rfc1213"
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = make_api_request(
            switch_ip=switch_ip,
            endpoint=endpoint,
            method="GET",
            headers=headers
        )

        if "resp" not in response or "system_rfc1213" not in response:
            logger.error("Malformed response: Missing expected fields.")
            raise InvalidResponse("Malformed API response.")

        if response["resp"].get("respCode") != 0:
            logger.error(f"API error: {response['resp'].get('respMsg')}")
            raise InvalidResponse(f"API Error: {response['resp'].get('respMsg')}")

        return response["system_rfc1213"]

    except Exception as e:
        logger.exception("Failed to fetch system RFC1213 information.")
        raise