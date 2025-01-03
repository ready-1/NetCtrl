"""
Helper function for listing all multicast groups.

This function interacts with the multicast groups listing endpoint
of the network switch API. It adheres to a consistent format with detailed
error handling and response validation.

Author: Bob King (Ready-1 LLC) 
Date: [Today's date]
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app")

def list_multicast_groups(switch_ip: str, token: str) -> dict:
    logger.debug(f"Entering list_multicast_groups with parameters: {json.dumps(locals(), indent=2)}")
