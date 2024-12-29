import os

from pprint import pprint

from net_core.api_helpers.device_helpers import get_device_info
from net_core.api_helpers.token_manager import TokenManager
from django.conf import settings

SWITCH_IP=os.getenv("SWITCH_IP")
SWITCH_USERNAME=os.getenv("SWITCH_USERNAME")
SWITCH_PASSWORD=os.getenv("SWITCH_PASSWORD")

def test_device_info():
    """
    Test the get_device_info function with a valid token.
    """
    try:
        # Step 1: Obtain a valid token using TokenManager
        token_manager = TokenManager()
        token = token_manager.get_token(SWITCH_IP, SWITCH_USERNAME, SWITCH_PASSWORD)
        print(f"Successfully obtained token: {token}")

        # Step 2: Call the get_device_info function with the token
        device_info = get_device_info(SWITCH_IP, token)
        print("Device Info Retrieved Successfully:")
        print(device_info)

    except Exception as e:
        pprint(f"Error during test: {e}")

# Run the test
if __name__ == "__main__":
    test_device_info()