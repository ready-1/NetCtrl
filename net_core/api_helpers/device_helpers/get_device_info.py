"""
Helper functions for device information retrieval.

This module provides functions to interact with the `/device_info` endpoint
of the network switch API. Each function adheres to a consistent format with
detailed error handling and response validation.

Author: Bob King (Ready-1 LLC)
Date: 2024-12-28
"""

import logging
from django.conf import settings
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app")

# Constants specific to this module
API_ENDPOINT = "/device_info"
TIMEOUT = 10  # Default timeout for API requests


def get_device_info(switch_ip: str, token: str) -> dict:
    """
    Retrieve detailed information about the network device via the `/device_info` endpoint.

    Purpose:
        Fetch comprehensive details about the network switch, including its hardware, software,
        and operational state.

    Inputs:
        - switch_ip (str): IP address of the target switch.
        - token (str): Bearer token for API authentication.

    Returns:
        - dict: A dictionary containing processed device information.

    Raises:
        - ValueError: If input parameters are invalid.
        - InvalidResponse: If the API response is not as expected.
        - Exception: For any network or unexpected errors.

    Example Usage:
        >>> device_info = get_device_info("Bearer abc123")
        >>> print(device_info)

    Example Response:
        {
            "resp": {
                "respCode": 0,
                "respMsg": "Success"
            },
            "device_info": {
                "name": "NG-Switch",
                "serialNumber": "N1MN648000T",
                "macAddr": "10:DA:43:D7:72:F9",
                ...
            }
        }

    JSON Response Structure:
        - resp (object):
            - respCode (int): Status code where `0` indicates success.
            - respMsg (str): Status message.
        - device_info (object):
            - name (str): Switch display name.
            - serialNumber (str): Switch serial number.
            - macAddr (str): Switch MAC address.
            - model (str): Switch model number.
            - lanIpAddress (str): LAN IP address.
            - swVer (str): Firmware version.
            - lastReboot (str): Time of last reboot.
            - numOfPorts (int): Total ports.
            - numOfActivePorts (int): Active ports.
            - rstpState (bool): RSTP status.
            - memoryUsed (str): RAM used.
            - memoryUsage (str): Memory usage percentage.
            - cpuUsage (str): CPU usage percentage.
            - fanState (str): Fan status.
            - poeState (bool): PoE status.
            - upTime (str): Uptime.
            - temperatureSensors (list): Sensor details.
                - sensorNum (int): Sensor ID.
                - sensorDesc (str): Sensor description.
                - sensorTemp (str): Sensor temperature.
                - sensorState (str): Sensor state:
                    * `0` = NONE
                    * `1` = NORMAL
                    * `2` = WARNING
                    * `3` = CRITICAL
                    * `4` = SHUTDOWN
                    * `5` = NOT PRESENT
                    * `6` = NOT OPERATIONAL.
            - bootVersion (str): Boot version.
            - rxData (int): Bytes received.
            - txData (int): Bytes transmitted.
            - adminPoePower (int): Admin PoE power.

    """
    if not token:
        raise ValueError("Token is required for authentication.")

    headers = {
        "Authorization": token,
    }

    endpoint = f"https://{switch_ip}/api/v1{API_ENDPOINT}"
    logger.debug(f"Making API call: GET {endpoint}")

    try:
        response = make_api_request(
            switch_ip=switch_ip,
            method="GET",
            endpoint=API_ENDPOINT,
            headers=headers,
            timeout=TIMEOUT,
        )

        if "resp" not in response or "deviceInfo" not in response:
            logger.error("Malformed response from the API.")
            raise InvalidResponse("Missing `resp` or `deviceInfo` in the response.")

        if response["resp"].get("respCode") != 0:
            logger.error(
                f"API call failed with message: {response['resp'].get('respMsg')}"
            )
            raise InvalidResponse(f"API call failed: {response['resp'].get('respMsg')}")

        return response["deviceInfo"]

    except Exception as e:
        logger.exception("Failed to fetch device information.")
        raise e
    

    {'deviceInfo': {'serialNumber': '53L69C5FF001D', 'macAddr': 'BC:A5:11:A0:7E:1D', 'model': 'M4300-52G-PoE+', 'swVer': '12.0.19.6', 'numOfPorts': 52, 'numOfActivePorts': 1, 'memoryUsage': '90.96%', 'cpuUsage': '16.67%', 'fanState': [{'FAN-1': 'Operational', 'FAN-2': 'Operational', 'FAN-3': 'Operational', 'FAN-4': 'Operational'}], 'poeState': True, 'upTime': '01 Days 04 Hrs 04 Mins 22 Secs', 'temperatureSensors': [{'sensorNum': 1, 'sensorDesc': 'MAC-A', 'sensorTemp': 28, 'sensorState': 1}, {'sensorNum': 2, 'sensorDesc': 'MAC-B', 'sensorTemp': 36, 'sensorState': 1}, {'sensorNum': 3, 'sensorDesc': 'System', 'sensorTemp': 36, 'sensorState': 1}], 'bootVersion': 'B1.0.0.17', 'rxData': 280824399, 'txData': 99128805}, 'resp': {'status': 'success', 'respCode': 0, 'respMsg': 'Operation success'}}