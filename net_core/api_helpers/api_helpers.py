import logging
import requests
import urllib3
from datetime import datetime, timedelta
from django.conf import settings

# Suppress only the specific SSL warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


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
        logger.info(f"Fetching token for switch {switch_ip}")
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
        protocol = "https" if settings.USE_HTTPS else "http"
        port = "8443" if settings.USE_HTTPS else "80"
        login_url = f"{protocol}://{switch_ip}:{port}/api/v1/login"

        # Construct payload matching Postman structure
        payload = {
            "login": {
                "username": username,
                "password": password
            }
        }

        # Define headers based on Postman
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        try:
            logger.debug(f"Login request details for {switch_ip}: URL={login_url}, Headers={headers}, Payload={payload}")
            response = requests.post(
                login_url,
                headers=headers,
                json=payload, # Pass payload as JSON
                verify=False,
            )
            logger.debug(f"Login response for {switch_ip}: {response}")
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

            # Log the response for debugging
            data = response.json()
            logger.debug(f"Login response for {switch_ip}: {data}")

            # Check API-specific response for errors
            if data.get("resp", {}).get("status") == "fail":
                error_message = data["resp"].get("respMsg", "Unknown error")
                raise Exception(f"API login failed: {error_message}")

            # Extract token and expiry
            token = data["login"]["token"]
            expires_in = int(data["login"].get("expire", 3600))  # Default to 1 hour
            cls._tokens[switch_ip] = {
                "token": token,
                "expiry": datetime.now() + timedelta(seconds=expires_in),
            }
        except requests.RequestException as e:
            logger.error(f"Failed to login to {switch_ip}: {str(e)}")
            raise Exception(f"Failed to login to {switch_ip}: {str(e)}")
        except ValueError:
            logger.error(f"Invalid JSON response from {login_url}")
            raise Exception(f"Invalid JSON response from {login_url}")


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
    

def make_api_request(switch_ip, endpoint, method="GET", data=None, params=None, timeout=10):
    """
    Makes an HTTP API request to a switch with robust error handling and token management.
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


def fetch_device_info(switch_ip):
    """
    Fetches detailed information about the device from the device_info endpoint.

    Args:
        switch_ip (str): The IP address of the switch.

    Returns:
        dict: A dictionary containing device information with the following keys:
            - serialNumber (str): The device's serial number.
            - macAddr (str): The MAC address of the device.
            - model (str): The model number of the device.
            - swVer (str): The firmware version of the device.
            - numOfPorts (int): The total number of ports on the device.
            - numOfActivePorts (int): The number of active ports on the device.
            - memoryUsage (str): The memory usage percentage.
            - cpuUsage (str): The CPU usage percentage.
            - fanState (list[dict]): A list of fan statuses.
            - poeState (bool): Indicates if PoE is enabled.
            - upTime (str): The device uptime.
            - temperatureSensors (list[dict]): A list of temperature sensor data.
            - bootVersion (str): The boot version.
            - rxData (int): Received data in bytes.
            - txData (int): Transmitted data in bytes.

    Raises:
        Exception: If the API response indicates a failure or if the request fails.

    Example Response:
    {
        "deviceInfo": {
            "serialNumber": "53L69C5FF001D",
            "macAddr": "BC:A5:11:A0:7E:1D",
            "model": "M4300-52G-PoE+",
            "swVer": "12.0.19.6",
            "numOfPorts": 52,
            "numOfActivePorts": 1,
            "memoryUsage": "90.71%",
            "cpuUsage": "16.33%",
            "fanState": [{"FAN-1": "Operational"}, {"FAN-2": "Operational"}],
            "poeState": true,
            "upTime": "00 Days 00 Hrs 36 Mins 45 Secs",
            "temperatureSensors": [
                {"sensorNum": 1, "sensorDesc": "MAC-A", "sensorTemp": 29, "sensorState": 1},
                {"sensorNum": 2, "sensorDesc": "MAC-B", "sensorTemp": 36, "sensorState": 1}
            ],
            "bootVersion": "B1.0.0.17",
            "rxData": 4619673,
            "txData": 1347062
        },
        "resp": {
            "status": "success",
            "respCode": 0,
            "respMsg": "Operation success"
        }
    }
    """
    response = make_api_request(
        switch_ip=switch_ip,
        endpoint="device_info",
        method="GET"
    )

    if response.get("resp", {}).get("status") != "success":
        error_message = response["resp"].get("respMsg", "Unknown error")
        raise Exception(f"API call to device_info failed: {error_message}")

    return response.get("deviceInfo", {})

def fetch_device_name(switch_ip):
    """
    Fetches the device name and location from the device_name endpoint.

    Args:
        switch_ip (str): The IP address of the switch.

    Returns:
        dict: A dictionary containing the following keys:
            - name (str): The name of the device.
            - location (str): The location of the device.

    Raises:
        Exception: If the API response indicates a failure or if the request fails.

    Example Response:
    {
        "resp": {
            "status": "success",
            "respCode": 0,
            "respMsg": "Operation success"
        },
        "deviceName": {
            "name": "Switch-01",
            "location": "Server Room"
        }
    }
    """
    response = make_api_request(
        switch_ip=switch_ip,
        endpoint="device_name",
        method="GET"
    )

    if response.get("resp", {}).get("status") != "success":
        error_message = response["resp"].get("respMsg", "Unknown error")
        raise Exception(f"API call to device_name failed: {error_message}")

    return response.get("deviceName", {})

