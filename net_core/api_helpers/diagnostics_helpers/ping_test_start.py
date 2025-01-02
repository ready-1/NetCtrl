"""
Helper function for POST /ping_test_start.

This module provides the implementation for starting a ping test on the M4300 switch
using the /ping_test_start endpoint of the REST API. It adheres to the standard 
format and error-handling requirements.

Author: Bob King (Ready-1 LLC)
Date: 2025-01-01
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for this module
logger = logging.getLogger("app.diagnostics_helpers")

# Constants
API_ENDPOINT = "/ping_test_start"
TIMEOUT = 10

def ping_test_start(
    switch_ip: str,
    token: str,
    host: str,
    action: int = 1,
    ip_version: int = 4,
    count: int = 1,
    size: int = 64,
    timeout: int = 10,
    interval: float = 1.0,
) -> dict:
    """
    Initiates a ping test on the M4300 switch.

    Purpose:
        Sends a POST request to the /ping_test_start endpoint to initiate a ping test.

    Parameters:
        switch_ip (str): The IP address of the target switch.
        token (str): Authentication token for the API.
        host (str): The target hostname or IP address.
        action (int, optional): Action to perform (1=start, 0=stop). Default is 1.
        ip_version (int, optional): IP version (4=IPv4, 6=IPv6). Default is 4.
        count (int, optional): Number of echo requests to send (1-1024). Default is 1.
        size (int, optional): Size of ping packets in bytes (1-655535). Default is 64.
        timeout (int, optional): Timeout for each ping packet in seconds (1-300). Default is 10.
        interval (float, optional): Interval between packets in seconds (0.5-10). Default is 1.0.

    Returns:
        dict: A dictionary containing the response from the API.

    Raises:
        ValueError: If any input parameters are invalid.
        InvalidResponse: If the API response is not as expected or contains errors.

    Example Usage:
        >>> response = ping_test_start("192.168.1.1", "abc123token", "8.8.8.8", count=5)
        >>> print(response)

    Example Response:
        {
            "resp": {
                "status": "success",
                "respCode": 0,
                "respMsg": "Ping test started successfully"
            },
            "testId": "test123"
        }

    JSON Response Structure:
        - resp (object):
            - status (enum: "success", "failure"): Overall status of the API call.
            - respCode (integer): Response code from the switch.
            - respMsg (string): Detailed message about the result.
        - testId (string): Identifier for the initiated ping test.
    """
    if not switch_ip or not isinstance(switch_ip, str):
        raise ValueError("Invalid switch_ip: Must be a non-empty string.")
    if not token or not isinstance(token, str):
        raise ValueError("Invalid token: Must be a non-empty string.")
    if not host or not isinstance(host, str):
        raise ValueError("Invalid host: Must be a valid hostname or IP address.")
    if action not in (0, 1):
        raise ValueError("Invalid action: Must be 0 (stop) or 1 (start).")
    if ip_version not in (4, 6):
        raise ValueError("Invalid ip_version: Must be 4 (IPv4) or 6 (IPv6).")
    if count < 1 or count > 1024:
        raise ValueError("Invalid count: Must be between 1 and 1024.")
    if size < 1 or size > 655535:
        raise ValueError("Invalid size: Must be between 1 and 655535.")
    if timeout < 1 or timeout > 300:
        raise ValueError("Invalid timeout: Must be between 1 and 300.")
    if interval < 0.5 or interval > 10.0:
        raise ValueError("Invalid interval: Must be between 0.5 and 10.0 seconds.")

    data = {
        "pingTest": {
            "action": action,
            "ipVersion": ip_version,
            "host": host,
            "count": count,
            "size": size,
            "timeout": timeout,
            "interval": interval,
        }
    }
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = make_api_request(
            switch_ip=switch_ip,
            endpoint=API_ENDPOINT,
            method="POST",
            headers=headers,
            data=data,
            timeout=TIMEOUT,
        )
    except Exception as e:
        logger.error(f"API request failed: {e}")
        raise

    # Validate response structure
    if not isinstance(response, dict) or "resp" not in response:
        logger.error(f"Unexpected response format: {response}")
        raise InvalidResponse(f"Invalid API response format: {response}")

    resp = response.get("resp", {})
    if resp.get("status") != "success" or resp.get("respCode") != 0:
        logger.error(f"API error: {resp}")
        raise InvalidResponse(f"API error: {resp}")

    return response