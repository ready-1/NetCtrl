# as_scope_lsa_the_number_of_lsas_currently_in_the_global_flood_queue_waiting_to_be_flooded__7ac64fc5

Pages: 760-760

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Number of Active The number of active OSPF areas. An active OSPF area is an area with at least one interface up.
Areas
ABR Status Shows whether the router is an OSPF Area Border Router.
ASBR Status Reflects whether the ASBR mode is enabled or disabled. Enable implies that the router is an
autonomous system border router. The router automatically becomes an ASBR when it is configured
to redistribute routes learnt from other protocols. The possible values for the ASBR status is enabled
(if the router is configured to redistribute routes learned by other protocols) or disabled (if the router
is not configured for the same).
Stub Router Status One of Active, Inactive.
Stub Router One of Configured, Startup, Resource Limitation.
Reason
Note: The row is only listed if stub router is active.
Stub Router The remaining time, in seconds, until OSPF exits stub router mode. This row is only listed if OSPF is
Startup Time in startup stub router mode.
Remaining
Stub Router The time elapsed since the router last entered the stub router mode. The row is only listed if stub
Duration router is active and the router entered stub mode because of a resource limitation. The duration is
displayed in DD:HH:MM:SS format.
External LSDB When the number of nondefault external LSAs exceeds the configured limit, External LSDB Limit,
Overflow OSPF goes into LSDB overflow state. In this state, OSPF withdraws all of its self-originated
nondefault external LSAs. After the Exit Overflow Interval, OSPF leaves the overflow state, if the
number of external LSAs has been reduced.
External LSA The number of external (LS type 5) link-state advertisements in the link-state database.
Count
External LSA The sum of the LS checksums of external link-state advertisements contained in the link-state
Checksum database.
AS_OPAQUE LSA Shows the number of AS Opaque LSAs in the link-state database.
Count
AS_OPAQUE LSA Shows the sum of the LS Checksums of AS Opaque LSAs contained in the link-state database.
Checksum
New LSAs The number of new link-state advertisements that have been originated.
Originated
LSAs Received The number of link-state advertisements received determined to be new instantiations.
LSA Count The total number of link state advertisements currently in the link state database.
Maximum Number The maximum number of LSAs that OSPF can store.
of LSAs
LSA High Water The maximum size of the link state database since the system started.
Mark
AS Scope LSA The number of LSAs currently in the global flood queue waiting to be flooded through the OSPF
Flood List Length domain. LSAs with AS flooding scope, such as type 5 external LSAs and type 11 Opaque LSAs.
Routing Commands 760
