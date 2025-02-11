# rip_output

Pages: 679-686

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ip protocols
This command lists a summary of the configuration and status for each unicast routing
protocol that is running. The command lists routing protocols that are configured and
enabled. If you specify a protocol, the command output is limited to the protocol.
Format show ip protocols [ospf | rip]
Mode Privileged Exec
Term Description
OSPFv2 output
Routing Protocol OSPFv2.
Router ID The router ID configured for OSPFv2.
OSPF Admin Mode Whether OSPF is enabled or disabled globally.
Maximum Paths The maximum number of next hops in an OSPF route.
Routing for The address ranges configured with an OSPF network command.
Networks
Distance The administrative distance (or “route preference”) for intra-area, inter-area, and external routes.
Default Route Whether OSPF is configured to originate a default route.
Advertise
Always Whether the default advertisement depends on a default route in the common routing table.
Metric The configured metric that is advertised with the default route.
Metric Type The metric type for the default route.
Redist Source The type of routes that OSPF is redistributing.
Metric The metric that is advertised for redistributed routes.
Metric Type The type of metric that is advertised for redistributed routes.
Subnets Whether OSPF redistributes subnets of classful addresses or only classful prefixes.
Dist List A distribution list that is used to filter routes. Only routes that pass the distribution list are
redistributed.
Number of Active The number of OSPF areas with at least one active interface and broken down by area type.
Areas
ABR Status Whether the switch functions as an area border router. A switch functions as an area border router if
it includes interfaces that are up in more than one area.
ASBR Status Whether the switch functions as an autonomous system boundary router. A switch functions as an
ASBR if it is redistributing any routes or originating a default route.
RIP output
RIP Admin Mode Whether RIP is globally enabled.
Routing Commands 679

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Description
Split Horizon Mode Whether RIP advertises routes on the interface on which the routes are received.
Default Metric The metric assigned to redistributed routes.
Default Route Whether the switch is originating a default route.
Advertise
Distance The administrative distance for RIP routes.
Redistribution A table showing information for each source protocol (connected, static, and OSPF). For each of
these sources, the distribution list and metric are shown. Fields that are not configured are left blank.
For OSPF, the configured OSPF match parameters are also displayed.
Interface The interfaces on which RIP is enabled and the version that is sent and accepted on each interface.
Command example:
(Router) #show ip protocols
Routing Protocol.......................... OSPFv2
Router ID................................. 6.6.6.6
OSPF Admin Mode........................... Enable
Maximum Paths............................. 32
Routing for Networks...................... 172.24.0.0 0.0.255.255 area 0
10.0.0.0 0.255.255.255 area 1
192.168.75.0 0.0.0.255 area 2
Distance.................................. Intra 110 Inter 110 Ext 110
Default Route Advertise................... Disabled
Always.................................... FALSE
Metric.................................... Not configured
Metric Type............................... External Type 2
Redist
Source Metric Metric Type Subnets Dist List
--------- ------- ----------- ------- ---------
static default 2 Yes None
connected 10 2 Yes 1
Number of Active Areas.................... 3 (3 normal, 0 stub, 0 nssa)
ABR Status................................ Yes
ASBR Status............................... Yes
Routing Protocol.......................... RIP
RIP Admin Mode............................ Enable
Split Horizon Mode........................ Simple
Default Metric............................ Not configured
Default Route Advertise................... Disable
Distance.................................. 120
Routing Commands 680

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Redistribution:
Source Metric Dist List Match
--------- ------ --------- --------------------------------------
connected 6
static 10 15
ospf 20 int ext1 ext2 nssa-ext1
Interface Send Recv
--------- ---- ----
0/25 RIPv2 RIPv2
show ip route
This command displays the routing table. The ip-address specifies the network for which
the route is to be displayed and displays the best matching best-route for the address. The
mask specifies the subnet mask for the given ip-address. When you use the
longer-prefixes keyword, the ip-address and mask pair becomes the prefix, and the
command displays the routes to the addresses that match that prefix. Use the protocol
parameter to specify the protocol that installed the routes. The value for protocol can be
connected, ospf, rip, or static. Use the all parameter to display all routes including
best and nonbest routes. If you do not use the all parameter, the command displays only
the best route.
Note: If you use the connected keyword for protocol, the all option is
not available because there are no best or nonbest connected routes.
Note: If you use the static keyword for protocol, the description
option is also available, for example: show ip route ip-address
static description. This command shows the description
configured with the specified static route(s).
Format show ip route [{ip-address [protocol] | {ip-address mask [longer-prefixes]
[protocol] | protocol} [all] | all}]
Modes Privileged EXEC
User EXEC
Term Definition
Route Codes The key for the routing protocol codes that might appear in the routing table output.
The show ip route command displays the routing tables in the following format:
Code IP-Address/Mask [Preference/Metric] via Next-Hop, Route-Timestamp, Interface,
Truncated
Routing Commands 681

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The columns for the routing table display the following information:
Term Definition
Code The codes for the routing protocols that created the routes.
Default Gateway The IP address of the default gateway. When the system does not have a more specific route to a
packet's destination, it sends the packet to the default gateway.
IP-Address/Mask The IP-Address and mask of the destination network corresponding to this route.
Preference The administrative distance associated with this route. Routes with low values are preferred over
routes with higher values.
Metric The cost associated with this route.
via Next-Hop The outgoing router IP address to use when forwarding traffic to the next router (if any) in the path
toward the destination.
Route-Timestamp The last updated time for dynamic routes. The format of Route-Timestamp will be
Days:Hours:Minutes if days > = 1
Hours:Minutes:Seconds if days < 1
Interface The outgoing router interface to use when forwarding traffic to the next destination. For reject routes,
the next hop interface would be Null0 interface.
T A flag appended to a route to indicate that it is an ECMP route, but only one of its next hops has
been installed in the forwarding table. The forwarding table may limit the number of ECMP routes or
the number of ECMP groups. When an ECMP route cannot be installed because such a limit is
reached, the route is installed with a single next hop. Such truncated routes are identified by a T
after the interface name.
To administratively control the traffic destined to a particular network and prevent it from
being forwarded through the router, you can configure a static reject route on the router. Such
traffic would be discarded and the ICMP destination unreachable message is sent back to the
source. This is typically used for preventing routing loops. The reject route added in the RTO
is of the type OSPF Inter-Area. Reject routes (routes of REJECT type installed by any
protocol) are not redistributed by OSPF/RIP. Reject routes are supported in both OSPFv2
and OSPFv3.
Command example:
(NETGEAR Switch) #show ip route
Route Codes: R - RIP Derived, O - OSPF Derived, C - Connected, S - Static
IA - OSPF Inter Area
E1 - OSPF External Type 1, E2 - OSPF External Type 2
N1 - OSPF NSSA External Type 1, N2 - OSPF NSSA External Type 2
Default gateway is 1.1.1.2
C 1.1.1.0/24 [0/1] directly connected, 0/11
C 2.2.2.0/24 [0/1] directly connected, 0/1
C 5.5.5.0/24 [0/1] directly connected, 0/5
S 7.0.0.0/8 [1/0] directly connected, Null0
Routing Commands 682

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
OIA 10.10.10.0/24 [110/6] via 5.5.5.2, 00h:00m:01s, 0/5
C 11.11.11.0/24 [0/1] directly connected, 0/11
S 12.0.0.0/8 [5/0] directly connected, Null0
S 23.0.0.0/8 [3/0] directly connected, Null0
C 1.1.1.0/24 [0/1] directly connected, 0/11
C 2.2.2.0/24 [0/1] directly connected, 0/1
C 5.5.5.0/24 [0/1] directly connected, 0/5
C 11.11.11.0/24 [0/1] directly connected, 0/11
S 10.3.2.0/24 [1/0] via 1.1.1.2, 0/11
Command example:
The following output indicates a truncated route:
(NETGEAR Switch) #show ip route
Route Codes: R - RIP Derived, O - OSPF Derived, C - Connected, S - Static
IA - OSPF Inter Area
E1 - OSPF External Type 1, E2 - OSPF External Type 2
N1 - OSPF NSSA External Type 1, N2 - OSPF NSSA External Type 2
O E1 100.1.161.0/24 [110/10] via 172.20.11.100, 00h:00m:13s, 2/11 T
O E1 100.1.162.0/24 [110/10] via 172.20.11.100, 00h:00m:13s, 2/11 T
O E1 100.1.163.0/24 [110/10] via 172.20.11.100, 00h:00m:13s, 2/11 T
show ip route ecmp-groups
This command reports all current ECMP groups in the IPv4 routing table. An ECMP group is
a set of two or more next hops used in one or more routes. The groups are numbered
arbitrarily from 1 to n. The output indicates the number of next hops in the group and the
number of routes that use the set of next hops. The output lists the IPv4 address and
outgoing interface of each next hop in each group.
Format show ip route ecmp-groups
Mode Privileged Exec
Command example:
(NETGEAR Switch) #show ip route ecmp-groups
ECMP Group 1 with 2 next hops (used by 1 route)
172.20.33.100 on interface 2/33
172.20.34.100 on interface 2/34
ECMP Group 2 with 3 next hops (used by 1 route)
172.20.32.100 on interface 2/32
172.20.33.100 on interface 2/33
172.20.34.100 on interface 2/34
Routing Commands 683

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ECMP Group 3 with 4 next hops (used by 1 route)
172.20.31.100 on interface 2/31
172.20.32.100 on interface 2/32
172.20.33.100 on interface 2/33
172.20.34.100 on interface 2/34
show ip route hw-failure
This command displays the routes that were not added to the hardware because of hash
errors or because the table was full.
Format show ip route hw-failure
Mode Privileged Exec
Command example:
(NETGEAR Switch) #show ip route hw-failure
Route Codes: R - RIP Derived, O - OSPF Derived, C - Connected, S - Static
IA - OSPF Inter Area
E1 - OSPF External Type 1, E2 - OSPF External Type 2
N1 - OSPF NSSA External Type 1, N2 - OSPF NSSA External Type 2
S U - Unnumbered Peer, L - Leaked Route, K - Kernel
P - Net Prototype
P 66.6.6.0/24 [1/1] via 9.0.0.2, 01d:22h:15m, 0/1 hw-failure
P 66.6.7.0/24 [1/1] via 9.0.0.2, 01d:22h:15m, 0/1 hw-failure
P 66.6.8.0/24 [1/1] via 9.0.0.2, 01d:22h:15m, 0/1 hw-failure
P 66.6.9.0/24 [1/1] via 9.0.0.2, 01d:22h:15m, 0/1 hw-failure
show ip route kernel
A kernel route is a special route that can be configured into the Linux kernel, for example,
through the Linux shell. The command output marks such a route with a K to denote that the
route is installed in the kernel.
Format show ip route kernel
Mode Privileged Exec
Command example:
(NETGEAR Switch) #show ip route kernel
Route Codes: C - Connected, S - Static
R - RIP Derived
O - OSPF Derived, IA - OSPF Inter Area
E1 - OSPF External Type 1, E2 - OSPF External Type 2
N1 - OSPF NSSA External Type 1, N2 - OSPF NSSA External Type 2
K - Kernel, P - Net Prototype
Routing Commands 684

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default Gateway(s): 172.26.2.1
show ip route net-prototype
This command displays the net prototype routes. The output of the command displays the
net prototype routes with a P.
Format show ip route net-p
Mode Privileged Exec
Command example:
(NETGEAR Switch) #show ip route net-prototype
Route Codes: R - RIP Derived, O - OSPF Derived, C - Connected, S - Static
IA - OSPF Inter Area
E1 - OSPF External Type 1, E2 - OSPF External Type 2
N1 - OSPF NSSA External Type 1, N2 - OSPF NSSA External Type 2
S U - Unnumbered Peer, L - Leaked Route, K - Kernel
P - Net Prototype
P 56.6.6.0/24 [1/1] via 9.0.0.2, 01d:22h:15m, 0/1
P 56.6.7.0/24 [1/1] via 9.0.0.2, 01d:22h:15m, 0/1
show ip route summary
This command displays a summary of the state of the routing table. When the optional all
keyword is given, some statistics, such as the number of routes from each source, include
counts for alternate routes. An alternate route is a route that is not the most preferred route to
its destination and therefore is not installed in the forwarding table. To include only the
number of best routes, do not use the optional keyword.
Format show ip route summary [all]
Modes Privileged EXEC
User EXEC
Term Definition
Connected Routes The total number of connected routes in the routing table.
Static Routes Total number of static routes in the routing table.
RIP Routes Total number of routes installed by RIP protocol.
OSPF Routes Total number of routes installed by OSPF protocol.
Intra Area Routes Total number of Intra Area routes installed by OSPF protocol.
Inter Area Routes Total number of Inter Area routes installed by OSPF protocol.
Routing Commands 685

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
External Type-1 Total number of External Type-1 routes installed by OSPF protocol.
Routes
External Type-2 Total number of External Type-2 routes installed by OSPF protocol.
Routes
Reject Routes Total number of reject routes installed by all protocols.
Net Prototype The number of net prototype routes.
Routes
Total Routes Total number of routes in the routing table.
Best Routes (High) The number of best routes currently in the routing table. This number only counts the best route to
each destination. The value in parentheses indicates the highest count of unique best routes since
counters were last cleared.
Alternate Routes The number of alternate routes currently in the routing table. An alternate route is a route that was
not selected as the best route to its destination.
Route Adds The number of routes that have been added to the routing table.
Route Modifies The number of routes that have been changed after they were initially added to the routing table.
Route Deletes The number of routes that have been deleted from the routing table.
Unresolved Route The number of route adds that failed because none of the route’s next hops were on a local subnet.
Adds Note that static routes can fail to be added to the routing table at startup because the routing
interfaces are not yet up. In such a situation, the counter is incremented. The static routes are added
to the routing table when the routing interfaces come up.
Invalid Route Adds The number of routes that failed to be added to the routing table because the route was invalid. A log
message is written for each of these failures.
Failed Route Adds The number of routes that failed to be added to the routing table because of a resource limitation in
the routing table.
Hardware Failed The number of routes that failed to be inserted into the hardware because of a hash error or a
Route Adds table-full condition.
Reserved Locals The number of routing table entries reserved for a local subnet on a routing interface that is down.
Space for local routes is always reserved so that local routes can be installed when a routing
interface bounces.
Unique Next Hops The number of distinct next hops used among all routes currently in the routing table. These include
(High) local interfaces for local routes and neighbors for indirect routes. The value in parentheses indicates
the highest count of unique next hops since counters were last cleared.
Next Hop Groups The current number of next hop groups in use by one or more routes. Each next hop group includes
(High) one or more next hops. The value in parentheses indicates the highest count of next hop groups
since counters were last cleared.
ECMP Groups The number of next hop groups with multiple next hops. The value in parentheses indicates the
(High) highest count of next hop groups since counters were last cleared.
ECMP Groups The number of next hop groups with multiple next hops.
Routing Commands 686
