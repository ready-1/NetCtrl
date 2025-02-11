# ip_multicast_commands_1039

Pages: 1039-1039

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
If no interface is specified, the command displays the status parameters of all PIM-enabled
interfaces.
Format show ip pim interface [unit/slot/port | vlan vlan-id]
Modes Privileged EXEC
User EXEC
Term Definition
Interface unit/slot/port, which is the interface number.
Mode Indicates the active PIM mode enabled on the interface is dense or sparse.
Hello Interval The frequency at which PIM hello messages are transmitted on this interface. By default, the value is
30 seconds.
Join Prune Interval The join/prune interval value for the PIM router. The interval is in seconds.
DR Priority The priority of the Designated Router configured on the interface. This field is not applicable if the
interface mode is Dense.
BSR Border Identifies whether this interface is configured as a bootstrap router border interface.
Neighbor Count The number of PIM neighbors learned on this interface. This is a dynamic value and is shown only
when a PIM interface is operational.
Designated Router The IP address of the elected Designated Router for this interface. This is a dynamic value and will
only be shown when a PIM interface is operational. This field is not applicable if the interface mode
is Dense.
Command example:
(NETGEAR) #show ip pim interface
Interface.........................................1/0/1
Mode............................................Sparse
Hello Interval (secs)...........................30
Join Prune Interval (secs)......................60
DR Priority.....................................1
BSR Border......................................Disabled
Neighbor Count..................................1
Designated Router...............................192.168.10.1
Interface.........................................1/0/2
Mode............................................Sparse
Hello Interval (secs)...........................30
Join Prune Interval (secs)......................60
DR Priority.....................................1
BSR Border......................................Disabled
IP Multicast Commands 1039
