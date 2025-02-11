# ospf_graceful_restart_commands

Pages: 754-757

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
OSPF Graceful Restart Commands
The OSPF protocol can be configured to participate in the checkpointing service, so that
these protocols can execute a graceful restart” when the management unit fails. In a graceful
restart, the hardware to continues forwarding IPv4 packets using OSPF routes while a
backup switch takes over management unit responsibility
Graceful restart uses the concept of helpful neighbors. A fully adjacent router enters helper
mode when it receives a link state announcement (LSA) from the restarting management unit
indicating its intention of performing a graceful restart. In helper mode, a switch continues to
advertise to the rest of the network that they have full adjacencies with the restarting router,
thereby avoiding announcement of a topology change and the potential for flooding of LSAs
and shortest-path-first (SPF) runs (which determine OSPF routes). Helpful neighbors
continue to forward packets through the restarting router. The restarting router relearns the
network topology from its helpful neighbors.
Graceful restart can be enabled for either planned or unplanned restarts, or both. A planned
restart is initiated by the operator through the initiate failover command. The
operator may initiate a failover in order to take the management unit out of service (for
example, to address a partial hardware failure), to correct faulty system behavior which
cannot be corrected through less severe management actions, or other reasons. An
unplanned restart is an unexpected failover caused by a fatal hardware failure of the
management unit or a software hang or crash on the management unit.
nsf (OSPF)
Use this command to enable the OSPF graceful restart functionality on an interface. To
disable graceful restart, use the no form of the command.
Default Disabled
Format nsf [ietf] [planned-only]
Modes OSPF Router Configuration
Parameter Description
ietf This keyword is accepted but not required.
planned-only This optional keyword indicates that OSPF should only perform a graceful restart when the restart is
planned (that is, when the restart is a result of the initiate failover command).
no nsf
Use this command to disable graceful restart for all restarts.
Routing Commands 754

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
nsf restart-interval (OSPF)
Use this command to configure the number of seconds that the restarting router asks its
neighbors to wait before exiting helper mode. This is referred to as the grace period. The
restarting router includes the grace period in its grace LSAs. For planned restarts (using the
initiate failover command), the grace LSAs are sent prior to restarting the
management unit, whereas for unplanned restarts, they are sent after reboot begins.
The grace period must be set long enough to allow the restarting router to reestablish all of its
adjacencies and complete a full database exchange with each of those neighbors. The value
for the seconds argument can be from 1–1800 seconds.
Default 120 seconds
Format nsf [ietf] restart-interval seconds
Modes OSPF Router Configuration
Parameter Description
ietf This keyword is accepted but not required.
seconds The number of seconds that the restarting router asks its neighbors to wait before exiting helper
mode. The range is from 1 to 1800 seconds.
no nsfrestart-interval
Use this command to revert the grace period to its default value.
Format no [ietf] nsf restart-interval
Modes OSPF Router Configuration
nsf helper
Use this command to enable helpful neighbor functionality for the OSPF protocol. You can
enable this functionality for planned or unplanned restarts, or both.
Default OSPF may act as a helpful neighbor for both planned and unplanned restarts
Format nsf helper [planned-only]
Modes OSPF Router Configuration
Parameter Description
planned-only This optional keyword indicates that OSPF should only help a restarting router performing a planned
restart.
Routing Commands 755

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no nsf helper
Use this command to disable helpful neighbor functionality for OSPF.
Format no nsf helper
Modes OSPF Router Configuration
nsf ietf helper disable (OSPF)
Use this command to disable helpful neighbor functionality for OSPF.
Note: The commands no nsf helper and nsf ietf helper disable
are functionally equivalent. The command nsf ietf helper
disable is supported solely for compatibility with other network
software CLI.
Format nsf ietf helper disable
Modes OSPF Router Configuration
nsf helper strict-lsa-checking (OSPF)
The restarting router is unable to react to topology changes. In particular, the restarting router
will not immediately update its forwarding table; therefore, a topology change may introduce
forwarding loops or black holes that persist until the graceful restart completes. By exiting the
graceful restart on a topology change, a router tries to eliminate the loops or black holes as
quickly as possible by routing around the restarting router. A helpful neighbor considers a link
down with the restarting router to be a topology change, regardless of the strict LSA checking
configuration.
Use this command to require that an OSPF helpful neighbor exit helper mode whenever a
topology change occurs.
Default Enabled.
Format nsf [ietf] helper strict-lsa-checking
Modes OSPF Router Configuration
Parameter Description
ietf This keyword is accepted but not required.
Routing Commands 756

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no nsf [ietf] helper strict-lsa-checking
Use this command to allow OSPF to continue as a helpful neighbor in spite of topology
changes.
Default Enabled.
Format nsf [ietf] helper strict-lsa-checking
Modes OSPF Router Configuration
OSPFv2 Stub Router Commands
max-metric router-lsa (OSPFv2 Router Configuration)
To configure OSPF to enter stub router mode, use this command in Router OSPF Global
Configuration mode. When OSPF is in stub router mode, as defined by RFC 3137, OSPF
sets the metric in the nonstub links in its router LSA to LsInfinity. Other routers therefore
compute very long paths through the stub router, and prefer any alternate path. Doing so
eliminates all transit traffic through the stub router, when alternate routes are available. Stub
router mode is useful when adding or removing a router from a network or to avoid transient
routes when a router reloads.
You can administratively force OSPF into stub router mode. OSPF remains in stub router
mode until you take OSPF out of stub router mode. Alternatively, you can configure OSPF to
start in stub router mode for a configurable period of time after the router boots up.
If you set the summary LSA metric to 16,777,215, other routers will skip the summary LSA
when they compute routes.
If you have configured the router to enter stub router mode on startup (max-metric router-lsa
on-startup), and then enter max-metric router lsa, there is no change. If OSPF is
administratively in stub router mode (the max-metric router-lsa command has been given),
and you configure OSPF to enter stub router mode on startup (max-metric router-lsa
on-startup), OSPF exits stub router mode (assuming the startup period has expired) and the
configuration is updated.
Default OSPF is not in stub router mode by default
Format max-metric router-lsa [on-startup seconds] [summary-lsa {metric}]
Mode OSPFv2 Router Configuration
Parameter Description
on-startup (Optional) OSPF starts in stub router mode after a reboot.
seconds (Required if on-startup) The number of seconds that OSPF remains in stub router mode after a
reboot. The range is 5 to 86,400 seconds. There is no default value.
Routing Commands 757
