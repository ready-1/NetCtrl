# igmp_and_mld_snooping_are_layer_2_functionalities_but_igmp_and_mld_are_layer_3_multicast

Pages: 1080-1104

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR) #show ipv6 pim statistics vlan 10
=====================================================================
Interface Stat Hello Register Reg-Stop Join/Pru BSR Assert CRP
=====================================================================
Vl10 Rx 0 0 0 0 0 0 0
Tx 2 0 0 0 0 0 0
Invalid Packets Received - 0
---------------------------------------------------------------------
Command example:
(NETGEAR) #show ipv6 pim statistics 1/0/5
=====================================================================
Interface Stat Hello Register Reg-Stop Join/Pru BSR Assert CRP
=====================================================================
1/0/5 Rx 0 0 6 5 0 0 0
Tx 10 9 0 0 0 0 0
Invalid Packets Received - 0
IPv6 MLD Commands
IGMP and MLD snooping are Layer 2 functionalities but IGMP and MLD are Layer 3 multicast
protocols. If you want to use IGMP and MLD snooping, a network must include a multicast
router that can function as a querier to solicit multicast group registrations. However, if
multicast traffic is destined to hosts within the same network, a multicast router is not required
but an IGMP and MLD snooping querier must be running on one of the switches in the
network and snooping must be enabled on all switches in the network. For more information,
see IGMP Snooping Configuration Commands on page569 and MLD Snooping
Commands on page589.
ipv6 mld router
Use this command, in the administrative mode of the router, to enable MLD in the router.
Default Disabled
Format ipv6 mld router
Mode Global Config
IPv6 Multicast Commands 1080

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ipv6 mld router
Use this command, in the administrative mode of the router, to disable MLD in the router.
Default Disabled
Format no ipv6 mld router
Mode Global Config
ipv6 mld query-interval
Use this command to set the MLD router’s query interval for the interface or range of
interfaces. The query-interval is the amount of time between the general queries sent when
the router is the querier on that interface. The range for the seconds argument is from 1 to
3600 seconds.
Default 125
Format ipv6 mld query-interval seconds
Mode Interface Config
no ipv6 mld query-interval
Use this command to reset the MLD query interval to the default value for that interface.
Format no ipv6 mld query-interval
Mode Interface Config
ipv6 mld query-max-response-time
Use this command to set the MLD querier’s maximum response time for the interface or
range of interfaces and this value is used in assigning the maximum response time in the
query messages that are sent on that interface. The range for the milliseconds argument
is from 0 to 65535 milliseconds.
Default 10000 milliseconds
Format ipv6 mld query-max-response-time milliseconds
Mode Interface Config
no ipv6 mld query-max-response-time
This command resets the MLD query max response time for the interface to the default
value.
Format no ipv6 mld query-max-response-time
Mode Interface Config
IPv6 Multicast Commands 1081

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ipv6 mld startup-query-interval
Use this command to set the interval between general IPv6 MLD queries that are sent when
the MLP process starts on the interface or range of interfaces. The range for the seconds
argument is 1 to 300 seconds. The default is 31 seconds.
Default 31
Format ipv6 mld startup-query-interval seconds
Mode Interface Config
no ipv6 mld startup-query-interval
Use this command to reset the startup query interval for IPv6 MLD to the default value of 31
seconds.
Format no ipv6 mld startup-query-interval
Mode Interface Config
ipv6 mld startup-query-count
Use this command to specify the number of IPv6 MLD queries that are sent when the MLP
process starts on the interface or range of interfaces and that is separated by the startup
query interval on the interface or range of interfaces. The range for the number argument is 1
to 20. The default is 2.
Default 2
Format ipv6 mld startup-query-count number
Mode Interface Config
no ipv6 mld startup-query-count
Use this command to reset the startup query count for IPv6 MLD to the default value of 2.
Format no ipv6 mld startup-query-count
Mode Interface Config
ipv6 mld last-member-query-interval
Use this command to set the last member query interval for an MLD interface or range of
interfaces, which is the value of the maximum response time parameter in the group specific
queries sent out of this interface. The range for the milliseconds argument is from 0 to
65535 milliseconds.
IPv6 Multicast Commands 1082

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default 1000 milliseconds
Format ipv6 mld last-member-query-interval milliseconds
Mode Interface Config
no ipv6 mld last-member-query-interval
Use this command to reset the last member query interval of the interface to the default
value.
Format no ipv6 mld last-member-query-interval
Mode Interface Config
ipv6 mld last-member-query-count
Use this command to set the number of listener-specific queries sent before the router
assumes that there are no local members on an interface or range of interfaces. The range
for the number argument is 1 to 20.
Default 2
Format ipv6 mld last-member-query-count number
Mode Interface Config
no ipv6 mld last-member-query-count
Use this command to reset the last-member-query-count of the interface to the default
value.
Format no ipv6 mld last-member-query-count
Mode Interface Config
ipv6 mld version
Use this command to configure the MLD version that the interface uses.
Default 2
Format ipv6 mld version {1 | 2}
Mode Interface Config
IPv6 Multicast Commands 1083

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ipv6 mld version
This command resets the MLD version used by the interface to the default value.
Format no ipv6 mld
Mode Interface Config
show ipv6 mld groups
Use this command to display information about multicast groups that MLD reported. The
information is displayed only when MLD is enabled on at least one interface. If MLD was not
enabled on even one interface, there is no group information to be displayed.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093. You can also specify a group address
(group-address).
Format show ipv6 mld groups {unit/slot/port | vlan vland-id | group-address}
Mode Privileged EXEC
User EXEC
The following fields are displayed as a table when unit/slot/port is specified.
Field Description
Group Address The address of the multicast group.
Interface Interface through which the multicast group is reachable.
Up Time Time elapsed in hours, minutes, and seconds since the multicast group has been known.
Expiry Time Time left in hours, minutes, and seconds before the entry is removed from the MLD membership
table.
When group-address is specified, the following fields are displayed for each multicast
group and each interface.
Field Description
Interface Interface through which the multicast group is reachable.
Group Address The address of the multicast group.
Last Reporter The IP Address of the source of the last membership report received for this multicast group address
on that interface.
Filter Mode The filter mode of the multicast group on this interface. The values it can take are include and
exclude.
IPv6 Multicast Commands 1084

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Description
Version 1 Host The time remaining until the router assumes there are no longer any MLD version-1 Hosts on the
Timer specified interface.
Group Compat The compatibility mode of the multicast group on this interface. The values it can take are MLDv1
Mode and MLDv2.
The following table is displayed to indicate all the sources associated with this group.
Field Description
Source Address The IP address of the source.
Uptime Time elapsed in hours, minutes, and seconds since the source has been known.
Expiry Time Time left in hours, minutes, and seconds before the entry is removed.
Command example:
(NETGEAR Switch) #show ipv6 mld groups ?
group-address Enter Group Address Info.
<unit/slot/port> Enter interface in unit/slot/port format.
Command example:
(NETGEAR Switch) #show ipv6 mld groups 1/0/1
Group Address.................................. FF43::3
Interface...................................... 1/0/1
Up Time (hh:mm:ss)............................. 00:03:04
Expiry Time (hh:mm:ss)......................... ------
Command example:
(NETGEAR Switch) #show ipv6 mld groups ff43::3
Interface...................................... 1/0/1
Group Address.................................. FF43::3
Last Reporter.................................. FE80::200:FF:FE00:3
Up Time (hh:mm:ss)............................. 00:02:53
Expiry Time (hh:mm:ss)......................... ------
Filter Mode.................................... Include
Version1 Host Timer............................ ------
Group compat mode.............................. v2
Source Address ExpiryTime
----------------- -----------
2003::10 00:04:17
2003::20 00:04:17
IPv6 Multicast Commands 1085

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ipv6 mld interface
Use this command to display MLD-related information for the interface.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
Format show ipv6 mld interface {unit/slot/port | vlan vland-id}
Mode Privileged EXEC
User EXEC
The following information is displayed for each of the interfaces or for only the specified
interface.
Field Description
Interface The interface number in unit/slot/port format.
MLD Mode Displays the configured administrative status of MLD.
Operational Mode The operational status of MLD on the interface.
MLD Version Indicates the version of MLD configured on the interface.
Query Interval Indicates the configured query interval for the interface.
Query Max Indicates the configured maximum query response time (in seconds) advertised in MLD queries on
Response Time this interface.
Robustness Displays the configured value for the tuning for the expected packet loss on a subnet attached to the
interface.
Startup Query This valued indicates the configured interval between General Queries sent by a Querier on startup.
interval
Startup Query This value indicates the configured number of Queries sent out on startup, separated by the Startup
Count Query Interval.
Last Member This value indicates the configured Maximum Response Time inserted into Group-Specific Queries
Query Interval sent in response to Leave Group messages.
Last Member This value indicates the configured number of Group-Specific Queries sent before the router
Query Count assumes that there are no local members.
The following information is displayed if the operational mode of the MLD interface is
enabled.
Field Description
Querier Status This value indicates whether the interface is an MLD querier or non-querier on the subnet it
is associated with.
Querier Address The IP address of the MLD querier on the subnet the interface is associated with.
IPv6 Multicast Commands 1086

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Description
Querier Up Time Time elapsed in seconds since the querier state has been updated.
Querier Expiry Time Time left in seconds before the Querier loses its title as querier.
Wrong Version Queries Indicates the number of queries received whose MLD version does not match the MLD
version of the interface.
Number of Joins The number of times a group membership has been added on this interface.
Number of Leaves The number of times a group membership has been removed on this interface.
Number of Groups The current number of membership entries for this interface.
show ipv6 mld traffic
Use this command to display MLD statistical information for the router.
Format show ipv6 mld traffic
Mode Privileged EXEC
User EXEC
Field Description
Valid MLD Packets Received The number of valid MLD packets received by the router.
Valid MLD Packets Sent The number of valid MLD packets sent by the router.
Queries Received The number of valid MLD queries received by the router.
Queries Sent The number of valid MLD queries sent by the router.
Reports Received The number of valid MLD reports received by the router.
Reports Sent The number of valid MLD reports sent by the router.
Leaves Received The number of valid MLD leaves received by the router.
Leaves Sent The number of valid MLD leaves sent by the router.
Bad Checksum MLD Packets The number of bad checksum MLD packets received by the router.
Malformed MLD Packets The number of malformed MLD packets received by the router.
clear ipv6 mld counters
Use this command to reset the MLD counters to zero on the specified interface.
Format clear ipv6 mld counters unit/slot/port
Mode Privileged Exec
IPv6 Multicast Commands 1087

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
clear ipv6 mld traffic
Use this command to clear all entries in the MLD traffic database.
Format clear ipv6 mld traffic
Mode Privileged Exec
IPv6 MLD-Proxy Commands
MLD-Proxy is the IPv6 equivalent of IGMP-Proxy. MLD-Proxy commands allow you to
configure the network device as well as to view device settings and statistics using either
serial interface or telnet session. The operation of MLD-Proxy commands is the same as for
IGMP-Proxy: MLD is for IPv6 and IGMP is for IPv4.MGMD is a term used to refer to both
IGMP and MLD.
ipv6 mld-proxy
Use this command to enable MLD-Proxy on the interface or range of interfaces. To enable
MLD-Proxy on the interface, you must enable multicast forwarding. Also, make sure that
there are no other multicast routing protocols enabled on the router.
Format ipv6 mld-proxy
Mode Interface Config
no ipv6 mld-proxy
Use this command to disable MLD-Proxy on the router.
Format no ipv6 mld-proxy
Mode Interface Config
ipv6 mld-proxy unsolicit-rprt-interval
Use this command to set the unsolicited report interval for the MLD-Proxy interface or range
of interfaces. This command is only valid when you enable MLD-Proxy on the interface. The
value of interval is 1-260 seconds.
Default 1
Format ipv6 mld-proxy unsolicit-rprt-interval interval
Mode Interface Config
IPv6 Multicast Commands 1088

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ipv6 mld-proxy unsolicited-report-interval
Use this command to reset the MLD-Proxy router’s unsolicited report interval to the default
value.
Format no ipv6 mld-proxy unsolicit-rprt-interval
Mode Interface Config
ipv6 mld-proxy reset-status
Use this command to reset the host interface status parameters of the MLD-Proxy interface
or range of interfaces. This command is only valid when you enable MLD-Proxy on the
interface.
Format ipv6 mld-proxy reset-status
Mode Interface Config
show ipv6 mld-proxy
Use this command to display a summary of the host interface status parameters.
Format show ipv6 mld-proxy
Mode Privileged EXEC
User EXEC
The command displays the following parameters only when you enable MLD-Proxy.
Field Description
Interface Index The interface number of the MLD-Proxy.
Admin Mode Indicates whether MLD-Proxy is enabled or disabled. This is a configured value.
Operational Mode Indicates whether MLD-Proxy is operationally enabled or disabled. This is a status
parameter.
Version The present MLD host version that is operational on the proxy interface.
Number of Multicast Groups The number of multicast groups that are associated with the MLD-Proxy interface.
Unsolicited Report Interval The time interval at which the MLD-Proxy interface sends unsolicited group
membership report.
Querier IP Address on Proxy The IP address of the Querier, if any, in the network attached to the upstream interface
Interface (MLD-Proxy interface).
Older Version 1 Querier Timeout The interval used to timeout the older version 1 queriers.
Proxy Start Frequency The number of times the MLD-Proxy has been stopped and started.
IPv6 Multicast Commands 1089

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show ipv6 mld-proxy
Interface Index..................................... 1/0/3
Admin Mode.......................................... Enable
Operational Mode.................................... Enable
Version............................................. 3
Num of Multicast Groups............................. 0
Unsolicited Report Interval......................... 1
Querier IP Address on Proxy Interface............... fe80::1:2:5
Older Version 1 Querier Timeout..................... 00:00:00
Proxy Start Frequency................................
show ipv6 mld-proxy interface
This command displays a detailed list of the host interface status parameters. It displays the
following parameters only when you enable MLD-Proxy.
Format show ipv6 mld-proxy interface
Modes Privileged EXEC
User EXEC
Term Definition
Interface Index The unit/slot/port of the MLD-proxy.
The column headings of the table associated with the interface are as follows.
Term Definition
Ver The MLD version.
Query Rcvd Number of MLD queries received.
Report Rcvd Number of MLD reports received.
Report Sent Number of MLD reports sent.
Leaves Rcvd Number of MLD leaves received. Valid for version 2 only.
Leaves Sent Number of MLD leaves sent on the Proxy interface. Valid for version 2 only.
Command example:
(NETGEAR Switch) #show ipv6 mld-proxy interface
Interface Index................................ 1/0/1
Ver Query Rcvd Report Rcvd Report Sent Leave Rcvd Leave Sent
------------------------------------------------------------------
1 2 0 0 0 2
2 3 0 4
IPv6 Multicast Commands 1090

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ipv6 mld-proxy groups
Use this command to display information about multicast groups that the MLD-Proxy
reported.
Format show ipv6 mld-proxy groups
Mode Privileged EXEC
User EXEC
Field Description
Interface The interface number of the MLD-Proxy.
Group Address The IP address of the multicast group.
Last Reporter The IP address of the host that last sent a membership report for the current group,
on the network attached to the MLD-Proxy interface (upstream interface).
Up Time (in secs) The time elapsed in seconds since last created.
Member State Possible values are:
• Idle_Member. The interface has responded to the latest group membership
query for this group.
• Delay_Member. The interface is going to send a group membership report to
respond to a group membership query for this group.
Filter Mode Possible values are Include or Exclude.
Sources The number of sources attached to the multicast group.
Command example:
(NETGEAR Switch) #show ipv6 mld-proxy groups
Interface Index................................ 1/0/3
G roup Address Last Reporter Up Time Member State F ilter Mode Sources
- ------------ -------------- ---------- ----------------- -------------- -------
F F1E::1 F E80::100:2.3 00:01:40 D ELAY_MEMBER Exclude 2
FF1E::2 F E80::100:2.3 00:02:40 DELAY_MEMBER Include 1
FF1E::3 F E80::100:2.3 00:01:40 DELAY_MEMBER Exclude 0
F F1E::4 F E80::100:2.3 00:02:44 DELAY_MEMBER Include 4
show ipv6 mld-proxy groups detail
Use this command to display information about multicast groups that MLD-Proxy reported.
Format show ipv6 mld-proxy groups detail
Mode Privileged EXEC
User EXEC
IPv6 Multicast Commands 1091

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Description
Interface The interface number of the MLD-Proxy.
Group Address The IP address of the multicast group.
Last Reporter The IP address of the host that last sent a membership report for the current group,
on the network attached to the MLD-Proxy interface (upstream interface).
Up Time (in secs) The time elapsed in seconds since last created.
Member State Possible values are:
• Idle_Member. The interface has responded to the latest group membership
query for this group.
• Delay_Member. The interface is going to send a group membership report to
respond to a group membership query for this group.
Filter Mode Possible values
Sources The number of sources attached to the multicast group.are Include or Exclude.
Group Source List The list of IP addresses of the sources attached to the multicast group.
Expiry Time The time left for a source to get deleted.
Command example:
(NETGEAR Switch) #show ipv6 igmp-proxy groups
Interface Index................................ 1/0/3
G roup Address Last Reporter Up Time Member State F ilter Mode Sources
- ------------ -------------- ---------- ----------------- -------------- -------
F F1E::1 F E80::100:2.3 2 44 D ELAY_MEMBER E xclude 2
Group Source List Expiry Time
------------------ ---------------
2 001::1 00:02:40
2001::2
F F1E::2 F E80::100:2.3 243 DELAY_MEMBER Include 1
Group Source List Expiry Time
------------------ ---------------
3001::1 00:03:32
3 002::2 00:03:32
F F1E::3 F E80::100:2.3 3 28 D ELAY_MEMBER Exclude 0
FF1E::4 F E80::100:2.3 2 55 D ELAY_MEMBER I nclude 4
IPv6 Multicast Commands 1092

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Group Source List Expiry Time
------------------ ---------------
4 001::1 00:03:40
5 002::2 00:03:40
4 001::2 00:03:40
5 002::2 00:03:40
IPv6 Multicast Commands 1093

Power over Ethernet Commands

This chapter contains the following sections:
• About PoE
• PoE Commands

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
About PoE
Power over Ethernet (PoE) describes a technology to pass electrical power safely along with
data on existing Ethernet cabling. The power supply equipment (PSE) is the device or switch
that delivers electrical power, and the PD or powered device is the end device that powers up
through the power delivered along the Ethernet cable.
The switch supports PoE and PoE+ as follows:
• PoE (802.3af 2003). This is the original standard, also known as the low-power standard,
which mandates delivery of up to 15.4 watts by the PSE. Because of power dissipation,
only 12.95 watts are assured to be available at the powered device (PD). The PD needs
to be designed so that it can accept power over Ethernet cabling. Category 3 cables can
be used to deliver power to the PD. However, with the advent of 802.11n, the newer
wireless APs required more power. To account for this, a newer standard was developed
in 2009, known as 802.3at.
• PoE+ (802.3at-2009). This is a newer standard than PoE. This is also known as the
high-power standard, which mandates delivery of up to 34.2 watts by the PSE. Because
of power dissipation, PoE+ provides only a maximum of 25.5 watts at the powered
device. Some PSEs can provide up to 51 watts. Before this standard became available in
2009, the industry started using different implementations to allow for more power. All
these needed to be brought under the purview of the newer 802.3at standard.
Note: PoE and PoE+ are supported only on physical, copper interfaces. The
default port mode is PoE+.
PoE Commands
poe
Use this command to enable the Power over Ethernet (PoE) functionality on a global basis or
per interface.
Default enabled
Format poe
Mode Global Config
Interface Config
Power over Ethernet Commands 1095

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no poe
Use this command to disable the Power over Ethernet (PoE) functionality on a global basis or
per interface.
Format no poe
Mode Global Config
Interface Config
poe detection
Use this command to configure the detection type on a global basis or per interface. It is used
to configure which types of PDs will be detected and powered by the switch. There are three
options:
• ieee—Detect resistive-type devices (IEEE standard)
• pre-ieee—Legacy capacitive detection only (nonstandard)
• auto—Perform resistive detection first (IEEE standard) and capacitive detection
(pre-IEEE standard)
Default auto
Format poe detection {ieee | pre-ieee | auto}
Mode Global Config
Interface Config
no poe detection
Use this command to set the detection mode to the default on a global basis or per interface.
Format no poe detection
Mode Global Config
Interface Config
poe high-power
Use this command to switch a port from 802.3af mode to high-power mode. This mode is
used to power up devices that require more power than the current IEEE 802.3af power
(more than 12.95 watts at the PD). There are three options:
• legacy—Use this mode if the device can power up (more than 12.95 watts) with higher
current and it cannot identify itself as a Class 4 device.
• pre-dot3at—Use this mode if the device cannot identify itself as a Class 4 device and it
does not have LLDP support.
• dot3at—Use this mode if the device is a Class 4 device capable of figuring out power.
Power over Ethernet Commands 1096

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default dot3at
Format poe high-power {legacy | pre-dot3at | dot3at}
Mode Interface Config
no poe high-power
Use this command to disable the high-power mode. The port will support only IEEE 902.3af
devices.
This command works on a global basis or per interface.
Format no poe high-power
Mode Interface Config
poe power limit
Use this command to configure the type of power limit for a port. If the power limit type is
user-defined, the command also allows you to configure a maximum power limit.
There are three options:
• class-based—Allows the port to draw up to the maximum power based on the
classification of the device connected.
• none—Allows the port to draw up to Class 0 maximum power if it is in low-power mode
and up to Class 4 maximum power if it is in high-power mode.
• user-defined—Allows you to define the maximum power to the port. This can be a
value from 3 through 30 watts. Therefore, the range is 3000–30000.
Default Class-based
Format poe power limit {class-based | none | user-defined maximum-power}
Mode Global Config
Interface Config
no poe power limit
Use this command to set the power limit type to the default. It also sets the maximum power
limit to the default if the power limit type is user-defined.
Format no poe power limit [user-defined]
Mode Global Config
Interface Config
Power over Ethernet Commands 1097

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
poe power management
Use this command to configure the power management mode based on each individual PoE
unit or on all PoE units.
Both the power management modes mentioned here will power up a device based on first
come, first served. When the available power is less than the power limit defined on a port, no
more power will be delivered.
Static and dynamic modes differ in how the available power is calculated, as follows:
• Static Power Management
Available power = power limit of the source - total allocated power
Where total allocated power is calculated as the power limit configured on the port.
• Dynamic Power Management
Available power = power limit of the source - total allocated power
Where total allocated power is calculated as the amount of power consumed by the port.
For example:
Assume that the power limit of the source is 300 watts. One port is powered up and is
drawing 3 watts of power. The power limit defined on the port is user-defined as 15 watts.
In this case, the available power for static and dynamic would be as follows:
• Static Power Management
Available power = 300 watts - 15 watts = 285 watts
• Dynamic Power Management
Available power = 300 watts - 3 watts = 297 watts
Default dynamic
Format poe power management {unit | all} {dynamic | static}
Mode Global Config
no poe power management
Use this command to set the power management mode to the default.
Format no poe power management {unit | all}
Mode Global Config
Power over Ethernet Commands 1098

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
poe priority
Use this command to configure the priority on a specific port. This is used for power
management purposes. The switch might not be able to supply power to all connected
devices, so the port priority is used to determine which ports will supply power if adequate
power capacity is not available for all enabled ports. For ports that have the same priority
level, the lower numbered port will have higher priority.
If a switch delivers peak power to a number of devices and you attach a new device to a
high-priority port, the switch can shut down power to a low-priority port before it powers up
the new device.
no poe priority
Use this command to set the priority to the default.
Format no poe priority
Mode Interface Config
poe reset
Use this command to reset the PoE state of every port (in global mode) or a specific port (in
interface mode). When the PoE port status is shown to be in an error state, this command
can be used to reset the PoE port. The command can also reset the power-delivering ports.
Note that this command takes effect only once after it is executed and cannot be saved
across power cycles.
Format poe reset
Mode Global Config
Interface Config
poe timer schedule
Use this command to allow you to attach a timer schedule to a PoE port.
You can define a time schedule using the existing time range commands. This schedule has
start and stop times. When this timer schedule is applied to a PoE-enabled port, the
capability of the port to deliver power is affected. At the scheduled start time, the PoE port is
disabled such that it cannot deliver any power. At the scheduled stop time, the PoE port is
reenabled so that it can deliver power.
Note: For information about creating a timer schedule, see Time Range
Commands for Time-Based ACLs on page995.
Format poe timer schedule name
Mode Interface Config
Power over Ethernet Commands 1099

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no poe timer schedule name
Use this command to detach the schedule from the port.
Format no poe timer schedule
Mode Interface Config
poe usagethreshold
Use this command to set a threshold (as a percentage) for the total amount of power that can
be delivered by the switch. For example, if the switch can deliver up to a maximum of 300
watts, a usage threshold of 90 percent ensures that only 270 watts are used for delivering
power to devices. This ensures that more power is not drawn than the switch can provide.
When the usage threshold is set, all the PDs are brought down and then brought back up. If
the consumed power is less than the threshold power (in the preceding case, 270 watts),
then the devices continue to power up. If the consumed power is 269 watts or less, the next
device is powered up. The moment consumed power exceeds the threshold power
( 270 watts), no other devices can power up.
This command allows you to set the usage threshold based on each individual PoE unit or all
PoE units.
Default 90
Format poe usagethreshold {unit | all} percentage
Mode Global Config
no poe usagethreshold
Use this command to set the usage threshold to a default value.
Format no poe usagethreshold {unit | all}
Mode Global Config
poe traps
Use this command to enable logging of specific PoE-related events, such as a PoE port
powering a device, the threshold being exceeded, and so on.
Default Enabled
Format poe traps
Mode Global Config
Power over Ethernet Commands 1100

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no poe traps
Use this command to disable logging the PoE traps.
Format no poe traps
Mode Global Config
show poe
Use this command to get global information regarding the PoE status.
Format show poe
Mode Privileged EXEC
User EXEC
Term Definition
Unit The unit on which PoE module is installed.
Firmware The firmware version of the PoE controller on the switch.
Version
PSE Main Indicates the status of the PoE controller:
Operational • ON—Indicates that the PoE controller is actively delivering power.
Status
• OFF—Indicates that the PoE controller is not delivering power.
• FAULTY—Indicates that the PoE controller is not functioning.
Power Source The source that provides power (internal power supply or RPS).
Total Power The maximum amount of power that can be delivered by this PoE unit.
Threshold The switch can power up one port, if consumed power is less than this power. That is, the
Power consumed power can be between the total power and threshold power values. The threshold
power value is effected by changing the system usage threshold.
Total Power The total amount of power being delivered to all the devices plugged into the switch.
Consumed
Usage The usage threshold level.
Threshold
Power The management mode used by the PoE controller.
Management
Mode
Traps The configured traps.
Command example:
(NETGEAR Switch) #show poe
Unit........................................... 2
Host........................................... XCM8948
Firmware Version............................... 1.0.0.2
Power over Ethernet Commands 1101

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
PSE Main Operational Status.................... ON
Total Power (Main AC).......................... 380
Total Power (RPS).............................. 300
Total Power (PD) .............................. 25
Power Source................................... Main AC
Threshold Power................................ 342
Total Power Consumed........................... 7
Usage Threshold................................ 90
Power Management Mode.......................... Dynamic
Configure port Auto Reset Mode................. Disable
Traps.......................................... Enable
show poe mpsm
This command displays the Multi Protocol Service Module (MPSM) and power bank values.
Format show poe mpsm [unit]
Mode Privileged EXEC
Command example:
(NETGEAR Switch) # show poe mpsm
Current Active MPSM = 1
Slot Power Bank
Value (W)
1 580
2 610
3 550
Command example:
(NETGEAR Switch) #show poe mpsm 2
Slot = 2
Current Active MPSM = 1
MPSM Number: 0 1 2 3 4 5
6 7
Power Bank Value (W): 260 610 1080 1430 1780 2130 2480 2830
Note: This command only applies when at least one module has PoE
capability
show poe port configuration
Use this command to see how the PoE ports are configured. You can display information
based on each individual port or all the ports collectively.
Format show poe port configuration [port | all]
Mode Privileged EXEC
User EXEC
Power over Ethernet Commands 1102

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show poe port configuration all
Admin Power Power Limit High Power Detection
Intf Mode Priority Limit Type Mode Type
(W)
------ ------- -------- ------ -------------- ------------- ---------------------
0 /1 Enable Low 15.400 User Defined Disable Auto
0 /2 Enable Low 15.400 User Defined Disable Auto
Command example:
(NETGEAR Switch) #show poe port configuration 0/2
Admin Power Power Limit High Power Detection
Intf Mode Priority Limit Type Mode Type
(W)
------ ------- -------- ------ -------------- ------------- ---------------------
0 /2 Enable Low 1 5.400 User Defined Disable Auto
show poe port info
Use this command to get information about the status of the PoE ports. You can display
information based on each individual port or all the ports collectively. The command displays
only PSE-capable ports.
Format show poe port info [port | all]
Mode Privileged EXEC
User EXEC
Term Definition
Intf Interface on which PoE is configured.
Class Class of the powered device according to the IEEE802.3af and IEEE802.3at definition.
Class Usage Max Power (watts)
• 0 Default 0.44-12.95
• 1 Optional 0.44-3.84
• 2 Optional 3.84-6.49
• 3 Optional 6.49-12.95
• 4 Optional 12.95-25.5
Power The power supplied to the powered device (in watts).
Output Current The current supplied to the powered device (in mA).
(mA)
Power over Ethernet Commands 1103

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Output Voltage The voltage supplied to the powered device (in volts).
(volts)
Status The Status field reports the state of power supplied to the port. The possible values are:
• Disabled—The PoE function is disabled on this port.
• Searching—The port is detecting the PoE device.
• Delivering Power—The port is providing power to the PoE device.
• Fault—The POE device is not IEEE compliant; no power is provided.
• Test—The port is in testing state.
• Other Fault—The port has experienced problems other than compliance issues.
When a port begins to deliver power, there is a trap indicating so. When a port stops delivering
power, there is a trap indicating so.
Command example:
(NETGEAR Switch) #show poe port info all
High Max Output Output
I ntf Power Power Class Power Current Voltage Status Fault
(W) (W) (mA) (volt) Status
------ - ------ - ---- - ------ - ----- - ------ - ------ - ---------------- --------
0/1 Yes 3 0.0 Unknown 00.000 0 00.00 Searching No Error
Command example:
(NETGEAR Switch) #show poe port info 0/33
H igh Max Output Output
I ntf Power Power Class Power Current Voltage Status Fault
(W) (W) (mA) (volt) Status
------ - ------ - ---- - ------ - ----- - ------ - ------ - ---------------- --------
0/33 N o 1 8.0 2 04.400 8 4 53.3 Delivering P ower No Error
show power rps
Note: This command applies to model M4300-52G-POE+ only.
Power over Ethernet Commands 1104
