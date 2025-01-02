"""
Helper function for DELETE /sw_portmirroring.

This module provides the `delete_port_mirroring_session` function for removing a port mirroring configuration session on the network switch.

Author: Bob King (Ready-1 LLC)
Date: 2025-01-01
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

logger = logging.getLogger("app.device_helpers")

def delete_port_mirroring(switch_ip: str, token: str, session_num: int) -> dict:
    """
    Deletes a port mirroring session on the switch.

    This function sends a DELETE request to the /sw_portmirroring endpoint to remove the specified
    port mirroring configuration session.

    Parameters:
        switch_ip (str): The IP address of the target switch.
        token (str): Bearer authentication token for the API.
        session_num (int): Port mirroring session number to delete (must be a valid integer).

    Returns:
        dict: A dictionary containing the response status, response code, and message.

    Raises:
        ValueError: If `session_num` is not a valid positive integer.
        InvalidResponse: If the API response is missing required fields or is in an unexpected format.

    Example Usage:
        >>> response = delete_port_mirroring("192.168.1.1", "your_token", 1)
        >>> print(response)
        {'status': 'success', 'respCode': 0, 'respMsg': 'Port mirroring session deleted successfully'}

    Example Response:
        {
            "resp": {
                "status": "success",
                "respCode": 0,
                "respMsg": "Port mirroring session deleted successfully"
            }
        }

    JSON Response Structure:
        resp (object): API response metadata.
            - status (enum): Allowed values - 'success', 'failure'.
            - respCode (int): Response code, where 0 indicates success.
            - respMsg (str): Descriptive message about the response.
    """
    if not isinstance(session_num, int) or session_num <= 0:
        raise ValueError("`session_num` must be a positive integer.")

    endpoint = f"/sw_portmirroring"
    params = {"sessionNum": session_num}

    try:
        response = make_api_request(
            switch_ip=switch_ip,
            endpoint=endpoint,
            method="DELETE",
            headers={"Authorization": f"Bearer {token}"},
            params=params
        )
        if not response or "resp" not in response:
            raise InvalidResponse("Missing 'resp' object in API response.")

        resp = response["resp"]
        if resp["status"] != "success":
            logger.error(
                "Failed to delete port mirroring session: %s", resp.get("respMsg", "Unknown error")
            )
            raise InvalidResponse(f"API Error: {resp.get('respMsg', 'Unknown error')}")

        return resp

    except Exception as e:
        logger.exception("Error while deleting port mirroring session.")
        raise e