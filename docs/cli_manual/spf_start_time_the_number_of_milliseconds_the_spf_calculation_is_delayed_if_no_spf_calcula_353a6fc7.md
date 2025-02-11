# spf_start_time_the_number_of_milliseconds_the_spf_calculation_is_delayed_if_no_spf_calcula_353a6fc7

Pages: 889-890

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
startup. This command does not take effect if OSPF is configured to be in stub router mode
permanently.
Format clear ipv6 ospf stub-router
Mode Privileged EXEC
OSPFv3 Show Commands
show ipv6 ospf
This command displays information relevant to the OSPF router.
Format show ipv6 ospf
Mode Privileged EXEC
User EXEC
Note: Some of the information below displays only if you enable OSPF and
configure certain features.
Term Definition
Router ID A 32-bit integer in dotted decimal format identifying the router, about which information is displayed.
This is a configured value.
OSPF Admin Mode Shows whether the administrative mode of OSPF in the router is enabled or disabled. This is a
configured value.
External LSDB The maximum number of non-default AS-external-LSAs entries that can be stored in the link-state
Limit database.
Exit Overflow The number of seconds that, after entering overflow state, a router will attempt to leave overflow
Interval state.
SPF Start Time The number of milliseconds the SPF calculation is delayed if no SPF calculation has been
scheduled during the current “wait interval”.
SPF Hold Time The number of milliseconds of the initial wait interval.
SPF Maximum The maximum number of milliseconds of the “wait interval”.
Hold Time
LSA Refresh Group The size of the LSA refresh group window, in seconds.
Pacing Time
AutoCost Ref BW Shows the value of the auto-cost reference bandwidth configured on the router.
Default Passive Shows whether the interfaces are passive by default.
Setting
IPv6 Commands 889

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Maximum Paths The maximum number of paths that OSPF can report for a given destination.
Default Metric Default value for redistributed routes.
Default Route Indicates whether the default routes received from other source protocols are advertised or not.
Advertise
Always Shows whether default routes are always advertised.
Metric The metric for the advertised default routes. If the metric is not configured, this field is blank.
Metric Type Shows whether the routes are External Type 1 or External Type 2.
Number of Active The number of active OSPF areas. An active OSPF area is an area with at least one interface up.
Areas
ABR Status Shows whether the router is an OSPF Area Border Router.
ASBR Status Shows if the ASBR mode is enabled or disabled. Enable implies that the router is an autonomous
system border router. Router automatically becomes an ASBR when it is configured to redistribute
routes learnt from other protocol. The possible values for the ASBR status is enabled (if the router is
configured to re-distribute routes learned by other protocols) or disabled (if the router is not
configured for the same).
Stub Router Status The status of the stub router: Active or Inactive.
Stub Router This is displayed only if the stub router is active.
Reason Shows the reason for the stub router: Configured, S tartup, or ResourceLimitation
Stub Router This is displayed only if the stub router is in startup stub router mode.
Startup Time The remaining time (in seconds) until OSPF exits stub router mode.
Remaining
Stub Router This row is only listed if the stub router is active and the router entered stub mode because of a
Duration resource limitation.
The time elapsed since the router last entered the stub router mode. The duration is displayed in
DD:HH:MM:SS format.
External LSDB When the number of non-default external LSAs exceeds the configured limit, External LSDB Limit,
Overflow OSPF goes into LSDB overflow state. In this state, OSPF withdraws all of its self-originated
non-default external LSAs. After the Exit Overflow Interval, OSPF leaves the overflow state, if the
number of external LSAs has been reduced.
External LSA The number of external (LS type 5) link-state advertisements in the link-state database.
Count
External LSA The sum of the LS checksums of external link-state advertisements contained in the link-state
Checksum database.
New LSAs The number of new link-state advertisements that have been originated.
Originated
LSAs Received The number of link-state advertisements received determined to be new instantiations.
LSA Count The total number of link state advertisements currently in the link state database.
IPv6 Commands 890
