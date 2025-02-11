# ospf_show_commands_show_ip_ospf

Pages: 758-759

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
summary-lsa (Optional) Set the metric in type 3 and type 4 summary LSAs to LsInfinity (0xFFFFFF).
metric (Optional) Metric to send in summary LSAs when in stub router mode. The range is 1 to 16,777,215.
The default is 16,711,680 (0xFF0000).
no max-metric router-lsa
Use this command in OSPFv2 Router Configuration mode to disable stub router mode. The
command clears either type of stub router mode (always or on-startup) and resets the
summary-lsa option. If OSPF is configured to enter global configuration mode on startup,
and during normal operation you want to immediately place OSPF in stub router mode, issue
the no max-metric router-lsa on-startup command. The no max-metric
router-lsa summary-lsa command causes OSPF to send summary LSAs with metrics
computed using normal procedures defined in RFC 2328.
Format no max-metric router-lsa [on-startup] [summary-lsa]
Mode OSPFv2 Router Configuration
clear ip ospf stub-router
Use the clear ip ospf stub-router command in Privileged EXEC mode to force OSPF to exit
stub router mode when it has automatically entered stub router mode because of a resource
limitation. OSPF only exits stub router mode if it entered stub router mode because of a
resource limitation or it if is in stub router mode at startup. If OSPF is configured to function
permanently in stub router mode, the command does not take effect.
Format clear ip ospf stub-router
Mode Privileged EXEC
OSPF Show Commands
show ip ospf
This command displays information relevant to the OSPF router.
Format show ip ospf
Mode Privileged EXEC
Note: Some of the information below displays only if you enable OSPF and
configure certain features.
Routing Commands 758

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Router ID A 32-bit integer in dotted decimal format identifying the router, about which information is displayed.
This is a configured value.
OSPF Admin Mode Shows whether the administrative mode of OSPF in the router is enabled or disabled. This is a
configured value.
RFC 1583 Indicates whether 1583 compatibility is enabled or disabled. This is a configured value.
Compatibility
External LSDB The maximum number of nondefault AS-external-LSA (link state advertisement) entries that can be
Limit stored in the link-state database.
Exit Overflow The number of seconds that, after entering overflow state, a router will attempt to leave overflow
Interval state.
Spf Delay Time The number of seconds between two subsequent changes of LSAs, during which time the routing
table calculation is delayed.
Spf Hold Time The number of seconds between two consecutive spf calculations.
Flood Pacing The average time, in milliseconds, between LS Update packet transmissions on an interface. This is
Interval the value configured with the command timers pacing flood on page742.
LSA Refresh Group The size in seconds of the LSA refresh group window. This is the value configured with the
Pacing Time command timers pacing lsa-group (OSPF) on page743.
Opaque Capability Shows whether the router is capable of sending Opaque LSAs. This is a configured value.
Autocost Ref BW Shows the value of auto-cost reference bandwidth configured on the router.
Default Passive Shows whether the interfaces are passive by default.
Setting
Maximum Paths The maximum number of paths that OSPF can report for a given destination.
Default Metric Default value for redistributed routes.
Stub Router When OSPF runs out of resources to store the entire link state database, or any other state
Configuration information, OSPF goes into stub router mode. As a stub router, OSPF reoriginates its own router
LSAs, setting the cost of all nonstub interfaces to infinity. Use this field to set stub router
configuration to one of Always, Startup, None.
Stub Router Configured value in seconds. This row is only listed if OSPF is configured to be a stub router at
Startup Time startup.
Summary LSA One of Enabled (met), Disabled, in which met is the metric to be sent in summary LSAs when in stub
Metric Override router mode.
Default Route Indicates whether the default routes received from other source protocols are advertised or not.
Advertise
Always Shows whether default routes are always advertised.
Metric The metric of the routes being redistributed. If the metric is not configured, this field is blank.
Metric Type Shows whether the routes are External Type 1 or External Type 2.
Routing Commands 759
