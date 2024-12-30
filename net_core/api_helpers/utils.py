import re
import requests
import logging
from django.conf import settings

from pprint import pprint

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


def make_api_request(switch_ip, endpoint, method="GET", headers=None, data=None, params=None, timeout=10, retries=3):
    """
    Makes an HTTP API request to a switch with robust error handling and token management.

    This function handles various error conditions, including expired or invalid tokens (stale tokens),
    by leveraging the TokenManager to clear stale tokens and fetch new ones. If the API returns a 403
    (Forbidden) or 401 (Unauthorized) status, indicating the token is no longer valid, the function will
    clear the token, request a new one, and retry the API call automatically.

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

    Token Management:
        - When a 403 or 401 status code is returned, the function detects the stale token condition.
        - The `TokenManager.clear_token` method is called to invalidate the current token.
        - The function then retries the API call, obtaining a fresh token automatically.
        - This process ensures uninterrupted operation when tokens expire or are invalidated.
    """
    # Determine protocol and port based on settings
    protocol = "https" if settings.USE_HTTPS else "http"
    port = "8443" if settings.USE_HTTPS else "80"
    url = f"{protocol}://{switch_ip}:{port}/api/v1/{endpoint.lstrip('/')}"

    # Retrieve a valid token for authentication
    token = TokenManager.get_token(switch_ip, settings.SWITCH_USERNAME, settings.SWITCH_PASSWORD)
    headers = {
        "Authorization": f"Bearer {token}",  # Include the token in the Authorization header
        "Accept": "application/json"  # Indicate that we expect a JSON response
    }

    # Attempt the request up to the specified number of retries
    for attempt in range(retries):
        try:
            # Log the attempt and make the API request
            logger.debug(f"Attempt {attempt + 1}: Making API call to {url} using {method}")
            response = requests.request(
                method=method.upper(),  # Convert HTTP method to uppercase (e.g., 'GET', 'POST')
                url=url,  # Complete API endpoint URL
                headers=headers,  # Authorization and other headers
                json=data,  # JSON payload for the request body
                params=params,  # Query parameters
                timeout=timeout,  # Request timeout in seconds
                verify=False  # Disable SSL verification (for development; not recommended in production)
            )
            response.raise_for_status()  # Raise HTTPError for 4xx or 5xx responses

            # Return the parsed JSON response if the request is successful
            return response.json()

        except requests.Timeout:
            # Handle timeout errors, log, and retry
            logger.warning(f"Timeout occurred on attempt {attempt + 1} for {url}. Retrying...")
        except requests.ConnectionError:
            # Handle connection errors (e.g., switch offline), log, and exit retry loop
            logger.error(f"Connection error for {url}. Is the switch online?")
            break
        except requests.HTTPError as http_err:
            # Handle HTTP errors based on status code
            if response.status_code in {403, 401}:  # Token-related errors
                logger.warning(f"Token issue detected (status {response.status_code}). Clearing token and retrying...")
                TokenManager.clear_token(switch_ip)  # Clear the stale token
                continue  # Retry the request with a fresh token
            elif 500 <= response.status_code < 600:  # Server-side errors
                logger.warning(f"Server error ({response.status_code}) on attempt {attempt + 1}. Retrying...")
            else:
                # Non-recoverable HTTP error; log and re-raise the exception
                logger.error(f"HTTP error occurred: {http_err}")
                raise
        except ValueError as json_err:
            # Handle JSON parsing errors (unexpected response format)
            logger.error(f"Failed to parse JSON response: {json_err}")
            raise
        except Exception as e:
            # Handle any other unexpected errors
            logger.error(f"Unexpected error occurred: {e}")
            raise

    # If all retries fail, log and raise a final exception
    logger.error(f"Request failed after {retries} attempts for {url}")
    raise requests.RequestException(f"Failed to complete API call to {url} after {retries} attempts")

