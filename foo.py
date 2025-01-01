import logging
import os
import json
import django
from django.conf import settings
from net_core.api_helpers.token_manager import TokenManager

# Set up Django environment
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
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

# Create a logger for the script
logger = logging.getLogger("script_logger")

def test_helper_function():
    logger.info("Testing helper function...")

    # Import your helper function here
    

    try:
        # Retrieve required settings
        switch_ip = os.getenv("SWITCH_IP", None)
        switch_username = os.getenv("SWITCH_USERNAME", None)
        switch_password = os.getenv("SWITCH_PASSWORD", None)

        if not switch_ip or not switch_username or not switch_password:
            raise ValueError("SWITCH_IP, SWITCH_USERNAME, and SWITCH_PASSWORD must be set in environment variables.")

        logger.debug(f"Using SWITCH_IP: {switch_ip}, SWITCH_USERNAME: {switch_username}")

        # Initialize the TokenManager
        token_manager = TokenManager()

        # Retrieve the token
        token = token_manager.get_token(switch_ip, switch_username, switch_password)
        logger.debug(f"Retrieved token: {token}")

    
    
        from net_core.api_helpers.device_helpers import get_active_image
    
        # Call the helper function
        response = get_active_image(switch_ip, token)
        
        pretty_response = json.dumps(response, indent=4)
        logger.info("Helper function response:\n%s", pretty_response)

    
    
    
    
    
    except Exception as e:
        logger.error("Error occurred while testing helper: %s", e)

if __name__ == "__main__":
    logger.info("Starting the script...")
    test_helper_function()
    logger.info("Script finished.")