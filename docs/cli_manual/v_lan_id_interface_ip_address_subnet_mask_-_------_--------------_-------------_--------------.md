# v_lan_id_interface_ip_address_subnet_mask_-_------_--------------_-------------_--------------

Pages: 704-714

## Content

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
