# vlan_config_set_igmp_exclude-mrouter-intf

Pages: 575-582

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
set igmp flood-report
This command lets the switch forward IGMP Join/Leave PDUs to all other ports in a VLAN.
These are IGMP Join/Leave PDUs that the switch receives from a host that is connected to a
downstream port.
Default Enabled for VLAN 1. Disabled for all other VLANs.
Format set igmp flood report [vlan-id]
Mode Global Config
VLAN Config
set igmp exclude-mrouter-intf
This command lets the switch forward IGMP Join/Leave PDUs to an upstream mrouter
interface. These are IGMP Join/Leave PDUs that the switch receives from a host that is
connected to a downstream port. In addition, the switch forwards a multicast data stream to
an upstream mrouter interface only if that port already received an IGMPv1 or IGMPv2
membership message. This behavior does not apply to IGMPv3 membership.
Default Enabled for VLAN 1. Disabled for all other VLANs.
Format set igmp exclude-mrouter-intf [vlan-id]
Mode Global Config
VLAN Config
As of software version12.0.7, a designated mrouter port that is either detected dynamically or
manually configured forwards the following information to the upstream router:
• All IGMPv1, IGMPv2, and IGMPv3 PDUs.
• All unknown multicast streams, that is, streams for which the switch did not receive IGMP
membership.
• All known multicast streams, that is, streams for which switch did receive IGMP
membership and for which it updated its hardware MFDB table.
As of software version 12.0.8. you can use the set igmp exclude-mrouter-intf
command to prevent the switch from forwarding unknown and known IGMPv1 and IGMPv2
multicast streams unless the downstream port received an IGMPv1 or IGMPv2 membership.
The switch still forward all IGMPv1, IGMPv2, and IGMPv3 PDUs.
set igmp report-suppression
Use this command to suppress the IGMP reports on a given VLAN ID. In order to optimize
the number of reports traversing the network with no added benefits, a Report Suppression
mechanism is implemented. When more than one client responds to an MGMD query for the
same Multicast Group address within the max-response-time, only the first response is
forwarded to the query and others are suppressed at the switch.
Switching Commands 575

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default Disabled
Format set igmp report-suppression vlan-id
Mode VLAN Config
Parameter Description
vlan-id A valid VLAN ID. Range is 1 to 4093.
Command example:
(NETGEAR Switch) #vlan database
(NETGEAR Switch) (Vlan)#set igmp report-suppression ?
<1-4093> Enter VLAN ID.
(NETGEAR Switch) (Vlan)#set igmp report-suppression 1
no set igmp report-suppression
Use this command to return the system to the default.
Format no set igmp report-suppression
Mode VLAN Config
set igmp header-validation
This command enables IGMP IP header validation.
If IGMP IP header validation is enabled, three fields, TTL (Time To Live), ToS (Type of
Service), and Router Alert options, are checked. The actual validated fields depend on the
IGMP version. The TTL field is validated in all the versions (IGMPv1, IGMPv2, and IGMPv3).
The Router Alert field is validated in IGMPv2 and IGMPv3. The ToS field is validated only in
IGMP version3.
Default Enabled
Format set igmp header-validation
Mode Global Config
Switching Commands 576

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no set igmp header-validation
This command disables the IGMP IP header validation.
Format no set igmp header-validation
Mode Global Config
set igmp-plus
This command enables all of the following global IGMP Snooping configuration commands:
• set igmp
• set igmp querier
• set igmp flood-report
• set igmp exclude-mrouter-intf
• set igmp fast-leave auto-assignment
Default Enabled
Format set igmp-plus
Mode Global Config
no set igmp-plus
This command disables all of the following global IGMP Snooping configuration commands:
• set igmp
• set igmp querier
• set igmp flood-report
• set igmp exclude-mrouter-intf
• set igmp fast-leave auto-assignment
Format no set igmp-plus
Mode Global Config
set igmp-plus vlan
After you enable the set igmp-plus command, you can enable the set igmp-plus
vlan command to enable all of the following global IGMP Snooping configuration
commands at the VLAN level for a particular VLAN:
• set igmp vlan
• set igmp exclude-mrouter-intf vlan
• set igmp fast-leave vlan
• set igmp flood-report vlan
Switching Commands 577

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
• set igmp querier vlan
• set igmp querier election participate vlan
The vlan argument in the set igmp-plus vlan command can be a VLAN from 1 to
4093.
Default Enabled for VLAN 1
Format set igmp-plus vlan
Mode VLAN Config
no set igmp-plus vlan
This command disables all of the following global IGMP Snooping configuration commands
at the VLAN level for a particular VLAN:
• set igmp vlan
• set igmp exclude-mrouter-intf vlan
• set igmp fast-leave vlan
• set igmp flood-report vlan
• set igmp querier vlan
• set igmp querier election participate vlan
The vlan argument in the no set igmp-plus vlan command can be a VLAN from 1 to
4093.
Format no set igmp-plus vlan
Mode VLAN Config
show igmpsnooping
This command displays IGMP Snooping information for an interface, VLAN, or LAG.
Configured information is displayed whether or not IGMP Snooping is enabled.
Format show igmpsnooping [unit/slot/port | vlan-id | lag lag-id]
Mode Privileged EXEC
If you do not use the optional arguments unit/slot/port, vlan-id, or lag-id the
command displays the following information.
Term Definition
Admin Mode Indicates whether or not IGMP Snooping is active on the switch.
Multicast Control Frame Count The number of multicast control frames that are processed by the CPU.
Switching Commands 578

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Interface Enabled for IGMP Snooping The list of interfaces on which IGMP Snooping is enabled.
VLANS Enabled for IGMP Snooping The list of VLANS on which IGMP Snooping is enabled.
When you specify the unit/slot/port values or a lag-id value, the following
information displays.
Term Definition
IGMP Snooping Indicates whether IGMP Snooping is active on the interface.
Admin Mode
Fast Leave Mode Indicates whether IGMP Snooping Fast-leave is active on the interface.
Group Membership The amount of time in seconds that a switch will wait for a report from a particular group on a
Interval (secs) particular interface before deleting the interface from the entry.This value may be configured.
Maximum The amount of time the switch waits after it sends a query on an interface because it did not receive
Response Time a report for a particular group on that interface. This value may be configured.
(secs)
Multicast Router The amount of time to wait before removing an interface from the list of interfaces with multicast
Expiry Time (secs) routers attached. The interface is removed if a query is not received. This value may be configured.
Report Indicates whether IGMP reports (set by the command set igmp report-suppression on p age575) in
Suppression Mode enabled or not.
Report Flood Mode Indicates whether the IGMP Report Flood Mode is enabled or not.
Exclude Mrouter Indicates whether the Exclude Mrouter Interface Mode is enabled or not.
Interface Mode
IGMP-PLUS Indicates whether IGMP Plus is globally enabled or not.
When you specify a value for vlan-id, the following information displays.
Term Definition
VLAN ID The VLAN ID.
IGMP Snooping Indicates whether IGMP Snooping is active on the VLAN.
Admin Mode
Fast Leave Mode Indicates whether IGMP Snooping Fast-leave is active on the VLAN.
Group Membership The amount of time in seconds that a switch will wait for a report from a particular group on a
Interval (secs) particular interface, which is participating in the VLAN, before deleting the interface from the
entry.This value may be configured.
Maximum The amount of time the switch waits after it sends a query on an interface, participating in the VLAN,
Response Time because it did not receive a report for a particular group on that interface. This value may be
(secs) configured.
Switching Commands 579

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Multicast Router The amount of time to wait before removing an interface that is participating in the VLAN from the list
Expiry Time (secs) of interfaces with multicast routers attached. The interface is removed if a query is not received. This
value may be configured.
Report Indicates whether IGMP reports (set by the command set igmp report-suppression on p age575) in
Suppression Mode enabled or not.
Report Flood Mode Indicates whether the IGMP Report Flood Mode is enabled or not.
Exclude Mrouter Indicates whether the Exclude Mrouter Interface Mode is enabled or not.
Interface Mode
IGMP-PLUS Indicates whether IGMP Plus is enabled for the VLAN or not.
Command example:
(NETGEAR switch) #show igmpsnooping 1
VLAN ID........................................ 1
IGMP Snooping Admin Mode....................... Enabled
Fast Leave Mode................................ Enabled
Group Membership Interval (secs)............... 600
Max Response Time (secs)....................... 120
Multicast Router Expiry Time (secs)............ 300
Report Suppression Mode........................ Disabled
Report Flood Mode.............................. Enabled
Exclude Mrouter Interface Mode................. Enabled
IGMP-Plus...................................... Enabled
show igmpsnooping fast-leave
This command displays the status of IGMP Snooping fast-leave for ports.
Format show igmpsnooping fast-leave
Mode Privileged EXEC
Term Definition
Interface The physical port or LAG for which the IGMP Snooping fast-leave information is displayed.
Fast-Leave Admin Indicates whether IGMP Snooping fast-leave is enabled or disabled on the physical port or LAG.
Mode
Fast-Leave Indicates the operational status of IGMP Snooping fast-leave on the physical port or LAG.
Operational Mode
Switching Commands 580

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR switch) #show igmpsnooping fast-leave
Fast Leave Auto-Assignment Mode................ Enable
Interface Fast-Leave Admin Mode Fast-Leave Operational Mode
---------- ---------------------- ----------------------------
1/1/1 Disable Disable
1/1/2 Disable Disable
1/1/3 Disable Disable
1/1/4 Disable Disable
show igmpsnooping group
This command displays the source and group IP addresses and the corresponding MAC
addresses that the switch detected through IGMP Snooping on a VLAN, interface, or LAG.
If you do not specify a specific VLAN, interface, or LAG, the command output display all
detected IGMP Snooping entries on all VLANs, interfaces, and LAGs on the switch.
Format show igmpsnooping group [vlan-id | interface (unit/slot/port) | lag lag-id]
Mode Privileged EXEC
Term Definition
VLAN ID The VLAN ID to which the host forwards IGMP member join requests.
Subscriber The IP address and MAC address of the host
MC Group The IP address and MAC address of the multicast group.
Interface The interface on which the IGMP member join request is detected.
Type The IGMP version.
Timeout (Sec) The period in seconds after which the most recent host update expires.
The timer is reset if an IGMP member join request is received for the multicast group.
Command example:
(NETGEAR switch) #show igmpsnooping group
V LAN ID S ubscriber M C Group I nterface Type Timeout(Sec)
- ------ ------------------------------ ----------------------------- --------- ---- ------------
1 1.1.1.6/00:00:00:00:00:06 2 24.1.1.6/01:00:5E:01:01:06 1 /0/16 I GMPv2 252
1 1.1.1.8/00:00:00:00:00:08 224.1.1.6/01:00:5E:01:01:06 1 /0/18 I GMPv2 256
1.1.1.9/00:00:00:00:00:09
1.1.1.10/00:00:00:00:00:0A
1.1.1.11/00:00:00:00:00:0B
1.1.1.12/00:00:00:00:00:0C
Switching Commands 581

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
1 1.1.1.9/00:00:00:00:00:09 2 24.1.1.7/01:00:5E:01:01:07 1 /0/18 I GMPv2 181
1 1.1.1.10/00:00:00:00:00:0A 2 24.1.1.8/01:00:5E:01:01:08 1 /0/18 I GMPv2 182
1 1.1.1.11/00:00:00:00:00:0B 2 24.1.1.9/01:00:5E:01:01:09 1 /0/18 I GMPv2 183
1 1.1.1.12/00:00:00:00:00:0C 2 24.1.1.10/01:00:5E:01:01:0A 1 /0/18 I GMPv2 184
In the command output example, both multicast group IP addresses and interfaces are used:
• The information on the 1st and 2nd lines is for the same group (224.1.1.6, with different
sources) but detected on different interfaces (1/0/16 and 1/0/18) and therefore displayed
on two separate lines.
• The information on the 2nd line is for a single group (224.1.1.6) on interface 1/0/18, but
includes subscriptions from different hosts. All the host IP addresses are combined on the
same line.
• The information on the 3rd, 4th, 5th, and 6th lines are for different multicast groups but
detected on the same interface. Because the group IP addresses are different, the
information is displayed on different lines.
show igmpsnooping mrouter interface
This command displays information about statically configured ports.
Format show igmpsnooping mrouter interface unit/slot/port
Mode Privileged EXEC
Term Definition
Interface The port for which multicast router information is displayed.
Multicast Router Indicates whether multicast router is statically enabled on the interface.
Attached
VLAN ID The list of VLANs of which the interface is a member.
show igmpsnooping mrouter vlan
This command displays information about statically configured ports.
Format show igmpsnooping mrouter vlan unit/slot/port
Mode Privileged EXEC
Term Definition
Interface The port on which multicast router information is displayed.
VLAN ID The list of VLANs of which the interface is a member.
Switching Commands 582
