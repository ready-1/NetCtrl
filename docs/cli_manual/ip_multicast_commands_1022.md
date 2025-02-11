# ip_multicast_commands_1022

Pages: 1022-1022

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ip mroute static-multicast
Use this command in Privileged EXEC or User EXEC mode to display the manually added
static multicast routes.
Format show ip mroute static-multicast
Modes Privileged EXEC
User EXEC
Parameter Description
Maximum Multicast The maximum number of allowed static multicast routes.
Static Address Count
Current Multicast Static The number of configured static multicast routes.
Address Count
Group Address The configured multicast group IP address.
Egress VLAN List The VLANs that are associated with the static multicast route.
Command example:
(M4300-48X) #show ip mroute static-multicast
Maximum Multicast Static Address Count ........ 32
Current Multicast Static Address Count ........ 4
Group Address Egress VLAN List
---------------------- -----------------------------------
225.1.1.1 1-2
225.1.1.5 1
225.1.1.2 1-2
225.1.1.3 1
clear ip mroute
This command deletes all or the specified IP multicast route entries.This command clears
only dynamic mroute entries. It does not clear static mroutes.
Format clear ip mroute {* | group-address [source-address]}
Modes Privileged EXEC
Parameter Description
* Deletes all IPv4 entries from the IP multicast routing table.
IP Multicast Commands 1022
