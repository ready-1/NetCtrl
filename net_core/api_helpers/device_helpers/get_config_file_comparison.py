"""
Helper function for fetching configuration file comparison results.

This module provides functionality to interact with the `/config_file_compare`
endpoint of the network switch API.

Author: Bob King (Ready-1 LLC)
Date: 2024-12-31
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app")

def get_config_file_comparison(switch_ip: str, token: str, directive: str):
    """
    Fetches the configuration file comparison for a given directive.

    Purpose:
        This function retrieves differences between configurations based on the directive
        provided (`rtos` or `stob`), using the `/config_file_compare` API endpoint.

    Parameters:
        switch_ip (str): The IP address of the target switch.
        token (str): Bearer token for authentication.
        directive (str): Comparison type. Valid values are:
            - 'rtos': Compare "running-config" and "startup-config".
            - 'stob': Compare "startup-config" and "backup-config".

    Returns:
        dict: A dictionary containing configuration differences with the following structure:
              {
                  "respCode": int,
                  "respMsg": str,
                  "diff": list[str]
              }

    Raises:
        ValueError: If `directive` is not one of the allowed values.
        InvalidResponse: If the API response is missing required fields or indicates an error.
        Exception: For unexpected errors during the API call.

    Example Usage:
        result = get_config_file_comparison("192.168.1.1", "token123", "rtos")
        print(result)

    Example Response:
        {
            "respCode": 0,
            "respMsg": "Success",
            "diff": [
                "*** /mnt/fastpath/startup-config\tWed Aug 19 06:01:45 2020",
                "--- /mnt/fastpath/backup-config\tTue Aug 11 06:20:31 2020",
                "***************",
                "*** 2,10 ****",
                "! System Description: GC752XP Insight Managed Switch",
                "! System Software Version: 20.28.42.2",
                "! q"
            ]
        }

    JSON Response Structure:
        - `resp` (object):
            - `respCode` (integer): Response code from the API.
                - `0`: Success.
                - Other values indicate an error.
            - `respMsg` (string): Response message.
        - `config_file_compare` (object):
            - `diff` (list[string]): Differences between the compared configurations.
    """
    # Validate directive
    valid_directives = {"rtos", "stob"}
    if directive not in valid_directives:
        raise ValueError(f"Invalid directive '{directive}'. Must be one of {valid_directives}.")

    endpoint = "/config_file_compare"
    params = {"directive": directive}
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = make_api_request(
            switch_ip=switch_ip,
            endpoint=endpoint,
            method="GET",
            headers=headers,
            params=params,
        )

        # Validate response structure
        if not response.get("resp") or not response.get("config_file_compare"):
            raise InvalidResponse(f"Unexpected response format: {response}")

        resp_code = response["resp"].get("respCode", -1)
        if resp_code != 0:
            error_message = response["resp"].get("respMsg", "Unknown error")
            logger.error(f"API error: {error_message} (respCode: {resp_code})")
            raise InvalidResponse(error_message)

        # Return the processed data
        return {
            "respCode": resp_code,
            "respMsg": response["resp"]["respMsg"],
            "diff": response["config_file_compare"].get("diff", []),
        }

    except Exception as e:
        logger.exception(f"Failed to fetch configuration file comparison: {str(e)}")
        raise