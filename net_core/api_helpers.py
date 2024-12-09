import logging
import requests
from django.conf import settings

# Get the logger defined in settings.py
logger = logging.getLogger('app')

VALID_HTTP_METHODS = {"GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "HEAD"}

def make_api_request(url, method="GET", headers=None, data=None, params=None, timeout=10):
    """
    Makes an API request with robust error handling and logging.
    """
    # Validate the URL
    if not url or not isinstance(url, str) or url.strip() == "":
        logger.error("The URL provided is empty or invalid.")
        raise ValueError("The URL provided is empty or invalid.")
    
    # Validate the HTTP method
    if method.upper() not in VALID_HTTP_METHODS:
        logger.error(f"Invalid HTTP method: {method}")
        raise ValueError(f"Invalid HTTP method: {method}")

    try:
        logger.debug(f"Starting API request: {method} {url}")
        response = requests.request(
            method=method.upper(),
            url=url,
            headers=headers,
            json=data,
            params=params,
            timeout=timeout
        )
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        try:
            return response.json()
        except ValueError:
            logger.error("Response is not valid JSON")
            raise ValueError("Response is not valid JSON")
    except requests.Timeout:
        logger.error("Request timed out")
        raise TimeoutError("The request timed out")
    except requests.ConnectionError as conn_err:
        logger.error(f"Connection error: {conn_err}")
        raise Exception("Connection error occurred") from conn_err
    except requests.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
        raise http_err  # Re-raise HTTPError for specific handling
    except requests.RequestException as req_err:
        logger.error(f"API request failed: {req_err}")
        raise Exception("API request failed") from req_err