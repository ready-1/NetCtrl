import os

from pprint import pprint

from net_core.api_helpers.device_helpers import get_device_name, set_device_name, reboot_device, config_copy, save_config, get_bonjour_status, set_bonjour_status
from net_core.api_helpers.token_manager import TokenManager



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
        token_manager.clear_token(SWITCH_IP)
        token = token_manager.get_token(SWITCH_IP, SWITCH_USERNAME, SWITCH_PASSWORD)
        print(f"Successfully obtained token: {token}")

        
        result = set_bonjour_status(SWITCH_IP, token, "disabled")
        print(result)
        result = get_bonjour_status(SWITCH_IP, token)
        print(result)
        result = set_bonjour_status(SWITCH_IP, token, "enabled")
        print(result)
        result = get_bonjour_status(SWITCH_IP, token)
        print(result)

    except Exception as e:
        pprint(f"Error during test: {e}")

# Run the test
if __name__ == "__main__":
    test_device_info()