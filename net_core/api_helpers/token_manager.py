import logging
import requests
import urllib3
from django.conf import settings
from django.core.cache import cache

logger = logging.getLogger('app.api_helpers.token_manager')
logger.propagate = False


# Suppress only the specific SSL warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class TokenManager:
    TOKEN_CACHE_PREFIX = "switch_token"

    @classmethod
    def get_token(cls, switch_ip: str, username: str, password: str) -> str:
        """
        Retrieves a valid token for the specified switch. Fetches a new token if none exists or if expired.

        Parameters:
            switch_ip (str): The IP address of the target switch.
            username (str): Admin username.
            password (str): Admin user's password.

        Returns:
            str: The valid token for the switch.
        """
        cache_key = f"{cls.TOKEN_CACHE_PREFIX}_{switch_ip}"
        cached_token = cache.get(cache_key)

        if cached_token:
            logger.debug(f"Using cached token for switch {switch_ip}")
            return cached_token

        logger.info(f"No valid token found for switch {switch_ip}. Fetching a new one...")
        return cls._fetch_token(switch_ip, username, password)

    @classmethod
    def _fetch_token(cls, switch_ip: str, username: str, password: str) -> str:
        protocol = "https" if settings.USE_HTTPS else "http"
        port = "8443" if settings.USE_HTTPS else "80"
        url = f"{protocol}://{switch_ip}:{port}/api/v1/login"

        data = {
            "login": {
                "username": username,
                "password": password
            }
        }
        try:
            response = requests.post(url, json=data, timeout=10, verify=False)
            response.raise_for_status()

            resp_data = response.json()
            logger.debug(f"Raw API response: {resp_data}")

            # Validate response structure
            if "resp" not in resp_data or "login" not in resp_data:
                raise ValueError("Invalid response structure from API")

            if resp_data["resp"]["status"] != "success" or resp_data["resp"]["respCode"] != 0:
                raise ValueError(f"Login failed: {resp_data['resp']['respMsg']}")

            token = resp_data["login"]["token"]
            expires = int(resp_data["login"].get("expire", 3600))  # Default to 3600 seconds

            # Cache the token
            cache_key = f"{cls.TOKEN_CACHE_PREFIX}_{switch_ip}"
            cache.set(cache_key, token, timeout=expires - 10)  # Subtract 10 seconds for safety
            logger.info(f"Token cached for switch {switch_ip} with expiration in {expires} seconds")

            return token

        except KeyError as e:
            logger.error(f"Missing key in API response: {e}")
            raise ValueError(f"Invalid response structure: {resp_data}") from e
        except requests.exceptions.RequestException as req_err:
            logger.error(f"HTTP request error: {req_err}")
            raise
        except ValueError as val_err:
            logger.error(f"Value error: {val_err}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise

    @classmethod
    def get_token_expiry(cls, switch_ip: str) -> int:
        """
        Gets the remaining time (in seconds) before a token expires.

        Parameters:
            switch_ip (str): The IP address of the target switch.

        Returns:
            int: Time remaining in seconds, or -1 if no token is cached.
        """
        cache_key = f"{cls.TOKEN_CACHE_PREFIX}_{switch_ip}"
        ttl = cache.ttl(cache_key)  # Redis-specific method for TTL
        return ttl if ttl is not None else -1
    
    @classmethod
    def clear_token(cls, switch_ip: str) -> None:
        """
        Clears the stored token for a given switch IP from the cache.

        Purpose:
            Removes the token associated with the specified switch IP from the
            cache, forcing the system to fetch a new token when needed.

        Parameters:
            switch_ip (str): IP address of the switch whose token needs to be cleared.

        Returns:
            None

        Example Usage:
            >>> TokenManager.clear_token("192.168.1.1")
        """
        cache_key = f"{cls.TOKEN_CACHE_PREFIX}_{switch_ip}"
        if cache.get(cache_key):
            cache.delete(cache_key)
            logger.info("Token cleared for switch %s.", switch_ip)
        else:
            logger.warning("No token found in cache for switch %s.", switch_ip)