# ospf_mtu-ignore_shows_whether_to_ignore_mtu_mismatches_in_database_descriptor_packets_sent_from

Pages: 897-903

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Passive Status Shows whether the interface is passive or not.
OSPF MTU-ignore Shows whether to ignore MTU mismatches in database descriptor packets sent from
neighboring routers.
Link LSA Suppression The configured state of Link LSA Suppression for the interface.
The following information only displays if OSPF is initialized on the interface.
Term Definition
OSPF Interface Type Broadcast LANs, such as Ethernet and IEEE 802.5, take the value broadcast. The
OSPF Interface Type is broadcast.
State The OSPF Interface States are: down, loopback, waiting, point-to-point, designated
router, and backup designated router.
Designated Router The router ID representing the designated router.
Backup Designated Router The router ID representing the backup designated router.
Number of Link Events The number of link events.
Metric Cost The cost of the OSPF interface.
show ipv6 ospf interface brief
This command displays brief information for the physical interface or virtual interface tables.
Format show ipv6 ospf interface brief
Modes Privileged EXEC
User EXEC
Term Definition
Interface unit/slot/port
OSPF Admin Mode States whether OSPF is enabled or disabled on a router interface.
OSPF Area ID The OSPF Area ID for the specified interface.
Router Priority The router priority. The router priority determines which router is the designated router.
Metric Cost The priority of the path. Low costs have a higher priority than high costs.
Hello Interval The frequency, in seconds, at which the interface sends Hello packets.
Dead Interval The amount of time, in seconds, the interface waits before assuming a neighbor is down.
Retransmit Interval The frequency, in seconds, at which the interface sends LSA.
IPv6 Commands 897

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Retransmit Delay The number of seconds the interface adds to the age of LSA packets before transmission.
Interval
LSA Ack Interval The amount of time, in seconds, the interface waits before sending an LSA acknowledgement
after receiving an LSA.
show ipv6 ospf interface stats
This command displays the statistics for a specific interface. The command displays
information only if OSPF is enabled.
Format show ipv6 ospf interface stats unit/slot/port
Modes Privileged EXEC
User EXEC
Term Definition
OSPFv3 Area ID The area id of this OSPF interface.
IP Address The IP address associated with this OSPF interface.
OSPFv3 Interface The number of times the specified OSPF interface has changed its state, or an error has
Events occurred.
Virtual Events The number of state changes or errors that occurred on this virtual link.
Neighbor Events The number of times this neighbor relationship has changed state, or an error has occurred.
Packets Received The number of OSPFv3 packets received on the interface.
Packets Transmitted The number of OSPFv3 packets sent on the interface.
LSAs Sent The total number of LSAs flooded on the interface.
LSA Acks Received The total number of LSA acknowledged from this interface.
LSA Acks Sent The total number of LSAs acknowledged to this interface.
Sent Packets The number of OSPF packets transmitted on the interface.
Received Packets The number of valid OSPF packets received on the interface.
Discards The number of received OSPF packets discarded because of an error in the packet or an error in
processing the packet.
Bad Version The number of received OSPF packets whose version field in the OSPF header does not match
the version of the OSPF process handling the packet.
Virtual Link Not Found The number of received OSPF packets discarded where the ingress interface is in a
non-backbone area and the OSPF header identifies the packet as belonging to the backbone,
but OSPF does not have a virtual link to the packet’s sender.
Area Mismatch The number of OSPF packets discarded because the area ID in the OSPF header is not the area
ID configured on the ingress interface.
IPv6 Commands 898

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Invalid Destination The number of OSPF packets discarded because the packet’s destination IP address is not the
Address address of the ingress interface and is not the AllDrRouters or AllSpfRouters multicast
addresses.
No Neighbor at Source The number of OSPF packets dropped because the sender is not an existing neighbor or the
Address sender’s IP address does not match the previously recorded IP address for that neighbor. NOTE:
Does not apply to Hellos.
Invalid OSPF Packet The number of OSPF packets discarded because the packet type field in the OSPF header is not
Type a known type.
Hellos Ignored The number of received Hello packets that were ignored by this router from the new neighbors
after the limit has been reached for the number of neighbors on an interface or on the system as
a whole.
The table in trapflags (OSPF) on page744 lists the number of OSPF packets of each type
sent and received on the interface.
show ipv6 ospf lsa-group
This command displays the number of self-originated LSAs within each LSA group.
Format show ipv6 ospf lsa-group
Modes Privileged EXEC
User EXEC
Term Definition
Total The number of LSAs the router is currently originating.
self-originated
LSAs
Average LSAs per The number of self-originated LSAs divided by the number of LSA groups. The number of LSA
group groups is the refresh interval (1800 seconds) divided by the pacing interval (configured with the
timers pacing lsa-group command) plus two.
Pacing group limit The maximum number of self-originated LSAs in one LSA group. If the number of LSAs in a group
exceeds this limit, OSPF redistributes LSAs throughout the refresh interval to achieve better
balance.
Groups For each LSA pacing group, the output shows the range of LSA ages in the group and the number of
LSAs in the group.
Command example:
(R1) #show ipv6 ospf lsa-group
Total self-originated LSAs: 3019
Average LSAs per group: 100
Pacing group limit: 400
Number of self-originated LSAs within each LSA group...
IPv6 Commands 899

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Group Start Age Group End Age Count
0 59 96
60 119 88
120 179 102
180 239 95
240 299 95
300 359 92
360 419 48
420 479 58
480 539 103
540 599 99
600 659 119
660 719 110
720 779 106
780 839 122
840 899 110
900 959 99
960 1019 135
1020 1079 101
1080 1139 94
1140 1199 115
1200 1259 110
1260 1319 111
1320 1379 111
1380 1439 99
1440 1499 102
1500 1559 96
1560 1619 106
1620 1679 111
1680 1739 106
1740 1799 80
1800 1859 0
1860 1919 0
show ipv6 ospf max-metric
This command displays the configured maximum metrics for stub-router mode.
Format show ipv6 ospf max-metric
Modes Privileged EXEC
User EXEC
Command example:
(config)#show ipv6 ospf max-metric
IPv6 Commands 900

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
OSPFv3 Router with ID (3.3.3.3)
Start time: 00:00:00, Time elapsed: 00:01:05
Originating router-LSAs with maximum metric
Condition: on startup for 1000 seconds, State: inactive
Advertise external-LSAs with metric 16711680
show ipv6 ospf neighbor
This command displays information about OSPF neighbors. If you do not specify a neighbor
IP address, the output displays summary information in a table. If you specify an interface or
tunnel, only the information for that interface or tunnel displays.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vlan-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in a unit/slot/port format. The vlan-id can
be a number from 1–4093. You can also use the tunnel keyword with the tunnel-id
argument to specify a tunnel.
The ip-address is the IP address of the neighbor, and when you specify this, detailed
information about the neighbor displays. The information displays only if OSPF is enabled
and the interface has a neighbor.
Format show ipv6 ospf neighbor [interface {unit/slot/port | vlan vlan-id | tunnel
tunnel-id}] [ip-address]
Modes Privileged EXEC
User EXEC
If you do not specify an IP address, a table with the following columns displays for all
neighbors or the neighbor associated with the interface that you specify.
Term Definition
Router ID The 4-digit dotted-decimal number of the neighbor router.
Priority The OSPF priority for the specified interface. The priority of an interface is a priority integer from 0 to
255. A value of 0 indicates that the router is not eligible to become the designated router on this
network.
Intf ID The interface ID of the neighbor.
Interface The interface of the local router in unit/slot/port format.
IPv6 Commands 901

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
State The state of the neighboring routers. Possible values are:
• Down. The initial state of the neighbor conversation. No recent information was received from
the neighbor.
• Attempt. No recent information was received from the neighbor but an attempt was made to
contact the neighbor.
• Init. An Hello packet from the neighbor was detected, but bidirectional communication is not yet
established.
• 2 way. Communication between the two routers is bidirectional.
• Exchange start. The two neighboring routers attempt to establish the master and the initial DD
sequence number.
• Exchange. The router is sending Database Description packets to the neighbor.
• Full. The neighboring routers are fully adjacent and appear in router-LSAs and network-LSAs.
Dead Time The amount of time, in seconds, to wait before the router assumes the neighbor is unreachable.
Restart Helper Indicates the status of this router as a helper during a graceful restart of the router specified in the
Status command line:
• Helping. The router is acting as a helpful neighbor to the specified router.
• Not Helping. The router is not a helpful neighbor at this time.
Restart Reason When this router is in helpful neighbor mode, this indicates the reason for the restart as provided by
the restarting router.
Remaining Grace The number of seconds remaining the in current graceful restart interval. This is displayed only when
Time this router is currently acting as a helpful neighbor for the router specified in the command.
Restart Helper Exit Indicates the reason that the specified router last exited a graceful restart.
Reason • None. Graceful restart has not been attempted
• In Progress. Restart is in progress
• Completed. The previous graceful restart completed successfully
• Timed Out. The previous graceful restart timed out
• Topology Changed. The previous graceful restart terminated prematurely because of a
topology change
If you specify an IP address for the neighbor router, the following fields display.
Term Definition
Interface The interface of the local router in unit/slot/port format.
Area ID The area ID associated with the interface.
Options An integer value that indicates the optional OSPF capabilities supported by the neighbor. These are
listed in its Hello packets. This enables received Hello Packets to be rejected (that is, neighbor
relationships will not even start to form) if there is a mismatch in certain crucial OSPF capabilities.
Router Priority The router priority for the specified interface.
Dead Timer Due The amount of time, in seconds, to wait before the router assumes the neighbor is unreachable.
State The state of the neighboring routers.
IPv6 Commands 902

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Events Number of times this neighbor relationship has changed state, or an error has occurred.
Retransmission An integer representing the current length of the retransmission queue of the specified neighbor
Queue Length router Id of the specified interface.
show ipv6 ospf range
This command displays the set of OSPFv3 area ranges configured for a given area.
Format show ipv6 ospf range area-id
Modes Privileged EXEC
Term Definition
Area ID The area whose prefixes are summarized.
IPv6 Prefix/Prefix The summary prefix and prefix length.
Length
Type S (Summary Link) or E (External Link)
Action Enabled or Disabled
Cost Metric to be advertised when the range is active.
show ipv6 ospf statistics
This command displays information about the 15 most recent Shortest Path First (SPF)
calculations. SPF is the OSPF routing table calculation.
Format show ipv6 ospf statistics
Modes Privileged EXEC
User EXEC
The command displays the following information with the most recent statistics displayed at
the end of the table.
Term Definition
Delta T The time since the routing table was computed. The time is in the format hours, minutes, and
seconds (hh:mm:ss).
Intra The time taken to compute intra-area routes, in milliseconds.
Summ The time taken to compute inter-area routes, in milliseconds.
Ext The time taken to compute external routes, in milliseconds.
SPF Total The total time taken to compute routes, in milliseconds. The total may exceed the sum of Intra,
Summ, and Ext times.
IPv6 Commands 903
