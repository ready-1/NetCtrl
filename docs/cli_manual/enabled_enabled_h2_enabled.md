# enabled_enabled_h2_enabled

Pages: 559-559

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
IP Address Displays whether IP Address Validation is enabled or disabled.
Validation
VLAN The VLAN ID for each displayed row.
Configuration Displays whether DAI is enabled or disabled on the VLAN.
Log Invalid Displays whether logging of invalid ARP packets is enabled on the VLAN.
ACL Name The ARP ACL Name, if configured on the VLAN.
Static Flag If the ARP ACL is configured static on the VLAN.
Command example:
(NETGEAR Switch) #show ip arp inspection vlan 10-12
Source Mac Validation : Disabled
Destination Mac Validation : Disabled
IP Address Validation : Disabled
Vlan Configuration Log Invalid ACL Name Static flag
---- ------------- ----------- --------- ----------
10 Enabled Enabled H2 Enabled
11 Disabled Enabled
12 Enabled Disabled
show ip arp inspection statistics
Use this command to display the statistics of the ARP packets that are processed by
Dynamic ARP Inspection (DAI). For the vlan-list argument, you can enter a list of VLANs
(for example, 12-18 or 12,14) to display the statistics on all DAI-enabled VLANs in the list, or
enter a single VLAN to display the statistics for only that VLAN. If you do not include the
vlan keyword and vlan-list argument, the command output displays a summary of the
forwarded and dropped ARP packets.
Format show ip arp inspection statistics [vlan vlan-list]
Mode Privileged EXEC
User EXEC
Term Definition
VLAN The VLAN ID for each displayed row.
Forwarded The total number of valid ARP packets forwarded in this VLAN.
Dropped The total number of not valid ARP packets dropped in this VLAN.
DHCP Drops The number of packets dropped due to DHCP snooping binding database match failure.
Switching Commands 559
