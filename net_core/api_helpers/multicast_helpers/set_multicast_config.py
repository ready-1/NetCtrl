"""
Helper function for setting multicast configurations.

This function interacts with the multicast configuration endpoint
of the network switch API. It adheres to a consistent format with detailed
error handling and response validation.

Author: Bob King (Ready-1 LLC) 
Date: [Today's date]
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app")

def set_multicast_config(switch_ip: str, token: str, config: dict) -> dict:
    logger.debug(f"Entering set_multicast_config with parameters: {json.dumps(locals(), indent=2)}")
