# mld_snooping

Pages: 596-598

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
MLD Control Frame Displays the number of MLD Control frames that are processed by the CPU.
Count
VLANs Enabled for VLANs on which MLD Snooping is enabled.
MLD Snooping
Exclude Mrouter Indicates whether the Exclude Mrouter Interface is globally enabled or not.
Interface Mode
MLD-Plus Indicates whether MLD Plus is enabled or not.
When you specify the unit/slot/port values, the following information displays for the
interface.
Term Definition
Admin Mode Indicates whether MLD Snooping is active on the interface.
Fast Leave Mode Indicates whether MLD Snooping Fast Leave is active on the interface.
Group Membership Shows the period in seconds that a switch will wait for a report from a particular group on a particular
Interval interface before deleting the interface from the entry. This value may be configured.
Max Response Displays the period the switch waits after it sends a query on an interface because it did not receive
Time a report for a particular group on that interface. This value may be configured.
Multicast Router Displays the period to wait before removing an interface from the list of interfaces with multicast
Expiry Time routers attached. The interface is removed if a query is not received. This value may be configured.
When you specify a value for vlan-id, the following information displays for the VLAN.
Term Definition
Admin Mode Indicates whether MLD Snooping is active on the VLAN.
Fast Leave Mode Indicates whether MLD Snooping Fast Leave is active on the VLAN.
Group Membership Shows the period in seconds that a switch will wait for a report from a particular group on a particular
Interval interface, which is participating in the VLAN, before deleting the interface from the entry. This value
may be configured.
Max Response Displays the period the switch waits after it sends a query on an interface, participating in the VLAN,
Time because it did not receive a report for a particular group on that interface. This value may be
configured.
Multicast Router Displays the period to wait before removing an interface that is participating in the VLAN from the list
Present Expiration of interfaces with multicast routers attached. The interface is removed if a query is not received. This
Time value may be configured.
Multicast Router Indicates whether the Exclude Mrouter Interface is enabled or not.
Expiry Time
MLD-Plus Indicates whether MLD Plus is enabled or not.
Switching Commands 596

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show mldsnooping mrouter interface
Use this command to display information about statically configured multicast router attached
interfaces.
Format show mldsnooping mrouter interface unit/slot/port
Mode Privileged EXEC
Term Definition
Interface Shows the interface on which multicast router information is displayed.
Multicast Router Indicates whether multicast router is statically enabled on the interface.
Attached
VLAN ID Displays the list of VLANs of which the interface is a member.
show mldsnooping mrouter vlan
Use this command to display information about statically configured multicast router-attached
interfaces.
Format show mldsnooping mrouter vlan unit/slot/port
Mode Privileged EXEC
Term Definition
Interface Shows the interface on which multicast router information is displayed.
VLAN ID Displays the list of VLANs of which the interface is a member.
show mldsnooping ssm entries
Use this command to display the source specific multicast forwarding database built by MLD
snooping.
A given source, group, and VLAN combination can have few interfaces in Include mode and
few interfaces in Exclude mode. In such instances, two rows for the same source, group, and
VLAN combination are displayed.
Format show mldsnooping ssm entries
Mode Privileged EXEC
Term Definition
VLAN The VLAN on which the entry is learned.
Group The IPv6 multicast group address.
Source The IPv6 source address.
Switching Commands 597

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Source Filter Mode The source filter mode (Include/Exclude) for the specified group.
Interfaces • If Source Filter Mode is “Include,” specifies the list of interfaces on which a incoming packet is
forwarded. If it’s source IP address is equal to the current entry’s Source, the destination IP
address is equal to the current entry’s Group and the VLAN ID on which it arrived is current
entry’s VLAN.
• If Source Filter Mode is “Exclude,” specifies the list of interfaces on which a incoming packet is
forwarded. If it’s source IP address is *not* equal to the current entry’s Source, the destination
IP address is equal to current entry’s Group and VLAN ID on which it arrived is current entry’s
VLAN.
show mldsnooping ssm stats
Use this command to display the statistics of MLD snooping’s SSMFDB. This command
takes no options.
Format show mldsnooping ssm stats
Mode Privileged EXEC
Term Definition
Total Entries The total number of entries that can possibly be in the MLD snooping’s SSMFDB.
Most SSMFDB The largest number of entries that have been present in the MLD snooping’s SSMFDB.
Entries Ever Used
Current Entries The current number of entries in the MLD snooping’s SSMFDB.
show mldsnooping ssm groups
Use this command to display the MLD SSM group membership information.
Format show mldsnooping ssm groups
Mode Privileged EXEC
Term Definition
VLAN VLAN on which the MLD v2 report is received.
Group The IPv6 multicast group address.
Interface The interface on which the MLD v2 report is received.
Reporter The IPv6 address of the host that sent the MLDv2 report.
Source Filter Mode The source filter mode (Include/Exclude) for the specified group.
Source Address List of source IP addresses for which source filtering is requested.
List
Switching Commands 598
