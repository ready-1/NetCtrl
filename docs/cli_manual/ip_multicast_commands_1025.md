# ip_multicast_commands_1025

Pages: 1025-1025

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip dvmrp
This command sets the administrative mode of DVMRP on an interface to inactive.
Format no ip dvmrp
Mode Interface Config
show ip dvmrp
This command displays the system-wide information for DVMRP.
Format show ip dvmrp
Modes Privileged EXEC
User EXEC
Term Definition
Admin Mode Indicates whether DVMRP is enabled or disabled.
Version String The version of DVMRP being used.
Number of Routes The number of routes in the DVMRP routing table.
Reachable Routes The number of entries in the routing table with non-infinite metrics.
The following fields are displayed for each interface.
Term Definition
Interface unit/slot/port
Interface Mode The mode of this interface. Possible values are Enabled and Disabled.
State The current state of DVMRP on this interface. Possible values are Operational or Non-Operational.
show ip dvmrp interface
This command displays the interface information for DVMRP on the specified interface.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
Format show ip dvmrp interface {unit/slot/port | vlan vland-id}
Modes Privileged EXEC
User EXEC
IP Multicast Commands 1025
