"""
Helper functions for the diagnostics-related traceroute status endpoint.

This module provides functions to interact with the `/traceroute_status` endpoint
of the network switch API. Each function adheres to a consistent format with detailed
error handling and response validation.

Author: Bob King (Ready-1 LLC) 
Date: [Today's date]
"""

import logging
import time
from net_core.api_helpers.utils import make_api_request, InvalidResponse
import re

# Configure logger for the module
logger = logging.getLogger("app")


def parse_traceroute_message(traceroute_msg: str) -> dict:
    """
    Parse the traceroute message to extract the target host and detailed hop information.

    Parameters:
        traceroute_msg (str): The raw traceroute message from the API response.

    Returns:
        dict: Parsed data including the target host and a list of hops.
    """
    target_pattern = re.compile(r"traceroute to ([\w\.\-]+) \(([\d\.]+)\)")
    hop_pattern = re.compile(
        r"(\d+)\s+[\w\.\-]+\s+\(([\d\.]+)\)\s+([\d\.]+)\s+ms\s+([\d\.]+)\s+ms\s+([\d\.]+)\s+ms"
    )

    target_match = target_pattern.search(traceroute_msg)
    target = None
    if target_match:
        target = {"host": target_match.group(1), "ip": target_match.group(2)}

    hops = []
    for hop_match in hop_pattern.finditer(traceroute_msg):
        hop_number = int(hop_match.group(1))
        ip_address = hop_match.group(2)
        latencies = [float(hop_match.group(3)), float(hop_match.group(4)), float(hop_match.group(5))]
        hops.append({"hop": hop_number, "ip": ip_address, "latency": latencies})

    return {"target": target, "hops": hops}


def get_traceroute_status(switch_ip: str, token: str, timeout: int = 60) -> dict:
    """
    Retrieve the status of a traceroute operation, waiting for it to complete.

    Purpose:
        Queries the `/traceroute_status` endpoint of the NetCtrl API to retrieve
        the current status, message, target host, and parsed hop details of the traceroute operation.

    Parameters:
        switch_ip (str): The IP address of the target switch.
        token (str): Authorization token for the API.
        timeout (int): Maximum time to wait for the traceroute to complete, in seconds.

    Returns:
        dict: Processed data containing traceroute status, target host, and parsed hop details.

    Raises:
        ValueError: If the `switch_ip` or `token` is invalid or empty.
        InvalidResponse: If the response format does not match the expected schema.
        TimeoutError: If the traceroute operation does not complete within the timeout period.
    """
    if not switch_ip or not isinstance(switch_ip, str):
        raise ValueError("Invalid or missing `switch_ip` parameter.")
    if not token or not isinstance(token, str):
        raise ValueError("Invalid or missing `token` parameter.")

    endpoint = "/traceroute_status"
    headers = {"Authorization": f"Bearer {token}"}

    start_time = time.time()
    while True:
        try:
            response = make_api_request(
                switch_ip=switch_ip,
                endpoint=endpoint,
                method="GET",
                headers=headers
            )

            # Validate response structure
            resp = response.get("resp", {})
            if resp.get("status") != "success" or resp.get("respCode") != 0:
                raise InvalidResponse(f"API returned error: {resp.get('respMsg')}")

            traceroute_info = response.get("tracerouteInfo", {})
            state = traceroute_info.get("state")
            traceroute_msg = traceroute_info.get("tracerouteMsg", "")

            if state not in [0, 1, 2]:
                raise InvalidResponse("Unexpected state value in tracerouteInfo.")

            state_map = {
                0: "PT_SUCCESS",
                1: "PT_IN_PROGRESS",
                2: "PT_FAILURE"
            }

            parsed_data = parse_traceroute_message(traceroute_msg)

            # If target is missing, the traceroute is still in progress
            if parsed_data["target"] is None and state_map[state] == "PT_IN_PROGRESS":
                if time.time() - start_time >= timeout:
                    raise TimeoutError("Traceroute did not complete within the timeout period.")
                time.sleep(1)
                continue  # Retry until timeout

            return {
                "state": state_map[state],
                "tracerouteMsg": traceroute_msg,
                **parsed_data  # Includes "target" and "hops"
            }

        except Exception as e:
            logger.error(f"Error while fetching traceroute status: {str(e)}")
            raise