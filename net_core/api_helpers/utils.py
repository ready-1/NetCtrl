import re
import requests
import logging
import json
from django.conf import settings
from pprint import pprint
from net_core.api_helpers.token_manager import TokenManager

logger = logging.getLogger('app.api_helpers')
logger.propagate = False

class InvalidResponse(Exception):
    """Custom exception for invalid API responses."""
    pass

def log_request_data(method, url, headers=None, data=None, params=None, timeout=10):
    logger.debug("\n\n")
    logger.debug(f"Making API call: {method} {url}")
    logger.debug(f"Headers: {json.dumps(headers, indent=4)}")
    logger.debug(f"Data: {json.dumps(data, indent=4)}")
    logger.debug(f"Params: {json.dumps(params, indent=4)}")
    logger.debug(f"Timeout: {timeout}")
    logger.debug("\n\n")

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

def format_mac_address(mac):
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

def make_api_request(switch_ip, endpoint, method="GET", headers=None, data=None, params=None, timeout=10, retries=3):
    """
    Makes an HTTP API request to a switch with robust error handling and token management.

    This function appends query parameters (`params`) to the URL, ensuring they are correctly included
    in the API request.

    Parameters:
        switch_ip (str): The IP address of the target switch.
        endpoint (str): The API endpoint to call (e.g., 'login').
        method (str): HTTP method to use (default: 'GET').
        headers (dict, optional): Custom headers to include in the request (default: None).
        data (dict, optional): JSON payload to send with the request (default: None).
        params (dict, optional): Query parameters to include in the URL (default: None).
        timeout (int): Timeout for the request in seconds (default: 10).
        retries (int): Number of retry attempts for recoverable errors (default: 3).

    Returns:
        dict: Parsed JSON response from the API if successful.

    Raises:
        requests.RequestException: If the request fails after all retry attempts.
        requests.HTTPError: If a non-recoverable HTTP error occurs.
        ValueError: If the response cannot be parsed as JSON.
        Exception: For unexpected errors during the API call.
    """
    # Determine protocol and port based on settings
    protocol = "https" if settings.USE_HTTPS else "http"
    port = "8443" if settings.USE_HTTPS else "80"
    url = f"{protocol}://{switch_ip}:{port}/api/v1/{endpoint.lstrip('/')}"

    # Append query parameters if provided
    if params:
        query_string = '&'.join(f"{key}={value}" for key, value in params.items())
        url = f"{url}?{query_string}"

    # Retrieve a valid token for authentication
    token = TokenManager.get_token(switch_ip, settings.SWITCH_USERNAME, settings.SWITCH_PASSWORD)
    headers = headers or {}
    headers.update({
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    })

    # Log the request details for debugging
    log_request_data(method, url, headers, data, params, timeout)

    # Attempt the request up to the specified number of retries
    for attempt in range(retries):
        try:
            logger.debug(f"Attempt {attempt + 1}: Making API call to {url} using {method} method")
            response = requests.request(
                method=method.upper(),
                url=url,
                headers=headers,
                json=data,
                timeout=timeout,
                verify=False  # Disable SSL verification (for development; not recommended in production)
            )
            response.raise_for_status()  # Raise HTTPError for 4xx or 5xx responses
            return response.json()
        except requests.Timeout:
            logger.warning(f"Timeout occurred on attempt {attempt + 1} for {url}. Retrying...")
        except requests.ConnectionError:
            logger.error(f"Connection error for {url}. Is the switch online?")
            break
        except requests.HTTPError as http_err:
            if response.status_code in {403, 401}:  # Token-related errors
                logger.warning(f"Token issue detected (status {response.status_code}). Clearing token and retrying...")
                TokenManager.clear_token(switch_ip)
                continue
            elif 500 <= response.status_code < 600:
                logger.warning(f"Server error ({response.status_code}) on attempt {attempt + 1}. Retrying...")
            else:
                logger.error(f"HTTP error occurred: {http_err}")
                raise
        except ValueError as json_err:
            logger.error(f"Failed to parse JSON response: {json_err}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error occurred: {e}")
            raise

    logger.error(f"Request failed after {retries} attempts for {url}")
    raise requests.RequestException(f"Failed to complete API call to {url} after {retries} attempts")