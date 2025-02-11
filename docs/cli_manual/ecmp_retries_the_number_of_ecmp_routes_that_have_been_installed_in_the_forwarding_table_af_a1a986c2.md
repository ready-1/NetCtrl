# ecmp_retries_the_number_of_ecmp_routes_that_have_been_installed_in_the_forwarding_table_af_a1a986c2

Pages: 687-697

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
ECMP Routes The number of routes with multiple next hops currently in the routing table.
Truncated ECMP The number of ECMP routes that are currently installed in the forwarding table with just one next
Routes hop. The forwarding table may limit the number of ECMP routes or the number of ECMP groups.
When an ECMP route cannot be installed because such a limit is reached, the route is installed with
a single next hop.
ECMP Retries The number of ECMP routes that have been installed in the forwarding table after initially being
installed with a single next hop.
Routes with n Next The current number of routes with each number of next hops.
Hops
Command example:
(NETGEAR Switch) #show ip route summary
Connected Routes............................... 7
Static Routes.................................. 1
RIP Routes..................................... 20
OSPF Routes.................................... 1004
Intra Area Routes............................ 4
Inter Area Routes............................ 1000
External Type-1 Routes....................... 0
External Type-2 Routes....................... 0
Reject Routes.................................. 0
Total routes................................... 1032
Best Routes (High)............................. 1032 (1032)
Alternate Routes............................... 0
Route Adds..................................... 1010
Route Modifies................................. 1
Route Deletes.................................. 10
Unresolved Route Adds.......................... 0
Invalid Route Adds............................. 0
Failed Route Adds.............................. 0
Reserved Locals................................ 0
Unique Next Hops (High)........................ 13 (13)
Next Hop Groups (High)......................... 13 (14)
ECMP Groups (High)............................. 2 (3)
ECMP Routes.................................... 1001
Truncated ECMP Routes.......................... 0
ECMP Retries................................... 0
Routes with 1 Next Hop......................... 31
Routes with 2 Next Hops........................ 1
Routes with 4 Next Hops........................ 1000
Routing Commands 687

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
clear ip route
This command lets you reset the IPv4 routing table counters or remove various types of
routes in the IPv4 routing table.
Format clear ip route {all | counters | ospf [ip-address subnet-mask [interface
unit/slot/port] | rip [ip-address subnet-mask [interface unit/slot/port]]}
Mode Privileged EXEC
Term Definition
all Removes all dynamic routes from the IPv4 routing table. Static routes are not removed.
counters The command resets the IPv4 routing table counters to zero. These are the IPv4 routing table
counters that display in the output of the show ip route summary command (see show ip route
summary on page685). The command resets event counters only. Counters that display in the
current state of the routing table, such as the number of routes of each type, are not reset.
ospf Removes all OSPF routes from the IPv4 routing table. By using the ip-address and
subnet-mask parameters you can remove specific OSPF routes. In addition, you can remove
specific OSPF routes from specific next hop interfaces by using the interface option and
unit/slot/port parameter.
rip Removes all RIP routes from the IPv4 routing table. By using the ip-address and subnet-mask
parameters you can remove specific RIP routes. In addition, you can remove specific RIP routes
from specific next hop interfaces by using the interface option and unit/slot/port parameter.
show ip route preferences
This command displays detailed information about the route preferences for each type of
route. Route preferences are used in determining the best route. Lower router preference
values are preferred over higher router preference values. A route with a preference of 255
cannot be used to forward traffic.
Format show ip route preferences
Modes Privileged EXEC
User EXEC
Term Definition
Local The local route preference value.
Static The static route preference value.
OSPF Intra The OSPF Intra route preference value.
OSPF Inter The OSPF Inter route preference value.
OSPF External The OSPF External route preference value.
RIP The RIP route preference value.
Routing Commands 688

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Configured Default Gateway The route preference value of the statically-configured default gateway
DHCP Default Gateway The route preference value of the default gateway learned from the DHCP server.
Command example:
(NETGEAR Switch) #show ip route preferences
Local.......................................... 0
Static......................................... 1
OSPF Intra..................................... 110
OSPF Inter..................................... 110
OSPF External.................................. 110
RIP............................................ 120
Configured Default Gateway..................... 253
DHCP Default Gateway........................... 254
show ip stats
This command displays IP statistical information. Refer to RFC 1213 for more information
about the fields that are displayed.
Format show ip stats
Modes Privileged EXEC
User EXEC
show routing heap summary
This command displays a summary of the memory allocation from the routing heap. The
routing heap is a chunk of memory set aside when the system boots for use by the routing
applications.
Format show routing heap summary
Mode Privileged Exec
Parameter Description
Heap Size The amount of memory, in bytes, allocated at startup for the routing heap.
Memory In Use The number of bytes currently allocated.
Memory on Free The number of bytes currently on the free list. When a chunk of memory from the routing heap is
List freed, it is placed on a free list for future reuse.
Routing Commands 689

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
Memory Available The number of bytes in the original heap that have never been allocated.
in Heap
In Use High Water The maximum memory in use since the system last rebooted.
Mark
Command example:
(NETGEAR Switch) #show routing heap summary
Heap Size....................... 95053184
Memory In Use................... 56998
Memory on Free List............. 47
Memory Available in Heap........ 94996170
In Use High Water Mark.......... 57045
Routing Policy Commands
ip policy route-map
Use this command to identify a route map to use for policy-based routing on an interface
specified by route-map-name. Policy-based routing is configured on the interface that
receives the packets, not on the interface from which the packets are sent.
When a route-map applied on the interface is changed, that is, if new statements are added
to route-map or match/set terms are added/removed from route-map statement, and also if
route-map that is applied on an interface is removed, route-map needs to be removed from
interface and added back again in order to have changed route-map configuration to be
effective.
Note: Route-map and Diffserv cannot work on the same interface.
Format ip policy route-map-name
Mode Interface Config
(NETGEAR Switch) (Config)#interface 1/0/1
(NETGEAR Switch) (Interface 1/0/1)#
(NETGEAR Switch) (Interface 1/0/1)# #ip policy route-map equal-access
Routing Commands 690

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip policy route-map
Use this command to disable policy-based routing on an interface.
Format no ip policy route-map-name
Mode Interface Config
route-map
To create a route map and enter Route Map Configuration mode, use the route-map
command in Global Configuration mode. One use of a route map is to limit the redistribution
of routes to a specified range of route prefixes. The redistribution command specifies a route
map which refers to a prefix list. The prefix list identifies the prefixes that may be
redistributed. The switch accepts up to 64 route maps.
Default No route maps are configured by default. If no permit or deny tag is given, permit is the default.
Format route-map map-tag [permit | deny] [sequence-number]
Mode Global Configuration
Parameter Description
map-tag Text name of the route map. Route maps with the same name are grouped together in order of their
sequence numbers. A route map name may be up to 32 characters long.
permit (Optional) Permit routes that match all of the match conditions in the route map.
deny (Optional) Deny routes that match all of the match conditions in the route map.
sequence-number (Optional) An integer used to order the set of route maps with the same name. Route maps are
ordered from lowest to greatest sequence number, with lower sequence numbers being considered
first. If no sequence number is specified, the system assigns a value ten greater than the last
statement in the route map. The range is 0 to 65,535.
no route-map
To delete a route map or one of its statements, use the no route-map command.
Format no route-map map-tag [permit | deny] [sequence-number]
Mode Global Configuration
match ip address {access-list-number | access-list-name}
Use this command to configure a route map in order to match based on the match criteria
configured in an IP access-list. Note that an IP ACL must be configured before it is linked to a
route-map. Actions present in an IP ACL configuration are applied with other actions involved
in route-map. If an IP ACL referenced by a route-map is removed or rules are added or
deleted from that ACL, the configuration is rejected.
Routing Commands 691

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If there are a list of IP access-lists specified in this command and the packet matches at least
one of these access-list match criteria, the corresponding set of actions in route-map are
applied to packet.
If there are duplicate IP access-list numbers/names in this command, the duplicate
configuration is ignored.
Default No match criteria are defined by default.
Format match ip address {access-list-number | access-list-name}
[...access-list-number | access-list-name]
Mode Route Map Configuration
Parameter Description
access-list-number The access-list number that identifies an access-list configured through access-list CLI
configuration commands. This number is 1 to 99 for standard access list number. This number is
100 to 199 for extended access list number.
access-list-name The access-list name that identifies named IP ACLs. Access-list name can be up to 31
characters in length. A maximum of 16 ACLs can be specified in this match clause.
Command example:
The following example creates a route-map with a match clause on ACL number and applies
that route-map on an interface:
(NETGEAR Switch) (config)#access-list 1 permit ip 10.1.0.0 0.0.255.255
(NETGEAR Switch) (config)#access-list 2 permit ip 10.2.0.0 0.0.255.255
(NETGEAR Switch) (config)#route-map equal-access permit 10
(NETGEAR Switch) (config-route-map)#match ip address 1
(NETGEAR Switch) (config-route-map)#set ip default next-hop 192.168.6.6
(NETGEAR Switch) (config-route-map)#route-map equal-access permit 20
(NETGEAR Switch) (config-route-map)#match ip address 2
(NETGEAR Switch) (config-route-map)#set ip default next-hop 172.16.7.7
(NETGEAR Switch) (config)#interface 1/0/1
(NETGEAR Switch) (Interface 1/0/1)#ip address 10.1.1.1 255.255.255.0
(NETGEAR Switch) (Interface 1/0/1)#ip policy route-map equal-access
(NETGEAR Switch) (config)#interface 1/0/2
(NETGEAR Switch) (Interface 1/0/2)#ip address 192.168.6.5 255.255.255.0
(NETGEAR Switch) (config)#interface 1/0/3
(NETGEAR Switch) (Interface 1/0/3)#ip address 172.16.7.6 255.255.255.0
The ip policy route-map equal-access command is applied to interface 1/0/1. All
packets coming inside 1/0/1 are policy-routed.
Sequence number 10 in route map equal-access is used to match all packets sourced from
any host in subnet 10.1.0.0. If there is a match, and if the router has no explicit route for the
packet’s destination, it is sent to next-hop address 192.168.6.6.
Routing Commands 692

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Sequence number 20 in route map equal-access is used to match all packets sourced from
any host in subnet 10.2.0.0. If there is a match, and if the router has no explicit route for the
packet’s destination, it is sent to next-hop address 172.16.7.7.
All other packets are forwarded as per normal L3 destination-based routing.
Command example:
The following example shows a scenario in which an IP ACL that is referenced by a
route-map is removed or rules are added or deleted from that ACL:
(NETGEAR Switch) #show ip access-lists
Current number of ACLs: 9 Maximum number of ACLs: 100
ACL ID/Name Rules Direction Interface(s) VLAN(s)
------------------------------- ----- --------- ---------------- ----------
1 1
2 1
3 1
4 1
5 1
madan 1
(NETGEAR Switch) #show mac access-lists
Current number of all ACLs: 9 Maximum number of all ACLs: 100
MAC ACL Name Rules Direction Interface(s) VLAN(s)
------------------------------- ----- --------- ---------------- ----------
madan 1
mohan 1
goud 1
(NETGEAR Switch) #
(NETGEAR Switch) #configure
(NETGEAR Switch) (Config)#route-map madan
(NETGEAR Switch) (route-map)#match ip address 1 2 3 4 5 madan
(NETGEAR Switch) (route-map)#match mac-list madan mohan goud
(NETGEAR Switch) (route-map)#exit
(NETGEAR Switch) (Config)#exit
(NETGEAR Switch) #show route-map
route-map madan permit 10
Match clauses:
ip address (access-lists) : 1 2 3 4 5 madan
mac-list (access-lists) : madan mohan goud
Set clauses:
(NETGEAR Switch) (Config)#access-list 2 permit every
Request denied. Another application using this ACL restricts the number of rules allowed.
(NETGEAR Switch) (Config)#ip access-list madan
Routing Commands 693

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
(NETGEAR Switch) (Config-ipv4-acl)#permit udp any any
Request denied. Another application using this ACL restricts the number of rules allowed.
no match ip address (for an access list)
To delete a match statement for an access list from a route map, use the no match ip
address command.
Format no match ip address [access-list-number | access-list-name]
Mode Route Map Configuration
match length
Use this command to configure a route map to match based on the Layer 3 packet length
between specified minimum and maximum values. min specifies the packet’s minimum
Layer 3 length, inclusive, allowed for a match. max specifies the packet’s maximum Layer 3
length, inclusive, allowed for a match. Each route-map statement can contain one ‘match’
statement on packet length range.
Default No match criteria are defined by default.
Format match length min max
Mode Route Map Configuration
Command example:
(NETGEAR Switch) (config-route-map)# match length 64 1500
no match length
Use this command to delete a match statement from a route map.
Format no match length
Mode Route Map Configuration
match mac-list
Use this command to configure a route map in order to match based on the match criteria
configured in an MAC access-list.
A MAC ACL is configured before it is linked to a route-map. Actions present in MAC ACL
configuration are applied with other actions involved in route-map. When a MAC ACL
referenced by a route-map is removed, the route-map rule is also removed and the
corresponding rule is not effective. When a MAC ACL referenced by a route-map is removed
or rules are added or deleted from that ACL, the configuration is rejected.
Routing Commands 694

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default No match criteria are defined by default.
Format match mac-list mac-list-name [mac-list-name]
Mode Route Map Configuration
Parameter Description
mac-list-name The mac-list name that identifies MAC ACLs. MAC access list name can be up to 31 characters
in length.
Command example:
(NETGEAR Switch) (config-route-map)# match mac-list MacList1
Example 2:
This example illustrates the scenario where MAC ACL referenced by a route-map is removed
or rules are added or deleted from that ACL, this is how configuration is rejected:
(NETGEAR Switch) #show mac access-lists
Current number of all ACLs: 9 Maximum number of all ACLs: 100
MAC ACL Name Rules Direction Interface(s) VLAN(s)
------------------------------- ----- --------- ---------------- ----------
madan 1
mohan 1
goud 1
(NETGEAR Switch) #
(NETGEAR Switch) #configure
(NETGEAR Switch) (Config)#route-map madan
(NETGEAR Switch) (route-map)#match mac-list madan mohan goud
(NETGEAR Switch) (route-map)#exit
(NETGEAR Switch) (Config)#exit
(NETGEAR Switch) #show route-map
route-map madan permit 10
Match clauses:
mac-list (access-lists) : madan mohan goud
Set clauses:
(NETGEAR Switch) (Config)#mac access-list extended madan
(NETGEAR Switch) (Config-mac-access-list)#permit 00:00:00:00:00:01 ff:ff:ff:ff:ff:ff any
Request denied. Another application using this ACL restricts the number of rules allowed.
Routing Commands 695

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no match mac-list
To delete a match statement from a route map, use the no match mac-list command.
Format no match mac-list […mac-list-name]
Mode Route Map Configuration
set interface
If you do not want to revert to normal forwarding but instead want to drop a packet that does
not match the specified criteria, a set statement must be configured to route the packets to
interface null 0 as the last entry in the route-map. A set interface null0 command must
be configured in a separate statement. It must not be added along with any other statement
that has other match or set terms.
A route-map statement that is used for policy-based routing (PBR) is configured as permit or
deny. If the statement is marked as deny, traditional destination-based routing is performed
on the packet meeting the match criteria. If the statement is marked as permit, and if the
packet meets all the match criteria, then set commands in the route-map statement are
applied. If no match is found in the route-map, the packet is not dropped, instead the packet
is forwarded using the routing decision taken by performing destination-based routing.
Format set interface null0
Mode Route Map Configuration
set ip next-hop
Use this command to specify the adjacent next-hop router in the path toward the destination
to which the packets should be forwarded. If more than one IP address is specified, the first
IP address associated with a currently up-connected interface is used to route the packets.
This command affects all incoming packet types and is always used if configured. If
configured next-hop is not present in the routing table, an ARP request is sent from the
router.
In a route-map statement, the set ip next-hop and set ip default next-hop
commands are mutually exclusive. However, the set ip default next-hop command
can be configured in a separate route-map statement.
Format set ip next-hop ip-address [...ip-address]
Mode Route Map Configuration
Parameter Description
ip-address The IP address of the next hop to which packets are output. It must be the address of an adjacent
router. A maximum of 16 next-hop IP addresses can be specified in this se clause.
Routing Commands 696

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no set ip next-hop
Use this command to remove a set command from a route map.
Format no set ip next-hop ip-address [...ip-address]
Mode Route Map Configuration
set ip default next-hop
Use this command to set a list of default next-hop IP addresses. If more than one IP address
is specified, the first next hop specified that appears to be adjacent to the router is used. The
optional specified IP addresses are tried in turn.
A packet is routed to the next hop specified by this command only if there is no active route
for the packet’s destination address in the routing table. A default route in the routing table is
not considered an active route for an unknown destination address for policy-based routing
(PBR).
In a route-map statement, the set ip next-hop and set ip default next-hop
commands are mutually exclusive. However, the set ip default next-hop command
can be configured in a separate route-map statement.
Format set ip default next-hop ip-address [...ip-address]
Mode Route Map Configuration
Parameter Description
ip-address The IP address of the next hop to which packets are output. It must be the address of an adjacent
router. A maximum of 16 next-hop IP addresses can be specified in this set clause.
no set ip default next-hop
Use this command to remove a set command from a route map.
Format no set ip default next-hop ip-address [...ip-address]
Mode Route Map Configuration
set ip precedence
Use this command to set the three IP precedence bits in the IP packet header. With three
bits, you have eight possible values for the IP precedence; value can be a number from
0 through 7. This command is used when implementing QoS and can be used by other QoS
services, such as weighted fair queuing (WFQ) and weighted random early detection
(WRED).
Format set ip precedence value
Mode Route Map Configuration
Routing Commands 697
