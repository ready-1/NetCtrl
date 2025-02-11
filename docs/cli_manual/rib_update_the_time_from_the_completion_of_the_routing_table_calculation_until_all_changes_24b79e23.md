# rib_update_the_time_from_the_completion_of_the_routing_table_calculation_until_all_changes_24b79e23

Pages: 904-920

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
RIB Update The time from the completion of the routing table calculation until all changes have been made in the
common routing table [the Routing Information Base (RIB)], in milliseconds
Reason The event or events that triggered the SPF. The reason codes are as follows:
• R. New router LSA
• N. New network LSA
• SN. New network (inter-area prefix) summary LSA
• SA. New ASBR (inter-area router) summary LSA
• X. New external LSA
• IP. New intra-area prefix LSA
• L. New Link LSA
Command example:
(NETGEAR Switch) #show ipv6 ospf statistics
Area 0.0.0.0: SPF algorithm executed 10 times
Delta T Intra Summ Ext SPF Total RIB Update Reason
2 3:32:46 0 0 0 0 0 R, IP
2 3:32:09 0 0 0 0 0 R, N, IP
2 3:32:04 0 0 0 0 0 R
2 3:31:44 0 0 0 0 0 R, N, IP
2 3:31:39 0 0 0 0 1 R
2 3:29:57 0 3 7 1 0 1 31 R
2 3:29:52 0 1 4 2 9 4 3 5 68 SN
0 4:07:23 0 9 2 3 3 3 1 17 SN
0 4:07:23 0 9 2 3 3 3 1 17 SN
0 4:07:18 0 0 0 1 4 85 SN
0 4:07:14 0 1 0 1 3 X
show ipv6 ospf stub table
This command displays the OSPF stub table. The information below will only be displayed if
OSPF is initialized on the switch.
Format show ipv6 ospf stub table
Modes Privileged EXEC
User EXEC
IPv6 Commands 904

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Area ID A 32-bit identifier for the created stub area.
Type of Service Type of service associated with the stub metric. For this release, Normal TOS is the only
supported type.
Metric Val The metric value is applied based on the TOS. It defaults to the least metric of the type of
service among the interfaces to other areas. The OSPF cost for a route is a function of the
metric value.
Import Summary LSA Controls the import of summary LSAs into stub areas.
show ipv6 ospf virtual-link
This command displays the OSPF Virtual Interface information for a specific area and
neighbor. The area-id parameter identifies the area and the neighbor parameter
identifies the neighbor’s Router ID.
Format show ipv6 ospf virtual-link area-id neighbor
Modes Privileged EXEC
User EXEC
Term Definition
Area ID The area id of the requested OSPF area.
Neighbor Router ID The input neighbor Router ID.
Hello Interval The configured hello interval for the OSPF virtual interface.
Dead Interval The configured dead interval for the OSPF virtual interface.
Interface Transmit Delay The configured transmit delay for the OSPF virtual interface.
Retransmit Interval The configured retransmit interval for the OSPF virtual interface.
Authentication Type The type of authentication the interface performs on LSAs it receives.
State The OSPF Interface States are: down, loopback, waiting, point-to-point, designated router,
and backup designated router. This is the state of the OSPF interface.
Neighbor State The neighbor state.
show ipv6 ospf virtual-link brief
This command displays the OSPFV3 Virtual Interface information for all areas in the system.
Format show ipv6 ospf virtual-link brief
Modes Privileged EXEC
User EXEC
IPv6 Commands 905

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Area ID The area id of the requested OSPFV3 area.
Neighbor The neighbor interface of the OSPFV3 virtual interface.
Hello Interval The configured hello interval for the OSPFV3 virtual interface.
Dead Interval The configured dead interval for the OSPFV3 virtual interface.
Retransmit Interval The configured retransmit interval for the OSPFV3 virtual interface.
Transmit Delay The configured transmit delay for the OSPFV3 virtual interface.
DHCPv6 Commands
This section describes the commands you use to configure the DHCPv6 server on the
system and to view DHCPv6 information.
service dhcpv6
This command enables DHCPv6 configuration on the router.
Default enabled
Format service dhcpv6
Mode Global Config
no service dhcpv6
This command disables DHCPv6 configuration on router.
Format no service dhcpv6
Mode Global Config
IPv6 Commands 906

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ipv6 dhcp client pd
Use this command to enable the Dynamic Host Configuration Protocol (DHCP) for IPv6 client
process (if the process is not currently running) and to enable requests for prefix delegation
through a specified interface. When prefix delegation is enabled and a prefix is successfully
acquired, the prefix is stored in the IPv6 general prefix pool with an internal name defined by
the automatic argument.
Note: The Prefix Delegation client is supported on only one IP interface.
The optional rapid-commit keyword enables the use of a two-message exchange method
for prefix delegation and other configuration. If enabled, the client includes the rapid commit
option in a solicit message.
The DHCP for IPv6 client, server, and relay functions are mutually exclusive on an interface.
If one of these functions is already enabled and a user tries to configure a different function
on the same interface, a message is displayed.
Default Prefix delegation is disabled on an interface.
Format ipv6 dhcp client pd [rapid-commit]
Mode Interface Config
Command example: The following examples enable prefix delegation on interface 1/0/1:
(NETGEAR Switch) #configure
(NETGEAR Switch) (Config)#interface 1/0/1
(NETGEAR Switch) (Interface 1/0/1)# ipv6 dhcp client pd
(NETGEAR Switch) #configure
(NETGEAR Switch) (Config)#interface 1/0/1
(NETGEAR Switch) (Interface 1/0/1)# ipv6 dhcp client pd rapid-commit
no ipv6 dhcp client pd
This command disables requests for prefix delegation.
Format no ipv6 dhcp client pd
Mode Interface Config
ipv6 dhcp server
Use this command to configure DHCPv6 server functionality on an interface or range of
interfaces. The pool-name is the DHCPv6 pool containing stateless and/or prefix delegation
parameters, automatic enables the server to automatically determine which pool to use
when allocating addresses for a client, rapid-commit is an option that allows for an
IPv6 Commands 907

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
abbreviated exchange between the client and server, and pref-value is a value used by
clients to determine preference between multiple DHCPv6 servers. For a particular interface,
DHCPv6 server and DHCPv6 relay functions are mutually exclusive.
Format ipv6 dhcp server {pool-name | automatic} [rapid-commit] [preference
pref-value]
Mode Interface Config
ipv6 dhcp relay destination
Use this command to configure an interface for DHCPv6 relay functionality on an interface or
range of interfaces.
• Use the destination keyword to set the relay server IPv6 address.
• The relay-address parameter is an IPv6 address of a DHCPv6 relay server.
• Use the interface keyword to set the relay server interface.
• The relay-interface parameter is an interface (unit/slot/port) to reach a relay
server.
• The optional remote-id is the Relay Agent Information Option remote ID suboption to
be added to relayed messages.This can either be the special keyword duid-ifid,
which causes the remote ID to be derived from the DHCPv6 server DUID and the relay
interface number, or it can be specified as a user-defined string.
Note: If relay-address is an IPv6 global address, then
relay-interface is not required. If relay-address is a link-local
or multicast address, then relay-interface is required. Finally, if
you do not specify a value for relay-address, then you must
specify a value for relay-interface and the
DHCPV6-ALL-AGENTS multicast address (for example, FF02::1:2)
is used to relay DHCPv6 messages to the relay server.
Format ipv6 dhcp relay {destination [relay-address] interface [relay-interface]|
interface [relay-interface]} [remote-id {duid-ifid | user-defined-string}]
Mode Interface Config
ipv6 dhcp pool
Use this command from Global Config mode to enter IPv6 DHCP Pool Config mode. Use the
exit command to return to Global Config mode. To return to the User EXEC mode, enter
Ctrl+Z. The pool-name must be less than 31 alpha-numeric characters. DHCPv6 pools
are used to specify information for DHCPv6 server to distribute to DHCPv6 clients. These
pools are shared between multiple interfaces over which DHCPv6 server capabilities are
configured.
IPv6 Commands 908

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Once the DHCP for IPv6 configuration information pool has been created, use the ipv6
dhcp server command to associate the pool with a server on an interface. If you do not
configure an information pool, use the ipv6 dhcp server interface configuration
command to enable the DHCPv6 server function on an interface.
When you associate a DHCPv6 pool with an interface, only that pool services requests on
the associated interface. The pool also services other interfaces. If you do not associate a
DHCPv6 pool with an interface, it can service requests on any interface. Not using any IPv6
address prefix means that the pool returns only configured options.
Format ipv6 dhcp pool pool-name
Mode Global Config
no ipv6 dhcp pool
This command removes the specified DHCPv6 pool.
Format no ipv6 dhcp pool pool-name
Mode Global Config
address prefix (IPv6)
Use this command to sets an address prefix for address assignment. This address must be in
hexadecimal, using 16-bit values between colons.
If lifetime values are not configured, the default lifetime values for valid-lifetime and
preferred-lifetime are considered to be infinite.
Format address prefix ipv6-prefix [lifetime {valid-lifetime preferred-lifetime |
infinite}]
Mode IPv6 DHCP Pool Config
Term Definition
lifetime (Optional) Sets a length of time for the hosts to remember router advertisements. If configured, both
valid and preferred lifetimes must be configured.
valid-lifetime The amount of time, in seconds, the prefix remains valid for the requesting router to use. The range
is from 60 through 4294967294. The preferred-lifetime value cannot exceed the
valid-lifetime value.
preferred-lifetime The amount of time, in seconds, that the prefix remains preferred for the requesting router to use.
The range is from 60 through 4294967294. The preferred-lifetime value cannot
exceed the valid-lifetime value.
infinite An unlimited lifetime.
IPv6 Commands 909

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
The following example configures an IPv6 address prefix for the IPv6 configuration pool
pool1:
(NETGEAR Switch) #configure
(NETGEAR Switch) (Config)# ipv6 dhcp pool pool1
(NETGEAR Switch) (Config-dhcp6s-pool)# address prefix 2001::/64
(NETGEAR Switch) (Config-dhcp6s-pool)# exit
domain-name (IPv6)
This command sets the DNS domain name which is provided to DHCPv6 client by DHCPv6
server. DNS domain name is configured for stateless server support. Domain name consist of
no more than 31 alpha-numeric characters. DHCPv6 pool can have multiple number of
domain names with maximum of 8.
Format domain-name dns-domain-name
Mode IPv6 DHCP Pool Config
no domain-name
This command removes dhcpv6 domain name from dhcpv6 pool.
Format no domain-name dns-domain-name
Mode IPv6 DHCP Pool Config
dns-server (IPv6)
This command sets the IPv6 DNS server address, which is provided to DHCPv6 clients by
the DHCPv6 server. The DNS server address is configured for stateless server support. The
DHCPv6 pool can contains a maximum of eight domain names.
Format dns-server dns-server-address
Mode IPv6 DHCP Pool Config
no dns-server
This command removes a DHCPv6 server address from a DHCPv6 server.
Format no dns-server dns-server-address
Mode IPv6 DHCP Pool Config
IPv6 Commands 910

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
prefix-delegation (IPv6)
Multiple IPv6 prefixes can be defined within a pool for distributing to specific DHCPv6 prefix
delegation clients.
• prefix is the delegated IPv6 prefix and prefixlength is the associated prefix length.
• duid is the client's unique DUID value, for example,
00:01:00:09:f8:79:4e:00:04:76:73:43:76.
• hostname is 31 characters textual client’s name which is useful for logging or tracing
only.
• valid lifetime is the valid lifetime for the delegated prefix in seconds, in a range from
0–4294967295 seconds.
• preferred lifetime is the preferred lifetime for the delegated prefix in seconds, in a range
from 0–4294967295 seconds.
Default valid-lifetime seconds: 2592000
preferred-lifetime seconds: 604800
Format prefix-delegation prefix/prefixlength duid [name hostname] [valid-lifetime
seconds] [preferred-lifetime seconds]
Mode IPv6 DHCP Pool Config
no prefix-delegation
This command deletes a specific prefix-delegation client.
Format no prefix-delegation prefix/prefix-delegation duid
Mode IPv6 DHCP Pool Config
show ipv6 dhcp
This command displays the DHCPv6 server name and status.
Format show ipv6 dhcp
Mode Privileged EXEC
Term Definition
DHCPv6 is The status of the DHCPv6 server.
Enabled (Disabled)
Server DUID If configured, shows the DHCPv6 unique identifier.
IPv6 Commands 911

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ipv6 dhcp statistics
This command displays the IPv6 DHCP statistics for all interfaces.
Format show ipv6 dhcp statistics
Mode Privileged EXEC
Term Definition
DHCPv6 Solicit Packets Received Number of solicit received statistics.
DHCPv6 Request Packets Received Number of request received statistics.
DHCPv6 Confirm Packets Received Number of confirm received statistics.
DHCPv6 Renew Packets Received Number of renew received statistics.
DHCPv6 Rebind Packets Received Number of rebind received statistics.
DHCPv6 Release Packets Received Number of release received statistics.
DHCPv6 Decline Packets Received Number of decline received statistics.
DHCPv6 Inform Packets Received Number of inform received statistics.
DHCPv6 Relay-forward Packets Received Number of relay forward received statistics.
DHCPv6 Relay-reply Packets Received Number of relay-reply received statistics.
DHCPv6 Malformed Packets Received Number of malformed packets statistics.
Received DHCPv6 Packets Discarded Number of DHCP discarded statistics.
Total DHCPv6 Packets Received Total number of DHCPv6 received statistics
DHCPv6 Advertisement Packets Transmitted Number of advertise sent statistics.
DHCPv6 Reply Packets Transmitted Number of reply sent statistics.
DHCPv6 Reconfig Packets Transmitted Number of reconfigure sent statistics.
DHCPv6 Relay-reply Packets Transmitted Number of relay-reply sent statistics.
DHCPv6 Relay-forward Packets Transmitted Number of relay-forward sent statistics.
Total DHCPv6 Packets Transmitted Total number of DHCPv6 sent statistics.
show ipv6 dhcp interface
This command displays DHCPv6 information for all relevant interfaces or the specified
interface.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vlan-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in a unit/slot/port format. The vlan-id can
be a number from 1–4093.
IPv6 Commands 912

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If you specify an interface, you can use the optional statistics parameter to view
statistics for the specified interface.
Format show ipv6 dhcp interface {unit/slot/port | vlan vlan-id} [statistics]
Mode Privileged EXEC
Term Definition
IPv6 Interface The interface name in unit/slot/port format.
Mode Shows whether the interface is a IPv6 DHCP relay or server.
If the interface mode is server, the following information displays.
Term Definition
Pool Name The pool name specifying information for DHCPv6 server distribution to DHCPv6 clients.
Server Preference The preference of the server.
Option Flags Shows whether rapid commit is enabled.
If the interface mode is relay, the following information displays.
Term Definition
Relay Address The IPv6 address of the relay server.
Relay Interface The relay server interface in unit/slot/port format.
Number
Relay Remote ID If configured, shows the name of the relay remote.
Option Flags Shows whether rapid commit is configured.
If you use the statistics parameter, the command displays the IPv6 DHCP statistics for the
specified interface. See show ipv6 dhcp statistics on page912 for information about the
output.
show ipv6 dhcp binding
This command displays configured DHCP pool.
Format show ipv6 dhcp binding [ipv6-address]
Mode Privileged EXEC
Term Definition
DHCP Client Address of DHCP Client.
Address
DUID String that represents the Client DUID.
IPv6 Commands 913

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
IAID Identity Association ID.
Prefix/Prefix Length IPv6 address and mask length for delegated prefix.
Prefix Type IPV6 Prefix type (IAPD, IANA, or IATA).
Client Address Address of DHCP Client.
Client Interface IPv6 Address of DHCP Client.
Expiration Address of DNS server address.
Valid Lifetime Valid lifetime in seconds for delegated prefix.
Preferred Lifetime Preferred lifetime in seconds for delegated prefix.
show ipv6 dhcp pool
This command displays configured DHCP pool.
Format show ipv6 dhcp pool pool-name
Mode Privileged EXEC
Term Definition
DHCP Pool Name Unique pool name configuration.
Client DUID Client’s DHCP unique identifier. DUID is generated using the combination of the local
system burned-in MAC address and a timestamp value.
Host Name of the client.
Prefix/Prefix Length IPv6 address and mask length for delegated prefix.
Preferred Lifetime Preferred lifetime in seconds for delegated prefix.
Valid Lifetime Valid lifetime in seconds for delegated prefix.
DNS Server Address Address of DNS server address.
Domain Name DNS domain name.
show serviceport ipv6 dhcp statistics
This command displays the statistics of the DHCPv6 client running on the serviceport
management interface.
Format show serviceport ipv6 dhcp statistics
Mode Privileged EXEC
User EXEC
IPv6 Commands 914

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Description
DHCPv6 Advertisement The number of DHCPv6 Advertisement packets received on the service port interface.
Packets Received
DHCPv6 Reply Packets The number of DHCPv6 Reply packets received on the service port interface.
Received
Received DHCPv6 The number of DHCPv6 Advertisement packets discarded on the service port interface.
Advertisement Packets
Discarded
Received DHCPv6 Reply The number of DHCPv6 Reply packets discarded on the service port interface.
Packets Discarded
DHCPv6 Malformed The number of DHCPv6 packets that are received malformed on the service port interface.
Packets Received
Total DHCPv6 Packets The total number of DHCPv6 packets received on the service port interface.
Received
DHCPv6 Solicit Packets The number of DHCPv6 Solicit packets transmitted on the service port interface.
Transmitted
DHCPv6 Request Packets The number of DHCPv6 Request packets transmitted on the service port interface.
Transmitted
DHCPv6 Renew Packets The number of DHCPv6 Renew packets transmitted on the service port interface.
Transmitted
DHCPv6 Rebind Packets The number of DHCPv6 Rebind packets transmitted on the service port interface.
Transmitted
DHCPv6 Release Packets The number of DHCPv6 Release packets transmitted on the service port interface.
Transmitted
Total DHCPv6 Packets The total number of DHCPv6 packets transmitted on the service port interface.
Transmitted
Command example:
(Netgear switch) #show serviceport ipv6 dhcp statistics
DHCPv6 Client Statistics
-------------------------
DHCPv6 Advertisement Packets Received................. 0
DHCPv6 Reply Packets Received......................... 0
Received DHCPv6 Advertisement Packets Discarded....... 0
Received DHCPv6 Reply Packets Discarded............... 0
DHCPv6 Malformed Packets Received..................... 0
Total DHCPv6 Packets Received......................... 0
DHCPv6 Solicit Packets Transmitted.................... 0
DHCPv6 Request Packets Transmitted.................... 0
DHCPv6 Renew Packets Transmitted...................... 0
DHCPv6 Rebind Packets Transmitted..................... 0
IPv6 Commands 915

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
DHCPv6 Release Packets Transmitted.................... 0
Total DHCPv6 Packets Transmitted...................... 0
clear ipv6 dhcp
Use this command to clear DHCPv6 statistics for all interfaces or for a specific interface. Use
the unit/slot/port parameter to specify the interface.
Format clear ipv6 dhcp {statistics | interface unit/slot/port statistics}
Mode Privileged EXEC
clear ipv6 dhcp binding
This command deletes an automatic address binding from the DHCP server database.
address is a valid IPv6 address.
A binding table entry on the DHCP for IPv6 server is automatically:
• Created whenever a prefix is delegated to a client from the configuration pool.
• Updated when the client renews, rebinds, or confirms the prefix delegation.
• Deleted when the client releases all the prefixes in the binding voluntarily, all prefixes’
valid lifetimes have expired or when you enter the clear ipv6 dhcp binding
command.
If the clear ipv6 dhcp binding command is used with the optional ipv6-address
argument specified, only the binding for the specified client is deleted. If the clear ipv6
dhcp binding command is used without the ipv6-address argument, all automatic client
bindings are deleted from the DHCP for IPv6 binding table.
Format clear ipv6 dhcp binding [ipv6-address]
Mode Privileged EXEC
clear network ipv6 dhcp statistics
Use this command to clear the DHCPv6 statistics on the network management interface.
Format clear network ipv6 dhcp statistics
Mode Privileged EXEC
clear serviceport ipv6 dhcp statistics
Use this command to clear the DHCPv6 client statistics on the service port interface.
Format clear serviceport ipv6 dhcp statistics
Mode Privileged EXEC
IPv6 Commands 916

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
DHCPv6 Snooping Configuration
Commands
This section describes commands you use to configure IPv6 DHCP Snooping.
ipv6 dhcp snooping
Use this command to globally enable IPv6 DHCP Snooping.
Default disabled
Format ipv6 dhcp snooping
Mode Global Config
no ipv6 dhcp snooping
Use this command to globally disable IPv6 DHCP Snooping.
Format no ipv6 dhcp snooping
Mode Global Config
ipv6 dhcp snooping vlan
Use this command to enable DHCP Snooping on a list of comma-separated VLAN ranges.
Default disabled
Format ipv6 dhcp snooping vlan vlan-list
Mode Global Config
no ipv6 dhcp snooping vlan
Use this command to disable DHCP Snooping on VLANs.
Format no ipv6 dhcp snooping vlan vlan-list
Mode Global Config
IPv6 Commands 917

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ipv6 dhcp snooping verify mac-address
Use this command to enable verification of the source MAC address with the client hardware
address in the received DCHP message.
Default enabled
Format ipv6 dhcp snooping verify mac-address
Mode Global Config
no ipv6 dhcp snooping verify mac-address
Use this command to disable verification of the source MAC address with the client hardware
address.
Format no ipv6 dhcp snooping verify mac-address
Mode Global Config
ipv6 dhcp snooping database
Use this command to configure the persistent location of the DHCP Snooping database. This
can be local or a remote file on a given IP machine.
Default local
Format ipv6 dhcp snooping database {local | tftp://hostIP/filename}
Mode Global Config
ip dhcp snooping database write-delay (DHCPv6)
Use this command to configure the interval in seconds at which the DHCP Snooping
database is persisted. For the seconds argument, the interval value is in a range from 15 to
86400 seconds.
Default 300 seconds
Format ip dhcp snooping database write-delay seconds
Mode Global Config
no ip dhcp snooping database write-delay
Use this command to set the write delay value to the default value.
Format no ip dhcp snooping database write-delay
Mode Global Config
IPv6 Commands 918

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ipv6 dhcp snooping binding
Use this command to configure static DHCP Snooping binding.
Format ipv6 dhcp snooping binding mac-address vlan vlan-id ipaddress interface
interface-id
Mode Global Config
no ipv6 dhcp snooping binding
Use this command to remove the DHCP static entry from the DHCP Snooping database.
Format no ipv6 dhcp snooping binding mac-address
Mode Global Config
ipv6 dhcp snooping trust
Use this command to configure an interface or range of interfaces as trusted.
Default disabled
Format ipv6 dhcp snooping trust
Mode Interface Config
no ipv6 dhcp snooping trust
Use this command to configure the port as untrusted.
Format no ipv6 dhcp snooping trust
Mode Interface Config
ipv6 dhcp snooping log-invalid
Use this command to control the logging DHCP messages filtration by the DHCP Snooping
application. This command can be used to configure a single interface or a range of
interfaces.
Default disabled
Format ipv6 dhcp snooping log-invalid
Mode Interface Config
IPv6 Commands 919

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ipv6 dhcp snooping log-invalid
Use this command to disable the logging DHCP messages filtration by the DHCP Snooping
application.
Format no ipv6 dhcp snooping log-invalid
Mode Interface Config
ipv6 dhcp snooping limit
Use this command to control the rate at which the DHCP Snooping messages come on an
interface or range of interfaces. By default, rate limiting is disabled. When enabled, the rate
can range from 0 to 300 packets per second, which is expressed in the pps argument. The
burst level range is 1 to 15 seconds, which is expressed in the seconds argument.
Rate limiting is configured on a physical port and may be applied to trusted and untrusted
ports.
Default disabled (no limit)
Format ipv6 dhcp snooping limit {rate pps [burst interval seconds]}
Mode Interface Config
no ipv6 dhcp snooping limit
Use this command to set the rate at which the DHCP Snooping messages come, and the
burst level, to the defaults.
Format no ipv6 dhcp snooping limit
Mode Interface Config
ipv6 verify source
Use this command to configure the IPv6SG source ID attribute to filter the data traffic in the
hardware. Source ID is the combination of IP address and MAC address. Normal command
allows data traffic filtration based on the IP address. With the port-security option, the
data traffic is filtered based on the IP and MAC addresses.
This command can be used to configure a single interface or a range of interfaces.
Default the source ID is the IP address
Format ipv6 verify source {port-security}
Mode Interface Config
IPv6 Commands 920
