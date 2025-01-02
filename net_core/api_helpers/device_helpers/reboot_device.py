"""
Helper function for rebooting a network device.

This module provides a function to interact with the `/device_reboot` endpoint
of the network switch API. The endpoint allows for scheduling a device reboot.

Author: Bob King (Ready-1 LLC)
Date: 2024-12-28
"""

import logging
from requests.exceptions import ConnectionError
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app")


def reboot_device(switch_ip: str, token: str, after_secs: int = 2) -> dict:
    """
    Reboots a network device via the `/device_reboot` endpoint using Bearer Authentication.

    Purpose:
        Sends a request to the device's API to reboot the device after a specified delay.

    Parameters:
        - switch_ip (str): IP address of the target switch.
        - token (str): Bearer token for authentication.
        - after_secs (int): Delay in seconds before reboot (default: 2).

    Returns:
        dict: A dictionary indicating success with `{"status": "success"}`.

    Raises:
        - ValueError: If `after_secs` is not within the range 0–10.
        - InvalidResponse: If the API response format is invalid or indicates an error.
        - requests.HTTPError: For HTTP request-related issues.

    Example Usage:
        >>> reboot_device("192.168.1.1", "token123", after_secs=5)

    Example Response:
        {
            "status": "success"
        }
    """
    if not (0 <= after_secs <= 10):
        raise ValueError("`after_secs` must be between 0 and 10 seconds.")

    endpoint = "device_reboot"  # Corrected endpoint
    data = {"deviceReboot": {"afterSecs": after_secs}}
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = make_api_request(
            switch_ip=switch_ip,
            endpoint=endpoint,
            method="POST",
            data=data,
            headers=headers
        )
        # Process the response
        resp = response.get("resp")
        if not resp or resp.get("respCode") != 0:
            raise InvalidResponse(f"Unexpected response: {response}")

        logger.info("Reboot initiated successfully on %s", switch_ip)
        return {"status": "success"}

    except ConnectionError as e:
        # Treat abrupt connection closures as a success state
        logger.warning(
            "Connection closed by device at %s. Assuming reboot initiated successfully.", switch_ip
        )
        return {"status": "success"}

    except Exception as e:
        logger.error("Failed to reboot device at %s: %s", switch_ip, str(e))
        raise