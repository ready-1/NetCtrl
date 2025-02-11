# ip_multicast_commands_1020

Pages: 1020-1020

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ip mroute group
This command displays the multicast configuration settings such as flags, timer settings,
incoming and outgoing interfaces, RPF neighboring routers, and expiration times of all the
entries in the multicast route table containing the given groupipaddr.
Format show ip mroute group groupipaddr {detail | summary}
Modes Privileged EXEC
User EXEC
Term Definition
Source IP Addr The IP address of the multicast data source.
Group IP Addr The IP address of the destination of the multicast packet.
Protocol The multicast routing protocol by which this entry was created.
Incoming Interface The interface on which the packet for this group arrives.
Outgoing Interface The list of outgoing interfaces on which this packet is forwarded.
List
show ip mroute source
This command displays the multicast configuration settings such as flags, timer settings,
incoming and outgoing interfaces, RPF neighboring routers, and expiration times of all the
entries in the multicast route table containing the given source IP address (sourceipaddr)
or source IP address and group IP address (groupipaddr) pair.
Format show ip mroute source sourceipaddr {summary | groupipaddr}
Modes Privileged EXEC
User EXEC
If you use the groupipaddr parameter, the command displays the following column
headings in the output table.
Term Definition
Source IP Addr The IP address of the multicast data source.
Group IP Addr The IP address of the destination of the multicast packet.
Expiry Time The time of expiry of this entry in seconds.
Up Time The time elapsed since the entry was created in seconds.
RPF Neighbor The IP address of the RPF neighbor.
Flags The flags associated with this entry.
IP Multicast Commands 1020
