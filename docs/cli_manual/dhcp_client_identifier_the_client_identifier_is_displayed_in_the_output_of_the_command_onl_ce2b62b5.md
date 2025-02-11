# dhcp_client_identifier_the_client_identifier_is_displayed_in_the_output_of_the_command_onl_ce2b62b5

Pages: 64-91

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
IPv6 Administrative Mode Whether enabled or disabled. Default value is enabled.
IPv6 Address/Length The IPv6 address and length. Default is Link Local format.
IPv6 Default Router TheIPv6 default router address on the service port. The factory default value is an
unspecified address.
Configured IPv4 Protocol The IPv4 network protocol being used. The options are bootp | dhcp | none.
Configured IPv6 Protocol The IPv6 network protocol being used. The options are dhcp | none.
DHCPv6 Client DUID The DHCPv6 client’s unique client identifier. This row is displayed only when the configured
IPv6 protocol is dhcp.
IPv6 Autoconfig Mode Whether IPv6 Stateless address autoconfiguration is enabled or disabled.
Burned in MAC Address The burned in MAC address used for in-band connectivity.
DHCP Client Identifier The client identifier is displayed in the output of the command only if DHCP is enabled with
the client-id option on the service port.
Command example:
The following example displays output for the service port:
(Netgear switch) #show serviceport
Interface Status............................... Up
IP Address..................................... 10.230.3.51
Subnet Mask.................................... 255.255.255.0
Default Gateway................................ 10.230.3.1
IPv6 Administrative Mode....................... Enabled
IPv6 Prefix is ................................ fe80::210:18ff:fe82:640/64
IPv6 Prefix is ................................ 2005::21/128
IPv6 Default Router is ........................ fe80::204:76ff:fe73:423a
Configured IPv4 Protocol ...................... DHCP
Configured IPv6 Protocol ...................... DHCP
DHCPv6 Client DUID ............................ 00:03:00:06:00:10:18:82:06:4C
IPv6 Autoconfig Mode........................... Disabled
Burned In MAC Address.......................... 00:10:18:82:06:4D
DHCP Client Identifier......................... 0NETGEAR-0010.1882.160C
Management Commands 64

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
IPv6 Management Commands
IPv6 management commands allow a device to be managed via an IPv6 address in a switch
or through IPv4 routing (that is, independent from the IPv6 routing package). For
Routing/IPv6 builds of the switch software, dual IPv4/IPv6 operation over the service port is
enabled. The switch software provides capabilities such as the following”
• Static assignment of IPv6 addresses and gateways for the service/network ports.
• The ability to ping an IPv6 link-local address over the service/network port.
• Using IPv6 management commands, you can send SNMP traps and queries via the
service/network port.
• The user can manage a device via the network port (in addition to a Routing Interface or
the Service port).
ipv6 management
Use this command to create an IPv6 management interface, enable IPv6 and DHCPv6 on
the management interface, and delete a previous IPv6 management interface, if there was
any. (The switch does not provide a default IPv6 management interface.)
Format ipv6 management {vlan number | port unit/slot/port} {autoconfig |
dhcp | prefix prefix-length}
Mode Global Config
no ipv6 management
Use this command to reset the IPv6 management interface to the default settings, that is,
remove the IPv6 management interface. (The switch does not provide a default IPv6
management interface.)
Format no ipv6 management
Mode Global Config
serviceport ipv6 enable
Use this command to enable IPv6 operation on the service port. By default, IPv6 operation is
enabled on the service port.
Default enabled
Format serviceport ipv6 enable
Mode Privileged EXEC
Management Commands 65

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no serviceport ipv6 enable
Use this command to disable IPv6 operation on the service port.
Format no serviceport ipv6 enable
Mode Privileged EXEC
serviceport ipv6 address
Use the options of this command to manually configure IPv6 global address, enable/disable
stateless global address autoconfiguration and to enable/disable dhcpv6 client protocol
information on the service port.
Note: Multiple IPv6 prefixes can be configured on the service port.
no serviceport ipv6 address
Use the command no serviceport ipv6 address to remove all configured IPv6
prefixes on the service port interface.
Use the command with the address option to remove the manually configured IPv6 global
address on the network port interface.
Use the command with the autoconfig option to disable the stateless global address
autoconfiguration on the service port.
Use the command with the dhcp option to disable the dhcpv6 client protocol on the service
port.
Format no serviceport ipv6 address {address/prefix-length [eui64] | autoconfig |
dhcp}
Mode Privileged EXEC
serviceport ipv6 gateway
Use this command to configure IPv6 gateway information (that is, default routers information)
for the service port.
Note: Only a single IPv6 gateway address can be configured for the service
port. There may be a combination of IPv6 prefixes and gateways that
are explicitly configured and those that are set through auto-address
configuration with a connected IPv6 router on their service port
interface.
Management Commands 66

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format serviceport ipv6 gateway gateway-address
Mode Privileged EXEC
Parameter Description
gateway-address Gateway address in IPv6 global or link-local address format.
no serviceport ipv6 gateway
Use this command to remove IPv6 gateways on the service port interface.
Format no serviceport ipv6 gateway
Mode Privileged EXEC
serviceport ipv6 neighbor
Use this command to manually add IPv6 neighbors to the IPv6 neighbor table for the service
port. If an IPv6 neighbor already exists in the neighbor table, the entry is automatically
converted to a static entry. Static entries are not modified by the neighbor discovery process.
They are, however, treated the same for IPv6 forwarding. Static IPv6 neighbor entries are
applied to the hardware when the corresponding interface is operationally active.
Format serviceport ipv6 neighbor ipv6-address macaddr
Mode Privileged EXEC
Parameter Description
ipv6-address The IPv6 address of the neighbor or interface.
macaddr The link-layer address.
no serviceport ipv6 neighbor
Use this command to remove IPv6 neighbors from the IPv6 neighbor table for the service
port.
Format no serviceport ipv6 neighbor ipv6-address macaddr
Mode Privileged EXEC
Management Commands 67

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show serviceport ipv6 neighbors
Use this command to displays information about the IPv6 neighbor entries cached on the
service port. The information is updated to show the type of the entry.
Default None
Format show serviceport ipv6 neighbors
Mode Privileged EXEC
Field Description
IPv6 Address The IPv6 address of the neighbor.
MAC Address The MAC Address of the neighbor.
isRtr Shows if the neighbor is a router. If TRUE, the neighbor is a router; if FALSE, it is not a router.
Neighbor State The state of the neighbor cache entry. The possible values are: Incomplete, Reachable, Stale,
Delay, Probe, and Unknown.
Age The time in seconds that has elapsed since an entry was added to the cache.
Type The type of neighbor entry. The type is Static if the entry is manually configured and Dynamic if
dynamically resolved.
Command example:
(NETGEAR Switch) #show serviceport ipv6 neighbors
Neighbor Age
I Pv6 Address M AC Address i sRtr S tate ( Secs) Type
- ------------------------------- - ---------------- - ---- - -------- - ----- -------
F E80::5E26:AFF:FEBD:852C 5 c:26:0a:bd:85:2c F ALSE R eachable 0 Dynamic
ping ipv6
Use this command to determine whether another computer is on the network. Ping provides
a synchronous response when initiated from the CLI and Web interfaces. To use the
command, configure the switch for network (in-band) connection. The source and target
devices must have the ping utility enabled and running on top of TCP/IP. The switch can be
pinged from any IP workstation with which the switch is connected through the default VLAN
(VLAN 1), as long as there is a physical path between the switch and the workstation. The
terminal interface sends three pings to the target station. Use the ipv6-address or
hostname parameter to ping an interface by using the global IPv6 address of the interface.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
Management Commands 68

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
You can utilize the ping or traceroute facilities over the service or network ports when using
an IPv6 global address ipv6-global-address or hostname. Any IPv6 global address or
gateway assignments to these interfaces causes IPv6 routes to be installed such that the
ping or traceroute request is routed out the service or network port properly. When
referencing an IPv6 link-local address, you must specify the interface keyword with either
the unit/slot/port argument, vlan keyword and vland-id argument, or
serviceport keyword.
Use the optional size keyword and datagram-size parameter to specify the size of the
ping packet.
Default The default count is 1.
The default interval is 3 seconds.
The default size is 0 bytes.
Format ping ipv6 {ipv6-global-address | hostname | {interface {unit/slot/port | vlan
vland-id | serviceport} link-local-address} [size datagram-size]}
Mode Privileged EXEC
User Exec
ping ipv6 interface
Use this command to determine whether another computer is on the network. To use the
command, configure the switch for network (in-band) connection. The source and target
devices must have the ping utility enabled and running on top of TCP/IP. The switch can be
pinged from any IP workstation with which the switch is connected through the default VLAN
(VLAN 1), as long as there is a physical path between the switch and the workstation. The
terminal interface sends three pings to the target station. You can use a loopback, network
port, service port, tunnel, VLAN, or physical interface as the source.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id
parameter is a number in the range of 1–4093. Use the optional size keyword and
datagram-size parameter to specify the size of the ping packet.
Format ping ipv6 interface {unit/slot/port | vlan vland-id | loopback loopback-id |
serviceport | tunnel tunnel-id} {link-local-address link-local-address |
ipv6-address} [size datagram-size]
Modes Privileged EXEC
User Exec
Management Commands 69

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Console Port Access Commands
This section describes the commands you use to configure the console port. You can use a
serial cable to connect a management host directly to the console port of the switch.
configure
This command gives you access to the Global Config mode. From the Global Config mode,
you can configure a variety of system settings, including user accounts. From the Global
Config mode, you can enter other command modes, including Line Config mode.
Format configure
Mode Privileged EXEC
line
This command gives you access to the Line Console mode, which allows you to configure
various Telnet settings and the console port, as well as to configure console login/enable
authentication.
Format line {console | telnet | ssh}
Mode Global Config
Term Definition
console Console terminal line.
telnet Virtual terminal for remote console access (Telnet).
ssh Virtual terminal for secured remote console access (SSH).
Command example:
((NETGEAR Switch)(config)#line telnet
(NETGEAR Switch)(config-telnet)#
serial baudrate
This command specifies the communication rate of the terminal interface. The supported
rates are 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200.
Default 9600
Format serial baudrate {1200 | 2400 | 4800 | 9600 | 19200 | 38400 | 57600 | 115200}
Mode Line Config
Management Commands 70

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no serial baudrate
This command sets the communication rate of the terminal interface.
Format no serial baudrate
Mode Line Config
serial timeout
This command specifies the maximum connect time (in minutes) without console activity. A
value of 0 indicates that a console can be connected indefinitely. The time range is 0 to 160.
Default 5
Format serial timeout 0-160
Mode Line Config
no serial timeout
This command sets the maximum connect time (in minutes) without console activity.
Format no serial timeout
Mode Line Config
set sup-console
This command allows access to the full CLI from any member. By default, the master is
allowed full CLI access. You can move full CLI access among the members, but at any time,
only one member can access the management CLI. You can issue the command on the
member or backup unit. After the console is transferred to the backup unit or to a member
unit, access to the full CLI on the master is disabled to avoid multiple simultaneous CLI
inputs. You can restore full access on the master by entering the command at the master
serial port.
Note: If you enter the command while the master is already allowed full CLI
access, the command does not take effect.
Format set sup-console
Mode Privileged EXEC
Management Commands 71

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show serial
This command displays serial communication settings for the switch.
Format show serial
Modes • Privileged EXEC
• User EXEC
Term Definition
Serial Port Login Timeout The time, in minutes, of inactivity on a serial port connection, after which the switch will close
(minutes) the connection. A value of 0 disables the timeout.
Baud Rate (bps) The default baud rate at which the serial port will try to connect.
Character Size (bits) The number of bits in a character. The number of bits is always 8.
Flow Control Whether Hardware Flow-Control is enabled or disabled. Hardware Flow Control is always
disabled.
Stop Bits The number of Stop bits per character. The number of Stop bits is always 1.
Parity The parity method used on the Serial Port. The Parity Method is always None.
Telnet Commands
This section describes the commands you use to configure and view Telnet settings. You can
use Telnet to manage the device from a remote management host.
ip telnet server enable
Use this command to enable Telnet connections to the system and to enable the Telnet
Server Admin Mode. This command opens the Telnet listening port.
Default enabled
Format ip telnet server enable
Mode Privileged EXEC
no ip telnet server enable
Use this command to disable Telnet access to the system and to disable the Telnet Server
Admin Mode. This command closes the Telnet listening port and disconnects all open Telnet
sessions.
Format no ip telnet server enable
Mode Privileged EXEC
Management Commands 72

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip telnet port
Use this command to configure the TCP port number on which the Telnet server detects
requests. The number argument can be a port number in the range from 1 to 65535.
Default 23
Format ip telnet port number
Mode Privileged EXEC
no ip telnet port
Use this command to reset the TCP port number on which the Telnet server detects requests
to the default of 23.
Format no ip telnet port
Mode Privileged EXEC
telnet
This command establishes a new outbound Telnet connection to a remote host. The host
must be a valid IP address or host name. Valid values for port should be a valid decimal
integer in the range of 0 to 65535, where the default value is 23. If debug is used, the current
Telnet options enabled is displayed. The optional line parameter sets the outbound Telnet
operational mode as linemode where, by default, the operational mode is character mode.
The localecho option enables local echo.
Format telnet {ip-address | hostname} port [debug] [line] [localecho]
Modes • Privileged EXEC
• User EXEC
transport input telnet
This command regulates new Telnet sessions. If enabled, new Telnet sessions can be
established until there are no more sessions available. An established session remains
active until the session is ended or an abnormal network error ends the session.
Note: If the Telnet Server Admin Mode is disabled, Telnet sessions cannot
be established. Use the ip telnet server enable command to
enable Telnet Server Admin Mode.
Default enabled
Format transport input telnet
Mode Line Config
Management Commands 73

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no transport input telnet
Use this command to prevent new Telnet sessions from being established.
Format no transport input telnet
Mode Line Config
transport output telnet
This command regulates new outbound Telnet connections. If enabled, new outbound Telnet
sessions can be established until the system reaches the maximum number of simultaneous
outbound Telnet sessions allowed. An established session remains active until the session is
ended or an abnormal network error ends it.
Default enabled
Format transport output telnet
Mode Line Config
no transport output telnet
Use this command to prevent new outbound Telnet connection from being established.
Format no transport output telnet
Mode Line Config
session-limit
This command specifies the maximum number of simultaneous outbound Telnet sessions.
The number argument can be a number in the range from 0–5. A value of 0 indicates that no
outbound Telnet session can be established.
Default 5
Format session-limit number
Mode Line Config
no session-limit
This command sets the maximum number of simultaneous outbound Telnet sessions to the
default value.
Format no session-limit
Mode Line Config
Management Commands 74

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
session-timeout (Line Config)
This command sets the Telnet session time-out value. The time-out value unit of time is
minutes and is specified by the minutes argument in the range 1–160 minutes.
Default 5
Format session-timeout minutes
Mode Line Config
no session-timeout
This command sets the Telnet session timeout value to the default. The timeout value unit of
time is minutes.
Format no session-timeout
Mode Line Config
telnetcon maxsessions
This command specifies the maximum number of Telnet connection sessions that can be
established. The number argument can be a number in the range from 0–5. A value of 0
indicates that no Telnet connection can be established.
Default 5
Format telnetcon maxsessions number
Mode Privileged EXEC
no telnetcon maxsessions
This command sets the maximum number of Telnet connection sessions that can be
established to the default value.
Format no telnetcon maxsessions
Mode Privileged EXEC
telnetcon timeout
This command sets the Telnet connection session time-out value. A session is active as long
as the session has not been idle for the value set. The time-out value unit of time is minutes
and is specified by the minutes argument in the range 1–160 minutes.
Management Commands 75

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: When you change the time-out value, the new value is applied to all
active and inactive sessions immediately. Any sessions that have
been idle longer than the new time-out value are disconnected
immediately.
Default 5
Format telnetcon timeout minutes
Mode Privileged EXEC
no telnetcon timeout
This command sets the Telnet connection session timeout value to the default.
Note: Changing the time-out value for active sessions does not become
effective until the session is accessed again. Also, any keystroke
activates the new time-out duration.
Format no telnetcon timeout
Mode Privileged EXEC
show telnet
This command displays the current outbound Telnet settings. In other words, these settings
apply to Telnet connections initiated from the switch to a remote system.
Format show telnet
Modes • Privileged EXEC
• User EXEC
Term Definition
Outbound Telnet The number of minutes an outbound Telnet session is allowed to remain inactive before being
Login Timeout logged off.
Maximum Number The number of simultaneous outbound Telnet connections allowed.
of Outbound Telnet
Sessions
Allow New Indicates whether outbound Telnet sessions will be allowed.
Outbound Telnet
Sessions
Management Commands 76

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show telnetcon
This command displays the current inbound Telnet settings. In other words, these settings
apply to Telnet connections initiated from a remote system to the switch.
Format show telnetcon
Modes • Privileged EXEC
• User EXEC
Term Definition
Remote Connection Login This object indicates the number of minutes a remote connection session is allowed to remain
Timeout (minutes) inactive before being logged off. May be specified as a number from 1 to 160. The factory
default is 5.
Maximum Number of This object indicates the number of simultaneous remote connection sessions allowed. The
Remote Connection factory default is 5.
Sessions
Allow New Telnet New Telnet sessions will not be allowed when this field is set to no. The factory default value
Sessions is yes.
Telnet Server Admin States whether the Telnet Server Admin Mode is enabled or disabled.
Mode
Telnet Server Port The port number on which the Telnet server can detect requests.
Secure Shell Commands
This section describes the commands you use to configure Secure Shell (SSH) access to the
switch. Use SSH to access the switch from a remote management host.
Note: The system allows a maximum of 5 SSH sessions.
ip ssh
Use this command to enable SSH access to the system. (This command is the short form of
the ip ssh server enable command.)
Default disabled
Format ip ssh
Mode Privileged EXEC
Management Commands 77

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip ssh port
Use this command to configure the TCP port number on which the Secure Shell (SSH) server
detects requests. The number argument can be a port number in the range from 1 to 65535.
Default 22
Format ip ssh port number
Mode Privileged EXEC
no ip ssh port
Use this command to reset the TCP port number on which the SSH server detects requests
to the default of 22.
Format no ip ssh port
Mode Privileged EXEC
ip ssh server enable
This command enables the IP secure shell server. No new SSH connections are allowed, but
the existing SSH connections continue to work until timed-out or logged-out.
Default enabled
Format ip ssh server enable
Mode Privileged EXEC
no ip ssh server enable
This command disables the IP secure shell server.
Format no ip ssh server enable
Mode Privileged EXEC
sshcon maxsessions
This command specifies the maximum number of SSH connection sessions that can be
established. The number argument can be a number in the range from 0–5. A value of 0
indicates that no ssh connection can be established. The range is 0 to 5.
Default 5
Format sshcon maxsessions number
Mode Privileged EXEC
Management Commands 78

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no sshcon maxsessions
This command sets the maximum number of allowed SSH connection sessions to the default
value.
Format no sshcon maxsessions
Mode Privileged EXEC
sshcon timeout
This command sets the SSH connection session timeout value, in minutes. A session is
active as long as the session has been idle for the value set. The time-out value unit of time
is minutes and is specified by the minutes argument in the range 1–160 minutes.
Changing the timeout value for active sessions does not become effective until the session is
re accessed. Also, any keystroke activates the new time-out duration.
Default 5
Format sshcon timeout minutes
Mode Privileged EXEC
no sshcon timeout
This command sets the SSH connection session time-out value, in minutes, to the default.
Changing the time-out value for active sessions does not become effective until the session
is re accessed. Also, any keystroke activates the new time-out duration.
Format no sshcon timeout
Mode Privileged EXEC
show ip ssh
This command displays the SSH settings.
Format show ip ssh
Mode Privileged EXEC
Term Definition
Administrative This field indicates whether the administrative mode of SSH is enabled or disabled.
Mode
Protocol Level The protocol level shows the value of version 2.
SSH Sessions The number of SSH sessions currently active.
Currently Active
Management Commands 79

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Max SSH Sessions The maximum number of SSH sessions allowed.
Allowed
SSH Timeout The SSH timeout value in minutes.
Keys Present Indicates whether the SSH RSA and DSA key files are present on the device.
Key Generation in Indicates whether RSA or DSA key files generation is currently in progress.
Progress
Management Security Commands
This section describes commands you use to generate keys and certificates, which you can
do in addition to loading them as before.
crypto certificate generate
Use this command to generate a self-signed certificate for HTTPS. The generated RSA key
for SSL has a length of 1024 bits. The resulting certificate is generated with a common name
equal to the lowest IP address of the device and a duration of 365 days.
Format crypto certificate generate
Mode Global Config
no crypto certificate generate
Use this command to delete the HTTPS certificate files from the device, regardless of
whether they are self-signed or downloaded from an outside source.
Format no crypto certificate generate
Mode Global Config
crypto key generate rsa
Use this command to generate an RSA key pair for SSH. The new key files will overwrite any
existing generated or downloaded RSA key files.
Format crypto key generate rsa
Mode Global Config
Management Commands 80

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no crypto key generate rsa
Use this command to delete the RSA key files from the device.
Format no crypto key generate rsa
Mode Global Config
crypto key generate dsa
Use this command to generate a DSA key pair for SSH. The new key files will overwrite any
existing generated or downloaded DSA key files.
Format crypto key generate dsa
Mode Global Config
no crypto key generate dsa
Use this command to delete the DSA key files from the device.
Format no crypto key generate dsa
Mode Global Config
Management Access Control List
Commands
You can use a management Access Control List (ACL) to help control access to the switch
management interface. A management ACL can help ensure that only known and trusted
devices are allowed to remotely manage the switch via TCP/IP. Management ACLs are only
configurable on IP (in-band) interfaces, not on the service port.
When a management ACL is enabled, incoming TCP packets initiating a connection (TCP
SYN) and all UDP packets are filtered based on their source IP address and destination port.
When the management ACL is disabled, incoming TCP/UDP packets are not filtered and are
processed normally.
management access-list
This command creates a management ACL. The management ACL name can be up to
32 alphanumeric characters. Executing this command enters into access-list configuration
mode, from which you must define the denied or permitted access conditions with the deny
and permit commands. If no match criteria are defined the default is to deny access (deny).
If you reenter to an access-list context, new rules are entered at the end of the access list.
Management Commands 81

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
\
Format management access list name
Mode Global Config
no management access-list
This command deletes a management ACL identified by the name parameter.
Format no management access list name
Mode Global Config
permit ip-source
This command sets permit conditions for the management access list based on the source IP
address of a packet. Optionally, you can specify a subnet mask, service type, priority, or a
combination of these for the rule. Each rule requires a unique priority. Use this command in
Management access-list configuration mode.
Format permit ip-source ip-address [mask {mask | prefix-length}] [service service]
[priority priority]
Mode Management access-list configuration
Parameter Definition
ip-address The source IP address.
mask The network mask of the source IP address.
prefix-length Specifies the number of bits that comprise the source IP address prefix. The prefix length must be
preceded by a forward slash (/).
service Indicates the service type: telnet, ssh, http, https, or snmp.
priority The priority for the rule.
permit service
This command sets permit conditions for the management access list based on the access
protocol. Each rule requires a unique priority. Use this command in Management access-list
configuration mode.
Format permit service service [priority priority]
Mode Management access-list configuration
Management Commands 82

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Definition
service Indicates the service type: telnet, ssh, http, https, or snmp.
priority The priority for the rule.
permit priority
This command assigns a permit priority to the rule. Each rule requires a unique priority. Use
this command in Management access-list configuration mode.
Format permit priority priority
Mode Management access-list configuration
deny ip-source
This command sets deny conditions for the management access list based on the source IP
address of a packet. Optionally, you can specify a subnet mask, service type, priority, or a
combination of these for the rule. Each rule requires a unique priority. Use this command in
Management access-list configuration mode.
Format deny ip-source ip-address [mask {mask | prefix-length}] [service service]
[priority priority]
Mode Management access-list configuration
Parameter Definition
ip-address The source IP address.
mask The network mask of the source IP address.
prefix-length Specifies the number of bits that comprise the source IP address prefix. The prefix length must be
preceded by a forward slash (/).
service Indicates the service type: telnet, ssh, http, https, or snmp.
priority The priority for the rule.
deny service
This command sets deny conditions for the management access list based on the access
protocol. Each rule requires a unique priority. Use this command in Management access-list
configuration mode.
Format deny service service [priority priority]
Mode Management access-list configuration
Management Commands 83

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Definition
service Indicates the service type: telnet, ssh, http, https, or snmp.
priority The priority for the rule.
deny priority
This command assigns a deny priority to the rule. Each rule requires a unique priority. Use
this command in Management access-list configuration mode.
Format deny priority priority
Mode Management access-list configuration
management access-class
This command activates the configured management ALC and restricts management
connections within the management ACL. The name parameter is the name of the existing
management ACL. You cannot update or remove a management ACL when it is active.
Format management access-class name
Mode Global Config
no management access-class
This command disables a management ACL.
Format no management access-class
Mode Global Config
show management access-list
This command displays information about the configured management ALC.
Format show management access-list [name]
Mode Privileged EXEC
Field Definition
List Name The name of the management ACL
List Admin Mode The administrative mode of the management ACL. To activate a management ACL, enter the
management access-class command (see management access-class on page84).
Packets Filtered The number of packets filtered by the management ACL
Rules The rules that are included in the ACL.
Management Commands 84

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show management access-list
List Name...................................... mgmtacl
List Admin Mode................................ Disabled
Packets Filtered............................... 0
Rules:
permit ip-source 192.168.2.10 mask 255.255.255.255 service ssh priority 1
permit ip-source 192.168.2.182 mask 255.255.255.255 service ssh priority 2
permit ip-source 192.168.2.23 mask 255.255.255.255 service ssh priority 3
NOTE: All other access is implicitly denied.
show management access-class
This command displays information about the configured management ALC.
Format show management access-class
Mode Privileged EXEC
Field Definition
List Name The name of the management ACL
List Admin Mode The administrative mode of the management ACL. To activate a management ACL, enter the
management access-class command (see management access-class on page84).
Packets Filtered The number of packets filtered by the management ACL
Command example:
(NETGEAR Switch) #show management access-class
List Name...................................... mgmtacl
List Admin Mode................................ Disabled
Packets Filtered............................... 0
Hypertext Transfer Protocol Commands
This section describes the commands you use to configure Hypertext Transfer Protocol
(HTTP) and secure HTTP access to the switch. Access to the switch by using a Web browser
is enabled by default. Everything you can view and configure by using the CLI is also
available by using the web.
Management Commands 85

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip http accounting exec, ip https accounting exec
This command applies user exec (start-stop/stop-only) accounting list to the line methods
HTTP and HTTPS.
Note: The user exec accounting list should be created using the command
aaa accounting on page123.
Format ip {http | https} accounting exec {default | listname}
Mode Global Config
Parameter Description
http or https The line method for which the list needs to be applied.
default The default list of methods for authorization services.
listname An alphanumeric character string used to name the list of accounting methods.
no ip http/https accounting exec
This command deletes the authorization method list.
Format no ip {http | https} accounting exec {default | listname}
Mode Global Config
ip http authentication
Use this command to specify authentication methods for http server users. The default
configuration is the local user database is checked. This action has the same effect as the
command ip http authentication local. The additional methods of authentication
are used only if the previous method returns an error, not if it fails. To ensure that the
authentication succeeds even if all methods return an error, specify none as the final method
in the command line.
For example, if none is specified as an authentication method after radius, no
authentication is used if the RADIUS server is down.
Default local
Format ip http authentication method1 [method2...]
Mode Global Config
Management Commands 86

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
local Uses the local username database for authentication.
none Uses no authentication.
radius Uses the list of all RADIUS servers for authentication.
tacacs Uses the list of all TACACS+ servers for authentication.
Command example:
The following example configures http authentication:
(NETGEAR Switch)(config)# ip http authentication radius local
no ip http authentication
Use this command to return to the default.
Format no ip http authentication
Mode Global Config
ip https authentication
Use this command to specify authentication methods for https server users. The default
configuration is the local user database is checked. This action has the same effect as the
command ip https authentication local. The additional methods of authentication
are used only if the previous method returns an error, not if it fails. To ensure that the
authentication succeeds even if all methods return an error, specify none as the final method
in the command line. For example, if none is specified as an authentication method after
radius, no authentication is used if the RADIUS server is down.
Default local
Format ip https authentication method1 [method2...]
Mode Global Config
Parameter Description
local Uses the local username database for authentication.
none Uses no authentication.
radius Uses the list of all RADIUS servers for authentication.
tacacs Uses the list of all TACACS+ servers for authentication.
Management Commands 87

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
The following example configures http authentication:
(NETGEAR Switch)(config)# ip https authentication radius local
no ip https authentication
Use this command to return to the default.
Format no ip https authentication
Mode Global Config
ip http server
This command enables access to the switch through the Web interface. When access is
enabled, the user can login to the switch from the Web interface. When access is disabled,
the user cannot login to the switch's Web server. Disabling the Web interface takes effect
immediately. All interfaces are affected.
Default enabled
Format ip http server
Mode Privileged EXEC
no ip http server
This command disables access to the switch through the Web interface. When access is
disabled, the user cannot login to the switch's Web server.
Format no ip http server
Mode Privileged EXEC
ip http secure-server
This command is used to enable the secure socket layer for secure HTTP.
Default disabled
Format ip http secure-server
Mode Privileged EXEC
Management Commands 88

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip http secure-server
This command is used to disable the secure socket layer for secure HTTP.
Format no ip http secure-server
Mode Privileged EXEC
ip http port
Use this command to configure the TCP port number on which the HTTP server detects
requests. The number argument can be a port number in the range from 1 to 65535.
Default 80
Format ip http port number
Mode Privileged EXEC
no ip http port
Use this command to reset the TCP port number on which the HTTP server detects requests
to the default of 80.
Format no ip http port
Mode Privileged EXEC
ip http session hard-timeout
This command configures the hard time-out for unsecure HTTP sessions. The time-out value
unit of time is hours and is specified by the hours argument in the range 1–168 hours.
Configuring this value to zero will give an infinite hard-time-out. When this time-out expires,
the user will be forced to reauthenticate. This timer begins on initiation of the web session
and is unaffected by the activity level of the connection.
Default 24
Format ip http session hard-timeout hours
Mode Privileged EXEC
no ip http session hard-timeout
This command restores the hard time-out for un-secure HTTP sessions to the default value.
Format no ip http session hard-timeout
Mode Privileged EXEC
Management Commands 89

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip http session maxsessions
This command limits the number of allowable unsecure HTTP sessions. The number
argument specifies the number of sessions in the range of 0–16. Zero is the configurable
minimum.
Default 16
Format ip http session maxsessions number
Mode Privileged EXEC
no ip http session maxsessions
This command restores the number of allowable un-secure HTTP sessions to the default
value.
Format no ip http session maxsessions
Mode Privileged EXEC
ip http session soft-timeout
This command configures the soft time-out for un-secure HTTP sessions. The time-out value
unit of time is minutes and is specified by the minutes argument in the range 1–60 minutes.
Configuring this value to zero will give an infinite soft-time-out. When this time-out expires the
user will be forced to reauthenticate. This timer begins on initiation of the Web session and is
restarted with each access to the switch.
Default 5
Format ip http session soft-timeout minutes
Mode Privileged EXEC
no ip http session soft-timeout
This command resets the soft time-out for un-secure HTTP sessions to the default value.
Format no ip http session soft-timeout
Mode Privileged EXEC
ip http secure-session hard-timeout
This command configures the hard time-out for secure HTTP sessions. The time-out value
unit of time is hours and is specified by the hours argument in the range 1–168 hours. When
this time-out expires, the user is forced to reauthenticate. This timer begins on initiation of the
Web session and is unaffected by the activity level of the connection. The secure-session
hard-time-out can not be set to zero (infinite).
Management Commands 90

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default 24
Format ip http secure-session hard-timeout hours
Mode Privileged EXEC
no ip http secure-session hard-timeout
This command resets the hard time-out for secure HTTP sessions to the default value.
Format no ip http secure-session hard-timeout
Mode Privileged EXEC
ip http secure-session maxsessions
This command limits the number of secure HTTP sessions. The number argument specifies
the number of sessions in the range of 0–16. Zero is the configurable minimum.
Default 16
Format ip http secure-session maxsessions number
Mode Privileged EXEC
no ip http secure-session maxsessions
This command restores the number of allowable secure HTTP sessions to the default value.
Format no ip http secure-session maxsessions
Mode Privileged EXEC
ip http secure-session soft-timeout
This command configures the soft time-out for secure HTTP sessions. The time-out value
unit of time is minutes and is specified by the minutes argument in the range 1–60 minutes.
Configuring this value to zero will give an infinite soft-time-out. When this time-out expires,
you are forced to reauthenticate. This timer begins on initiation of the Web session and is
restarted with each access to the switch. The secure-session soft-time-out can not be set to
zero (infinite).
Default 5
Format ip http secure-session soft-timeout minutes
Mode Privileged EXEC
Management Commands 91
