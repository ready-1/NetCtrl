# Netgear M4300 CLI Command Reference

## Connection & Authentication
```bash
ssh admin@192.168.99.92  # Tailscale-accessible IP
# Password: FuseFuse123!
```

## Basic Configuration
```bash
configure terminal
hostname SWITCH-01
interface 1/1/1
 description "Uplink to core router"
exit
```

## VLAN Management
```bash
vlan database
vlan 10 name Staff
vlan 20 name Guests
exit

interface range 1/1/1-24
 switchport mode general
 switchport general allowed vlan add 10 tagged
 switchport general allowed vlan add 20 tagged
exit
```

## SSL Certificate Management
```bash
crypto pki import certificate <name> terminal
# Paste PEM-encoded certificate
exit
```

## Diagnostics & Monitoring
```bash
show interface status
show running-config
show vlan
show logging
```

## Safety Notes
```bash
# DANGER ZONE - Requires Network Super Admin role
write memory  # Save configuration to flash
reload        # Reboot switch
```

## Netmiko/Expect Integration Example
```python
from netmiko import Netmiko

switch = {
    'device_type': 'netgear_os',
    'host': '192.168.99.92',
    'username': 'admin',
    'password': 'FuseFuse123!',
}

connection = Netmiko(**switch)
connection.send_command('configure terminal')
connection.send_command('vlan 30 name IoT')
connection.save_config()
```

> **Important**: Always verify commands in maintenance window. Use `show running-config` to confirm changes before saving.
