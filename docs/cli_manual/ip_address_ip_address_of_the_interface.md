# ip_address_ip_address_of_the_interface

Pages: 553-553

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
clear ip dhcp snooping statistics
Use this command to clear all DHCP Snooping statistics.
Format clear ip dhcp snooping statistics
Mode Privileged EXEC
User EXEC
show ip verify source
Use this command to display the IPSG configurations on all ports.
Format show ip verify source
Mode Privileged EXEC
User EXEC
Term Definition
Interface Interface address in unit/slot/port format.
Filter Type Is one of two values:
ip-mac: User has configured MAC address filtering on this interface.
ip: Only IP address filtering on this interface.
IP Address IP address of the interface
MAC Address If MAC address filtering is not configured on the interface, the MAC Address field is empty. If port
security is disabled on the interface, then the MAC Address field displays “permit-all.”
VLAN The VLAN for the binding rule.
Command example:
(NETGEAR Switch) #show ip verify source
Interface Filter Type IP Address MAC Address Vlan
--------- ----------- --------------- ----------------- -----
0/1 ip-mac 210.1.1.3 00:02:B3:06:60:80 10
0/1 ip-mac 210.1.1.4 00:0F:FE:00:13:04 10
show ip verify interface
Use this command to display the IPSG filter type for a specific interface.
Format show ip verify interface unit/slot/port
Mode Privileged EXEC
User EXEC
Switching Commands 553
