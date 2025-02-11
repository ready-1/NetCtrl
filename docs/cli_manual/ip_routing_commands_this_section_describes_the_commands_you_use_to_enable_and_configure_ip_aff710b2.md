# ip_routing_commands_this_section_describes_the_commands_you_use_to_enable_and_configure_ip_aff710b2

Pages: 664-672

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
IP Routing Commands
This section describes the commands you use to enable and configure IP routing on the
switch.
autostate
This command enables AutoState for a VLAN routing interface. AutoState changes the state
of a VLAN routing interface automatically based on link state events (up or down).
By default, AutoState is disabled, which means that a VLAN routing interface could remain up
even if the link is down.
Format autostate
Mode Interface Config
no autostate
This command disables AutoState for a VLAN routing interface.
Format no autostate
Mode Interface Config
routing
This command enables IPv4 and IPv6 routing for an interface or range of interfaces. You can
view the current value for this function with the show ip brief command. The value is
labeled as Routing Mode.
Default disabled
Format routing
Mode Interface Config
no routing
This command disables routing for an interface.
You can view the current value for this function with the show ip brief command. The
value is labeled as Routing Mode.
Format no routing
Mode Interface Config
Routing Commands 664

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip routing
This command enables the IP Router Admin Mode for the switch.
Format ip routing
Mode Global Config
no ip routing
This command disables the IP Router Admin Mode for the switch.
Format no ip routing
Mode Global Config
ip address
This command configures an IP address on an interface or range of interfaces. You can also
use this command to configure one or more secondary IP addresses on the interface. The
command supports RFC 3021 and accepts using 31-bit prefixes on IPv4 point-to-point links.
This command adds the label IP address in the command show ip interface on page675.
Note: The 31-bit subnet mask is only supported on routing interfaces. The
feature is not supported on network port and service port interfaces
because the switch acts as a host, not a router, on these management
interfaces.
Format ip address ipaddr {subnetmask | /masklen} [secondary]
Mode Interface Config
Parameter Description
ipaddr The IP address of the interface.
subnetmask A 4-digit dotted-decimal number which represents the subnet mask of the interface.
masklen Implements RFC 3021. Using the / notation of the subnet mask, this is an integer that indicates the
length of the subnet mask. Range is 5 to 32 bits.
Command example:
The following example configures the subnet mask with an IP address in the dotted decimal
format on interface 0/4/1.
(NETGEAR Switch) #config
(NETGEAR Switch) (Config)#interface 0/4/1
(NETGEAR Switch) (Interface 0/4/1)#ip address 192.168.10.1 255.255.255.254
Routing Commands 665

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
The following example configures the subnet mask with an IP address in the / notation on
interface 0/4/1.
(NETGEAR Switch) #config
(NETGEAR Switch) (Config)#interface 0/4/1
(NETGEAR Switch) (Interface 0/4/1)#ip address 192.168.10.1 /31
no ip address
This command deletes an IP address from an interface. The value for ipaddr is the IP
address of the interface in a.b.c.d format where the range for a, b, c, and d is 1-255. The
value for subnetmask is a 4-digit dotted-decimal number which represents the Subnet Mask
of the interface. To remove all of the IP addresses (primary and secondary) configured on the
interface, enter the command no ip address.
Format no ip address [ipaddr subnetmask [secondary]]
Mode Interface Config
ip address dhcp
This command enables the DHCPv4 client on an in-band interface so that it can acquire
network information, such as the IP address, subnet mask, and default gateway, from a
network DHCP server. When DHCP is enabled on the interface, the system automatically
deletes all manually configured IPv4 addresses on the interface.
To enable the DHCPv4 client on an in-band interface and send DHCP client messages with
the client identifier option, use the ip address dhcp client-id configuration command
in interface configuration mode.
Default disabled
Format ip address dhcp [client-id]
Mode Interface Config
Command example:
The following example enables DHCPv4 on interface 0/4/1:
(NETGEAR Switch) #config
(NETGEAR Switch) (Config)#interface 0/4/1
(NETGEAR Switch) (Interface 0/4/1)#ip address dhcp
Routing Commands 666

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip address dhcp
The no ip address dhcp command releases a leased address and disables DHCPv4 on
an interface. The no form of the ip address dhcp client-id command removes the
client-id option and also disables the DHCP client on the in-band interface.
Format no ip address dhcp [client-id]
Mode Interface Config
ip default-gateway
This command manually configures a default gateway for the switch. Only one default
gateway can be configured. If you invoke this command multiple times, each command
replaces the previous value.
When the system does not have a more specific route to a packet’s destination, it sends the
packet to the default gateway. The system installs a default IPv4 route with the gateway
address as the next hop address. The route preference is 253. A default gateway configured
with this command is more preferred than a default gateway learned from a DHCP server.
Format ip default-gateway ipaddr
Mode Global Config
Parameter Description
ipaddr The IPv4 address of an attached router.
Command example:
The following example sets the default gateway to 10.1.1.1:
(NETGEAR Switch) #config
(NETGEAR Switch) (Config)#ip default-gateway 10.1.1.1
no ip default-gateway
This command removes the default gateway address from the configuration.
Format no ip default-gateway ipaddr
Mode Interface Config
Routing Commands 667

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip load-sharing
This command configures the IP equal-cost multipath (ECMP) load balancing mode.
Default 6
Format ip load-sharing mode {inner | outer}
Mode Global Config
Parameter Description
mode • 1. The mode is based on a hash using the source IP address of the packet.
• 2. The mode is based on a hash using the destination IP address of the packet.
• 3. The mode is based on a hash using the source and destination IP addresses of the packet.
• 4. The mode is based on a hash using the source IP address and the Source TCP/UDP Port
field of the packet.
• 5. The mode is based on a hash using the destination IP address and the Destination TCP/UDP
Port field of the packet.
• 6. The mode is based on a hash using the source and destination IP addresses and the Source
and Destination TCP/UDP Port fields of the packet.
inner The inner IP header is used for tunneled packets.
outer The outer IP header is used for tunneled packets.
no ip load-sharingThis command resets the IP ECMP load balancing mode to default
m ode(6).
Format no ip load-sharing
Mode Global Config
ip unnumbered gratuitous-arp accept
This command enables the switch to automatically configure static interface routes to an
unnumbered peer when the switch dynamically receives gratuitous ARP messages. The
switch uses the IP address of the loopback interface (see the ip unnumbered loopback
command) as the IP address for the unnumbered peer. This behavior is enabled by default.
Format ip unnumbered gratuitous-arp accept
Mode Interface Config
Routing Commands 668

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip unnumbered gratuitous-arp accept
This command prevents the switch from automatically configuring static interface routes to
an unnumbered peer when the switch dynamically receives gratuitous ARP messages.
Format no ip unnumbered gratuitous-arp accept
Mode Interface Config
ip unnumbered loopback
This command enables the switch to identify an unnumbered interface and specifies the
numbered loopback interface from which the unnumbered interface can borrow an address.
The interface argument specifies the loopback interface number.
Format ip unnumbered loopback interface
Mode Interface Config
no ip unnumbered loopback
This removes an unnumbered interface configuration.
Format no ip unnumbered loopback
Mode Interface Config
release dhcp
Use this command to force the DHCPv4 client to release the leased address from a specified
interface or VLAN. The DHCP client sends a DHCP Release message telling the DHCP
server that it no longer needs the IP address, and that the IP address can be reassigned to
another.
Format release dhcp {unit/slot/port | vlan vlan-id}
Mode Privileged EXEC
Routing Commands 669

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
renew dhcp
Use this command to force the DHCPv4 client to immediately renew an IPv4 address lease
for a specified interface or VLAN.
Note: This command can be used on in-band ports as well as the service or
network (out-of-band) port.
Format renew dhcp {unit/slot/port | vlan vlan-id}
Mode Privileged EXEC
renew dhcp service-port
Use this command to renew an IP address on a service port.
Format renew dhcp service-port
Mode Privileged EXEC
ip route
This command configures a static route. The ipaddr parameter is a valid IP address, and
subnetmask is a valid subnet mask. The nexthopip parameter is a valid IP address of the
next hop router. Specifying Null0 as nexthop parameter adds a static reject route. The
optional preference parameter is an integer (value from 1 to 255) that allows you to specify
the preference value (sometimes called administrative distance) of an individual static route.
Among routes to the same destination, the route with the lowest preference value is the route
entered into the forwarding database. By specifying the preference of a static route, you
control whether a static route is more or less preferred than routes from dynamic routing
protocols. The preference also controls whether a static route is more or less preferred than
other static routes to the same destination. A route with a preference of 255 cannot be used
to forward traffic.
For the static routes to be visible, you must perform the following steps:
• Enable ip routing globally.
• Enable ip routing for the interface.
• Confirm that the associated link is also up.
Default preference—1
Format ip route ipaddr subnetmask [nexthopip | Null0 | interface {unit/slot/port |
vlan vlan-id}] [preference] [description description]
Mode Global Config
Routing Commands 670

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip route
This command deletes a single next hop to a destination static route. If you use the
nexthopip argument, the next hop is deleted. If you use the preference keyword, the
preference value of the static route is reset to its default. The other keywords and arguments
function in a similar way.
Format no ip route ipaddr subnetmask [nexthopip | Null0 |interface {unit/slot/port |
vlan vlan-id}] [preference] [description description]
Mode Global Config
ip route default
This command configures the default route. The value for nexthopip is a valid IP address
of the next hop router. The preference is an integer value from 1 to 255. A route with a
preference of 255 cannot be used to forward traffic.
Default preference—1
Format ip route default nexthopip [preference]
Mode Global Config
no ip route default
This command deletes all configured default routes. If the optional nexthopip parameter is
designated, the specific next hop is deleted from the configured default route and if the
optional preference value is designated, the preference of the configured default route is
reset to its default.
Format no ip route default [nexthopip] [preference]
Mode Global Config
ip route distance
This command sets the default distance (preference) for static routes. The distance can be a
number in the range of 1–255. Lower route distance values are preferred when determining
the best route. The ip route and ip route default commands allow you to optionally
set the distance (preference) of an individual static route. The default distance is used when
no distance is specified in these commands. Changing the default distance does not update
the distance of existing static routes, even if they were assigned the original default distance.
The new default distance will only be applied to static routes created after invoking the ip
route distance command.
Default 1
Format ip route distance number
Mode Global Config
Routing Commands 671

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip route distance
This command sets the default static route preference value in the router. Lower route
preference values are preferred when determining the best route.
Format no ip route distance
Mode Global Config
ip route net-prototype
This command adds net prototype IPv4 routes to the hardware.
Format ip route net-prototype prefix/prefix-length nexthopip num-routes
Mode Global Config
Parameter Definition
prefix/prefix-length The destination network and mask for the route.
nexthopip The next-hop IP address, which must belong to an active routing interface but does not
need to be resolved.
num-routes The number of routes that must be added to the hardware starting from the specified
prefix argument and within the specified prefix length.
no ip route net-prototype
This command deletes all the net prototype IPv4 routes that were added to the hardware.
Format no ip route net-prototype
Mode Global Config
ip netdirbcast
This command enables the forwarding of network-directed broadcasts on an interface or
range of interfaces. When enabled, network directed broadcasts are forwarded. When
disabled they are dropped.
Default disabled
Format ip netdirbcast
Mode Interface Config
Routing Commands 672
