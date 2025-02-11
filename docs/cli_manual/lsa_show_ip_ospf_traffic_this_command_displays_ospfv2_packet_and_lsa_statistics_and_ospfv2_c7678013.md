# lsa_show_ip_ospf_traffic_this_command_displays_ospfv2_packet_and_lsa_statistics_and_ospfv2_c7678013

Pages: 777-787

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Area ID A 32-bit identifier for the created stub area.
Type of Service The type of service associated with the stub metric. NETGEAR supports only Normal TOS.
Metric Val The metric value is applied based on the TOS. It defaults to the least metric of the type of service
among the interfaces to other areas. The OSPF cost for a route is a function of the metric value.
Import Summary Controls the import of summary LSAs into stub areas.
LSA
show ip ospf traffic
This command displays OSPFv2 packet and LSA statistics and OSPFv2 message queue
statistics. Packet statistics count packets and LSAs since OSPFv2 counters were last
cleared (using the command clear ip ospf counters on page736).
Note: The clear ip ospf counters command does not clear the message
queue high water marks.
Format show ip ospf traffic
Modes Privileged EXEC
Parameter Description
OSPFv2 Packet The number of packets of each type sent and received since OSPF counters were last cleared.
Statistics
LSAs The number of LSAs retransmitted by this router since OSPF counters were last cleared.
Retransmitted
LS Update Max The maximum rate of LS Update packets received during any 5-second interval since OSPF
Receive Rate counters were last cleared. The rate is in packets per second.
LS Update Max The maximum rate of LS Update packets transmitted during any 5-second interval since OSPF
Send Rate counters were last cleared. The rate is in packets per second.
Number of LSAs The number of LSAs of each type received since OSPF counters were last cleared.
Received
OSPFv2 Queue For each OSPFv2 message queue, the current count, the high water mark, the number of packets
Statistics that failed to be enqueued, and the queue limit. The high water marks are not cleared when OSPF
counters are cleared.
Routing Commands 777

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show ip ospf traffic
Time Since Counters Cleared: 4000 seconds
OSPFv2 Packet Statistics
Hello Database Desc LS Request LS Update LS ACK Total
Recd: 500 10 20 50 20 600
Sent: 400 8 16 40 16 480
LSAs Retransmitted................0
LS Update Max Receive Rate........20 pps
LS Update Max Send Rate...........10 pps
Number of LSAs Received
T1 (NETGEAR Switch)...............10
T2 (Network)......................0
T3 (Net Summary)..................300
T4 (ASBR Summary).................15
T5 (External).....................20
T7 (NSSA External)................0
T9 (Link Opaque)..................0
T10 (Area Opaque).................0
T11 (AS Opaque)...................0
Total.............................345
OSPFv2 Queue Statistics
Current Max Drops Limit
Hello 0 10 0 500
ACK 2 12 0 1680
Data 24 47 0 500
Event 1 8 0 1000
show ip ospf virtual-link
This command displays the OSPF Virtual Interface information for a specific area and
neighbor. The area-id parameter identifies the area and the neighbor parameter
identifies the neighbor's Router ID.
Format show ip ospf virtual-link area-id neighbor
Modes Privileged EXEC
User EXEC
Routing Commands 778

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Area ID The area id of the requested OSPF area.
Neighbor Router ID The input neighbor Router ID.
Hello Interval The configured hello interval for the OSPF virtual interface.
Dead Interval The configured dead interval for the OSPF virtual interface.
Interface Transmit The configured transmit delay for the OSPF virtual interface.
Delay
Retransmit Interval The configured retransmit interval for the OSPF virtual interface.
Authentication The configured authentication type of the OSPF virtual interface.
Type
State The OSPF Interface States are: down, loopback, waiting, point-to-point, designated router, and
backup designated router. This is the state of the OSPF interface.
Neighbor State The neighbor state.
show ip ospf virtual-link brief
This command displays the OSPF Virtual Interface information for all areas in the system.
Format show ip ospf virtual-link brief
Modes Privileged EXEC
User EXEC
Term Definition
Area ID The area id of the requested OSPF area.
Neighbor The neighbor interface of the OSPF virtual interface.
Hello Interval The configured hello interval for the OSPF virtual interface.
Dead Interval The configured dead interval for the OSPF virtual interface.
Retransmit Interval The configured retransmit interval for the OSPF virtual interface.
Transmit Delay The configured transmit delay for the OSPF virtual interface.
Routing Commands 779

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Routing Information Protocol Commands
This section describes the commands you use to view and configure Routing Information
Protocol (RIP), which is a distance-vector routing protocol that you use to route traffic within a
small network.
router rip
Use this command to enter Router RIP mode.
Format router rip
Mode Global Config
enable (RIP)
This command resets the default administrative mode of RIP in the router (active).
Default enabled
Format enable
Mode Router RIP Config
no enable (RIP)
This command sets the administrative mode of RIP in the router to inactive.
Format no enable
Mode Router RIP Config
ip rip
This command enables RIP on a router interface or range of interfaces.
Default disabled
Format ip rip
Mode Interface Config
no ip rip
This command disables RIP on a router interface.
Format no ip rip
Mode Interface Config
Routing Commands 780

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
auto-summary
This command enables the RIP auto-summarization mode.
Default disabled
Format auto-summary
Mode Router RIP Config
no auto-summary
This command disables the RIP auto-summarization mode.
Format no auto-summary
Mode Router RIP Config
default-information originate (RIP)
This command is used to control the advertisement of default routes.
Format default-information originate
Mode Router RIP Config
no default-information originate (RIP)
This command is used to control the advertisement of default routes.
Format no default-information originate
Mode Router RIP Config
default-metric (RIP)
This command is used to set a default for the metric of distributed routes. The value for the
metric argument can be from 0–15.
Format default-metric metric
Mode Router RIP Config
no default-metric (RIP)
This command is used to reset the default metric of distributed routes to its default value.
Format no default-metric
Mode Router RIP Config
Routing Commands 781

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
distance rip
This command sets the route preference value of RIP in the router. Lower route preference
values are preferred when determining the best route. A route with a preference of 255
cannot be used to forward traffic. The value for the preference argument can be from
1–255.
Default 15
Format distance rip preference
Mode Router RIP Config
no distance rip
This command sets the default route preference value of RIP in the router.
Format no distance rip
Mode Router RIP Config
distribute-list out (RIP)
This command is used to specify the access list to filter routes received from the source
protocol. The value for the access-list argument can be from 1–199.
Default 0
Format distribute-list access-list out {ospf | static | connected}
Mode Router RIP Config
no distribute-list out
This command is used to specify the access list to filter routes received from the source
protocol. The value for the access-list argument can be from 1–199.
Format no distribute-list access list out {ospf | static | connected}
Mode Router RIP Config
ip rip authentication
This command sets the RIP version 2 authentication type and key for the interface or range
of interfaces. The type of authentication can be either none, simple, or encrypt. If you
select simple or encrypt, the key parameter is composed of standard displayable,
noncontrol keystrokes from a standard 101/102-key keyboard. The authentication key must
be 8 bytes or less if the authentication type is simple. If the type is encrypt, the key can
be up to 16 bytes. Unauthenticated interfaces do not need an authentication key. If the type is
encrypt, a keyid in the range of 0 and 255 must be specified. The default value for the
Routing Commands 782

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
authentication type is none. Neither the default password key nor the default key id are
configured.
Default none
Format ip rip authentication {none | {simple key} | {encrypt key keyid}}
Mode Interface Config
no ip rip authentication
This command sets the default RIP Version 2 Authentication Type for an interface.
Format no ip rip authentication
Mode Interface Config
ip rip receive version
This command configures an interface or range of interfaces to allow RIP control packets of
the specified version or versions to be received.
The options are: rip1 to receive only RIP version 1 formatted packets; rip2 for RIP
version 2; both to receive packets from either format; or none to not allow any RIP control
packets to be received.
Default both
Format ip rip receive version {rip1 | rip2 | both | none}
Mode Interface Config
no ip rip receive version
This command configures the interface to allow RIP control packets of the default version(s)
to be received.
Format no ip rip receive version
Mode Interface Config
ip rip send version
This command configures an interface or range of interfaces to allow RIP control packets of
the specified version to be sent.
The options are: rip1 to send only RIP version-1 formatted packets; rip2 for RIP version 2;
rip-1c to send RIP version-2 formatted packets through a broadcast; or none to not allow
any RIP control packets to be sent.
Routing Commands 783

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default rip2
Format ip rip send version {rip1 | rip1c | rip2 | none}
Mode Interface Config
no ip rip send version
This command configures the interface to allow RIP control packets of the default version to
be sent.
Format no ip rip send version
Mode Interface Config
hostroutesaccept
This command enables the RIP hostroutesaccept mode.
Default enabled
Format hostroutesaccept
Mode Router RIP Config
no hostroutesaccept
This command disables the RIP hostroutesaccept mode.
Format no hostroutesaccept
Mode Router RIP Config
split-horizon
This command sets the RIP split horizon mode. Split horizon is a technique for avoiding
problems caused by including routes in updates sent to the router from which the route was
originally learned. The options are: none, no special processing; simple, a route is not
included in updates sent to the router from which it was learned; poison, a route is included
in updates sent to the router from which it was learned, but the metric is set to infinity.
Default simple
Format split-horizon {none | simple | poison}
Mode Router RIP Config
Routing Commands 784

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no split-horizon
This command sets the default RIP split horizon mode.
Format no split-horizon
Mode Router RIP Config
redistribute (RIP)
This command configures RIP protocol to redistribute routes from the specified source
protocol or routers. Five possible match options exist. When you submit the command
redistribute ospf match, the match option or options that you specify are added to
any match types presently being redistributed. Internal routes are redistributed by default.
The metric argument can have a value in the range from 0–15.
Default metric—not-configured
match—internal
Format for OSPF as redistribute ospf [metric metric] [match [[internal] [external 1]
source protocol [ external 2] [nssa-external 1] [nssa-external 2]]
Format for other redistribute {static | connected} [metric metric]
source protocols
Mode Router RIP Config
no redistribute
This command deconfigures RIP protocol to redistribute routes from the specified source
protocol or routers.
Format no redistribute {ospf | static | connected} [metric] [match [[internal]
[external 1] [external 2] [nssa-external 1] [nssa-external 2]]
Mode Router RIP Config
show ip rip
This command displays information relevant to the RIP router.
Format show ip rip
Modes Privileged EXEC
User EXEC
Term Definition
RIP Admin Mode Enable or disable.
Split Horizon Mode None, simple or poison reverse.
Routing Commands 785

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Auto Summary Mode Enable or disable. If enabled, groups of adjacent routes are summarized into single entries,
in order to reduce the total number of entries The default is enable.
Host Routes Accept Mode Enable or disable. If enabled the router accepts host routes. The default is enable.
Global Route Changes The number of route changes made to the IP Route Database by RIP. This does not
include the refresh of a route's age.
Global queries The number of responses sent to RIP queries from other systems.
Default Metric The default metric of redistributed routes if one has already been set, or blank if not
configured earlier. The valid values are 1 to 15.
Default Route Advertise The default route.
show ip rip interface brief
This command displays general information for each RIP interface. For this command to
display successful results, routing must be enabled per interface (for example, through the
ip rip command).
Format show ip rip interface brief
Modes Privileged EXEC
User EXEC
Term Definition
Interface unit/slot/port
IP Address The IP source address used by the specified RIP interface.
Send Version The RIP version(s) used when sending updates on the specified interface. The types are none,
RIP-1, RIP-1c, RIP-2
Receive Version The RIP version(s) allowed when receiving updates from the specified interface. The types are
none, RIP-1, RIP-2, Both
RIP Mode The administrative mode of router RIP operation (enabled or disabled).
Link State The mode of the interface (up or down).
show ip rip interface
This command displays information related to a particular RIP interface.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vlan-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in a unit/slot/port format. The vlan-id can
be a number from 1–4093.
Routing Commands 786

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format show ip rip interface {unit/slot/port | vlan vlan-id}
Modes Privileged EXEC
User EXEC
Term Definition
Interface unit/slot/port This is a configured value.
IP Address The IP source address used by the specified RIP interface. This is a configured value.
Send Version The RIP version(s) used when sending updates on the specified interface. The types are none,
RIP-1, RIP-1c, RIP-2. This is a configured value.
Receive Version The RIP version(s) allowed when receiving updates from the specified interface. The types are
none, RIP-1, RIP-2, Both. This is a configured value.
RIP Admin Mode RIP administrative mode of router RIP operation; enable activates, disable de-activates it. This is a
configured value.
Link State Indicates whether the RIP interface is up or down. This is a configured value.
Authentication The RIP Authentication Type for the specified interface. The types are none, simple, and encrypt.
Type This is a configured value.
The following information will be invalid if the link state is down.
Term Definition
Bad Packets The number of RIP response packets received by the RIP process which were subsequently
Received discarded for any reason.
Bad Routes The number of routes contained in valid RIP packets that were ignored for any reason.
Received
Updates Sent The number of triggered RIP updates actually sent on this interface.
Routing Commands 787
