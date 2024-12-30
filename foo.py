import os

from pprint import pprint

from net_core.api_helpers.device_helpers import get_device_name, set_device_name, reboot_device, config_copy, save_config, get_bonjour_status, set_bonjour_status, get_lldp_remote_devices
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

        
        result = get_lldp_remote_devices(SWITCH_IP, token)
        pprint(result)


    except Exception as e:
        pprint(f"Error during test: {e}")

# Run the test
if __name__ == "__main__":
    test_device_info()