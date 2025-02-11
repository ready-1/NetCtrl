# MULTICAST STATIC ROUTES

Pages: 1021-1104

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If you use the summary parameter, the command displays the following column headings in
the output table.
Term Definition
Source IP Addr The IP address of the multicast data source.
Group IP Addr The IP address of the destination of the multicast packet.
Protocol The multicast routing protocol by which this entry was created.
Incoming Interface The interface on which the packet for this source arrives.
Outgoing Interface The list of outgoing interfaces on which this packet is forwarded.
List
show ip mroute static
Use this command in Privileged EXEC or User EXEC mode to display all the static routes
configured in the static mcast table, if it is specified, or display the static route associated with
the particular sourceipaddr.
Format show ip mroute static [sourceipaddr]
Modes Privileged EXEC
User EXEC
Parameter Description
Source IP IP address of the multicast source network.
Source Mask The subnetwork mask pertaining to the sourceIP.
RPF Address The IP address of the RPF next-hop router toward the source.
Preference The administrative distance for this Static MRoute.
Command example:
console#show ip mroute static
MULTICAST STATIC ROUTES
Source IP S ource Mask RPF Address Preference
--------------- --------------- --------------- ----------
1.1.1.1 255.255.255.0 2.2.2.2 23
IP Multicast Commands 1021

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ip mroute static-multicast
Use this command in Privileged EXEC or User EXEC mode to display the manually added
static multicast routes.
Format show ip mroute static-multicast
Modes Privileged EXEC
User EXEC
Parameter Description
Maximum Multicast The maximum number of allowed static multicast routes.
Static Address Count
Current Multicast Static The number of configured static multicast routes.
Address Count
Group Address The configured multicast group IP address.
Egress VLAN List The VLANs that are associated with the static multicast route.
Command example:
(M4300-48X) #show ip mroute static-multicast
Maximum Multicast Static Address Count ........ 32
Current Multicast Static Address Count ........ 4
Group Address Egress VLAN List
---------------------- -----------------------------------
225.1.1.1 1-2
225.1.1.5 1
225.1.1.2 1-2
225.1.1.3 1
clear ip mroute
This command deletes all or the specified IP multicast route entries.This command clears
only dynamic mroute entries. It does not clear static mroutes.
Format clear ip mroute {* | group-address [source-address]}
Modes Privileged EXEC
Parameter Description
* Deletes all IPv4 entries from the IP multicast routing table.
IP Multicast Commands 1022

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
group-address IP address of the multicast group.
source-address The optional IP address of a multicast source that is sending multicast traffic to the group.
Command example:
The following example deletes all entries from the IP multicast routing table:
(NETGEAR Switch) # clear ip mroute *
Command example:
The following example deletes all entries from the IP multicast routing table that match the
multicast group address (224.1.2.1), irrespective of which source is sending for this group:
(NETGEAR Switch) # clear ip mroute 224.1.2.1
Command example:
The following example deletes all entries from the IP multicast routing table that match the
multicast group address (224.1.2.1) and the multicast source address (192.168.10.10):
(NETGEAR Switch) # clear ip mroute 224.1.2.1 192.168.10.10
DVMRP Commands
This section describes the Distance Vector Multicast Routing Protocol (DVMRP) commands.
ip dvmrp (Global Config)
This command sets administrative mode of DVMRP in the router to active.
Default disabled
Format ip dvmrp
Mode Global Config
no ip dvmrp
This command sets administrative mode of DVMRP in the router to inactive.
Format no ip dvmrp
Mode Global Config
IP Multicast Commands 1023

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip dvmrp metric
This command configures the metric for an interface or range of interfaces. This value is used
in the DVMRP messages as the cost to reach this network. The metric argument is a value
in the range 1 to 31.
Default 1
Format ip dvmrp metric metric
Mode Interface Config
no ip dvmrp metric
This command resets the metric for an interface to the default value. This value is used in the
DVMRP messages as the cost to reach this network.
Format no ip dvmrp metric
Mode Interface Config
ip dvmrp trapflags
This command enables the DVMRP trap mode.
Default disabled
Format ip dvmrp trapflags
Mode Global Config
no ip dvmrp trapflags
This command disables the DVMRP trap mode.
Format no ip dvmrp trapflags
Mode Global Config
ip dvmrp (Interface Config)
This command sets the administrative mode of DVMRP on an interface or range of interfaces
to active.
Default disabled
Format ip dvmrp
Mode Interface Config
IP Multicast Commands 1024

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip dvmrp
This command sets the administrative mode of DVMRP on an interface to inactive.
Format no ip dvmrp
Mode Interface Config
show ip dvmrp
This command displays the system-wide information for DVMRP.
Format show ip dvmrp
Modes Privileged EXEC
User EXEC
Term Definition
Admin Mode Indicates whether DVMRP is enabled or disabled.
Version String The version of DVMRP being used.
Number of Routes The number of routes in the DVMRP routing table.
Reachable Routes The number of entries in the routing table with non-infinite metrics.
The following fields are displayed for each interface.
Term Definition
Interface unit/slot/port
Interface Mode The mode of this interface. Possible values are Enabled and Disabled.
State The current state of DVMRP on this interface. Possible values are Operational or Non-Operational.
show ip dvmrp interface
This command displays the interface information for DVMRP on the specified interface.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
Format show ip dvmrp interface {unit/slot/port | vlan vland-id}
Modes Privileged EXEC
User EXEC
IP Multicast Commands 1025

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Interface Mode Indicates whether DVMRP is enabled or disabled on the specified interface.
Metric The metric of this interface. This is a configured value.
Local Address The IP address of the interface.
The following field is displayed only when DVMRP is operational on the interface.
Term Definition
Generation ID The Generation ID value for the interface. This is used by the neighboring routers to detect that the
DVMRP table should be resent.
The following fields are displayed only if DVMRP is enabled on this interface.
Term Definition
Received Bad The number of invalid packets received.
Packets
Received Bad The number of invalid routes received.
Routes
Sent Routes The number of routes that have been sent on this interface.
show ip dvmrp neighbor
This command displays the neighbor information for DVMRP.
Format show ip dvmrp neighbor
Modes Privileged EXEC
User EXEC
Term Definition
IfIndex The value of the interface used to reach the neighbor.
Nbr IP Addr The IP address of the DVMRP neighbor for which this entry contains information.
State The state of the neighboring router. The possible value for this field are ACTIVE or DOWN.
Up Time The time since this neighboring router was learned.
Expiry Time The time remaining for the neighbor to age out. This field is not applicable if the State is DOWN.
Generation ID The Generation ID value for the neighbor.
Major Version The major version of DVMRP protocol of neighbor.
Minor Version The minor version of DVMRP protocol of neighbor.
Capabilities The capabilities of neighbor.
IP Multicast Commands 1026

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Received Routes The number of routes received from the neighbor.
Rcvd Bad Pkts The number of invalid packets received from this neighbor.
Rcvd Bad Routes The number of correct packets received with invalid routes.
show ip dvmrp nexthop
This command displays the next hop information on outgoing interfaces for routing multicast
datagrams.
Format show ip dvmrp nexthop
Modes Privileged EXEC
User EXEC
Term Definition
Source IP The sources for which this entry specifies a next hop on an outgoing interface.
Source Mask The IP Mask for the sources for which this entry specifies a next hop on an outgoing interface.
Next Hop Interface The interface in unit/slot/port format for the outgoing interface for this next hop.
Type The network is a LEAF or a BRANCH.
show ip dvmrp prune
This command displays the table listing the router’s upstream prune information.
Format show ip dvmrp prune
Modes Privileged EXEC
User EXEC
Term Definition
Group IP The multicast Address that is pruned.
Source IP The IP address of the source that has pruned.
Source Mask The network Mask for the prune source. It should be all 1s or both the prune source and prune mask
must match.
Expiry Time (secs) The expiry time in seconds. This is the time remaining for this prune to age out.
IP Multicast Commands 1027

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ip dvmrp route
This command displays the multicast routing information for DVMRP.
Format show ip dvmrp route
Modes Privileged EXEC
User EXEC
Term Definition
Source Address The multicast address of the source group.
Source Mask The IP Mask for the source group.
Upstream Neighbor The IP address of the neighbor which is the source for the packets for a specified multicast address.
Interface The interface used to receive the packets sent by the sources.
Metric The distance in hops to the source subnet. This field has a different meaning than the Interface
Metric field.
Expiry Time (secs) The expiry time in seconds, which is the time left for this route to age out.
Up Time (secs) The time when a specified route was learnt, in seconds.
PIM Commands
This section describes the commands you use to configure Protocol Independent Multicast
-Dense Mode (PIM-DM) and Protocol Independent Multicast - Sparse Mode (PIM-SM).
PIM-DM and PIM-SM are multicast routing protocols that provides scalable inter-domain
multicast routing across the Internet, independent of the mechanisms provided by any
particular unicast routing protocol. Only one PIM mode can be operational at a time.
ip pim dense
This command administratively enables the PIM Dense mode across the router.
Default disabled
Format ip pim dense
Mode Global Config
Command example:
(NETGEAR) (Config) #ip pim dense
IP Multicast Commands 1028

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip pim dense
This command administratively disables the PIM Dense mode across the router.
Format no ip pim dense
Mode Global Config
ip pim sparse
This command administratively enables the PIM Sparse mode across the router.
Default disabled
Format ip pim sparse
Mode Global Config
Command example:
(NETGEAR) (Config) #ip pim sparse
no ip pim sparse
This command administratively disables the PIM Sparse mode across the router.
Format no ip pim sparse
Mode Global Config
ip pim
Use this command to administratively enable PIM on the specified interface.
Default disabled
Format ip pim
Mode Interface Config
Command example:
(NETGEAR) (Interface 1/0/1) #ip pim
no ip pim
Use this command to disable PIM on the specified interface.
Format no ip pim
Mode Interface Config
IP Multicast Commands 1029

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip pim hello-interval
This command configures the transmission frequency of PIM hello messages the specified
interface. The seconds argument is a value in a range of 0 to 18000 seconds.
Default 30
Format ip pim hello-interval seconds
Mode Interface Config
Command example:
(NETGEAR) (Interface 1/0/1) #ip pim hello-interval 50
no ip pim hello-interval
This command resets the transmission frequency of hello messages between PIM enabled
neighbors to the default value.
Format no ip pim hello-interval
Mode Interface Config
ip pim bsr-border
Use this command to prevent bootstrap router (BSR) messages from being sent or received
on the specified interface.
Note: This command takes effect only when Sparse mode in enabled in the
Global mode.
Default disabled
Format ip pim bsr-border
Mode Interface Config
(NETGEAR) (Interface 1/0/1) #ip pim bsr-border
no ip pim bsr-border
Use this command to disable the specified interface from being the BSR border.
Format no ip pim bsr-border
Mode Interface Config
IP Multicast Commands 1030

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip pim bsr-candidate
This command is used to configure the router to announce its candidacy as a bootstrap
router (BSR).
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
Note: This command takes effect only when PIM-SM is configured as the
PIM mode.
Default Disabled
Format ip pim bsr-candidate interface {unit/slot/port | vlan vlan-id}
hash-mask-length [bsr-priority] [interval interval]
Mode Global Config
Parameters Description
unit/slot/port Interface or VLAN number on this router from which the BSR address is derived, to make it a
candidate. This interface or VLAN must be enabled with PIM.
hash-mask-length Length of a mask (32 bits maximum) that is to be ANDed with the group address before the hash
function is called. All groups with the same seed hash correspond to the same RP. For example, if
this value is 24, only the first 24 bits of the group addresses matter. This allows you to get one RP for
multiple groups.
bsr-priority [Optional] Priority of the candidate BSR. The range is an integer from 0 to 255. The BSR with the
larger priority is preferred. If the priority values are the same, the router with the larger IP address is
the BSR. The default value is 0.
interval [Optional] Indicates the BSR candidate advertisement interval. The range is from 1 to 16383
seconds. The default value is 60 seconds.
Command example: The following shows examples of the command.
(NETGEAR) (Config) #ip pim bsr-candidate interface 1/0/1 32 5
(NETGEAR) (Config) #ip pim bsr-candidate interface 1/0/1 32 5 interval 100
no ip pim bsr-candidate
Use this command to remove the configured PIM Candidate BSR router.
Format no ip pim bsr-candidate interface {unit/slot/port | vlan vlan-id}
Mode Global Config
IP Multicast Commands 1031

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip pim dr-priority
Use this command to set the priority value for which a router is elected as the designated
router (DR). The priority argument is a value in the range of 0–2147483647.
Note: This command takes effect only when Sparse mode is enabled in the
Global mode.
Default 1
Format ip pim dr-priority priority
Mode Interface Config
Command example:
(NETGEAR) (Interface 1/0/1) #ip pim dr-priority 10
no ip pim dr-priority
Use this command to return the DR Priority on the specified interface to its default value.
Format no ip pim dr-priority
Mode Interface Config
ip pim join-prune-interval
Use this command to configure the frequency of PIM Join/Prune messages on a specified
interface. The join/prune interval is specified in seconds. The seconds argument can be
configured as a value from 0 to 18000 seconds.
Note: This command takes effect only when PIM-SM is configured as the
PIM mode.
Default 60
Format ip pim join-prune-interval seconds
Mode Interface Config
Command example:
(NETGEAR) (Interface 1/0/1) #ip pim join-prune-interval 90
IP Multicast Commands 1032

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip pim join-prune-interval
Use this command to set the join/prune interval on the specified interface to the default value.
Format no ip pim join-prune-interval
Mode Interface Config
ip pim rp-address
This command defines the address of a PIM Rendezvous point (RP) for a specific multicast
group range.
Note: This command takes effect only when PIM-SM is configured as the
PIM mode.
Default 0
Format ip pim rp-address rp-address group-address group-mask [override]
Mode Global Config
Parameter Description
rp-address The IP address of the RP.
group-address The group address supported by the RP.
group-mask The group mask for the group address.
override [Optional] Indicates that if there is a conflict, the RP configured with this command prevails over the
RP learned by BSR.
Command example:
(NETGEAR) (Config) #ip pim rp-address 192.168.10.1
224.1.2.0 255.255.255.0
no ip pim rp-address
Use this command to remove the address of the configured PIM Rendezvous point (RP) for
the specified multicast group range.
Format no ip pim rp-address rp-address group-address group-mask [override]
Mode Global Config
IP Multicast Commands 1033

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip pim rp-candidate
Use this command to configure the router to advertise itself as a PIM candidate rendezvous
point (RP) to the bootstrap router (BSR) for a specific multicast group range.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
Note: This command takes effect only when PIM-SM is configured as the
PIM mode.
Default Disabled
Format ip pim rp-candidate interface {unit/slot/port | vlan vland-id} group-address
group-mask [interval interval]
Mode Global Config
Parameter Description
unit/slot/port or The interface type in the unit/slot/port format or the VLAN ID is advertised as a candidate RP
vland-id address. This interface or VLAN must be enabled with PIM.
group-address The multicast group address that is advertised in association with the RP address.
group-mask The multicast group prefix that is advertised in association with the RP address.
interval [Optional] Indicates the RP candidate advertisement interval. The range is from 1 to 16383 seconds.
The default value is 60 seconds.
Command example: The following shows examples of the command.
(NETGEAR) (Config) #ip pim rp-candidate interface 1/0/1 224.1.2.0 255.255.255.0
(NETGEAR) (Config) #ip pim rp-candidate interface 1/0/1 224.1.2.0 255.255.255.0 interval

no ip pim rp-candidate
Use this command to remove the configured PIM candidate Rendezvous point (RP) for a
specific multicast group range.
Format no ip pim rp-candidate interface {unit/slot/port | vlan vland-id}
group-address group-mask
Mode Global Config
IP Multicast Commands 1034

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip pim ssm
Use this command to define the Source Specific Multicast (SSM) range of IP multicast
addresses on the router.
Note: This command takes effect only when PIM-SM is configured as the
PIM mode.
Default disabled
Format ip pim ssm {default | group-address group-mask}
Mode Global Config
Parameter Description
default Defines the SSM range access list to 232/8.
Command example:
(NETGEAR) (Config) #ip pim ssm default
(NETGEAR) (Config) #ip pim ssm 232.1.2.0 255.255.255.0
no ip pim ssm
Use this command to remove the Source Specific Multicast (SSM) range of IP multicast
addresses on the router.
Format no ip pim ssm {default | group-address group-mask}
Mode Global Config
ip pim-trapflags
This command enables the PIM trap mode for both Sparse Mode (SM) and Dense Mode.
(DM).
Default disabled
Format ip pim-trapflags
Mode Global Config
IP Multicast Commands 1035

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip pim-trapflags
This command sets the PIM trap mode to the default.
Format no ip pim-trapflags
Mode Global Config
show ip mfc
This command displays multicast route entries in the multicast forwarding (MFC) database.
Format show ip mfc
Modes Privileged EXEC
User EXEC
Term Definition
MFC IPv4 Mode Indicates whether IPv4 multicast routing is operational.
MFC IPv6 Mode Indicates whether IPv6 Multicast routing is operational.
MFC Entry Count The number of entries present in MFC.
Current multicast IPv4 Protocol The current operating IPv4 multicast routing protocol.
Current multicast IPv6 Protocol The current operating multicast IPv6 routing protocol.
Total Software Forwarded The total number of multicast packets forwarded in software.
packets
Source Address The source address of the multicast route entry.
Group Address The group address of the multicast route entry.
Packets Forwarded in Software The number of multicast packets that are forwarded in software for a specific multicast
for this entry route entry.
Protocol The multicast touting protocol that added a specific entry
Expiry Time (secs) The expiration time in seconds for a specific multicast route entry.
Up Time (secs) The up time in seconds for a specific multicast routing entry.
Incoming interface The incoming interface for a specific multicast route entry.
Outgoing interface list The outgoing interface list for a specific multicast route entry.
Command example:
(NETGEAR) #show ip mfc
MFC IPv4 Mode.................................. Enabled
MFC IPv6 Mode.................................. Disabled
MFC Entry Count ............................... 1
IP Multicast Commands 1036

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Current multicast IPv4 protocol................ PIMSM
Current multicast IPv6 protocol................ No protocol enabled.
Total software forwarded packets .............. 0
Source address: 192.168.10.5
Group address: 225.1.1.1
Packets forwarded in software for this entry: 0 Protocol: PIM-SM
Expiry Time (secs): 206 Up Time (secs): 4
Incoming interface: 1/0/10 Outgoing interface list: None
show ip pim
This command displays the system-wide information for PIM-DM or PIM-SM.
Format show ip pim
Modes Privileged EXEC
User EXEC
Note: If the PIM mode is PIM-DM (dense), some of the fields in the following
table do not display in the command output because they are
applicable only to PIM-SM.
Term Definition
PIM Mode Indicates the configured mode of the PIM protocol as dense (PIM-DM) or sparse
(PIM-SM)
Interface unit/slot/port
Interface Mode Indicates whether PIM is enabled or disabled on this interface.
Operational Status The current state of PIM on this interface: Operational or Non-Operational.
The following example shows PIM Mode - Dense:
(NETGEAR) #show ip pim
P IM Mode Dense
I nterface Interface-Mode Operational-Status
--------- -------------- ------------------
1/0/1 Enabled Operational
1/0/3 Disabled Non-Operational
Command example:
The following example shows PIM Mode - Sparse
(NETGEAR) #show ip pim
IP Multicast Commands 1037

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
PIM Mode Sparse
Interface I nterface-Mode Operational-Status
--------- -------------- ------------------
1/0/1 Enabled Operational
1/0/3 Disabled Non-Operational
Command example:
The following example shows that PIM is not configured:
(NETGEAR) #show ip pim
PIM Mode None
None of the routing interfaces are enabled for PIM.
show ip pim ssm
This command displays the configured source specific IP multicast addresses.
Format show ip pim ssm
Modes Privileged EXEC
User EXEC
Term Definition
Group Address The IP multicast address of the SSM group.
Prefix Length The network prefix length.
Command example:
(NETGEAR) #show ip pim ssm
Group Address/Prefix Length
----------------------------
232.0.0.0/8
Command example:
If no SSM group range is configured, the command displays the following message:
No SSM address range is configured.
show ip pim interface
This command displays the PIM interface status parameters.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
IP Multicast Commands 1038

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
If no interface is specified, the command displays the status parameters of all PIM-enabled
interfaces.
Format show ip pim interface [unit/slot/port | vlan vlan-id]
Modes Privileged EXEC
User EXEC
Term Definition
Interface unit/slot/port, which is the interface number.
Mode Indicates the active PIM mode enabled on the interface is dense or sparse.
Hello Interval The frequency at which PIM hello messages are transmitted on this interface. By default, the value is
30 seconds.
Join Prune Interval The join/prune interval value for the PIM router. The interval is in seconds.
DR Priority The priority of the Designated Router configured on the interface. This field is not applicable if the
interface mode is Dense.
BSR Border Identifies whether this interface is configured as a bootstrap router border interface.
Neighbor Count The number of PIM neighbors learned on this interface. This is a dynamic value and is shown only
when a PIM interface is operational.
Designated Router The IP address of the elected Designated Router for this interface. This is a dynamic value and will
only be shown when a PIM interface is operational. This field is not applicable if the interface mode
is Dense.
Command example:
(NETGEAR) #show ip pim interface
Interface.........................................1/0/1
Mode............................................Sparse
Hello Interval (secs)...........................30
Join Prune Interval (secs)......................60
DR Priority.....................................1
BSR Border......................................Disabled
Neighbor Count..................................1
Designated Router...............................192.168.10.1
Interface.........................................1/0/2
Mode............................................Sparse
Hello Interval (secs)...........................30
Join Prune Interval (secs)......................60
DR Priority.....................................1
BSR Border......................................Disabled
IP Multicast Commands 1039

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Neighbor Count..................................1
Designated Router...............................192.168.10.1
Command example:
If none of the interfaces are enabled for PIM, the following message is displayed:
None of the routing interfaces are enabled for PIM.
show ip pim neighbor
This command displays PIM neighbors discovered by PIMv2 Hello messages.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
If the interface number is not specified, the command displays the status parameters of all
PIM-enabled interfaces.
Format show ip pim neighbor [unit/slot/port | vlan vlan-id]
Modes Privileged EXEC
User EXEC
Term Definition
Neighbor Address The IP address of the PIM neighbor on an interface.
Interface unit/slot/port
Up Time The time since this neighbor has become active on this interface.
Expiry Time Time remaining for the neighbor to expire.
DR Priority The DR Priority configured on this Interface (PIM-SM only).
Note: DR Priority is applicable only when sparse-mode configured routers are neighbors.
Otherwise, NA is displayed in this field.
Command example:
(NETGEAR) #show ip pim neighbor 1/0/1
Neighbor Addr Interface Uptime Expiry Time DR
(hh:mm:ss) (hh:mm:ss) Priority
--------------- --------- ----------- ----------- --------
192.168.10.2 1/0/1 00:02:55 00:01:15 NA
IP Multicast Commands 1040

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR) #show ip pim neighbor
Neighbor Addr Interface Uptime Expiry Time DR
(hh:mm:ss) (hh:mm:ss) Priority
--------------- --------- ----------- ----------- --------
192.168.10.2 1/0/1 00:02:55 00:01:15 1
192.168.20.2 1/0/2 00:03:50 00:02:10 1
Command example:
If no neighbors were learned on any of the interfaces, the following message is displayed:
No neighbors exist on the router.
show ip pim bsr-router
This command displays the bootstrap router (BSR) information.
Format show ip pim bsr-router {candidate | elected}
Mode Privileged EXEC
User EXEC
Parameter Definition
BSR Address IP address of the BSR.
BSR Priority Priority as configured in the ip pim bsr-candidate command.
BSR Hash Mask Length Length of a mask (maximum 32 bits) that is to be ANDed with the group address before the
hash function is called. This value is configured in the ip pim bsr-candidate command.
C-BSR Advertisement Indicates the configured C-BSR Advertisement interval with which the router, acting as a
Interval C-BSR, will periodically send the C-BSR advertisement messages.
Next Bootstrap Time (in hours, minutes, and seconds) in which the next bootstrap message is due from this
Message BSR.
Command example:
(NETGEAR) #show ip pim bsr-router elected
BSR Address................................... 192.168.10.1
BSR Priority................................ 0
BSR Hash Mask Length........................ 30
Next Bootstrap message (hh:mm:ss)........... 00:00:24
IP Multicast Commands 1041

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR) #show ip pim bsr-router candidate
BSR Address................................... 192.168.10.1
BSR Priority................................ 0
BSR Hash Mask Length........................ 30
C-BSR Advertisement Interval (secs)......... 60
Next Bootstrap message (hh:mm:ss)........... NA
Command example:
If no configured or elected BSRs exist on the router, the following message is displayed:
No BSR's exist/learned on this router.
show ip pim rp-hash
This command displays the rendezvous point (RP) selected for the specified group address.
Format show ip pim rp-hash group-address
Modes Privileged EXEC
User EXEC
Term Definition
RP Address The IP address of the RP for the group specified.
Type Indicates the mechanism (BSR or static) by which the RP was selected.
Command example:
(NETGEAR) #show ip pim rp-hash 224.1.2.0
RP Address 192.168.10.1
Type Static
Command example:
If no RP Group mapping exist on the router, the following message is displayed:
No RP-Group mappings exist/learned on this router.
show ip pim rp mapping
Use this command to display the mapping for the PIM group to the active Rendezvous points
(RP) of which the router is a aware (either configured or learned from the bootstrap router
(BSR)). Use the optional parameters to limit the display to a specific RP address
(rp-address) or to view group-to-candidate RP (candidate) or group to Static RP
mapping information (static).
IP Multicast Commands 1042

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format show ip pim rp mapping [rp-address | candidate | static]
Modes Privileged EXEC
User EXEC
Term Definition
RP Address The IP address of the RP for the group specified.
Group Address The IP address of the multicast group.
Group Mask The subnet mask associated with the group.
Origin Indicates the mechanism (BSR or static) by which the RP was selected.
C-RP Indicates the configured C-RP Advertisement interval with which the router acting as a Candidate
Advertisement RP will periodically send the C-RP advertisement messages to the elected BSR.
Interval
Command example:
(NETGEAR) #show ip pim rp mapping 192.168.10.1
RP Address 192.168.10.1
Group Address 224.1.2.1
Group Mask 255.255.255.0
Origin Static
Command example:
(NETGEAR) #show ip pim rp mapping
R P Address 192.168.10.1
Group Address 224.1.2.1
Group Mask 255.255.255.0
Origin Static
RP Address 192.168.20.1
Group Address 229.2.0.0
Group Mask 255.255.0.0
Origin Static
Command example:
(NETGEAR) # show ip pim rp mapping candidate
RP Address.................................... 192.168.10.1
Group Address.............................. 224.1.2.1
Group Mask................................. 255.255.0.0
Origin..................................... BSR
IP Multicast Commands 1043

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
C-RP Advertisement Interval (secs)......... 60
Next Candidate RP Advertisement (hh:mm:ss). 00:00:15
Command example:
If no RP Group mapping exist on the router, the following message is displayed:
No RP-Group mappings exist on this router.
show ip pim statistics
This command displays statistics for the received PIM control packets per interface. This
command displays statistics only if PIM sparse mode is enabled.
Format show ip pim statistics
Modes Privileged EXEC
User EXEC
Term Definition
Stat • Rx packets received.
• Tx packets transmitted.
Interface The PIM-enabled routing interface.
Hello The number of PIM Hello messages.
Register The number of PIM Register messages.
Reg-Stop The number of PIM Register-stop messages.
Join/Pru The number of PIM Join/Prune messages.
BSR The number of PIM Boot Strap messages.
Assert The number of PIM Assert messages.
CRP The number of PIM Candidate RP Advertisement messages.
Command example:
(NETGEAR) #show ip pim statistics
=====================================================================
Interface Stat Hello Register Reg-Stop Join/Pru BSR Assert CRP
=====================================================================
Vl10 Rx 0 0 0 0 0 0 0
Tx 2 0 0 0 0 0 0
Invalid Packets Received - 0
---------------------------------------------------------------------
Vl20 Rx 0 0 0 5 0 0 0
Tx 8 7 0 0 0 0 0
IP Multicast Commands 1044

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Invalid Packets Received - 0
---------------------------------------------------------------------
1/0/5 Rx 0 0 6 5 0 0 0
Tx 10 9 0 0 0 0 0
Invalid Packets Received - 0
---------------------------------------------------------------------
Command example:
(NETGEAR) #show ip pim statistics vlan 10
=====================================================================
Interface Stat Hello Register Reg-Stop Join/Pru BSR Assert CRP
=====================================================================
Vl10 Rx 0 0 0 0 0 0 0
Tx 2 0 0 0 0 0 0
Invalid Packets Received - 0
---------------------------------------------------------------------
Command example:
(NETGEAR) #show ip pim statistics 1/0/5
=====================================================================
Interface Stat Hello Register Reg-Stop Join/Pru BSR Assert CRP
=====================================================================
1/0/5 Rx 0 0 6 5 0 0 0
Tx 10 9 0 0 0 0 0
Invalid Packets Received - 0
IP Multicast Commands 1045

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Internet Group Message Protocol
Commands
This section describes the commands you use to view and configure Internet Group Message
Protocol (IGMP) settings.
ip igmp
This command sets the administrative mode of IGMP in the system to active on an interface,
range of interfaces, or on all interfaces.
Default disabled
Format ip igmp
Modes Global Config
Interface Config
no ip igmp
This command sets the administrative mode of IGMP in the system to inactive.
Format no ip igmp
Modes Global Config
Interface Config
ip igmp header-validation
Use this command to enable header validation for IGMP messages.
Default disabled
Format ip igmp header-validation
Mode Global Config
no ip igmp header-validation
This command disables header validation for IGMP messages.
Format no ip igmp header-validation
Mode Global Config
IP Multicast Commands 1046

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip igmp version
This command configures the version of IGMP for an interface or range of interfaces. The
value for version is either 1, 2 or 3.
Default 3
Format ip igmp version version
Modes Interface Config
no ip igmp version
This command resets the version of IGMP to the default value.
Format no ip igmp version
Modes Interface Config
ip igmp last-member-query-count
This command sets the number of Group-Specific Queries sent by the interface or range of
interfaces before the router assumes that there are no local members on the interface. The
range for count is from 1 to 20.
Format ip igmp last-member-query-count count
Modes Interface Config
no ip igmp last-member-query-count
This command resets the number of Group-Specific Queries to the default value.
Format no ip igmp last-member-query-count
Modes Interface Config
ip igmp last-member-query-interval
This command configures the Maximum Response Time inserted in Group-Specific Queries
which are sent in response to Leave Group messages. The range for deciseconds is 0 to
255 tenths of a second. This value can be configured on one interface or a range of
interfaces
Default 10 tenths of a second (1 second)
Format ip igmp last-member-query-interval deciseconds
Modes Interface Config
IP Multicast Commands 1047

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip igmp last-member-query-interval
This command resets the Maximum Response Time to the default value.
Format no ip igmp last-member-query-interval
Modes Interface Config
ip igmp query-interval
This command configures the query interval for the specified interface or range of interfaces.
The query interval determines how fast IGMP Host-Query packets are transmitted on this
interface. The range for the seconds argument is 1 to 3600 seconds.
Default 125 seconds
Format ip igmp query-interval seconds
Modes Interface Config
no ip igmp query-interval
This command resets the query interval for the specified interface to the default value. This is
the frequency at which IGMP Host-Query packets are transmitted on this interface.
Format no ip igmp query-interval
Modes Interface Config
ip igmp query-max-response-time
This command configures the maximum response time interval for the specified interface or
range of interfaces, which is the maximum query response time advertised in IGMPv2
queries on this interface. The deciseconds argument is the time interval, specified in 0 to
255 tenths of a second.
Default 100
Format ip igmp query-max-response-time desciseconds
Mode Interface Config
no ip igmp query-max-response-time
This command resets the maximum response time interval for the specified interface, which
is the maximum query response time advertised in IGMPv2 queries on this interface to the
default value. The maximum response time interval is reset to the default time.
Format no ip igmp query-max-response-time
Mode Interface Config
IP Multicast Commands 1048

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip igmp robustness
This command configures the robustness that allows tuning of the interface or range of
interfaces. The robustness is the tuning for the expected packet loss on a subnet. If a subnet
is expected to have a lot of loss, the Robustness variable may be increased for the interface.
The number argument specifies the packet loss number in the range from 1 to 255.
Default 2
Format ip igmp robustness number
Mode Interface Config
no ip igmp robustness
This command sets the robustness value to default.
Format no ip igmp robustness
Mode Interface Config
ip igmp startup-query-count
This command sets the number of Queries sent out on startup, separated by the Startup
Query Interval on the interface or range of interfaces. The range for the number argument is
1 to 20.
Default 2
Format ip igmp startup-query-count number
Mode Interface Config
no ip igmp startup-query-count
This command resets the number of Queries sent out on startup, separated by the Startup
Query Interval on the interface to the default value.
Format no ip igmp startup-query-count
Mode Interface Config
ip igmp startup-query-interval
This command sets the interval between General Queries sent on startup on the interface or
range of interfaces. The time interval value is in seconds. The range for the seconds
argument is 1 to 300 seconds.
IP Multicast Commands 1049

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

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format show ip igmp interface {unit/slot/port | vlan vlan-id}
Modes Privileged EXEC
User EXEC
Term Definition
Interface unit/slot/port
IGMP Admin Mode The administrative status of IGMP.
Interface Mode Indicates whether IGMP is enabled or disabled on the interface.
IGMP Version The version of IGMP running on the interface. This value can be configured to create a router
capable of running either IGMP version 1 or 2.
Query Interval The frequency at which IGMP Host-Query packets are transmitted on this interface.
Query Max The maximum query response time advertised in IGMPv2 queries on this interface.
Response Time
Robustness The tuning for the expected packet loss on a subnet. If a subnet is expected to be have a lot of loss,
the Robustness variable may be increased for that interface.
Startup Query The interval between General Queries sent by a Querier on startup.
Interval
Startup Query The number of Queries sent out on startup, separated by the Startup Query Interval.
Count
Last Member The Maximum Response Time inserted into Group-Specific Queries sent in response to Leave
Query Interval Group messages.
Last Member The number of Group-Specific Queries sent before the router assumes that there are no local
Query Count members.
show ip igmp interface membership
This command displays the list of interfaces that registered in the multicast group. The
multiipaddr argument specifies the IP address of the multicast group.
Format show ip igmp interface membership multiipaddr [detail]
Mode Privileged EXEC
Term Definition
Interface Valid unit, slot and port number separated by forward slashes.
Interface IP The IP address of the interface participating in the multicast group.
State The interface that has IGMP in Querier mode or Non-Querier mode.
IP Multicast Commands 1052

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

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Number of Joins The number of times a group membership has been added on this interface.
Number of Groups The current number of membership entries for this interface.
IGMP Proxy Commands
The IGMP Proxy is used by IGMP Router (IPv4 system) to enable the system to issue IGMP
host messages on behalf of hosts that the system discovered through standard IGMP router
interfaces. With IGMP Proxy enabled, the system acts as proxy to all the hosts residing on its
router interfaces.
ip igmp-proxy
This command enables the IGMP Proxy on the an interface or range of interfaces. To enable
the IGMP Proxy on an interface, you must enable multicast forwarding. Also, make sure that
there are no multicast routing protocols enabled on the router.
Format ip igmp-proxy
Mode Interface Config
no ip igmp-proxy
This command disables the IGMP Proxy on the router.
Format no ip igmp-proxy
Mode Interface Config
ip igmp-proxy unsolicit-rprt-interval
This command sets the unsolicited report interval for the IGMP Proxy interface or range of
interfaces. This command is valid only when you enable IGMP Proxy on the interface or
range of interfaces. The value for the seconds argument is a number in the range 1–260
seconds.
Default 1
Format ip igmp-proxy unsolicit-rprt-interval seconds
Mode Interface Config
IP Multicast Commands 1054

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip igmp-proxy unsolicit-rprt-interval
This command resets the unsolicited report interval of the IGMP Proxy router to the default
value.
Format no ip igmp-proxy unsolicit-rprt-interval
Mode Interface Config
ip igmp-proxy reset-status
This command resets the host interface status parameters of the IGMP Proxy interface (or
range of interfaces). This command is valid only when you enable IGMP Proxy on the
interface.
Format ip igmp-proxy reset-status
Mode Interface Config
show ip igmp-proxy
This command displays a summary of the host interface status parameters. It displays the
following parameters only when you enable IGMP Proxy.
Format show ip igmp-proxy
Modes Privileged EXEC
User EXEC
Term Definition
Interface index The interface number of the IGMP Proxy.
Admin Mode States whether the IGMP Proxy is enabled or not. This is a configured value.
Operational Mode States whether the IGMP Proxy is operationally enabled or not. This is a status parameter.
Version The present IGMP host version that is operational on the proxy interface.
Number of The number of multicast groups that are associated with the IGMP Proxy interface.
Multicast Groups
Unsolicited Report The time interval at which the IGMP Proxy interface sends unsolicited group membership report.
Interval
Querier IP Address The IP address of the Querier, if any, in the network attached to the upstream interface (IGMP-Proxy
on Proxy Interface interface).
Older Version 1 The interval used to timeout the older version 1 queriers.
Querier Timeout
IP Multicast Commands 1055

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Older Version 2 The interval used to timeout the older version 2 queriers.
Querier Timeout
Proxy Start The number of times the IGMP Proxy has been stopped and started.
Frequency
Command example:
(NETGEAR Switch) #show ip igmp-proxy
Interface Index............................................. 1/0/1
Admin Mode................................................ Enable
Operational Mode......................................... Enable
Version......................................................... 3
Num of Multicast Groups............................. 0
Unsolicited Report Interval.......................... 1
Querier IP Address on Proxy Interface........ 5.5.5.50
Older Version 1 Querier Timeout................ 0
Older Version 2 Querier Timeout................ 00::00:00
Proxy Start Frequency................................. 1
show ip igmp-proxy interface
This command displays a detailed list of the host interface status parameters. It displays the
following parameters only when you enable IGMP Proxy.
Format show ip igmp-proxy interface
Modes Privileged EXEC
User EXEC
Term Definition
Interface Index The unit/slot/port of the IGMP proxy.
The column headings of the table associated with the interface are as follows.
Term Definition
Ver The IGMP version.
Query Rcvd Number of IGMP queries received.
Report Rcvd Number of IGMP reports received.
Report Sent Number of IGMP reports sent.
IP Multicast Commands 1056

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Leaves Rcvd Number of IGMP leaves received. Valid for version 2 only.
Leaves Sent Number of IGMP leaves sent on the Proxy interface. Valid for version 2 only.
Command example:
(NETGEAR Switch) #show ip igmp-proxy interface
Interface Index................................ 1/0/1
Ver Query Rcvd Report Rcvd Report Sent Leave Rcvd Leave Sent
------------------------------------------------------------------
1 0 0 0
2 0 0 0 0 0
3 0 0 0
show ip igmp-proxy groups
This command displays information about the subscribed multicast groups that IGMP Proxy
reported. It displays a table of entries with the following as the fields of each column.
Format show ip igmp-proxy groups
Modes Privileged EXEC
User EXEC
Term Definition
Interface The interface number of the IGMP Proxy.
Group Address The IP address of the multicast group.
Last Reporter The IP address of host that last sent a membership report for the current group on the network
attached to the IGMP Proxy interface (upstream interface).
Up Time (in secs) The time elapsed since last created.
Member State The status of the entry. Possible values are IDLE_MEMBER or DELAY_MEMBER.
• IDLE_MEMBER - interface has responded to the latest group membership query for this group.
• DELAY_MEMBER - interface is going to send a group membership report to respond to a group
membership query for this group.
Filter Mode Possible values are Include or Exclude.
Sources The number of sources attached to the multicast group.
IP Multicast Commands 1057

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show ip igmp-proxy groups
Interface Index................................ 1/0/1
G roup Address Last Reporter Up Time Member State F ilter Mode Sources
- ------------ - ------------- - --------- - ------------ - ------------ -------
2 25.4.4.4 5 .5.5.48 0 0:02:21 D ELAY_MEMBER I nclude 3
2 26.4.4.4 5.5.5.48 0 0:02:21 DELAY_MEMBER I nclude 3
2 27.4.4.4 5 .5.5.48 0 0:02:21 D ELAY_MEMBER E xclude 0
2 28.4.4.4 5 .5.5.48 0 0:02:21 DELAY_MEMBER I nclude 3
show ip igmp-proxy groups detail
This command displays complete information about multicast groups that IGMP Proxy
reported. It displays a table of entries with the following as the fields of each column.
Format show ip igmp-proxy groups detail
Modes Privileged EXEC
User EXEC
Term Definition
Interface The interface number of the IGMP Proxy.
Group Address The IP address of the multicast group.
Last Reporter The IP address of host that last sent a membership report for the current group, on the network
attached to the IGMP-Proxy interface (upstream interface).
Up Time (in secs) The time elapsed since last created.
Member State The status of the entry. Possible values are IDLE_MEMBER or DELAY_MEMBER.
• IDLE_MEMBER - interface has responded to the latest group membership query for this group.
• DELAY_MEMBER - interface is going to send a group membership report to respond to a group
membership query for this group.
Filter Mode Possible values are Include or Exclude.
Sources The number of sources attached to the multicast group.
Group Source List The list of IP addresses of the sources attached to the multicast group.
Expiry Time Time left before a source is deleted.
IP Multicast Commands 1058

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show ip igmp-proxy groups
Interface Index................................ 1/0/1
G roup Address Last Reporter Up Time Member State F ilter Mode Sources
------------- - ------------- - ---------- - ----------- - ----------- ---------
2 25.4.4.4 5 .5.5.48 0 0:02:21 D ELAY_MEMBER I nclude 3
G roup Source List Expiry Time
----------------- -----------------
5.1.2.3 00:02:21
6 .1.2.3 00:02:21
7.1.2.3 00:02:21
2 26.4.4.4 5 .5.5.48 0 0:02:21 D ELAY_MEMBER I nclude 3
Group Source List Expiry Time
----------------- -----------------
2.1.2.3 00:02:21
6 .1.2.3 00:01:44
8 .1.2.3 00:01:44
2 27.4.4.4 5 .5.5.48 0 0:02:21 D ELAY_MEMBER E xclude 0
2 28.4.4.4 5 .5.5.48 0 0:03:21 D ELAY_MEMBER I nclude 3
Group Source List Expiry Time
----------------- -----------------
9 .1.2.3 00:03:21
6 .1.2.3 00:03:21
7 .1.2.3 00:03:21
IP Multicast Commands 1059

IPv6 Multicast Commands

This chapter describes the IPv6 multicast commands.
The chapter contains the following sections:
• IPv6 Multicast Forwarder
• IPv6 PIM Commands
• IPv6 MLD Commands
• IPv6 MLD-Proxy Commands
Note: No specific command exists to enable multicast for IPv6. If you enable
multicast with a global config command, multicast is enabled for both
IPv4 and IPv6.
The commands in this chapter are in one of three functional groups:
• Show commands. Display switch settings, statistics, and other information.
• Configuration commands. Configure features and options of the switch. For every
configuration command, there is a show command that displays the configuration setting.
• Clear commands. Clear some or all of the settings to factory defaults.

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
IPv6 Multicast Forwarder
ipv6 mroute
This command configures an IPv6 Multicast Static Route for a source.
Default No MRoute is configured on the system.
Format ipv6 mroute src-ip-addr src-mask rpf-addr [interface] preference
Mode Global Config
Parameter Description
src-ip-addr The IP address of the multicast source network.
src-mask The IP mask of the multicast data source.
rpf-ip-addr The IP address of the RPF next-hop router toward the source.
interface [Optional] Specify the interface if the RPF Address is a link-local address.
preference The administrative distance for this Static MRoute, that is, the preference value. The range is 1 to
255.
no ipv6 mroute
This command removes the configured IPv6 Multicast Static Route.
Format no ip mroute src-ip-addr
Mode Global Config
Note: There is no specific IP multicast enable for IPv6. Enabling of multicast
at global config is common for both IPv4 and IPv6.
show ipv6 mroute
Use this command to show the mroute entries that are specific to IPv6. (This command is the
IPv6 equivalent of the IPv4 show ip mroute command.)
Format show ipv6 mroute [detail | summary]
Modes Privileged EXEC
User EXEC
IPv6 Multicast Commands 1061

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If you use the detail parameter, the command displays the following Multicast Route Table
fields.
Term Definition
Source IP Addr The IP address of the multicast data source.
Group IP Addr The IP address of the destination of the multicast packet.
Expiry Time The time of expiry of this entry in seconds.
Up Time The time elapsed since the entry was created in seconds.
RPF Neighbor The IP address of the RPF neighbor.
Flags The flags associated with this entry.
If you use the summary parameter, the command displays the following fields.
Term Definition
Source IP Addr The IP address of the multicast data source.
Group IP Addr The IP address of the destination of the multicast packet.
Protocol The multicast routing protocol by which the entry was created.
Incoming Interface The interface on which the packet for the source/group arrives.
Outgoing Interface List The list of outgoing interfaces on which the packet is forwarded.
show ipv6 mroute group
This command displays the multicast configuration settings specific to IPv6 such as flags,
timer settings, incoming and outgoing interfaces, RPF neighboring routers, and expiration
times of all the entries in the multicast route table containing the given group IPv6 address
group-address.
Format show ipv6 mroute group group-address {detail | summary}
Modes Privileged EXEC
User EXEC
Term Definition
Source IP Addr The IP address of the multicast data source.
Group IP Addr The IP address of the destination of the multicast packet.
Protocol The multicast routing protocol by which this entry was created.
Incoming Interface The interface on which the packet for this group arrives.
Outgoing Interface List The list of outgoing interfaces on which this packet is forwarded.
IPv6 Multicast Commands 1062

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ipv6 mroute source
This command displays the multicast configuration settings that are specific to IPv6 such as
flags, timer settings, incoming and outgoing interfaces, RPF neighboring routers, and
expiration times of all the entries in the multicast route table for the specified source IP
address (source-address).
Format show ipv6 mroute source source-address {detail | summary}
Modes Privileged EXEC
User EXEC
If you use the detail keyword, the command displays the following column headings in the
output table.
Term Definition
Source IP Addr The IP address of the multicast data source.
Group IP Addr The IP address of the destination of the multicast packet.
Expiry Time The time of expiry of this entry in seconds.
Up Time The time elapsed since the entry was created in seconds.
RPF Neighbor The IP address of the RPF neighbor.
Flags The flags associated with this entry.
If you use the summary keyword, the command displays the following column headings in
the output table.
Term Definition
Source IP Addr The IP address of the multicast data source.
Group IP Addr The IP address of the destination of the multicast packet.
Protocol The multicast routing protocol by which this entry was created.
Incoming Interface The interface on which the packet for this source arrives.
Outgoing Interface List The list of outgoing interfaces on which this packet is forwarded.
show ipv6 mroute static
Use the show ipv6 mroute static command in Privileged EXEC or User EXEC mode
to display all the configured IPv6 multicast static routes.
Format show ipv6 mroute static [source-address]
Modes Privileged EXEC
User EXEC
IPv6 Multicast Commands 1063

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
Source Address IP address of the multicast source network.
Source Mask The subnetwork mask pertaining to the sourceIP.
RPF Address The IP address of the RPF next-hop router toward the source.
Interface The interface that is used to reach the RPF next-hop. This is valid if the RPF address is a link-local
address.
Preference The administrative distance for this Static MRoute.
clear ipv6 mroute
This command deletes all or the specified IPv6 multicast route entries.
Note: This command clears only dynamic mroute entries. It does not clear
static mroutes.
Format clear ipv6 mroute {* | group-address [source-address]}
Modes Privileged EXEC
Parameter Description
* Deletes all IPv6 entries from the IPv6 multicast routing table.
group-address IPv6 address of the multicast group.
source-address The IPv6 address of a multicast source that is sending multicast traffic to the group.
The following example deletes all entries from the IPv6 multicast routing table:
(NETGEAR Switch) # clear ipv6 mroute *
Command example:
The following example deletes all entries from the IPv6 multicast routing table that match the
multicast group address (FF4E::1), irrespective of which source is sending for this group:
(NETGEAR Switch) # clear ipv6 mroute FF4E::1
Command example:
The following example deletes all entries from the IPv6 multicast routing table that match the
multicast group address (FF4E::1) and the multicast source address (2001::2):
(NETGEAR Switch) # clear ipv6 mroute FF4E::1 2001::2
IPv6 Multicast Commands 1064

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
IPv6 PIM Commands
This section describes the commands you use to configure Protocol Independent Multicast
-Dense Mode (PIM-DM) and Protocol Independent Multicast - Sparse Mode (PIM-SM) for
IPv6 multicast routing. PIM-DM and PIM-SM are multicast routing protocols that provides
scalable inter-domain multicast routing across the Internet, independent of the mechanisms
provided by any particular unicast routing protocol. Only one PIM mode can be operational at
a time.
ipv6 pim dense
This command enables the administrative mode of PIM-DM in the router.
Default disabled
Format ipv6 pim dense
Mode Global Config
Command example:
(NETGEAR) (Config) #ipv6 pim dense
no ipv6 pim dense
This command disables the administrative mode of PIM-DM in the router.
Format no ipv6 pim dense
Mode Global Config
ipv6 pim sparse
This command enables the administrative mode of PIM-SM in the router.
Default disabled
Format ipv6 pim sparse
Mode Global Config
Command example:
(NETGEAR) (Config) #ipv6 pim sparse
IPv6 Multicast Commands 1065

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ipv6 pim sparse
This command disables the administrative mode of PIM-SM in the router.
Format no ipv6 pim sparse
Mode Global Config
ipv6 pim
This command administratively enables PIM on an interface or range of interfaces.
Default disabled
Format ipv6 pim
Mode Interface Config
Command example:
(NETGEAR) (Interface 1/0/1) #ipv6 pim
no ipv6 pim
This command sets the administrative mode of PIM on an interface to disabled.
Format no ipv6 pim
Mode Interface Config
ipv6 pim hello-interval
Use this command to configure the PIM hello interval for the specified router interface or
range of interfaces. The seconds argument is the hello-interval, specified in the range
0–18000 seconds.
Default 30
Format ipv6 pim hello-interval seconds
Mode Interface Config
Command example:
(NETGEAR) (Interface 1/0/1) #ipv6 pim hello-interval 50
IPv6 Multicast Commands 1066

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ipv6 pim hello-interval
Use this command to set the PIM hello interval to the default value.
Format no ipv6 pim hello-interval
Mode Interface Config
ipv6 pim bsr-border
Use this command to prevent bootstrap router (BSR) messages from being sent or received
on the specified interface.
Note: This command takes effect only when PIM-SM is enabled in the
Global mode.
Default disabled
Format ipv6 pim bsr-border
Mode Interface Config
(NETGEAR) (Interface 1/0/1) #ipv6 pim bsr-border
no ipv6 pim bsr-border
Use this command to disable the setting of BSR border on the specified interface.
Format no ipv6 pim bsr-border
Mode Interface Config
ipv6 pim bsr-candidate
This command is used to configure the router to announce its candidacy as a bootstrap
router (BSR).
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
Note: This command takes effect only when PIM-SM is configured as the
PIM mode.
IPv6 Multicast Commands 1067

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default Disabled
Format ipv6 pim bsr-candidate interface {unit/slot/port | vlan vland-id}
hash-mask-length [bsr-priority] [interval interval]
Mode Global Config
Parameters Description
unit/slot/port Interface or VLAN number on this router from which the BSR address is derived, to make it a
candidate. This interface or VLAN must be enabled with PIM.
hash-mask-length Length of a mask (32 bits maximum) that is to be ANDed with the group address before the hash
function is called. All groups with the same seed hash correspond to the same RP. For example, if
this value was 24, only the first 24 bits of the group addresses matter. This allows you to get one RP
for multiple groups.
bsr-priority [Optional] Priority of the candidate BSR. The range is an integer from 0 to 255. The BSR with the
larger priority is preferred. If the priority values are the same, the router with the larger IPv6 address
is the BSR. The default value is 0.
interval [Optional] Indicates the BSR candidate advertisement interval. The range is from 1 to 16383
seconds. The default value is 60 seconds.
Command example:
(NETGEAR) (Config) #ipv6 pim bsr-candidate interface 1/0/1 32 5
(NETGEAR) (Config) #ipv6 pim bsr-candidate interface 1/0/1 32 5 interval 100
no ipv6 pim bsr-candidate
This command is used to remove the configured PIM Candidate BSR router.
Format no ipv6 pim bsr-candidate interface {unit/slot/port | vlan vland-id}
Mode Global Config
ipv6 pim dr-priority
Use this command to set the priority value for which a router is elected as the designated
router (DR). The priority argument is a value in the range of 0–2147483647.
Note: This command takes effect only when PIM-SM is enabled in the
Global mode.
IPv6 Multicast Commands 1068

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default 1
Format ipv6 pim dr-priority priority
Mode Interface Config
Command example:
(NETGEAR) (Interface 1/0/1) #ipv6 pim dr-priority 10
no ipv6 pim dr-priority
Use this command to return the DR Priority on the specified interface to its default value.
Format no ipv6 pim dr-priority
Mode Interface Config
ipv6 pim join-prune-interval
This command is used to configure the join/prune interval for the PIM-SM router on an
interface or range of interfaces. The join/prune interval is specified in seconds. The seconds
argument can be configured as a value from 0 to 18000 seconds.
Note: This command takes effect only when PIM-SM is enabled in the
Global mode.
Default 60
Format ipv6 pim join-prune-interval seconds
Mode Interface Config
Command example: The following shows examples of the command.
(NETGEAR) (Interface 1/0/1) #ipv6 pim join-prune-interval 90
no ipv6 pim join-prune-interval
Use this command to set the join/prune interval on the specified interface to the default value.
Format no ipv6 pim join-prune-interval
Mode Interface Config
IPv6 Multicast Commands 1069

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ipv6 pim rp-address
This command defines the address of a PIM Rendezvous point (RP) for a specific multicast
group range.
Note: This command takes effect only when PIM-SM is configured as the
PIM mode.
Default 0
Format ipv6 pim rp-address rp-address group-address/prefix-length [override]
Mode Global Config
Parameter Description
rp-address The IPv6 address of the RP.
group-address/ The group address and prefix length supported by the RP.
prefix-length
override [Optional] Indicates that if there is a conflict, the RP configured with this command prevails over the
RP learned by BSR.
no ipv6 pim rp-address
This command is used to remove the address of the configured PIM Rendezvous point (RP)
for the specified multicast group range.
Format no ipv6 pim rp-address rp-address group-address/prefix-length [override]
Mode Global Config
ipv6 pim rp-candidate
This command is used to configure the router to advertise itself as a PIM candidate
rendezvous point (RP) to the bootstrap router (BSR) for a specific multicast group range.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
Note: This command takes effect only when PIM-SM is configured as the
PIM mode.
IPv6 Multicast Commands 1070

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default Disabled
Format ipv6 pim rp-candidate interface {unit/slot/port | vlan vland-id}
group-address group-mask [interval interval]
Mode Global Config
Parameter Description
unit/slot/port or The interface type in the unit/slot/port format or the VLAN ID is advertised as a candidate RP
vland-id address. This interface or VLAN must be enabled with PIM.
group-address The multicast group address that is advertised in association with the RP address.
group-mask The multicast group prefix that is advertised in association with the RP address.
interval [Optional] Indicates the RP candidate advertisement interval. The range is from 1 to 16383 seconds.
The default value is 60 seconds.
no ipv6 pim rp-candidate
This command is used to disable the router to advertise itself as a PIM candidate rendezvous
point (RP) to the bootstrap router (BSR).
Format no ipv6 pim rp-candidate interface {unit/slot/port | vlan vlan-id}
group-address group-mask
Mode Global Config
ipv6 pim ssm
Use this command to define the Source Specific Multicast (SSM) range of IPv6 multicast
addresses on the router.
Note: This command takes effect only when PIM-SM is configured as the
PIM mode.
Note: Some platforms do not support a non-zero data threshold rate. For
these platforms, only a “Switch on First Packet” policy is supported.
Default disabled
Format ipv6 pim ssm {default | group-address group-mask}
Mode Global Config
IPv6 Multicast Commands 1071

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
default Defines the SSM range access list FF3x::/32.
no ipv6 pim ssm
Use this command to remove the Source Specific Multicast (SSM) range of IP multicast
addresses on the router.
Format no ipv6 pim ssm {default | group-address group-mask}
Mode Global Config
show ipv6 pim
This command displays the system-wide information for PIM-DM or PIM-SM.
Format show ipv6 pim
Modes Privileged EXEC
User EXEC
Note: If the PIM mode is PIM-DM (dense), some of the fields in the following
table do not display in the command output because they are
applicable only to PIM-SM.
Term Definition
PIM Mode Indicates whether the PIM mode is dense (PIM-DM) or sparse (PIM-SM)
Interface unit/slot/port
Interface Mode Indicates whether PIM is enabled or disabled on this interface.
Operational Status The current state of PIM on this interface: Operational or Non-Operational.
The following example displays PIM Mode - Dense:
(NETGEAR) #show ipv6 pim
PIM Mode Dense
Interface Interface-Mode Operational-Status
--------- -------------- ------------------
1/0/1 Enabled Operational
1/0/3 Disabled Non-Operational
IPv6 Multicast Commands 1072

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
The following example displays PIM Mode - Sparse:
(NETGEAR) #show ipv6 pim
P IM Mode Sparse
Interface Interface-Mode Operational-Status
--------- -------------- ------------------
1/0/1 Enabled Operational
1/0/3 Disabled Non-Operational
Command example:
The following example shows that PIM is not configured:
(NETGEAR) #show ipv6 pim
PIM Mode None
None of the routing interfaces are enabled for PIM.
show ipv6 pim ssm
This command displays the configured source specific IPv6 multicast addresses. If no SSM
Group range is configured, the command output show the following message:
No SSM address range is configured.
Format show ipv6 pim ssm
Modes Privileged EXEC
User EXEC
Term Definition
Group Address The IPv6 multicast address of the SSM group.
Prefix Length The network prefix length.
show ipv6 pim interface
This command displays the interface information for PIM on the specified interface.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
IPv6 Multicast Commands 1073

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If no interface is specified, the command displays the status parameters for all PIM-enabled
interfaces.
Format show ipv6 pim interface [unit/slot/port | vlan vland-id]
Modes Privileged EXEC
User EXEC
Term Definition
Interface unit/slot/port
Mode Indicates whether the PIM mode enabled on the interface is dense or sparse.
Hello Interval The frequency at which PIM hello messages are transmitted on this interface. By default, the value is
30 seconds.
Join Prune Interval The join/prune interval for the PIM router. The interval is in seconds.
DR Priority The priority of the Designated Router configured on the interface. This field is not applicable if the
interface mode is Dense
BSR Border Identifies whether this interface is configured as a bootstrap router border interface.
Neighbor Count The number of PIM neighbors learned on this interface. This is a dynamic value and is shown only
when a PIM interface is operational.
Designated Router The IP address of the elected Designated Router for this interface. This is a dynamic value and will
only be shown when a PIM interface is operational. This field is not applicable if the interface mode
is Dense
Command example:
(NETGEAR) #show ipv6 pim interface
Interface.........................................1/0/1
Mode............................................Sparse
Hello Interval (secs)...........................30
Join Prune Interval (secs)......................60
DR Priority.....................................1
BSR Border......................................Disabled
Neighbor Count..................................1
Designated Router...............................192.168.10.1
Interface.........................................1/0/2
Mode............................................Sparse
Hello Interval (secs)...........................30
Join Prune Interval (secs)......................60
DR Priority.....................................1
BSR Border......................................Disabled
Neighbor Count..................................1
Designated Router...............................192.168.10.1
IPv6 Multicast Commands 1074

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
If none of the interfaces are enabled for PIM, the following message is displayed:
None of the routing interfaces are enabled for PIM.
show ipv6 pim neighbor
This command displays PIM neighbors discovered by PIMv2 Hello messages.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
If the interface number is not specified, this command displays the neighbors discovered on
all the PIM-enabled interfaces.
Format show ipv6 pim neighbor [{unit/slot/port | vlan vland-id]
Modes Privileged EXEC
User EXEC
Term Definition
Neighbor Address The IPv6 address of the PIM neighbor on an interface.
Interface unit/slot/port
Up Time The time since this neighbor has become active on this interface.
Expiry Time Time remaining for the neighbor to expire.
DR Priority The DR Priority configured on this Interface (PIM-SM only).
Note: DR Priority is applicable only when sparse-mode configured routers are neighbors.
Otherwise, NA is displayed in this field.
Command example:
(NETGEAR) #show ipv6 pim neighbor
Neighbor Addr I nterface Uptime Expiry Time
( HH:MM::SS) (HH:MM::SS)
- ---------------- - -------- ----------- -----------
2001:DB8:39::/32 1/0/1 00:02:55 00:01:15
2 001:DB8:A3::/32 1/0/2 00:03:50 00:02:10
Command example:
If no neighbors were learned on any of the interfaces, the following message is displayed:
No neighbors are learnt on any interface.
IPv6 Multicast Commands 1075

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ipv6 pim bsr-router
This command displays the bootstrap router (BSR) information.
Format show ipv6 pim bsr-router {candidate | elected}
Mode Privileged EXEC
User EXEC
Term Definition
BSR Address IPv6 address of the BSR.
BSR Priority Priority as configured in the ipv6 pim bsr-candidate command.
BSR Hash Mask Length Length of a mask (maximum 32 bits) that is to be ANDed with the group address before the
hash function is called. This value is configured in the ipv6 pim bsr-candidate command.
C-BSR Advertisement Indicates the configured C-BSR Advertisement interval with which the router, acting as a
Interval C-BSR, will periodically send the C-BSR advertisement messages.
Next Bootstrap Time (in hours, minutes, and seconds) in which the next bootstrap message is due from this
Message BSR.
Command example:
(NETGEAR) #show ipv6 pim bsr-router elected
BSR Address................................... 192.168.10.1
BSR Priority................................ 0
BSR Hash Mask Length........................ 30
Next Bootstrap message (hh:mm:ss)........... 00:00:24
Command example:
(NETGEAR) #show ipv6 pim bsr-router candidate
BSR Address................................... 192.168.10.1
BSR Priority................................ 0
BSR Hash Mask Length........................ 30
C-BSR Advertisement Interval (secs)......... 60
Next Bootstrap message (hh:mm:ss)........... NA
Command example:
If no configured or elected BSRs exist on the router, the following message is displayed:
No BSR's exist/learned on this router.
IPv6 Multicast Commands 1076

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ipv6 pim rp-hash
This command displays which rendezvous point (RP) is being used for a specified group that
you must specify with the group-address argument.
Format show ipv6 pim rp-hash group-address
Modes Privileged EXEC
User EXEC
Term Definition
RP Address The IPv6 address of the RP for the group specified.
Type Indicates the mechanism (BSR or static) by which the RP was selected.
Command example:
(NETGEAR) #show ipv6 pim rp-hash 224.1.2.0
RP Address192.168.10.1
Type Static
Command example:
If no RP Group mapping exists on the router, the following message is displayed:
No RP-Group mappings exist/learned on this router.
show ipv6 pim rp mapping
Use this command to display the mapping for the PIM group to the active Rendezvous points
(RP) of which the router is a aware (either configured or learned from the bootstrap router
[BSR]). Use the optional parameters to limit the display to a specific RP address
(rp-address) or to view group-to-candidate RP (candidate) or group to Static RP
mapping information (static).
Format show ipv6 pim rp mapping [rp-address | candidate | static]
Modes Privileged EXEC
User EXEC
Term Definition
RP Address The IPv6 address of the RP for the group specified.
Group Address The IPv6 address and prefix length of the multicast group.
IPv6 Multicast Commands 1077

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Origin Indicates the mechanism (BSR or static) by which the RP was selected.
C-RP Indicates the configured C-RP Advertisement interval with which the router acting as a Candidate
Advertisement RP will periodically send the C-RP advertisement messages to the elected BSR.
Interval
Command example:
(NETGEAR) #show ipv6 pim rp mapping 192.168.10.1
R P Address 192.168.10.1
Group Address 224.1.2.1
Group Mask 255.255.255.0
Origin Static
Command example:
(NETGEAR) #show ipv6 pim rp mapping
RP Address 192.168.10.1
Group Address 224.1.2.1
Group Mask 255.255.255.0
Origin Static
R P Address 192.168.20.1
Group Address 229.2.0.0
Group Mask 255.255.0.0
Origin Static
Command example:
(NETGEAR) # show ipv6 pim rp mapping candidate
RP Address.................................... 192.168.10.1
Group Address.............................. 224.1.2.1
Group Mask................................. 255.255.0.0
Origin..................................... BSR
C-RP Advertisement Interval (secs)......... 60
Next Candidate RP Advertisement (hh:mm:ss). 00:00:15
Command example:
If no RP Group mapping exist on the router, the following message is displayed:
No RP-Group mappings exist on this router.
IPv6 Multicast Commands 1078

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ipv6 pim statistics
This command displays statistics for the received PIM control packets per interface. This
command displays statistics only if PIM sparse mode is enabled.
Format show ipv6 pim statistics
Modes Privileged EXEC
User EXEC
Term Definition
Stat • Rx packets received.
• Tx packets transmitted.
Interface The PIM-enabled routing interface.
Hello The number of PIM Hello messages.
Register The number of PIM Register messages.
Reg-Stop The number of PIM Register-stop messages.
Join/Pru The number of PIM Join/Prune messages.
BSR The number of PIM Boot Strap messages.
Assert The number of PIM Assert messages.
CRP The number of PIM Candidate RP Advertisement messages.
Command example:
(NETGEAR) #show ipv6 pim statistics
=====================================================================
Interface Stat Hello Register Reg-Stop Join/Pru BSR Assert CRP
=====================================================================
Vl10 Rx 0 0 0 0 0 0 0
Tx 2 0 0 0 0 0 0
Invalid Packets Received - 0
---------------------------------------------------------------------
Vl20 Rx 0 0 0 5 0 0 0
Tx 8 7 0 0 0 0 0
Invalid Packets Received - 0
---------------------------------------------------------------------
1/0/5 Rx 0 0 6 5 0 0 0
Tx 10 9 0 0 0 0 0
Invalid Packets Received - 0
---------------------------------------------------------------------
IPv6 Multicast Commands 1079

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
