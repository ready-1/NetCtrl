"""
Helper functions for managing multicast operations.

This module provides functions to interact with the multicast feature
of the network switch API. Each function adheres to a consistent format with detailed
error handling and response validation.

Author: Bob King (Ready-1 LLC) 
Date: [Today's date]
"""

import logging
import requests
from django.conf import settings
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger for the module
logger = logging.getLogger("app")

from .get_multicast_info import get_multicast_info
from .set_multicast_config import set_multicast_config
from .get_multicast_group_info import get_multicast_group_info
from .add_multicast_group import add_multicast_group
from .remove_multicast_group import remove_multicast_group
from .update_multicast_group import update_multicast_group
from .list_multicast_groups import list_multicast_groups

# Constants specific to this module
API_VERSION = "v1"
TIMEOUT = 10  # Default timeout for API requests
