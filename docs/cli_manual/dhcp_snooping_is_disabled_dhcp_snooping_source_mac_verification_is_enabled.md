# dhcp_snooping_is_disabled_dhcp_snooping_source_mac_verification_is_enabled

Pages: 921-923

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ipv6 verify source
Use this command to disable the IPv6SG configuration in the hardware. You cannot disable
port-security alone if it is configured.
Format no ipv6 verify source
Mode Interface Config
ipv6 verify binding
Use this command to configure static IPv6 source guard (IPv6SG) entries.
Format ipv6 verify binding mac-address vlan vlan-id ipv6-address interface
interface-id
Mode Global Config
no ipv6 verify binding
Use this command to remove the IPv6SG static entry from the IPv6SG database.
Format no ipv6 verify binding mac-address vlan vlan-id ipv6-address interface
interface-id
Mode Global Config
show ipv6 dhcp snooping
Use this command to display the DHCP Snooping global configurations and per port
configurations.
Format show ipv6 dhcp snooping
Mode Privileged EXEC
User EXEC
Term Definition
Interface The interface for which data is displayed.
Trusted If it is enabled, DHCP snooping considers the port as trusted. The factory default is disabled.
Log Invalid Pkts If it is enabled, DHCP snooping application logs invalid packets on the specified interface.
Command example:
(NETGEAR Switch) #show ipv6 dhcp snooping
DHCP snooping is Disabled
DHCP snooping source MAC verification is enabled
DHCP snooping is enabled on the following VLANs:
IPv6 Commands 921

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
11 - 30, 40
Interface Trusted Log Invalid Pkts
--------- -------- ----------------
0/1 Yes No
0/2 No Yes
0/3 No Yes
0/4 No No
0/6 No No
show ipv6 dhcp snooping binding
Use this command to display the DHCP Snooping binding entries. To restrict the output, use
the following options:
• static. Restrict the output based on static entries.
• dynamic. Restrict the output based on DCHP snooping.
• interface unit/slot/port. Restrict the output based on a specific interface.
• vlan-id. Restrict the output based on a VLAN.
Format show ipv6 dhcp snooping binding [static | dynamic] [interface unit/slot/port]
[vlan-id]
Mode Privileged EXEC
User EXEC
Term Definition
MAC Address Displays the MAC address for the binding that was added. The MAC address is the key to the
binding database.
IPv6 Address Displays the valid IPv6 address for the binding rule.
VLAN The VLAN for the binding rule.
Interface The interface to add a binding into the DHCP snooping interface.
Type Binding type; statically configured from the CLI or dynamically learned.
Lease (sec) The remaining lease time for the entry.
Command example:
(NETGEAR Switch) #show ipv6 dhcp snooping binding
Total number of bindings: 2
M AC Address IPv6 Address VLAN Interface Type Lease time (Secs)
------------------ -------------- ---- --------- ---- ------------------
0 0:02:B3:06:60:80 2000::1/64 10 0/1 86400
0 0:0F:FE:00:13:04 3000::1/64 10 0/1 86400
IPv6 Commands 922

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ipv6 dhcp snooping database
Use this command to display the DHCP Snooping configuration related to the database
persistency.
Format show ipv6 dhcp snooping database
Mode Privileged EXEC
User EXEC
Term Definition
Agent URL Bindings database agent URL.
Write Delay The maximum write time to write the database into local or remote.
Command example:
(NETGEAR Switch) #show ipv6 dhcp snooping database
agent url: /10.131.13.79:/sai1.txt
write-delay: 5000
show ipv6 dhcp snooping interfaces
Use this command to show the DHCP Snooping status of all interfaces or a specified
interface.
Format show ipv6 dhcp snooping interfaces [interface unit/slot/port]
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show ipv6 dhcp snooping interfaces
Interface Trust State Rate Limit Burst Interval
(pps) (seconds)
- ---------- ---------- - ---------- --------------
1/0/1 N o 151
1/0/2 N o 151
1/0/3 No 151
(NETGEAR Switch) #show ip dhcp snooping interfaces ethernet 1/0/1
Interface Trust State Rate Limit Burst Interval
(pps) (seconds)
- ---------- ---------- - ---------- --------------
1 /0/1 Y es 151
IPv6 Commands 923
