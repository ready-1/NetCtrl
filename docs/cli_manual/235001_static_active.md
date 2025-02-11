# 235.0.0.1 STATIC ACTIVE

Pages: 567-654

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show mvr interface
This command displays the MVR-enabled interfaces configuration.
Format show mvr interface [interface-id [members [vlan vid]]]
Mode Privileged EXEC
The following table explains the output parameters.
Term Description
Port Interface number
Type The MVR port type. It can be none, receiver, or source type.
Status The interface status. It consists of two characteristics:
• active or inactive indicates whether the port is forwarding.
• inVLAN or notInVLAN indicates whether the port is part of any VLAN.
Immediate Leave The state of immediate mode. It can be enabled or disabled.
Command example:
(NETGEAR Switch)#show mvr interface
Port Type Status Immediate Leave
--------- --------------- --------------------- --------------------
0/9 RECEIVER ACTIVE/inVLAN DISABLED
(switch)#show mvr interface 0/9
Type: RECEIVER Status: ACTIVE Immediate Leave: DISABLED
(switch)#show mvr interface 0/23 members
235.0.0.1 STATIC ACTIVE
(switch)#show mvr interface 0/23 members vlan 12
235.0.0.1 STATIC ACTIVE
235.1.1.1 STATIC ACTIVE
show mvr traffic
This command displays global MVR statistics.
Format show mvr traffic
Mode Privileged EXEC
Switching Commands 567

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The following table explains the output parameters.
Term Definition
IGMP Query Received Number of received IGMP queries
IGMP Report V1 Received Number of received IGMP reports V1
IGMP Report V2 Received Number of received IGMP reports V2
IGMP Leave Received Number of received IGMP leaves
IGMP Query Transmitted Number of transmitted IGMP queries
IGMP Report V1 Transmitted Number of transmitted IGMP reports V1
IGMP Report V2 Transmitted Number of transmitted IGMP reports V2
IGMP Leave Transmitted Number of transmitted IGMP leaves
IGMP Packet Receive Failures Number of failures on receiving the IGMP packets
IGMP Packet Transmit Failures Number of failures on transmitting the IGMP packets
Command example:
(NETGEAR Switch)#show mvr traffic
IGMP Query Received…........................................ 2
IGMP Report V1 Received….................................... 0
IGMP Report V2 Received….................................... 3
IGMP Leave Received…........................................ 0
IGMP Query Transmitted…..................................... 2
IGMP Report V1 Transmitted…................................. 0
IGMP Report V2 Transmitted…................................. 3
IGMP Leave Transmitted…..................................... 1
IGMP Packet Receive Failures…............................... 0
IGMP Packet Transmit Failures….............................. 0
debug mvr trace
This command enables MVR debug tracing. By default, MVR debug tracing is disabled.
Format debug mvr trace
Mode Privileged EXEC
Switching Commands 568

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no debug mvr trace
This command disables MVR debug tracing.
Format no debug mvr trace
Mode Privileged EXEC
debug mvr packet
This command enables debug tracing of MVR packets on the receiving side, transmitting
side, or both sides. By default, debug tracing of MVR packets is enabled.
Format debug mvr packet [receive | transmit]
Mode Privileged EXEC
no debug mvr packet
This command disables debug tracing of MVR packets on the receiving side, transmitting
side, or both sides.
Format no debug mvr packet [receive | transmit]
Mode Privileged EXEC
IGMP Snooping Configuration Commands
This section describes the commands you use to configure IGMP snooping. The switch
supports IGMP Versions 1, 2, and 3. The IGMP snooping feature can help conserve
bandwidth because it allows the switch to forward IP multicast traffic only to connected hosts
that request multicast traffic. IGMPv3 adds source filtering capabilities to IGMP versions 1
and 2.
Note: This note clarifies the prioritization of MGMD Snooping
Configurations. Many of the IGMP/MLD Snooping commands are
available both in the Interface and VLAN modes. Operationally the
system chooses or prefers the VLAN configured values over the
Interface configured values for most configurations when the interface
participates in the VLAN.
set igmp
This command enables IGMP Snooping on the system (Global Config Mode), an interface, or
a range of interfaces. This command also enables IGMP snooping on a particular VLAN
Switching Commands 569

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
(VLAN Config Mode) and can enable IGMP snooping on all interfaces participating in a
VLAN.
If an interface has IGMP Snooping enabled and you enable this interface for routing or enlist
it as a member of a port-channel (LAG), IGMP Snooping functionality is disabled on that
interface. IGMP Snooping functionality is re-enabled if you disable routing or remove
port-channel (LAG) membership from an interface that has IGMP Snooping enabled.
The IGMP application supports the following activities:
• Validation of the IP header checksum (as well as the IGMP header checksum) and
discarding of the frame upon checksum error.
• Maintenance of the forwarding table entries based on the MAC address versus the IP
address.
• Filters unknown IPv4 multicast packets on a VLAN if IGMP snooping is enabled, with the
exception of group addresses in the range 224.0.0.x. These control packets are always
flooded to all ports in the VLAN.
Default Enabled for VLAN 1; Disabled for other VLANs.
Format set igmp [vlan-id]
Mode Global Config
Interface Config
VLAN Config
no set igmp
This command disables IGMP Snooping on the system, an interface, a range of interfaces, or
a VLAN.
Format no set igmp [vlan-id]
Mode Global Config
Interface Config
VLAN Config
set igmp interfacemode
This command enables IGMP Snooping on all interfaces. If an interface has IGMP Snooping
enabled and you enable this interface for routing or enlist it as a member of a port-channel
(LAG), IGMP Snooping functionality is disabled on that interface. IGMP Snooping
functionality is re-enabled if you disable routing or remove port-channel (LAG) membership
from an interface that has IGMP Snooping enabled.
Default Disabled
Format set igmp interfacemode
Mode Global Config
Switching Commands 570

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no set igmp interfacemode
This command disables IGMP Snooping on all interfaces on the switch at the same time. It is
disabled by default. This command does not take effect on the interface where routing is
enabled or is a member of a port-channel (LAG). Disable routingon the interface before
setting IGMP Snooping. The interface that is a member of a port-channel (LAG) must be
removed before setting IGMP Snooping
Default Disabled
Format no set igmp interfacemode
Mode Global Config
set igmp fast-leave
This command enables or disables IGMP Snooping fast-leave on a selected interface, a
range of interfaces, or a VLAN.
When you enable fast-leave, the switch immediately removes a layer 2 LAN interface from its
forwarding table if the following situation occurs:
1. The switch does not send MAC-based general queries to the layer 2 LAN interface.
2. The switch receives an IGMP leave message for the associated multicast group.
Enable fast-leave only on VLANs for which a single host is connected to each layer 2 LAN
interface. Doing so prevents the inadvertent dropping of other hosts that are connected to the
same layer 2 LAN interface but are still interested in receiving multicast traffic that is directed
to the multicast group.
Fast-leave processing is supported for IGMPv2 hosts only.
Default Enabled for VLAN 1; Disabled for other VLANs.
Format set igmp fast-leave [vlan-id]
Mode Interface Config
Interface Range
VLAN Config
no set igmp fast-leave
This command disables IGMP Snooping fast-leave admin mode on a selected interface.
Format no set igmp fast-leave [vlan-id]
Mode Interface Config
Interface Range
VLAN Config
Switching Commands 571

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
set igmp fast-leave auto-assignment
This command globally enables or disables the automatic assignment of fast-leave for all
ports and LAGs.
On the switch, Rapid Spanning Tree Protocol (RSTP) is the default network protocol for STP.
RSTP functions at port level. Each port starts up as an edge port and functions in that
capacity until it receives an RSTP BPDU from a neighbor device. An edge port does not
participate in STP and is meant to be connected to end devices or hosts on which STP is not
enabled. However, if a port receives an RSTP BPDU, the port stops functioning as an edge
port and starts participating in STP.
Consequently, as long as the port functions as an edge port, IGMP Snooping fast-leave is
enabled. If a port receives an RSTP BPDU and stops functioning as an edge port, IGMP
Snooping fast-leave is also disabled on the port.
The set igmp fast-leave auto-assignment command controls the fast-leave
operational state, but not the configured value. On a port, a dynamically-assigned operational
value for fast-leave overrides a configured value for fast-leave.
The set igmp fast-leave auto-assignment command does the following:
• It overrides the configured port level fast-leave mode, which is disabled by default.
• It does not modify the VLAN configuration for fast-leave mode.
Between a port and a VLAN that is configured for that port, IGMP Snooping gives
precedence to the fast-leave mode for the port.
You can display the operational status of IGMP Snooping fast-leave at port level by using the
show igmpsnooping fast-leave command (see show igmpsnooping fast-leave on
p age580).
Default Enabled
Format set igmp fast-leave auto-assignment
Mode Global Config
set igmp groupmembership-interval
This command sets the IGMP group membership interval time on a VLAN, one interface, a
range of interfaces, or all interfaces. The group membership interval time is the amount of
time in seconds that a switch waits for a report from a particular group on a particular
interface before deleting the interface from the entry. This value must be greater than the
IGMPv3 maximum response time value. The range is 2 to 3600 seconds.
Default 260 seconds
Format set igmp groupmembership-interval [vlan-id] seconds
Mode Interface Config
Global Config
VLAN Config
Switching Commands 572

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no set igmp groupmembership-interval
This command sets the IGMPv3 group membership interval time to the default value.
Format no set igmp groupmembership-interval [vlan-id]
Mode Interface Config
Global Config
VLAN Config
set igmp maxresponse
This command sets the IGMP maximum response time for the system, on a particular
interface or VLAN, or on a range of interfaces. The maximum response time is the amount of
time in seconds that a switch will wait after sending a query on an interface because it did not
receive a report for a particular group in that interface. This value must be less than the IGMP
query Interval time value. The range is 1 to 300 seconds.
Default 600 seconds
Format set igmp maxresponse [vlan-id] seconds
Mode Global Config
Interface Config
VLAN Config
no set igmp maxresponse
This command sets the max response time (on the interface or VLAN) to the default value.
Format no set igmp maxresponse [vlan-id]
Mode Global Config
Interface Config
VLAN Config
set igmp mcrtrexpiretime
This command sets the multicast router present expiration time. The time is set for the
system, on a particular interface or VLAN, or on a range of interfaces. This is the amount of
time in seconds that a switch waits for a query to be received on an interface before the
interface is removed from the list of interfaces with multicast routers attached. The range is 0
to 3600 seconds. A value of 0 indicates an infinite time-out, that is, no expiration.
Default 0
Format set igmp mcrtrexpiretime [vlan-id] seconds
Mode Global Config
Interface Config
VLAN Config
Switching Commands 573

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no set igmp mcrtrexpiretime
This command sets the multicast router present expiration time to 0. The time is set for the
system, on a particular interface or a VLAN.
Format no set igmp mcrtrexpiretime [vlan-id]
Mode Global Config
Interface Config
VLAN Config
set igmp mrouter
This command configures the VLAN ID that has the multicast router mode enabled.
Format set igmp mrouter vlan-id
Mode Interface Config
no set igmp mrouter
This command disables multicast router mode for a particular VLAN ID.
Format no set igmp mrouter vlan-id
Mode Interface Config
set igmp mrouter interface
This command configures the interface or range of interfaces as a multicast router interface.
When configured as a multicast router interface, the interface is treated as a multicast router
interface in all VLANs.
Default disabled
Format set igmp mrouter interface
Mode Interface Config
no set igmp mrouter interface
This command disables the status of the interface as a statically configured multicast router
interface.
Format no set igmp mrouter interface
Mode Interface Config
Switching Commands 574

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

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show igmpsnooping ssm
This command displays information about Source Specific Multicasting (SSM) by entry,
group, or statistics. SSM delivers multicast packets to receivers that originated from a source
address specified by the receiver. SSM is only available with IGMPv3 and MLDv2.
Format show igmpsnooping ssm {entries | groups | stats}
Mode Privileged EXEC
show mac-address-table igmpsnooping
This command displays the IGMP Snooping entries in the MFDB table.
Format show mac-address-table igmpsnooping
Mode Privileged EXEC
Term Definition
VLAN ID The VLAN in which the MAC address is learned.
MAC Address A multicast MAC address for which the switch has forwarding or filtering information. The format is 6
two-digit hexadecimal numbers that are separated by colons, for example 01:23:45:67:89:AB.
Type The type of the entry, which is either static (added by the user) or dynamic (added to the table as a
result of a learning process or protocol).
Description The text description of this multicast table entry.
Interfaces The list of interfaces that are designated for forwarding (Fwd:) and filtering (Flt:).
IGMP Snooping Querier Commands
IGMP Snooping requires that one central switch or router periodically query all end-devices
on the network to announce their multicast memberships. This central device is the “IGMP
Querier”. The IGMP query responses, known as IGMP reports, keep the switch updated with
the current multicast group membership on a port-by-port basis. If the switch does not
receive updated membership information in a timely fashion, it will stop forwarding multicasts
to the port where the end device is located.
This section describes commands used to configure and display information on IGMP
Snooping Queriers on the network and, separately, on VLANs.
Switching Commands 583

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: This note clarifies the prioritization of MGMD Snooping
Configurations. Many of the IGMP/MLD Snooping commands are
available both in the Interface and VLAN modes. Operationally the
system chooses or prefers the VLAN configured values over the
Interface configured values for most configurations when the interface
participates in the VLAN.
set igmp querier
Use this command to enable IGMP Snooping Querier on the system, using Global Config
mode, or on a VLAN. Using this command, you can specify the IP Address that the Snooping
Querier switch should use as the source address while generating periodic queries.
If a VLAN has IGMP Snooping Querier enabled and IGMP Snooping is operationally disabled
on it, IGMP Snooping Querier functionality is disabled on that VLAN. IGMP Snooping
functionality is re-enabled if IGMP Snooping is operational on the VLAN.
Note: The Querier IP Address assigned for a VLAN takes preference over
global configuration.
The IGMP Snooping Querier application supports sending periodic general queries on the
VLAN to solicit membership reports.
Default Enabled in Global Config mode with default VLAN 1
Format set igmp querier [vlan-id] [address ipaddress]
Mode Global Config
VLAN Mode
no set igmp querier
Use this command to disable IGMP Snooping Querier on the system. Use the optional
address parameter to reset the querier address to 0.0.0.0.
Format no set igmp querier [vlan-id] [address]
Mode Global Config
VLAN Mode
Switching Commands 584

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
set igmp querier query-interval
Use this command to set the IGMP querier query interval time. It is the period in seconds,
from 1–1800 seconds, that the switch waits before sending another general query.
Default 60 seconds
Format set igmp querier query-interval seconds
Mode Global Config
no set igmp querier query-interval
Use this command to set the IGMP querier query interval time to its default value.
Format no set igmp querier query-interval
Mode Global Config
set igmp querier timer expiry
Use this command to set the IGMP querier timer expiration period in seconds, from 60–300
seconds. This is the period that the switch remains in non-querier mode after it has
discovered a multicast querier in the network.
Default 60 seconds
Format set igmp querier timer expiry seconds
Mode Global Config
no set igmp querier timer expiry
Use this command to set the IGMP querier timer expiration period to its default value.
Format no set igmp querier timer expiry
Mode Global Config
set igmp querier version
Use this command to set the IGMP version of the query that the snooping switch sends
periodically.
Default 1
Format set igmp querier version {1 | 2}
Mode Global Config
Switching Commands 585

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no set igmp querier version
Use this command to set the IGMP Querier version to its default value.
Format no set igmp querier version
Mode Global Config
set igmp querier election participate
Use this command to enable the Snooping Querier to participate in the Querier Election
process when it discovers the presence of another Querier in the VLAN. When this mode is
enabled, if the Snooping Querier finds that the other Querier’s source address is better (less)
than the Snooping Querier’s address, it stops sending periodic queries. If the Snooping
Querier wins the election, then it will continue sending periodic queries.
Default disabled
Format set igmp querier election participate
Mode VLAN Config
no set igmp querier election participate
Use this command to set the Snooping Querier not to participate in querier election but go
into non-querier mode as soon as it discovers the presence of another querier in the same
VLAN.
Format no set igmp querier election participate
Mode VLAN Config
show igmpsnooping querier
Use this command to display IGMP Snooping Querier information. Configured information is
displayed whether or not IGMP Snooping Querier is enabled.
Format show igmpsnooping querier [detail | vlan vlan-id]
Mode Privileged EXEC
When the optional argument vlan-id is not used, the command displays the following
information.
Field Description
Admin Mode Indicates whether or not IGMP Snooping Querier is active on the switch.
Admin Version The version of IGMP that will be used while sending out the queries.
Switching Commands 586

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Description
Querier Address The IP Address which will be used in the IPv4 header while sending out IGMP queries. It can be
configured using the appropriate command.
Query Interval The amount of time in seconds that a Snooping Querier waits before sending out the periodic
general query.
Querier Timeout The amount of time to wait in the Non-Querier operational state before moving to a Querier state.
When you specify a value for vlan-id, the following additional information displays.
Field Description
VLAN Admin Mode Indicates whether iGMP Snooping Querier is active on the VLAN.
VLAN Operational Indicates whether IGMP Snooping Querier is in “Querier” or “Non-Querier” state. When the switch is
State in Querier state, it will send out periodic general queries. When in Non-Querier state, it will wait for
moving to Querier state and does not send out any queries.
VLAN Operational Indicates the time to wait before removing a Leave from a host upon receiving a Leave request. This
Max Response value is calculated dynamically from the Queries received from the network. If the Snooping Switch
Time is in Querier state, then it is equal to the configured value.
Querier Election Indicates whether the IGMP Snooping Querier participates in querier election if it discovers the
Participation presence of a querier in the VLAN.
Querier VLAN The IP address will be used in the IPv4 header while sending out IGMP queries on this VLAN. It can
Address be configured using the appropriate command.
Operational The version of IPv4 will be used while sending out IGMP queries on this VLAN.
Version
Last Querier Indicates the IP address of the most recent Querier from which a Query was received.
Address
Last Querier Indicates the IGMP version of the most recent Querier from which a Query was received on this
Version VLAN.
When the optional argument detail is used, the command shows the global information
and the information for all Querier-enabled VLANs.
set igmp proxy-querier
If a non-querier switch receives an IGMP leave message, the non-querier switch can send
queries with 0::0 as source IP addresses. This command enables the switch to send such
proxy queries through different command modes in the following ways:
• in Global Config mode, on the entire switch
• in Interface Config mode, on an interface
• in VLAN Config mode, on a particular VLAN and all interfaces participating in the VLAN.
Switching Commands 587

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
By default, the proxy querrier is enabled.
Default enabled
Format set igmp proxy-querier [vlan-id]
Mode Global Config
Interface Config
VLAN Config
no set igmp proxy-querier
This command stops the switch from sending proxy queries through different command
modes in the following ways:
• in Global Config mode, on the entire switch
• in Interface Config mode, on an interface
• in VLAN Config mode, on a particular VLAN and all interfaces participating in the VLAN.
This command is specific to IGMP.
Format no set igmp proxy-querier [vlan-id]
Mode Global Config
Interface Config
VLAN Config
show igmpsnooping proxy-querier
This command shows the global admin mode of the IGMP snooping proxy-querier and the
interface on which it is enabled.
Format show igmpsnooping proxy-querier
Mode Privileged EXEC
Command example:
(Netgear Switch) #show igmpsnooping proxy-querier
Admin Mode..................................... Enable
Interfaces Enabled for IGMP Proxy Querier...... 1/0/1
1/0/2
1/0/3
1/0/4
Switching Commands 588

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
MLD Snooping Commands
This section describes commands used for MLD Snooping. In IPv4, Layer 2 switches can
use IGMP Snooping to limit the flooding of multicast traffic by dynamically configuring Layer 2
interfaces so that multicast traffic is forwarded only to those interfaces associated with IP
multicast addresses. In IPv6, MLD Snooping performs a similar function. With MLD
Snooping, IPv6 multicast data is selectively forwarded to a list of ports that want to receive
the data, instead of being flooded to all ports in a VLAN. This list is constructed by snooping
IPv6 multicast control packets.
Note: This note clarifies the prioritization of MGMD Snooping
Configurations. Many of the IGMP/MLD Snooping commands are
available both in the Interface and VLAN modes. Operationally the
system chooses or prefers the VLAN configured values over the
Interface configured values for most configurations when the interface
participates in the VLAN.
set mld
This command enables MLD Snooping on the system (Global Config Mode) or an interface
(Interface Config Mode). This command also enables MLD Snooping on a particular VLAN
and enables MLD Snooping on all interfaces participating in a VLAN.
If an interface has MLD Snooping enabled and you enable this interface for routing or enlist it
as a member of a port-channel (LAG), MLD Snooping functionality is disabled on that
interface. MLD Snooping functionality is re-enabled if you disable routing or remove port
channel (LAG) membership from an interface that has MLD Snooping enabled.
MLD Snooping supports the following activities:
• Validation of address version, payload length consistencies and discarding of the frame
upon error.
• Maintenance of the forwarding table entries based on the MAC address versus the IPv6
address.
• Filters out unknown IPv6 multicast packets on a VLAN if MLD snooping is enabled, with
the exception of group addresses in the range ffx2::/16 and FF05::X. These control
packets are always flooded to all ports in the VLAN.
Default Enabled for VLAN 1; Disabled for other VLANs.
Format set mld vlan-id
Mode Global Config
Interface Config
VLAN Mode
Switching Commands 589

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no set mld
Use this command to disable MLD Snooping on the system.
Format no set mld vlan-id
Mode Global Config
Interface Config
VLAN Mode
set mld interfacemode
Use this command to enable MLD Snooping on all interfaces. If an interface has MLD
Snooping enabled and you enable this interface for routing or enlist it as a member of a
port-channel (LAG), MLD Snooping functionality is disabled on that interface. MLD Snooping
functionality is re-enabled if you disable routing or remove port-channel (LAG) membership
from an interface that has MLD Snooping enabled.
Default Disabled
Format set mld interfacemode
Mode Global Config
no set mld interfacemode
Use this command to disable MLD Snooping on all interfaces.
Format no set mld interfacemode
Mode Global Config
set mld fast-leave
Use this command to enable MLD Snooping fast-leave admin mode on a selected interface
or VLAN. Enabling fast-leave allows the switch to immediately remove the Layer 2 LAN
interface from its forwarding table entry upon receiving and MLD done message for that
multicast group without first sending out MAC-based general queries to the interface.
Note: You should enable fast-leave admin mode only on VLANs where only
one host is connected to each Layer 2 LAN port. This prevents the
inadvertent dropping of the other hosts that were connected to the
same layer 2 LAN port but were still interested in receiving multicast
traffic directed to that group.
Note: Fast-leave processing is supported only with MLD version 1 hosts.
Switching Commands 590

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default Enabled for VLAN 1; Disabled for other VLANs.
Format set mld fast-leave vlan-id
Mode Interface Config
VLAN Mode
no set mld fast-leave
Use this command to disable MLD Snooping fast-leave admin mode on a selected interface.
Format no set mld fast-leave vlan-id
Mode Interface Config
VLAN Mode
set mld groupmembership-interval
Use this command to set the MLD Group Membership Interval time on a VLAN, one interface
or all interfaces. The Group Membership Interval time is the amount of time in seconds that a
switch waits for a report from a particular group on a particular interface before deleting the
interface from the entry. This value must be greater than the MLDv2 maximum response time
value. The range is 2 to 3600 seconds.
Default 260 seconds
Format set mld groupmembership-interval vlan-id seconds
Mode Interface Config
Global Config
VLAN Mode
no set groupmembership-interval
Use this command to set the MLDv2 group membership Interval time to the default value.
Format no set mld groupmembership-interval
Mode Interface Config
Global Config
VLAN Mode
set mld maxresponse
Use this command to set the MLD maximum response time for the system, on a particular
interface or VLAN. The maximum response time is the amount of time in seconds that a
switch will wait after sending a query on an interface because it did not receive a report for a
particular group in that interface. This value must be less than the MLD query interval time
value. The range is 1 to 65 seconds.
Switching Commands 591

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default 10 seconds
Format set mld maxresponse seconds
Mode Global Config
Interface Config
VLAN Mode
no set mld maxresponse
Use this command to set the max response time (on the interface or VLAN) to the default
value.
Format no set mld maxresponse
Mode Global Config
Interface Config
VLAN Mode
set mld mcrtexpiretime
Use this command to set the multicast router present expiration time. The time is set for the
system, on a particular interface or VLAN. This is the amount of time in seconds that a switch
waits for a query to be received on an interface before the interface is removed from the list of
interfaces with multicast routers attached. The range is 0 to 3600 seconds. A value of 0
indicates an infinite time-out, that is, no expiration.
Default 0
Format set mld mcrtexpiretime vlan-id seconds
Mode Global Config
Interface Config
no set mld mcrtexpiretime
Use this command to set the multicast router present expiration time to 0. The time is set for
the system, on a particular interface or a VLAN.
Format no set mld mcrtexpiretime vlan-id
Mode Global Config
Interface Config
Switching Commands 592

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
set mld mrouter
Use this command to configure the VLAN ID for the VLAN that has the multicast router
attached mode enabled.
Format set mld mrouter vlan-id
Mode Interface Config
no set mld mrouter
Use this command to disable multicast router attached mode for a VLAN with a particular
VLAN ID.
Format no set mld mrouter vlan-id
Mode Interface Config
set mld mrouter interface
Use this command to configure the interface as a multicast router-attached interface. When
configured as a multicast router interface, the interface is treated as a multicast
router-attached interface in all VLANs.
Default disabled
Format set mld mrouter interface
Mode Interface Config
no set mld mrouter interface
Use this command to disable the status of the interface as a statically configured multicast
router-attached interface.
Format no set mld mrouter interface
Mode Interface Config
set mld exclude-mrouter-intf
Use this command to control whether unknown multicast data is sent to an mrouter interface.
If either IGMP Snooping or MLD Snooping is enabled on a VLAN, by default, dynamic
mrouter mode is enabled on the interface that receives MLD PDUs from the upstream router.
When the mrouter mode is enabled on the interface, unknown multicast data is sent to that
interface.
If you enter the command, the switch blocks all unknown multicast data through the mrouter
port, whether the port is configured dynamically or statically. Only MLD PDUs are allowed to
pass through the mrouter port to the upstream router interface.
Switching Commands 593

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Enter the command in Global Config mode to globally apply the setting to all interfaces.
Enter the command in VLAN Config mode to apply the setting at interface level.
For the VLAN configuration to take effect, you must first enter the set mld
exclude-mrouter-intf command and then enter the same command for a specific
VLAN.
Default Enabled
Format set mld exclude-mrouter-intf [vlan-id]
Mode Global Config
VLAN Config
no set mld exclude-mrouter-intf
Use this command to let the switch pass unknown multicast data to an mrouter interface.
Enter the command in Global Config mode to globally apply the setting to all interfaces.
Enter the command in VLAN Config mode to apply the setting at interface level.
Format no set mld exclude-mrouter-intf [vlan-id]
Mode Global Config
VLAN Config
set mld-plus
This command enables both of the following global MLD Snooping configuration commands:
• set mld
• set mld exclude-mrouter-intf
Default Enabled
Format set mld-plus
Mode Global Config
no set mld-plus
This command disables both of the following global MLD Snooping configuration commands:
• set mld
• set mld exclude-mrouter-intf
Format no set mld-plus
Mode Global Config
Switching Commands 594

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
set mld-plus vlan
After you enable the set mld-plus command, you can enable the set mld-plus vlan
command to enable all of the following global MLD Snooping configuration commands at the
VLAN level for a particular VLAN:
• set mld vlan
• set mld exclude-mrouter-intf vlan
• set mld fast-leave vlan
The vlan argument in the set mld-plus vlan command can be a VLAN from 1 to 4093.
Default Enabled for VLAN 1
Format set mld-plus vlan
Mode VLAN Config
no set mld-plus vlan
This command disables all of the following global MLD Snooping configuration commands at
the VLAN level for a particular VLAN:
• set mld vlan
• set mld exclude-mrouter-intf vlan
• set mld fast-leave vlan
The vlan argument in the no set mld-plus vlan command can be a VLAN from 1 to
4093.
Format no set mld-plus vlan
Mode VLAN Config
show mldsnooping
Use this command to display MLD Snooping information. Configured information is displayed
whether or not MLD Snooping is enabled.
Format show mldsnooping [unit/slot/port | vlan-id]
Mode Privileged EXEC
When the optional arguments unit/slot/port or vlan-id are not used, the command
displays the following information.
Term Definition
Admin Mode Indicates whether or not MLD Snooping is active on the switch.
Interfaces Enabled Interfaces on which MLD Snooping is enabled.
for MLD Snooping
Switching Commands 595

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

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show mac-address-table mldsnooping
Use this command to display the MLD Snooping entries in the Multicast Forwarding
Database (MFDB) table.
Format show mac-address-table mldsnooping
Mode Privileged EXEC
Term Definition
VLAN ID The VLAN in which the MAC address is learned.
MAC Address A multicast MAC address for which the switch has forwarding or filtering information. The format is 6
two-digit hexadecimal numbers that are separated by colons, for example 01:23:45:67:89:AB.
Type The type of entry, which is either static (added by the user) or dynamic (added to the table as a result
of a learning process or protocol.)
Description The text description of this multicast table entry.
Interfaces The list of interfaces that are designated for forwarding (Fwd:) and filtering (Flt:).
clear mldsnooping
Use this command to delete all MLD snooping entries from the MFDB table.
Format clear mldsnooping
Mode Privileged EXEC
MLD Snooping Querier Commands
In an IPv6 environment, MLD Snooping requires that one central switch or router periodically
query all end-devices on the network to announce their multicast memberships. This central
device is the MLD Querier. The MLD query responses, known as MLD reports, keep the
switch updated with the current multicast group membership on a port-by-port basis. If the
switch does not receive updated membership information in a timely fashion, it will stop
forwarding multicasts to the port where the end device is located.
This section describes the commands you use to configure and display information on MLD
Snooping queries on the network and, separately, on VLANs.
Switching Commands 599

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: This note clarifies the prioritization of MGMD Snooping
Configurations. Many of the IGMP/MLD Snooping commands are
available both in the Interface and VLAN modes. Operationally the
system chooses or prefers the VLAN configured values over the
Interface configured values for most configurations when the interface
participates in the VLAN.
set mld querier
Use this command to enable MLD Snooping Querier on the system (Global Config Mode) or
on a VLAN. Using this command, you can specify the IP address that the snooping querier
switch should use as a source address while generating periodic queries.
If a VLAN has MLD Snooping Querier enabled and MLD Snooping is operationally disabled
on it, MLD Snooping Querier functionality is disabled on that VLAN. MLD Snooping
functionality is re-enabled if MLD Snooping is operational on the VLAN.
The MLD Snooping Querier sends periodic general queries on the VLAN to solicit
membership reports.
Default disabled
Format set mld querier [vlan-id] [address ipv6-address]
Mode Global Config
VLAN Mode
no set mld querier
Use this command to disable MLD Snooping Querier on the system. Use the optional
parameter address to reset the querier address.
Format no set mld querier [vlan-id] [address]
Mode Global Config
VLAN Mode
set mld querier query_interval
Use this command to set the MLD querier query interval time. It is the time in seconds, from
1–1800 seconds, that the switch waits before sending another general query.
Default disabled
Format set mld querier query_interval seconds
Mode Global Config
Switching Commands 600

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no set mld querier query_interval
Use this command to set the MLD Querier Query Interval time to its default value.
Format no set mld querier query-interval
Mode Global Config
set mld querier timer expiry
Use this command to set the MLD querier timer expiration period. It is the period in seconds,
from 60–300 seconds, that the switch remains in non-querier mode after it has discovered a
multicast querier in the network.
Default 60 seconds
Format set mld querier timer expiry seconds
Mode Global Config
no set mld querier timer expiry
Use this command to set the MLD querier timer expiration period to its default value.
Format no set mld querier timer expiry
Mode Global Config
set mld querier election participate
Use this command to enable the Snooping Querier to participate in the Querier Election
process when it discovers the presence of another Querier in the VLAN. When this mode is
enabled, if the Snooping Querier finds that the other Querier’s source address is better (less)
than the Snooping Querier’s address, it stops sending periodic queries. If the Snooping
Querier wins the election, then it will continue sending periodic queries.
Default disabled
Format set mld querier election participate
Mode VLAN Config
no set mld querier election participate
Use this command to set the snooping querier not to participate in querier election but go into
a non-querier mode as soon as it discovers the presence of another querier in the same
VLAN.
Format no set mld querier election participate
Mode VLAN Config
Switching Commands 601

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show mldsnooping querier
Use this command to display MLD Snooping Querier information. Configured information is
displayed whether or not MLD Snooping Querier is enabled.
Format show mldsnooping querier [detail | vlan vlan-id]
Mode Privileged EXEC
When you do not specify a value for vlan-id, the command displays the following
information.
Field Description
Admin Mode Indicates whether or not MLD Snooping Querier is active on the switch.
Admin Version Indicates the version of MLD that will be used while sending out the queries. This is defaulted to
MLD v1 and it cannot be changed.
Querier Address Shows the IP address which will be used in the IPv6 header while sending out MLD queries. It can
be configured using the appropriate command.
Query Interval Shows the amount of time in seconds that a Snooping Querier waits before sending out the periodic
general query.
Querier Timeout Displays the amount of time to wait in the Non-Querier operational state before moving to a Querier
state.
When you specify a value for vlan-id, the following information displays.
Field Description
VLAN Admin Mode Indicates whether MLD Snooping Querier is active on the VLAN.
VLAN Operational Indicates whether MLD Snooping Querier is in “Querier” or “Non-Querier” state. When the switch is
State in Querier state, it will send out periodic general queries. When in Non-Querier state, it will wait for
moving to Querier state and does not send out any queries.
VLAN Operational Indicates the time to wait before removing a Leave from a host upon receiving a Leave request. This
Max Response value is calculated dynamically from the Queries received from the network. If the Snooping Switch
Time is in Querier state, then it is equal to the configured value.
Querier Election Indicates whether the MLD Snooping Querier participates in querier election if it discovers the
Participate presence of a querier in the VLAN.
Querier VLAN The IP address will be used in the IPv6 header while sending out MLD queries on this VLAN. It can
Address be configured using the appropriate command.
Operational This version of IPv6 will be used while sending out MLD queriers on this VLAN.
Version
Last Querier Indicates the IP address of the most recent Querier from which a Query was received.
Address
Last Querier Indicates the MLD version of the most recent Querier from which a Query was received on this
Version VLAN.
Switching Commands 602

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
When the optional detail keyword is used, the command shows the global information and
the information for all Querier-enabled VLANs.
set mld proxy-querier
If a non-querier switch receives an MLD leave message, the non-querier switch can send
queries with 0::0 as the source IP addresses. This command enables the switch to send such
proxy queries through different command modes the following ways:
• in Global Config mode, on the entire switch
• in Interface Config mode, on an interface
• in VLAN Config mode, on a particular VLAN and all interfaces participating in the VLAN.
By default, the proxy-querier is enabled.
Default enabled
Format set mld proxy-querier [vlan-id]
Mode Global Config
Interface Config
VLAN Config
no set mld proxy-querier
This command stops the switch from sending proxy queries through different command
modes in the following ways:
• in Global Config mode, on the entire switch
• in Interface Config mode, on an interface
• in VLAN Config mode, on a particular VLAN and all interfaces participating in the VLAN.
This command is specific to MLD.
Format no set mld proxy-querier [vlan-id]
Mode Global Config
Interface Config
VLAN Config
show mldsnooping proxy-querier
This command shows the global admin mode of the MLD snooping proxy-querier and the
interface on which it is enabled.
Format show mldsnooping proxy-querier
Mode Privileged EXEC
Switching Commands 603

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(Netgear Switch) #show mldsnooping proxy-querier
Admin Mode..................................... Enable
Interfaces Enabled for MLD Proxy Querier....... 1/0/1
1/0/2
1/0/3
Port Security Commands
This section describes the command you use to configure Port Security on the switch. Port
security, which is also known as port MAC locking, allows you to secure the network by
locking allowable MAC addresses on a given port. Packets with a matching source MAC
address are forwarded normally, and all other packets are discarded.
Note: To enable the SNMP trap specific to port security, see snmp-server
enable traps violation on page133.
port-security
This command enables port locking on an interface, a range of interfaces, or at the system
level.
Default disabled
Format port-security
Mode Global Config (to enable port locking globally)
Interface Config (to enable port locking on an interface or range of interfaces)
no port-security
This command disables port locking for one (Interface Config) or all (Global Config) ports.
Format no port-security
Mode Global Config
Interface Config
Switching Commands 604

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
port-security max-dynamic
This command sets the maximum number of dynamically locked MAC addresses allowed on
a specific port. The valid range is 0–4096.
Default 4096
Format port-security max-dynamic maxvalue
Mode Interface Config
no port-security max-dynamic
This command resets the maximum number of dynamically locked MAC addresses allowed
on a specific port to its default value.
Format no port-security max-dynamic
Mode Interface Config
port-security max-static
This command sets the maximum number of statically locked MAC addresses allowed on a
port. The valid range is 0–20.
Default 1
Format port-security max-static maxvalue
Mode Interface Config
no port-security max-static
This command sets maximum number of statically locked MAC addresses to the default
value.
Format no port-security max-static
Mode Interface Config
port-security mac-address
This command adds a MAC address to the list of statically locked MAC addresses for an
interface or range of interfaces. The vid is the VLAN ID.
Format port-security mac-address mac-address vid
Mode Interface Config
Switching Commands 605

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no port-security mac-address
This command removes a MAC address from the list of statically locked MAC addresses.
Format no port-security mac-address mac-address vid
Mode Interface Config
port-security mac-address move
This command converts dynamically locked MAC addresses to statically locked addresses
for an interface or range of interfaces.
Format port-security mac-address move
Mode Interface Config
port-security mac-address sticky
This command enables sticky mode Port MAC Locking on a port. If accompanied by a MAC
address and a VLAN id (for interface config mode only), it adds a sticky MAC address to the
list of statically locked MAC addresses. These sticky addresses are converted back to
dynamically locked addresses if sticky mode is disabled on the port. The vid is the VLAN ID.
The Global command applies the sticky mode to all valid interfaces (physical and LAG).
There is no global sticky mode as such.
Sticky addresses that are dynamically learned display in the output of the show
running-config command as port-security mac-address sticky mac vid entries.
This distinguishes them from static entries.
Format port-security mac-address sticky [mac-address vid]
Mode Global Config
Interface Config
Command example:
(NETGEAR)(Config)# port-security mac-address sticky
(NETGEAR)(Interface)# port-security mac-address sticky
(NETGEAR)(Interface)# port-security mac-address sticky
00:00:00:00:00:01 2
no port-security mac-address sticky
Use this command to disable the sticky mode.
Format no port-security mac-address sticky [mac-address vid]
Mode Global Config
Interface Config
Switching Commands 606

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
port-security violation shutdown
This command allows an interface to be diagnostically disabled when a violation occurs for
port MAC locking.
Format port-security violation shutdown
Mode Interface Config
no port-security violation shutdown
This command prevents an interface from being diagnostically disabled when a violation
occurs for port MAC locking.
Format no port-security violation shutdown
Mode Interface Config
show port-security
This command displays the port-security settings for the port or ports. If you do not use a
parameter, the command displays the Port Security Administrative mode. Use the optional
parameters to display the settings on a specific interface or on all interfaces. Instead of
unit/slot/port, lag lag-intf-num can be used as an alternate way to specify the
LAG interface, in which lag-intf-num is the LAG port number.
Format show port-security [unit/slot/port | all]
Mode Privileged EXEC
Term Definition
Admin Mode Port Locking mode for the entire system. This field displays if you do not supply any parameters.
For each interface, or for the interface you specify, the following information displays.
Term Definition
Admin Mode Port Locking mode for the Interface.
Dynamic Limit Maximum dynamically allocated MAC Addresses.
Static Limit Maximum statically allocated MAC Addresses.
Violation Trap Whether violation traps are enabled.
Mode
Sticky Mode The administrative mode of the port security Sticky Mode feature on the interface.
Switching Commands 607

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show port-security 0/1
Admin Dynamic Static Violation Sticky
Intf Mode Limit Limit Trap Mode Mode
------ ------- ---------- --------- --------- --------
0 /1 Disabled 1 1 Disabled Enabled
show port-security dynamic
This command displays the dynamically locked MAC addresses for the port. Instead of
unit/slot/port, lag lag-intf-num can be used as an alternate way to specify the
LAG interface, in which lag-intf-num is the LAG port number.
Format show port-security dynamic unit/slot/port
Mode Privileged EXEC
Term Definition
MAC Address MAC Address of dynamically locked MAC.
show port-security static
This command displays the statically locked MAC addresses for a port. Instead of
unit/slot/port, lag lag-intf-num can be used as an alternate way to specify the
LAG interface, in which lag-intf-num is the LAG port number.
Format show port-security static {unit/slot/port | lag lag-intf-num}
Mode Privileged EXEC
Term Definition
Statically Configured MAC The statically configured MAC address.
Address
VLAN ID The ID of the VLAN that includes the host with the specified MAC address.
Sticky Indicates whether the static MAC address entry is added in sticky mode.
Command example:
(NETGEAR Switch) #show port-security static 1/0/1
Number of static MAC addresses configured: 2
Statically configured MAC Address VLAN ID Sticky
--------------------------------- ------- ------
00:00:00:00:00:01 2 Yes
00:00:00:00:00:02 2 No
Switching Commands 608

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show port-security violation
This command displays the source MAC address of the last packet discarded on a locked
port. Instead of unit/slot/port, lag lag-intf-num can be used as an alternate way to
specify the LAG interface, in which lag-intf-num is the LAG port number.
Format show port-security violation {unit/slot/port | lag lag-intf-num}
Mode Privileged EXEC
Term Definition
MAC Address The source MAC address of the last frame that was discarded at a locked port.
VLAN ID The VLAN ID, if applicable, associated with the MAC address of the last frame that was discarded at
a locked port.
LLDP (802.1AB) Commands
This section describes the command you use to configure Link Layer Discovery Protocol
(LLDP), which is defined in the IEEE 802.1AB specification. LLDP allows stations on an 802
LAN to advertise major capabilities and physical descriptions. The advertisements allow a
network management system (NMS) to access and display this information.
lldp transmit
Use this command to enable the LLDP advertise capability on an interface or a range of
interfaces.
Default disabled
Format lldp transmit
Mode Interface Config
no lldp transmit
Use this command to return the local data transmission capability to the default.
Format no lldp transmit
Mode Interface Config
Switching Commands 609

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
lldp receive
Use this command to enable the LLDP receive capability on an interface or a range of
interfaces.
Default disabled
Format lldp receive
Mode Interface Config
no lldp receive
Use this command to return the reception of LLDPDUs to the default value.
Format no lldp receive
Mode Interface Config
lldp timers
Use this command to set the timing parameters for local data transmission on ports enabled
for LLDP. The interval-seconds determines the number of seconds to wait between
transmitting local data LLDPDUs. The range is 1–32768 seconds. The hold-value is the
multiplier on the transmit interval that sets the TTL in local data LLDPDUs. The multiplier
range is 2–10. The reinit-seconds is the delay before reinitialization, and the range is
1–0 seconds.
Default interval—30 seconds
hold—4
reinit—2 seconds
Format lldp timers [interval interval-seconds] [hold hold-value] [reinit
reinit-seconds]
Mode Global Config
no lldp timers
Use this command to return any or all timing parameters for local data transmission on ports
enabled for LLDP to the default values.
Format no lldp timers [interval] [hold] [reinit]
Mode Global Config
lldp transmit-tlv
Use this command to specify which optional type length values (TLVs) in the 802.1AB basic
management set are transmitted in the LLDPDUs from an interface or range of interfaces.
Use sys-name to transmit the system name TLV.
Switching Commands 610

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
To configure the system name, see snmp-server on page129. Use sys-desc to transmit
the system description TLV. Use sys-cap to transmit the system capabilities TLV. Use
port-desc to transmit the port description TLV. To configure the port description, see
description (Interface Config) on page373
Default no optional TLVs are included
Format lldp transmit-tlv [sys-desc] [sys-name] [sys-cap] [port-desc]
Mode Interface Config
no lldp transmit-tlv
Use this command to remove an optional TLV from the LLDPDUs. Use the command without
parameters to remove all optional TLVs from the LLDPDU.
Format no lldp transmit-tlv [sys-desc] [sys-name] [sys-cap] [port-desc]
Mode Interface Config
lldp transmit-mgmt
Use this command to include transmission of the local system management address
information in the LLDPDUs. This command can be used to configure a single interface or a
range of interfaces.
Format lldp transmit-mgmt
Mode Interface Config
no lldp transmit-mgmt
Use this command to include transmission of the local system management address
information in the LLDPDUs. Use this command to cancel inclusion of the management
information in LLDPDUs.
Format no lldp transmit-mgmt
Mode Interface Config
lldp notification
Use this command to enable remote data change notifications on an interface or a range of
interfaces.
Default disabled
Format lldp notification
Mode Interface Config
Switching Commands 611

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no lldp notification
Use this command to disable notifications.
Default disabled
Format no lldp notification
Mode Interface Config
lldp notification-interval
Use this command to configure how frequently the system sends remote data change
notifications. The interval parameter is the number of seconds to wait between sending
notifications. The valid interval range is 5–3600 seconds.
Default 5
Format lldp notification-interval interval
Mode Global Config
no lldp notification-interval
Use this command to return the notification interval to the default value.
Format no lldp notification-interval
Mode Global Config
clear lldp statistics
Use this command to reset all LLDP statistics, including MED-related information.
Format clear lldp statistics
Mode Privileged Exec
clear lldp remote-data
Use this command to delete all information from the LLDP remote data table, including
MED-related information.
Format clear lldp remote-data
Mode Global Config
Switching Commands 612

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show lldp
Use this command to display a summary of the current LLDP configuration.
Format show lldp
Mode Privileged Exec
Term Definition
Transmit Interval How frequently the system transmits local data LLDPDUs, in seconds.
Transmit Hold The multiplier on the transmit interval that sets the TTL in local data LLDPDUs.
Multiplier
Re-initialization The delay before reinitialization, in seconds.
Delay
Notification Interval How frequently the system sends remote data change notifications, in seconds.
show lldp interface
Use this command to display a summary of the current LLDP configuration for a specific
interface or for all interfaces.
Format show lldp interface {unit/slot/port | all}
Mode Privileged Exec
Term Definition
Interface The interface in a unit/slot/port format.
Link Shows whether the link is up or down.
Transmit Shows whether the interface transmits LLDPDUs.
Receive Shows whether the interface receives LLDPDUs.
Notify Shows whether the interface sends remote data change notifications.
TLVs Shows whether the interface sends optional TLVs in the LLDPDUs. The TLV codes can be 0 (Port
Description), 1 (System Name), 2 (System Description), or 3 (System Capability).
Mgmt Shows whether the interface transmits system management address information in the LLDPDUs.
show lldp statistics
Use this command to display the current LLDP traffic and remote table statistics for a specific
interface or for all interfaces.
Format show lldp statistics {unit/slot/port | all}
Mode Privileged Exec
Switching Commands 613

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Last Update The amount of time since the last update to the remote table in days, hours, minutes, and seconds.
Total Inserts Total number of inserts to the remote data table.
Total Deletes Total number of deletes from the remote data table.
Total Drops Total number of times the complete remote data received was not inserted due to insufficient
resources.
Total Ageouts Total number of times a complete remote data entry was deleted because the Time to Live interval
expired.
The table contains the following column headings.
Term Definition
Interface The interface in unit/slot/port format.
TX Total Total number of LLDP packets transmitted on the port.
RX Total Total number of LLDP packets received on the port.
Discards Total number of LLDP frames discarded on the port for any reason.
Errors The number of invalid LLDP frames received on the port.
Ageouts Total number of times a complete remote data entry was deleted for the port because the Time to
Live interval expired.
TVL Discards The number of TLVs discarded.
TVL Unknowns Total number of LLDP TLVs received on the port where the type value is in the reserved range, and
not recognized.
TLV MED The total number of LLDP-MED TLVs received on the interface.
TLV 802.1 The total number of LLDP TLVs received on the interface which are of type 802.1.
TLV 802.3 The total number of LLDP TLVs received on the interface which are of type 802.3.
show lldp remote-device
Use this command to display summary information about remote devices that transmit
current LLDP data to the system. You can show information about LLDP remote data
received on all ports or on a specific port.
Format show lldp remote-device {unit/slot/port | all}
Mode Privileged EXEC
Switching Commands 614

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Local Interface The interface that received the LLDPDU from the remote device.
RemID An internal identifier to the switch to mark each remote device to the system.
Chassis ID The ID that is sent by a remote device as part of the LLDP message, it is usually a MAC address of
the device.
Port ID The port number that transmitted the LLDPDU.
System Name The system name of the remote device.
Command example:
(NETGEAR switch) #show lldp remote-device all
LLDP Remote Device Summary
Local
Interface RemID Chassis ID Port ID System Name
------- ------- -------------------- ------------------ ------------------
0/1
0/2
0/3
0/4
0/5
0/6
0/7 2 00:FC:E3:90:01:0F 00:FC:E3:90:01:11
0/7 3 00:FC:E3:90:01:0F 00:FC:E3:90:01:12
0/7 4 00:FC:E3:90:01:0F 00:FC:E3:90:01:13
0/7 5 00:FC:E3:90:01:0F 00:FC:E3:90:01:14
0/7 1 00:FC:E3:90:01:0F 00:FC:E3:90:03:11
0/7 6 00:FC:E3:90:01:0F 00:FC:E3:90:04:11
0/8
0/9
0/10
0/11
0/12
show lldp remote-device detail
Use this command to display detailed information about remote devices that transmit current
LLDP data to an interface on the system.
Format show lldp remote-device detail unit/slot/port
Mode Privileged EXEC
Switching Commands 615

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Local Interface The interface that received the LLDPDU from the remote device.
Remote Identifier An internal identifier to the switch to mark each remote device to the system.
Chassis ID The type of identification used in the Chassis ID field.
Subtype
Chassis ID The chassis of the remote device.
Port ID Subtype The type of port on the remote device.
Port ID The port number that transmitted the LLDPDU.
System Name The system name of the remote device.
System Description Describes the remote system by identifying the system name and versions of hardware, operating
system, and networking software supported in the device.
Port Description Describes the port in an alpha-numeric format. The port description is configurable.
System Indicates the primary function(s) of the device.
Capabilities
Supported
System Shows which of the supported system capabilities are enabled.
Capabilities
Enabled
Management For each interface on the remote device with an LLDP agent, lists the type of address the remote
Address LLDP agent uses and specifies the address used to obtain information related to the device.
Time To Live The amount of time (in seconds) the remote device's information received in the LLDPDU should be
treated as valid information.
Command example:
(NETGEAR switch) #show lldp remote-device detail 0/7
LLDP Remote Device Detail
Local Interface: 0/7
Remote Identifier: 2
Chassis ID Subtype: MAC Address
Chassis ID: 00:FC:E3:90:01:0F
Port ID Subtype: MAC Address
Port ID: 00:FC:E3:90:01:11
System Name:
System Description:
Port Description:
System Capabilities Supported:
System Capabilities Enabled:
Time to Live: 24 seconds
Switching Commands 616

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show lldp local-device
Use this command to display summary information about the advertised LLDP local data.
This command can display summary information or detail for each interface.
Format show lldp local-device {unit/slot/port | all}
Mode Privileged EXEC
Term Definition
Interface The interface in a unit/slot/port format.
Port ID The port ID associated with this interface.
Port Description The port description associated with the interface.
show lldp local-device detail
Use this command to display detailed information about the LLDP data a specific interface
transmits.
Format show lldp local-device detail unit/slot/port
Mode Privileged EXEC
Term Definition
Interface The interface that sends the LLDPDU.
Chassis ID The type of identification used in the Chassis ID field.
Subtype
Chassis ID The chassis of the local device.
Port ID Subtype The type of port on the local device.
Port ID The port number that transmitted the LLDPDU.
System Name The system name of the local device.
System Description Describes the local system by identifying the system name and versions of hardware, operating
system, and networking software supported in the device.
Port Description Describes the port in an alpha-numeric format.
System Indicates the primary function(s) of the device.
Capabilities
Supported
System Shows which of the supported system capabilities are enabled.
Capabilities
Enabled
Management The type of address and the specific address the local LLDP agent uses to send and receive
Address information.
Switching Commands 617

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
LLDP-MED Commands
Link Layer Discovery Protocol - Media Endpoint Discovery (LLDP-MED) (ANSI-TIA-1057)
provides an extension to the LLDP standard. Specifically, LLDP-MED provides extensions for
network configuration and policy, device location, Power over Ethernet (PoE) management
and inventory management.
lldp med
Use this command to enable MED on an interface or a range of interfaces. By enabling MED,
you will be effectively enabling the transmit and receive function of LLDP.
Default disabled
Format lldp med
Mode Interface Config
no lldp med
Use this command to disable MED.
Format no lldp med
Mode Interface Config
lldp med confignotification
Use this command to configure an interface or a range of interfaces to send the topology
change notification.
Default disabled
Format lldp med confignotification
Mode Interface Config
no ldp med confignotification
Use this command to disable notifications.
Format no lldp med confignotification
Mode Interface Config
Switching Commands 618

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
lldp med transmit-tlv
Use this command to specify which optional Type Length Values (TLVs) in the LLDP MED
set will be transmitted in the Link Layer Discovery Protocol Data Units (LLDPDUs) from this
interface or a range of interfaces.
Default By default, the capabilities and network policy TLVs are included.
Format lldp med transmit-tlv [capabilities] [ex-pd] [ex-pse] [inventory] [location]
[network-policy]
Mode Interface Config
Parameter Definition
capabilities Transmit the LLDP capabilities TLV.
ex-pd Transmit the LLDP extended PD TLV.
ex-pse Transmit the LLDP extended PSE TLV.
inventory Transmit the LLDP inventory TLV.
location Transmit the LLDP location TLV.
network-policy Transmit the LLDP network policy TLV.
no lldp med transmit-tlv
Use this command to remove a TLV.
Format no lldp med transmit-tlv [capabilities] [network-policy] [ex-pse] [ex-pd]
[location] [inventory]
Mode Interface Config
lldp med all
Use this command to configure LLDP-MED on all the ports.
Format lldp med all
Mode Global Config
lldp med confignotification all
Use this command to configure all the ports to send the topology change notification.
Format lldp med confignotification all
Mode Global Config
Switching Commands 619

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
lldp med faststartrepeatcount
Use this command to set the value of the fast start repeat count. count is the number of
LLDP PDUs that are transmitted when the product is enabled. The range is 1 to 10.
Default 3
Format lldp med faststartrepeatcount [count]
Mode Global Config
no lldp med faststartrepeatcount
Use this command to return to the factory default value.
Format no lldp med faststartrepeatcount
Mode Global Config
lldp med transmit-tlv all
Use this command to specify which optional Type Length Values (TLVs) in the LLDP MED
set will be transmitted in the Link Layer Discovery Protocol Data Units (LLDPDUs).
Default By default, the capabilities and network policy TLVs are included.
Format lldp med transmit-tlv all [capabilities] [ex-pd] [ex-pse] [inventory]
[location] [network-policy]
Mode Global Config
Term Definition
capabilities Transmit the LLDP capabilities TLV.
ex-pd Transmit the LLDP extended PD TLV.
ex-pse Transmit the LLDP extended PSE TLV.
inventory Transmit the LLDP inventory TLV.
location Transmit the LLDP location TLV.
network-policy Transmit the LLDP network policy TLV.
no lldp med transmit-tlv
Use this command to remove a TLV.
Format no lldp med transmit-tlv [capabilities] [network-policy] [ex-pse] [ex-pd]
[location] [inventory]
Mode Global Config
Switching Commands 620

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show lldp med
Use this command to display a summary of the current LLDP MED configuration.
Format show lldp med
Mode Privileged Exec
Command example:
(NETGEAR Switch) #show lldp med
LLDP MED Global Configuration
Fast Start Repeat Count: 3
Device Class: Network Connectivity
(NETGEAR Switch) #
show lldp med interface
Use this command to display a summary of the current LLDP MED configuration for a
specific interface. unit/slot/port indicates a specific physical interface; all indicates all
valid LLDP interfaces.
Format show lldp med interface {unit/slot/port | all}
Mode Privileged Exec
Command example:
(NETGEAR Switch) #show lldp med interface all
Interface Link configMED operMED ConfigNotify TLVsTx
--------- ------ --------- -------- ------------ -----------
1/0/1 Down Disabled Disabled Disabled 0,1
1/0/2 Up Disabled Disabled Disabled 0,1
1/0/3 Down Disabled Disabled Disabled 0,1
1/0/4 Down Disabled Disabled Disabled 0,1
1/0/5 Down Disabled Disabled Disabled 0,1
1/0/6 Down Disabled Disabled Disabled 0,1
1/0/7 Down Disabled Disabled Disabled 0,1
1/0/8 Down Disabled Disabled Disabled 0,1
1/0/9 Down Disabled Disabled Disabled 0,1
1/0/10 Down Disabled Disabled Disabled 0,1
1/0/11 Down Disabled Disabled Disabled 0,1
1/0/12 Down Disabled Disabled Disabled 0,1
1/0/13 Down Disabled Disabled Disabled 0,1
1/0/14 Down Disabled Disabled Disabled 0,1
Switching Commands 621

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
TLV Codes: 0- Capabilities, 1- Network Policy
2- Location, 3- Extended PSE
4- Extended Pd, 5- Inventory
--More-- or (q)uit
(NETGEAR Switch) #show lldp med interface 1/0/2
Interface Link configMED operMED ConfigNotify TLVsTx
--------- ------ --------- -------- ------------ -----------
1/0/2 Up Disabled Disabled Disabled 0,1
TLV Codes: 0- Capabilities, 1- Network Policy
2- Location, 3- Extended PSE
4- Extended Pd, 5- Inventory
show lldp med local-device detail
Use this command to display detailed information about the LLDP MED data that a specific
interface transmits. unit/slot/port indicates a specific physical interface.
Format show lldp med local-device detail unit/slot/port
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show lldp med local-device detail 1/0/8
LLDP MED Local Device Detail
Interface: 1/0/8
Network Policies
Media Policy Application Type : voice
Vlan ID: 10
Priority: 5
DSCP: 1
Unknown: False
Tagged: True
Media Policy Application Type : streamingvideo
Vlan ID: 20
Priority: 1
DSCP: 2
Unknown: False
Tagged: True
Switching Commands 622

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Inventory
Hardware Rev: xxx xxx xxx
Firmware Rev: xxx xxx xxx
Software Rev: xxx xxx xxx
Serial Num: xxx xxx xxx
Mfg Name: xxx xxx xxx
Model Name: xxx xxx xxx
Asset ID: xxx xxx xxx
Location
Subtype: elin
Info: xxx xxx xxx
Extended POE
Device Type: pseDevice
Extended POE PSE
Available: 0.3 Watts
Source: primary
Priority: critical
Extended POE PD
Required: 0.2 Watts
Source: local
Priority: low
show lldp med remote-device
Use this command to display the summary information about remote devices that transmit
current LLDP MED data to the system. You can show information about LLDP MED remote
data received on all valid LLDP interfaces or on a specific physical interface.
Format show lldp med remote-device {unit/slot/port | all}
Mode Privileged EXEC
Term Definition
Local Interface The interface that received the LLDPDU from the remote device.
Remote ID An internal identifier to the switch to mark each remote device to the system.
Device Class Device classification of the remote device.
Switching Commands 623

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show lldp med remote-device all
LLDP MED Remote Device Summary
Local
Interface Remote ID Device Class
--------- --------- ------------
1/0/8 1 Class I
1 /0/9 2 Not Defined
1 /0/10 3 Class II
1/0/11 4 Class III
1/0/12 5 Network Con
show lldp med remote-device detail
Use this command to display detailed information about remote devices that transmit current
LLDP MED data to an interface on the system.
Format show lldp med remote-device detail unit/slot/port
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show lldp med remote-device detail 1/0/8
LLDP MED Remote Device Detail
Local Interface: 1/0/8
Remote Identifier: 18
Capabilities
MED Capabilities Supported: capabilities, networkpolicy, location, extendedpse
MED Capabilities Enabled: capabilities, networkpolicy
Device Class: Endpoint Class I
Network Policies
Media Policy Application Type : voice
Vlan ID: 10
Priority: 5
DSCP: 1
Unknown: False
Tagged: True
Media Policy Application Type : streamingvideo
Vlan ID: 20
Priority: 1
Switching Commands 624

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
DSCP: 2
Unknown: False
Tagged: True
Inventory
Hardware Rev: xxx xxx xxx
Firmware Rev: xxx xxx xxx
Software Rev: xxx xxx xxx
Serial Num: xxx xxx xxx
Mfg Name: xxx xxx xxx
Model Name: xxx xxx xxx
Asset ID: xxx xxx xxx
Location
Subtype: elin
Info: xxx xxx xxx
Extended POE
Device Type: pseDevice
Extended POE PSE
Available: 0.3 Watts
Source: primary
Priority: critical
Extended POE PD
Required: 0.2 Watts
Source: local
Priority: low
Switching Commands 625

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Denial of Service Commands
This section describes the commands you use to configure Denial of Service (DoS) Control.
The switch provides support for classifying and blocking specific types of Denial of Service
attacks. You can configure your system to monitor and block these types of attacks:
• SIP = DIP. Source IP address = Destination IP address.
• First Fragment. TCP Header size smaller then configured value.
• TCP Fragment. Allows the device to drop packets that have a TCP payload where the IP
payload length minus the IP header size is less than the minimum allowed TCP header
size.
• TCP Flag. TCP Flag SYN set and Source Port < 1024 or TCP Control Flags = 0 and TCP
Sequence Number = 0 or TCP Flags FIN, URG, and PSH set and TCP Sequence
Number = 0 or TCP Flags SYN and FIN set.
• L4 Port. Source TCP/UDP Port = Destination TCP/UDP Port.
• ICMP. Limiting the size of ICMP Ping packets.
• SMAC = DMAC. Source MAC address = Destination MAC address.
• TCP Port. Source TCP Port = Destination TCP Port.
• UDP Port. Source UDP Port = Destination UDP Port.
• TCP Flag & Sequence. TCP Flag SYN set and Source Port < 1024 or TCP Control Flags
= 0 and TCP Sequence Number = 0 or TCP Flags FIN, URG, and PSH set and TCP
Sequence Number = 0 or TCP Flags SYN and FIN set.
• TCP Offset. Allows the device to drop packets that have a TCP header Offset set to 1.
• TCP SYN. TCP Flag SYN set.
• TCP SYN & FIN. TCP Flags SYN and FIN set.
• TCP FIN & URG & PSH. TCP Flags FIN and URG and PSH set and TCP Sequence
Number = 0.
• ICMP V6. Limiting the size of ICMPv6 Ping packets.
• ICMP Fragment. Checks for fragmented ICMP packets.
dos-control all
This command enables Denial of Service protection checks globally.
Default disabled
Format dos-control all
Mode Global Config
Switching Commands 626

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dos-control all
This command disables Denial of Service prevention checks globally.
Format no dos-control all
Mode Global Config
dos-control sipdip
This command enables Source IP address = Destination IP address (SIP = DIP) Denial of
Service protection. If the mode is enabled, Denial of Service prevention is active for this type
of attack. If packets ingress with SIP = DIP, the packets will be dropped if the mode is
enabled.
Default disabled
Format dos-control sipdip
Mode Global Config
no dos-control sipdip
This command disables Source IP address = Destination IP address (SIP = DIP) Denial of
Service prevention.
Format no dos-control sipdip
Mode Global Config
dos-control firstfrag
This command enables Minimum TCP Header Size Denial of Service protection. If the mode
is enabled, Denial of Service prevention is active for this type of attack. If packets ingress
having a TCP Header Size smaller then the configured value, the packets will be dropped if
the mode is enabled. The default is disabled. The range is 0–255. If you enable dos-control
firstfrag, but do not provide a Minimum TCP Header Size, the system sets that value to 20.
Default disabled (20)
Format dos-control firstfrag [size]
Mode Global Config
Switching Commands 627

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dos-control firstfrag
This command sets Minimum TCP Header Size Denial of Service protection to the default
value of disabled.
Format no dos-control firstfrag
Mode Global Config
dos-control tcpfrag
This command enables TCP Fragment Denial of Service protection. If the mode is enabled,
Denial of Service prevention is active for this type of attack and packets that have a TCP
payload in which the IP payload length minus the IP header size is less than the minimum
allowed TCP header size are dropped.
Default disabled
Format dos-control tcpfrag
Mode Global Config
no dos-control tcpfrag
This command disables TCP Fragment Denial of Service protection.
Format no dos-control tcpfrag
Mode Global Config
dos-control tcpflag
This command enables TCP Flag Denial of Service protections. If the mode is enabled,
Denial of Service prevention is active for this type of attacks. If packets ingress having TCP
Flag SYN set and a source port less than 1024 or having TCP Control Flags set to 0 and TCP
Sequence Number set to 0 or having TCP Flags FIN, URG, and PSH set and TCP Sequence
Number set to 0 or having TCP Flags SYN and FIN both set, the packets will be dropped if
the mode is enabled.
Default disabled
Format dos-control tcpflag
Mode Global Config
Switching Commands 628

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dos-control tcpflag
This command sets disables TCP Flag Denial of Service protections.
Format no dos-control tcpflag
Mode Global Config
dos-control l4port
This command enables L4 Port Denial of Service protections. If the mode is enabled, Denial
of Service prevention is active for this type of attack. If packets ingress having Source
TCP/UDP Port Number equal to Destination TCP/UDP Port Number, the packets will be
dropped if the mode is enabled.
Note: Some applications mirror source and destination L4 ports - RIP for
example uses 520 for both. If you enable dos-control l4port,
applications such as RIP may experience packet loss which would
render the application inoperable.
Default Disabled
Format dos-control l4port
Mode Global Config
no dos-control l4port
This command disables L4 Port Denial of Service protections.
Format no dos-control l4port
Mode Global Config
dos-control smacdmac
This command enables Source MAC address = Destination MAC address (SMAC = DMAC)
Denial of Service protection. If the mode is enabled, Denial of Service prevention is active for
this type of attack. If packets ingress with SMAC = DMAC, the packets will be dropped if the
mode is enabled.
Default disabled
Format dos-control smacdmac
Mode Global Config
Switching Commands 629

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dos-control smacdmac
This command disables Source MAC address = Destination MAC address (SMAC = DMAC)
DoS protection.
Format no dos-control smacdmac
Mode Global Config
dos-control tcpport
This command enables TCP L4 source = destination port number (Source TCP Port =
Destination TCP Port) Denial of Service protection. If the mode is enabled, Denial of Service
prevention is active for this type of attack. If packets ingress with Source TCP Port =
Destination TCP Port, the packets will be dropped if the mode is enabled.
Default Disabled
Format dos-control tcpport
Mode Global Config
no dos-control tcpport
This command disables TCP L4 source = destination port number (Source TCP Port =
Destination TCP Port) Denial of Service protection.
Format no dos-control tcpport
Mode Global Config
dos-control udpport
This command enables UDP L4 source = destination port number (Source UDP Port =
Destination UDP Port) DoS protection. If the mode is enabled, Denial of Service prevention is
active for this type of attack. If packets ingress with Source UDP Port = Destination UDP Port,
the packets will be dropped if the mode is enabled.
Default Disabled
Format dos-control udpport
Mode Global Config
Switching Commands 630

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dos-control udpport
This command disables UDP L4 source = destination port number (Source UDP Port =
Destination UDP Port) Denial of Service protection.
Format no dos-control udpport
Mode Global Config
dos-control tcpflagseq
This command enables TCP Flag and Sequence Denial of Service protections. If the mode is
enabled, Denial of Service prevention is active for this type of attack. If packets ingress
having TCP Flag SYN set and a source port less than 1024 or having TCP Control Flags set
to 0 and TCP Sequence Number set to 0 or having TCP Flags FIN, URG, and PSH set and
TCP Sequence Number set to 0 or having TCP Flags SYN and FIN both set, the packets will
be dropped if the mode is enabled.
Default Disabled
Format dos-control tcpflagseq
Mode Global Config
no dos-control tcpflagseq
This command sets disables TCP Flag and Sequence Denial of Service protection.
Format no dos-control tcpflagseq
Mode Global Config
dos-control tcpoffset
This command enables TCP Offset Denial of Service protection. If the mode is enabled,
Denial of Service prevention is active for this type of attack. If packets ingress having TCP
Header Offset equal to one (1), the packets will be dropped if the mode is enabled.
Default Disabled
Format dos-control tcpoffset
Mode Global Config
no dos-control tcpoffset
This command disabled TCP Offset Denial of Service protection.
Format no dos-control tcpoffset
Mode Global Config
Switching Commands 631

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
dos-control tcpsyn
This command enables TCP SYN and L4 source = 0-1023 Denial of Service protection. If the
mode is enabled, Denial of Service prevention is active for this type of attack. If packets
ingress having TCP flag SYN set and an L4 source port from 0 to 1023, the packets will be
dropped if the mode is enabled.
Default Disabled
Format dos-control tcpsyn
Mode Global Config
no dos-control tcpsyn
This command sets disables TCP SYN and L4 source = 0-1023 Denial of Service protection.
Format no dos-control tcpsyn
Mode Global Config
dos-control tcpsynfin
This command enables TCP SYN and FIN Denial of Service protection. If the mode is
enabled, Denial of Service prevention is active for this type of attack. If packets ingress
having TCP flags SYN and FIN set, the packets will be dropped if the mode is enabled.
Default Disabled
Format dos-control tcpsynfin
Mode Global Config
no dos-control tcpsynfin
This command sets disables TCP SYN & FIN Denial of Service protection.
Format no dos-control tcpsynfin
Mode Global Config
dos-control tcpfinurgpsh
This command enables TCP FIN and URG and PSH and SEQ = 0 checking Denial of Service
protections. If the mode is enabled, Denial of Service prevention is active for this type of
attack. If packets ingress having TCP FIN, URG, and PSH all set and TCP Sequence
Number set to 0, the packets will be dropped if the mode is enabled.
Switching Commands 632

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default Disabled
Format dos-control tcpfinurgpsh
Mode Global Config
no dos-control tcpfinurgpsh
This command sets disables TCP FIN and URG and PSH and SEQ = 0 checking Denial of
Service protections.
Format no dos-control tcpfinurgpsh
Mode Global Config
dos-control icmpv4
This command enables Maximum ICMPv4 Packet Size Denial of Service protections. If the
mode is enabled, Denial of Service prevention is active for this type of attack. If ICMPv4 Echo
Request (PING) packets ingress with a size greater than the configured value, the packets
are dropped if the mode is enabled. The value for the size is from 0–16376.
Default Disabled (512)
Format dos-control icmpv4 [size]
Mode Global Config
no dos-control icmpv4
This command disables Maximum ICMP Packet Size Denial of Service protections.
Format no dos-control icmpv4
Mode Global Config
dos-control icmpv6
This command enables Maximum ICMPv6 Packet Size Denial of Service protections. If the
mode is enabled, Denial of Service prevention is active for this type of attack. If ICMPv6 Echo
Request (PING) packets ingress having a size greater than the configured value, the packets
will be dropped if the mode is enabled. The value for the size is from 0–16376.
Default Disabled (512)
Format dos-control icmpv6 [size]
Mode Global Config
Switching Commands 633

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dos-control icmpv6
This command disables Maximum ICMP Packet Size Denial of Service protections.
Format no dos-control icmpv6
Mode Global Config
dos-control icmpfrag
This command enables ICMP Fragment Denial of Service protection. If the mode is enabled,
Denial of Service prevention is active for this type of attack. If packets ingress having
fragmented ICMP packets, the packets will be dropped if the mode is enabled.
Default disabled
Format dos-control icmpfrag
Mode Global Config
no dos-control icmpfrag
This command disabled ICMP Fragment Denial of Service protection.
Format no dos-control icmpfrag
Mode Global Config
show dos-control
This command displays Denial of Service configuration information.
Format show dos-control
Mode Privileged EXEC
Term Definition
First Fragment Mode The administrative mode of First Fragment DoS prevention. When enabled, this causes the
switch to drop packets that have a TCP header smaller then the configured Min TCP Hdr
Size.
Min TCP Hdr Size The minimum TCP header size the switch will accept if First Fragment DoS prevention is
enabled.
ICMPv4 Mode The administrative mode of ICMPv4 DoS prevention. When enabled, this causes the switch
to drop ICMP packets that have a type set to ECHO_REQ (ping) and a size greater than the
configured ICMPv4 Payload Size.
Max ICMPv4 Payload Size The maximum ICMPv4 payload size to accept when ICMPv4 DoS protection is enabled.
Switching Commands 634

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
ICMPv6 Mode The administrative mode of ICMPv6 DoS prevention. When enabled, this causes the switch
to drop ICMP packets that have a type set to ECHO_REQ (ping) and a size greater than the
configured ICMPv6 Payload Size.
Max ICMPv6 Payload Size The maximum ICMPv6 payload size to accept when ICMPv6 DoS protection is enabled.
ICMPv4 Fragment Mode The administrative mode of ICMPv4 Fragment DoS prevention. When enabled, this causes
the switch to drop fragmented ICMPv4 packets.
TCP Port Mode The administrative mode of TCP Port DoS prevention. When enabled, this causes the
switch to drop packets that have the TCP source port equal to the TCP destination port.
UDP Port Mode The administrative mode of UDP Port DoS prevention. When enabled, this causes the
switch to drop packets that have the UDP source port equal to the UDP destination port.
SIPDIP Mode The administrative mode of SIP=DIP DoS prevention. Enabling this causes the switch to
drop packets that have a source IP address equal to the destination IP address. The factory
default is disabled.
SMACDMAC Mode The administrative mode of SMAC=DMAC DoS prevention. Enabling this causes the switch
to drop packets that have a source MAC address equal to the destination MAC address.
TCP FIN&URG& PSH The administrative mode of TCP FIN & URG & PSH DoS prevention. Enabling this causes
Mode the switch to drop packets that have TCP flags FIN, URG, and PSH set and TCP Sequence
Number = 0.
TCP Flag & Sequence The administrative mode of TCP Flag DoS prevention. Enabling this causes the switch to
Mode drop packets that have TCP control flags set to 0 and TCP sequence number set to 0.
TCP SYN Mode The administrative mode of TCP SYN DoS prevention. Enabling this causes the switch to
drop packets that have TCP Flags SYN set.
TCP SYN & FIN Mode The administrative mode of TCP SYN & FIN DoS prevention. Enabling this causes the
switch to drop packets that have TCP Flags SYN and FIN set.
TCP Fragment Mode The administrative mode of TCP Fragment DoS prevention. Enabling this causes the switch
to drop packets that have a TCP payload in which the IP payload length minus the IP
header size is less than the minimum allowed TCP header size.
TCP Offset Mode The administrative mode of TCP Offset DoS prevention. Enabling this causes the switch to
drop packets that have a TCP header Offset equal to 1.
auto-dos
This command enables Auto-DoS on the switch. By default, Auto-Dos is disabled.
When you enable Auto-DoS, all denial of service (DoS) checks are activated. If the switch
detects a DoS attack, the offending packets are copied to the CPU and Auto-DoS shuts down
the port and moves the port to the diagnostically disabled state. To use the port again, you
must manually reenable the port.
Format auto-dos
Mode Global Config
Switching Commands 635

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no auto-dos
This command disables Auto-DoS on the switch.
Format no auto-dos
Mode Global Config
show auto-dos
The output of this command shows whether Auto-DoS is enabled on the switch.
Format show auto-dos
Mode Global Config
MAC Database Commands
This section describes the commands you use to configure and view information about the
MAC databases.
bridge aging-time
This command configures the forwarding database address aging time-out in seconds. The
seconds parameter must be within the range of 10 to 1,000,000 seconds. In an SVL
system, the [fdbid/all] parameter is not used and will be ignored if entered. In an SVL system,
the [fdbid/all] parameter is not used and will be ignored if entered.
Default 300
Format bridge aging-time seconds
Mode Global Config
no bridge aging-time
This command sets the forwarding database address aging time-out to the default value. In
an SVL system, the [fdbid/all] parameter is not used and will be ignored if entered.
Format no bridge aging-time
Mode Global Config
Switching Commands 636

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show forwardingdb agetime
This command displays the timeout for address aging.
Default all
Format show forwardingdb agetime
Mode Privileged EXEC
Term Definition
Address Aging Displays the system's address aging timeout value in seconds.
Timeout
show mac-address-table multicast
This command displays the Multicast Forwarding Database (MFDB) information. If you enter
the command with no parameter, the entire table is displayed. You can display the table entry
for one MAC Address by specifying the MAC address as an optional parameter.
Format show mac-address-table multicast macaddr
Mode Privileged EXEC
Term Definition
VLAN ID The VLAN in which the MAC address is learned.
MAC Address A multicast MAC address for which the switch has forwarding or filtering information. The format is 6
two-digit hexadecimal numbers that are separated by colons, for example 01:23:45:67:89:AB.
Source The component that is responsible for this entry in the Multicast Forwarding Database. The source
can be IGMP Snooping, GMRP, and Static Filtering.
Type The type of the entry. Static entries are those that are configured by the end user. Dynamic entries
are added to the table as a result of a learning process or protocol.
Description The text description of this multicast table entry.
Interfaces The list of interfaces that are designated for forwarding (Fwd:) and filtering (Flt:).
Fwd Interface The resultant forwarding list is derived from combining all the component’s forwarding interfaces and
removing the interfaces that are listed as the static filtering interfaces.
Switching Commands 637

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
If one or more entries exist in the multicast forwarding table, the output is similar to the
following:
(NETGEAR Switch) #show mac-address-table multicast
Fwd
V LAN ID MAC Address Source Type Description Interface Interface
------- ----------------- ------- ------- --------------- --------- ---------
1 01:00:5E:01:02:03 Filter Static Mgmt Config Fwd: Fwd:
1/0/1, 1/0/1,
1/0/2, 1/0/2,
1/0/3, 1/0/3,
1 /0/4, 1/0/4,
1/0/5, 1/0/5,
1/0/6, 1/0/6,
1 /0/7, 1/0/7,
1/0/8, 1/0/8,
1/0/9, 1/0/9,
1/0/10, 1/0/10,
show mac-address-table stats
This command displays the Multicast Forwarding Database (MFDB) statistics.
Format show mac-address-table stats
Mode Privileged EXEC
Term Definition
Total Entries The total number of entries that can possibly be in the Multicast Forwarding Database table.
Most MFDB Entries The largest number of entries that have been present in the Multicast Forwarding Database table.
Ever Used This value is also known as the MFDB high-water mark.
Current Entries The current number of entries in the MFDB.
Switching Commands 638

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ISDP Commands
This section describes the commands you use to configure the industry standard Discovery
Protocol (ISDP).
isdp run
This command enables ISDP on the switch.
Default Enabled
Format isdp run
Mode Global Config
no isdp run
This command disables ISDP on the switch.
Format no isdp run
Mode Global Config
isdp holdtime
This command configures the hold time for ISDP packets that the switch transmits. The hold
time specifies how long a receiving device should store information sent in the ISDP packet
before discarding it. The period is in the range 10–255 seconds.
Default 180 seconds
Format isdp holdtime seconds
Mode Global Config
isdp timer
This command sets the period of time between sending new ISDP packets. The period is in
the range 5–254 seconds.
Default 60 seconds
Format isdp timer seconds
Mode Global Config
Switching Commands 639

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
isdp advertise-v2
This command enables the sending of ISDP version 2 packets from the device.
Default Enabled
Format isdp advertise-v2
Mode Global Config
no isdp advertise-v2
This command disables the sending of ISDP version 2 packets from the device.
Format no isdp advertise-v2
Mode Global Config
isdp enable
This command enables ISDP on an interface or range of interfaces.
Note: ISDP must be enabled both globally and on the interface in order for
the interface to transmit ISDP packets. If ISDP is globally disabled on
the switch, the interface will not transmit ISDP packets, regardless of
the ISDP status on the interface. To enable ISDP globally, use the
command isdp run on page639.
Default Enabled
Format isdp enable
Mode Interface Config
no isdp enable
This command disables ISDP on the interface.
Format no isdp enable
Mode Interface Config
clear isdp counters
This command clears ISDP counters.
Format clear isdp counters
Mode Privileged EXEC
Switching Commands 640

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
clear isdp table
This command clears entries in the ISDP table.
Format clear isdp table
Mode Privileged EXEC
show isdp
This command displays global ISDP settings.
Format show isdp
Mode Privileged EXEC
Term Definition
Timer The frequency with which this device sends ISDP packets. This value is given in seconds.
Hold Time The length of time the receiving device should save information sent by this device. This value is
given in seconds.
Version 2 The setting for sending ISDPv2 packets. If disabled, version 1 packets are transmitted.
Advertisements
Neighbors table The amount of time that has passed since the ISPD neighbor table changed.
time since last
change
Device ID The Device ID advertised by this device. The format of this Device ID is characterized by the value of
the Device ID Format object.
Device ID Format Indicates the Device ID format capability of the device.
Capability • serialNumber indicates that the device uses a serial number as the format for its Device ID.
• macAddress indicates that the device uses a Layer 2 MAC address as the format for its Device
ID.
• other indicates that the device uses its platform-specific format as the format for its Device ID.
Device ID Format Indicates the Device ID format of the device.
• serialNumber indicates that the value is in the form of an ASCII string containing the device
serial number.
• macAddress indicates that the value is in the form of a Layer 2 MAC address.
• other indicates that the value is in the form of a platform specific ASCII string containing info
that identifies the device. For example, ASCII string contains serialNumber
appended/prepended with system name.
Command example:
(NETGEAR Switch) #show isdp
Timer.......................................... 30
Hold Time...................................... 180
Version 2 Advertisements....................... Enabled
Switching Commands 641

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Neighbors table time since last change......... 0 days 00:00:00
Device ID...................................... 1114728
Device ID format capability.................... Serial Number, Host Name
Device ID format............................... Serial Number
show isdp interface
This command displays ISDP settings for the specified interface.
Format show isdp interface {all | unit/slot/port}
Mode Privileged EXEC
Term Definition
Interface The unit/slot/port of the specified interface.
Mode ISDP mode enabled/disabled status for the interface(s).
Command example:
(NETGEAR Switch) #show isdp interface 0/1
Interface Mode
--------------- ----------
0/1 Enabled
Command example:
(NETGEAR Switch) #show isdp interface all
I nterface Mode
- -------------- ----------
0/1 Enabled
0/2 Enabled
0/3 Enabled
0/4 Enabled
0/5 Enabled
0/6 Enabled
0/7 Enabled
0/8 Enabled
Switching Commands 642

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show isdp entry
This command displays ISDP entries. If the device-id is specified, then only entries for
that device are shown.
Format show isdp entry {all | device-id}
Mode Privileged EXEC
Term Definition
Device ID The device ID associated with the neighbor which advertised the information.
IP Addresses The IP address(es) associated with the neighbor.
Capability ISDP Functional Capabilities advertised by the neighbor.
Platform The hardware platform advertised by the neighbor.
Interface The interface (unit/slot/port) on which the neighbor's advertisement was received.
Port ID The port ID of the interface from which the neighbor sent the advertisement.
Hold Time The hold time advertised by the neighbor.
Version The software version that the neighbor is running.
Advertisement The version of the advertisement packet received from the neighbor.
Version
Entry Last The time when the entry was last changed.
Changed Time
Command example:
(NETGEAR Switch) #show isdp entry Switch
D evice ID Switch
Address(es):
IP Address: 172.20.1.18
I P Address: 172.20.1.18
C apability Router IGMP
P latform Netgear XCM8900
I nterface 0/1
P ort ID GigabitEthernet1/1
Holdtime 64
A dvertisement Version 2
E ntry last changed time 0 days 00:13:50
Switching Commands 643

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show isdp neighbors
This command displays the list of neighboring devices.
Format show isdp neighbors [unit/slot/port | detail]
Mode Privileged EXEC
Term Definition
Device ID The device ID associated with the neighbor which advertised the information.
IP Addresses The IP addresses associated with the neighbor.
Capability ISDP functional capabilities advertised by the neighbor.
Platform The hardware platform advertised by the neighbor.
Interface The interface (unit/slot/port) on which the neighbor's advertisement was received.
Port ID The port ID of the interface from which the neighbor sent the advertisement.
Hold Time The hold time advertised by the neighbor.
Advertisement The version of the advertisement packet received from the neighbor.
Version
Entry Last Time when the entry was last modified.
Changed Time
Version The software version that the neighbor is running.
Command example:
(NETGEAR Switch) #show isdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge,
S - Switch, H - Host, I - IGMP, r - Repeater
D evice ID Intf H oldtime C apability Platform Port ID
- --------------- - ---- - -------- ----------- - ------------- -------------------
S witch 0/1 165 R I c isco WS-C4948 GigabitEthernet1/1
Command example:
(NETGEAR Switch) #show isdp neighbors detail
D evice ID 0001f45f1bc0
Address(es):
I P Address: 10.27.7.57
C apability Router Trans Bridge Switch IGMP
P latform SecureChassis C2
I nterface 0/48
P ort ID ge.3.14
Switching Commands 644

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
H oldtime 131
A dvertisement Version 2
E ntry last changed time 0 days 00:01:59
V ersion: 05.00.56
show isdp traffic
This command displays ISDP statistics.
Format show isdp traffic
Mode Privileged EXEC
Term Definition
ISDP Packets Received Total number of ISDP packets received
ISDP Packets Transmitted Total number of ISDP packets transmitted
ISDPv1 Packets Received Total number of ISDPv1 packets received
ISDPv1 Packets Transmitted Total number of ISDPv1 packets transmitted
ISDPv2 Packets Received Total number of ISDPv2 packets received
ISDPv2 Packets Transmitted Total number of ISDPv2 packets transmitted
ISDP Bad Header Number of packets received with a bad header
ISDP Checksum Error Number of packets received with a checksum error
ISDP Transmission Failure Number of packets which failed to transmit
ISDP Invalid Format Number of invalid packets received
ISDP Table Full Number of times a neighbor entry was not added to the table due to a full database
ISDP IP Address Table Full Displays the number of times a neighbor entry was added to the table without an IP
address.
Command example:
(NETGEAR Switch) #show isdp traffic
ISDP Packets Received.......................... 4253
ISDP Packets Transmitted....................... 127
ISDPv1 Packets Received........................ 0
ISDPv1 Packets Transmitted..................... 0
ISDPv2 Packets Received........................ 4253
ISDPv2 Packets Transmitted..................... 4351
ISDP Bad Header................................ 0
ISDP Checksum Error............................ 0
ISDP Transmission Failure...................... 0
ISDP Invalid Format............................ 0
Switching Commands 645

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ISDP Table Full................................ 392
ISDP IP Address Table Full..................... 737
debug isdp packet
This command enables tracing of ISDP packets processed by the switch. ISDP must be
enabled on both the device and the interface in order to monitor packets for a particular
interface.
Note: To display the debug trace, enable the debug console command.
Format debug isdp packet [receive | transmit]
Mode Privileged EXEC
no debug isdp packet
This command disables tracing of ISDP packets on the receive or the transmit sides or on
both sides.
Format no debug isdp packet [receive | transmit]
Mode Privileged EXEC
Interface Error Disabling and Auto Recovery
Commands
Interface error disabling automatically disables an interface when an error is detected. No
traffic is allowed until the interface is either manually reenabled or, if auto recovery is
configured, the configured auto recovery interval expires.
If an error condition is detected for an interface, the switch places the interface in an
error-disabled state (also referred to as a diagnostic-disabled state) by shutting down the
interface. The error-disabled interface does not allow any traffic until the interface is
reenabled. You can manually enable the error-disabled interface. Alternatively, you can
enable auto recovery, which automatically reenables the interface after the expiration of the
configured interval.
errdisable recovery cause
This command enables auto recovery for a specific cause or for all causes. If auto recovery is
enabled, interfaces in the error-disabled state are reenabled when the recovery interval
expires. If errors continue on the interface, the interface can be placed back in the
error-disabled state and disabled. You can manually reenable an interface in the
error-disabled state by entering the no shutdown command for the interface.
Switching Commands 646

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format errdisable recovery cause {all | arp-inspection | bpduguard | dhcp-rate-limit
| sfp-mismatch | udld | ucast-storm | bcast-storm | mcast-storm | bpdustorm |
mac-locking | denial-of-service | link-flap}
Mode Global Config
no errdisable recovery cause
Use this command to disable auto recovery for a specific cause or for all causes. When
disabled, interfaces that are in an error-disabled state do not recover automatically.
Format no errdisable recovery cause {all | arp-inspection | bpduguard |
dhcp-rate-limit | sfp-mismatch | udld | ucast-storm | bcast-storm |
mcast-storm | bpdustorm | mac-locking | denial-of-service | link-flap}
Mode Global Config
errdisable recovery interval
Use this command to configure the auto recovery period, which is used for all causes. The
period can be from 30 to 86400 seconds. When the recovery period expires, the switch
attempts to bring interfaces in the error-disabled state back into service.
Default 300 seconds
Format errdisable recovery interval period
Mode Global Config
no errdisable recovery interval
Use this command to reset the auto recovery period to the default period of 300 seconds.
Format no errdisable recovery interval
Mode Global Config
show errdisable recovery
Use this command to display whether auto recovery is enabled for the various features for
which it can be enabled.
Format show errdisable recovery
Mode Privileged EXEC
Switching Commands 647

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
dhcp-rate-limit Auto recovery is enabled or disabled for rate limiting of the DHCP Snooping feature.
arp-inspection Auto recovery is enabled or disabled for the ARP Inspection feature.
udld Auto recovery is enabled or disabled for the UDLD feature.
bpdguard Auto recovery is enabled or disabled for the BPDU Guard feature.
bpdustorm Auto recovery is enabled or disabled for BPDU storm conditions.
sfp-mismatch Auto recovery is enabled or disabled for SFP mismatch conditions.
time interval The period after which auto recovery occurs.
mac-locking Auto recovery is enabled or disabled for port MAC locking conditions.
denial-of-service Auto recovery is enabled or disabled for DoS conditions.
link-flap Auto recovery is enabled or disabled for the link-flap feature.
Command example:
(M4300-96X) #show errdisable recovery
Errdisable Reason Auto-recovery Status
------------------ ---------------------
dhcp-rate-limit Disabled
arp-inspection Disabled
udld Disabled
bcast-storm Disabled
mcast-storm Disabled
ucast-storm Disabled
bpduguard Disabled
bpdustorm Disabled
keepalive Disabled
mac-locking Disabled
denial-of-service Disabled
link-flap Disabled
Timeout for Auto-recovery from D-Disable state 300
show interfaces status err-disabled
Use this command to display the interfaces that are error-disabled, the reason they are
error-disabled, and the period remaining before auto recovery occurs.
Format show interfaces status err-disabled
Mode Privileged EXEC
Switching Commands 648

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
interface An interface that is error-disabled.
Errdisable Reason The reason the interface is error-disabled.
Auto-Recovery The period that is remaining before auto recovery occurs.
Time Left
Command example:
(NETGEAR Switch) #show interfaces status err-disabled
Interface Errdisable Reason Auto-Recovery Time Left(sec)
- --------- - ---------------- ------------------
0/1 udld 279
0/2 bpduguard 285
0/3 bpdustorm 291
0/4 keepalive 11
UniDirectional Link Detection Commands
The purpose of the UniDirectional Link Detection (UDLD) feature is to detect and avoid
unidirectional links. A unidirectional link is a forwarding anomaly in a Layer 2 communication
channel in which a bi-directional link stops passing traffic in one direction. Use the UDLD
commands to detect unidirectional links’ physical ports. UDLD must be enabled on both sides
of the link in order to detect a unidirectional link. The UDLD protocol operates by exchanging
packets containing information about neighboring devices.
udld enable (Global Config)
This command enables UDLD globally on the switch.
Default Disabled
Format udld enable
Mode Global Config
no udld enable (Global Config)
This command disables udld globally on the switch.
Format no udld enable
Mode Global Config
Switching Commands 649

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
udld message time
This command configures the interval between UDLD probe messages on ports that are in
the advertisement phase. The range is from 7 to 90 seconds.
Default 15 seconds
Format udld message time seconds
Mode Global Config
udld timeout interval
This command configures the time interval after which UDLD link is considered to be
unidirectional. The range is from 5 to 60 seconds.
Default 5 seconds
Format udld timeout interval seconds
Mode Global Config
udld reset
This command resets all interfaces that have been shutdown by UDLD.
Default None
Format udld reset
Mode Privileged EXEC
udld enable (Interface Config)
This command enables UDLD on the specified interface.
Default disable
Format udld enable
Mode Interface Config
no udld enable (Interface Config)
This command disables UDLD on the specified interface.
Format no udld enable
Mode Interface Config
Switching Commands 650

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
udld port
This command selects the UDLD mode operating on this interface. If the aggressive
keyword is not entered, the port operates in normal mode.
Default normal
Format udld port [aggressive]
Mode Interface Config
show udld
This command displays either the global settings of UDLD or the UDLD settings for the
specified unit/slot/port. If the all keyword is entered, the command displays information for
all ports.
Format show udld [unit/slot/port | all]
Mode User EXEC
Privileged EXEC
If you do not enter a value for the unit/slot/port parameter, the command output
displays the fields that are shown in the following table.
Parameter Description
Admin Mode The global administrative mode of UDLD.
Message Interval The time period (in seconds) between the transmission of UDLD probe packets.
Timeout Interval The time period (in seconds) before making a decision that the link is unidirectional.
If you enter a value for the unit/slot/port parameter or you use the all keyword, the
command output displays the fields that are shown in the following table.
Parameter Description
Port The identifying port of the interface.
Admin Mode The administrative mode of UDLD configured on this interface. This is either Enabled or Disabled.
UDLD Mode The UDLD mode configured on this interface. This is either Normal or Aggressive.
UDLD Status The status of the link as determined by UDLD. The options are:
• Undetermined. UDLD has not collected enough information to determine the state of the port.
• Not applicable. UDLD is disabled, either globally or on the port.
• Shutdown. UDLD has detected a unidirectional link and shutdown the port. That is, the port is
in an errDisabled state.
• Bidirectional. UDLD has detected a bidirectional link.
• Undetermined (Link Down). The port would transition into this state when the port link
physically goes down due to any reasons other than the port been put into D-Disable mode by
the UDLD protocol on the switch.
Switching Commands 651

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
The following output displays after you enable UDLD and configure nondefault interval
values:
(NETGEAR Switch) #show udld
Admin Mode..................................... Enabled
Message Interval............................... 13
Timeout Interval............................... 31
Command example:
(NETGEAR Switch) #show udld 0/1
Port Admin Mode UDLD Mode UDLD Status
----- ---------- ----------- --------------
0/1 Enabled Normal Not Applicable
Command example:
(NETGEAR Switch) #show udld all
Port Admin Mode UDLD Mode UDLD Status
----- ---------- ----------- --------------
0/1 Enabled Normal Shutdown
0/2 Enabled Normal Undetermined
0/3 Enabled Normal Bidirectional
0/4 Enabled Normal Not Applicable
0/5 Enabled Normal Not Applicable
0/6 Enabled Normal Not Applicable
0/7 Enabled Normal Not Applicable
0/8 Enabled Normal Shutdown
0/9 Enabled Normal Not Applicable
0/10 Enabled Normal Not Applicable
0/11 Enabled Normal Not Applicable
0/12 Enabled Normal Undetermined
0/13 Enabled Normal Bidirectional
0/14 Disabled Normal Not Applicable
0/15 Disabled Normal Not Applicable
0/16 Disabled Normal Not Applicable
0/17 Disabled Normal Not Applicable
0/18 Disabled Normal Not Applicable
0/19 Disabled Normal Not Applicable
0/20 Disabled Normal Not Applicable
Switching Commands 652

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Link Debounce Commands
Link debouncing functions on a per-port basis on physical interfaces. After you configure link
debouncing, if the switch receives a link-down notification, the switch starts monitoring the
link event by starting a timer with the configured debounce time. Any intermediate link-down
and link-up events are ignored hereafter. When the timer expires, link debounce checks if the
current state of the link is still down; if so, it forwards a link-down notification to the upper
layer applications.
You must explicitly enable link debounce per interface with an appropriate debounce timer
value, taking into consideration the network topology and the features enabled on the switch,
such as LAG or spanning tree.
Note: Link debouncing is disabled by default.
link debounce time
This command configures the debounce time. The possible values for the milliseconds
parameter are in the 100–5000 range.
Format link debounce time milliseconds
Mode Interface Config
no link debounce time
This command disables the debounce time.
Format no link debounce time
Mode Interface Config
show interface debounce
This command displays the flap counts for all interfaces.
Format show interface debounce
Mode Privileged EXEC
Switching Commands 653

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show interface debounce
Interface Debounce Time(ms) Flaps
--------- -------------- -------
1/0/1 0 0
1/0/2 0 0
1/0/3 0 0
1/0/4 0 0
1/0/5 0 0
1/0/6 0 0
Bonjour Commands
A Mac that supports Bonjour can discover the switch in the network so that you can find the
switch IP address and log in to the local browser user interface of the switch. Bonjour is
enabled by default on the switch. You can disable Bonjour for security reasons.
bonjour run
This command enables Bonjour on the switch.
Default Enabled
Format bonjour run
Mode Global Config
no bonjour run
This command disables Bonjour on the switch.
Format no bonjour run
Mode Global Config
show bonjour run
This command displays the Bonjour information and the published services.
Format show bonjour run
Mode Privileged EXEC
Switching Commands 654
