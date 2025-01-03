import logging
from net_core.api_helpers.multicast_helpers.get_multicast_info import get_multicast_info

# Configure logging
logging.basicConfig(level=logging.INFO)

def main():
    # Define the switch IP and token
    switch_ip = "192.168.1.1"  # Replace with the actual switch IP
    token = "your_token_here"   # Replace with the actual token

    try:
        # Call the get_multicast_info function
        multicast_info = get_multicast_info(switch_ip, token)
        logging.info("Multicast Information Retrieved Successfully:")
        logging.info(multicast_info)
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
