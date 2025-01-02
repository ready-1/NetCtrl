"""
Helper function for GET /device_cable_test endpoint.

This function retrieves the cable test results for a specific port on the network switch.

Author: Bob King (Ready-1 LLC)
Date: 2025-01-01
"""

import logging
from net_core.api_helpers.utils import make_api_request, InvalidResponse

# Configure logger
logger = logging.getLogger("app")

def get_device_cable_test(switch_ip: str, token: str, portid: int):
    """
    Fetches the cable test results for a specific port on a network switch.

    Parameters:
        switch_ip (str): The IP address of the target switch.
        token (str): Bearer token for API authentication.
        portid (int): The port ID to test (valid range: 1 - 4096).

        Returns:
        dict: Processed cable test results including status, statusText, lengths, and failure distance.
        The structure includes:
            - status (int): Numeric status of the cable test.
            - statusText (str): Human-readable description of the cable test status.
            - lenKnown (int): Known cable length in meters (0 if unknown).
            - shortestLen (int): Shortest possible cable length in meters.
            - longestLen (int): Longest possible cable length in meters.
            - cableFailureLen (int): Distance to detected fault in meters.

    Raises:
        ValueError: If the portid is invalid.
        InvalidResponse: If the response from the API is not as expected.
        Exception: For unexpected errors during the API call.

    Example Usage:
        ```
        result = get_device_cable_test("192.168.1.1", "example_token", 1)
        print(result)
        ```

    Example Response:
        {
            "cableTestStatus": {
                "status": 2,
                "lenKnown": 10,
                "shortestLen": 9,
                "longestLen": 11,
                "cableFailureLen": 0
            }
        }

    JSON Response Structure:
        resp (object): {
            status (str): Status of the operation ("success" or "failure").
            respCode (int): Response code.
            respMsg (str): Response message.
        }
        cableTestStatus (object): {
            status (int): Cable test status (0 - Untested, 1 - Fail, ..., 7 - No Cable).
            statusText (str): Human-readable description of the status.
            lenKnown (int): Known cable length in meters (0 if unknown).
            shortestLen (int): Shortest possible cable length in meters.
            longestLen (int): Longest possible cable length in meters.
            cableFailureLen (int): Distance to detected fault in meters.
        }
    """
    # Validate inputs
    if not 1 <= portid <= 4096:
        raise ValueError("portid must be between 1 and 4096.")

    endpoint = f"/device_cable_test"
    params = {"portid": portid}
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = make_api_request(
            switch_ip=switch_ip,
            endpoint=endpoint,
            method="GET",
            headers=headers,
            params=params,
        )

        # Validate response format
        if "resp" not in response or "cableTestStatus" not in response:
            raise InvalidResponse("Missing expected keys in the response.")

        if response["resp"]["status"] != "success" or response["resp"]["respCode"] != 0:
            raise InvalidResponse(f"API error: {response['resp']['respMsg']}")

        # Map status codes to human-readable text
        status_text_map = {
            0: "Untested",
            1: "Fail",
            2: "Normal",
            3: "Open",
            4: "Short",
            5: "Open Short",
            6: "Cross Talk",
            7: "No Cable",
        }

        cable_test_status = response["cableTestStatus"]
        status = cable_test_status["status"]
        status_text = status_text_map.get(status, "Unknown")

        return {
            "status": status,
            "statusText": status_text,
            **cable_test_status
        }

    except Exception as e:
        logger.error(f"Error fetching cable test results: {e}")
        raise



