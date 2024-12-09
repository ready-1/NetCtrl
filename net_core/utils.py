import re

def validate_ip_address(ip):
    try:
        octets = ip.split('.')
        if len(octets) != 4:
            raise ValueError("Invalid IP address format")
        for octet in octets:
            if not 0 <= int(octet) <= 255:
                raise ValueError("Invalid IP address format")
    except (ValueError, TypeError):
        raise ValueError("Invalid IP address format")
    return ip

def format_mac_address(mac):
    # Normalize MAC address to standard format (e.g., 00:11:22:33:44:55)
    return mac.lower().replace('-', ':')

