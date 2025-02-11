# 0 Sets the routine precedence

Pages: 698-763

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
0 Sets the routine precedence
1 Sets the priority precedence
2 Sets the immediate precedence
3 Sets the Flash precedence
4 Sets the Flash override precedence
5 Sets the critical precedence
6 Sets the internetwork control precedence
7 Sets the network control precedence
no set ip precedence
Use this command to reset the three IP precedence bits in the IP packet header to the
default.
Format no set ip precedence
Mode Route Map Configuration
show ip policy
This command lists the route map associated with each interface.
Format show ip policy
Mode Privileged Exec
Term Definition
Interface The interface.
Route-map The route map
show route-map
To display a route map, use the show route-map command in Privileged EXEC mode.
Format show route-map [map-name]
Mode Privileged EXEC
Parameter Description
map-name (Optional) Name of a specific route map.
Routing Commands 698

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) # show route-map test
route-map test, permit, sequence 10
Match clauses:
ip address prefix-lists: orange
Set clauses:
set metric 50
Router Discovery Protocol Commands
This section describes the commands you use to view and configure Router Discovery
Protocol settings on the switch. The Router Discovery Protocol enables a host to discover the
IP address of routers on the subnet.
ip irdp
This command enables Router Discovery on an interface or range of interfaces.
Default disabled
Format ip irdp
Mode Interface Config
no ip irdp
This command disables Router Discovery on an interface.
Format no ip irdp
Mode Interface Config
ip irdp address
This command configures the address that the interface uses to send the router discovery
advertisements. The valid values for ipaddr are 224.0.0.1, which is the all-hosts IP
multicast address, and 255.255.255.255, which is the limited broadcast address.
Default 224.0.0.1
Format ip irdp address ipaddr
Mode Interface Config
Routing Commands 699

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip irdp address
This command configures the default address used to advertise the router for the interface.
Format no ip irdp address
Mode Interface Config
ip irdp holdtime
This command configures the value of the holdtime field of the router advertisement sent
from this interface. The seconds argument holdtime value is in the range of 4 to 9000
seconds.
Default 3 * maxinterval
Format ip irdp holdtime seconds
Mode Interface Config
no ip irdp holdtime
This command resets the default value of the holdtime field of the router advertisement sent
from this interface.
Format no ip irdp holdtime
Mode Interface Config
ip irdp maxadvertinterval
This command configures the maximum time allowed between sending router
advertisements from the interface. The range for the seconds argument is 4 to 1800
seconds.
Default 600
Format ip irdp maxadvertinterval seconds
Mode Interface Config
no ip irdp maxadvertinterval
This command resets the default maximum time.
Format no ip irdp maxadvertinterval
Mode Interface Config
Routing Commands 700

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip irdp minadvertinterval
This command configures the minimum time allowed between sending router advertisements
from the interface. The range for seconds argument is 3–1800 seconds.
Default 0.75 * maxadvertinterval
Format ip irdp minadvertinterval seconds
Mode Interface Config
no ip irdp minadvertinterval
This command resets the default minimum time to the default.
Format no ip irdp minadvertinterval
Mode Interface Config
ip irdp multicast
This command configures the destination IP address for router advertisements as 224.0.0.1,
which is the default address. The no form of the command configures the IP address as
255.255.255.255 to instead send router advertisements to the limited broadcast address.
Format ip irdp multicast ip address
Mode Interface Config
no ip irdp multicast
By default, router advertisements are sent to 224.0.0.1. To instead send router
advertisements to the limited broadcast address, 255.255.255.255, use the no form of this
command.
Format no ip irdp multicast
Mode Interface Config
ip irdp preference
This command configures the preferability of the address as a default router address, relative
to other router addresses on the same subnet. The preference number can be a number
from -2147483648 to 2147483647.
Default 0
Format ip irdp preference number
Mode Interface Config
Routing Commands 701

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip irdp preference
This command configures the default preferability of the address as a default router address,
relative to other router addresses on the same subnet.
Format no ip irdp preference
Mode Interface Config
show ip irdp
This command displays the router discovery information for all interfaces, a specified
interface, or specified VLAN. The argument unit/slot/port corresponds to a physical
routing interface or VLAN routing interface. The vlan keyword and vland-id argument are
used to specify the VLAN ID of the routing VLAN directly instead of in a unit/slot/port
format. The vland-id argument can be a number from 1–4093.
Format show ip irdp {unit/slot/port | vlan vland-id | all}
Modes Privileged EXEC
User EXEC
Term Definition
Interface The unit/slot/port that corresponds to a physical routing interface or VLAN routing interface.
vlan Use this keyword to specify the VLAN ID of the routing VLAN directly instead of in a
unit/slot/port format.
Ad Mode The advertise mode, which indicates whether router discovery is enabled or disabled on this
interface.
Dest Address The destination IP address for router advertisements.
Max Int The maximum advertise interval, which is the maximum time, in seconds, allowed between sending
router advertisements from the interface.
Min Int The minimum advertise interval, which is the minimum time, in seconds, allowed between sending
router advertisements from the interface.
Hold Time The amount of time, in seconds, that a system should keep the router advertisement before
discarding it.
Preference The preference of the address as a default router address, relative to other router addresses on the
same subnet.
Routing Commands 702

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Virtual LAN Routing Commands
This section describes the commands you use to view and configure VLAN routing and to
view VLAN routing status information.
vlan routing
This command enables routing on a VLAN. The vlanid value has a range from 1 to 4093.
The interface-id value has a range from 1 to 128. Typically, you do not supply the
interface ID argument, and the system automatically selects the interface ID. However, if you
specify an interface ID, the interface ID becomes the port number in the unit/slot/port
for the VLAN routing interface.
If you select an interface ID that is already in use, the CLI displays an error message and
does not create the VLAN interface. For products that use text-based configuration, including
the interface ID in the vlan routing command for the text configuration ensures that the
unit/slot/port for the VLAN interface stays the same across a restart. Keeping the
unit/slot/port the same ensures that the correct interface configuration is applied to
each interface when the system restarts.
Format vlan routing vlanid [interface-id]
Mode VLAN Config
no vlan routing
This command deletes routing on a VLAN.
Format no vlan routing vlanid
Mode VLAN Config
Command example:
The following example specifies a VLAN ID value. The interface ID argument is not used.
(NETGEAR Switch)(Vlan)#vlan 14
(NETGEAR Switch)(Vlan)#vlan routing 14 ?
<cr> Press enter to execute the command.
<1-24> Enter interface ID
Typically, you press Enter without supplying the Interface ID value; the system automatically
selects the interface ID.
Command example:
The following example specifies interface ID 51 for VLAN 14 interface. The interface ID
becomes the port number in the unit/slot/port for the VLAN routing interface. In this
example, unit/slot/port is 4/51 for VLAN 14 interface.
Routing Commands 703

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
(NETGEAR Switch)(Vlan)#vlan 14 51
(NETGEAR Switch)(Vlan)#
(NETGEAR Switch)#show ip vlan
MAC Address used by Routing VLANs: 00:11:88:59:47:36
Logical
V LAN ID Interface IP Address Subnet Mask
- ------ -------------- ------------- --------------
1 0 4/1 172.16.10.1 255.255.255.0
1 1 4/50 172.16.11.1 255.255.255.0
1 2 4/3 172.16.12.1 255.255.255.0
1 3 4/4 172.16.13.1 255.255.255.0
1 4 4/51 0.0.0.0 0.0.0.0 <--u/s/p is 4/51 for VLAN 14 interface
Command example:
The following example selects an interface ID that is already in use. In this case, the CLI
displays an error message and does not create the VLAN interface.
(NETGEAR Switch) #show ip vlan
MAC Address used by Routing VLANs: 00:11:88:59:47:36
Logical
VLAN ID Interface IP Address Subnet Mask
------- -------------- --------------- ---------------
10 4/1 172.16.10.1 255.255.255.0
11 4/50 172.16.11.1 255.255.255.0
12 4/3 172.16.12.1 255.255.255.0
13 4/4 172.16.13.1 255.255.255.0
14 4/51 0.0.0.0 0.0.0.0
(NETGEAR Switch)#config
(NETGEAR Switch)(Config)#exit
(NETGEAR Switch)#vlan database
(NETGEAR Switch)(Vlan)#vlan 15
(NETGEAR Switch)(Vlan)#vlan routing 15 1
Interface ID 1 is already assigned to another interface
Command example:
The show running-config command lists the interface ID for each routing VLAN:
(NETGEAR Switch) #show running-config
!!Current Configuration:
!
!System Description "Netgear XCM8900"
!System Up Time "0 days 8 hrs 38 mins 3 secs"
Routing Commands 704

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
!Cut-through mode is configured as disabled
! Additional Packages NETGEAR QOS,NETGEAR Multicast,NETGEAR IPv6,NETGEAR IPv6
Management,NETGEAR Metro,NETGEAR Routing,NETGEAR Data Center
!Current SNTP Synchronized Time: SNTP Client Mode Is Disabled
!
vlan database
exit
configure
no logging console
aaa authentication enable "enableNetList" none
line console
serial timeout 0
exit
line telnet
exit
line ssh
exit
!
router rip
exit
router ospf
exit
ipv6 router ospf
exit
exit
interface vlan
Use this command to enter Interface configuration mode for the specified VLAN. The vlan-id
range is 1 to 4093.
Format interface vlan vlan-id
Mode Global Config
show ip vlan
This command displays the VLAN routing information for all VLANs with routing enabled.
Format show ip vlan
Modes Privileged EXEC
User EXEC
Routing Commands 705

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
MAC Address used The MAC Address associated with the internal bridge-router interface (IBRI). The same MAC
by Routing VLANs Address is used by all VLAN routing interfaces. It will be displayed above the per-VLAN information.
VLAN ID The identifier of the VLAN.
Logical Interface The logical unit/slot/port associated with the VLAN routing interface.
IP Address The IP address associated with this VLAN.
Subnet Mask The subnet mask that is associated with this VLAN.
Virtual Router Redundancy Protocol
Commands
This section describes the commands you use to view and configure Virtual Router
Redundancy Protocol (VRRP) and to view VRRP status information. VRRP helps provide
failover and load balancing when you configure two devices as a VRRP pair.
ip vrrp (Global Config)
Use this command in Global Config mode to enable the administrative mode of VRRP on the
router.
Default none
Format ip vrrp
Mode Global Config
no ip vrrp
Use this command in Global Config mode to disable the default administrative mode of
VRRP on the router.
Format no ip vrrp
Mode Global Config
Routing Commands 706

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip vrrp (Interface Config)
Use this command in Interface Config mode to create a virtual router associated with the
interface or range of interfaces. The parameter vrid is the virtual router ID, which has an
integer value range from 1 to 255.
Format ip vrrp vrid
Mode Interface Config
no ip vrrp
Use this command in Interface Config mode to delete the virtual router associated with the
interface. The virtual Router ID, vrid, is an integer value that ranges from 1 to 255.
Format no ip vrrp vrid
Mode Interface Config
ip vrrp mode
This command enables the virtual router configured on the specified interface. Enabling the
status field starts a virtual router. The parameter vrid is the virtual router ID which has an
integer value ranging from 1 to 255.
Default disabled
Format ip vrrp vrid mode
Mode Interface Config
no ip vrrp mode
This command disables the virtual router configured on the specified interface. Disabling the
status field stops a virtual router. The parameter vrid is the virtual router ID which has an
integer value ranging from 1 to 255.
Format no ip vrrp vrid mode
Mode Interface Config
ip vrrp ip
This command sets the virtual router IP address value for an interface or range of interfaces.
The value for ipaddr is the IP address which is to be configured on that interface for VRRP.
The parameter vrid is the virtual router ID which has an integer value range from 1 to 255.
Routing Commands 707

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
You can use the optional secondary keyword to designate the IP address as a secondary
IP address.
Default none
Format ip vrrp vrid ip ipaddr [secondary]
Mode Interface Config
no ip vrrp ip
Use this command in Interface Config mode to delete a secondary IP address value from the
interface. To delete the primary IP address, you must delete the virtual router on the
interface.
The value for ipaddr is the IP address which is to be configured on that interface for VRRP.
The parameter vrid is the virtual router ID which has an integer value range from 1 to 255.
Format no ip vrrp vrid ipaddress secondary
Mode Interface Config
ip vrrp accept-mode
Use this command to allow the VRRP Master to accept ping packets sent to one of the virtual
router's IP addresses. The parameter vrid is the virtual router ID which has an integer value
range from 1 to 255.
Note: VRRP accept-mode allows only ICMP Echo Request packets. No
other type of packet is allowed to be delivered to a VRRP address.
Default disabled
Format ip vrrp vrid accept-mode
Mode Interface Config
no ip vrrp accept-mode
Use this command to prevent the VRRP Master from accepting ping packets sent to one of
the virtual router's IP addresses. The parameter vrid is the virtual router ID which has an
integer value range from 1 to 255.
Format no ip vrrp vrid accept-mode
Mode Interface Config
Routing Commands 708

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip vrrp authentication
This command sets the authorization details value for the virtual router configured on a
specified interface or range of interfaces. The parameter none or simple specifies the
authorization type for virtual router configured on the specified interface. The parameter key
is optional and is only required when authorization type is a simple text password. The
parameter vrid is the virtual router ID which has an integer value ranges from 1 to 255.
Default no authorization
Format ip vrrp vrid authentication {none | simple key}
Mode Interface Config
no ip vrrp authentication
This command sets the default authorization details value for the virtual router configured on
a specified interface or range of interfaces. The parameter vrid is the virtual router ID which
has an integer value ranges from 1 to 255.
Format no ip vrrp vrid authentication
Mode Interface Config
ip vrrp preempt
This command sets the preemption mode value for the virtual router configured on a
specified interface or range of interfaces. The parameter vrid is the virtual router ID which
has an integer value ranges from 1 to 255.
Default enabled
Format ip vrrp vrid preempt
Mode Interface Config
no ip vrrp preempt
This command sets the default preemption mode value for the virtual router configured on a
specified interface or range of interfaces. The parameter vrid is the virtual router ID which
has an integer value ranges from 1 to 255.
Format no ip vrrp vrid preempt
Mode Interface Config
ip vrrp priority
This command sets the priority of a router within a VRRP group. It can be used to configure
an interface or a range of interfaces. Higher values equal higher priority. The range is from
Routing Commands 709

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
1 to 254. The parameter vrid is the virtual router ID which has an integer value ranges from
1 to 255.
The router with the highest priority is elected master. If a router is configured with the address
used as the address of the virtual router, the router is called the address owner. The priority of
the address owner is always 255 so that the address owner is always master. If the master
has a priority less than 255 (it is not the address owner) and you configure the priority of
another router in the group higher than the master’s priority, the router will take over as
master only if preempt mode is enabled.
Default 100 unless the router is the address owner, in which case its priority is automatically set to 255.
Format ip vrrp vrid priority priority
Mode Interface Config
no ip vrrp priority
This command sets the default priority value for the virtual router configured on a specified
interface or range of interfaces. The parameter vrid is the virtual router ID which has an
integer value ranges from 1 to 255.
Format no ip vrrp vrid priority
Mode Interface Config
ip vrrp timers advertise
This command sets the frequency, from 1–255 seconds, that an interface or range of
interfaces on the specified virtual router sends a virtual router advertisement. The parameter
vrid is the virtual router ID which has an integer value ranges from 1 to 255.
Default 1
Format ip vrrp vrid timers advertise seconds
Mode Interface Config
no ip vrrp timers advertise
This command sets the default virtual router advertisement value for an interface or range of
interfaces. The parameter vrid is the virtual router ID which has an integer value ranges
from 1 to 255.
Format no ip vrrp vrid timers advertise
Mode Interface Config
Routing Commands 710

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip vrrp track interface
Use this command to alter the priority of the VRRP router based on the availability of its
interfaces. This command is useful for tracking interfaces that are not configured for VRRP.
The parameter vrid is the virtual router ID which has an integer value ranges from 1 to 255.
Only IP interfaces are tracked. A tracked interface is up if the IP on that interface is up.
Otherwise, the tracked interface is down. You can use this command to configure a single
interface or range of interfaces. The argument unit/slot/port corresponds to a physical
routing interface or VLAN routing interface. The vlan keyword and vlan-id parameter are
used to specify the VLAN ID of the routing VLAN directly instead of in a unit/slot/port
format. The vlan-id can be a number from 1–4093.
When the tracked interface is down or the interface has been removed from the router, the
priority of the VRRP router will be decremented by the value specified in the priority
argument. When the interface is up for IP protocol, the priority will be incremented by the
priority value.
A VRRP configured interface can track more than one interface. When a tracked interface
goes down, then the priority of the router will be decreased by 10 (the default priority
decrement) for each downed interface. The default priority decrement is changed using the
priority argument. The default priority of the virtual router is 100, and the default
decrement priority is 10. By default, no interfaces are tracked. If you specify just the interface
to be tracked, without giving the optional priority, then the default priority will be set. The
default priority decrement is 10.
Default priority: 10
Format ip vrrp vrid track interface {unit/slot/port | vlan vlan-id} [decrement
priority]
Mode Interface Config
no ip vrrp track interface
Use this command to remove the interface or range of interfaces from the tracked list or to
restore the priority decrement to its default. The parameter vrid is the virtual router ID which
has an integer value ranges from 1 to 255.
Format no ip vrrp vrid track interface {unit/slot/port | vlan vlan-id} [decrement]
Mode Interface Config
ip vrrp track ip route
Use this command to track the route reachability on an interface or range of interfaces. The
parameter vrid is the virtual router ID which has an integer value ranges from 1 to 255.
When the tracked route is deleted, the priority of the VRRP router will be decremented by the
value specified in the priority argument. When the tracked route is added, the priority will
be incremented by the same.
A VRRP configured interface can track more than one route. When a tracked route goes
down, then the priority of the router will be decreased by 10 (the default priority decrement)
Routing Commands 711

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
for each downed route. By default no routes are tracked. If you specify just the route to be
tracked, without giving the optional priority, then the default priority will be set. The default
priority decrement is 10. The default priority decrement is changed using the priority
argument.
Default priority: 10
Format ip vrrp vrid track ip route ip-address/prefix-length [decrement priority]
Mode Interface Config
no ip vrrp track ip route
Use this command to remove the route from the tracked list or to restore the priority
decrement to its default. When removing a tracked IP route from the tracked list, the priority
should be incremented by the decrement value if the route is not reachable. The parameter
vrid is the virtual router ID which has an integer value ranges from 1 to 255.
Format no ip vrrp vrid track interface unit/slot/port [decrement]
Mode Interface Config
show ip vrrp interface stats
This command displays the statistical information about each virtual router configured on the
switch. The parameter vrid is the virtual router ID which has an integer value ranges from 1
to 255.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vlan-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in a unit/slot/port format. The vlan-id can
be a number from 1–4093.
Format show ip vrrp interface stats {unit/slot/port | vlan vlan-id} vrid
Modes Privileged EXEC
User EXEC
Term Definition
Uptime The time that the virtual router has been up, in days, hours, minutes and seconds.
Protocol The protocol configured on the interface.
State Transitioned The total number of times virtual router state has changed to MASTER.
to Master
Advertisement The total number of VRRP advertisements received by this virtual router.
Received
Advertisement The total number of VRRP advertisements received for which advertisement interval is different than
Interval Errors the configured value for this virtual router.
Routing Commands 712

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Authentication The total number of VRRP packets received that don't pass the authentication check.
Failure
IP TTL errors The total number of VRRP packets received by the virtual router with IP TTL (time to live) not equal
to 255.
Zero Priority The total number of VRRP packets received by virtual router with a priority of '0'.
Packets Received
Zero Priority The total number of VRRP packets sent by the virtual router with a priority of '0'.
Packets Sent
Invalid Type The total number of VRRP packets received by the virtual router with invalid 'type' field.
Packets Received
Address List Errors The total number of VRRP packets received for which address list does not match the locally
configured list for the virtual router.
Invalid The total number of VRRP packets received with unknown authentication type.
Authentication
Type
Authentication The total number of VRRP advertisements received for which the authentication type is not equal to
Type Mismatch the locally configured type for this virtual router.
Packet Length The total number of VRRP packets received with packet length less than length of VRRP header.
Errors
show ip vrrp
This command displays whether VRRP functionality is enabled or disabled on the switch. It
also displays some global parameters which are required for monitoring. This command
takes no options.
Format show ip vrrp
Modes Privileged EXEC
User EXEC
Term Definition
VRRP Admin Mode The administrative mode for VRRP functionality on the switch.
Router Checksum The total number of VRRP packets received with an invalid VRRP checksum value.
Errors
Router Version The total number of VRRP packets received with Unknown or unsupported version number.
Errors
Router VRID Errors The total number of VRRP packets received with invalid VRID for this virtual router.
Routing Commands 713

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ip vrrp interface
This command displays all configuration information and VRRP router statistics of a virtual
router configured on a specific interface. The parameter vrid is the virtual router ID which
has an integer value ranges from 1 to 255.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vlan-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in a unit/slot/port format. The vlan-id can
be a number from 1–4093.
Format show ip vrrp interface {unit/slot/port | vlan vlan-id} vrid
Modes Privileged EXEC
User EXEC
Term Definition
IP Address The configured IP address for the Virtual router.
VMAC address The VMAC address of the specified router.
Authentication type The authentication type for the specific virtual router.
Priority The priority value for the specific virtual router, taking into account any priority decrements for
tracked interfaces or routes.
Configured Priority The priority configured through the ip vrrp vrid priority priority command.
Advertisement The advertisement interval in seconds for the specific virtual router.
interval
Pre-Empt Mode The preemption mode configured on the specified virtual router.
Administrative The status (Enable or Disable) of the specific router.
Mode
Accept Mode When enabled, the VRRP Master can accept ping packets sent to one of the virtual router’s IP
addresses.
State The state (Master/backup) of the virtual router.
Command example:
show ip vrrp interface <u/s/p> vrid
Primary IP Address............................. 1.1.1.5
VMAC Address................................... 00:00:5e:00:01:01
Authentication Type............................ None
Priority....................................... 80
Configured priority.......................... 100
Advertisement Interval (secs).................. 1
Pre-empt Mode.................................. Enable
Administrative Mode............................ Enable
Routing Commands 714

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Accept Mode.................................... Enable
State.......................................... Initialized
T rack Interface State DecrementPriority
- -------------- - ----- ------------------
< 1/0/1> d own 10
T rackRoute (pfx/len) S tate DecrementPriority
- ----------------------- ------ ------------------
1 0.10.10.1/255.255.255.0 d own 10
show ip vrrp interface brief
This command displays information about each virtual router configured on the switch. This
command takes no options. It displays information about each virtual router.
Format show ip vrrp interface brief
Modes Privileged EXEC
User EXEC
Term Definition
Interface unit/slot/port
VRID The router ID of the virtual router.
IP Address The virtual router IP address.
Mode Indicates whether the virtual router is enabled or disabled.
State The state (Master/backup) of the virtual router.
clear ip vrrp interface stats
This command clears VRRP statistical information from an interface or a VLAN. The virtual
router ID, vrid, is an integer value that ranges from 1 to 255.
Format clear ip vrrp interface stats {unit/slot/port vrid} | {vlan vlan-id vrid}
Modes Interface Config
DHCP and BootP Relay Commands
This section describes the commands you use to configure BootP/DHCP Relay on the
switch. A DHCP relay agent operates at Layer 3 and forwards DHCP requests and replies
between clients and servers when they are not on the same physical subnet.
Routing Commands 715

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
bootpdhcprelay cidoptmode
This command enables the circuit ID option mode for BootP/DHCP Relay on the system.
Default disabled
Format bootpdhcprelay cidoptmode
Mode Global Config
no bootpdhcprelay cidoptmode
This command disables the circuit ID option mode for BootP/DHCP Relay on the system.
Format no bootpdhcprelay cidoptmode
Mode Global Config
bootpdhcprelay maxhopcount
This command configures the maximum allowable relay agent hops for BootP/DHCP Relay
on the system. The hops parameter has a range of 1 to 16.
Default 4
Format bootpdhcprelay maxhopcount hops
Mode Global Config
no bootpdhcprelay maxhopcount
This command configures the default maximum allowable relay agent hops for BootP/DHCP
Relay on the system.
Format no bootpdhcprelay maxhopcount
Mode Global Config
bootpdhcprelay minwaittime
This command configures the minimum wait time in seconds for BootP/DHCP Relay on the
system. When the BootP relay agent receives a BOOTREQUEST message, it can use the
seconds-since-client-began-booting field of the request as a factor in deciding whether to
relay the request or not. The minwaittime seconds parameter has a range of 0 to 100
seconds.
Default 0
Format bootpdhcprelay minwaittime seconds
Mode Global Config
Routing Commands 716

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no bootpdhcprelay minwaittime
This command configures the default minimum wait time in seconds for BootP/DHCP Relay
on the system.
Format no bootpdhcprelay minwaittime
Mode Global Config
show bootpdhcprelay
This command displays the BootP/DHCP Relay information.
Format show bootpdhcprelay
Modes Privileged EXEC
User EXEC
Term Definition
Maximum Hop Count The maximum allowable relay agent hops.
Minimum Wait Time (Seconds) The minimum wait time.
Admin Mode Indicates whether relaying of requests is enabled or disabled.
Circuit Id Option Mode The DHCP circuit Id option which may be enabled or disabled.
IP Helper Commands
This section describes the commands to configure and monitor the IP Helper agent. IP
Helper relays DHCP and other broadcast UDP packets from a local client to one or more
servers which are not on the same network at the client.
The IP Helper feature provides a mechanism that allows a router to forward certain
configured UDP broadcast packets to a particular IP address. This allows various
applications to reach servers on nonlocal subnets, even if the application was designed to
assume a server is always on a local subnet and uses broadcast packets (with either the
limited broadcast address 255.255.255.255, or a network directed broadcast address) to
reach the server.
The network administrator can configure relay entries both globally and on routing interfaces.
Each relay entry maps an ingress interface and destination UDP port number to a single IPv4
address (the helper address). The network administrator may configure multiple relay entries
for the same interface and UDP port, in which case the relay agent relays matching packets
to each server address. Interface configuration takes priority over global configuration. That
is, if a packet’s destination UDP port matches any entry on the ingress interface, the packet
is handled according to the interface configuration. If the packet does not match any entry on
the ingress interface, the packet is handled according to the global IP helper configuration.
Routing Commands 717

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The network administrator can configure discard relay entries, which direct the system to
discard matching packets. Discard entries are used to discard packets received on a specific
interface when those packets would otherwise be relayed according to a global relay entry.
Discard relay entries may be configured on interfaces, but are not configured globally.
In addition to configuring the server addresses, the network administrator also configures
which UDP ports are forwarded. Certain UDP port numbers can be specified by name in the
UI as a convenience, but the network administrator can configure a relay entry with any UDP
port number. The network administrator may configure relay entries that do not specify a
destination UDP port. The relay agent relays assumes these entries match packets with the
UDP destination ports listed in the following table. This is the list of default ports.
T able 10. Default ports—UDP port numbers implied by wildcard
Protocol UDP Port Number
IEN-116 Name Service 42
DNS 53
NetBIOS Name Server 137
NetBIOS Datagram Server 138
TACACS Server 49
Time Service 37
DHCP 67
Trivial File Transfer Protocol (TFTP) 69
The system limits the number of relay entries to four times the maximum number of routing
interfaces. The network administrator can allocate the relay entries as he likes. There is no
limit to the number of relay entries on an individual interface, and no limit to the number of
servers for a given interface and UDP port pair.
The relay agent relays DHCP packets in both directions. It relays broadcast packets from the
client to one or more DHCP servers, and relays to the client packets that the DHCP server
unicasts back to the relay agent. For other protocols, the relay agent only relays broadcast
packets from the client to the server. Packets from the server back to the client are assumed
to be unicast directly to the client. Because there is no relay in the return direction for
protocols other than DHCP, the relay agent retains the source IP address from the original
client packet. The relay agent uses a local IP address as the source IP address of relayed
DHCP client packets.
When a switch receives a broadcast UDP packet on a routing interface, the relay agent
checks if the interface is configured to relay the destination UDP port. If so, the relay agent
unicasts the packet to the configured server IP addresses. Otherwise, the relay agent checks
if there is a global configuration for the destination UDP port. If so, the relay agent unicasts
the packet to the configured server IP addresses. Otherwise the packet is not relayed. Note
that if the packet matches a discard relay entry on the ingress interface, then the packet is not
forwarded, regardless of the global configuration.
Routing Commands 718

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The relay agent only relays packets that meet the following conditions:
• The destination MAC address must be the all-ones broadcast address
(FF:FF:FF:FF:FF:FF)
• The destination IP address must be the limited broadcast address (255.255.255.255) or a
directed broadcast address for the receive interface.
• The IP time-to-live (TTL) must be greater than 1.
• The protocol field in the IP header must be UDP (17).
• The destination UDP port must match a configured relay entry.
clear ip helper statistics
Use this command to reset to zero the statistics displayed in the output of the show ip
helper statistics command.
Format clear ip helper statistics
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #clear ip helper statistics
ip helper-address (Global Config)
Use this command to configure the relay of certain UDP broadcast packets received on any
interface. This command can be invoked multiple times, either to specify multiple server
addresses for a given UDP port number or to specify multiple UDP port numbers handled by
a specific server.
Default No helper addresses are configured.
Format ip helper-address server-address [dest-udp-port | dhcp | domain | isakmp |
mobile-ip | nameserver | netbios-dgm | netbios-ns | ntp | pim-auto-rp | rip |
tacacs | tftp | time]
Mode Global Config
Parameter Description
server-address The IPv4 unicast or directed broadcast address to which relayed UDP broadcast packets are sent.
The server address cannot be an IP address configured on any interface of the local router.
dest-udp-port A destination UDP port number from 0 to 65535.
Routing Commands 719

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
port-name As an option, you can specify the destination UDP port by its name. Whether you specify a port by
its number or its name does not matter for the configuration. The names recognized are as follows:
• dhcp (port 67)
• domain (port 53)
• isakmp (port 500)
• mobile-ip (port 434)
• nameserver (port 42)
• netbios-dgm (port 138)
• netbios-ns (port 137)
• ntp (port 123)
• pim-auto-rp (port 496)
• rip (port 520)
• tacacs (port 49)
• tftp (port 69)
• time (port 37)
Other ports must be specified by number.
Command example:
The following example relays DHCP packets that are received on any interface to two DHCP
servers, 10.1.1.1 and 10.1.2.1:
(NETGEAR Switch)#config
(NETGEAR Switch)(config)#ip helper-address 10.1.1.1 dhcp
(NETGEAR Switch)(config)#ip helper-address 10.1.2.1 dhcp
Command example:
The following example relays UDP packets that are received on any interface for all default
ports to the server at 20.1.1.1:
(NETGEAR Switch)#config
(NETGEAR Switch)(config)#ip helper-address 20.1.1.1
no ip helper-address (Global Config)
Use the no ip helper-address command to delete an IP helper entry. Use the command
without any arguments to clear all global IP helper addresses.
Format no ip helper-address [server-address] [dest-udp-port | dhcp | domain | isakmp
| mobile-ip | nameserver | netbios-dgm | netbios-ns | ntp | pim-auto-rp | rip
| tacacs | tftp | time]
Mode Global Config
Routing Commands 720

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip helper-address (Interface Config)
Use this command to configure the relay of certain UDP broadcast packets received on a
specific interface or range of interfaces. This command can be invoked multiple times on a
routing interface, either to specify multiple server addresses for a given port number or to
specify multiple port numbers handled by a specific server.
Default No helper addresses are configured.
Format ip helper-address {server-address | discard} [dest-udp-port | dhcp | domain |
isakmp | mobile ip | nameserver | netbios-dgm | netbios-ns | ntp |
pim-auto-rp | rip | tacacs | tftp | time]
Mode Interface Config
Parameter Description
server-address The IPv4 unicast or directed broadcast address to which relayed UDP broadcast packets are sent.
The server address cannot be in a subnet on the interface where the relay entry is configured, and
cannot be an IP address configured on any interface of the local router.
discard Matching packets should be discarded rather than relayed, even if a global ip helper-address
configuration matches the packet.
dest-udp-port A destination UDP port number from 0 to 65535.
port-name As an option, you can specify the destination UDP port by its name. Whether you specify a port by
its number or its name does not matter for the configuration.The names recognized are as follows:
• dhcp (port 67)
• domain (port 53)
• isakmp (port 500)
• mobile-ip (port 434)
• nameserver (port 42)
• netbios-dgm (port 138)
• netbios-ns (port 137)
• ntp (port 123)
• pim-auto-rp (port 496)
• rip (port 520)
• tacacs (port 49)
• tftp (port 69)
• time (port 37)
Other ports must be specified by number.
Command example:
The following example relays DHCP packets that are received on interface 1/0/2 to two
DHCP servers, 192.168.10.1 and 192.168.20.1:
(NETGEAR Switch)#config
(NETGEAR Switch)(config)#interface 1/0/2
(NETGEAR Switch)(interface 1/0/2)#ip helper-address 192.168.10.1 dhcp
(NETGEAR Switch)(interface 1/0/2)#ip helper-address 192.168.20.1 dhcp
Routing Commands 721

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
The following example relays DHCP and DNS packets to 192.168.30.1:
(NETGEAR Switch)#config
(NETGEAR Switch)(config)#interface 1/0/2
(NETGEAR Switch)(interface 1/0/2)#ip helper-address 192.168.30.1 dhcp
(NETGEAR Switch)(interface 1/0/2)#ip helper-address 192.168.30.1 dns
Command example:
The following example takes precedence over the ip helper-address command that you
enter in global configuration mode. With the following configuration, the relay agent relays
DHCP packets that are received on any interface other than 1/0/2 and 1/0/17 to
192.168.40.1, relays DHCP and DNS packets that are received on 1/0/2 to 192.168.40.2,
relays SNMP traps (port 162) that are received on interface 1/0/17 to 192.168.23.1, and
drops DHCP packets that are received on 1/0/17:
(NETGEAR Switch)#config
(NETGEAR Switch)(config)#ip helper-address 192.168.40.1 dhcp
(NETGEAR Switch)(config)#interface 1/0/2
(NETGEAR Switch)(interface 1/0/2)#ip helper-address 192.168.40.2 dhcp
(NETGEAR Switch)(interface 1/0/2)#ip helper-address 192.168.40.2 domain
(NETGEAR Switch)(interface 1/0/2)#exit
(NETGEAR Switch)(config)#interface 1/0/17
(NETGEAR Switch)(interface 1/0/17)#ip helper-address 192.168.23.1 162
(NETGEAR Switch)(interface 1/0/17)#ip helper-address discard dhcp
no ip helper-address (Interface Config)
Use this command to delete a relay entry on an interface. The command without any
arguments clears all helper addresses on the interface.
Format no ip helper-address [server-address | discard] [dest-udp-port | dhcp |
domain | isakmp | mobile ip | nameserver | netbios-dgm | netbios-ns | ntp |
pim-auto-rp | rip | tacacs | tftp | time]
Mode Interface Config
ip helper enable
Use this command to enable relay of UDP packets. This command can be used to
temporarily disable IP helper without deleting all IP helper addresses. This command
replaces the bootpdhcprelay enable command, but affects not only relay of DHCP
packets, but also relay of any other protocols for which an IP helper address has been
configured.
Routing Commands 722

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default disabled
Format ip helper enable
Mode Global Config
Command example:
(NETGEAR Switch)(config)#ip helper enable
no ip helper enable
Use the no form of this command to disable relay of all UDP packets.
Format no ip helper enable
Mode Global Config
show ip helper-address
Use this command to display the IP helper address configuration. The argument
unit/slot/port corresponds to a physical routing interface or VLAN routing interface.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vlan-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in a unit/slot/port format. The vlan-id can
be a number from 1–4093.
Format show ip helper-address [unit/slot/port | vlan vlan-id]
Mode Privileged EXEC
Parameter Description
interface The relay configuration is applied to packets that arrive on this interface. This field is set to any for
global IP helper entries.
UDP Port The relay configuration is applied to packets whose destination UDP port is this port. Entries whose
UDP port is identified as any are applied to packets with the destination UDP ports listed in Table 4.
Discard If Yes, packets arriving on the given interface with the given destination UDP port are discarded
rather than relayed. Discard entries are used to override global IP helper address entries which
otherwise might apply to a packet.
Hit Count The number of times the IP helper entry has been used to relay or discard a packet.
Server Address The IPv4 address of the server to which packets are relayed.
Command example:
(NETGEAR Switch) #show ip helper-address
IP helper is enabled
Routing Commands 723

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

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
IP Event Dampening Commands
dampening
Use this command to enable IP event dampening on a routing interface.
Format dampening [half-life period] [reuse-threshold suppress-threshold
max-suppress-time [restart restart-penalty]]
Mode Interface Config
Parameter Description
Half-life period The number of seconds it takes for the penalty to reduce by half. The configurable range is 1-30
seconds. Default value is 5 seconds.
Reuse Threshold The value of the penalty at which the dampened interface is restored. The configurable range is
1-20,000. Default value is 1000.
Suppress The value of the penalty at which the interface is dampened. The configurable range is 1-20,000.
Threshold Default value is 2000.
Max Suppress The maximum amount of time (in seconds) an interface can be in suppressed state after it stops
Time flapping. The configurable range is 1-255 seconds. The default value is four times of half-life period.
If half-period value is allowed to default, the maximum suppress time defaults to 20 seconds.
Restart Penalty Penalty applied to the interface after the device reloads. The configurable range is 1-20,000. Default
value is 2000.
no dampening
This command disables IP event dampening on a routing interface.
Format no dampening
Mode Interface Config
show dampening interface
This command summarizes the number of interfaces configured with dampening and the
number of interfaces being suppressed.
Format show dampening interface
Mode Privileged EXEC
Command example:
(NETGEAR Switch)# show dampening interface
2 interfaces are configured with dampening.
1 interface is being suppressed.
Routing Commands 752

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show interface dampening
This command displays the status and configured parameters of the interfaces configured
with dampening.
Format show interface dampening
Mode Privileged EXEC
Parameter Description
Flaps The number times the link state of an interface changed from UP to DOWN.
Penalty Accumulated Penalty.
Supp Indicates if the interface is suppressed or not.
ReuseTm Number of seconds until the interface is allowed to come up again.
HalfL Configured half-life period.
ReuseV Configured reuse-threshold.
SuppV Configured suppress threshold.
MaxSTm Configured maximum suppress time in seconds.
MaxP Maximum possible penalty.
Restart Configured restart penalty.
Note: The command clear counters on page244 resets the flap count to zero.
Note: Any change in the dampening configuration resets the current penalty, reuse time and suppressed state to their
default values, meaning 0, 0, and False respectively.
Command example:
Router# show interface dampening
Interface 0/2
Flaps Penalty Supp ReuseTm HalfL ReuseV SuppV MaxSTm MaxP Restart
0 0 F ALSE 0 5 1 000 2 000 2 0 1 6000 0
Interface 0/3
Flaps Penalty Supp ReuseTm HalfL ReuseV SuppV MaxSTm MaxP Restart
6 1 865 T RUE 1 8 2 0 1 000 2 001 3 0 2 828 1500
Routing Commands 753

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

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Retransmit List The total number of LSAs waiting to be acknowledged by all neighbors. An LSA may be pending
Entries acknowledgment from more than one neighbor.
Maximum Number The maximum number of LSAs that can be waiting for acknowledgment at any given time.
of Retransmit
Entries
Retransmit Entries The maximum number of LSAs on all neighbors’ retransmit lists at any given time.
High Water Mark
NSF Support Indicates whether nonstop forwarding (NSF) is enabled for the OSPF protocol for planned restarts,
unplanned restarts or both (Always).
NSF Restart The user-configurable grace period during which a neighboring router will be in the helper state after
Interval receiving notice that the management unit is performing a graceful restart.
NSF Restart Status The current graceful restart status of the router.
• Not Restarting
• Planned Restart
• Unplanned Restart
NSF Restart Age Number of seconds until the graceful restart grace period expires.
NSF Restart Exit Indicates why the router last exited the last restart:
Reason • N one— Graceful restart has not been attempted.
• In Progress— Restart is in progress.
• C ompleted— The previous graceful restart completed successfully.
• Timed O ut— The previous graceful restart timed out.
• Topology C hanged— The previous graceful restart terminated prematurely because of a
topology change.
NSF Help Support Indicates whether helpful neighbor functionality has been enabled for OSPF for planned restarts,
unplanned restarts, or both (Always).
NSF help Strict Indicates whether strict LSA checking has been enabled. If enabled, then an OSPF helpful neighbor
LSA checking will exit helper mode whenever a topology change occurs. If disabled, an OSPF neighbor will
continue as a helpful neighbor in spite of topology changes.
Prefix-suppression Displays whether prefix-suppression is enabled or disabled.
(alpha3) #show ip ospf
Router ID...................................... 3.3.3.3
OSPF Admin Mode................................ Enable
RFC 1583 Compatibility......................... Enable
External LSDB Limit............................ No Limit
Exit Overflow Interval......................... 0
Spf Delay Time................................. 5
Spf Hold Time.................................. 10
Flood Pacing Interval.......................... 33 ms
LSA Refresh Group Pacing Time.................. 60 sec
Opaque Capability.............................. Enable
Routing Commands 761

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
AutoCost Ref BW................................ 100 Mbps
Default Passive Setting........................ Disabled
Maximum Paths.................................. 4
Default Metric................................. Not configured
Stub Router Configuration...................... <val>
Stub Router Startup Time....................... <val> seconds
Summary LSA Metric Override.................... Enabled (<met>)
Default Route Advertise........................ Disabled
Always......................................... FALSE
Metric......................................... Not configured
Metric Type.................................... External Type 2
Number of Active Areas......................... 1 (1 normal, 0 stub, 0 nssa)
ABR Status..................................... Disable
ASBR Status.................................... Disable
Stub Router.................................... FALSE
Stub Router Status............................. Inactive
Stub Router Reason............................. <reason>
Stub Router Startup Time Remaining............. <duration> seconds
Stub Router Duration........................... <duration>
External LSDB Overflow......................... FALSE
External LSA Count............................. 0
External LSA Checksum.......................... 0
AS_OPAQUE LSA Count............................ 0
AS_OPAQUE LSA Checksum......................... 0
New LSAs Originated............................ 55
LSAs Received.................................. 82
LSA Count...................................... 1
Maximum Number of LSAs......................... 24200
LSA High Water Mark............................ 9
AS Scope LSA Flood List Length................. 0
Retransmit List Entries........................ 0
Maximum Number of Retransmit Entries........... 96800
Retransmit Entries High Water Mark............. 1
NSF Helper Support............................. Always
NSF Helper Strict LSA Checking................. Enabled
Prefix-suppression............................. Disabled
Routing Commands 762

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ip ospf abr
This command displays the internal OSPF routing table entries to Area Border Routers
(ABR). This command takes no options.
Format show ip ospf abr
Mode Privileged EXEC
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
show ip ospf area
This command displays information about the area. The area-id identifies the OSPF area
that is being displayed.
Format show ip ospf area area-id
Modes Privileged EXEC
User EXEC
Term Definition
AreaID The area id of the requested OSPF area.
External Routing A number representing the external routing capabilities for this area.
Spf Runs The number of times that the intra-area route table has been calculated using this area's link-state
database.
Area Border Router The total number of area border routers reachable within this area.
Count
Area LSA Count Total number of link-state advertisements in this area's link-state database, excluding AS External
LSA's.
Area LSA A number representing the Area LSA Checksum for the specified AreaID excluding the external (LS
Checksum type 5) link-state advertisements.
Flood List Length The number of LSAs waiting to be flooded within the area.
Routing Commands 763
