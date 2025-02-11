# ip_multicast_commands_1018

Pages: 1018-1018

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ip mcast
This command displays the system-wide multicast information.
Format show ip mcast
Modes Privileged EXEC
User EXEC
Term Definition
Admin Mode The administrative status of multicast. Possible values are enabled or disabled.
Protocol State The current state of the multicast protocol. Possible values are Operational or Non-Operational.
Table Max Size The maximum number of entries allowed in the multicast table.
Protocol The multicast protocol running on the router. Possible values are PIMDM, PIMSM, or DVMRP.
Multicast The number of entries in the multicast forwarding cache.
Forwarding Cache
Entry Count
show ip mcast boundary
This command displays all the configured administrative scoped multicast boundaries.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
Format show ip mcast boundary {unit/slot/port | vlan vlan-id | all}
Modes Privileged EXEC
User EXEC
Term Definition
Interface unit/slot/port
Group Ip The group IP address.
Mask The group IP mask.
show ip mcast interface
This command displays the multicast information for the specified interface.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
IP Multicast Commands 1018
