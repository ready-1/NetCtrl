"""
Helper functions for configuration copy within switches.

This module provides functionality to copy configurations (e.g., running-config
to startup-config) using the `/config_copy` endpoint of the network switch API.

Author: Bob King (Ready-1 LLC)
Date: 2024-12-28
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app")

# Constants
TIMEOUT = 10  # Default timeout for API requests


def config_copy(switch_ip: str, token: str, directive: str) -> dict:
    """
    Copy configuration within the switch.

    Purpose:
        Copies configurations such as running-config to startup-config or other
        allowed directives using the `/config_copy` API endpoint.

    Parameters:
        switch_ip (str): The IP address of the target switch.
        token (str): Authentication token for API access.
        directive (str): Directive specifying the copy action.
                        Options:
                          - `rtos`: Running-config to startup-config
                          - `stob`: Startup-config to backup-config
                          - `btos`: Backup-config to startup-config
                          - `rtof`: Running-config to factory-default

    Returns:
        dict: Response data from the API with keys:
              - `resp`: General response details.
              - `respCode`: Status code (0 indicates success).
              - `respMsg`: Detailed message.

    Raises:
        ValueError: If the `directive` is not one of the allowed values.
        InvalidResponse: If the API response is malformed or indicates an error.

    Example Usage:
        ```python
        response = config_copy(
            switch_ip="192.168.1.1",
            token="eyJhbGc...",
            directive="rtos"
        )
        print(response)
        ```

    Example Response:
        ```json
        {
            "resp": {
                "respCode": 0,
                "respMsg": "Configuration copied successfully."
            }
        }
        ```

    JSON Response Structure:
        - `resp` (object): Contains response details.
            - `respCode` (int): Status code.
                * `0`: Success.
                * Non-zero values indicate specific errors.
            - `respMsg` (str): Human-readable message.

    """
    # Validate input
    valid_directives = ["rtos", "stob", "btos", "rtof"]
    if directive not in valid_directives:
        raise ValueError(
            f"Invalid directive '{directive}'. Allowed values: {valid_directives}"
        )

    # API endpoint and parameters
    endpoint = "/config_copy"
    params = {"directive": directive}
    headers = {"Authorization": f"Bearer {token}"}

    try:
        # Make the API request
        response = make_api_request(
            switch_ip=switch_ip,
            endpoint=endpoint,
            method="POST",
            params=params,
            headers=headers,
            timeout=TIMEOUT,
        )

        # Validate response structure
        if "resp" not in response or "respCode" not in response["resp"]:
            raise InvalidResponse("Malformed response from the API.")

        # Check for API-level errors
        if response["resp"]["respCode"] != 0:
            error_msg = response["resp"].get("respMsg", "Unknown error.")
            logger.error(f"API error: {error_msg}")
            raise InvalidResponse(f"API error: {error_msg}")

        return response

    except Exception as e:
        logger.exception("Error during config_copy operation.")
        raise