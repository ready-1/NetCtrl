"""
Helper function for retrieving multicast group information.

This function interacts with the multicast group information endpoint
of the network switch API. It adheres to a consistent format with detailed
error handling and response validation.

Author: Bob King (Ready-1 LLC) 
Date: [Today's date]
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app")

def get_multicast_group_info(switch_ip: str, token: str, group_id: str) -> dict:
    logger.debug(f"Entering get_multicast_group_info with parameters: {json.dumps(locals(), indent=2)}")
