# mac_verify_represents_the_number_of_dhcp_messages_that_were_filtered_on_an_untrusted_inter_295f2455

Pages: 924-926

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ipv6 dhcp snooping statistics
Use this command to list statistics for IPv6 DHCP Snooping security violations on untrusted
ports.
Format show ipv6 dhcp snooping statistics
Mode Privileged EXEC
User EXEC
Term Definition
Interface The IPv6 address of the interface in unit/slot/port format.
MAC Verify Represents the number of DHCP messages that were filtered on an untrusted interface because of
Failures source MAC address and client hardware address mismatch.
Client Ifc Mismatch Represents the number of DHCP release and Deny messages received on the different ports than
learned previously.
DHCP Server Msgs Represents the number of DHCP server messages received on Untrusted ports.
Rec’d
Command example:
(NETGEAR Switch) #show ipv6 dhcp snooping statistics
Interface MAC Verify Client Ifc DHCP Server
Failures Mismatch Msgs Rec'd
----------- ---------- ---------- -----------
1/0/2 0 0 0
1/0/3 0 0 0
1/0/4 0 0 0
1/0/5 0 0 0
1/0/6 0 0 0
1/0/7 0 0 0
1/0/8 0 0 0
1/0/9 0 0 0
1/0/10 0 0 0
1/0/11 0 0 0
1/0/12 0 0 0
1/0/13 0 0 0
1/0/14 0 0 0
1/0/15 0 0 0
1/0/16 0 0 0
1/0/17 0 0 0
1/0/18 0 0 0
1/0/19 0 0 0
1/0/20 0 0 0
IPv6 Commands 924

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
clear ipv6 dhcp snooping binding
Use this command to clear all DHCPv6 Snooping bindings on all interfaces or on a specific
interface.
Format clear ipv6 dhcp snooping binding [interface unit/slot/port]
Mode Privileged EXEC
User EXEC
clear ipv6 dhcp snooping statistics
Use this command to clear all DHCPv6 Snooping statistics.
Format clear ipv6 dhcp snooping statistics
Mode Privileged EXEC
User EXEC
show ipv6 verify
Use this command to display the IPv6 configuration on a specified interface in the
unit/slot/port format.
Format show ipv6 verify unit/slot/port
Mode Privileged EXEC
User EXEC
Term Definition
Interface Interface address in unit/slot/port format.
Filter Type Is one of two values:
• ip-v6mac: User has configured MAC address filtering on this interface.
• ipv6: Only IPv6 address filtering on this interface.
IPv6 Address IPv6 address of the interface
MAC Address If MAC address filtering is not configured on the interface, the MAC Address field is empty. If port
security is disabled on the interface, then the MAC Address field displays “permit-all.”
VLAN The VLAN for the binding rule.
Command example:
(NETGEAR Switch) #show ipv6 verify 0/1
I nterface Filter Type IP Address MAC Address Vlan
- -------- ----------- --------------- ----------------- -----
0/1 ipv6-mac 2000::1/64 00:02:B3:06:60:80 10
0/1 ipv6-mac 3000::1/64 00:0F:FE:00:13:04 10
IPv6 Commands 925

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ipv6 verify source
Use this command to display the IPv6SG configurations on all ports. If the interface option
is specified, the output is restricted to the specified unit/slot/port argument.
Format show ipv6 verify source [interface unit/slot/port]
Mode Privileged EXEC
User EXEC
Term Definition
Interface Interface address in unit/slot/port format.
Filter Type Is one of two values:
• ip-v6mac: User has configured MAC address filtering on this interface.
• ipv6: Only IPv6 address filtering on this interface.
IPv6 Address IPv6 address of the interface
MAC Address If MAC address filtering is not configured on the interface, the MAC Address field is empty. If port
security is disabled on the interface, then the MAC Address field displays permit-all.
VLAN The VLAN for the binding rule.
Command example:
(NETGEAR Switch) #show ipv6 verify source
I nterface Filter Type IP Address MAC Address Vlan
- -------- ----------- --------------- - ---------------- -----
0/1 ipv6-mac 2000::1/64 00:02:B3:06:60:80 10
0/1 ipv6-mac 3000::1/64 00:0F:FE:00:13:04 10
show ipv6 source binding
Use this command to display the IPv6SG bindings.
Format show ipv6 source binding [dhcp-snooping | static] [interface unit/slot/port]
[vlan-id]
Mode Privileged EXEC
User EXEC
Term Definition
MAC Address The MAC address for the entry that is added.
IP Address The IP address of the entry that is added.
Type Entry type; statically configured from CLI or dynamically learned from DHCP Snooping.
IPv6 Commands 926
