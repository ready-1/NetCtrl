# ip_multicast_commands_1051

Pages: 1051-1051

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If you do not use the detail keyword, the following fields display.
Term Definition
IP Address The IP address of the interface participating in the multicast group.
Subnet Mask The subnet mask of the interface participating in the multicast group.
Interface Mode This displays whether IGMP is enabled or disabled on this interface.
The following fields are not displayed if the interface is not enabled.
Term Definition
Querier Status This displays whether the interface has IGMP in Querier mode or Non-Querier mode.
Groups The list of multicast groups that are registered on this interface.
If you use the detail keyword, the following fields display.
Term Definition
Multicast IP The IP address of the registered multicast group on this interface.
Address
Last Reporter The IP address of the source of the last membership report received for the specified multicast
group address on this interface.
Up Time The time elapsed since the entry was created for the specified multicast group address on this
interface.
Expiry Time The amount of time remaining to remove this entry before it is aged out.
Version1 Host The time remaining until the local router assumes that there are no longer any IGMP version 1
Timer multicast members on the IP subnet attached to this interface. This could be an integer value or
“-----” if there is no Version 1 host present.
Version2 Host The time remaining until the local router assumes that there are no longer any IGMP version 2
Timer multicast members on the IP subnet attached to this interface. This could be an integer value or
“-----” if there is no Version 2 host present.
Group The group compatibility mode (v1, v2 or v3) for this group on the specified interface.
Compatibility Mode
show ip igmp interface
This command displays the IGMP information for the interface.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
IP Multicast Commands 1051
