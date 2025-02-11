# pim_commands_this_section_describes_the_commands_you_use_to_configure_protocol_independent_multicast

Pages: 1028-1028

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ip dvmrp route
This command displays the multicast routing information for DVMRP.
Format show ip dvmrp route
Modes Privileged EXEC
User EXEC
Term Definition
Source Address The multicast address of the source group.
Source Mask The IP Mask for the source group.
Upstream Neighbor The IP address of the neighbor which is the source for the packets for a specified multicast address.
Interface The interface used to receive the packets sent by the sources.
Metric The distance in hops to the source subnet. This field has a different meaning than the Interface
Metric field.
Expiry Time (secs) The expiry time in seconds, which is the time left for this route to age out.
Up Time (secs) The time when a specified route was learnt, in seconds.
PIM Commands
This section describes the commands you use to configure Protocol Independent Multicast
-Dense Mode (PIM-DM) and Protocol Independent Multicast - Sparse Mode (PIM-SM).
PIM-DM and PIM-SM are multicast routing protocols that provides scalable inter-domain
multicast routing across the Internet, independent of the mechanisms provided by any
particular unicast routing protocol. Only one PIM mode can be operational at a time.
ip pim dense
This command administratively enables the PIM Dense mode across the router.
Default disabled
Format ip pim dense
Mode Global Config
Command example:
(NETGEAR) (Config) #ip pim dense
IP Multicast Commands 1028
