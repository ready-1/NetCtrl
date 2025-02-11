# ip_multicast_commands_1050

Pages: 1050-1050

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default 31
Format ip igmp startup-query-interval seconds
Mode Interface Config
no ip igmp startup-query-interval
This command resets the interval between General Queries sent on startup on the interface
to the default value.
Format no ip igmp startup-query-interval
Mode Interface Config
show ip igmp
This command displays the system-wide IGMP information.
Format show ip igmp
Modes Privileged EXEC
User EXEC
Term Definition
IGMP Admin Mode The administrative status of IGMP. This is a configured value.
Interface unit/slot/port
Interface Mode Indicates whether IGMP is enabled or disabled on the interface. This is a configured value.
Protocol State The current state of IGMP on this interface. Possible values are Operational or Non-Operational.
show ip igmp groups
This command displays the registered multicast groups on the interface.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
If detail is specified this command displays the registered multicast groups on the interface
in detail.
Format show ip igmp groups {unit/slot/port | vlan vland-id} [detail]
Mode Privileged EXEC
IP Multicast Commands 1050
