import re
import requests
import logging
from django.conf import settings

from net_core.api_helpers.token_manager import TokenManager

logger = logging.getLogger('app')

class InvalidResponse(Exception):
    """Custom exception for invalid API responses."""
    pass

# TODO: document this function
def validate_ip_address(ip):
    """
    Validate that a given IP address is in a valid format.

    Args:
        ip: The IP address to validate.

    Returns:
        The validated IP address.

    Raises:
        ValueError: If the IP address is invalid.
    """
    try:
        octets = ip.split('.')
        if len(octets) != 4:
            raise ValueError("Invalid IP address format")
        for octet in octets:
            if not 0 <= int(octet) <= 255:
                raise ValueError("Invalid IP address format")
    except (ValueError, TypeError):
        raise ValueError("Invalid IP address format")
    return ip

# TODO: document this function
def format_mac_address(mac):
    # Normalize MAC address to standard format (e.g., 00:11:22:33:44:55)
    """
    Normalize a MAC address to standard format (e.g., 00:11:22:33:44:55).

    Args:
        mac (str): The MAC address to normalize.

    Returns:
        str: The normalized MAC address.

    Raises:
        ValueError: If the MAC address is invalid.
    """
    return mac.lower().replace('-', ':')


def make_api_request(switch_ip, endpoint, method="GET", data=None, params=None,  headers=None, timeout=10):
    """
    Makes an HTTP API request to a switch with robust error handling and token management.

    Parameters:
        switch_ip (str): The IP address of the target switch.
        endpoint (str): The API endpoint to call (e.g., 'login').
        method (str): HTTP method to use (default: 'GET').
        data (dict, optional): JSON payload to send with the request (default: None).
        params (dict, optional): Query parameters to include in the URL (default: None).
        headers (dict, optional): Custom headers to include in the request (default: None).
        timeout (int): Timeout for the request in seconds (default: 10).

    Returns:
        dict: Parsed JSON response from the API.

    Raises:
        requests.HTTPError: If an HTTP error occurs during the request.
        Exception: For unexpected issues during the API call.
    """
    protocol = "https" if settings.USE_HTTPS else "http"
    port = "8443" if settings.USE_HTTPS else "80"
    url = f"{protocol}://{switch_ip}:{port}/api/v1/{endpoint}"

    # Get a valid token using TokenManager
    token = TokenManager.get_token(switch_ip, settings.SWITCH_USERNAME, settings.SWITCH_PASSWORD)
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    try:
        # Make the API request
        logger.debug(f"Making API call: {method} {url}")
        response = requests.request(
            method=method.upper(),
            url=url,
            headers=headers,
            json=data,
            params=params,
            timeout=timeout,
            verify=False  # Disable SSL for now
        )
        response.raise_for_status()

        # Parse and return the JSON response
        return response.json()
    except requests.HTTPError as http_err:
        if response.status_code == 401:  # Unauthorized
            logger.warning(f"Token expired for switch {switch_ip}. Fetching a new token...")
            TokenManager._fetch_token(switch_ip, settings.SWITCH_USERNAME, settings.SWITCH_PASSWORD)
            return make_api_request(switch_ip, endpoint, method, data, params, timeout)
        logger.error(f"HTTP error occurred: {http_err}")
        raise
    except Exception as e:
        logger.error(f"API call failed: {e}")
        raise

