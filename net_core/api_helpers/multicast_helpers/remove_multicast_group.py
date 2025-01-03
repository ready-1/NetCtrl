"""
Helper function for removing an existing multicast group.

This function interacts with the multicast group removal endpoint
of the network switch API. It adheres to a consistent format with detailed
error handling and response validation.

Author: Bob King (Ready-1 LLC) 
Date: [Today's date]
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app")

def remove_multicast_group(switch_ip: str, token: str, group_id: str) -> dict:
    logger.debug(f"Entering remove_multicast_group with parameters: {json.dumps(locals(), indent=2)}")
