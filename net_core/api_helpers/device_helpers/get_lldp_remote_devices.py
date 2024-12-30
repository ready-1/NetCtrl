"""
Helper function for retrieving LLDP remote device information.

This module provides the helper function to interact with the
`GET /lldp_remote_devices` endpoint of the network switch API.

Author: Bob King (Ready-1 LLC)
Date: 2024-12-30
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app.device_helpers")

def get_lldp_remote_devices(switch_ip: str, token: str):
    """
    Retrieve LLDP remote device information from a switch.

    Purpose:
        Fetches the LLDP information for remote devices connected to the switch
        using the `GET /lldp_remote_devices` endpoint.

    Parameters:
        switch_ip (str): The IP address of the target switch.
        token (str): The authentication token for the API.

    Returns:
        list[dict]: A list of dictionaries containing LLDP remote device information.

    Raises:
        ValueError: If `switch_ip` or `token` is invalid.
        InvalidResponse: If the API response is invalid or unexpected.
        Exception: For unexpected errors.

    Example Usage:
        >>> devices = get_lldp_remote_devices("192.168.1.1", "example_token")
        >>> print(devices)

    Example Response:
        [
            {
                "id": 31,
                "ifIndex": 31,
                "remoteId": 5,
                "chassisId": "A0:40:A0:5B:41:AF",
                "chassisIdSubtype": 4,
                "remotePortId": "A0:40:A0:5B:41:AF",
                "remotePortIdSubtype": 3,
                "remotePortDesc": "lldp0",
                "remoteSysName": "BioTech-Wing",
                "remoteSysDesc": "Linux 3.14.77 ...",
                "sysCapabilitiesSupported": ["bridge, WLAN access point"],
                "sysCapabilitiesEnabled": ["bridge, WLAN access point"],
                "mgmtAddresses": [{"type": "IPv4", "address": "192.168.8.58"}],
                "remoteTTL": 18
            }
        ]

    JSON Response Structure:
        - lldp_remote_devices (list of objects):
            - id (integer): LLDP ID Number.
            - ifIndex (integer): Internal interface number.
            - remoteId (integer): Identifier for device on remote system.
            - chassisId (string): Remote device hardware platform.
            - chassisIdSubtype (integer): Chassis ID field subtype:
                * 1: Chassis component
                * 2: Interface alias
                * 3: Port component
                * 4: MAC address
                * 5: Network address
                * 6: Interface name
                * 7: Local
            - remotePortId (string): Device port that transmitted LLDP data.
            - remotePortIdSubtype (integer): Remote port field subtype (see above).
            - remotePortDesc (string): Remote system port description.
            - remoteSysName (string): Name assigned to the remote device.
            - remoteSysDesc (string): Description of the remote device.
            - sysCapabilitiesSupported (string): List of primary functions supported.
            - sysCapabilitiesEnabled (string): List of primary functions enabled.
            - mgmtAddresses (array of objects):
                - type (string): Type of address (e.g., "IPv4").
                - address (string): IP address.
            - remoteTTL (integer): Time To Live information for the remote device.
    """
    if not switch_ip or not isinstance(switch_ip, str):
        raise ValueError("Invalid switch IP address.")
    if not token or not isinstance(token, str):
        raise ValueError("Invalid token.")

    endpoint = "/lldp_remote_devices"
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = make_api_request(
            switch_ip=switch_ip,
            endpoint=endpoint,
            method="GET",
            headers=headers,
            timeout=10
        )

        # Validate response structure
        if "lldp_remote_devices" not in response:
            raise InvalidResponse("Missing `lldp_remote_devices` in API response.")

        return response["lldp_remote_devices"]

    except InvalidResponse as e:
        logger.error(f"Invalid API response: {e}")
        raise
    except Exception as e:
        logger.error(f"Error fetching LLDP remote devices: {e}")
        raise