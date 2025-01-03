import logging
import os
import json
import time

import django
from net_core.api_helpers.token_manager import TokenManager

# Set up Django environment
django.setup()

# Configure logging
logging.basicConfig(
    filename='app.log',  # Log file name
    filemode='w',        # Overwrite the log file on each run
    level=logging.DEBUG,  # Set the logging level to DEBUG
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)

logger = logging.getLogger("app")
logger.propagate = False

def test_helper_function():
    print("\033[H\033[J", end="")
    logger.info("Starting test of helper function...")

    try:
        # Retrieve required settings
        switch_ip = "192.168.99.92"
        switch_username = "admin"
        switch_password = "FuseFuse123!"

        if not switch_ip or not switch_username or not switch_password:
            raise ValueError("SWITCH_IP, SWITCH_USERNAME, and SWITCH_PASSWORD must be set in environment variables.")

        logger.debug(f"Using SWITCH_IP: {switch_ip}, SWITCH_USERNAME: {switch_username}, SWITCH_PASSWORD: {switch_password}")

        token_manager = TokenManager()
        token_manager.clear_token(switch_ip)
        token = token_manager.get_token(switch_ip, switch_username, switch_password)
        logger.debug(f"Retrieved token: {token}\n\n")

        from net_core.api_helpers.multicast_helpers.get_multicast_info import get_multicast_info

        logger.debug("Testing get_multicast_info...")
        multicast_info = get_multicast_info(switch_ip, token)
        logger.debug(f"get_multicast_info result: {multicast_info}")

    except Exception as e:
        logger.error("Error occurred while testing helper function: %s", e)

if __name__ == "__main__":
    logger.info("Starting the script...")
    test_helper_function()
    logger.info("Script finished.")
