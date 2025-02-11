# LSA

Pages: 777-892

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Area ID A 32-bit identifier for the created stub area.
Type of Service The type of service associated with the stub metric. NETGEAR supports only Normal TOS.
Metric Val The metric value is applied based on the TOS. It defaults to the least metric of the type of service
among the interfaces to other areas. The OSPF cost for a route is a function of the metric value.
Import Summary Controls the import of summary LSAs into stub areas.
LSA
show ip ospf traffic
This command displays OSPFv2 packet and LSA statistics and OSPFv2 message queue
statistics. Packet statistics count packets and LSAs since OSPFv2 counters were last
cleared (using the command clear ip ospf counters on page736).
Note: The clear ip ospf counters command does not clear the message
queue high water marks.
Format show ip ospf traffic
Modes Privileged EXEC
Parameter Description
OSPFv2 Packet The number of packets of each type sent and received since OSPF counters were last cleared.
Statistics
LSAs The number of LSAs retransmitted by this router since OSPF counters were last cleared.
Retransmitted
LS Update Max The maximum rate of LS Update packets received during any 5-second interval since OSPF
Receive Rate counters were last cleared. The rate is in packets per second.
LS Update Max The maximum rate of LS Update packets transmitted during any 5-second interval since OSPF
Send Rate counters were last cleared. The rate is in packets per second.
Number of LSAs The number of LSAs of each type received since OSPF counters were last cleared.
Received
OSPFv2 Queue For each OSPFv2 message queue, the current count, the high water mark, the number of packets
Statistics that failed to be enqueued, and the queue limit. The high water marks are not cleared when OSPF
counters are cleared.
Routing Commands 777

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show ip ospf traffic
Time Since Counters Cleared: 4000 seconds
OSPFv2 Packet Statistics
Hello Database Desc LS Request LS Update LS ACK Total
Recd: 500 10 20 50 20 600
Sent: 400 8 16 40 16 480
LSAs Retransmitted................0
LS Update Max Receive Rate........20 pps
LS Update Max Send Rate...........10 pps
Number of LSAs Received
T1 (NETGEAR Switch)...............10
T2 (Network)......................0
T3 (Net Summary)..................300
T4 (ASBR Summary).................15
T5 (External).....................20
T7 (NSSA External)................0
T9 (Link Opaque)..................0
T10 (Area Opaque).................0
T11 (AS Opaque)...................0
Total.............................345
OSPFv2 Queue Statistics
Current Max Drops Limit
Hello 0 10 0 500
ACK 2 12 0 1680
Data 24 47 0 500
Event 1 8 0 1000
show ip ospf virtual-link
This command displays the OSPF Virtual Interface information for a specific area and
neighbor. The area-id parameter identifies the area and the neighbor parameter
identifies the neighbor's Router ID.
Format show ip ospf virtual-link area-id neighbor
Modes Privileged EXEC
User EXEC
Routing Commands 778

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Area ID The area id of the requested OSPF area.
Neighbor Router ID The input neighbor Router ID.
Hello Interval The configured hello interval for the OSPF virtual interface.
Dead Interval The configured dead interval for the OSPF virtual interface.
Interface Transmit The configured transmit delay for the OSPF virtual interface.
Delay
Retransmit Interval The configured retransmit interval for the OSPF virtual interface.
Authentication The configured authentication type of the OSPF virtual interface.
Type
State The OSPF Interface States are: down, loopback, waiting, point-to-point, designated router, and
backup designated router. This is the state of the OSPF interface.
Neighbor State The neighbor state.
show ip ospf virtual-link brief
This command displays the OSPF Virtual Interface information for all areas in the system.
Format show ip ospf virtual-link brief
Modes Privileged EXEC
User EXEC
Term Definition
Area ID The area id of the requested OSPF area.
Neighbor The neighbor interface of the OSPF virtual interface.
Hello Interval The configured hello interval for the OSPF virtual interface.
Dead Interval The configured dead interval for the OSPF virtual interface.
Retransmit Interval The configured retransmit interval for the OSPF virtual interface.
Transmit Delay The configured transmit delay for the OSPF virtual interface.
Routing Commands 779

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Routing Information Protocol Commands
This section describes the commands you use to view and configure Routing Information
Protocol (RIP), which is a distance-vector routing protocol that you use to route traffic within a
small network.
router rip
Use this command to enter Router RIP mode.
Format router rip
Mode Global Config
enable (RIP)
This command resets the default administrative mode of RIP in the router (active).
Default enabled
Format enable
Mode Router RIP Config
no enable (RIP)
This command sets the administrative mode of RIP in the router to inactive.
Format no enable
Mode Router RIP Config
ip rip
This command enables RIP on a router interface or range of interfaces.
Default disabled
Format ip rip
Mode Interface Config
no ip rip
This command disables RIP on a router interface.
Format no ip rip
Mode Interface Config
Routing Commands 780

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
auto-summary
This command enables the RIP auto-summarization mode.
Default disabled
Format auto-summary
Mode Router RIP Config
no auto-summary
This command disables the RIP auto-summarization mode.
Format no auto-summary
Mode Router RIP Config
default-information originate (RIP)
This command is used to control the advertisement of default routes.
Format default-information originate
Mode Router RIP Config
no default-information originate (RIP)
This command is used to control the advertisement of default routes.
Format no default-information originate
Mode Router RIP Config
default-metric (RIP)
This command is used to set a default for the metric of distributed routes. The value for the
metric argument can be from 0–15.
Format default-metric metric
Mode Router RIP Config
no default-metric (RIP)
This command is used to reset the default metric of distributed routes to its default value.
Format no default-metric
Mode Router RIP Config
Routing Commands 781

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
distance rip
This command sets the route preference value of RIP in the router. Lower route preference
values are preferred when determining the best route. A route with a preference of 255
cannot be used to forward traffic. The value for the preference argument can be from
1–255.
Default 15
Format distance rip preference
Mode Router RIP Config
no distance rip
This command sets the default route preference value of RIP in the router.
Format no distance rip
Mode Router RIP Config
distribute-list out (RIP)
This command is used to specify the access list to filter routes received from the source
protocol. The value for the access-list argument can be from 1–199.
Default 0
Format distribute-list access-list out {ospf | static | connected}
Mode Router RIP Config
no distribute-list out
This command is used to specify the access list to filter routes received from the source
protocol. The value for the access-list argument can be from 1–199.
Format no distribute-list access list out {ospf | static | connected}
Mode Router RIP Config
ip rip authentication
This command sets the RIP version 2 authentication type and key for the interface or range
of interfaces. The type of authentication can be either none, simple, or encrypt. If you
select simple or encrypt, the key parameter is composed of standard displayable,
noncontrol keystrokes from a standard 101/102-key keyboard. The authentication key must
be 8 bytes or less if the authentication type is simple. If the type is encrypt, the key can
be up to 16 bytes. Unauthenticated interfaces do not need an authentication key. If the type is
encrypt, a keyid in the range of 0 and 255 must be specified. The default value for the
Routing Commands 782

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
authentication type is none. Neither the default password key nor the default key id are
configured.
Default none
Format ip rip authentication {none | {simple key} | {encrypt key keyid}}
Mode Interface Config
no ip rip authentication
This command sets the default RIP Version 2 Authentication Type for an interface.
Format no ip rip authentication
Mode Interface Config
ip rip receive version
This command configures an interface or range of interfaces to allow RIP control packets of
the specified version or versions to be received.
The options are: rip1 to receive only RIP version 1 formatted packets; rip2 for RIP
version 2; both to receive packets from either format; or none to not allow any RIP control
packets to be received.
Default both
Format ip rip receive version {rip1 | rip2 | both | none}
Mode Interface Config
no ip rip receive version
This command configures the interface to allow RIP control packets of the default version(s)
to be received.
Format no ip rip receive version
Mode Interface Config
ip rip send version
This command configures an interface or range of interfaces to allow RIP control packets of
the specified version to be sent.
The options are: rip1 to send only RIP version-1 formatted packets; rip2 for RIP version 2;
rip-1c to send RIP version-2 formatted packets through a broadcast; or none to not allow
any RIP control packets to be sent.
Routing Commands 783

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default rip2
Format ip rip send version {rip1 | rip1c | rip2 | none}
Mode Interface Config
no ip rip send version
This command configures the interface to allow RIP control packets of the default version to
be sent.
Format no ip rip send version
Mode Interface Config
hostroutesaccept
This command enables the RIP hostroutesaccept mode.
Default enabled
Format hostroutesaccept
Mode Router RIP Config
no hostroutesaccept
This command disables the RIP hostroutesaccept mode.
Format no hostroutesaccept
Mode Router RIP Config
split-horizon
This command sets the RIP split horizon mode. Split horizon is a technique for avoiding
problems caused by including routes in updates sent to the router from which the route was
originally learned. The options are: none, no special processing; simple, a route is not
included in updates sent to the router from which it was learned; poison, a route is included
in updates sent to the router from which it was learned, but the metric is set to infinity.
Default simple
Format split-horizon {none | simple | poison}
Mode Router RIP Config
Routing Commands 784

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no split-horizon
This command sets the default RIP split horizon mode.
Format no split-horizon
Mode Router RIP Config
redistribute (RIP)
This command configures RIP protocol to redistribute routes from the specified source
protocol or routers. Five possible match options exist. When you submit the command
redistribute ospf match, the match option or options that you specify are added to
any match types presently being redistributed. Internal routes are redistributed by default.
The metric argument can have a value in the range from 0–15.
Default metric—not-configured
match—internal
Format for OSPF as redistribute ospf [metric metric] [match [[internal] [external 1]
source protocol [ external 2] [nssa-external 1] [nssa-external 2]]
Format for other redistribute {static | connected} [metric metric]
source protocols
Mode Router RIP Config
no redistribute
This command deconfigures RIP protocol to redistribute routes from the specified source
protocol or routers.
Format no redistribute {ospf | static | connected} [metric] [match [[internal]
[external 1] [external 2] [nssa-external 1] [nssa-external 2]]
Mode Router RIP Config
show ip rip
This command displays information relevant to the RIP router.
Format show ip rip
Modes Privileged EXEC
User EXEC
Term Definition
RIP Admin Mode Enable or disable.
Split Horizon Mode None, simple or poison reverse.
Routing Commands 785

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Auto Summary Mode Enable or disable. If enabled, groups of adjacent routes are summarized into single entries,
in order to reduce the total number of entries The default is enable.
Host Routes Accept Mode Enable or disable. If enabled the router accepts host routes. The default is enable.
Global Route Changes The number of route changes made to the IP Route Database by RIP. This does not
include the refresh of a route's age.
Global queries The number of responses sent to RIP queries from other systems.
Default Metric The default metric of redistributed routes if one has already been set, or blank if not
configured earlier. The valid values are 1 to 15.
Default Route Advertise The default route.
show ip rip interface brief
This command displays general information for each RIP interface. For this command to
display successful results, routing must be enabled per interface (for example, through the
ip rip command).
Format show ip rip interface brief
Modes Privileged EXEC
User EXEC
Term Definition
Interface unit/slot/port
IP Address The IP source address used by the specified RIP interface.
Send Version The RIP version(s) used when sending updates on the specified interface. The types are none,
RIP-1, RIP-1c, RIP-2
Receive Version The RIP version(s) allowed when receiving updates from the specified interface. The types are
none, RIP-1, RIP-2, Both
RIP Mode The administrative mode of router RIP operation (enabled or disabled).
Link State The mode of the interface (up or down).
show ip rip interface
This command displays information related to a particular RIP interface.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vlan-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in a unit/slot/port format. The vlan-id can
be a number from 1–4093.
Routing Commands 786

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format show ip rip interface {unit/slot/port | vlan vlan-id}
Modes Privileged EXEC
User EXEC
Term Definition
Interface unit/slot/port This is a configured value.
IP Address The IP source address used by the specified RIP interface. This is a configured value.
Send Version The RIP version(s) used when sending updates on the specified interface. The types are none,
RIP-1, RIP-1c, RIP-2. This is a configured value.
Receive Version The RIP version(s) allowed when receiving updates from the specified interface. The types are
none, RIP-1, RIP-2, Both. This is a configured value.
RIP Admin Mode RIP administrative mode of router RIP operation; enable activates, disable de-activates it. This is a
configured value.
Link State Indicates whether the RIP interface is up or down. This is a configured value.
Authentication The RIP Authentication Type for the specified interface. The types are none, simple, and encrypt.
Type This is a configured value.
The following information will be invalid if the link state is down.
Term Definition
Bad Packets The number of RIP response packets received by the RIP process which were subsequently
Received discarded for any reason.
Bad Routes The number of routes contained in valid RIP packets that were ignored for any reason.
Received
Updates Sent The number of triggered RIP updates actually sent on this interface.
Routing Commands 787

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ICMP Throttling Commands
This section describes the commands you use to configure options for the transmission of
various types of ICMP messages.
ip unreachables
Use this command to enable the generation of ICMP Destination Unreachable messages on
an interface or range of interfaces. By default, the generation of ICMP Destination
Unreachable messages is enabled.
Default enable
Format ip unreachables
Mode Interface Config
no ip unreachables
Use this command to prevent the generation of ICMP Destination Unreachable messages.
Format no ip unreachables
Mode Interface Config
ip redirects
Use this command to enable the generation of ICMP Redirect messages by the router. By
default, the generation of ICMP Redirect messages is enabled. You can use this command to
configure an interface, a range of interfaces, or all interfaces.
Default enable
Format ip redirects
Mode Global Config
Interface Config
no ip redirects
Use this command to prevent the generation of ICMP Redirect messages by the router.
Format no ip redirects
Mode Global Config
Interface Config
Routing Commands 788

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ipv6 redirects
Use this command to enable the generation of ICMPv6 Redirect messages by the router. By
default, the generation of ICMP Redirect messages is enabled. You can use this command to
configure an interface, a range of interfaces, or all interfaces.
Default enable
Format ipv6 redirects
Mode Interface Config
no ipv6 redirects
Use this command to prevent the generation of ICMPv6 Redirect messages by the router.
Format no ipv6 redirects
Mode Interface Config
ip icmp echo-reply
Use this command to enable the generation of ICMP Echo Reply messages by the router. By
default, the generation of ICMP Echo Reply messages is enabled.
Default enable
Format ip icmp echo-reply
Mode Global Config
no ip icmp echo-reply
Use this command to prevent the generation of ICMP Echo Reply messages by the router.
Format no ip icmp echo-reply
Mode Global Config
ip icmp error-interval
Use this command to limit the rate at which IPv4 ICMP error messages are sent. The rate
limit is configured as a token bucket, with two configurable parameters, burst-size and
burst-interval.
The burst-interval specifies how often the token bucket is initialized with burst-size
tokens. burst-interval is from 0 to 2147483647 milliseconds (msec). The burst-size is the
number of ICMP error messages that can be sent during one burst-interval. The range is
from 1 to 200 messages. To disable ICMP rate limiting, set the burst-interval to zero (0).
Routing Commands 789

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default burst-interval of 1000 msec.
burst-size of 100 messages
Format ip icmp error-interval burst-interval [burst-size]
Mode Global Config
no ip icmp error-interval
Use the no ip icmp error-interval command to return the burst-interval and
burst-size to their default values.
Format no ip icmp error-interval
Mode Global Config
Routing Commands 790

Captive Portal Commands

This section describes the CLI commands that you can use to manage the captive portal
features on the switch. The chapter contains the following sections:
• Captive Portal Global Commands
• Captive Portal Configuration Commands
• Captive Portal Status Commands
• Captive Portal Client Connection Commands
• Captive Portal Interface Commands
• Captive Portal Local User Commands
• Captive Portal User Group Commands

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Captive Portal Global Commands
The commands in this section enable you to configure the captive portal settings that affect
the captive portal feature on the switch and all captive portal instances.
captive-portal
Use this command to enter the Captive Portal Configuration Mode.
Format captive-portal
Mode Global Config
enable (Captive Portal Config Mode)
This command globally enables the captive portal feature on the switch.
Default Disable
Format enable
Mode Captive Portal Config
no enable (Captive Portal Config Mode)
The no enable command disables the captive portal functionality.
Format no enable
Mode Captive Portal Config
http port
This command configures an additional HTTP port. Valid port numbers are in the range of
0-65535, excluding port numbers 80 and 443 which are reserved. The HTTP port default is 0
which denotes no additional port and the default port (80) is used.
Default 0
Format http port port-number
Mode Captive Portal Config
Command example:
(NETGEAR Switch) (Config-CP) #http port 8080
(NETGEAR Switch) (Config-CP) #no http port
Captive Portal Commands 792

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no http port
This command removes the specified additional HTTP port.
Format no http port port-number
Mode Captive Portal Config
https port
This command configures an additional HTTPS secure port. The HTTPS secure port default
is 0 which denotes no additional port and the default port (443) is used. Port number 80 is
reserved.
Default 0
Format https port port-number
Mode Captive Portal Config
Parameter Description
port-num Port number in the range of 0-65535.
Command example:
(NETGEAR Switch) (Config-CP) #https port 60000
(NETGEAR Switch) (Config-CP) #no https port
no https port
This command set the HTTPS secure port to the default.
Format no https port port-number
Mode Captive Portal Config
snmp-server enable traps captive-portal
This command globally enables the captive portal traps. The specific captive portal traps are
configured using the trapflags command in Captive Portal Config Mode.
Default Disable
Format snmp-server enable traps captive-portal
Mode Global Config
Captive Portal Commands 793

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no snmp-server enable traps captive-portal
This command globally disables all the captive portal traps.
Format no snmp-server enable traps captive-portal
Mode Global Config
trapflags (Captive Portal Config Mode)
This command enables captive portal SNMP traps. If no parameters are specified, then all
traps are enabled. SNMP traps can also be enabled individually by supplying the optional
parameters.
The client-auth-failure option allows the SNMP agent to send a trap when a client
attempts to authenticate with a captive portal but is unsuccessful.
The client-connect option allows the SNMP agent to send a trap when a client
authenticates with and connects to a captive portal.
The client-db-full option allows the SNMP agent to send a trap each time an entry
cannot be added to the client database because it is full.
The client-disconnect option allows the SNMP agent to send a trap when a client
disconnects from a captive portal.
Default Disabled
Format trapflags [client-auth-failure | client-connect | client-db-full |
client-disconnect]
Mode Captive Portal Config
no trapflags
This command disables all captive portal SNMP traps when no parameters are specified. The
optional parameters specify individual traps to disable.
Format no trapflags [client-auth-failure | client-connect | client-db-full |
client-disconnect]
Mode Captive Portal Config
authentication timeout
This command configures the authentication time-out. If the captive portal user does not
enter valid credentials within this time limit, the authentication page needs to be served again
in order for the client to gain access to the network. The seconds variable is the
authentication time-out and is a number in the range of 60-600 seconds.
Captive Portal Commands 794

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default 300
Format authentication timeout seconds
Mode Captive Portal Config
no authentication timeout
This command sets the authentication timeout to the default value.
Format no authentication timeout
Mode Captive Portal Config
show captive-portal
This command reports status of the captive portal feature.
Format show captive-portal
Mode Privileged EXEC
Term Description
Administrative Shows whether the CP is enabled.
Mode
Operational Status Indicates whether the CP operational status is enabled or disabled.
Disable Reason If CP is disabled, this field displays the reason, which can be None, Administratively
Disabled, No IPv4 Address, or Routing Enabled, but no IPv4 routing interface.
Captive Portal IP Shows the IP address that the captive portal feature uses.
Address
show captive-portal status
This command reports status of all captive portal instances in the system.
Format show captive-portal status
Mode Privileged EXEC
Term Description
Additional HTTP Displays the port number of the additional HTTP port configured for traffic. A value of 0 indicates that
Port only port 80 is configured for HTTP traffic.
Additional HTTP Displays the port number of the additional HTTPS secure port. A value of 0 indicates no additional
Secure Port port and the default port (443) is used.
Captive Portal Commands 795

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Description
Peer Switch Displays the interval at which statistics are reported in the Cluster Controller. The reporting interval is
Statistics Reporting in the range of 0, 15-3600 seconds where 0 disables statistical reporting.
Interval
Authentication Displays the number of seconds to keep the authentication session open with the client. When the
Timeout timeout expires, the switch disconnects any active TCP or SSL connection with the client.
Supported Captive Shows the number of supported captive portals in the system.
Portals
Configured Captive Shows the number of captive portals configured on the switch.
Portals
Active Captive Shows the number of captive portal instances that are operationally enabled.
Portals
Local Supported Shows the number of users that can be added and configured using the local user database.
Users
Configured Local Shows the number of users that are configured from the local user database.
Users
System Supported Shows the total number of authenticated users that the system can support.
Users
Authenticated Shows the number of users currently authenticated to all captive portal instances on this switch.
Users
Command example:
(NETGEAR Switch) #show captive-portal status
Additional HTTP Port........................... 0
Additional HTTP Secure Port.................... 0
Peer Switch Statistics Reporting Interval...... 120
Authentication Timeout......................... 300
Supported Captive Portals...................... 10
Configured Captive Portals..................... 1
Active Captive Portals......................... 0
Local Supported Users.......................... 128
Configured Local Users......................... 0
System Supported Users......................... 1024
Authenticated Users............................ 0
Captive Portal Commands 796

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show captive-portal trapflags
This command shows which captive portal SNMP traps are enabled. The show trapflags
command shows the global captive portal traps configuration. For more information, see the
sample output of show trapflags on page141.
Format show captive-portal trapflags
Mode Privileged EXEC
Term Description
Client Shows whether the SNMP agent sends a trap when a client attempts to authenticate with a captive
Authentication portal but is unsuccessful.
Failure Traps
Client Connection Shows whether the SNMP agent sends a trap when a client authenticates with and connects to a
Traps captive portal.
Client Database Shows whether the SNMP agent sends a trap each time an entry cannot be added to the client
Full Traps database because it is full.
Client Shows whether the SNMP agent sends a trap when a client disconnects from a captive portal.
Disconnection
Traps
Captive Portal Configuration Commands
The commands in this section are related to captive portal configurations.
configuration (for captive portal)
Use this command to enter the Captive Portal Instance Mode.
The captive portal configuration, identified by CP ID 1, is the default CP configuration. You
can create up to nine additional captive portal configurations. The system supports a total of
ten CP configurations. The Captive Portal ID cp-id variable is a number in the range of
1-10.
Format configuration cp-id
Mode Captive Portal Config
Captive Portal Commands 797

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no configuration
This command deletes a captive portal configuration. The command fails if interfaces are
associated to this configuration. The default captive portal configuration cannot be deleted.
The Captive Portal ID cp-id variable is a number in the range of 1-10.
Format no configuration cp-id
Mode Captive Portal Config
enable (Captive Portal Instance)
This command enables a captive portal configuration.
Default Enable
Format enable
Mode Captive Portal Instance
no enable
This command disables a captive portal configuration.
Format no enable
Mode Captive Portal Instance
name
This command configures the name for a captive portal configuration. The cp-name can
contain up to 32 alphanumeric characters.
Format name cp-name
Mode Captive Portal Instance
protocol
This command configures the protocol mode for a captive portal configuration. The CP can
use HTTP or HTTPS protocols.
Default https
Format protocol {http | https}
Mode Captive Portal Instance
Captive Portal Commands 798

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
verification
This command configures the verification mode for a captive portal configuration. The type of
user verification to perform can be one of the following:
• guest. The user does not need to be authenticated by a database.
• local. The switch uses a local database to authenticated users.
• radius. The switch uses a database on a remote RADIUS server to authenticate users.
Default guest
Format verification {guest | local | radius}
Mode Captive Portal Instance
group
This command assigns a group ID to a captive portal configuration. Each Captive Portal
configuration must contain at least one group ID. The group-id can have a number in the
1–1024 range. Group ID 1 is the default.
Default group-ID 1
Format group group-id
Mode Captive Portal Instance
radius-auth-server
Use this command to configure a captive portal configuration RADIUS authentication server.
Default Disable
Format radius-auth-server server-name
Mode Captive Portal Instance
no radius-auth-server
This command disables a captive portal configuration RADIUS authentication server.
Format no radius-auth-server
Mode Captive Portal Instance
Captive Portal Commands 799

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
redirect
This command enables the redirect mode for a captive portal configuration.
Default Disable
Format redirect
Mode Captive Portal Instance
no redirect
This command disables the redirect mode for a captive portal configuration.
Format no redirect
Mode Captive Portal Instance
redirect-url
Use this command to specify the URL to which the newly authenticated client is redirected if
the URL Redirect Mode is enabled. This command is only available if the redirect mode is
enabled.
Format redirect-url url
Mode Captive Portal Instance
max-bandwidth-up
This command configures the maximum rate at which a client can send data into the network.
Default 0
Format max-bandwidth-up rate
Mode Captive Portal Config
Parameter Description
rate Rate in bps. 0 indicates limit not enforced.
no max-bandwidth-up
This command sets the maximum rate at which a client can send data into the network to the
default.
Format no max-bandwidth-up
Mode Captive Portal Instance
Captive Portal Commands 800

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
max-bandwidth-down
This command configures the maximum rate at which a client can receive data from the
network.
Default 0
Format max-bandwidth-down rate
Mode Captive Portal Instance
Parameter Description
rate Rate in bps. 0 indicates limit not enforced.
no max-bandwidth-down
This command sets to the default the maximum rate at which a client can receive data from
the network.
Format no max-bandwidth-down
Mode Captive Portal Instance
max-input-octets
This command configures the maximum number of octets the user is allowed to transmit.
After this limit has been reached the user will be disconnected. If the value is set to 0 then the
limit is not enforced.
Default 0
Format max-input-octets bytes
Mode Captive Portal Instance
Parameter Description
bytes Input octets in bytes. 0 indicates limit not enforced.
no max-input-octets
This command sets to the default the maximum number of octets the user is allowed to
transmit.
Format no max-input-octets
Mode Captive Portal Instance
Captive Portal Commands 801

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
max-output-octets
This command configures the maximum number of octets the user is allowed to receive. After
this limit has been reached the user will be disconnected. If the value is set to 0 then the limit
is not enforced.
Default 0
Format max-output-octets bytes
Mode Captive Portal Instance
Parameter Description
bytes Output octets in bytes. 0 indicates limit not enforced.
no max-output-octets
This command sets to the default the maximum number of octets the user is allowed to
receive.
Format no max-output-octets
Mode Captive Portal Instance
max-total-octets
This command configures the maximum number of octets the user is allowed to transfer, i.e.,
the sum of octets transmitted and received. After this limit has been reached the user will be
disconnected. If the value is set to 0, then the limit is not enforced.
Default 0
Format max-total-octets bytes
Mode Captive Portal Instance
Parameter Description
bytes Total octets in bytes. 0 indicates limit not enforced.
no max-total-octets
This command sets to the default the maximum number of octets the user is allowed to
transfer, that is, the sum of octets transmitted and received.
Format no max-total-octets
Mode Captive Portal Instance
Captive Portal Commands 802

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
session-timeout (Captive Portal Instance)
This command configures the session time-out for a captive portal configuration. The
timeout variable is a number that represents the session time-out in seconds. Use 0 to
indicate that the time-out is not enforced.
Default 0
Format session-timeout timeout
Mode Captive Portal Instance
no session-timeout
Use this command to set the session time-out for a captive portal configuration to the default
value.
Format no session-timeout
Mode Captive Portal Instance
idle-timeout
This command configures the idle time-out for a captive portal configuration. The timeout
variable is a number that represents the idle time-out in seconds. Use 0 to indicate that the
time-out is not enforced.
Default 0
Format idle-timeout timeout
Mode Captive Portal Instance
no idle-timeout
Use this command to set the idle time-out for a captive portal configuration to the default
value.
Format no idle-timeout
Mode Captive Portal Instance
locale
This command is not intended to be a user command. The administrator must use the WEB
user interface to create and customize captive portal web content. The command is primarily
used by the show running config command and process as it provides the ability to
save and restore configurations using a text-based format.
Captive Portal Commands 803

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format locale web-id
Mode Captive Portal Instance
do (Captive Portal Instance mode)
Use this command to run Privileged Exec mode commands.
Format do
Mode Captive Portal Instance
script-text
Use this command to specify, in UTF-16 byte stream format, the text that is displayed if
javascript is disabled in the users browser.
Format script-text UTF-16
Mode Captive Portal Instance
show (Captive Portal Instance)
Use this command to display the switches options and settings.
Format show
Mode Captive Portal Instance
wip-msg
Use this command to specify, in UTF-16 byte stream format, the message displayed when
authentication is in progress.
Format wip-msg UTF-16
Mode Captive Portal Instance
interface (Captive Portal Instance)
This command associates an interface to a captive portal configuration or removes the
interface captive portal association.
Format interface unit/slot/port
Mode Captive Portal Instance
Captive Portal Commands 804

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no interface
This command removes the association between an interface and a captive portal
configuration.
Format no interface unit/slot/port
Mode Captive Portal Instance
block
This command blocks all traffic for a captive portal configuration.
Format block
Mode Captive Portal Instance
no block
This command unblocks all traffic for a captive portal configuration.
Format no block
Mode Captive Portal Instance
clear (Captive Portal Instance Config)
This command sets the configuration for this instance to the default values.
Format clear
Mode Captive Portal Instance
user-logout
This command enables the ability for an authenticated user to de-authenticate from the
network. This command is configurable for a captive portal configuration.
Format user-logout
Mode Captive Portal Instance
no user-logout
This command removes the association between an interface and a captive portal
configuration.
Format no user-logout
Mode Captive Portal Instance
Captive Portal Commands 805

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
background-color
Use this command to customize the background color of the Captive Portal authentication
page using a well-known color name or RGB value. For example, red or RGB hex-code, that
is, #FF0000. The range of color-code is 1-32 characters.
Default #BFBFBF
Format background-color color-code
Mode Captive Portal Instance
foreground-color
Use this command to customize the foreground color of the Captive Portal authentication
page using a well-known color name or RGB value. For example, red or RGB hex-code, that
is, #FF0000. The range of color-code is 1-32 characters.
Default #999999
Format foreground-color color-code
Mode Captive Portal Instance
separator-color
Use this command to customize the separator bar color of the Captive Portal authentication
page using a well-known color name or RGB value. For example, red or RGB hex-code; that
is, #FF0000.The range of color-code is 1-32 characters.
Default #BFBFBF
Format separator-color color-code
Mode Captive Portal Instance
Captive Portal Commands 806

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Captive Portal Status Commands
Use the commands in this section to view information about the status of one or more captive
portal instances.
show captive-portal configuration
This command displays the operational status of each captive portal configuration. The
cp-id variable is the captive portal ID, which ranges from 1-10.
Format show captive-portal configuration cp-id
Mode Privileged EXEC
Term Description
CP ID Shows the captive portal ID.
CP Name Shows the captive portal name.
Operational Status Shows whether the captive portal is enabled or disabled.
Disable Reason If the captive portal is disabled, this field indicates the reason.
Blocked Status Shows the blocked status, which is Blocked or Not Blocked.
Authenticated Shows the number of authenticated users connected to the network through this captive portal.
Users
Configured Locales Shows the number of locales defined for this captive portal.
show captive-portal configuration interface
This command displays information for all interfaces assigned to a captive portal
configuration or a specific interface assigned to a captive portal configuration. The cp-id
variable is the captive portal ID, which ranges from 1-10.
Format show captive-portal configuration cp-id interface [unit/slot/port]
Mode Privileged EXEC
Term Description
CP ID Shows the captive portal ID.
CP Name Shows the captive portal name.
Interface unit/slot/port
Interface Describes the interface.
Description
Operational Status Shows whether the captive portal is enabled or disabled
Captive Portal Commands 807

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Description
Block Status Shows the blocked status, which is Blocked or Not Blocked.
If you include the optional unit/slot/port information, the following additional information appears:
Disable Reason If the captive portal is disabled, this field indicates the reason.
Authenticated Shows the number of authenticated users connected to the network through this captive portal.
Users
show captive-portal configuration status
This command displays information of all configured captive portal configurations or a
specific captive portal configuration. The cp-id variable is the captive portal ID, which
ranges from 1-10.
Format show captive-portal configuration cp-id status
Mode Privileged EXEC
Term Description
CP ID Shows the captive portal ID.
CP Name Shows the captive portal name.
CP Mode Shows whether the CP is enabled or disabled.
Protocol Mode Shows the current connection protocol, which is either HTTP or HTTPS.
Verification Mode Shows the current account type, which is Guest, Local, or RADIUS.
URL Redirect Indicates whether the Redirect URL Mode is enabled or disabled.
Mode
Max Bandwidth Up The maximum rate in bytes per second (bps) at which a client can send data into the network.
(bytes/sec)
Max Bandwidth The maximum rate in bps at which a client can receive data from the network.
Down (bytes/sec)
Max Input Octets The maximum number of octets the user is allowed to transmit.
(bytes)
Max Output Octets The maximum number of octets the user is allowed to receive.
(bytes)
Max Total Octets The maximum number of octets the user is allowed to transfer, i.e., the sum of octets transmitted
(bytes) and received.
Session Timeout Shows the number of seconds a user is permitted to remain connected to the network. Once the
(seconds) Session Timeout value is reached, the user is logged out automatically. A value of 0 means that the
user does not have a session Timeout limit.
Idle Timeout Shows the number of seconds the user can remain idle before the switch automatically logs the user
(seconds) out. A value of 0 means that the user will not be logged out automatically.
Captive Portal Commands 808

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show captive-portal configuration locales
This command displays locales associated with a specific captive portal configuration. The
cp-id variable is the captive portal ID, which ranges from 1-10.
Format show captive-portal configuration cp-id locales
Mode Privileged EXEC
Term Description
Locale Code Two-letter abbreviation for languages.
Locale Link The names of the languages.
Captive Portal Client Connection
Commands
Use the commands in this section to view information about the clients connected to the
captive portals configured on the switch.
show captive-portal client status
This command displays client connection details or a connection summary for connected
captive portal users. Use the optional macaddr keyword, which is the MAC address of a
client, to view additional information about that client.
Format show captive-portal client [macaddr] status
Mode Privileged EXEC
Term Description
Client MAC Identifies the MAC address of the wireless client (if applicable).
Address
Client IP Address Identifies the IP address of the wireless client (if applicable).
Protocol Mode Shows the current connection protocol, which is either HTTP or HTTPS.
Verification Mode Shows the current account type, which is Guest, Local, or RADIUS.
Session Time Shows the amount of time that has passed since the client was authorized.
If you specify a client MAC address, the following additional information displays:
CP ID Shows the captive portal ID the connected client is using.
CP Name Shows the name of the captive portal the connected client is using.
Captive Portal Commands 809

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Description
Interface Valid slot and port number separated by a forward slash.
Interface Describes the interface.
Description
User Name Displays the user name (or Guest ID) of the connected client.
If cluster support is available, the following fields display:
Switch MAC Identifies the MAC address of the switch (if applicable).
Address
Switch IP Address Identifies the IP address of the switch (if applicable).
Switch Type (local Shows the current switch type, which is local or peer.
or peer)
show captive-portal client statistics
This command displays the statistics for a specific captive portal client.
Format show captive-portal client macaddr statistics
Mode Privileged EXEC
Term Description
Client MAC Identifies the MAC address of the wireless client (if applicable).
Address
Bytes Received Total bytes the client has received.
Bytes Transmitted Total bytes the client has transmitted.
Packets Total packets the client has transmitted.
Transmitted
Packets Received Total packets the client has received.
show captive-portal interface client status
This command displays information about clients authenticated on all interfaces or a specific
interface.
Format show captive-portal interface [unit/slot/port] client status
Mode Privileged EXEC
Captive Portal Commands 810

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Description
Interface Valid unit, slot and port number.
Interface Describes the interface.
Description
Client MAC Identifies the MAC address of the wireless client (if applicable).
Address
If you use the optional unit/slot/port information, the following additional information appears:
Client IP Address Identifies the IP address of the wireless client (if applicable).
CP ID Shows the captive portal ID the connected client is using.
CP Name Shows the name of the captive portal the connected client is using.
Protocol Shows the current connection protocol, which is either HTTP or HTTPS.
Verification Shows the current account type, which is Guest, Local, or RADIUS.
User Name Displays the user name (or Guest ID) of the connected client.
show captive-portal configuration client status
This command displays the clients authenticated to all captive portal configurations or a
specific configuration. The optional cp-id variable is the captive portal ID, which ranges
from 1-10.
Format show captive-portal configuration [cp-id] client status
Mode Privileged EXEC
Term Description
CP ID Shows the captive portal ID the connected client is using.
CP Name Shows the name of the captive portal the connected client is using.
Client MAC Identifies the MAC address of the wireless client (if applicable).
Address
If you use the optional cp-id information, the following additional information appears:
Client IP Address Identifies the IP address of the wireless client (if applicable).
Interface Valid slot and port number separated by a forward slash.
Interface Describes the interface.
Description
captive-portal client deauthenticate
This command deauthenticates a specific captive portal client. You can specify a captive
portal configuration ID to indicate the captive portal configuration that the client is
deauthenticating from. The optional cp-id variable is the captive portal ID, which ranges
Captive Portal Commands 811

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
from 1-10. If no value is entered, then the specified clients (or all clients) are deauthenticated
from all captive portal configurations.
You can use the optional macaddr variable to specify the MAC address of the client to
deauthenticate. If no value is specified, then all clients are deauthenticated from the specified
captive portal configuration (or all configurations).
Format captive-portal client deauthenticate [cp-id] [macaddr]
Mode Privileged EXEC
Captive Portal Interface Commands
Use the commands in this section to view information about the interfaces on the switch that
are associated with captive portals or that are capable of supporting a captive portal.
show captive-portal interface configuration status
This command displays the interface to configuration assignments for all captive portal
configurations or a specific configuration. The optional cp-id variable is the captive portal
ID, which ranges from 1-10.
Format show captive-portal interface configuration [cp-id] status
Mode Privileged EXEC
Term Description
CP ID Shows the captive portal ID the connected client is using.
CP Name Shows the name of the captive portal the connected client is using.
Interface Valid slot and port number separated by a forward slash.
Interface Describes the interface.
Description
Type Shows the type of interface.
show captive-portal interface capability
This command displays all the captive portal eligible interfaces or the interface capabilities for
a specific captive portal interface.
Format show captive-portal interface capability [unit/slot/port]
Mode Privileged EXEC
Captive Portal Commands 812

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Description
Interface Valid slot and port number separated by a forward slash.
Interface Describes the interface.
Description
Type Shows the type of interface.
If you use the optional unit/slot/port information, the following additional information appears:
Session Timeout Indicates whether or not this field is supported by the specified captive portal interface.
Idle Timeout Indicates whether or not this field is supported by the specified captive portal interface.
Bytes Received Indicates whether or not this field is supported by the specified captive portal interface.
Counter
Bytes Transmitted Indicates whether or not this field is supported by the specified captive portal interface.
Counter
Packets Received Indicates whether or not this field is supported by the specified captive portal interface.
Counter
Packets Indicates whether or not this field is supported by the specified captive portal interface.
Transmitted
Counter
Roaming Indicates whether or not this field is supported by the specified captive portal interface.
Captive Portal Local User Commands
Use these commands to view and configure captive portal users in the local database.
user (Captive Portal Config Mode)
This command is used to create a local user. The user-id variable is the user ID, which can
be a number between 1 and 128. The username variable is the name of the user and can
have up to 32 alphanumeric characters. The password variable is 8-64 characters.
Two ways exist to create a user: with the user name command or with the user password
command. If the user is created with the user name command, you must assign the
password with the user password command. If the user is created with the user
password command, you can assign the name with the user name command at a later
time.
You can also modify the password after you created a user by using the user password
command with the user ID and a new password.
Format user user-id name username
Mode Captive Portal Config
Captive Portal Commands 813

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format user user-id password password
Mode Captive Portal Config
Command example:
The following example uses name to create the user.
(NETGEAR Switch)(Config-CP) #user 1 name test
Command example:
The following example uses password to create the user:
(NETGEAR Switch)(Config-CP) #user 1 password test1234
no user
This command deletes a user from the local user database. If the user has an existing
session, it is disconnected. The user-id variable is the user ID, which can be a number
between 1 and 128.
Format no user user-id
Mode Captive Portal Config
Command example:
(NETGEAR Switch)(Config-CP) #no user 1
user name (Captive Portal Config)
This command assigns a name to the User ID. This name is used at the client station for
authentication. The user-id variable is the local user ID created with the user command
and can be from 1 to 128 characters. The username variable is the name of the user and
can have up to 32 alphanumeric characters.
Format user user-id name username
Mode Captive Portal Config
Command example:
(NETGEAR Switch)(Config-CP) #user 1 name johnsmith
user password (Captive Portal Config)
This command sets or modifies the password for the associated captive portal user. The
user-id variable is the local user ID created with the user command and can be from 1 to
Captive Portal Commands 814

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
128 characters. The password variable is the user id’s password and can have from 8 to 64
alphanumeric characters.
Format user user-id password password
Mode Captive Portal Config
Command example:
(NETGEAR Switch)(Config-CP) #user 1 password
Enter Password (8 - 64 characters):
Re-enter password:
user password encrypted
This command modifies the password for the associated captive portal user. The command
accepts the password in an encrypted format. This command is used primarily by the show
running config command process.
The user-id variable is the local user ID created with the user command. The
encrypted-pwd variable is the password in encrypted format, which can be up to 128
hexadecimal characters.
Format user user-id password encrypted encrypted-pwd
Mode Captive Portal Config
Command example:
(NETGEAR Switch)(Config-CP) #user 1 password encrypted 42 65 74 74 65 72 20 73 61 66 65
20 74 68 61 6e 20 73 6f 72 72 79
user group (captive portal local user commands)
This command assigns/modifies the group name for the associated captive portal user. The
user-id variable is the user ID, which is a number in the range of 1 to 128. The
group-name variable is a name up to 32 characters.
Format user user-id group group-name
Mode Captive Portal Config
Command example:
(NETGEAR Switch)(Config-CP) #user 1 group 123
user session-timeout
This command sets the session timeout value for the associated captive portal user. The
user-id variable is the ID of a user configured in the local database, and is a number in the
Captive Portal Commands 815

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
range of 1 to 128. The timeout variable is a number that represents the session time-out in
seconds. Use 0 to indicate that the time-out is not enforced.
Default 0
Format user user-id session-timeout timeout
Mode Captive Portal Config
Command example:
(NETGEAR Switch)(Config-CP) #user 1 session-timeout 86400
no user session-timeout
This command sets the session timeout value for the associated captive portal user to the
default value. The user-id variable is the ID of a user configured in the local database, and
is a number in the range of 1 to 128.
Format no user user-id session-timeout
Mode Captive Portal Config
Command example:
(NETGEAR Switch)(Config-CP) #no user 1 session-timeout
user idle-timeout
This command sets the session idle timeout value for the associated captive portal user. The
user-id variable is the ID of a user configured in the local database, and is a number in the
range of 1 to 128. The timeout variable is a number that represents the idle time-out in
seconds. Use 0 to indicate that the time-out is not enforced.
Default 0
Format user user-id idle-timeout timeout
Mode Captive Portal Config
Command example:
(NETGEAR Switch)(Config-CP) #user 1 idle-timeout 600
Captive Portal Commands 816

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no user idle-timeout
This command sets the session idle timeout value for the associated captive portal user to
the default value. The user-id variable is the ID of a user configured in the local database,
and is a number in the range of 1 to 128.
Format no user user-id idle-timeout
Mode Captive Portal Config
Command example:
(NETGEAR Switch)(Config-CP) #no user 1 idle-timeout
user max-bandwidth-up
This command is used to configure the bandwidth in bytes per second (bps, with the bps
variable) at which the client can send data into the network. 0 denotes using the default value
configured for the captive portal. The user-id variable is the ID of a user configured in the
local database, and is a number in the range of 1 to 128.
Default 0
Format user user-id max-bandwidth-up bps
Mode Captive Portal Config
Parameter Description
user-id User ID from 1 to 128 characters.
bps Client transmit rate in bytes per second (bps). 0 denotes unlimited bandwidth.
no user max-bandwidth-up
Use this command to set to the default the bandwidth at which the client can send data into
the network. The user-id variable is the ID of a user configured in the local database, and
is a number in the range of 1 to 128.
Format no user user-id max-bandwidth-up
Mode Captive Portal Config
user max-bandwidth-down
This command is used configure the bandwidth in bytes per second (bps, with the variable) at
which the client can receive data from the network. 0 denotes using the default value
configured for the captive portal. The user-id variable is the ID of a user configured in the
local database, and is a number in the range of 1 to 128.
Captive Portal Commands 817

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default 0
Format user user-id max-bandwidth-down bps
Mode Captive Portal Config
Parameter Description
user-id User ID from 1 to 128 characters.
bps Client receive rate in bps. 0 denotes unlimited bandwidth.
no user max-bandwidth down
Use this command to set to the default value the bandwidth at which the client can receive
data from the network. The user-id variable is the ID of a user configured in the local
database, and is a number in the range of 1 to 128.
Format no user user-id max-bandwidth-down
Mode Captive Portal Config
user max-input-octets
This command is used to limit the number of octets in bytes that the user is allowed to
transmit. After this limit has been reached, the user will be disconnected. 0 octets denote
unlimited transmission. The user-id variable is the ID of a user configured in the local
database, and is a number in the range of 1 to 128.
Default 0
Format user user-id max-input-octets octets
Mode Captive Portal Config
Parameter Description
user-id User ID from 1 to 128 characters.
octets Number of bytes.
no user max-input-octets
Use this command to set to the default the number of octets in bytes that the user is allowed
to transmit. The user-id variable is the ID of a user configured in the local database, and is
a number in the range of 1 to 128.
Format no user user-id max-input-octets
Mode Captive Portal Config
Captive Portal Commands 818

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
user max-output-octets
This command is used to limit the number of octets in bytes that the user is allowed to
receive. After this limit has been reached, the user will be disconnected. 0 octets denote
unlimited transmission. The user-id variable is the ID of a user configured in the local
database, and is a number in the range of 1 to 128.
Default 0
Format user user-id max-output-octets octets
Mode Captive Portal Config
Parameter Description
user-id User ID from 1 to 128 characters.
octets Number of bytes.
no user max-output-octets
Use this command to set to the default the number of octets in bytes that the user is allowed
to receive. The user-id variable is the ID of a user configured in the local database, and is
a number in the range of 1 to 128.
Format no user user-id max-output-octets
Mode Captive Portal Config
user max-total-octets
This command is used to limit the number of octets in bytes that the user is allowed to
transmit and receive. The maximum number of octets is the sum of octets transmitted and
received. After this limit has been reached, the user will be disconnected. 0 octets denote
unlimited transmission. The user-id variable is the ID of a user configured in the local
database, and is a number in the range of 1 to 128.
Default 0
Format user user-id max-total-octets octets
Mode Captive Portal Config
Parameter Description
user-id User ID from 1 to 128 characters.
octets Number of bytes.
Captive Portal Commands 819

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no user max-total-octets
Use this command to set to the default the number of octets in bytes that the user is allowed
to transmit and receive. The user-id variable is the ID of a user configured in the local
database, and is a number in the range of 1 to 128.
Format no user user-id max-total-octets
Mode Captive Portal Config
show captive-portal user
This command displays all configured users or a specific user in the captive portal local user
database. Enter the optional user ID to view information about the specified user. The
optional user-id variable is the ID of a user configured in the local database, and is a
number in the range of 1 to 128. Enter the group keyword or the group keyword and
group-id variable to view the user information organized by groups.
Format show captive-portal user [user-id] [group [group-id]]
Mode Privileged EXEC
Field Description
User ID Displays the ID of the user.
User Name Displays the user name.
Session Timeout Displays the number of seconds the user can remain in a session before being disconnected from
the Captive Portal.
Idle Timeout Displays the number of seconds the user can remain idle before being disconnected from the
Captive Portal.
Group ID Displays the group identifier for the group to which the user belongs.
When you include the [user-id] variable, the following information also displays:
Password Indicates whether a password has been configured for the user.
Configured
Max Bandwidth Up The maximum rate in bytes per second (bps) at which a client can send data into the network.
(bps)
Max Bandwidth The maximum rate in bps at which a client can receive data from the network.
Down (bps)
Max Bandwidth The maximum number of octets the user is allowed to transmit.
Input Octets (bytes)
Captive Portal Commands 820

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Description
Max Bandwidth The maximum number of octets the user is allowed to receive.
Output Octets
(bytes)
Max Bandwidth The maximum number of octets the user is allowed to transfer, i.e., the sum of octets transmitted
Total Octets (bytes) and received.
clear captive-portal users
This command deletes all captive portal user entries.
Format clear captive-portal users
Mode Privileged EXEC
Captive Portal User Group Commands
Use the following commands to configure CP user groups.
user group (captive portal user group commands)
Use this command to create a user group. The group-id variable is a number in the range
of 1–10.
Format user group group-id
Mode Captive Portal Config
no user group
Use this command to delete a user group. The group-id variable is a number in the range
of 1–10.
Format no user group group-id
Mode Captive Portal Config
user group name
Use this command to configure a group name. The group-id variable is a number in the
range of 1–10. The name variable can be up to 32 alphanumeric characters.
Format user group group-id name name
Mode Captive Portal Config
Captive Portal Commands 821

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
user group moveusers
This command moves existing users from one user group to another. Note that the
destination group must already exist before a move can be successful. The group-id and
destination-group-id variables are each a number in the range of 1-10.
Format user group group-id moveusers destination-group-id
Mode Captive Portal Config
Command example:
(NETGEAR Switch)(Config-CP) #user group 2 moveusers 3
Captive Portal Commands 822

IPv6 Commands

This chapter describes the IPv6 commands. The chapter contains the following sections:
• Tunnel Interface Commands
• Loopback Interface Commands
• IPv6 Routing Commands
• OSPFv3 Commands
• DHCPv6 Commands
The commands in this chapter are in one of three functional groups:
• Show commands. Display switch settings, statistics, and other information.
• Configuration commands. Configure features and options of the switch. For every
configuration command, there is a show command that displays the configuration setting.
• Clear commands. Clear some or all of the settings to factory defaults.
Note: For information about IPv6 management commands, see IPv6
Management Commands.

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Tunnel Interface Commands
The commands in this section describe how to create, delete, and manage tunnel
interfaces.Several different types of tunnels provide functionality to facilitate the transition of
IPv4 networks to IPv6 networks. These tunnels are divided into two classes: configured and
automatic. The distinction is that configured tunnels are explicitly configured with a
destination or endpoint of the tunnel. Automatic tunnels, in contrast, infer the endpoint of the
tunnel from the destination address of packets routed into the tunnel. To assign an IP
address to the tunnel interface, see ip address on page665. To assign an IPv6 address to
the tunnel interface, see ipv6 address on page828.
interface tunnel
Use this command to enter the Interface Config mode for a tunnel interface. The tunnel-id
range is 0 to 7.
Format interface tunnel tunnel-id
Mode Global Config
no interface tunnel
This command removes the tunnel interface and associated configuration parameters for the
specified tunnel interface.
Format no interface tunnel tunnel-id
Mode Global Config
tunnel source
This command specifies the source transport address of the tunnel, either explicitly or by
reference to an interface.
Format tunnel source {ipv4-address | ethernet unit/slot/port}
Mode Interface Config
tunnel destination
This command specifies the destination transport address of the tunnel.
Format tunnel destination ipv4-address
Mode Interface Config
IPv6 Commands 824

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
tunnel mode ipv6ip
This command specifies the mode of the tunnel. With the optional 6to4 argument, the tunnel
mode is set to 6to4 automatic. Without the optional 6to4 argument, the tunnel mode is
configured.
Format tunnel mode ipv6ip [6to4]
Mode Interface Config
show interface tunnel
This command displays the parameters related to tunnel such as tunnel mode, tunnel source
address and tunnel destination address.
Format show interface tunnel [tunnel-id]
Mode Privileged EXEC
If you do not specify a tunnel ID, the command shows the following information for each
configured tunnel.
Term Definition
Tunnel ID The tunnel identification number.
Interface The name of the tunnel interface.
Tunnel Mode The tunnel mode.
Source Address The source transport address of the tunnel.
Destination The destination transport address of the tunnel.
Address
If you specify a tunnel ID, the command shows the following information for the tunnel.
Term Definition
Interface Link Shows whether the link is up or down.
Status
MTU Size The maximum transmission unit for packets on the interface.
IPv6 If you enable IPv6 on the interface and assign an address, the IPv6 address and prefix display.
Address/Length
IPv6 Commands 825

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Loopback Interface Commands
The commands in this section describe how to create, delete, and manage loopback
interfaces. A loopback interface is always expected to be up. This interface can provide the
source address for sent packets and can receive both local and remote packets. The
loopback interface is typically used by routing protocols.
To assign an IP address to the loopback interface, see ip address on page665. To assign
an IPv6 address to the loopback interface, see ipv6 address on page828.
interface loopback
Use this command to enter the Interface Config mode for a loopback interface. The range of
the loopback ID is 0 to 7.
Format interface loopback loopback-id
Mode Global Config
no interface loopback
This command removes the loopback interface and associated configuration parameters for
the specified loopback interface.
Format no interface loopback loopback-id
Mode Global Config
show interface loopback
This command displays information about configured loopback interfaces.
Format show interface loopback [loopback-id]
Mode Privileged EXEC
If you do not specify a loopback ID, the following information appears for each loopback
interface on the system.
Term Definition
Loopback ID The loopback ID associated with the rest of the information in the row.
Interface The interface name.
IP Address The IPv4 address of the interface.
IPv6 Commands 826

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If you specify a loopback ID, the following information appears.
Term Definition
Interface Link Shows whether the link is up or down.
Status
IP Address The IPv4 address of the interface.
MTU size The maximum transmission size for packets on this interface, in bytes.
IPv6 Routing Commands
This section describes the IPv6 commands you use to configure IPv6 on the system and on
the interfaces. This section also describes IPv6 management commands and show
commands.
ipv6 hop-limit
This command defines the unicast hop count used in ipv6 packets originated by the node.
The value is also included in router advertisements. Valid values for hops are 1-255
inclusive. The default “not configured” means that a value of zero is sent in router
advertisements and a value of 64 is sent in packets originated by the node. Note that this is
not the same as configuring a value of 64.
Default not configured
Format ipv6 hop-limit hops
Mode Global Config
no ipv6 hop-limit
This command returns the unicast hop count to the default.
Format no ipv6 hop-limit
Mode Global Config
ipv6 unicast-routing
Use this command to enable the forwarding of IPv6 unicast datagrams.
Default disabled
Format ipv6 unicast-routing
Mode Global Config
IPv6 Commands 827

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ipv6 unicast-routing
Use this command to disable the forwarding of IPv6 unicast datagrams.
Format no ipv6 unicast-routing
Mode Global Config
ipv6 enable
Use this command to enable IPv6 routing on an interface or range of interfaces, including
tunnel and loopback interfaces, that has not been configured with an explicit IPv6 address.
When you use this command, the interface is automatically configured with a link-local
address. You do not need to use this command if you configured an IPv6 global address on
the interface.
Default disabled
Format ipv6 enable
Mode Interface Config
no ipv6 enable
Use this command to disable IPv6 routing on an interface.
Format no ipv6 enable
Mode Interface Config
ipv6 address
Use this command to configure an IPv6 address on an interface or range of interfaces,
including tunnel and loopback interfaces, and to enable IPv6 processing on this interface.
You can assign multiple globally reachable addresses to an interface by using this command.
You do not need to assign a link-local address by using this command since one is
automatically created. The prefix field consists of the bits of the address to be configured.
The prefix_length designates how many of the high-order contiguous bits of the address
make up the prefix.
You can express IPv6 addresses in eight blocks. Also of note is that instead of a period, a
colon now separates each block. For simplification, leading zeros of each 16 bit block can be
omitted. One sequence of 16 bit blocks containing only zeros can be replaced with a double
colon “::”, but not more than one at a time (otherwise it is no longer a unique representation).
• Dropping zeros: 3ffe:ffff:100:f101:0:0:0:1 becomes 3ffe:ffff:100:f101::1
• Local host: 0000:0000:0000:0000:0000:0000:0000:0001 becomes ::1
• Any host: 0000:0000:0000:0000:0000:0000:0000:0000 becomes ::
The hexadecimal letters in the IPv6 addresses are not case-sensitive. An example of an IPv6
prefix and prefix length is 3ffe:1::1234/64.
IPv6 Commands 828

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The optional eui-64 field designates that IPv6 processing on the interfaces was enabled
using an EUI-64 interface ID in the low order 64 bits of the address. If you use this option, the
value of prefix_length must be 64 bits.
Format ipv6 address prefix/prefix_length [eui64]
Mode Interface Config
no ipv6 address
Use this command to remove all IPv6 addresses on an interface or specified IPv6 address.
The prefix parameter consists of the bits of the address to be configured. The
prefix_length designates how many of the high-order contiguous bits of the address
comprise the prefix.The optional eui-64 field designates that IPv6 processing on the
interfaces was enabled using an EUI-64 interface ID in the low order 64 bits of the address.
If you do not supply any parameters, the command deletes all the IPv6 addresses on an
interface.
Format no ipv6 address [prefix/prefix_length] [eui64]
Mode Interface Config
ipv6 address autoconfig
Use this command to allow an in-band interface to acquire an IPv6 address through IPv6
Neighbor Discovery Protocol (NDP) and through the use of Router Advertisement messages.
Default disabled
Format ipv6 address autoconfig
Mode Interface Config
no ipv6 address autoconfig
This command the IPv6 autoconfiguration status on an interface to the default value.
Format no ipv6 address autoconfig
Mode Interface Config
IPv6 Commands 829

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ipv6 address dhcp
This command enables the DHCPv6 client on an in-band interface so that it can acquire
network information, such as the IPv6 address, from a network DHCP server.
Default disabled
Format ipv6 address dhcp
Mode Interface Config
no ipv6 address dhcp
This command releases a leased address and disables DHCPv6 on an interface.
Format no ipv6 address dhcp
Mode Interface Config
ipv6 route
Use this command to configure an IPv6 static route. The ipv6-prefix is the IPv6 network
that is the destination of the static route. The prefix_length is the length of the IPv6
prefix—a decimal value (usually 0-64) that shows how many of the high-order contiguous bits
of the address comprise the prefix (the network portion of the address). A slash mark must
precede the prefix_length. The next-hop-address is the IPv6 address of the next hop
that can be used to reach the specified network. Specifying Null0 as nexthop parameter
adds a static reject route.
The preference parameter is a value the router uses to compare this route with routes from
other route sources that have the same destination. The range for preference is 1–255,
and the default value is 1.
You can specify a unit/slot/port or vlan-id or tunnel_id interface to identify direct
static routes from point-to-point and broadcast interfaces.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id
parameter is a number in the range of 1–4093.
The interface must be specified when using a link-local address as the next hop. A route with
a preference of 255 cannot be used to forward traffic.
Default disabled
Format ipv6 route ipv6-prefix/prefix_length {next-hop-address | Null0 | interface
{unit/slot/port | vlan vlan-id | tunnel tunnel_id} next-hop-address}
[preference]
Mode Global Config
IPv6 Commands 830

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ipv6 route
Use this command to delete an IPv6 static route. Use the command without the optional
parameters to delete all static routes to the specified destination. Use the preference
parameter to revert the preference of a route to the default preference.
Format no ipv6 route ipv6-prefix/prefix_length [{next-hop-address | Null0 |
interface {unit/slot/port| vlan vland-id | tunnel tunnel_id}
next-hop-address} [preference]]
Mode Global Config
ipv6 route distance
This command sets the default distance (preference) for IPv6 static routes. Lower route
distance values are preferred when determining the best route. The ipv6 route
distance command lets you optionally set the distance (preference) of an individual static
route. The default distance is used when no distance is specified in this command. The
preference can be a number in the range 1–255.
Changing the default distance does not update the distance of existing static routes, even if
they were assigned the original default distance. The new default distance will only be
applied to static routes created after entering the ipv6 route distance command.
Default 1
Format ipv6 route distance preference
Mode Global Config
no ipv6 route distance
This command resets the default static route preference value in the router to the original
default preference. Lower route preference values are preferred when determining the best
route.
Format no ipv6 route distance
Mode Global Config
ipv6 route net-prototype
This command adds net prototype IPv6 routes to the hardware.
Use the prefix/prefix-length argument to specify the The destination network and
mask for the route.
Use the nexthopip argument to specify the next-hop IP address, which must belong to an
active routing interface but it does not need to be resolved. The routes are added starting
from the specified prefix and prefix-length.
IPv6 Commands 831

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Use the num-routes argument to specify the number of routes that you want to add to the
hardware.
Format ipv6 route net-prototype prefix/prefix-length nexthopip num-routes
Mode Global Config
no ipv6 route net-prototype
This command removes all net prototype IPv6 routes from the hardware.
Format no ipv6 route net-prototype
Mode Global Config
ipv6 mtu
This command sets the maximum transmission unit (MTU) size, in bytes, of IPv6 packets on
an interface or range of interfaces. This command replaces the default or link MTU with a
new MTU value. The size variable is a number in the range 1280–1500.
Note: The default MTU value for a tunnel interface is 1480. You cannot change
this value.
Default 0 or link speed (MTU value (1500))
Format ipv6 mtu size
Mode Interface Config
no ipv6 mtu
This command resets maximum transmission unit value to default value.
Format no ipv6 mtu
Mode Interface Config
IPv6 Commands 832

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ipv6 nd dad attempts
This command sets the number of duplicate address detection probes transmitted on an
interface or range of interfaces. Duplicate address detection verifies that an IPv6 address on
an interface is unique. The number variable is a number in the range 0–600.
Default 1
Format ipv6 nd dad attempts number
Mode Interface Config
no ipv6 nd dad attempts
This command resets to number of duplicate address detection value to default value.
Format no ipv6 nd dad attempts
Mode Interface Config
ipv6 nd managed-config-flag
This command sets the managed address configuration flag in router advertisements on the
interface or range of interfaces. When the value is true, end nodes use DHCPv6. When the
value is false, end nodes automatically configure addresses.
Default false
Format ipv6 nd managed-config-flag
Mode Interface Config
no ipv6 nd managed-config-flag
This command resets the “managed address configuration” flag in router advertisements to
the default value.
Format no ipv6 nd managed-config-flag
Mode Interface Config
ipv6 nd mtu
This command sets the MTU value for IPv6 router advertisements on an interface. The mtu
argument is a number in the range from 1280 to the maximum MTU that the interface is
capable of minus 18.
Default 0
Format ipv6 nd mtu mtu
Mode Interface Config
IPv6 Commands 833

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ipv6 nd mtu
This command resets the MTU value for IPv6 router advertisements on an interface to 0.
Format no ipv6 nd mtu
Mode Interface Config
ipv6 nd ns-interval
This command sets the interval between router advertisements for advertised neighbor
solicitations, in milliseconds. An advertised value of 0 means the interval is unspecified. This
command can configure a single interface or a range of interfaces. The milliseconds
variable is a period in milliseconds in the range of 1000–4294967295.
Default 0
Format ipv6 nd ns-interval {milliseconds | 0}
Mode Interface Config
no ipv6 nd ns-interval
This command resets the neighbor solicit retransmission interval of the specified interface to
the default value.
Format no ipv6 nd ns-interval
Mode Interface Config
ipv6 nd other-config-flag
This command sets the other stateful configuration flag in router advertisements sent from
the interface.
Default false
Format ipv6 nd other-config-flag
Mode Interface Config
no ipv6 nd other-config-flag
This command resets the “other stateful configuration” flag back to its default value in router
advertisements sent from the interface.
Format no ipv6 nd other-config-flag
Mode Interface Config
IPv6 Commands 834

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ipv6 nd ra-interval
This command sets the transmission interval between router advertisements on the interface
or range of interfaces. The seconds variable is a number in the range 4–1800 seconds.
Default 600
Format ipv6 nd ra-interval-max seconds
Mode Interface Config
no ipv6 nd ra-interval
This command sets router advertisement interval to the default.
Format no ipv6 nd ra-interval-max
Mode Interface Config
ipv6 nd ra-lifetime
This command sets the value, in seconds, that is placed in the Router Lifetime field of the
router advertisements sent from the interface or range of interfaces. The lifetime variable
can be zero, or it must be an integer between the value of the router advertisement
transmission interval and 9000. A value of zero means this router is not to be used as the
default router.
Default 1800
Format ipv6 nd ra-lifetime lifetime
Mode Interface Config
no ipv6 nd ra-lifetime
This command resets router lifetime to the default value.
Format no ipv6 nd ra-lifetime
Mode Interface Config
ipv6 nd raguard attach-policy
This command enables the IPv6 RA guard host mode on the configured interface. All router
advertisement (RAs) and router redirect packets that are received on this interface are
dropped.
Format ipv6 nd raguard attach-policy
Mode Interface Config
IPv6 Commands 835

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ipv6 nd raguard attach-policy
This command disables the IPv6 RA guard host mode on the configured interface.
Format no ipv6 nd raguard attach-policy
Mode Interface Config
ipv6 nd ra hop-limit unspecified
This command configures the router to send Router Advertisements on an interface with an
unspecified (0) Current Hop Limit value. This tells the hosts on that link to ignore the Hop
Limit from this router.
Default Disable
Format ipv6 nd ra hop-limit unspecified
Mode Interface Config
no ipv6 nd ra hop-limit unspecified
This command configures the router to send Router Advertisements on an interface with the
global configured Hop Limit value.
Format no ipv6 nd ra hop-limit unspecified
Mode Interface Config
ipv6 nd reachable-time
This command sets the router advertisement time to consider a neighbor reachable after
neighbor discovery confirmation. Reachable time is specified in milliseconds in a range of
0–4294967295 milliseconds. A value of zero means the time is unspecified by the router.
This command can configure a single interface or a range of interfaces.
Default 0
Format ipv6 nd reachable-time milliseconds
Mode Interface Config
no ipv6 nd reachable-time
This command means reachable time is unspecified for the router.
Format no ipv6 nd reachable-time
Mode Interface Config
IPv6 Commands 836

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ipv6 nd router-preference
Use this command to configure default router preferences that the interface advertises in
router advertisement messages.
Default medium
Format ipv6 nd router-preference {low | medium | high}
Mode Interface Config
no ipv6 nd router-preference
This command resets the router preference advertised by the interface to the default value.
Format no ipv6 nd router-preference
Mode Interface Config
ipv6 nd suppress-ra
This command suppresses router advertisement transmission on an interface or range of
interfaces.
Default disabled
Format ipv6 nd suppress-ra
Mode Interface Config
no ipv6 nd suppress-ra
This command enables router transmission on an interface.
Format no ipv6 nd suppress-ra
Mode Interface Config
ipv6 nd prefix
Use the ipv6 nd prefix command to configure parameters associated with prefixes the
router advertises in its router advertisements. The first optional parameter is the valid lifetime
of the router, in seconds in the range of 0–4294967295 seconds.You can specify a value or
indicate that the lifetime value is infinite. The second optional parameter is the preferred
lifetime of the router in seconds in the range of 0–4294967295 seconds.
This command can be used to configure a single interface or a range of interfaces.
The router advertises its global IPv6 prefixes in its router advertisements (RAs). An RA only
includes the prefixes of the IPv6 addresses configured on the interface where the RA is
transmitted. Addresses are configured using the ipv6 address interface configuration
command. Each prefix advertisement includes information about the prefix, such as its
IPv6 Commands 837

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
lifetime values and whether hosts should use the prefix for on-link determination or address
auto-configuration. Use the ipv6 nd prefix command to configure these values.
The ipv6 nd prefix command allows you to preconfigure RA prefix values before you
configure the associated interface address. In order for the prefix to be included in RAs, you
must configure an address that matches the prefix using the ipv6 address command.
Prefixes specified using ipv6 nd prefix without associated interface address will not be
included in RAs and will not be committed to the device configuration.
Default valid-lifetime—2592000
preferred-lifetime— 604800
autoconfig—enabled
on-link—enabled
Format ipv6 nd prefix prefix/prefix_length [{seconds | infinite} {seconds |
infinite}] [no-autoconfig off-link]
Mode Interface Config
no ipv6 nd prefix
This command sets prefix configuration to default values.
Format no ipv6 nd prefix prefix/prefix_length
Mode Interface Config
ipv6 neighbor
Configures a static IPv6 neighbor with the given IPv6 address and MAC address on a routing
or host interface.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id
parameter is a number in the range of 1–4093.
Format ipv6 neighbor ipv6address {unit/slot/port | vlan vland-id} macaddr
Mode Global Config
Parameter Definition
ipv6address The IPv6 address of the neighbor.
unit/slot/port The unit/slot/port for the interface.
vlan-id The VLAN for the interface.
macaddr The MAC address for the neighbor.
IPv6 Commands 838

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ipv6 neighbor
Removes a static IPv6 neighbor with the given IPv6 address on a routing or host interface.
Format no ipv6 neighbor ipv6address {unit/slot/port | vlan vland-id}
Mode Global Config
ipv6 neighbors dynamicrenew
Use this command to automatically renew the IPv6 neighbor entries. Enables/disables the
periodic NUD (neighbor unreachability detection) to be run on the existing IPv6 neighbor
entries based on the activity of the entries in the hardware. If the setting is disabled, only
those entries that are actively used in the hardware are triggered for NUD at the end of
STALE timeout of 1200 seconds. If the setting is enabled, periodically every 40 seconds a set
of 300 entries are triggered for NUD irrespective of their usage in the hardware.
Default Disabled
Format ipv6 neighbors dynamicrenew
Mode Global Config
no ipv6 neighbors dynamicrenew
Disables automatic renewing of IPv6 neighbor entries.
Format no ipv6 neighbors dynamicrenew
Mode Global Config
ipv6 nud
Use this command to configure Neighbor Unreachability Detection (NUD). NUD verifies that
communication with a neighbor exists.
Format ipv6 nud {backoff-multiple | max-multicast-solicits | max-unicast-solicits}
Mode Global Config
Term Definition
backoff-multiple Sets the exponential backoff multiple to calculate time outs in NS transmissions during NUD. The
value ranges from 1 to 5. 1 is the default. The next timeout value is limited to a maximum value of 60
seconds if the value with exponential backoff calculation is greater than 60 seconds.
max-multicast-solici Sets the maximum number of multicast solicits sent during Neighbor Unreachability Detection. The
ts value ranges from 3 to 255. 3 is the default.
max-unicast-solicits Sets the maximum number of unicast solicits sent during Neighbor Unreachability Detection. The
value ranges from 3 to 10. 3 is the default.
IPv6 Commands 839

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ipv6 prefix-list (IPv6 routing commands)
To create a prefix list or add a prefix list entry, use the ipv6 prefix-list command in Global
Configuration mode. Prefix lists allow matching of route prefixes with those specified in the
prefix list. Each prefix list includes a sequence of prefix list entries ordered by their sequence
numbers. A router sequentially examines each prefix list entry to determine if the route’s
prefix matches that of the entry. An empty or nonexistent prefix list permits all prefixes. An
implicit deny is assume if a given prefix does not match any entries of a prefix list. Once a
match or deny occurs the router does not go through the rest of the list.
Up to 128 prefix lists may be configured. The maximum number of statements allowed in
prefix list is 64.
Default No prefix lists are configured by default. When neither the ge nor the le option is configured, the
destination prefix must match the network/length exactly. If the ge option is configured without the le
option, any prefix with a network mask greater than or equal to the ge value is considered a match.
Similarly, if the le option is configured without the ge option, a prefix with a network mask less than or
equal to the le value is considered a match.
Format ip prefix-list list-name {[seq number] {permit | deny}
ipv6-prefix/prefix-length [ge length] [le length] | renumber
renumber-interval first-statement-number}
Mode Global Configuration
Parameter Description
list-name The text name of the prefix list. Up to 32 characters.
seq number (Optional) The sequence number for this prefix list statement. Prefix list statements are ordered
from lowest sequence number to highest and applied in that order. If you do not specify a
sequence number, the system will automatically select a sequence number five larger than the
last sequence number in the list. Two statements may not be configured with the same
sequence number. The value range for number is from 1 to 4,294,967,294.
permit Permit routes whose destination prefix matches the statement.
deny Deny routes whose destination prefix matches the statement.
ipv6-prefix/prefix-length Specifies the match criteria for routes being compared to the prefix list statement. The
ipv6-prefix can be any valid IP prefix. The length is any IPv6 prefix length from 0 to 32.
ge length (Optional) If this option is configured, then a prefix is only considered a match if its network
mask length is greater than or equal to this value. This value must be longer than the network
length and less than or equal to 32.
le length (Optional) If this option is configured, then a prefix is only considered a match if its network
mask length is less than or equal to this value. This value must be longer than the ge length and
less than or equal to 32.
renumber (Optional) Provides the option to renumber the sequence numbers of the IP prefix list
statements with a given interval starting from a particular sequence number. The valid range for
renumber-interval i s 1– 100, and the valid range for first-statement-number is
1 – 1000.
IPv6 Commands 840

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip prefix-list
To delete a prefix list or a statement in a prefix list, use the no ip prefix-list command.
The no ip prefix-list list-name command deletes the entire prefix list. To remove
an individual statement from a prefix list, you must specify the statement exactly, with all its
options.
Format no ip prefix-list list-name [[seq number] {permit | deny} network/length [ge
length] [le length]]
Mode Global Configuration
ipv6 unreachables
Use this command to enable the generation of ICMPv6 Destination Unreachable messages
on the interface or range of interfaces. By default, the generation of ICMPv6 Destination
Unreachable messages is enabled.
Default enable
Format ipv6 unreachables
Mode Interface Config
no ipv6 unreachables
Use this command to prevent the generation of ICMPv6 Destination Unreachable messages.
Format no ipv6 unreachables
Mode Interface Config
ipv6 unresolved-traffic
Use this command to control the rate at which IPv6 data packets come into the CPU. By
default, rate limiting is disabled. When enabled, the rate, expressed by the seconds
variable, can range from 50 to 1024 packets per second.
Default enable
Format ipv6 unresolved-traffic rate-limit seconds
Mode Global Config
IPv6 Commands 841

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ipv6 unresolved-traffic
Use this command to disable the rate limiting.
Format no ipv6 unresolved-traffic rate-limit
Mode Global Config
ipv6 icmp error-interval
Use this command to limit the rate at which ICMPv6 error messages are sent. The rate limit is
configured as a token bucket, with two configurable parameters, burst-size and burst-interval.
The burst-interval specifies how often the token bucket is initialized with burst-size
tokens. burst-interval is from 0 to 2147483647 milliseconds (msec).
The burst-size is the number of ICMPv6 error messages that can be sent during one
burst-interval. The range is from 1 to 200 messages.
To disable ICMP rate limiting, set burst-interval to zero (0).
Default burst-interval of 1000 msec.
burst-size of 100 messages
Format ipv6 icmp error-interval burst-interval [burst-size]
Mode Global Config
no ipv6 icmp error-interval
Use the no ipv6 icmp error-interval command to return the burst-interval and
burst-size to their default values.
Format no ipv6 icmp error-interval
Mode Global Config
show ipv6 brief
Use this command to display the IPv6 status of forwarding mode and IPv6 unicast routing
mode.
Format show ipv6 brief
Mode Privileged EXEC
IPv6 Commands 842

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
IPv6 Forwarding Shows whether the IPv6 forwarding mode is enabled.
Mode
IPv6 Unicast Shows whether the IPv6 unicast routing mode is enabled.
Routing Mode
IPv6 Hop Limit Shows the unicast hop count used in IPv6 packets originated by the node. For more information, see
ipv6 hop-limit on page827.
ICMPv6 Rate Limit Shows how often the token bucket is initialized with burst-size tokens. For more information, see
Error Interval ipv6 icmp error-interval on page842.
ICMPv6 Rate Limit Shows the number of ICMPv6 error messages that can be sent during one burst-interval. For more
Burst Size information, see ipv6 icmp error-interval on page842.
Maximum Routes Shows the maximum IPv6 route table size.
IPv6 Unresolved Shows the rate in packets-per-second for the number of IPv6 data packets trapped to CPU when the
Data Rate Limit packet fails to be forwarded in the hardware due to unresolved hardware address of the destined
IPv6 node.
IPv6 Neighbors Shows the dynamic renewal mode for the periodic NUD (neighbor unreachability detection) run on
Dynamic Renew the existing IPv6 neighbor entries based on the activity of the entries in the hardware.
IPv6 NUD Shows the maximum number of unicast Neighbor Solicitations sent during NUD (neighbor
Maximum Unicast unreachabililty detection) before switching to multicast Neighbor Solicitations.
Solicits
IPv6 NUD Shows the maximum number of multicast Neighbor Solicitations sent during NUD (neighbor
Maximum Multicast unreachabililty detection) when in UNREACHABLE state.
Solicits
IPv6 NUD Shows the exponential backoff multiple to be used in the calculation of the next timeout value for
Exponential Neighbor Solicitation transmission during NUD (neighbor unreachabililty detection) following the
Backoff Multiple exponential backoff algorithm.
Command example:
(NETGEAR Switch) #show ipv6 brief
IPv6 Unicast Routing Mode...................... Disable
IPv6 Hop Limit................................. 0
ICMPv6 Rate Limit Error Interval............... 1000 msec
ICMPv6 Rate Limit Burst Size................... 100 messages
Maximum Routes................................. 4096
IPv6 Unresolved Data Rate Limit................ 1024 pps
IPv6 Neighbors Dynamic Renew................... Disable
IPv6 NUD Maximum Unicast Solicits.............. 3
IPv6 NUD Maximum Multicast Solicits............ 3
IPv6 NUD Exponential Backoff Multiple.......... 1
IPv6 Commands 843

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ipv6 interface
Use this command to show the usability status of IPv6 interfaces and whether ICMPv6
Destination Unreachable messages may be sent.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id
parameter is a number in the range of 1–4093.
The loopback keyword with the number variable specifies the loopback interface directly
and is a number in the range 0–7. The tunnel keyword with the number variable specifies
the IPv6 tunnel interface and is a number in the range 0–7.
Format show ipv6 interface [brief | unit/slot/port | vlan vlan-id | loopback number
| tunnel number]
Mode Privileged EXEC
If you use the brief parameter, the following information displays for all configured IPv6
interfaces.
Term Definition
Interface The interface in unit/slot/port format.
IPv6 Operational Shows whether the mode is enabled or disabled.
Mode
IPv6 Shows the IPv6 address and length on interfaces with IPv6 enabled.
Address/Length
Method Indicates how each IP address was assigned. The field contains one of the following values:
• DHCP. The address is leased from a DHCP server.
• Manual. The address is manually configured.
Global addresses with no annotation are assumed to be manually configured.
If you specify an interface, the following information also displays.
Term Definition
Routing Mode Shows whether IPv6 routing is enabled or disabled.
IPv6 Enable Mode Shows whether IPv6 is enabled on the interface.
Administrative Mode Shows whether the interface administrative mode is enabled or disabled.
Bandwidth Shows bandwidth of the interface.
Interface Maximum Transmission The MTU size, in bytes.
Unit
Router Duplicate Address Detection The number of consecutive duplicate address detection probes to transmit.
Transmits
IPv6 Commands 844

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Address Autoconfigure Mode Shows whether the autoconfigure mode is enabled or disabled.
Address DHCP Mode Shows whether the DHCPv6 client is enabled on the interface.
IPv6 Hop Limit Unspecified Indicates if the router is configured on this interface to send Router Advertisements
with unspecified (0) as the Current Hop Limit value.
Router Advertisement NS Interval The interval, in milliseconds, between router advertisements for advertised
neighbor solicitations.
Router Advertisement Lifetime Shows the router lifetime value of the interface in router advertisements.
Router Advertisement Reachable The amount of time, in milliseconds, to consider a neighbor reachable after
Time neighbor discovery confirmation.
Router Advertisement Interval The frequency, in seconds, that router advertisements are sent.
Router Advertisement Managed Shows whether the managed configuration flag is set (enabled) for router
Config Flag advertisements on this interface.
Router Advertisement Other Config Shows whether the other configuration flag is set (enabled) for router
Flag advertisements on this interface.
Router Advertisement Router Shows the router preference.
Preference
Router Advertisement Suppress Shows whether router advertisements are suppressed (enabled) or sent (disabled).
Flag
IPv6 Destination Unreachables Shows whether ICMPv6 Destination Unreachable messages may be sent
(enabled) or not (disabled). For more information, see ipv6 unreachables on
p age841.
ICMPv6 Redirect Specifies if ICMPv6 redirect messages are sent back to the sender by the Router in
the redirect scenario is enabled on this interface.
If an IPv6 prefix is configured on the interface, the following information also displays.
Term Definition
IPv6 Prefix is The IPv6 prefix for the specified interface.
Preferred Lifetime The amount of time the advertised prefix is a preferred prefix.
Valid Lifetime The amount of time the advertised prefix is valid.
Onlink Flag Shows whether the onlink flag is set (enabled) in the prefix.
Autonomous Flag Shows whether the autonomous address-configuration flag (autoconfig) is set (enabled) in the
prefix.
IPv6 Commands 845

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show ipv6 interface brief
Oper.
Interface Mode IPv6 Address/Length
---------- -------- ---------------------------------
1/0/33 Enabled FE80::211:88FF:FE2A:3E3C/128
2033::211:88FF:FE2A:3E3C/64
2/0/17 Enabled FE80::211:88FF:FE2A:3E3C/128
2017::A42A:26DB:1049:43DD/128 [DHCP]
0/4/1 Enabled FE80::211:88FF:FE2A:3E3C/128
2001::211:88FF:FE2A:3E3C/64 [AUTO]
0/4/2 Disabled FE80::211:88FF:FE2A:3E3C/128 [TENT]
Command example:
(NETGEAR Switch) #show ipv6 interface 0/4/1
IPv6 is enabled
IPv6 Prefix is ................................ fe80::210:18ff:fe00:1105/128
2001::1/64
Routing Mode................................... Enabled
IPv6 Enable Mode............................... Enabled
Administrative Mode............................ Enabled
IPv6 Operational Mode.......................... Enabled
Bandwidth...................................... 10000 kbps
Interface Maximum Transmit Unit................ 1500
Router Duplicate Address Detection Transmits... 1
Address DHCP Mode.............................. Disabled
IPv6 Hop Limit Unspecified..................... Enabled
Router Advertisement NS Interval............... 0
Router Advertisement Lifetime.................. 1800
Router Advertisement Reachable Time............ 0
Router Advertisement Interval.................. 600
Router Advertisement Managed Config Flag....... Disabled
Router Advertisement Other Config Flag......... Disabled
Router Advertisement Router Preference......... medium
Router Advertisement Suppress Flag............. Disabled
IPv6 Destination Unreachables.................. Enabled
ICMPv6 Redirects............................... Enabled
Prefix 2001::1/64
Preferred Lifetime............................. 604800
Valid Lifetime................................. 2592000
Onlink Flag.................................... Enabled
Autonomous Flag................................ Enabled
IPv6 Commands 846

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ipv6 interface vlan
Use the show ipv6 interface vlan in Privileged EXEC mode to show to show the usability
status of IPv6 VLAN interfaces.
Format show ipv6 interface vlan vlan-id [prefix]
Mode Privileged EXEC
User EXEC
Parameter Description
vlan-id Valid VLAN ID
prefix Display IPv6 Interface Prefix Information
show ipv6 nd raguard policy
This command shows the status of the IPv6 RA guard host mode on the switch. The output
lists the ports and interfaces on which IPv6 RA guard host mode is enabled and the
associated device roles.
Format show ipv6 nd raguard policy
Modes EXEC
Command example:
(Switching) # show ipv6 nd raguard policy
Configured Interfaces
Interface Role
--------------- -------
Gi1/0/1 Host
show ipv6 neighbors
Use this command to display information about the IPv6 neighbors.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id
parameter is a number in the range of 1–4093.
IPv6 Commands 847

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The tunnel keyword with the number variable specifies the IPv6 tunnel interface and is a
number in the range 0–7.
Format show ipv6 neighbor [interface {unit/slot/port | vlan vlan-id | tunnel number
| ipv6-address]
Mode Privileged EXEC
Term Definition
Interface The interface in unit/slot/port format.
IPv6 Address IPV6 address of neighbor or interface.
MAC Address Link-layer Address.
IsRtr Shows whether the neighbor is a router. If the value is TRUE, the neighbor is known to be a router,
and FALSE otherwise. A value of FALSE might mean that routers are not always known to be
routers.
Neighbor State State of neighbor cache entry. Possible values are Incomplete, Reachable, Stale, Delay, Probe, and
Unknown.
Last Updated The time in seconds that has elapsed since an entry was added to the cache.
Type The type of neighbor entry. The type is Static if the entry is manually configured and Dynamic if
dynamically resolved.
clear ipv6 neighbors
Use this command to clear all entries IPv6 neighbor table or an entry on a specific interface.
Use the optional unit/slot/port parameter to specify an interface.
Format clear ipv6 neighbors [unit/slot/port]
Mode Privileged EXEC
show ipv6 protocols
This command lists a summary of the configuration and status for the active IPv6 routing
protocols. The command lists routing protocols that are configured and enabled. If a protocol
is selected on the command line, the display is limited to that protocol.
Format show ipv6 protocols [ospf]
Mode Privileged Exec
Parameter Description
Routing Protocol OSPFv3.
Router ID The router ID configured for OSPFv3.
OSPF Admin Mode Whether OSPF is enabled or disabled globally.
IPv6 Commands 848

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
Maximum Paths The maximum number of next hops in an OSPF route.
Default Route Whether OSPF is configured to originate a default route.
Advertise
Always Whether default advertisement depends on having a default route in the common routing table.
Metric The metric configured to be advertised with the default route.
Metric Type The metric type for the default route.
Command example:
(NETGEAR Switch) #show ipv6 protocols
Routing Protocol .............................. OSPFv3
Router ID ..................................... 1.1.1.1
OSPF Admin Mode ............................... Enable
Maximum Paths ................................. 4
Distance ...................................... Intra 110 Inter 110 Ext 110
Default Route Advertise ....................... Disabled
Always ........................................ FALSE
Metric ........................................ Not configured
Metric Type ................................... External Type 2
Number of Active Areas ........................ 0 (0 normal, 0 stub, 0 nssa)
ABR Status .................................... Disable
ASBR Status ................................... Disable
show ipv6 route
This command displays the IPv6 routing table The ipv6-address specifies a specific IPv6
address for which the best-matching route would be displayed. The
ipv6-prefix/ipv6-prefix-length specifies a specific IPv6 network for which the
matching route would be displayed.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id
parameter is a number in the range of 1–4093.
The protocol specifies the protocol that installed the routes. The protocol is one of the
following keywords: connected, ospf, or static. The all keyword specifies that all
routes including best and nonbest routes are displayed. Otherwise, only the best routes are
displayed.
IPv6 Commands 849

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: If you use the connected keyword for protocol, the all option is
not available because there are no best or nonbest connected routes.
Format show ipv6 route [ipv6-address [protocol] | {{ipv6-prefix/ipv6-prefix-length |
unit/slot/port | vlan vland-id} [protocol] | protocol | summary} [all] | all]
Modes Privileged EXEC
User EXEC
Term Definition
Route Codes The key for the routing protocol codes that might appear in the routing table output.
The show ipv6 route command displays the routing tables in the following format:
Codes: C - connected, S - static
O - OSPF Intra, OI - OSPF Inter, OE1 - OSPF Ext 1, OE2 - OSPF Ext 2
ON1 - OSPF NSSA Ext Type 1, ON2 - OSPF NSSA Ext Type 2, Truncated
The columns for the routing table display the following information.
Term Definition
Code The code for the routing protocol that created this routing entry.
Default Gateway The IPv6 address of the default gateway. When the system does not have a more specific route to a
packet's destination, it sends the packet to the default gateway.
IPv6-Prefix/IPv6-Pr The IPv6-Prefix and prefix-length of the destination IPv6 network corresponding to this route.
efix-Length
Preference/Metric The administrative distance (preference) and cost (metric) associated with this route. An example of
this output is [1/0], where 1 is the preference and 0 is the metric.
Tag The decimal value of the tag associated with a redistributed route, if it is not 0.
Next-Hop The outgoing router IPv6 address to use when forwarding traffic to the next router (if any) in the path
toward the destination.
Route-Timestamp The last updated time for dynamic routes. The format of Route-Timestamp is:
Days:Hours:Minutes if days > = 1
Hours:Minutes:Seconds if days < 1
Interface The outgoing router interface to use when forwarding traffic to the next destination. For reject routes,
the next hop interface would be Null0 interface.
T A flag appended to an IPv6 route to indicate that it is an ECMP route, but only one of its next hops
has been installed in the forwarding table. The forwarding table may limit the number of ECMP
routes or the number of ECMP groups. When an ECMP route cannot be installed because such a
limit is reached, the route is installed with a single next hop. Such truncated routes are identified by
a T after the interface name.
IPv6 Commands 850

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
To administratively control the traffic destined to a particular network and prevent it from
being forwarded through the router, you can configure a static reject route on the router. Such
traffic would be discarded and the ICMP destination unreachable message is sent back to the
source. This is typically used for preventing routing loops. The reject route added in the RTO
is of the type OSPF Inter-Area. Reject routes (routes of REJECT type installed by any
protocol) are not redistributed by OSPF/RIP. Reject routes are supported in both OSPFv2
and OSPFv3.
Command example:
(NETGEAR Switch) #show ipv6 route
IPv6 Routing Table - 3 entries
Codes: C - connected, S - static
O - OSPF Intra, OI - OSPF Inter, OE1 - OSPF Ext 1, OE2 - OSPF Ext 2
ON1 - OSPF NSSA Ext Type 1, ON2 - OSPF NSSA Ext Type 2
S 2001::/64 [10/0] directly connected, Null0
C 2003::/64 [0/0]
via ::, 0/11
S 2005::/64 [1/0]
via 2003::2, 0/11
C 5001::/64 [0/0]
via ::, 0/5
OE1 6001::/64 [110/1]
via fe80::200:42ff:fe7d:2f19, 00h:00m:23s, 0/5
OI 7000::/64 [110/6]
via fe80::200:4fff:fe35:c8bb, 00h:01m:47s, 0/11
Command example:
The following example displays a truncated route:
(NETGEAR Switch) #show ipv6 route
IPv6 Routing Table - 2 entries
Codes: C - connected, S - static, 6To4 - 6to4 Route
O - OSPF Intra, OI - OSPF Inter, OE1 - OSPF Ext 1, OE2 - OSPF Ext 2
ON1 - OSPF NSSA Ext Type 1, ON2 - OSPF NSSA Ext Type 2
C 2001:db9:1::/64 [0/0]
via ::, 0/1
OI 3000::/64 [110/1]
via fe80::200:e7ff:fe2e:ec3f, 00h:00m:11s, 0/1 T
IPv6 Commands 851

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ipv6 route ecmp-groups
This command reports all current ECMP groups in the IPv6 routing table. An ECMP group is
a set of two or more next hops used in one or more routes. The groups are numbered
arbitrarily from 1 to n. The output indicates the number of next hops in the group and the
number of routes that use the set of next hops. The output lists the IPv6 address and
outgoing interface of each next hop in each group.
Format show ipv6 route ecmp-groups
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show ipv6 route ecmp-groups
ECMP Group 1 with 2 next hops (used by 1 route)
2001:DB8:1::1 on interface 2/1
2001:DB8:2::14 on interface 2/2
ECMP Group 2 with 3 next hops (used by 1 route)
2001:DB8:4::15 on interface 2/32
2001:DB8:7::12 on interface 2/33
2001:DB8:9::45 on interface 2/34
show ipv6 route hw-failure
This command displays the routes that were not added to the hardware because of hash
errors or because the table was full.
Format show ipv6 route hw-failure
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show ipv6 route hw-failure
IPv6 Routing Table - 4 entries
Codes: C - connected, S - static, 6To4 - 6to4 Route
O - OSPF Intra, OI - OSPF Inter, OE1 - OSPF Ext 1, OE2 - OSPF Ext 2
ON1 - OSPF NSSA Ext Type 1, ON2 - OSPF NSSA Ext Type 2, K - kernel
P - Net Prototype
P 3001::/64 [0/1]
via 2001::4, 00h:00m:04s, 0/1 hw-failure
P 3001:0:0:1::/64 [0/1]
via 2001::4, 00h:00m:04s, 0/1 hw-failure
P 3001:0:0:2::/64 [0/1]
via 2001::4, 00h:00m:04s, 0/1 hw-failure
P 3001:0:0:3::/64 [0/1]
via 2001::4, 00h:00m:04s, 0/1 hw-failure
IPv6 Commands 852

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ipv6 route kernel
This command displays kernel routes, if any exist.
Format show ipv6 route kernel
Mode Privileged EXEC
show ipv6 route 6to4
This command displays IPv6-over-IPv4 tunnels that are manually configured in the switch.
Format show ipv6 route 6to4
Mode Privileged EXEC
show ipv6 route net-prototype
This command displays the net prototype routes. The output displays the net prototype
routes with a P.
Format show ipv6 route net-prototype
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show ipv6 route net-prototype
IPv6 Routing Table - 2 entries
Codes: C - connected, S - static, 6To4 - 6to4 Route
O - OSPF Intra, OI - OSPF Inter, OE1 - OSPF Ext 1, OE2 - OSPF Ext 2
ON1 - OSPF NSSA Ext Type 1, ON2 - OSPF NSSA Ext Type 2, K - kernel
P - Net Prototype
P 3001::/64 [0/1]
via 2001::4, 00h:00m:04s, 0/1
P 3001:0:0:1::/64 [0/1]
via 2001::4, 00h:00m:04s, 0/1
show ipv6 route preferences
Use this command to show the preference value associated with the type of route. Lower
numbers have a greater preference. A route with a preference of 255 cannot be used to
forward traffic.
Format show ipv6 route preferences
Mode Privileged EXEC
IPv6 Commands 853

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Local Preference of directly-connected routes.
Static Preference of static routes.
OSPF Intra Preference of routes within the OSPF area.
OSPF Inter Preference of routes to other OSPF routes that are outside of the area.
OSPF External Preference of OSPF external routes.
show ipv6 route summary
This command displays a summary of the state of the routing table. When the optional all
keyword is given, some statistics, such as the number of routes from each source, include
counts for alternate routes. An alternate route is a route that is not the most preferred route to
its destination and therefore is not installed in the forwarding table. To include only the
number of best routes, do not use the optional all keyword.
Format show ipv6 route summary [all]
Modes Privileged EXEC
User EXEC
Term Definition
Connected Routes Total number of connected routes in the routing table.
Static Routes Total number of static routes in the routing table.
OSPF Routes Total number of routes installed by OSPFv3 protocol.
Reject Routes Total number of reject routes installed by all protocols.
Net Prototype Routes The total number of net prototype routes.
Number of Prefixes Summarizes the number of routes with prefixes of different lengths.
Total Routes The total number of routes in the routing table.
Best Routes The number of best routes currently in the routing table. This number only counts the
best route to each destination.
Alternate Routes The number of alternate routes currently in the routing table. An alternate route is a
route that was not selected as the best route to its destination.
Route Adds The number of routes that have been added to the routing table.
Route Modifies The number of routes that have been changed after they were initially added to the
routing table.
Route Deletes The number of routes that have been deleted from the routing table.
IPv6 Commands 854

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Unresolved Route Adds The number of route adds that failed because none of the route’s next hops were on a
local subnet. Note that static routes can fail to be added to the routing table at startup
because the routing interfaces are not yet up. This counter gets incremented in this
case. The static routes are added to the routing table when the routing interfaces come
up.
Invalid Route Adds The number of routes that failed to be added to the routing table because the route
was invalid. A log message is written for each of these failures.
Failed Route Adds The number of routes that failed to be added to the routing table because of a resource
limitation in the routing table.
Hardware Failed Route Adds The number of routes that failed to be inserted into the hardware because of a hash
error or a table-full condition.
Reserved Locals The number of routing table entries reserved for a local subnet on a routing interface
that is down. Space for local routes is always reserved so that local routes can be
installed when a routing interface bounces.
Unique Next Hops The number of distinct next hops used among all routes currently in the routing table.
These include local interfaces for local routes and neighbors for indirect routes.
Unique Next Hops High Water The highest count of unique next hops since counters were last cleared.
Next Hop Groups The current number of next hop groups in use by one or more routes. Each next hop
group includes one or more next hops.
Next Hop Groups High Water The highest count of next hop groups since counters were last cleared.
ECMP Groups The number of next hop groups with multiple next hops.
ECMP Routes The number of routes with multiple next hops currently in the routing table.
Truncated ECMP Routes The number of ECMP routes that are currently installed in the forwarding table with
just one next hop. The forwarding table may limit the number of ECMP routes or the
number of ECMP groups. When an ECMP route cannot be installed because such a
limit is reached, the route is installed with a single next hop.
ECMP Retries The number of ECMP routes that have been installed in the forwarding table after
initially being installed with a single next hop.
Routes with n Next Hops The current number of routes with each number of next hops.
Command example:
(NETGEAR Switch) #show ipv6 route summary
Connected Routes............................... 4
Static Routes.................................. 0
6To4 Routes.................................... 0
OSPF Routes.................................... 13
Intra Area Routes............................ 0
Inter Area Routes............................ 13
External Type-1 Routes....................... 0
External Type-2 Routes....................... 0
IPv6 Commands 855

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Reject Routes.................................. 0
Total routes................................... 17
Best Routes (High)............................. 17 (17)
Alternate Routes............................... 0
Route Adds..................................... 44
Route Deletes.................................. 27
Unresolved Route Adds.......................... 0
Invalid Route Adds............................. 0
Failed Route Adds.............................. 0
Reserved Locals................................ 0
Unique Next Hops (High)........................ 8 (8)
Next Hop Groups (High)......................... 8 (8)
ECMP Groups (High)............................. 3 (3)
ECMP Routes.................................... 12
Truncated ECMP Routes.......................... 0
ECMP Retries................................... 0
Routes with 1 Next Hop......................... 5
Routes with 2 Next Hops........................ 1
Routes with 3 Next Hops........................ 1
Routes with 4 Next Hops........................ 10
Number of Prefixes:
/64: 17
clear ipv6 route counters
The command resets to zero the IPv6 routing table counters reported in the command show
ipv6 route summary on page854. The command only resets event counters. Counters that
report the current state of the routing table, such as the number of routes of each type, are
not reset.
Format clear ipv6 route counters
Mode Privileged Exec
clear ipv6 snooping counters
This command clears the counters that are associated with the IPv6 RA guard host mode.
Format clear ipv6 snooping counters
Modes EXEC
Global Config
IPv6 Commands 856

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(Switching) # clear ipv6 snooping counters
show ipv6 snooping counters
This command displays the counters that are associated with the IPv6 RA guard host mode.
The output displays the number of router advertisements and router redirect packets that are
dropped globally because of the IPv6 RA guard host mode.
Format show ipv6 snooping counters
Modes EXEC
Global Config
Command example:
(Swtiching) # show ipv6 snooping counters
IPv6 Dropped Messages
RA (Router Advertisement - ICMP type 134): 431
REDIR (Router Redirect - ICMP type 137): 6599
RA Redir
------- -------
0 0
show ipv6 vlan
This command displays IPv6 VLAN routing interface addresses.
Format show ipv6 vlan
Modes Privileged EXEC
User EXEC
Term Definition
MAC Address used by Routing VLANs Shows the MAC address.
The rest of the output for this command is displayed in a table with the following column
headings.
Column Headings Definition
VLAN ID The VLAN ID of a configured VLAN.
Logical Interface The interface in unit/slot/port format that is associated with the VLAN ID.
IPv6 The IPv6 prefix and prefix length associated with the VLAN ID.
Address/Prefix
Length
IPv6 Commands 857

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ipv6 traffic
Use this command to show traffic and statistics for IPv6 and ICMPv6. Specify a logical,
loopback, or tunnel interface to view information about traffic on a specific interface.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id
parameter is a number in the range of 1–4093.
If you do not specify an interface, the command displays information about traffic on all
interfaces.
Format show ipv6 traffic [{unit/slot/port | vlan vlan-id | loopback loopback-id |
tunnel tunnel-id}]
Mode Privileged EXEC
Term Definition
Total Datagrams Received Total number of input datagrams received by the interface, including those received
in error.
Received Datagrams Locally Total number of datagrams successfully delivered to IPv6 user-protocols (including
Delivered ICMP). This counter increments at the interface to which these datagrams were
addressed, which might not necessarily be the input interface for some of the
datagrams.
Received Datagrams Discarded Number of input datagrams discarded due to errors in their IPv6 headers, including
Due To Header Errors version number mismatch, other format errors, hop count exceeded, errors
discovered in processing their IPv6 options, etc.
Received Datagrams Discarded Number of input datagrams that could not be forwarded because their size
Due To MTU exceeded the link MTU of outgoing interface.
Received Datagrams Discarded Number of input datagrams discarded because no route could be found to transmit
Due To No Route them to their destination.
Received Datagrams With Number of locally-addressed datagrams received successfully but discarded
Unknown Protocol because of an unknown or unsupported protocol. This counter increments at the
interface to which these datagrams were addressed, which might not be necessarily
the input interface for some of the datagrams.
Received Datagrams Discarded Number of input datagrams discarded because the IPv6 address in their IPv6
Due To Invalid Address header's destination field was not a valid address to be received at this entity. This
count includes invalid addresses (for example, ::0) and unsupported addresses
(for example, addresses with unallocated prefixes). Forentities which are not IPv6
routers and therefore do not forward datagrams, this counter includes datagrams
discarded because the destination address was not a local address.
Received Datagrams Discarded Number of input datagrams discarded because datagram frame didn't carry enough
Due To Truncated Data data.
IPv6 Commands 858

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
