# ls_request_1_1_ls_update_141_42_ls_acknowledgment_40_135_show_ip_ospf_lsa-group

Pages: 771-775

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
No Neighbor at The number of OSPF packets dropped because the sender is not an existing neighbor or the
Source Address sender’s IP address does not match the previously recorded IP address for that neighbor.
Note: Does not apply to Hellos.
Invalid OSPF The number of OSPF packets discarded because the packet type field in the OSPF header is not a
Packet Type known type.
Hellos Ignored The number of received Hello packets that were ignored by this router from the new neighbors after
the limit has been reached for the number of neighbors on an interface or on the system as a whole.
The following table lists the number of OSPF packets of each type sent and received on the
interface.
Packet Type Sent Received
Hello 6960 6960
Database Description 3 3
LS Request 1 1
LS Update 141 42
LS Acknowledgment 40 135
show ip ospf lsa-group
This command displays the number of self-originated LSAs within each LSA group.
Format show ip ospf lsa-group
Modes Privileged EXEC
User EXEC
Field Description
Total self-originated LSAs The number of LSAs the router is currently originating.
Average LSAs per group The number of self-originated LSAs divided by the number of LSA groups. The
number of LSA groups is the refresh interval (1800 seconds) divided by the pacing
interval (configured with timers pacing lsa-group) plus two.
Pacing group limit The maximum number of self-originated LSAs in one LSA group. If the number of
LSAs in a group exceeds this limit, OSPF redistributes LSAs throughout the refresh
interval to achieve better balance.
Groups For each LSA pacing group, the output shows the range of LSA ages in the group
and the number of LSAs in the group.
Routing Commands 771

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ip ospf neighbor
This command displays information about OSPF neighbors. If you do not specify a neighbor
IP address, the output displays summary information in a table. If you specify an interface or
tunnel, only the information for that interface or tunnel displays.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vlan-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in a unit/slot/port format. The vlan-id can
be a number from 1–4093.
The ip-address argument is the IP address of the neighbor, and when you specify this,
detailed information about the neighbor displays.
Format show ip ospf neighbor [interface {unit/slot/port | vlan vland-id}]
[ip-address]
Modes Privileged EXEC
User EXEC
If you do not specify an IP address, a table with the following columns displays for all
neighbors or the neighbor associated with the interface that you specify:
Term Definition
Router ID The 4-digit dotted-decimal number of the neighbor router.
Priority The OSPF priority for the specified interface. The priority of an interface is a priority integer from 0 to
255. A value of '0' indicates that the router is not eligible to become the designated router on this
network.
IP Address The IP address of the neighbor.
Interface The interface of the local router in unit/slot/port format.
State The state of the neighboring routers. Possible values are:
• Down. Initial state of the neighbor conversation; no recent information has been received from
the neighbor.
• Attempt. No recent information has been received from the neighbor but a more concerted
effort should be made to contact the neighbor.
• Init. An Hello packet has recently been seen from the neighbor, but bidirectional communication
has not yet been established.
• 2 way. Communication between the two routers is bidirectional.
• Exchange start. The first step in creating an adjacency between the two neighboring routers,
the goal is to decide which router is the master and to decide upon the initial DD sequence
number.
• Exchange. The router is describing its entire link state database by sending Database
Description packets to the neighbor.
• Loading. Link State Request packets are sent to the neighbor asking for the more recent LSAs
that have been discovered (but not yet received) in the Exchange state.
• Full. The neighboring routers are fully adjacent and they will now appear in router-LSAs and
network-LSAs.
Dead Time The amount of time, in seconds, to wait before the router assumes the neighbor is unreachable.
Routing Commands 772

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If you specify an IP address for the neighbor router, the following fields display.
Term Definition
Interface unit/slot/port
Neighbor IP The IP address of the neighbor router.
Address
Interface Index The interface ID of the neighbor router.
Area ID The area ID of the OSPF area associated with the interface.
Options An integer value that indicates the optional OSPF capabilities supported by the neighbor. The
neighbor's optional OSPF capabilities are also listed in its Hello packets. This enables received
Hello Packets to be rejected (that is, neighbor relationships will not even start to form) if there is a
mismatch in certain crucial OSPF capabilities.
Router Priority The OSPF priority for the specified interface. The priority of an interface is a priority integer from 0 to
255. A value of 0 indicates that the router is not eligible to become the designated router on this
network.
Dead Timer Due The amount of time, in seconds, to wait before the router assumes the neighbor is unreachable.
Up Time Neighbor uptime; how long since the adjacency last reached the Full state.
State The state of the neighboring routers.
Events The number of times this neighbor relationship has changed state, or an error has occurred.
Retransmitted The number of LSAs retransmitted to this neighbor.
LSAs
Retransmission An integer representing the current length of the retransmission queue of the specified neighbor
Queue Length router Id of the specified interface.
Restart Helper Indicates the status of this router as a helper during a graceful restart of the router specified in the
Status command line:
• Helping. This router is acting as a helpful neighbor to this neighbor. A helpful neighbor does not
report an adjacency change during graceful restart, but continues to advertise the restarting
router as a FULL adjacency. A helpful neighbor continues to forward data packets to the
restarting router, trusting that the restarting router's forwarding table is maintained during the
restart.
• Not Helping. This router is not a helpful neighbor at this time.
Restart Reason When this router is in helpful neighbor mode, this indicates the reason for the restart as provided by
the restarting router:
• Unknown (0)
• Software restart (1)
• Software reload/upgrade (2)
• Switch to redundant control processor (3)
• Unrecognized - a value not defined in RFC 3623
When the switch sends a grace LSA, it sets the Restart Reason to Software Restart on a planned
warm restart (when the initiate failover command is invoked), and to Unknown on an
unplanned warm restart.
Routing Commands 773

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Remaining Grace The number of seconds remaining the in current graceful restart interval. This is displayed only when
Time this router is currently acting as a helpful neighbor for the router specified in the command.
Restart Helper Exit Indicates the reason that the specified router last exited a graceful restart.
Reason • None. Graceful restart has not been attempted
• In Progress. Restart is in progress
• Completed. The previous graceful restart completed successfully
• Timed Out. The previous graceful restart timed out
• Topology Changed. The previous graceful restart terminated prematurely because of a
topology change
Command example:
(alpha1) #show ip ospf neighbor 170.1.1.50
Interface.....................................0/17
Neighbor IP Address...........................170.1.1.50
Interface Index...............................17
Area Id.......................................0.0.0.2
Options.......................................0x2
Router Priority...............................1
Dead timer due in (secs)......................15
Up Time.......................................0 days 2 hrs 8 mins 46 secs
State.........................................Full/BACKUP-DR
Events........................................4
Retransmitted LSAs............................32
Retransmission Queue Length...................0
Restart Helper Status........................ Helping
Restart Reason............................... Software Restart (1)
Remaining Grace Time......................... 10 sec
Restart Helper Exit Reason................... In Progress
show ip ospf range
This command displays the set of OSPFv2 area ranges configured for a given area.
Format show ip ospf range area-id
Modes Privileged EXEC
Term Definition
Prefix The summary prefix.
Subnet Mask The subnetwork mask of the summary prefix.
Type S (Summary Link) or E (External Link)
Routing Commands 774

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Action Advertise or Suppress
Cost Metric to be advertised when the range is active. If a static cost is not configured, the field displays
Auto. If the action is Suppress, the field displays N/A.
Active Whether the range is currently active. Y or N.
Command example:
(R1) #show ip ospf range 0
Prefix Subnet Mask Type Action Cost Active
10.1.0.0 255.255.0.0 S Advertise Auto N
172.20.0.0 255.255.0.0 S Advertise 500 Y
show ip ospf statistics
This command displays information about recent Shortest Path First (SPF) calculations. The
SPF is the OSPF routing table calculation. The output lists the number of times the SPF has
run for each OSPF area. A table follows this information. For each of the 15 most recent SPF
runs, the command shows statistics for how long ago the SPF ran, how long the SPF took,
the reasons why the SPF was scheduled, the individual components of the routing table
calculation time and to show the RIB update time. The most recent statistics are displayed at
the end of the table.
Format show ip ospf statistics
Modes Privileged EXEC
Term Definition
Delta T The time since the routing table was computed. The time is in the format hours, minutes, and
seconds (hh:mm:ss).
Intra The time taken to compute intra-area routes, in milliseconds.
Summ The time taken to compute inter-area routes, in milliseconds.
Ext The time taken to compute external routes, in milliseconds.
SPF Total The total time to compute routes, in milliseconds. The total may exceed the sum of the Intra, Summ,
and Ext times.
Routing Commands 775
