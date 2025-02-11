# ip_multicast_commands_1036

Pages: 1036-1036

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip pim-trapflags
This command sets the PIM trap mode to the default.
Format no ip pim-trapflags
Mode Global Config
show ip mfc
This command displays multicast route entries in the multicast forwarding (MFC) database.
Format show ip mfc
Modes Privileged EXEC
User EXEC
Term Definition
MFC IPv4 Mode Indicates whether IPv4 multicast routing is operational.
MFC IPv6 Mode Indicates whether IPv6 Multicast routing is operational.
MFC Entry Count The number of entries present in MFC.
Current multicast IPv4 Protocol The current operating IPv4 multicast routing protocol.
Current multicast IPv6 Protocol The current operating multicast IPv6 routing protocol.
Total Software Forwarded The total number of multicast packets forwarded in software.
packets
Source Address The source address of the multicast route entry.
Group Address The group address of the multicast route entry.
Packets Forwarded in Software The number of multicast packets that are forwarded in software for a specific multicast
for this entry route entry.
Protocol The multicast touting protocol that added a specific entry
Expiry Time (secs) The expiration time in seconds for a specific multicast route entry.
Up Time (secs) The up time in seconds for a specific multicast routing entry.
Incoming interface The incoming interface for a specific multicast route entry.
Outgoing interface list The outgoing interface list for a specific multicast route entry.
Command example:
(NETGEAR) #show ip mfc
MFC IPv4 Mode.................................. Enabled
MFC IPv6 Mode.................................. Disabled
MFC Entry Count ............................... 1
IP Multicast Commands 1036
