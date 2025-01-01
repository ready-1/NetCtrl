import logging
import os
import json
import django
from net_core.api_helpers.token_manager import TokenManager

# Set up Django environment
django.setup()

# Configure logging
LOG_FILE = "script.log"

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),  # Logs to a file
        logging.StreamHandler()        # Logs to the console
    ]
)

logger = logging.getLogger("script_logger")

def test_helper_function():
    print("\033[H\033[J", end="")
    logger.info("Starting test of helper function...")

    try:
        # Retrieve required settings
        switch_ip = os.getenv("SWITCH_IP", None)
        switch_username = os.getenv("SWITCH_USERNAME", None)
        switch_password = os.getenv("SWITCH_PASSWORD", None)

        if not switch_ip or not switch_username or not switch_password:
            raise ValueError("SWITCH_IP, SWITCH_USERNAME, and SWITCH_PASSWORD must be set in environment variables.")

        logger.debug(f"Using SWITCH_IP: {switch_ip}, SWITCH_USERNAME: {switch_username}, SWITCH_PASSWORD: {switch_password}")

        token_manager = TokenManager()
        token = token_manager.get_token(switch_ip, switch_username, switch_password)
        logger.debug(f"Retrieved token: {token}")

        from net_core.api_helpers.diagnostics_helpers import ping_test_start

       
        result = ping_test_start(switch_ip, token, "237.84.2.178", action=1, ip_version=4, count=3, size=64, timeout=10, interval=1.0)
        pretty_json = json.dumps(result, indent=4)
        logger.info(f"API response: {pretty_json}")


    except Exception as e:
        logger.error("Error occurred while testing helper function: %s", e)

if __name__ == "__main__":
    logger.info("Starting the script...")
    test_helper_function()
    logger.info("Script finished.")