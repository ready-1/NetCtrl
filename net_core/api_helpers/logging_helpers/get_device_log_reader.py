"""
Helper function for retrieving logs from the device.

This module provides a function to interact with the `/device_log_reader` endpoint
of the network switch API to fetch logs. It handles input validation, API requests,
and response processing for logs.

Author: Bob King (Ready-1 LLC) 
Date: 2025-01-02
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app")

# Constants specific to this module
API_ENDPOINT = "/device_log_reader"
TIMEOUT = 10  # Default timeout for API requests

def get_device_log_reader(switch_ip: str, token: str, num_logs: int = 10):
    """
    Retrieve logs from the device.

    Purpose:
        Fetches logs from the switch using the `/device_log_reader` API endpoint.

    Parameters:
        switch_ip (str): The IP address of the target switch.
        token (str): Bearer token for authentication.
        num_logs (int): The number of logs to retrieve (default: 10).

    Returns:
        dict: Parsed JSON response containing logs.

    Raises:
        ValueError: If `num_logs` is not a positive integer.
        InvalidResponse: If the API response is invalid or contains errors.
        Exception: For unexpected errors during the API call.

    Example Usage:
        ```python
        logs = get_device_log_reader("192.168.1.1", "token123", num_logs=5)
        print(logs)
        ```

    Example Response:
        ```json
        {
            "resp": {
                "status": "success",
                "respCode": 0,
                "respMsg": "Operation success"
            },
            "log_reader": {
                "logs": [
                    "<9> Jan  2 22:38:34 Lab Switch-1 OpEN[tRpcsrv.01000]: openapi_logging.c(1294) 2406 %% RestAgent: Failed to get basic key from HTTP_AUTHORIZATION header",
                    "<9> Jan  2 22:38:31 Lab Switch-1 OpEN[tRpcsrv.01000]: openapi_logging.c(1294) 2402 %% RestAgent: ",
                    ...
                ]
            }
        }
        ```

    JSON Response Structure:
        - `resp` (object): Response metadata.
            - `status` (string): Status of the operation (`success`, `failure`).
            - `respCode` (int): Response code (e.g., `0` for success).
            - `respMsg` (string): Detailed response message.
        - `log_reader` (object): Log data.
            - `logs` (list of strings): List of log entries.
    """
    if not isinstance(num_logs, int) or num_logs <= 0:
        raise ValueError("`num_logs` must be a positive integer.")

    params = {"num_logs": num_logs}
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = make_api_request(
            switch_ip=switch_ip,
            endpoint=API_ENDPOINT,
            method="GET",
            headers=headers,
            params=params,
            timeout=TIMEOUT,
        )
        if not isinstance(response, dict) or "resp" not in response or "log_reader" not in response:
            raise InvalidResponse("Unexpected response format.")

        resp = response.get("resp", {})
        if resp.get("status") != "success" or resp.get("respCode") != 0:
            raise InvalidResponse(f"API Error: {resp.get('respMsg', 'Unknown error')}")

        return response["log_reader"]

    except Exception as e:
        logger.error(f"Failed to retrieve logs: {e}")
        raise