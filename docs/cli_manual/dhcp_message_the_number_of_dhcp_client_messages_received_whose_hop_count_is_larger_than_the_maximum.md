# dhcp_message_the_number_of_dhcp_client_messages_received_whose_hop_count_is_larger_than_the_maximum

Pages: 724-744

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
I nterface UDP Port Discard Hit Count Server Address
--------------- ----------- -------- ---------- ---------------
1 /0/1 d hcp N o 1 0 10.100.1.254
1/0/17 a ny Y es 2 10.100.2.254
show ip helper statistics
Use this command to display the number of DHCP and other UDP packets processed and
relayed by the UDP relay agent.
Format show ip helper statistics
Mode Privileged EXEC
Parameter Description
DHCP client The number of valid messages received from a DHCP client. The count is only incremented if IP
messages received helper is enabled globally, the ingress routing interface is up, and the packet passes a number of
validity checks, such as having a TTL>1 and having valid source and destination IP addresses.
DHCP client The number of DHCP client messages relayed to a server. If a message is relayed to multiple
messages relayed servers, the count is incremented once for each server.
DHCP server The number of DHCP responses received from the DHCP server. This count only includes
messages received messages that the DHCP server unicasts to the relay agent for relay to the client.
DHCP server The number of DHCP server messages relayed to a client.
messages relayed
UDP clients The number of valid UDP packets received. This count includes DHCP messages and all other
messages received protocols relayed. Conditions are similar to those for the first statistic in this table.
UDP clients The number of UDP packets relayed. This count includes DHCP messages relayed as well as all
messages relayed other protocols. The count is incremented for each server to which a packet is sent.
DHCP message The number of DHCP client messages received whose hop count is larger than the maximum
hop count allowed. The maximum hop count is a configurable value listed in show bootpdhcprelay. A log
exceeded max message is written for each such failure. The DHCP relay agent does not relay these packets.
DHCP message The number of DHCP client messages received whose secs field is less than the minimum value.
with secs field The minimum secs value is a configurable value and is displayed in show bootpdhcprelay. A log
below min message is written for each such failure. The DHCP relay agent does not relay these packets.
DHCP message The number of DHCP client messages received whose gateway address, giaddr, is already set to an
with giaddr set to IP address configured on one of the relay agent’s own IP addresses. In this case, another device is
local address attempting to spoof the relay agent’s address. The relay agent does not relay such packets. A log
message gives details for each occurrence.
Packets with The number of packets received with TTL of 0 or 1 that might otherwise have been relayed.
expired TTL
Packets that The number of packets ignored by the relay agent because they match a discard relay entry.
matched a discard
entry
Routing Commands 724

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch)#show ip helper statistics
DHCP client messages received.................. 8
DHCP client messages relayed................... 2
DHCP server messages received.................. 2
DHCP server messages relayed................... 2
UDP client messages received................... 8
UDP client messages relayed.................... 2
DHCP message hop count exceeded max............ 0
DHCP message with secs field below min......... 0
DHCP message with giaddr set to local address.. 0
Packets with expired TTL....................... 0
Packets that matched a discard entry........... 0
Open Shortest Path First Commands
This section describes the commands you use to view and configure Open Shortest Path
First (OSPF), which is a link-state routing protocol that you use to route traffic within a
network. This section contains the following subsections:
• General OSPF Commands on page725
• OSPF Interface Commands on page745
• IP Event Dampening Commands on page752
• OSPFv2 Stub Router Commands on page757
• OSPF Show Commands on page758
General OSPF Commands
router ospf
Use this command to enter Router OSPF mode.
Format router ospf
Mode Global Config
enable (OSPF)
This command resets the default administrative mode of OSPF in the router (active).
Default enabled
Format enable
Mode Router OSPF Config
Routing Commands 725

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no enable (OSPF)
This command sets the administrative mode of OSPF in the router to inactive.
Format no enable
Mode Router OSPF Config
network area (OSPF)
Use this command to enable OSPFv2 on an interface and set its area ID if the IP address of
an interface is covered by this network command.
Default disabled
Format network ip-address wildcard-mask area area-id
Mode Router OSPF Config
no network area (OSPF)
Use this command to disable the OSPFv2 on a interface if the IP address of an interface was
earlier covered by this network command.
Format no network ip-address wildcard-mask area area-id
Mode Router OSPF Config
1583compatibility
This command enables OSPF 1583 compatibility.
Note: 1583 compatibility mode is enabled by default. If all OSPF routers in
the routing domain are capable of operating according to RFC 2328,
OSPF 1583 compatibility mode should be disabled.
Default enabled
Format 1583compatibility
Mode Router OSPF Config
Routing Commands 726

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no 1583compatibility
This command disables OSPF 1583 compatibility.
Format no 1583compatibility
Mode Router OSPF Config
area default-cost (OSPF)
This command configures the default cost for the stub area. For the value argument, you
must specify an integer value between 1–16777215.
Format area area-id default-cost value
Mode Router OSPF Config
area nssa (OSPF)
This command configures the specified area-id to function as an NSSA.
Format area area-id nssa
Mode Router OSPF Config
no area nssa
This command disables nssa from the specified area id.
Format no area area-id nssa
Mode Router OSPF Config
area nssa default-info-originate (OSPF)
This command configures the metric value and type for the default route advertised into the
NSSA. The optional metric parameter specifies the metric of the default route and must be
in the range 1–16777214. If no metric is specified, the default value is ****. The metric type
can be comparable (nssa-external 1) or noncomparable (nssa-external 2).
Format area area-id nssa default-info-originate [metric] [comparable |
non-comparable]
Mode Router OSPF Config
Routing Commands 727

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no area nssa default-info-originate (OSPF)
This command disables the default route advertised into the NSSA.
Format no area area-id nssa default-info-originate [metric] [comparable |
non-comparable]
Mode Router OSPF Config
area nssa no-redistribute (OSPF)
This command configures the NSSA Area Border router (ABR) so that learned external
routes will not be redistributed to the NSSA.
Format area area-id nssa no-redistribute
Mode Router OSPF Config
no area nssa no-redistribute (OSPF)
This command disables the NSSA ABR so that learned external routes are redistributed to
the NSSA.
Format no area area-id nssa no-redistribute
Mode Router OSPF Config
area nssa no-summary (OSPF)
This command configures the NSSA so that summary LSAs are not advertised into the
NSSA.
Format area area-id nssa no-summary
Mode Router OSPF Config
no area nssa no-summary (OSPF)
This command disables nssa from the summary LSAs.
Format no area area-id nssa no-summary
Mode Router OSPF Config
area nssa translator-role (OSPF)
This command configures the translator role of the NSSA. The always keyword causes the
router to assume the role of the translator the instant it becomes a border router; The and the
candidate keyword causes the router to participate in the translator election process when
it attains border router status.
Routing Commands 728

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format area area-id nssa translator-role {always | candidate}
Mode Router OSPF Config
no area nssa translator-role (OSPF)
This command disables the nssa translator role from the specified area id.
Format no area area-id nssa translator-role {always | candidate}
Mode Router OSPF Config
area nssa translator-stab-intv (OSPF)
This command configures the translator stabilityinterval of the NSSA. The
stabilityinterval is the period of time that an elected translator continues to perform its
duties after it determines that its translator status has been deposed by another router.
Format area area-id nssa translator-stab-intv stabilityinterval
Mode Router OSPF Config
no area nssa translator-stab-intv (OSPF)
This command disables the nssa translator’s stabilityinterval from the specified area
id.
Format no area area-id nssa translator-stab-intv stabilityinterval
Mode Router OSPF Config
area range (OSPF)
Use the area range command in Router Configuration mode to configure a summary prefix
that an area border router advertises for a specific area.
Default No area ranges are configured by default. No cost is configured by default.
Format area area-id range ip-address netmask {summarylink | nssaexternallink}
[advertise | not-advertise] [cost cost]
Mode OSPFv2 Router Configuration
Parameter Description
area-id The area identifier for the area whose networks are to be summarized.
prefix netmask The summary prefix to be advertised when the ABR computes a route to one or more networks
within this prefix in this area.
Routing Commands 729

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
summarylink When this keyword is given, the area range is used when summarizing prefixes advertised in type 3
summary LSAs.
nssaexternallink When this keyword is given, the area range is used when translating type 7 LSAs to type 5 LSAs.
advertise [Optional] When this keyword is given, the summary prefix is advertised when the area range is
active. This is the default.
not-advertise [Optional] When this keyword is given, neither the summary prefix nor the contained prefixes are
advertised when the area range is active. When the not-advertise option is given, any static cost
previously configured is removed from the system configuration.
cost [Optional] If an optional cost is given, OSPF sets the metric field in the summary LSA to the
configured value rather than setting the metric to the largest cost among the networks covered by
the area range. A static cost may only be configured if the area range is configured to advertise the
summary. The range is 0 to 16,777,215. If the cost is set to 16,777,215 for type 3 summarization, a
type 3 summary LSA is not advertised, but contained networks are suppressed. This behavior is
equivalent to specifying the not-advertise option. If the range is configured for type 7 to type 5
translation, a type 5 LSA is sent if the metric is set to 16,777,215; however, other routers will not
compute a route from a type 5 LSA with this metric.
no area range
The no area range command deletes a specified area range or reverts an option to its
default.
Format no area area-id range prefix netmask {summarylink | nssaexternallink}
[advertise | not-advertise] [cost]
Mode OSPFv2 Router Configuration
Command example:
!! Create area range
(NETGEAR Switch) (Config-router)#area 1 range 10.0.0.0 255.0.0.0 summarylink
!! Delete area range
(NETGEAR Switch) (Config-router)#no area 1 range 10.0.0.0 255.0.0.0 summarylink
You can use the no area range command to revert the
[advertise | not-advertise] option to its default without deleting the area range.
Deleting and recreating the area range would cause OSPF to temporarily advertise the
prefixes contained within the range. Note that using either the advertise or
not-advertise keyword reverts the configuration to the default. For example:
!! Create area range. Suppress summary.
(NETGEAR Switch) (Config-router)#area 1 range 10.0.0.0 255.0.0.0 summarylink
not-advertise
!! Advertise summary.
(NETGEAR Switch) (Config-router)#no area 1 range 10.0.0.0 255.0.0.0 summarylink
not-advertise
Routing Commands 730

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
You can also use the no area range command to remove a static area range cost, so that
OSPF sets the cost to the largest cost among the contained routes.
!! Create area range with static cost.
(NETGEAR Switch) (Config-router)#area 1 range 10.0.0.0 255.0.0.0 summarylink cost 1000
!! Remove static cost.
(NETGEAR Switch) (Config-router)#no area 1 range 10.0.0.0 255.0.0.0 summarylink cost
area stub (OSPF)
This command creates a stub area for the specified area ID. A stub area is characterized by
the fact that AS External LSAs are not propagated into the area. Removing AS External LSAs
and Summary LSAs can significantly reduce the link state database of routers within the stub
area.
Format area area-id stub
Mode Router OSPF Config
no area stub
This command deletes a stub area for the specified area ID.
Format no area area-id stub
Mode Router OSPF Config
area stub no-summary (OSPF)
This command configures the Summary LSA mode for the stub area identified by area-id.
Use this command to prevent LSA Summaries from being sent.
Default disabled
Format area area-id stub no-summary
Mode Router OSPF Config
no area stub no-summary
This command configures the default Summary LSA mode for the stub area identified by
area-id.
Format no area area-id stub no-summary
Mode Router OSPF Config
Routing Commands 731

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
area virtual-link (OSPF)
This command creates the OSPF virtual interface for the specified area-id and neighbor.
The neighbor parameter is the Router ID of the neighbor.
Format area area-id virtual-link neighbor
Mode Router OSPF Config
no area virtual-link
This command deletes the OSPF virtual interface from the given interface, identified by
area-id and neighbor. The neighbor parameter is the Router ID of the neighbor.
Format no area area-id virtual-link neighbor
Mode Router OSPF Config
area virtual-link authentication
This command configures the authentication type and key for the OSPF virtual interface
identified by area-id and neighbor. The neighbor parameter is the Router ID of the
neighbor. The type of authentication can be either none, simple, or encrypt. If you select
simple or encrypt, the key parameter is composed of standard displayable, noncontrol
keystrokes from a standard 101/102-key keyboard. The authentication key must be 8 bytes
or less if the authentication type is simple. If the type is encrypt, the key can be up to 16
bytes. Unauthenticated interfaces do not need an authentication key. If the type is encrypt,
a keyid in the range of 0 and 255 must be specified. The default value for authentication
type is none. Neither the default password key nor the default key id are configured.
Default none
Format area area-id virtual-link neighbor authentication {none | simple key| encrypt
key keyid}
Mode Router OSPF Config
no area virtual-link authentication
This command configures the default authentication type for the OSPF virtual interface
identified by area-id and neighbor. The neighbor parameter is the Router ID of the
neighbor.
Format no area area-id virtual-link neighbor authentication
Mode Router OSPF Config
Routing Commands 732

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
area virtual-link dead-interval (OSPF)
This command configures the dead interval for the OSPF virtual interface on the virtual
interface identified by area-id and neighbor. The neighbor parameter is the Router ID
of the neighbor. The range for seconds is 1 to 65535.
Default 40
Format area area-id virtual-link neighbor dead-interval seconds
Mode Router OSPF Config
no area virtual-link dead-interval
This command configures the default dead interval for the OSPF virtual interface on the
virtual interface identified by area-id and neighbor. The neighbor parameter is the
Router ID of the neighbor.
Format no area area-id virtual-link neighbor dead-interval
Mode Router OSPF Config
area virtual-link hello-interval (OSPF)
This command configures the hello interval for the OSPF virtual interface on the virtual
interface identified by area-id and neighbor. The neighbor parameter is the Router ID
of the neighbor. The range for seconds is 1 to 65535.
Default 10
Format area area-id virtual-link neighbor hello-interval 1-65535
Mode Router OSPF Config
no area virtual-link hello-interval
This command configures the default hello interval for the OSPF virtual interface on the
virtual interface identified by area-id and neighbor. The neighbor parameter is the
Router ID of the neighbor.
Format no area area-id virtual-link neighbor hello-interval
Mode Router OSPF Config
Routing Commands 733

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
area virtual-link retransmit-interval (OSPF)
This command configures the retransmit interval for the OSPF virtual interface on the virtual
interface identified by area-id and neighbor. The neighbor parameter is the Router ID
of the neighbor. The range for seconds is 0 to 3600.
Default 5
Format area area-id virtual-link neighbor retransmit-interval seconds
Mode Router OSPF Config
no area virtual-link retransmit-interval
This command configures the default retransmit interval for the OSPF virtual interface on the
virtual interface identified by area-id and neighbor. The neighbor parameter is the
Router ID of the neighbor.
Format no area area-id virtual-link neighbor retransmit-interval
Mode Router OSPF Config
area virtual-link transmit-delay (OSPF)
This command configures the transmit delay for the OSPF virtual interface on the virtual
interface identified by area-id and neighbor. The neighbor parameter is the Router ID
of the neighbor. The range for seconds is 0 to 3600 (1 hour).
Default 1
Format area area-id virtual-link neighbor transmit-delay seconds
Mode Router OSPF Config
no area virtual-link transmit-delay
This command resets the default transmit delay for the OSPF virtual interface to the default
value.
Format no area area-id virtual-link neighbor transmit-delay
Mode Router OSPF Config
auto-cost (OSPF)
By default, OSPF computes the link cost of each interface from the interface bandwidth.
Faster links have lower metrics, making them more attractive in route selection. The
configuration parameters in the auto-cost reference bandwidth and bandwidth
commands give you control over the default link cost. You can configure for OSPF an
interface bandwidth that is independent of the actual link speed. A second configuration
parameter allows you to control the ratio of interface bandwidth to link cost. The link cost is
Routing Commands 734

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
computed as the ratio of a reference bandwidth to the interface bandwidth (ref_bw / interface
bandwidth), in which interface bandwidth is defined by the bandwidth command. Because
the default reference bandwidth is 100 Mbps, OSPF uses the same default link cost for all
interfaces whose bandwidth is 100 Mbps or greater. Use the auto-cost command to
change the reference bandwidth, specifying the reference bandwidth in megabits per second
(Mbps). For the mbps parameter, the reference bandwidth range is 1–4294967 Mbps.
Default 100 Mbps
Format auto-cost reference-bandwidth mbps
Mode Router OSPF Config
no auto-cost reference-bandwidth (OSPF)
Use this command to set the reference bandwidth to the default value.
Format no auto-cost reference-bandwidth
Mode Router OSPF Config
capability opaque
Use this command to enable Opaque Capability on the Router. The information contained in
Opaque LSAs may be used directly by OSPF or indirectly by an application wishing to
distribute information throughout the OSPF domain. The switch supports the storing and
flooding of Opaque LSAs of different scopes. The default value of enabled means that OSPF
will forward opaque LSAs by default. If you want to upgrade from a previous release, where
the default was disabled, opaque LSA forwarding will be enabled. If you want to disable
opaque LSA forwarding, then you should enter the command no capability opaque in OSPF
router configuration mode after the software upgrade.
Default enabled
Format capability opaque
Mode Router Config
no capability opaque
Use this command to disable opaque capability on the router.
Format no capability opaque
Mode Router Config
Routing Commands 735

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
clear ip ospf
Use this command to disable and re-enable OSPF.
Format clear ip ospf
Mode Privileged EXEC
clear ip ospf configuration
Use this command to reset the OSPF configuration to factory defaults.
Format clear ip ospf configuration
Mode Privileged EXEC
clear ip ospf counters
Use this command to reset global and interface statistics.
Format clear ip ospf counters
Mode Privileged EXEC
clear ip ospf neighbor
Use this command to drop the adjacency with all OSPF neighbors. On each neighbor’s
interface, send a one-way hello. Adjacencies may then be re-established. To drop all
adjacencies with a specific router ID, specify the neighbor’s Router ID using the optional
parameter neighbor-id.
Format clear ip ospf neighbor [neighbor-id]
Mode Privileged EXEC
clear ip ospf neighbor interface
To drop adjacency with all neighbors on a specific interface, use the optional parameter
unit/slot/port. To drop adjacency with a specific router ID on a specific interface, use
the optional parameter neighbor-id.
Format clear ip ospf neighbor interface [unit/slot/port] [neighbor-id]
Mode Privileged EXEC
Routing Commands 736

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
clear ip ospf redistribution
Use this command to flush all self-originated external LSAs. Reapply the redistribution
configuration and reoriginate prefixes as necessary.
Format clear ip ospf redistribution
Mode Privileged EXEC
default-information originate (OSPF)
This command is used to control the advertisement of default routes. The metric argument
can be a number in the range 0–16777214. The metric type can be 1 or 2.
Default metric—unspecified
type—2
Format default-information originate [always] [metric metric] [metric-type {1 | 2}]
Mode Router OSPF Config
no default-information originate (OSPF)
This command is used to reset the advertisement of default routes to default values.
Format no default-information originate [metric] [metric-type]
Mode Router OSPF Config
default-metric (OSPF)
This command is used to set a default for the metric of distributed routes. The metric
argument can be a number in the range 0–16777214.
Format default-metric metric
Mode Router OSPF Config
no default-metric (OSPF)
This command is used to reset the default for the metric of distributed routes.
Format no default-metric
Mode Router OSPF Config
distance ospf (OSPF)
This command sets the route preference value of OSPF in the router. Lower route preference
values are preferred when determining the best route. The type of OSPF route can be
Routing Commands 737

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
intra-area, inter-area, or external. All the external type routes are given the same
preference value. The range of preference value is 1 to 255.
Default 110
Format distance ospf {intra-area preference | inter-area preference | external
preference}
Mode Router OSPF Config
no distance ospf
This command resets the default route preference value of OSPF routes in the router. The
type of OSPF route can be intra-area, inter-area, or external.
Format no distance ospf {intra-area | inter-area | external}
Mode Router OSPF Config
distribute-list out (OSPF)
Use this command to specify the access list to filter routes received from the source protocol.
The access-list argument can be a number from 1–199.
Format distribute-list access-list out {rip | static | connected}
Mode Router OSPF Config
no distribute-list out
Use this command to reset the access list to filter routes received from the source protocol.
Format no distribute-list access-list out {rip | static | connected}
Mode Router OSPF Config
exit-overflow-interval (OSPF)
This command configures the exit overflow interval for OSPF. It describes the number of
seconds after entering overflow state that a router will wait before attempting to leave the
overflow state. This allows the router to again originate nondefault AS-external-LSAs. When
set to 0, the router will not leave overflow state until restarted. The range for the seconds
argument is 0 to 2147483647 seconds.
Default 0
Format exit-overflow-interval seconds
Mode Router OSPF Config
Routing Commands 738

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no exit-overflow-interval
This command configures the default exit overflow interval for OSPF.
Format no exit-overflow-interval
Mode Router OSPF Config
external-lsdb-limit (OSPF)
This command configures the external LSDB limit for OSPF. If the value is -1, then there is no
limit. When the number of nondefault AS-external-LSAs in a router's link-state database
reaches the external LSDB limit, the router enters overflow state. The router never holds
more than the external LSDB limit nondefault AS-external-LSAs in it database. The external
LSDB limit MUST be set identically in all routers attached to the OSPF backbone and/or any
regular OSPF area. The range for the limit argument is -1 to 2147483647.
Default -1
Format external-lsdb-limit limit
Mode Router OSPF Config
no external-lsdb-limit
This command configures the default external LSDB limit for OSPF.
Format no external-lsdb-limit
Mode Router OSPF Config
log-adjacency-changes
To enable logging of OSPFv2 neighbor state changes, use the log-adjacency-changes
command in router configuration mode. State changes are logged with INFORMATIONAL
severity.
Default Adjacency state changes are logged, but without the detail option.
Format log-adjacency-changes [detail]
Mode OSPFv2 Router Configuration
Parameter Description
detail (Optional) When this keyword is specified, all adjacency state changes are logged. Otherwise,
OSPF only logs transitions to FULL state and when a backwards transition occurs.
Routing Commands 739

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no log-adjacency-changes
Use the no form of the command to disable state change logging.
Format no log-adjacency-changes [detail]
Mode OSPFv2 Router Configuration
prefix-suppression (Router OSPF Config)
This command suppresses the advertisement of all the IPv4 prefixes except for prefixes that
are associated with secondary IPv4 addresses, loopbacks, and passive interfaces from the
OSPFv2 router advertisements.
To suppress a loopback or passive interface, use the ip ospf prefix-suppression command in
interface configuration mode. Prefixes associated with secondary IPv4 addresses can never
be suppressed.
Default Prefix suppression is disabled.
Format prefix-suppression
Mode Router OSPF Config
no prefix-suppression
This command disables prefix-suppression. No prefixes are suppressed from getting
advertised.
Format no prefix-suppression
Mode Router OSPF Config
router-id (OSPF)
This command sets a 4-digit dotted-decimal number uniquely identifying the router ospf id.
The ipaddress is a configured value.
Format router-id ipaddress
Mode Router OSPF Config
Routing Commands 740

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
redistribute (OSPF)
This command configures the OSPF protocol to allow redistribution of routes from the
specified source protocol or routers. The metric argument can be in the range 0–16777214.
The metric type can be 1 or 2. The tag argument can be in the range 0–4294967295.
Default metric—unspecified
type—2
tag—0
Format redistribute {rip | static | connected} [metric metric] [metric-type {1 | 2}]
[tag tag] [subnets]
Mode Router OSPF Config
no redistribute
This command configures OSPF protocol to prohibit redistribution of routes from the
specified source protocol or routers.
Format no redistribute {rip | static | connected} [metric] [metric-type] [tag]
[subnets]
Mode Router OSPF Config
maximum-paths (OSPF)
This command sets the number of paths that OSPF can report for a given destination in
which maxpaths is platform dependent.
Default 4
Format maximum-paths maxpaths
Mode Router OSPF Config
no maximum-paths
This command resets the number of paths that OSPF can report for a given destination back
to its default value.
Format no maximum-paths
Mode Router OSPF Config
Routing Commands 741

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
passive-interface default
Use this command to enable global passive mode by default for all interfaces. It overrides
any interface level passive mode. OSPF will not form adjacencies over a passive interface.
Default disabled
Format passive-interface default
Mode Router OSPF Config
no passive-interface default
Use this command to disable the global passive mode by default for all interfaces. Any
interface previously configured to be passive reverts to nonpassive mode.
Format no passive-interface default
Mode Router OSPF Config
passive-interface (OSPF)
Use this command to set the interface as passive. It overrides the global passive mode that is
currently effective on the interface. The argument unit/slot/port corresponds to a
physical routing interface or VLAN routing interface. The vlan keyword and vlan-id
parameter are used to specify the VLAN ID of the routing VLAN directly instead of in a
unit/slot/port format. The vlan-id can be a number from 1–4093.
Default disabled
Format passive-interface {unit/slot/port | vlan vlan-id}
Mode Router OSPF Config
no passive-interface
Use this command to set the interface as nonpassive. It overrides the global passive mode
that is currently effective on the interface. The argument unit/slot/port corresponds to a
physical routing interface or VLAN routing interface. The vlan keyword and vlan-id
parameter are used to specify the VLAN ID of the routing VLAN directly instead of in a
unit/slot/port format. The vlan-id can be a number from 1–4093.
Format no passive-interface {unit/slot/port | vlan vlan-id}
Mode Router OSPF Config
timers pacing flood
To adjust the rate at which OSPFv2 sends LS Update packets, use the timers pacing flood
command in router OSPFv2 global configuration mode. OSPF distributes routing information
in Link State Advertisements (LSAs), which are bundled into Link State Update (LS Update)
Routing Commands 742

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
packets. To reduce the likelihood of sending a neighbor more packets than it can buffer,
OSPF rate limits the transmission of LS Update packets. By default, OSPF sends up to 30
updates per second on each interface (1/the pacing interval). Use this command to adjust
this packet rate.
Default 33 milliseconds
Format timers pacing flood milliseconds
Mode OSPFv2 Router Configuration
Parameter Description
milliseconds The average time between transmission of LS Update packets. The range is from 5 ms to 100 ms.
The default is 33 ms.
no timers pacing flood
To revert LSA transmit pacing to the default rate, use the no timers pacing flood command.
Format no timers pacing flood
Mode OSPFv2 Router Configuration
timers pacing lsa-group (OSPF)
To adjust how OSPF groups LSAs for periodic refresh, use the timers pacing lsa-group
command in OSPFv2 Router Configuration mode. OSPF refreshes self-originated LSAs
approximately once every 30 minutes. When OSPF refreshes LSAs, it considers all
self-originated LSAs whose age is from 1800 to 1800 plus the pacing group size. Grouping
LSAs for refresh allows OSPF to combine refreshed LSAs into a minimal number of LS
Update packets. Minimizing the number of Update packets makes LSA distribution more
efficient.
When OSPF originates a new or changed LSA, it selects a random refresh delay for the LSA.
When the refresh delay expires, OSPF refreshes the LSA. By selecting a random refresh
delay, OSPF avoids refreshing a large number of LSAs at one time, even if a large number of
LSAs are originated at one time.
Default 60 seconds
Format timers pacing lsa-group seconds
Mode OSPFv2 Router Configuration
Parameter Description
seconds Width of the window in which LSAs are refreshed. The range for the pacing group window is from 10
to 1800 seconds.
Routing Commands 743

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
timers spf
Use this command to configure the SPF delay time and hold time. The valid range for both
the delay time and hold time parameters is 0–65535 seconds.
Default delay-time—5
hold-time—10
Format timers spf delay-time hold-time
Mode Router OSPF Config
trapflags (OSPF)
Use this command to enable individual OSPF traps, enable a group of trap flags at a time, or
enable all the trap flags at a time. The different groups of trapflags, and each group’s specific
trapflags to enable or disable, are listed in the following table.
Table 11. Trapflags groups
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
retransmit • packets
• virt-packets
state-change • if-state-change
• neighbor-state-change
• virtif-state-change
• virtneighbor-state-change
• To enable the individual flag, enter trapflags and the trapflag group name followed by
the individual flag.
• To enable all the flags in that group, enter trapflags and the trapflag group name
followed by all.
• To enable all flags, enter the command as trapflags all.
Routing Commands 744
