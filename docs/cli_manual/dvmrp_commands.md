# dvmrp_commands

Pages: 1023-1023

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
group-address IP address of the multicast group.
source-address The optional IP address of a multicast source that is sending multicast traffic to the group.
Command example:
The following example deletes all entries from the IP multicast routing table:
(NETGEAR Switch) # clear ip mroute *
Command example:
The following example deletes all entries from the IP multicast routing table that match the
multicast group address (224.1.2.1), irrespective of which source is sending for this group:
(NETGEAR Switch) # clear ip mroute 224.1.2.1
Command example:
The following example deletes all entries from the IP multicast routing table that match the
multicast group address (224.1.2.1) and the multicast source address (192.168.10.10):
(NETGEAR Switch) # clear ip mroute 224.1.2.1 192.168.10.10
DVMRP Commands
This section describes the Distance Vector Multicast Routing Protocol (DVMRP) commands.
ip dvmrp (Global Config)
This command sets administrative mode of DVMRP in the router to active.
Default disabled
Format ip dvmrp
Mode Global Config
no ip dvmrp
This command sets administrative mode of DVMRP in the router to inactive.
Format no ip dvmrp
Mode Global Config
IP Multicast Commands 1023
