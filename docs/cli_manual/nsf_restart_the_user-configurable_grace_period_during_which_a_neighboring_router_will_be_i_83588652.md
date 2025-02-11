# nsf_restart_the_user-configurable_grace_period_during_which_a_neighboring_router_will_be_i_83588652

Pages: 891-892

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Maximum Number The maximum number of LSAs that OSPF can store.
of LSAs
LSA High Water The maximum size of the link state database since the system started.
Mark
Retransmit List The total number of LSAs waiting to be acknowledged by all neighbors. An LSA may be pending
Entries acknowledgment from more than one neighbor.
Maximum Number The maximum number of LSAs that can be waiting for acknowledgment at any given time.
of Retransmit
Entries
Retransmit Entries The highest number of LSAs that have been waiting for acknowledgment.
High Water Mark
Redistributing This field is a heading and appears only if you configure the system to take routes learned from a
non-OSPF source and advertise them to its peers.
Source Shows source protocol/routes that are being redistributed. Possible values are static, connected, or
RIP.
Metric The metric of the routes being redistributed.
Metric Type Shows whether the routes are External Type 1 or External Type 2.
Tag The decimal value attached to each external route.
Subnets For redistributing routes into OSPF, the scope of redistribution for the specified protocol.
Distribute-List The access list used to filter redistributed routes.
Prefix-suppression Displays whether prefix-suppression is enabled or disabled on the given interface.
NSF Support Indicates whether nonstop forwarding (NSF) is enabled for the OSPF protocol for planned restarts,
unplanned restarts or both (Always).
NSF Restart The user-configurable grace period during which a neighboring router will be in the helper state after
Interval receiving notice that the management unit is performing a graceful restart.
NSF Restart Status The current graceful restart status of the router.
NSF Restart Age Number of seconds until the graceful restart grace period expires.
NSF Restart Exit Indicates why the router last exited the last restart:
Reason • None . Graceful restart has not been attempted.
• In Progress . Restart is in progress.
• Completed . The previous graceful restart completed successfully.
• Timed Out . The previous graceful restart timed out.
• Topology Changed. The previous graceful restart terminated prematurely because of a
topology change.
IPv6 Commands 891

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
NSF Help Support Indicates whether helpful neighbor functionality has been enabled for OSPF for planned restarts,
unplanned restarts, or both (Always).
NSF help Strict Indicates whether strict LSA checking has been enabled. If enabled, then an OSPF helpful neighbor
LSA checking will exit helper mode whenever a topology change occurs. If disabled, an OSPF neighbor will
continue as a helpful neighbor in spite of topology changes.
show ipv6 ospf abr
This command displays the internal OSPFv3 routes to reach Area Border Routers (ABR).
This command takes no options.
Format show ipv6 ospf abr
Modes Privileged EXEC
User EXEC
Term Definition
Type The type of the route to the destination. It can be either:
• intra — Intra-area route
• inter — Inter-area route
Router ID Router ID of the destination.
Cost Cost of using this route.
Area ID The area ID of the area from which this route is learned.
Next Hop Next hop toward the destination.
Next Hop Intf The outgoing router interface to use when forwarding traffic to the next hop.
show ipv6 ospf area
This command displays information about the area. The area-id identifies the OSPF area
that is displayed.
Format show ipv6 ospf area area-id
Modes Privileged EXEC
User EXEC
Term Definition
AreaID The area id of the requested OSPF area.
External Routing A number representing the external routing capabilities for this area.
Spf Runs The number of times that the intra-area route table has been calculated using this area's link-state
database.
IPv6 Commands 892
