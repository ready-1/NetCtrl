# ip_multicast_commands_1042

Pages: 1042-1042

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR) #show ip pim bsr-router candidate
BSR Address................................... 192.168.10.1
BSR Priority................................ 0
BSR Hash Mask Length........................ 30
C-BSR Advertisement Interval (secs)......... 60
Next Bootstrap message (hh:mm:ss)........... NA
Command example:
If no configured or elected BSRs exist on the router, the following message is displayed:
No BSR's exist/learned on this router.
show ip pim rp-hash
This command displays the rendezvous point (RP) selected for the specified group address.
Format show ip pim rp-hash group-address
Modes Privileged EXEC
User EXEC
Term Definition
RP Address The IP address of the RP for the group specified.
Type Indicates the mechanism (BSR or static) by which the RP was selected.
Command example:
(NETGEAR) #show ip pim rp-hash 224.1.2.0
RP Address 192.168.10.1
Type Static
Command example:
If no RP Group mapping exist on the router, the following message is displayed:
No RP-Group mappings exist/learned on this router.
show ip pim rp mapping
Use this command to display the mapping for the PIM group to the active Rendezvous points
(RP) of which the router is a aware (either configured or learned from the bootstrap router
(BSR)). Use the optional parameters to limit the display to a specific RP address
(rp-address) or to view group-to-candidate RP (candidate) or group to Static RP
mapping information (static).
IP Multicast Commands 1042
