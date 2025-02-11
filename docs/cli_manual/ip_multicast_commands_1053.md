# ip_multicast_commands_1053

Pages: 1053-1053

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Group The group compatibility mode (v1, v2 or v3) for the specified group on this interface.
Compatibility Mode
Source Filter Mode The source filter mode (Include/Exclude) for the specified group on this interface. This is “-----” for
IGMPv1 and IGMPv2 Membership Reports.
If you use the detail keyword, the following fields display.
Term Definition
Interface Valid unit, slot and port number separated by forward slashes.
Group The group compatibility mode (v1, v2 or v3) for the specified group on this interface.
Compatibility Mode
Source Filter Mode The source filter mode (Include/Exclude) for the specified group on this interface. This is “-----” for
IGMPv1 and IGMPv2 Membership Reports.
Source Hosts The list of unicast source IP addresses in the group record of the IGMPv3 Membership Report with
the specified multicast group IP address. This is “-----” for IGMPv1 and IGMPv2 Membership
Reports.
Expiry Time The amount of time remaining to remove this entry before it is aged out. This is “-----” for IGMPv1
and IGMPv2 Membership Reports.
show ip igmp interface stats
This command displays the IGMP statistical information for the interface. The statistics are
only displayed when the interface is enabled for IGMP.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
Format show ip igmp interface stats [unit/slot/port | vlan vland-id]
Modes Privileged EXEC
User EXEC
Term Definition
Querier Status The status of the IGMP router, whether it is running in Querier mode or Non-Querier mode.
Querier IP Address The IP address of the IGMP Querier on the IP subnet to which this interface is attached.
Querier Up Time The time since the interface Querier was last changed.
Querier Expiry The amount of time remaining before the Other Querier Present Timer expires. If the local system is
Time the querier, the value of this object is zero.
Wrong Version The number of queries received whose IGMP version does not match the IGMP version of the
Queries interface.
IP Multicast Commands 1053
