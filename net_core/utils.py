import re

def validate_ip_address(ip):
    # Simple IPv4 validation
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not re.match(pattern, ip):
        raise ValueError("Invalid IP address format")
    return ip

def format_mac_address(mac):
    # Normalize MAC address to standard format (e.g., 00:11:22:33:44:55)
    return mac.lower().replace('-', ':')

