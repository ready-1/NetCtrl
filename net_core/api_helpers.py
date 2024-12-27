import logging
import requests
from datetime import datetime, timedelta
from django.conf import settings

# Get the logger defined in settings.py
logger = logging.getLogger('app')

# Define valid HTTP methods for validation
VALID_HTTP_METHODS = {"GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "HEAD"}


class TokenManager:
    """
    Manages API tokens for multiple switches, including fetching, refreshing,
    and validating tokens.
    """
    _tokens = {}  # Stores tokens and expiry times keyed by switch IP

    @classmethod
    def get_token(cls, switch_ip, username, password):
        """
        Returns a valid token for the specified switch.
        Fetches a new token if the current one is expired or unavailable.
        """
        if not cls._is_token_valid(switch_ip):
            cls._fetch_token(switch_ip, username, password)
        return cls._tokens[switch_ip]["token"]

    @classmethod
    def _is_token_valid(cls, switch_ip):
        """
        Checks if the token for a given switch is valid.
        """
        token_data = cls._tokens.get(switch_ip)
        if not token_data:
            return False
        return datetime.now() < token_data["expiry"]

    @classmethod
    def _fetch_token(cls, switch_ip, username, password):
        """
        Logs in to the switch and retrieves a new token.
        """
        login_url = f"https://{switch_ip}/login"  # Replace with actual login endpoint
        response = requests.post(
            login_url,
            json={"username": username, "password": password},
        )
        if response.status_code == 200:
            data = response.json()
            token = data["token"]
            expires_in = data["expires"]  # Time in seconds until token expires
            cls._tokens[switch_ip] = {
                "token": token,
                "expiry": datetime.now() + timedelta(seconds=expires_in),
            }
        else:
            raise Exception(f"Failed to login to {switch_ip}: {response.text}")

    @classmethod
    def logout(cls, switch_ip):
        """
        Logs out from the specified switch and invalidates its token.
        """
        if switch_ip in cls._tokens:
            token = cls._tokens[switch_ip]["token"]
            logout_url = f"https://{switch_ip}/logout"  # Replace with actual logout endpoint
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.post(logout_url, headers=headers)
            if response.status_code == 200:
                del cls._tokens[switch_ip]
            else:
                raise Exception(f"Failed to logout from {switch_ip}: {response.text}")

def make_api_request(url, method="GET", headers=None, data=None, params=None, timeout=10):
    """
    Makes an HTTP API request with robust error handling and detailed logging.
    
    Args:
        url (str): The target URL for the API request.
        method (str): The HTTP method to use for the request (e.g., "GET", "POST").
        headers (dict, optional): HTTP headers to include in the request.
        data (dict, optional): Payload to send in the body of the request (for POST/PUT methods).
        params (dict, optional): Query parameters to include in the request URL.
        timeout (int, optional): Timeout duration in seconds for the request (default: 10).

    Returns:
        dict: Parsed JSON response from the API.

    Raises:
        ValueError: If the URL or HTTP method is invalid, or if the response is not valid JSON.
        TimeoutError: If the request exceeds the specified timeout duration.
        Exception: For connection errors, generic API failures, or any other unforeseen errors.
    """

    # Validate the URL is non-empty and a proper string
    if not url or not isinstance(url, str) or url.strip() == "":
        logger.error("The URL provided is empty or invalid.")
        raise ValueError("The URL provided is empty or invalid.")
    
    # Validate the HTTP method against predefined valid methods
    if method.upper() not in VALID_HTTP_METHODS:
        logger.error(f"Invalid HTTP method: {method}")
        raise ValueError(f"Invalid HTTP method: {method}")

    try:
        # Log the request details for debugging purposes
        logger.debug(f"Starting API request: Method={method}, URL={url}")
        logger.debug(f"Headers: {headers}")
        logger.debug(f"Data: {data}")
        logger.debug(f"Params: {params}")
        
        # Perform the HTTP request
        response = requests.request(
            method=method.upper(),
            url=url,
            headers=headers,
            json=data,
            params=params,
            timeout=timeout
        )
        
        # Raise an HTTPError for responses with 4xx or 5xx status codes
        response.raise_for_status()

        # Attempt to parse the response JSON
        try:
            return response.json()
        except ValueError:
            logger.error("Response is not valid JSON")
            raise ValueError("Response is not valid JSON")
    
    # Catch specific exceptions and log meaningful messages
    except requests.Timeout:
        logger.error("Request timed out")
        raise TimeoutError("The request timed out")
    except requests.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
        raise Exception("Connection error occurred") from conn_err
    except requests.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
        raise http_err  # Re-raise HTTPError to allow higher-level handling
    except requests.RequestException as req_err:
        logger.error(f"API request failed: {req_err}")
        raise Exception("API request failed") from req_err