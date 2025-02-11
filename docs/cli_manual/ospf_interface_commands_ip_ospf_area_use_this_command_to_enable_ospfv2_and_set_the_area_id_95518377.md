# ospf_interface_commands_ip_ospf_area_use_this_command_to_enable_ospfv2_and_set_the_area_id_95518377

Pages: 745-751

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default disabled
Format trapflags {all | errors {all | authentication-failure | bad-packet |
config-error | virt-authentication-failure | virt-bad-packet |
virt-config-error} | lsa {all | lsa-maxage | lsa-originate} | overflow {all |
lsdb-overflow | lsdb-approaching-overflow} | retransmit {all | packets |
virt-packets} | state-change {all | if-state-change | neighbor-state-change |
virtif-state-change | virtneighbor-state-change}}
Mode Router OSPF Config
no trapflags
Use this command to revert to the default reference bandwidth.
• To disable the individual flag, enter no trapflags and the trapflag group name
followed by the individual flag.
• To disable all the flags in that group, enter no trapflags and the trapflag group
name followed by all.
• To disable all flags, enter the command as no trapflags all.
Format no trapflags {all | errors {all | authentication-failure | bad-packet |
config-error | virt-authentication-failure | virt-bad-packet |
virt-config-error} | lsa {all | lsa-maxage | lsa-originate} | overflow {all |
lsdb-overflow | lsdb-approaching-overflow} | retransmit {all | packets |
virt-packets} | state-change {all | if-state-change | neighbor-state-change |
virtif-state-change | virtneighbor-state-change}}
Mode Router OSPF Config
OSPF Interface Commands
ip ospf area
Use this command to enable OSPFv2 and set the area ID of an interface or range of
interfaces. The area-id is an IP address formatted as a 4-digit dotted-decimal number or a
decimal value in the range of 0–4294967295. This command supersedes the effects of the
network area command. It can also be used to configure the advertiseability of the
secondary addresses on this interface into the OSPFv2 domain.
Default disabled
Format ip ospf area area-id [secondaries none]
Mode Interface Config
Routing Commands 745

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip ospf area
Use this command to disable OSPF on an interface.
Format no ip ospf area [secondaries none]
Mode Interface Config
bandwidth
By default, OSPF computes the link cost of an interface as the ratio of the reference
bandwidth to the interface bandwidth. Reference bandwidth is specified with the auto-cost
command. For the purpose of the OSPF link cost calculation, use the bandwidth command to
specify the interface bandwidth. The bandwidth is specified in kilobits per second; The kbps
argument can be in the range 1–10000000. If no bandwidth is configured, the bandwidth
defaults to the actual interface bandwidth for port-based routing interfaces and to 10 Mbps for
VLAN routing interfaces. This command does not affect the actual speed of an interface. You
can use this command to configure a single interface or a range of interfaces.
Default actual interface bandwidth
Format bandwidth kbps
Mode Interface Config
no bandwidth
Use this command to set the interface bandwidth to its default value.
Format no bandwidth
Mode Interface Config
ip ospf authentication
This command sets the OSPF authentication type and key for the specified interface or range
of interfaces. The type of authentication can be either none, simple, or encrypt. If you
select simple or encrypt, the key parameter is composed of standard displayable,
noncontrol keystrokes from a standard 101/102-key keyboard. The authentication key must
be 8 bytes or less if the authentication type is simple. If the type is encrypt, the key can
be up to 16 bytes. Unauthenticated interfaces do not need an authentication key. If the type is
encrypt, a keyid in the range of 0 and 255 must be specified. The default value for
authentication type is none. Neither the default password key nor the default key id are
configured.
Format ip ospf authentication {none | simple key | encrypt key keyid}
Mode Interface Config
Routing Commands 746

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip ospf authentication
This command resets the default OSPF authentication type for the interface.
Format no ip ospf authentication
Mode Interface Config
ip ospf cost
This command configures the cost on an OSPF interface or range of interfaces. The cost
parameter has a range of 1 to 65535.
Default 10
Format ip ospf cost cost
Mode Interface Config
no ip ospf cost
This command configures the default cost on an OSPF interface.
Format no ip ospf cost
Mode Interface Config
ip ospf database-filter all out
This command disables OSPFv2 LSA flooding on an interface. Use this command in
Interface Configuration mode.
Default Disabled
Format ip ospf database-filter all out
Mode Interface Configuration
no ip ospf database-filter all out
This command enables OSPFv2 LSA flooding on an interface. Use this command in
Interface Configuration mode.
Default Disabled
Format no ip ospf database-filter all out
Mode Interface Configuration
Routing Commands 747

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip ospf dead-interval
This command sets the OSPF dead interval for the specified interface or range of interfaces.
The value for seconds is a valid positive integer in the range 1–65535 and represents the
period in seconds that a router's Hello packets are allowed to go undetected before its
neighbor routers declare that the router is down. The value for the length of time must be the
same for all routers attached to a common network. This value should be some multiple of
the Hello Interval (for example, 4).
Default 40
Format ip ospf dead-interval seconds
Mode Interface Config
no ip ospf dead-interval
This command sets the default OSPF dead interval for the specified interface.
Format no ip ospf dead-interval
Mode Interface Config
ip ospf hello-interval
This command sets the OSPF hello interval for the specified interface or range of interfaces.
The value for seconds is a valid positive integer, which represents the length of time in
seconds. The value for the period must be the same for all routers attached to a network.
Valid values for seconds are in the range from 1 to 65535.
Default 10
Format ip ospf hello-interval seconds
Mode Interface Config
no ip ospf hello-interval
This command sets the default OSPF hello interval for the specified interface.
Format no ip ospf hello-interval
Mode Interface Config
ip ospf network
Use this command to configure OSPF to treat an interface or range of interfaces as a
point-to-point rather than broadcast interface. The broadcast option sets the OSPF network
type to broadcast. The point-to-point option sets the OSPF network type to
point-to-point. OSPF treats interfaces as broadcast interfaces by default. (Loopback
Routing Commands 748

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
interfaces have a special loopback network type, which cannot be changed.) When there are
only two routers on the network, OSPF can operate more efficiently by treating the network
as a point-to-point network. For point-to-point networks, OSPF does not elect a designated
router or generate a network link state advertisement (LSA). Both endpoints of the link must
be configured to operate in point-to-point mode.
Default broadcast
Format ip ospf network {broadcast | point-to-point}
Mode Interface Config
no ip ospf network
Use this command to return the OSPF network type to the default.
Format no ip ospf network
Mode Interface Config
ip ospf prefix-suppression
This command suppresses the advertisement of the IPv4 prefixes that are associated with an
interface, except for those associated with secondary IPv4 addresses. This command takes
precedence over the global configuration. If this configuration is not specified, the global
prefix-suppression configuration applies.
prefix-suppression can be disabled at the interface level by using the disable option. The
disable option is useful for excluding specific interfaces from performing prefix-suppression
when the feature is enabled globally.
Note that the disable option disable is not equivalent to not configuring the interface specific
prefix-suppression. If prefix-suppression is not configured at the interface level, the global
prefix-suppression configuration is applicable for the IPv4 prefixes associated with the
interface.
Default Prefix-suppression is not configured.
Format ip ospf prefix-suppression [disable]
Mode Interface Config
no ip ospf prefix-suppression
This command removes prefix-suppression configurations at the interface level. When you
enter the no ip ospf prefix-suppression command, global prefix-suppression
applies to the interface. Not configuring the command is not equal to disabling interface level
prefix-suppression.
Routing Commands 749

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format no ip ospf prefix-suppression
Mode Interface Config
ip ospf priority
This command sets the OSPF priority for the specified router interface or range of interfaces.
The priority argument for the interface is a priority integer from 1 to 255, in which 1 is the
lowest priority and 255 is the highest priority. A value of 0 indicates that the router is not
eligible to become the designated router on this network.
Default 1
Format ip ospf priority priority
Mode Interface Config
no ip ospf priority
This command sets the default OSPF priority for the specified router interface.
Format no ip ospf priority
Mode Interface Config
ip ospf retransmit-interval
This command sets the OSPF retransmit Interval for the specified interface or range of
interfaces. The retransmit interval is specified in seconds. The value for seconds is the
number of seconds between link-state advertisement retransmissions for adjacencies
belonging to this router interface. This value is also used when retransmitting database
description and link-state request packets. The value for second ranges from 0 to 3600
(1 hour).
Default 5
Format ip ospf retransmit-interval second
Mode Interface Config
no ip ospf retransmit-interval
This command sets the default OSPF retransmit Interval for the specified interface.
Format no ip ospf retransmit-interval
Mode Interface Config
Routing Commands 750

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip ospf transmit-delay
This command sets the OSPF Transit Delay for the specified interface or range of interfaces.
The transmit delay is specified in seconds. In addition, it sets the estimated number of
seconds it takes to transmit a link state update packet over this interface. The value for
second ranges from 0 to 3600 (1 hour).
Default 1
Format ip ospf transmit-delay second
Mode Interface Config
no ip ospf transmit-delay
This command sets the default OSPF Transit Delay for the specified interface.
Format no ip ospf transmit-delay
Mode Interface Config
ip ospf mtu-ignore
This command disables OSPF maximum transmission unit (MTU) mismatch detection on an
interface or range of interfaces. OSPF Database Description packets specify the size of the
largest IP packet that can be sent without fragmentation on the interface. When a router
receives a Database Description packet, it examines the MTU advertised by the neighbor. By
default, if the MTU is larger than the router can accept, the Database Description packet is
rejected and the OSPF adjacency is not established.
Default enabled
Format ip ospf mtu-ignore
Mode Interface Config
no ip ospf mtu-ignore
This command enables the OSPF MTU mismatch detection.
Format no ip ospf mtu-ignore
Mode Interface Config
Routing Commands 751
