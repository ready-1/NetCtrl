# ip_multicast_commands_1019

Pages: 1019-1019

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format show ip mcast interface {unit/slot/port | vlan vlan-id}
Modes Privileged EXEC
User EXEC
Term Definition
Interface unit/slot/port
TTL The time-to-live value for this interface.
show ip mroute
This command displays a summary or all the details of the multicast table.
Format show ip mroute {detail | summary}
Modes Privileged EXEC
User EXEC
If you use the detail parameter, the command displays the following fields.
Term Definition
Source IP Addr The IP address of the multicast data source.
Group IP Addr The IP address of the destination of the multicast packet.
Expiry Time The time of expiry of this entry in seconds.
Up Time The time elapsed since the entry was created in seconds.
RPF Neighbor The IP address of the RPF neighbor.
Flags The flags associated with this entry.
If you use the summary parameter, the command displays the following fields.
Term Definition
Source IP Addr The IP address of the multicast data source.
Group IP Addr The IP address of the destination of the multicast packet.
Protocol The multicast routing protocol by which the entry was created.
Incoming Interface The interface on which the packet for the source/group
arrives.
Outgoing Interface The list of outgoing interfaces on which the packet
List is forwarded.
IP Multicast Commands 1019
