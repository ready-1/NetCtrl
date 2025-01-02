"""
Helper function for the 3.2 GET /ping_test_status endpoint.

This module provides the functionality to query the ping test status
from the network switch using the REST API. It parses the pingMsg field
into a structured dictionary upon a successful ping test.

Author: Bob King (Ready-1 LLC)
Date: 2025-01-01
"""

import logging
import time
import re
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app")

# Constants
TIMEOUT = 10  # Default timeout for API requests
ENDPOINT = "/ping_test_status"
MAX_RETRIES = 10  # Number of retries before timing out
RETRY_INTERVAL = 1  # Time in seconds between retries

def parse_ping_message(ping_msg: str) -> dict:
    """
    Parses the pingMsg field into a structured dictionary.

    Parameters:
        ping_msg (str): The raw ping message from the API response.

    Returns:
        dict: A structured dictionary containing parsed ping statistics.
    """
    try:
        # Extract relevant ping data using regex
        transmitted = int(re.search(r"(\d+) packets transmitted", ping_msg).group(1))
        received = int(re.search(r"(\d+) packets received", ping_msg).group(1))
        packet_loss = int(re.search(r"(\d+)% packet loss", ping_msg).group(1))
        rtt_values = re.search(r"round-trip min/avg/max = ([\d.]+)/([\d.]+)/([\d.]+) ms", ping_msg)

        return {
            "transmitted": transmitted,
            "received": received,
            "packet_loss": packet_loss,
            "rtt_min": float(rtt_values.group(1)),
            "rtt_avg": float(rtt_values.group(2)),
            "rtt_max": float(rtt_values.group(3)),
        }
    except (AttributeError, ValueError) as e:
        logger.error(f"Error parsing pingMsg: {e}")
        raise InvalidResponse("Failed to parse pingMsg.")

def get_ping_test_status(switch_ip: str, token: str) -> dict:
    """
    Fetches and parses the status of the ongoing ping test from the switch.

    Parameters:
        switch_ip (str): The IP address of the target switch.
        token (str): The bearer token for authentication.

    Returns:
        dict: A structured dictionary containing the ping test status and API metadata.

        - `ping_status` (dict): Contains parsed statistics from the ping test.
            - `transmitted` (int): Number of packets transmitted.
            - `received` (int): Number of packets received.
            - `packet_loss` (int): Percentage of packet loss.
            - `rtt_min` (float): Minimum round-trip time in milliseconds.
            - `rtt_avg` (float): Average round-trip time in milliseconds.
            - `rtt_max` (float): Maximum round-trip time in milliseconds.
        - `response` (dict): Metadata about the API response.
            - `status` (str): `success` or `failure`.
            - `respCode` (int): Status code (e.g., `0` for success).
            - `respMsg` (str): Description of the response.

    Raises:
        ValueError: If the input parameters are invalid.
        InvalidResponse: If the API response is not as expected.
        TimeoutError: If the maximum retries are reached without a valid response.

    Example Usage:
        ```
        result = get_ping_test_status("192.168.1.1", "Bearer <token>")
        print(result)
        ```

    Example Return:
        {
            "ping_status": {
                "transmitted": 1,
                "received": 1,
                "packet_loss": 0,
                "rtt_min": 0.539,
                "rtt_avg": 0.539,
                "rtt_max": 0.539
            },
            "response": {
                "status": "success",
                "respCode": 0,
                "respMsg": "Operation success"
            }
        }
    """
    if not switch_ip or not isinstance(switch_ip, str):
        raise ValueError("Invalid switch_ip: Must be a non-empty string.")

    if not token or not isinstance(token, str):
        raise ValueError("Invalid token: Must be a non-empty string.")

    headers = {
        "Authorization": f"Bearer {token}"
    }

    retries = 0
    while retries < MAX_RETRIES:
        try:
            # Make the API request
            response = make_api_request(
                switch_ip=switch_ip,
                endpoint=ENDPOINT,
                method="GET",
                headers=headers,
                timeout=TIMEOUT
            )

            # Validate the response structure
            if "resp" not in response or "pingTestStatus" not in response:
                raise InvalidResponse("Missing required keys in response.")

            resp = response["resp"]
            if resp.get("respCode") != 0:
                raise InvalidResponse(f"API returned error: {resp.get('respMsg')}")

            # Check if the ping test is complete
            ping_status = response["pingTestStatus"]
            if ping_status.get("state") == 0:  # PT_SUCCESS
                logger.info("Ping test completed successfully.")
                # Parse and return the ping statistics
                parsed_data = parse_ping_message(ping_status.get("pingMsg", ""))
                return {"ping_status": parsed_data, "response": resp}
            elif ping_status.get("state") == 1:  # PT_IN_PROGRESS
                logger.debug("Ping test in progress, retrying...")
            elif ping_status.get("state") == 2:  # PT_FAILURE
                raise InvalidResponse("Ping test failed.")

        except InvalidResponse as e:
            logger.error(f"Invalid response for ping test status: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error while fetching ping test status: {e}")
            raise

        # Increment retries and wait before retrying
        retries += 1
        time.sleep(RETRY_INTERVAL)

    raise TimeoutError(f"Ping test did not complete within {MAX_RETRIES * RETRY_INTERVAL} seconds.")