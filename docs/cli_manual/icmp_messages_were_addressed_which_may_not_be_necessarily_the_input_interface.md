# icmp_messages_were_addressed_which_may_not_be_necessarily_the_input_interface

Pages: 859-888

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Received Datagrams Discarded Number of input IPv6 datagrams for which no problems were encountered to
Other prevent their continue processing, but which were discarded (e.g., for lack of buffer
space). Note that this counter does not include datagrams discarded while awaiting
re-assembly.
Received Datagrams Reassembly Number of IPv6 fragments received which needed to be reassembled at this
Required interface. Note that this counter increments at the interface to which these
fragments were addressed, which might not be necessarily the input interface for
some of the fragments.
Datagrams Successfully Number of IPv6 datagrams successfully reassembled. Note that this counter
Reassembled increments at the interface to which these datagrams were addressed, which might
not be necessarily the input interface for some of the fragments.
Datagrams Failed To Reassemble Number of failures detected by the IPv6 reassembly algorithm (for whatever reason:
timed out, errors, etc.). Note that this is not necessarily a count of discarded IPv6
fragments since some algorithms (notably the algorithm in by combining them as
they are received. This counter increments at the interface to which these
fragments were addressed, which might not be necessarily the input interface for
some of the fragments.
Datagrams Forwarded Number of output datagrams which this entity received and forwarded to their final
destinations. In entities which do not act as IPv6 routers, this counter will include
only those packets which were Source-Routed via this entity, and the Source-Route
processing was successful. Note that for a successfully forwarded datagram the
counter of the outgoing interface increments.
Datagrams Locally Transmitted Total number of IPv6 datagrams which local IPv6 user-protocols (including ICMP)
supplied to IPv6 in requests for transmission. Note that this counter does not
include any datagrams counted in ipv6IfStatsOutForwDatagrams.
Datagrams Transmit Failed Number of output IPv6 datagrams for which no problem was encountered to
prevent their transmission to their destination, but which were discarded (e.g., for
lack of buffer space). Note that this counter would include datagrams counted in
ipv6IfStatsOutForwDatagrams if any such packets met this (discretionary) discard
criterion.
Fragments Created Number of output datagram fragments that have been generated as a result of
fragmentation at this output interface.
Datagrams Successfully Number of IPv6 datagrams that have been successfully fragmented at this output
Fragmented interface.
Datagrams Failed To Fragment Number of IPv6 datagrams that have been discarded because they needed to be
fragmented at this output interface but could not be.
Fragments Created The number of fragments that were created.
Multicast Datagrams Received Number of multicast packets received by the interface.
Multicast Datagrams Transmitted Number of multicast packets transmitted by the interface.
Total ICMPv6 messages received Total number of ICMP messages received by the interface which includes all those
counted by ipv6IfIcmpInErrors. Note that this interface is the interface to which the
ICMP messages were addressed which may not be necessarily the input interface
for the messages.
IPv6 Commands 859

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
ICMPv6 Messages with errors Number of ICMP messages which the interface received but determined as having
ICMP-specific errors (bad ICMP checksums, bad length, etc.).
ICMPv6 Destination Unreachable Number of ICMP Destination Unreachable messages received by the interface.
Messages Received
ICMPv6 Messages Prohibited Number of ICMP destination unreachable/communication administratively
Administratively Received prohibited messages received by the interface.
ICMPv6 Time Exceeded Messages Number of ICMP Time Exceeded messages received by the interface.
Received
ICMPv6 Parameter Problem Number of ICMP Parameter Problem messages received by the interface.
Messages Received
ICMPv6 Packet Too Big Messages Number of ICMP Packet Too Big messages received by the interface.
Received
ICMPv6 Echo Request Messages Number of ICMP Echo (request) messages received by the interface.
Received
ICMPv6 Echo Reply Messages Number of ICMP Echo Reply messages received by the interface.
Received
ICMPv6 Router Solicit Messages Number of ICMP Router Solicit messages received by the interface.
Received
ICMPv6 Router Advertisement Number of ICMP Router Advertisement messages received by the interface.
Messages Received
ICMPv6 Neighbor Solicit Messages Number of ICMP Neighbor Solicit messages received by the interface.
Received
ICMPv6 Neighbor Advertisement Number of ICMP Neighbor Advertisement messages received by the interface.
Messages Received
ICMPv6 Redirect Messages Number of Redirect messages received by the interface.
Received
ICMPv6 Group Membership Query Number of ICMPv6 Group Membership Query messages received by the interface.
Messages Received
ICMPv6 Group Membership Number of ICMPv6 Group Membership response messages received by the
Response Messages Received interface.
ICMPv6 Group Membership Number of ICMPv6 Group Membership reduction messages received by the
Reduction Messages Received interface.
Total ICMPv6 Messages Total number of ICMP messages which this interface attempted to send. Note that
Transmitted this counter includes all those counted by icmpOutErrors.
ICMPv6 Messages Not Transmitted Number of ICMP messages which this interface did not send due to problems
Due To Error discovered within ICMP such as a lack of buffers. This value should not include
errors discovered outside the ICMP layer such as the inability of IPv6 to route the
resultant datagram. In some implementations there may be no types of error which
contribute to this counter's value.
IPv6 Commands 860

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
ICMPv6 Destination Unreachable Number of ICMP Destination Unreachable messages sent by the interface.
Messages Transmitted
ICMPv6 Messages Prohibited Number of ICMP destination unreachable/communication administratively
Administratively Transmitted prohibited messages sent.
ICMPv6 Time Exceeded Messages Number of ICMP Time Exceeded messages sent by the interface.
Transmitted
ICMPv6 Parameter Problem Number of ICMP Parameter Problem messages sent by the interface.
Messages Transmitted
ICMPv6 Packet Too Big Messages Number of ICMP Packet Too Big messages sent by the interface.
Transmitted
ICMPv6 Echo Request Messages Number of ICMP Echo (request) messages sent by the interface.ICMP echo
Transmitted messages sent.
ICMPv6 Echo Reply Messages Number of ICMP Echo Reply messages sent by the interface.
Transmitted
ICMPv6 Router Solicit Messages Number of ICMP Router Solicitation messages sent by the interface.
Transmitted
ICMPv6 Router Advertisement Number of ICMP Router Advertisement messages sent by the interface.
Messages Transmitted
ICMPv6 Neighbor Solicit Messages Number of ICMP Neighbor Solicitation messages sent by the interface.
Transmitted
ICMPv6 Neighbor Advertisement Number of ICMP Neighbor Advertisement messages sent by the interface.
Messages Transmitted
ICMPv6 Redirect Messages Number of Redirect messages sent. For a host, this object will always be zero,
Received since hosts do not send redirects.
ICMPv6 Group Membership Query Number of ICMPv6 Group Membership Query messages sent.
Messages Transmitted
ICMPv6 Group Membership Number of ICMPv6 Group Membership Response messages sent.
Response Messages Transmitted
ICMPv6 Group Membership Number of ICMPv6 Group Membership Reduction messages sent.
Reduction Messages Transmitted
ICMPv6 Duplicate Address Detects Number of duplicate addresses detected by the interface.
clear ipv6 statistics
Use this command to clear IPv6 statistics for all interfaces or for a specific interface, including
loopback and tunnel interfaces. IPv6 statistics display in the output of the show ipv6
IPv6 Commands 861

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
traffic command. If you do not specify an interface, the counters for all IPv6 traffic
statistics reset to zero.
Format clear ipv6 statistics [{unit/slot/port | loopback loopback-id | tunnel
tunnel-id}]
Mode Privileged EXEC
OSPFv3 Commands
This section describes the commands you use to configure OSPFv3, which is a link-state
routing protocol that you use to route traffic within a network. This section includes the
following subsections:
• Global OSPFv3 Commands on page862
• OSPFv3 Interface Commands on page879
• OSPFv3 Graceful Restart Commands on page884
• OSPFv3 Stub Router Commands on page887
• OSPFv3 Show Commands on page889
Global OSPFv3 Commands
ipv6 router ospf
Use this command to enter Router OSPFv3 Config mode.
Format ipv6 router ospf
Mode Global Config
area default-cost (OSPFv3)
This command configures the monetary default cost for the stub area. For the value
argument, you must specify an integer value between 1–16777215.
Format area area-id default-cost value
Mode Router OSPFv3 Config
IPv6 Commands 862

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
area nssa (OSPFv3)
This command configures the specified area-id to function as an NSSA.
Format area area-id nssa
Mode Router OSPFv3 Config
no area nssa
This command disables nssa from the specified area id.
Format no area area-id nssa
Mode Router OSPFv3 Config
area nssa default-info-originate (OSPFv3)
This command configures the metric value and type for the default route advertised into the
NSSA. The optional metric parameter specifies the metric of the default route and must be
in the range of 1–16777214. If no metric is specified, the default value is 10. The metric type
can be comparable (nssa-external 1) or noncomparable (nssa-external 2).
Format area area-id nssa default-info-originate [metric] [comparable |
non-comparable]
Mode Router OSPFv3 Config
no area nssa default-info-originate (OSPFv3)
This command disables the default route advertised into the NSSA.
Format no area area-id nssa default-info-originate [metric] [comparable |
non-comparable]
Mode Router OSPFv3 Config
area nssa no-redistribute (OSPFv3)
This command configures the NSSA ABR so that learned external routes will not be
redistributed to the NSSA.
Format area area-id nssa no-redistribute
Mode Router OSPFv3 Config
IPv6 Commands 863

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no area nssa no-redistribute (OSPFv3)
This command disables the NSSA ABR so that learned external routes are redistributed to
the NSSA.
Format no area area-id nssa no-redistribute
Mode Router OSPFv3 Config
area nssa no-summary (OSPFv3)
This command configures the NSSA so that summary LSAs are not advertised into the
NSSA.
Format area area-id nssa no-summary
Mode Router OSPFv3 Config
no area nssa no-summary (OSPFv3)
This command disables nssa from the summary LSAs.
Format no area area-id nssa no-summary
Mode Router OSPFv3 Config
area nssa translator-role (OSPFv3)
This command configures the translator role of the NSSA. Selecting always causes the
router to assume the role of the translator the instant it becomes a border router and
selecting candidate causes the router to participate in the translator election process when
it attains border router status.
Format area area-id nssa translator-role {always | candidate}
Mode Router OSPFv3 Config
no area nssa translator-role (OSPFv3)
This command disables the nssa translator role from the specified area id.
Format no area area-id nssa translator-role {always | candidate}
Mode Router OSPFv3 Config
IPv6 Commands 864

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
area nssa translator-stab-intv (OSPFv3)
This command configures the translator stabilityinterval of the NSSA. The
stabilityinterval is the period of time that an elected translator continues to perform its
duties after it determines that its translator status has been deposed by another router.
Format area area-id nssa translator-stab-intv stabilityinterval
Mode Router OSPFv3 Config
no area nssa translator-stab-intv (OSPFv3)
This command disables the nssa translator’s stabilityinterval from the specified area
id.
Format no area area-id nssa translator-stab-intv stabilityinterval
Mode Router OSPFv3 Config
area range (OSPFv3)
Use this command to configure a summary prefix that an area border router advertises for a
specific area.
Default No area ranges are configured by default. No cost is configured by default.
Format area area-id range prefix netmask {summarylink | nssaexternallink} [advertise
| not-advertise] [cost cost]
Mode Router OSPFv3 Config
Parameter Description
area-id The area identifier for the area whose networks are to be summarized.
prefix netmask The summary prefix to be advertised when the ABR computes a route to one or more networks
within this prefix in this area.
summarylink When this keyword is given, the area range is used when summarizing prefixes advertised in type 3
summary LSAs.
nssaexternallink When this keyword is given, the area range is used when translating type 7 LSAs to type 5 LSAs.
advertise [Optional] When this keyword is given, the summary prefix is advertised when the area range is
active. This is the default.
not-advertise [Optional] When this keyword is given, neither the summary prefix nor the contained prefixes are
advertised when the area range is active. When the not-advertise option is given, any static cost
previously configured is removed from the system configuration.
cost [Optional] If an optional cost is given, OSPF sets the metric field in the inter-area -prefix LSA to the
configured value rather than setting the metric to the largest cost among the networks covered by
the area range.
IPv6 Commands 865

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no area range
The no area range command deletes a summary prefix or removes a static cost.
Format no area area-id range prefix netmask {summarylink | nssaexternallink} cost
Mode Router OSPFv3 Config
area stub (OSPFv3)
This command creates a stub area for the specified area ID. A stub area is characterized by
the fact that AS External LSAs are not propagated into the area. Removing AS External LSAs
and Summary LSAs can significantly reduce the link state database of routers within the stub
area.
Format area area-id stub
Mode Router OSPFv3 Config
no area stub
This command deletes a stub area for the specified area ID.
Format no area area-id stub
Mode Router OSPFv3 Config
area stub no-summary (OSPFv3)
This command disables the import of Summary LSAs for the stub area identified by
area-id.
Default enabled
Format area area-id stub no-summary
Mode Router OSPFv3 Config
no area stub no-summary
This command sets the Summary LSA import mode to the default for the stub area identified
by area-id.
Format no area area-id stub summarylsa
Mode Router OSPFv3 Config
IPv6 Commands 866

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
area virtual-link (OSPFv3)
This command creates the OSPF virtual interface for the specified area-id and neighbor.
The neighbor parameter is the Router ID of the neighbor.
Format area area-id virtual-link neighbor
Mode Router OSPFv3 Config
no area virtual-link
This command deletes the OSPF virtual interface for the specified area-id and neighbor.
The neighbor parameter is the Router ID of the neighbor.
Format no area area-id virtual-link neighbor
Mode Router OSPFv3 Config
area virtual-link dead-interval (OSPFv3)
This command configures the dead interval for the OSPF virtual interface on the virtual
interface identified by area-id and neighbor. The neighbor parameter is the Router ID
of the neighbor. The range for seconds is 1 to 65535.
Default 40
Format area area-id virtual-link neighbor dead-interval seconds
Mode Router OSPFv3 Config
no area virtual-link dead-interval
This command configures the default dead interval for the OSPF virtual interface on the
virtual interface identified by area-id and neighbor. The neighbor parameter is the
Router ID of the neighbor.
Format no area area-id virtual-link neighbor dead-interval
Mode Router OSPFv3 Config
area virtual-link hello-interval (OSPFv3)
This command configures the hello interval for the OSPF virtual interface on the virtual
interface identified by area-id and neighbor. The neighbor parameter is the Router ID
of the neighbor. The range for seconds is from 1 to 65535.
Default 10
Format area area-id virtual-link neighbor hello-interval seconds
Mode Router OSPFv3 Config
IPv6 Commands 867

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no area virtual-link hello-interval
This command configures the default hello interval for the OSPF virtual interface on the
virtual interface identified by area-id and neighbor. The neighbor parameter is the
Router ID of the neighbor.
Format no area area-id virtual-link neighbor hello-interval
Mode Router OSPFv3 Config
area virtual-link retransmit-interval (OSPFv3)
This command configures the retransmit interval for the OSPF virtual interface on the virtual
interface identified by area-id and neighbor. The neighbor parameter is the Router ID
of the neighbor. The range for seconds is 0 to 3600.
Default 5
Format area area-id virtual-link neighbor retransmit-interval seconds
Mode Router OSPFv3 Config
no area virtual-link retransmit-interval
This command configures the default retransmit interval for the OSPF virtual interface on the
virtual interface identified by area-id and neighbor. The neighbor parameter is the
Router ID of the neighbor.
Format no area area-id virtual-link neighbor retransmit-interval
Mode Router OSPFv3 Config
area virtual-link transmit-delay (OSPFv3)
This command configures the transmit delay for the OSPF virtual interface on the virtual
interface identified by area-id and neighbor. The neighbor parameter is the Router ID
of the neighbor. The range for seconds is 0 to 3600 (1 hour).
Default 1
Format area area-id virtual-link neighbor transmit-delay seconds
Mode Router OSPFv3 Config
IPv6 Commands 868

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no area virtual-link transmit-delay
This command configures the default transmit delay for the OSPF virtual interface on the
virtual interface identified by area-id and neighbor. The neighbor parameter is the
Router ID of the neighbor.
Format no area area-id virtual-link neighbor transmit-delay
Mode Router OSPFv3 Config
auto-cost (OSPFv3)
By default, OSPF computes the link cost of each interface from the interface bandwidth.
Faster links have lower metrics, making them more attractive in route selection. The
configuration parameters in the auto-cost reference bandwidth and bandwidth
commands give you control over the default link cost. You can configure for OSPF an
interface bandwidth that is independent of the actual link speed. A second configuration
parameter allows you to control the ratio of interface bandwidth to link cost. The link cost is
computed as the ratio of a reference bandwidth to the interface bandwidth (ref_bw / interface
bandwidth), where interface bandwidth is defined by the bandwidth command. Because the
default reference bandwidth is 100 Mbps, OSPF uses the same default link cost for all
interfaces whose bandwidth is 100 Mbps or greater. Use the auto-cost
reference-bandwidth command to change the reference bandwidth, specifying the
reference bandwidth in megabits per second (Mbps). For the mbps variable, the reference
bandwidth range is 1–4294967 Mbps.
Default 100 Mbps
Format auto-cost reference-bandwidth mbps
Mode Router OSPFv3 Config
no auto-cost reference-bandwidth (OSPFv3)
Use this command to set the reference bandwidth to the default value.
Format no auto-cost reference-bandwidth
Mode Router OSPFv3 Config
clear ipv6 ospf
Use this command to disable and re-enable OSPF.
Format clear ipv6 ospf
Mode Privileged EXEC
IPv6 Commands 869

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
clear ipv6 ospf configuration
Use this command to reset the OSPF configuration to factory defaults.
Format clear ipv6 ospf configuration
Mode Privileged EXEC
clear ipv6 ospf counters
Use this command to reset global and interface statistics.
Format clear ipv6 ospf counters
Mode Privileged EXEC
clear ipv6 ospf neighbor
Use this command to drop the adjacency with all OSPF neighbors. On each neighbor’s
interface, send a one-way hello. Adjacencies may then be re-established. To drop all
adjacencies with a specific router ID, specify the neighbor’s Router ID using the optional
parameter neighbor-id.
Format clear ipv6 ospf neighbor [neighbor-id]
Mode Privileged EXEC
clear ipv6 ospf neighbor interface
To drop adjacency with all neighbors on a specific interface, use the optional parameter
unit/slot/port.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id
parameter is a number in the range of 1–4093.
To drop adjacency with a specific router ID on a specific interface, use the optional parameter
neighbor-id.
Format clear ipv6 ospf neighbor interface [unit/slot/port | vlan vland-id]
[neighbor-id]
Mode Privileged EXEC
IPv6 Commands 870

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
clear ipv6 ospf redistribution
Use this command to flush all self-originated external LSAs. Reapply the redistribution
configuration and re-originate prefixes as necessary.
Format clear ipv6 ospf redistribution
Mode Privileged EXEC
default-information originate (OSPFv3)
This command is used to control the advertisement of default routes. The metric argument
can be a number in the range 0–16777214. The metric type can be 1 or 2.
Default metric—unspecified
type—2
Format default-information originate [always] [metric metric] [metric-type {1 | 2}]
Mode Router OSPFv3 Config
no default-information originate (OSPFv3)
This command is used to control the advertisement of default routes.
Format no default-information originate [metric] [metric-type]
Mode Router OSPFv3 Config
default-metric (OSPFv3)
This command is used to set a default for the metric of distributed routes. The metric
argument can be a number in the range 0–16777214.
Format default-metric metric
Mode Router OSPFv3 Config
no default-metric (OSPFv3)
This command is used to set a default for the metric of distributed routes.
Format no default-metric
Mode Router OSPFv3 Config
distance ospf (OSPFv3)
This command sets the route preference value of OSPF route types in the router. Lower
route preference values are preferred when determining the best route. The type of OSPF
IPv6 Commands 871

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
route can be intra, inter, or external. All the external type routes are given the same
preference value. The range for the preference value is from 1 to 255.
Default 110
Format distance ospf {intra-area preference | inter-area preference | external
preference}
Mode Router OSPFv3 Config
no distance ospf
This command sets the default route preference value of OSPF routes in the router. The type
of OSPF route can be intra, inter, or external. All the external type routes are given the same
preference value.
Format no distance ospf {intra-area | inter-area | external}
Mode Router OSPFv3 Config
enable (OSPFv3)
This command resets the default administrative mode of OSPF in the router (active).
Default enabled
Format enable
Mode Router OSPFv3 Config
no enable (OSPFv3)
This command sets the administrative mode of OSPF in the router to inactive.
Format no enable
Mode Router OSPFv3 Config
exit-overflow-interval (OSPFv3)
This command configures the exit overflow interval for OSPF. It describes the number of
seconds after entering Overflow state that a router will wait before attempting to leave the
overflow state. This allows the router to again originate nondefault AS-external-LSAs. When
set to 0, the router does not leave overflow state until restarted. The range for seconds is
from 0 to 2147483647 seconds.
Default 0
Format exit-overflow-interval seconds
Mode Router OSPFv3 Config
IPv6 Commands 872

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no exit-overflow-interval
This command configures the default exit overflow interval for OSPF.
Format no exit-overflow-interval
Mode Router OSPFv3 Config
external-lsdb-limit (OSPFv3)
This command configures the external LSDB limit for OSPF. If the value is –1, then there is
no limit. When the number of nondefault AS-external-LSAs in a router’s link-state database
reaches the external LSDB limit, the router enters overflow state. The router never holds
more than the external LSDB limit nondefault AS-external-LSAs in it database. The external
LSDB limit MUST be set identically in all routers attached to the OSPF backbone and/or any
regular OSPF area. The range for limit is from –1 to 2147483647.
Default -1
Format external-lsdb-limit limit
Mode Router OSPFv3 Config
no external-lsdb-limit
This command configures the default external LSDB limit for OSPF.
Format no external-lsdb-limit
Mode Router OSPFv3 Config
maximum-paths (OSPFv3)
This command sets the number of paths that OSPF can report for a given destination where
maxpaths is platform dependent.
Default 4
Format maximum-paths maxpaths
Mode Router OSPFv3 Config
no maximum-paths
This command resets the number of paths that OSPF can report for a given destination back
to its default value.
Format no maximum-paths
Mode Router OSPFv3 Config
IPv6 Commands 873

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
passive-interface default (OSPFv3)
Use this command to enable global passive mode by default for all interfaces. It overrides
any interface level passive mode. OSPF shall not form adjacencies over a passive interface.
Default disabled
Format passive-interface default
Mode Router OSPFv3 Config
no passive-interface default
Use this command to disable the global passive mode by default for all interfaces. Any
interface previously configured to be passive reverts to nonpassive mode.
Format no passive-interface default
Mode Router OSPFv3 Config
passive-interface (OSPFv3)
Use this command to set the interface or tunnel as passive.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id
parameter is a number in the range of 1–4093. You can also use the tunnel keyword and
tunnel-id argument.
Using these arguments overrides the global passive mode that is effective on the interface or
tunnel.
Default disabled
Format passive-interface {unit/slot/port | vlan vland-id | tunnel tunnel-id}
Mode Router OSPFv3 Config
no passive-interface
Use this command to set the interface, VLAN, or tunnel as nonpassive. It overrides the global
passive mode that is currently effective on the interface or tunnel.
Format no passive-interface {unit/slot/port | vlan vlan-id | tunnel tunnel-id}
Mode Router OSPFv3 Config
IPv6 Commands 874

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
prefix-suppression (OSPFv3)
This command suppresses the advertisement of all the IPv6 prefixes except for prefixes that
are associated with secondary IPv6 addresses, loopbacks, and passive interfaces from the
OSPFv3 router advertisements.
To suppress a loopback or passive interface, use the ipv ospf prefix-suppression
command in interface configuration mode. Prefixes associated with secondary IPv6
addresses can never be suppressed.
Default Prefix suppression is disabled.
Format prefix-suppression
Mode Router OSPFv3 Config
no prefix-suppression
This command disables prefix-suppression. No prefixes are suppressed from getting
advertised.
Format no prefix-suppression
Mode Router OSPFv3 Config
redistribute (OSPFv3)
This command configures the OSPFv3 protocol to allow redistribution of routes from the
specified source protocol/routers. The metric argument can be a number in the range
0–16777214. The metric type can be 1 or 2. The tag argument can be a number in the range
0–4294967295.
Default metric—unspecified
type—2
tag—0
Format redistribute {static | connected} [metric metric] [metric-type {1 | 2}]
[ tag taq]
Mode Router OSPFv3 Config
no redistribute
This command configures OSPF protocol to prohibit redistribution of routes from the
specified source protocol/routers.
Format no redistribute {static | connected} [metric] [metric-type] [tag]
Mode Router OSPFv3 Config
IPv6 Commands 875

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
router-id (OSPFv3)
This command sets a 4-digit dotted-decimal number uniquely identifying the router ospf id.
The ipaddress is a configured value.
Format router-id ipaddress
Mode Router OSPFv3 Config
timers pacing lsa-group (OSPFv3)
Use this command to adjust how OSPFv3 groups LSAs for periodic refresh. OSPFv3
refreshes self-originated LSAs approximately once every 30 minutes. When OSPFv3
refreshes LSAs, it considers all self-originated LSAs whose age is from 1800 to 1800 plus the
pacing group size. Grouping LSAs for refresh allows OSPFv3 to combine refreshed LSAs
into a minimal number of LS Update packets. Minimizing the number of Update packets
makes LSA distribution more efficient.
When OSPFv3 originates a new or changed LSA, it selects a random refresh delay for the
LSA. When the refresh delay expires, OSPFv3 refreshes the LSA. By selecting a random
refresh delay, OSPFv3 avoids refreshing a large number of LSAs at one time, even if a large
number of LSAs are originated at one time.
The seconds argument represents the width of the window in which LSAs are refreshed. For
the seconds argument, the range for the pacing group window is from 10 to 1800 seconds.
Default 60 seconds
Format timers pacing lsa-group seconds
Mode Router OSPFv3 Config
no timers pacing lsa-group
This command returns the LSA Group Pacing parameter to the factory default value of 60
seconds.
Format no timers pacing lsa-group
Mode Router OSPFv3 Config
timers throttle spf
The initial wait interval is set to an amount of delay specified by the spf-hold value. If an
SPF calculation is not scheduled during the current wait interval, the next SPF calculation is
scheduled at a delay of spf-start. If there has been an SPF calculation scheduled during
the current wait interval, the wait interval is set to two times the current wait interval until the
wait interval reaches the maximum time in milliseconds as specified in spf-maximum.
IPv6 Commands 876

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Subsequent wait times remain at the maximum until the values are reset or an LSA is
received between SPF calculations.
Default spf-start = 2000 ms
spf-hold = 5000 ms
spf-maximum = 5000 ms
Format timers throttle spf spf-start spf-hold spf-maximum
Mode Router OSPFv3 Config
Parameter Description
spf-start Indicates the SPF schedule delay in milliseconds when no SPF calculation has been scheduled
during the current wait interval. Value range is 1 to 600000 milliseconds.
spf-hold Indicates the initial SPF wait interval in milliseconds. Value range is 1 to 600000 milliseconds.
spf-maximum Indicates the maximum SPF wait interval in milliseconds. Value range is 1 to 600000 milliseconds.
no timers throttle spf
This command returns the SPF throttling parameters to the factory default values.
Format no timers throttle spf
Mode Router OSPFv3 Config
trapflags (OSPFv3)
Use this command to enable individual OSPF traps, enable a group of trap flags at a time, or
enable all the trap flags at a time. The different groups of trapflags, and each group’s specific
trapflags to enable or disable, are listed in the following table.
Table 12. Trapflag groups (OSPFv3)
Group Flags
errors • authentication-failure
• bad-packet
• config-error
• virt-authentication-failure
• virt-bad-packet
• virt-config-error
lsa • lsa-maxage
• lsa-originate
overflow • lsdb-overflow
• lsdb-approaching-overflow
IPv6 Commands 877

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 12. Trapflag groups (OSPFv3)
Group Flags
retransmit • packets
• virt-packets
state-change • if-state-change
• neighbor-state-change
• virtif-state-change
• virtneighbor-state-change
• To enable the individual flag, enter the trapflags group name followed by a particular
flag.
• To enable all the flags in that group, enter trapflags group name followed by all.
• To enable all the flags, enter the command as trapflags all.
Default disabled
Format trapflags {all | errors {all | authentication-failure | bad-packet |
config-error | virt-authentication-failure | virt-bad-packet |
virt-config-error} | lsa {all | lsa-maxage | lsa-originate} | overflow {all |
lsdb-overflow | lsdb-approaching-overflow} | retransmit {all | packets |
virt-packets} | state-change {all | if-state-change | neighbor-state-change |
virtif-state-change | virtneighbor-state-change}}
Mode Router OSPFv3 Config
no trapflags
Use this command to revert to the default reference bandwidth.
• To disable the individual flag, enter the no trapflags group name followed by a
particular flag.
• To disable all the flags in that group, enter no trapflags group name followed by
all.
• To disable all the flags, enter the command as no trapflags all.
Format no trapflags {all | errors {all | authentication-failure | bad-packet |
config-error | virt-authentication-failure | virt-bad-packet |
virt-config-error} | lsa {all | lsa-maxage | lsa-originate} | overflow {all |
lsdb-overflow | lsdb-approaching-overflow} | retransmit {all | packets |
virt-packets} | state-change {all | if-state-change | neighbor-state-change |
virtif-state-change | virtneighbor-state-change}}
Mode Router OSPFv3 Config
IPv6 Commands 878

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
OSPFv3 Interface Commands
ipv6 ospf area
This command sets the OSPF area to which the specified router interface or range of
interfaces belongs. It also enables OSPF on the specified router interface or range of
interfaces. The area-id is a 32-bit integer, formatted as a 4-digit dotted-decimal number or
a decimal value in the range of 0-4294967295. The area-id uniquely identifies the area to
which the interface connects. Assigning an area ID for an area that does not yet exist, causes
the area to be created with default values.
Format ipv6 ospf area area-id
Mode Interface Config
ipv6 ospf cost
This command configures the cost on an OSPF interface or range of interfaces. The cost
parameter has is in the range of 1 to 65535.
Default 10
Format ipv6 ospf cost cost
Mode Interface Config
no ipv6 ospf cost
This command configures the default cost on an OSPF interface.
Format no ipv6 ospf cost
Mode Interface Config
ipv6 ospf dead-interval
This command sets the OSPF dead interval for the specified interface or range of interfaces.
The value for seconds is a valid positive integer, which represents the length of time in
seconds that a router's Hello packets have not been seen before its neighbor routers declare
that the router is down. The value for the length of time must be the same for all routers
attached to a common network. This value should be some multiple of the Hello Interval (that
is, 4). A valid value for seconds is in the range from 1-65535.
Default 40
Format ipv6 ospf dead-interval seconds
Mode Interface Config
IPv6 Commands 879

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ipv6 ospf dead-interval
This command sets the default OSPF dead interval for the specified interface or range of
interfaces.
Format no ipv6 ospf dead-interval
Mode Interface Config
ipv6 ospf hello-interval
This command sets the OSPF hello interval for the specified interface. The value for
seconds is a valid positive integer, which represents the length of time in seconds. The
value for the length of time must be the same for all routers attached to a network. A valid
value for seconds is in the range from 1 to 65535.
Default 10
Format ipv6 ospf hello-interval seconds
Mode Interface Config
no ipv6 ospf hello-interval
This command sets the default OSPF hello interval for the specified interface.
Format no ipv6 ospf hello-interval
Mode Interface Config
ipv6 ospf link-lsa-suppression
Use this command to enable Link LSA Suppression on an interface. When Link LSA
Suppression is enabled on a point-to-point (P2P) interface, no Link LSA protocol packets are
originated (transmitted) on the interface. This configuration does not apply to non-P2P
interfaces.
Default False
Format ipv6 ospf link-lsa-suppression
Mode Privileged EXEC
IPv6 Commands 880

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ipv6 ospf link-lsa-suppression
This command returns Link LSA Suppression for the interface to disabled. When Link LSA
Suppression is disabled, Link LSA protocol packets are originated (transmitted) on the P2P
interface.
Format no ipv6 ospf link-lsa-suppression
Mode Privileged EXEC
ipv6 ospf mtu-ignore
This command disables OSPF maximum transmission unit (MTU) mismatch detection on an
interface or range of interfaces. OSPF Database Description packets specify the size of the
largest IP packet that can be sent without fragmentation on the interface. When a router
receives a Database Description packet, it examines the MTU advertised by the neighbor. By
default, if the MTU is larger than the router can accept, the Database Description packet is
rejected and the OSPF adjacency is not established.
Default enabled
Format ipv6 ospf mtu-ignore
Mode Interface Config
no ipv6 ospf mtu-ignore
This command enables the OSPF MTU mismatch detection.
Format no ipv6 ospf mtu-ignore
Mode Interface Config
ipv6 ospf network
This command changes the default OSPF network type for the interface or range of
interfaces. Normally, the network type is determined from the physical IP network type. By
default all Ethernet networks are OSPF type broadcast. Similarly, tunnel interfaces default to
point-to-point. When an Ethernet port is used as a single large bandwidth IP network
between two routers, the network type can be point-to-point since there are only two routers.
Using point-to-point as the network type eliminates the overhead of the OSPF designated
router election. It is normally not useful to set a tunnel to OSPF network type broadcast.
Default broadcast
Format ipv6 ospf network {broadcast | point-to-point}
Mode Interface Config
IPv6 Commands 881

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ipv6 ospf network
This command sets the interface type to the default value.
Format no ipv6 ospf network {broadcast | point-to-point}
Mode Interface Config
ipv6 ospf prefix-suppression
This command suppresses the advertisement of the IPv6 prefixes that are associated with an
interface, except for those associated with secondary IPv6 addresses. This command takes
precedence over the global configuration. If this configuration is not specified, the global
prefix-suppression configuration applies.
prefix-suppression can be disabled at the interface level by using the disable option. The
disable option is useful for excluding specific interfaces from performing prefix-suppression
when the feature is enabled globally.
Note that the disable option disable is not equivalent to not configuring the interface specific
prefix-suppression. If prefix-suppression is not configured at the interface level, the global
prefix-suppression configuration is applicable for the IPv6 prefixes associated with the
interface.
Default prefix-suppression is not configured.
Format ipv6 ospf prefix-suppression [disable]
Mode Interface Config
no ipv6 ospf prefix-suppression
This command removes prefix-suppression configurations at the interface level. When the no
ipv6 ospf prefix-suppression command is used, global prefix-suppression applies
to the interface. Not configuring the command is not equal to disabling interface level
prefix-suppression.
Format no ipv6 ospf prefix-suppression
Mode Interface Config
ipv6 ospf priority
This command sets the OSPF priority for the specified router interface or range of interfaces.
For the priority argument, the priority of the interface is an integer in the range from 0 to
IPv6 Commands 882

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
255. A value of 0 indicates that the router is not eligible to become the designated router on
this network.
Default 1, which is the highest router priority
Format ipv6 ospf priority priority
Mode Interface Config
no ipv6 ospf priority
This command sets the default OSPF priority for the specified router interface.
Format no ipv6 ospf priority
Mode Interface Config
ipv6 ospf retransmit-interval
This command sets the OSPF retransmit Interval for the specified interface or range of
interfaces. The retransmit interval is specified in seconds. The value for seconds is the
number of seconds between link-state advertisement retransmissions for adjacencies
belonging to this router interface. This value is also used when retransmitting database
description and link-state request packets. For the seconds argument, a valid value is in the
range from 0 to 3600 seconds (1 hour).
Default 5
Format ipv6 ospf retransmit-interval seconds
Mode Interface Config
no ipv6 ospf retransmit-interval
This command sets the default OSPF retransmit Interval for the specified interface.
Format no ipv6 ospf retransmit-interval
Mode Interface Config
ipv6 ospf transmit-delay
This command sets the OSPF Transit Delay for the specified interface or range of interfaces.
The transmit delay is specified in seconds. In addition, it sets the estimated number of
seconds it takes to transmit a link state update packet over this interface. For the seconds
argument, a valid value is in the range from 0 to 3600 seconds (1 hour).
Default 1
IPv6 Commands 883

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format ipv6 ospf transmit-delay seconds
Mode Interface Config
no ipv6 ospf transmit-delay
This command sets the default OSPF Transit Delay for the specified interface.
Format no ipv6 ospf transmit-delay
Mode Interface Config
OSPFv3 Graceful Restart Commands
The OSPFv3 protocol can be configured to participate in the checkpointing service, so that
these protocols can execute a graceful restart when the management unit fails. In a graceful
restart, the hardware to continues forwarding IPv6 packets using OSPFv3 routes while a
backup switch takes over management unit responsibility.
Graceful restart uses the concept of helpful neighbors. A fully adjacent router enters helper
mode when it receives a link state announcement (LSA) from the restarting management unit
indicating its intention of performing a graceful restart. In helper mode, a switch continues to
advertise to the rest of the network that they have full adjacencies with the restarting router,
thereby avoiding announcement of a topology change and and the potential for flooding of
LSAs and shortest-path-first (SPF) runs (which determine OSPF routes). Helpful neighbors
continue to forward packets through the restarting router. The restarting router relearns the
network topology from its helpful neighbors.
Graceful restart can be enabled for either planned or unplanned restarts, or both. You can
initiate a planned restart through the management command initiate failover. You
can initiate a failover in order to take the management unit out of service (for example, to
address a partial hardware failure), to correct faulty system behavior which cannot be
corrected through less severe management actions, or other reasons. An unplanned restart
is an unexpected failover caused by a fatal hardware failure of the management unit or a
software hang or crash on the management unit.
nsf (OSPFv3)
Use this command to enable the OSPF graceful restart functionality on an interface. To
disable graceful restart, use the no form of the command.
Default Disabled
Format nsf [ietf] [planned-only]
Modes Router OSPFv3 Config
IPv6 Commands 884

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
ietf This keyword is accepted but not required.
planned-only This optional keyword indicates that OSPF should only perform a graceful restart when the restart is
planned (that is, when the restart is a result of the initiate failover command).
no nsf (OSPFv3)
Use this command to disable graceful restart for all restarts.
Format no nsf [ietf] [planned-only]
Modes Router OSPFv3 Config
nsf restart-interval (OSPFv3)
Use this command to configure the number of seconds that the restarting router asks its
neighbors to wait before exiting helper mode. This is referred to as the grace period. The
restarting router includes the grace period in its grace LSAs. For planned restarts (using the
initiate failover command), the grace LSAs are sent prior to restarting the
management unit, whereas for unplanned restarts, they are sent after reboot begins.
The grace period must be set long enough to allow the restarting router to reestablish all of its
adjacencies and complete a full database exchange with each of those neighbors. For the
seconds argument, a valid value is in the range from 0 to 1800 seconds.
Default 120 seconds
Format nsf [ietf] restart-interval seconds
Modes Router OSPFv3 Config
Parameter Description
ietf This keyword is accepted but not required.
seconds The number of seconds that the restarting router asks its neighbors to wait before exiting helper
mode. The range is from 1 to 1800 seconds.
no nsfrestart-interval (OSPFv3)
Use this command to revert the grace period to its default value.
Format no [ietf] nsf restart-interval
Modes Router OSPFv3 Config
IPv6 Commands 885

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
nsf helper (OSPFv3)
Use this command to enable helpful neighbor functionality for the OSPF protocol. You can
enable this functionality for planned or unplanned restarts, or both.
Default OSPF may act as a helpful neighbor for both planned and unplanned restarts
Format nsf helper [planned-only]
Modes Router OSPFv3 Config
Parameter Description
planned-only This optional keyword indicates that OSPF should only help a restarting router performing a planned
restart.
no nsf helper (OSPFv3)
Use this command to disable helpful neighbor functionality for OSPF.
Format no nsf helper
Modes Router OSPFv3 Config
nsf ietf helper disable (OSPFv3)
Use this command to disable helpful neighbor functionality for OSPF.
Note: The commands no nsf helper and nsf ietf helper disable
are functionally equivalent. The command nsf ietf helper
disable is supported solely for compatibility with other network
software CLI.
Format nsf ietf helper disable
Modes Router OSPFv3 Config
nsf helper strict-lsa-checking (OSPFv3)
The restarting router is unable to react to topology changes. In particular, the restarting router
will not immediately update its forwarding table; therefore, a topology change may introduce
forwarding loops or black holes that persist until the graceful restart completes. By exiting the
graceful restart on a topology change, a router tries to eliminate the loops or black holes as
quickly as possible by routing around the restarting router. A helpful neighbor considers a link
down with the restarting router to be a topology change, regardless of the strict LSA checking
configuration.
IPv6 Commands 886

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Use this command to require that an OSPF helpful neighbor exit helper mode whenever a
topology change occurs.
Default Enabled.
Format nsf [ietf] helper strict-lsa-checking
Modes Router OSPFv3 Config
Parameter Description
ietf This keyword is accepted but not required.
no nsf [ietf] helper strict-lsa-checking (OSPFv3)
Use this command to allow OSPF to continue as a helpful neighbor in spite of topology
changes.
Default Enabled.
Format nsf [ietf] helper strict-lsa-checking
Modes Router OSPFv3 Config
OSPFv3 Stub Router Commands
max-metric router-lsa (OSPFv3 Router Configuration)
To configure OSPFv3 to enter stub router mode, use this command in Router OSPFv3
Global Configuration mode. When OSPFv3 is in stub router mode, OSPFv3 sets the metric in
the nonstub links in its router LSA to MaxLinkMetric. Other routers therefore compute very
long paths through the stub router, and prefer any alternate path. Doing so eliminates all
transit traffic through the stub router, when alternate routes are available. Stub router mode is
useful when adding or removing a router from a network or to avoid transient routes when a
router reloads.
You can administratively force OSPFv3 into stub router mode. OSPFv3 remains in stub
router mode until you take OSPFv3 out of stub router mode. Alternatively, you can configure
OSPF to start in stub router mode for a configurable period of time after the router boots up.
If you set the summary LSA metric to 16,777,215, other routers skip the summary LSA when
they compute routes.
If you have configured the router to enter stub router mode on startup (max-metric router-lsa
on-startup), and then enter max-metric router lsa, there is no change. If OSPFv3 is
administratively in stub router mode (the max-metric router-lsa command has been given),
and you configure OSPFv3 to enter stub router mode on startup (max-metric router-lsa
on-startup), OSPFv3 exits stub router mode (assuming the startup period has expired) and
IPv6 Commands 887

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
the configuration is updated. Without any parameters, stub router mode only sends maximum
metric values for router LSAs.
Default OSPF is not in stub router mode by default
Format max-metric router-lsa [on-startup seconds] [summary-lsa {metric}]
max-metric router-lsa [external-lsa [max-metric-value]] [inter-area-lsas
[max-metric-value]] [on-startup seconds] [summary-lsa [max-metric-value]]
Mode OSPFv3 Router Configuration
Parameter Description
external-lsa (Optional) Sends the maximum metric values for external LSAs. max-metric-value is the
maximum metric value to use for LSAs. The range is 1 to 16777215 (0xFFFFFF). The default value
is 16711680 (0xFF0000).
inter-area-lsas (Optional) Sends the maximum metric values for Inter-Area-Router LSAs. max-metric-value is
the maximum metric value to use for LSAs. The range is 1 to 16777215 (0xFFFFFF). The default
value is 16711680 (0xFF0000).
on-startup (Optional) Starts OSPF in stub router mode. seconds is the number of seconds that OSPF remains
in stub router mode after a reboot. The range is 5 to 86,400 seconds. There is no default value.
summary-lsa (Optional) Sends the maximum metric values for Summary LSAs. max-metric-value is the
maximum metric value to use for LSAs. The range is 1 to 16777215 (0xFFFFFF). The default value
is 16711680 (0xFF0000).
no max-metric router-lsa
Use this command in OSPFv3 Router Configuration mode to disable stub router mode. The
command clears either type of stub router mode (always or on-startup) and resets all LSA
options. If OSPF is configured to enter global configuration mode on startup, and during
normal operation you want to immediately place OSPF in stub router mode, issue the
command no max-metric router-lsa on-startup. The command no max-metric
router-lsa with the external-lsa, inter-area-lsas, on-startup, or
summary-lsa option causes OSPF to send summary LSAs with metrics computed using
normal procedures.
Format no max-metric router-lsa [external-lsa] [inter-area-lsas] [on-startup]
[summary-lsa]
Mode OSPFv3 Router Configuration
clear ipv6 ospf stub-router
Use this command to force OSPF to exit stub router mode when it has automatically entered
stub router mode because of a resource limitation. OSPF only exits stub router mode if it
entered stub router mode because of a resource limitation or it if is in stub router mode at
IPv6 Commands 888
