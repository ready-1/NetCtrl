"""
Helper function for starting or stopping a traceroute operation.

This module provides a function to initiate or stop a traceroute operation on the
network switch using the 3.3 POST /traceroute_start API endpoint. The function
adheres to the standardized style for maintainability, includes detailed
response validation, and provides error handling.

Author: Bob King (Ready-1 LLC)
Date: 2025-01-01
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app")

# Constants
API_VERSION = "v1"
TIMEOUT = 10  # Default timeout for API requests

def traceroute_start(
    switch_ip: str,
    token: str,
    action: int,
    host: str = "www.netgear.com",
    size: int = 38,
    ip_version: int = 4,
    init_ttl: int = 1,
    max_ttl: int = 30,
    port: int = 33434,
    n_queries: int = 3,
    wait: int = 3
):
    """
    Initiates or stops a traceroute operation on the network switch.

    Parameters:
        switch_ip (str): IP address of the target switch.
        token (str): Authentication token for the API.
        action (int): Traceroute action (1 = Start, 0 = Stop).
        host (str, optional): Target host or IP address for the traceroute (default: "www.netgear.com").
        size (int, optional): Size of probe packets in bytes (default: 38, range: 38-32768).
        ip_version (int, optional): IP address version (default: 4, values: 4 = IPv4, 6 = IPv6).
        init_ttl (int, optional): Initial Time To Live (default: 1, range: 1-255).
        max_ttl (int, optional): Maximum Time To Live (default: 30, range: 1-255).
        port (int, optional): UDP destination port for probe packets (default: 33434, range: 1-65535).
        n_queries (int, optional): Number of probes per hop (default: 3, range: 1-10).
        wait (int, optional): Time between probes in seconds (default: 3, range: 1-60).

    Returns:
        dict: Parsed JSON response containing traceroute status.

    Raises:
        ValueError: If inputs are invalid.
        InvalidResponse: If the API response is invalid or unexpected.
        Exception: For other unforeseen errors.

    Example Usage:
        >>> response = traceroute_start(
                switch_ip="192.168.1.1",
                token="eyJhbGci...",
                action=1,
                host="8.8.8.8",
                size=64,
                ip_version=4,
                init_ttl=1,
                max_ttl=30,
                port=33434,
                n_queries=3,
                wait=5
            )
        >>> print(response)
        {"resp": {"status": "success", "respCode": 0, "respMsg": "Traceroute started."}}

    Example Response:
        {
            "resp": {
                "status": "success",
                "respCode": 0,
                "respMsg": "Traceroute started."
            }
        }

    JSON Response Structure:
        - resp (object): Response metadata.
            - status (str): Status of the operation (`success` or `failure`).
            - respCode (int): Response code (`0` for success, other values indicate errors).
            - respMsg (str): Message detailing the response.
    """
    # Input validation
    if not isinstance(switch_ip, str) or not switch_ip:
        raise ValueError("Invalid switch_ip: must be a non-empty string.")
    if not isinstance(token, str) or not token:
        raise ValueError("Invalid token: must be a non-empty string.")
    if not isinstance(action, int) or action not in [0, 1]:
        raise ValueError("Invalid action: must be 0 (Stop) or 1 (Start).")
    if not isinstance(host, str) or not host:
        raise ValueError("Invalid host: must be a non-empty string.")
    if not isinstance(size, int) or not (38 <= size <= 32768):
        raise ValueError("Invalid size: must be an integer between 38 and 32768.")
    if not isinstance(ip_version, int) or ip_version not in [4, 6]:
        raise ValueError("Invalid ip_version: must be 4 (IPv4) or 6 (IPv6).")
    if not isinstance(init_ttl, int) or not (1 <= init_ttl <= 255):
        raise ValueError("Invalid init_ttl: must be an integer between 1 and 255.")
    if not isinstance(max_ttl, int) or not (1 <= max_ttl <= 255):
        raise ValueError("Invalid max_ttl: must be an integer between 1 and 255.")
    if not isinstance(port, int) or not (1 <= port <= 65535):
        raise ValueError("Invalid port: must be an integer between 1 and 65535.")
    if not isinstance(n_queries, int) or not (1 <= n_queries <= 10):
        raise ValueError("Invalid n_queries: must be an integer between 1 and 10.")
    if not isinstance(wait, int) or not (1 <= wait <= 60):
        raise ValueError("Invalid wait: must be an integer between 1 and 60.")

    endpoint = f"/{API_VERSION}/traceroute_start"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "tracerouteStart": {
            "action": action,
            "host": host,
            "size": size,
            "ipVersion": ip_version,
            "initTTL": init_ttl,
            "maxTTL": max_ttl,
            "port": port,
            "nQueries": n_queries,
            "wait": wait,
        }
    }

    try:
        # Make the API request
        response = make_api_request(
            switch_ip=switch_ip,
            endpoint=endpoint,
            method="POST",
            headers=headers,
            data=data,
            timeout=TIMEOUT
        )
        # Validate response
        if not isinstance(response, dict) or "resp" not in response:
            raise InvalidResponse("Unexpected response structure.")

        resp = response.get("resp", {})
        if resp.get("respCode") != 0:
            raise InvalidResponse(f"API error: {resp.get('respMsg', 'Unknown error')}")

        return response

    except Exception as e:
        logger.error(f"Failed to initiate traceroute: {e}")
        raise