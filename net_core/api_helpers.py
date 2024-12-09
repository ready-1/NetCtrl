import logging
import requests
from django.conf import settings

# Get the logger defined in settings.py
logger = logging.getLogger('app')

def make_api_request(url, method="GET", headers=None, data=None, params=None, timeout=10):
    """
    Makes a robust API request with centralized logging.
    
    :param url: The API endpoint URL
    :param method: HTTP method (GET, POST, PUT, DELETE)
    :param headers: Dictionary of request headers
    :param data: JSON data payload for POST/PUT requests
    :param params: Dictionary of query parameters for GET requests
    :param timeout: Timeout in seconds for the API call
    :return: JSON response data if successful; raises exceptions on failure
    """
    try:
        if settings.DEBUG == True:
            logger.debug(f"Starting API request: {method} {url}")
            logger.debug(f"Headers: {headers}")
            logger.debug(f"Data: {data}")
            logger.debug(f"Params: {params}")
        else:
            logger.info(f"Starting API request: {method} {url}")
        
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            json=data,
            params=params,
            timeout=timeout
        )
        
        logger.info(f"Response Status: {response.status_code}")
        response.raise_for_status()
        
        try:
            json_response = response.json()
            if settings.DEBUG == True:
                logger.debug(f"Response JSON: {json_response}")
            else:
                logger.info(f"API Call to {url} completed successfully.")
            logger.debug(f"Response JSON: {json_response}")
            return json_response
        except ValueError:
            logger.error("Response is not valid JSON")
            raise ValueError("Response is not valid JSON")
    
    except requests.Timeout:
        logger.error("Request timed out")
        raise TimeoutError("The request timed out")
    
    except requests.ConnectionError as conn_err:
        logger.error(f"Connection error: {conn_err}")
        raise
    
    except requests.RequestException as req_err:
        logger.error(f"API request failed: {req_err}")
        raise