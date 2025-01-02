"""
Helper function for the `POST /system_rfc1213` endpoint.

This module provides functionality to set the device name, location, and contact
information using the `POST /system_rfc1213` API endpoint.

Author: Bob King (Ready-1 LLC)
Date: 2025-01-01
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app.device_helpers.set_system_rfc1213")

def set_system_rfc1213(switch_ip: str, token: str, system_name: str, location: str, contact: str) -> dict:
    """
    Sets the device name, location, and contact information.

    Summary:
        This function calls the `POST /system_rfc1213` endpoint to set the system's
        name, location, and contact information.

    Purpose:
        Allows updating critical system metadata.

    Inputs:
        - switch_ip (str): IP address of the target switch.
        - token (str): Authentication token for the API.
        - system_name (str): New system name (max length: 255 characters).
        - location (str): New location description (max length: 255 characters).
        - contact (str): New contact information (max length: 255 characters).

    Returns:
        dict: Contains the API response. Format:
            {
                "resp": {
                    "status": str,
                    "respCode": int,
                    "respMsg": str
                }
            }

    Raises:
        - ValueError: If inputs are invalid.
        - InvalidResponse: If the API response format is invalid or indicates an error.

    Example Usage:
        >>> set_system_rfc1213(
                "192.168.1.1",
                "abcd1234",
                "Switch-1",
                "Main Office",
                "admin@example.com"
            )
        {
            "resp": {
                "status": "success",
                "respCode": 0,
                "respMsg": "Operation successful"
            }
        }

    Example Response:
        {
            "resp": {
                "status": "success",
                "respCode": 0,
                "respMsg": "Operation successful"
            }
        }

    JSON Response Structure:
        - resp (object):
            - status (str): Status of the operation.
                * "success" = The operation was successful.
                * "failure" = The operation failed.
            - respCode (int): Response code (0 for success, other for failure).
            - respMsg (str): Detailed message about the operation.

    """

    # Validate inputs
    if not isinstance(switch_ip, str) or not switch_ip.strip():
        raise ValueError("Invalid switch IP address provided.")
    if not isinstance(token, str) or not token.strip():
        raise ValueError("Invalid token provided.")
    if not isinstance(system_name, str) or len(system_name) > 255:
        raise ValueError("System name must be a string with a maximum length of 255 characters.")
    if not isinstance(location, str) or len(location) > 255:
        raise ValueError("Location must be a string with a maximum length of 255 characters.")
    if not isinstance(contact, str) or len(contact) > 255:
        raise ValueError("Contact must be a string with a maximum length of 255 characters.")

    endpoint = "/system_rfc1213"
    payload = {
        "system_rfc1213": {
            "sysName": system_name,
            "sysLocation": location,
            "sysContact": contact
        }
    }
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = make_api_request(
            switch_ip=switch_ip,
            endpoint=endpoint,
            method="POST",
            headers=headers,
            data=payload,
        )
    except Exception as e:
        logger.error(f"API request failed for {endpoint}: {e}")
        raise

    # Validate API response
    if "resp" not in response or not isinstance(response["resp"], dict):
        logger.error(f"Invalid API response format for {endpoint}: {response}")
        raise InvalidResponse("Response format is invalid.")

    resp = response["resp"]
    if resp.get("respCode") != 0:
        logger.error(f"API error: {resp.get('respMsg')}")
        raise InvalidResponse(f"API error: {resp.get('respMsg')}")

    logger.info(f"POST {endpoint} successful for {switch_ip}.")
    return response