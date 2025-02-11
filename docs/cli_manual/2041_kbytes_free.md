# 2041 Kbytes free.

Pages: 59-144

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
do (Privileged EXEC commands)
This command executes Privileged EXEC mode commands from any of the configuration
modes.
Format do Priv Exec Mode Command
Mode • Global Config
• Interface Config
• VLAN Config
• Routing Config
Command example:
The following is an example of the do command that executes the Privileged Exec command
script list in Global Config Mode.
(NETGEAR Switch) #configure
(NETGEAR Switch)(config)#do script list
Configuration Script Name Size(Bytes)
-------------------------------- -----------
backup-config 2105
running-config 4483
startup-config 445
3 configuration script(s) found.
2041 Kbytes free.
ip management
Use this command to create an IPv4 management interface, enable DHCP on the IPv4
management interface, delete a previous IPv4 management interface, and set the source
interface for all applications, including RADIUS, TACACS, DNS, SNTP, SNMP, and SysLog.
Default vlan 1
Format ip management {vlan number | port unit/slot/port} {dhcp | ipaddr
{prefix-length | subnet-mask}}
Mode Global Config
Management Commands 59

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip management source-interface
Use this command to specify the source IP address for all applications, including RADIUS,
TACACS, DNS, SNTP, SNMP, and SysLog.
For the loopback keyword, you can enter a number between 0 and 7.
Default vlan 1
Format ip management source-interface {serviceport | vlan number | port
unit/slot/port | loopback number}
Mode Global Config
no ip management
Use this command to reset the IPv4 management interface to the default settings.
Format no ip management
Mode Global Config
serviceport ip
This command sets the IP address, the netmask, and the gateway of the network
management port. You can specify the none option to clear the IPv4 address and mask and
the default gateway (that is, reset each of these values to 0.0.0.0).
Format serviceport ip {ipaddr netmask [gateway] | none}
Mode Privileged EXEC
serviceport protocol
This command specifies the network management port configuration protocol. If you modify
this value, the change is effective immediately. If you use the bootp parameter, the switch
periodically sends requests to a BootP server until a response is received. If you use the dhcp
parameter, the switch periodically sends requests to a DHCP server until a response is
received. If you use the none parameter, you must configure the network information for the
switch manually.
Format serviceport protocol {none | bootp | dhcp}
Mode Privileged EXEC
Management Commands 60

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
serviceport protocol dhcp
This command enables the DHCPv4 client on a Service port. If the client-id optional
parameter is given, the DHCP client messages are sent with the client identifier option.
Default none
Format serviceport protocol dhcp [client-id]
Mode Privileged Exec
There is no support for the no form of the command serviceport protocol dhcp
client-id. To remove the client-id option from the DHCP client messages, issue the
command serviceport protocol dhcp without the client-id option. The command
serviceport protocol none can be used to disable the DHCP client and client-id
option on the interface.
Command example:
(NETGEAR Switch) # serviceport protocol dhcp client-id
mac management address
This command sets locally administered MAC addresses. The following rules apply:
• Bit 6 of byte 0 (called the U/L bit) indicates whether the address is universally
administered (b'0') or locally administered (b'1').
• Bit 7 of byte 0 (called the I/G bit) indicates whether the destination address is an
individual address (b'0') or a group address (b'1').
• The second character, of the twelve character macaddr, must be 2, 6, A or E.
A locally administered address must have bit 6 On (b'1') and bit 7 Off (b'0').
Format mac management address macaddr
Mode Privileged EXEC
mac management type
This command specifies whether the switch uses the burned in MAC address or the
locally-administered MAC address.
Default burnedin
Format mac management type {local | burnedin}
Mode Privileged EXEC
Management Commands 61

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no network mac-type
This command resets the value of MAC address to its default.
Format no mac management type
Mode Privileged EXEC
show ip management
This command displays configuration settings that are associated with the switch
management interface. The management interface is the logical interface that is used for
in-band connectivity with the switch over any of the switch front panel ports. The
configuration parameters that are associated with the switch management interface do not
affect the configuration of the front panel ports through which traffic is switched or routed. The
management interface is always considered to be up, whether or not any member ports are
up. Therefore, the output of the show ip management command always shows interface
status as up.
Format show ip management
Modes • Privileged EXEC
• User EXEC
Term Definition
Interface Status The management interface status; it is always considered to be up.
IP Address The IP address of the interface. The factory default value is 0.0.0.0.
Subnet Mask The IP subnet mask for this interface. The factory default value is 0.0.0.0.
Default Gateway The default gateway for this IP interface. The factory default value is 0.0.0.0.
IPv6 Administrative Mode Whether enabled or disabled.
IPv6 Address/Length The IPv6 address and length.
IPv6 Default Router The IPv6 default router address.
Burned In MAC Address The burned- in MAC address used for in-band connectivity.
Locally Administered MAC You can configure a locally administered MAC address for in-band connectivity. This
Address configuration requires the following:
• The MAC Address Type must be set to Locally Administered.
• Enter the address as 12 hexadecimal digits (6 bytes) with a colon between bytes.
• Bit 1 of byte 0 must be set to a 1 and bit 0 to a 0. That is, byte 0 must contain the
xxxx xx10 mask.
• The MAC address must be unique.
We recommend that you use the MAC address that is the numerically smallest MAC
address of all ports that belong to the bridge. When concatenated with dot1dStpPriority,
a unique Bridge Identifier is formed, which is used in the Spanning Tree Protocol.
Management Commands 62

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
MAC Address Type The MAC address that must be used for in-band connectivity. The choices are the
burned in or the Locally Administered address. The factory default is to use the burned
in MAC address.
DHCPv6 Client DUID The DHCPv6 client’s unique client identifier. This row is displayed only when the
configured IPv6 protocol is DHCP.
IPv6 Autoconfig Mode Whether IPv6 Stateless address autoconfiguration is enabled or disabled.
DHCP Client Identifier The client identifier is displayed in the output of the command only if DHCP is enabled
with the client-id option on the management interface.
Command example:
(NETGEAR Switch) #show ip management
IPv4 Interface Status.......................... Up
IPv4 Management Interface...................... vlan 1
IP Address..................................... 169.254.100.100
Subnet Mask.................................... 255.255.255.0
Method......................................... DHCP
Routing Mode................................... Enable
Default Gateway................................ 0.0.0.0
Source Interface............................... vlan 1
Burned In MAC Address.......................... DC:EF:09:D3:2D:48
Locally Administered MAC address............... 00:00:00:00:00:00
MAC Address Type............................... Burned In
IPv6 Management Interface is not Configured.
show serviceport
This command displays service port configuration information.
Format show serviceport
Mode • Privileged EXEC
• User EXEC
Term Definition
Interface Status The network interface status. It is always considered to be up.
IP Address The IP address of the interface. The factory default value is 0.0.0.0.
Subnet Mask The IP subnet mask for this interface. The factory default value is 0.0.0.0.
Default Gateway The default gateway for this IP interface. The factory default value is 0.0.0.0.
Management Commands 63

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

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip http secure-session soft-timeout
This command restores the soft time-out for secure HTTP sessions to the default value.
Format no ip http secure-session soft-timeout
Mode Privileged EXEC
ip http secure-port
This command is used to set the SSL port where port can be 1025-65535 and the default is
port 443.
Default 443
Format ip http secure-port portid
Mode Privileged EXEC
no ip http secure-port
This command is used to reset the SSL port to the default value.
Format no ip http secure-port
Mode Privileged EXEC
show ip http
This command displays the http settings for the switch.
Format show ip http
Mode Privileged EXEC
Term Definition
HTTP Mode (Unsecure) The insecure HTTP server administrative mode.
HTTP Port The insecure HTTP server port number
Maximum Allowable HTTP The number of allowable un-secure http sessions.
Sessions
HTTP Session Hard Timeout The hard time-out for insecure http sessions in hours.
HTTP Session Soft Timeout The soft time-out for insecure http sessions in minutes.
HTTP Mode (Secure) The secure HTTP server administrative mode.
Secure Port The secure HTTP server port number.
Secure Protocol Level(s) The protocol level can be SSL3 or TSL 1.2.
Management Commands 92

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Maximum Allowable HTTPS The number of allowable secure http sessions.
Sessions
HTTPS Session Hard The hard time-out for secure http sessions in hours.
Timeout
HTTPS Session Soft The soft time-out for secure http sessions in minutes.
Timeout
Certificate Present Indicates if the secure-server certificate files are present on the switch.
Certificate Generation in Indicates if certificate generation is in progress.
Progress
Access Commands
Use the commands in this section to close remote connections or to view information about
connections to the system.
disconnect
Use the disconnect command to close HTTP, HTTPS, Telnet or SSH sessions. Use all to
close all active sessions, or use session-id to specify the session ID to close. To view the
possible values for session-id, use the show loginsession command.
Format disconnect {session_id | all}
Mode Privileged EXEC
show loginsession
This command displays current Telnet, SSH and serial port connections to the switch. This
command displays truncated user names. Use the show loginsession long command
to display the complete usernames.
Format show loginsession
Mode Privileged EXEC
Term Definition
ID Login Session ID.
User Name The name the user entered to log on to the system.
Connection From IP address of the remote client machine or EIA-232 for the serial port connection.
Idle Time Time this session has been idle.
Management Commands 93

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Session Time Total time this session has been connected.
Session Type Shows the type of session, which can be HTTP, HTTPS, telnet, serial, or SSH.
show loginsession long
This command displays the complete user names of the users currently logged in to the
switch.
Format show loginsession long
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show loginsession long
User Name
------------
admin
test1111test1111test1111test1111test1111test1111test1111test1111
User Account Commands
This section describes the commands you use to add, manage, and delete switch users. The
switch provides two default users: admin and guest. The admin user can view and configure
the switch settings. The guest user can view the switch settings only.
The first time that you log in as an admin user, no password is required (that is, the password
is blank). As of software version 12.0.9.3, after you log in for the first time, you are required to
specify a new password that you must use each subsequent time that you log in. After you
specify the new password, you are logged out and then must log in again, using your new
password.
The default guest user cannot log in until the admin user specifies a password for the guest
user.
You cannot reset the new password to the default password. For example, if you enter the
username admin nopassword command or clear password command, the password
is not reset to the default password.
However, if you enter the clear-config command, the passwords for the default admin
user and default guest user are reset to defaults. In such a situation, the admin user must
again specify a new password after logging in for the first time. Similarly, the admin user must
again specify a password for the default guest user.
Management Commands 94

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: You cannot delete the admin user, which is the only user with
read/write privileges on the switch. You can configure up to five
read-only users (that is, guest users) on the switch.
aaa authentication login
Note: In software version 12.0.11.8 and later software versions, a user with
privilege level 1 cannot enter in Privilege Exec Mode and cannot
execute Privilege Exec commands.
Use this command to set authentication at login. The default and optional list names created
with the command are used with the aaa authentication login command. Create a list
by entering the aaa authentication login list-name method command, where
list-name is any character string used to name this list. The method argument identifies
the list of methods that the authentication algorithm tries, in the given sequence.
The additional methods of authentication are used only if the previous method returns an
error, not if there is an authentication failure. To ensure that the authentication succeeds
even if all methods return an error, specify none as the final method in the command line.
For example, if none is specified as an authentication method after radius, no
authentication is used if the RADIUS server is down.
If you configure local as the first method in the list, the switch tries no other methods.
Default • defaultList. Used by the console and only contains the method none.
• networkList. Used by telnet and SSH and only contains the method local.
Format aaa authentication login {default | list-name} method1 [method2...]
Mode Global Config
Parameter Definition
default Uses the listed authentication methods that follow this argument as the default list of methods when
a user logs in.
list-name Character string of up to 15 characters used to name the list of authentication methods activated
when a user logs in.
method1... At least one from the following:
[method2...] • enable. Uses the enable password for authentication.
• line. Uses the line password for authentication.
• local. Uses the local username database for authentication.
• none. Uses no authentication.
• radius. Uses the list of all RADIUS servers for authentication.
• tacacs. Uses the list of all TACACS servers for authentication.
Management Commands 95

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch)(config)# aaa authentication login default radius local enable none
no aaa authentication login
This command returns to the default.
Format aaa authentication login {default | list-name}
Mode Global Config
aaa authentication enable
Use this command to set authentication for accessing higher privilege levels. The default
enable list is enableList. It is used by console, and contains the method as enable
followed by none.
A separate default enable list, enableNetList, is used for Telnet and SSH users instead of
enableList. This list is applied by default for Telnet and SSH, and contains enable
followed by deny methods. By default, the enable password is not configured. That means
that, by default, Telnet and SSH users will not get access to Privileged EXEC mode. On the
other hand, with default conditions, a console user always enter the Privileged EXEC mode
without entering the enable password.
The default and optional list names created with the aaa authentication enable
command are used with the enable authentication command. Create a list by entering
the aaa authentication enable list-name method command where list-name
is any character string used to name this list. The method argument identifies the list of
methods that the authentication algorithm tries in the given sequence.
The user manager returns ERROR (not PASS or FAIL) for enable and line methods if no
password is configured, and moves to the next configured method in the authentication list.
The method none reflects that there is no authentication needed.
The user will only be prompted for an enable password if one is required. The following
authentication methods do not require passwords:
• none
• deny
• enable (if no enable password is configured)
• line (if no line password is configured)
See the examples below.
1. aaa authentication enable default enable none
2. aaa authentication enable default line none
3. aaa authentication enable default enable radius none
4. aaa authentication enable default line tacacs none
Management Commands 96

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Examples 1 and 2 do not prompt for a password, however because examples 3 and 4
contain the radius and tacacs methods, the password prompt is displayed.
If the login methods include only enable, and there is no enable password configured, the
switch does not prompt for a user name. In such cases, the switch prompts only for a
password. The switch supports configuring methods after the local method in authentication
and authorization lists. If the user is not present in the local database, then the next
configured method is tried.
The additional methods of authentication are used only if the previous method returns an
error, not if it fails. To ensure that the authentication succeeds even if all methods return an
error, specify none as the final method in the command line.
Use the command show authorization methods on page101 to display information about
the authentication methods.
Note: Requests sent by the switch to a RADIUS or TACACS server include
the username $enabx$, in which x is the requested privilege level.
The login user ID is also sent to a TACACS+ server.
Default default
Format aaa authentication enable {default | list-name} method1 [method2...]
Mode Global Config
Parameter Description
default Uses the listed authentication methods that follow this argument as the default list of methods, when
using higher privilege levels.
list-name Character string used to name the list of authentication methods activated, when using access
higher privilege levels. Range: 1-15 characters.
method1 Specify at least one from the following:
[method2...] • deny. Used to deny access.
• enable. Uses the enable password for authentication.
• line. Uses the line password for authentication.
• none. Uses no authentication.
• radius. Uses the list of all RADIUS servers for authentication.
• tacacs. Uses the list of all TACACS+ servers for authentication.
Command example:
The following example sets authentication to access higher privilege levels:
(NETGEAR Switch)(config)# aaa authentication enable default enable
Management Commands 97

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no aaa authentication enable
Use this command to return to the default configuration.
Format no aaa authentication enable {default | list-name}
Mode Global Config
aaa authorization
Use this command to configure command and exec authorization method lists. This list is
identified by default or a user-specified list-name. If tacacs is specified as the
authorization method, authorization commands are notified to a TACACS+ server. If none is
specified as the authorization method, command authorization is not applicable. A maximum
of five authorization method lists can be created for the commands type.
Note: The local method is not supported for command authorization.
Command authorization with RADIUS functions only if the applied
authentication method is also RADIUS.
Format aaa authorization {exec | commands} {default | list-name} method1
[method2…]
Mode Global Config
Term Definition
exec Provides authorization for user EXEC terminal sessions.
commands Provides authorization for all user-executed commands.
default The default list of methods for authorization services.
list-name Character string used to name the list of authorization methods.
method1 [method2…] Use either tacacs or radius for authorization purpose.
no aaa authorization
This command deletes the authorization method list.
Format no aaa authorization {exec | commands} {default | <list-name>}
<method1> [<method2>…]
Mode Global Config
Management Commands 98

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Per-Command Authorization
When authorization is configured for a line mode, the user manager sends information about
an entered command to the AAA server. The AAA server validates the received command,
and responds with either a PASS or FAIL response. If approved, the command is executed.
Otherwise, the command is denied and an error message is shown to the user. The various
utility commands such as tftp, ping, and outbound telnet should also pass command
authorization. Applying the script is treated as a single command apply script, which also
goes through authorization. Startup-config commands applied on device boot-up are not an
object of the authorization process.
The per-command authorization usage scenario is this:
1. Configure Authorization Method List
aaa authorization commands listname tacacs radius none
2. Apply AML to an Access Line Mode (console, telnet, SSH)
authorization commands listname
3. Commands entered by the user will go through command authorization via TACACS+ or
RADIUS server and will be accepted or denied.
Exec Authorization
When exec authorization is configured for a line mode, the user may not be required to use
the enable command to enter Privileged EXEC mode. If the authorization response indicates
that the user has sufficient privilege levels for Privileged EXEC mode, then the user bypasses
User EXEC mode entirely.
The exec authorization usage scenario is as follows:
1. Configure Authorization Method List
aaa authorization exec listname method1 [method2....]
2. Apply AML to an Access Line Mode (console, telnet, SSH)
authorization exec listname
3. When the user logs in, in addition to authentication, authorization will be performed to
determine if the user is allowed direct access to Privileged EXEC mode.
Format aaa authorization {commands | exec} {default | list-name} method1 [method2]
Mode Global Config
Parameter Description
commands Provides authorization for all user-executed commands.
exec Provides exec authorization.
default The default list of methods for authorization services.
Management Commands 99

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
list-name Alphanumeric character string used to name the list of authorization methods.
method TACACS+, RADIUS, Local, and none are supported.
(NETGEAR Switch) #
(NETGEAR Switch) #configure
(NETGEAR Switch) (Config)#aaa authorization exec default tacacs+ none
(NETGEAR Switch) (Config)#aaa authorization commands default tacacs+ none
no aaa authorization
This command deletes the authorization method list.
Format no aaa authorization {commands | exec} {default | list-name}
Mode Global Config
authorization commands
This command applies a command authorization method list to an access method (console,
telnet, ssh). For usage scenarios on per command authorization, see the command aaa
authorization on page98.
Format authorization commands [default | list-name]
Mode Line console, Line telnet, Line SSH
Parameter Description
commands This causes command authorization for each command execution attempt.
no authorization commands
This command removes command authorization from a line config mode.
Format no authorization {commands | exec}
Mode Line console, Line telnet, Line SSH
Command example:
(NETGEAR Switch) (Config)#line console
(NETGEAR Switch) (Config-line)#authorization commands list2
(NETGEAR Switch) (Config-line)#
(NETGEAR Switch) (Config-line)#exit
Management Commands 100

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
authorization exec
This command applies a command authorization method list to an access method so that the
user may not be required to use the enable command to enter Privileged EXEC mode. For
usage scenarios on exec authorization, see the command aaa authorization on page98.
Format authorization exec list-name
Mode Line console, Line telnet, Line SSH
Parameter Description
list-name The command authorization method list.
no authorization exec
This command removes command authorization from a line config mode.
Format no authorization exec
Mode Line console, Line telnet, Line SSH
authorization exec default
This command applies a default command authorization method list to an access method so
that the user may not be required to use the enable command to enter Privileged EXEC
mode. For usage scenarios on exec authorization, see the command aaa authorization on
p age98.
Format authorization exec default
Mode Line console, Line telnet, Line SSH
no authorization exec default
This command removes command authorization from a line config mode.
Format no authorization exec default
Mode Line console, Line telnet, Line SSH
show authorization methods
This command displays the configured authorization method lists.
Format show authorization methods
Mode Privileged EXEC
Management Commands 101

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show authorization methods
Command Authorization List Method
- ------------------------- --------------------------------------
d fltCmdAuthList tacacs none
l ist2 none undefined
l ist4 tacacs undefined
L ine Command Method List
------------ ------------------------------
C onsole dfltCmdAuthList
Telnet dfltCmdAuthList
SSH dfltCmdAuthList
Exec Authorization List Method
- ---------------------- --------------------------------------
d fltExecAuthList tacacs none
l ist2 none undefined
l ist4 tacacs undefined
L ine Exec Method List
------------ ------------------------------
Console dfltExecAuthList
Telnet dfltExecAuthList
S SH dfltExecAuthList
enable authentication
Use this command to specify the authentication method list when accessing a higher
privilege level from a remote telnet or console.
Format enable authentication {default | list-name}
Mode Line Config
Parameter Description
default Uses the default list created with the aaa authentication enable command.
list-name Uses the indicated list created with the aaa authentication enable command.
Command example:
The following example specifies the default authentication method to access a higher
privilege level console:
(NETGEAR Switch)(config)# line console
Management Commands 102

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
(NETGEAR Switch)(config-line)# enable authentication default
no enable authentication
Use this command to return to the default specified by the enable authentication command.
Format no enable authentication
Mode Line Config
username (Global Config, with an encrypted password entered)
Use the username command in Global Config mode to add a new user with an encrypted
password to the local user database.
For a new user, the default (privilege) level is 1.
Using the encrypted keyword allows you to transfer local user passwords between devices
without knowing the passwords.
If you use the password parameter with the encrypted parameter, the password must be
exactly 128 hexadecimal characters in length. If the password strength feature is enabled,
this command checks for password strength and returns an appropriate error if it fails to meet
the password strength criteria.
The optional parameter override-complexity-check disables the validation of the
password strength.
Note: In software version 12.0.11.8 and later software versions, when you
configure a user password, the password does not display in clear text
but encrypted.
Format username name {password password [encryption-type encryption-type]
[encrypted [override-complexity-check] | level level [encrypted [override-
complexity-check]] | override-complexity-check]} | {level level [override-
complexity-check] password [encryption-type encryption-type]}
Mode Global Config
Parameter Description
name The name of the user. The range is from 1 to 32 characters.
password T he authentication password for the user ranges from 8 to 64characters. The
password must be entered in encrypted format (it cannot be plain text).
The special characters allowed in the password include the following:
! # $ % & ' ( ) * + , - . / : ; < = > @ [ \ ] ^ _ ` { | } ~.
The password length can be zero if the no passwords min-length command is
executed.
encryption-type The encryption algorithm type, which can be SHA-512 (the default) or SHA-256.
Management Commands 103

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
encrypted Specifies that the password that is entered or copied from another switch configuration
is already encrypted, and is shown in the configuration as it is without any further
encryption.
override-complexity-check Disables the validation of the password strength.
level The user level. Level 0 can be assigned by a level 15 user to another user to suspend
that user’s access. Range 0-15. Enter access level 1 for Read Access or 15 for Read/
Write Access. In a situation in which the level is optional and you do not specify it, the
level is set to 1.
Command example:
The following example configures a password for the user “bob” with encryption type
SHA-512, (privilege) level 1, and the encrypted keyword set:
(NETGEAR Switch)(Config)#username "bob" password
$6$p6eTphdakQA88tjm$Hwg72k7wbEc0d6z7DioCNa9ezCqEOI1BiheodqFOktx.WRJeasjDm3D5M.x4Z4DIvBE
drWFBc/l2i6hiWYz.30 encryption-type sha512 level 1 encrypted
Command example:
The following example configures a password for the user “tom” with encryption type
SHA-512, (privilege) level 1, and both the encrypted keyword and
override-complexity-check keyword set:
(NETGEAR Switch)(Config)#username "tom" password
$6$p6eTphdakQA88tjm$Hwg72k7wbEc0d6z7DioCNa9ezCqEOI1BiheodqFOktx.WRJeasjDm3D5M.x4Z4DIvBE
drWFBc/l2i6hiWYz.30 encryption-type sha512 level 1 encrypted override-complexity-check
username (Global Config, with a plain text password entered)
Use the username command in Global Config mode to add a new user to the local user
database, allowing the user to enter a password in plain text. The password is displayed as a
series of asterisks (*).
For a new user, the default (privilege) level is 1.
The optional parameter override-complexity-check disables the validation of the
password strength.
Note: In software version 12.0.11.8 and later software versions, when you
configure a user password, the password does not display in clear text
but encrypted.
Management Commands 104

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format username name {[[encryption-type encryption-type] password | override-
complexity-check password | level level [password | override-complexity-check
password]] | override-complexity-check password}
Mode Global Config
Parameter Description
name The name of the user. The range is from 1 to 32 characters.
encryption-type The encryption algorithm type, which can be SHA-512 (the default) or SHA-256.
password Indicates that the user must enter a plain text password.
T his password must range from 8 to 64characters. Even though the password is
entered in plain text, the password is shown as a series of asterisks (*).
The special characters allowed in the password include the following:
! # $ % & ' ( ) * + , - . / : ; < = > @ [ \ ] ^ _ ` { | } ~.
The password length can be zero if the no passwords min-length command is
executed.
override-complexity-check Disables the validation of the password strength.
level The user level. Level 0 can be assigned by a level 15 user to another user to suspend
that user’s access. Range 0-15. Enter access level 1 for Read Access or 15 for Read/
Write Access. In a situation in which the level is optional and you do not specify it, the
level is set to 1.
Command example:
The following example configures a password for the user “bob” with (privilege) level 15:
(NETGEAR Switch)(Config)#username bob level 15 password
Enter new password:*********
Confirm new password:*********
Command example:
The following example configures a password for the user “test123” with (privilege) level 15,
and the encryption set to SHA-512:
(NETGEAR Switch)(Config)#username test123 level 15 password encryption-type sha512
Enter new password:********
Confirm new password:********
Command example:
The following example configures a password for the user “test1234” with the
override-complexity-check password keyword set:
(NETGEAR Switch)(Config)#username test1234 override-complexity-check password
Management Commands 105

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Enter new password:********
Confirm new password:********
no username
Use this command to remove a user name.
Format no username name
Mode Global Config
username name nopassword
Use this command to remove an existing user’s password (NULL password).
Format username name nopassword [level level]
Mode Global Config
Parameter Description
name The name of the user. Range: 1-32 characters.
password The authentication password for the user. Range 8-64 characters.
level The user level. Level 0 can be assigned by a level 15 user to another user to suspend that user’s
access. Range 0-15.
username name unlock
Use this command to allows a locked user account to be unlocked. Only a user with
read/write access can reactivate a locked user account.
Format username name unlock
Mode Global Config
username snmpv3 accessmode
This command specifies the snmpv3 access privileges for the specified login user. The valid
access mode values are readonly and readwrite. The username is the login user name
for which the specified access mode applies. The default is readwrite for the admin user
and readonly for all other users. You must enter the username in the same case you used
when you added the user. To see the case of the user name, enter the show users
command.
Management Commands 106

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Defaults • admin - readwrite
• other - readonly
Format username snmpv3 accessmode username {readonly | readwrite}
Mode Global Config
no username snmpv3 accessmode
This command sets the snmpv3 access privileges for the specified user as readwrite for
the admin user and readonly for all other users. The username value is the user name for
which the specified access mode will apply.
Format no username snmpv3 accessmode username
Mode Global Config
username snmpv3 authentication
This command specifies the authentication protocol to be used for the specified user. The
valid authentication protocols are none, md5 or sha. If you specify md5 or sha, the login
password is also used as the SNMPv3 authentication password and therefore must be at
least eight characters in length. The username is the user name associated with the
authentication protocol. You must enter the username in the same case you used when you
added the user. To see the case of the user name, enter the show users command.
Default no authentication
Format username snmpv3 authentication username {none | md5 | sha}
Mode Global Config
no username snmpv3 authentication
This command sets the authentication protocol to be used for the specified user to none. The
username is the user name for which the specified authentication protocol is used.
Format no username snmpv3 authentication username
Mode Global Config
username snmpv3 encryption
This command specifies the encryption protocol used for the specified user. The valid
encryption protocols are des or none.
If you select des, you can specify the required key on the command line. The encryption key
must be 8 to 64 characters long. If you select the des protocol but do not provide a key, the
user is prompted for the key. When you use the des protocol, the login password is also used
Management Commands 107

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
as the snmpv3 encryption password, so it must be a minimum of eight characters. If you
select none, you do not need to provide a key.
The username value is the login user name associated with the specified encryption. You
must enter the username in the same case you used when you added the user. To see the
case of the user name, enter the show users command.
Default no encryption
Format username snmpv3 encryption username {none | des [key]}
Mode Global Config
no username snmpv3 encryption
This command sets the encryption protocol to none. The username is the login user name
for which the specified encryption protocol will be used.
Format no username snmpv3 encryption username
Mode Global Config
username snmpv3 encryption encrypted
This command specifies the des encryption protocol and the required encryption key for the
specified user. The encryption key must be 8 to 64 characters long.
Default no encryption
Format username snmpv3 encryption encrypted username des key
Mode Global Config
show users
This command displays the configured user names and their settings. The show users
command displays truncated user names. Use the show users long command to display
the complete usernames. The show users command is only available for users with
read/write privileges. The SNMPv3 fields are displayed only if SNMP is available on the
system.
Format show users
Mode Privileged EXEC
Term Definition
User Name The name the user enters to login using the serial port, Telnet or Web.
Access Mode Shows whether the user is able to change parameters on the switch (Read/Write) or is only
able to view them (Read Only). As a factory default, the “admin” user has Read/Write
access and the “guest” has Read Only access.
Management Commands 108

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
SNMPv3 Access Mode The SNMPv3 Access Mode. If the value is set to ReadWrite, the SNMPv3 user is able to
set and retrieve parameters on the system. If the value is set to ReadOnly, the SNMPv3
user is only able to retrieve parameter information. The SNMPv3 access mode may be
different than the CLI and Web access mode.
SNMPv3 Authentication The authentication protocol to be used for the specified login user.
SNMPv3 Encryption The encryption protocol to be used for the specified login user.
show users long
This command displays the complete user names of the configured users on the switch.
Format show users long
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show users long
User Name
------------
admin
guest
test1111test1111test1111test1111
show users accounts
This command displays the local user status with respect to user account lockout and
password aging.This command displays truncated user names. Use the show users long
command to display the complete user names.
Format show users accounts [detail]
Mode Privileged EXEC
Term Definition
User Name The local user account’s user name.
Access Level The user’s access level (1 for read-only or 15 for read/write).
Password Aging Number of days, since the password was configured, until the password expires.
Password Expiry The current password expiration date in date format.
Date
Lockout Indicates whether the user account is locked out (true or false).
Management Commands 109

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If the detail keyword is included, the following additional fields display.
Term Definition
Password Override Displays the user's Password override complexity check status. By default it is disabled.
Complexity Check
Password Strength Displays the user password's strength (Strong or Weak). This field is displayed only if the
Password Strength feature is enabled.
Command example:
The following example displays information about the local user database.
(NETGEAR Switch)#show users accounts
UserName Privilege Password Password Lockout
Aging Expiry date
------------------- --------- -------- ------------ -------
admin 15 --- --- False
guest 1 --- --- False
console#show users accounts detail
UserName....................................... admin
Privilege...................................... 15
Password Aging................................. ---
Password Expiry................................ ---
Lockout........................................ False
Override Complexity Check...................... Disable
Password Strength.............................. ---
UserName....................................... guest
Privilege...................................... 1
Password Aging................................. ---
Password Expiry................................ ---
Lockout........................................ False
Override Complexity Check...................... Disable
Password Strength.............................. ---
show users login-history [long]
Use this command to display information about the login history of users.
Format show users login-history [long]
Mode Privileged EXEC
Management Commands 110

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show users login-history [username]
Use this command to display information about the login history of users.
Format show users login-history [username name]
Mode Privileged EXEC
Parameter Description
name Name of the user. Range: 1-20 characters.
Command example:
The following example shows user login history outputs:
Console>show users login-history
L ogin Time U sername P rotocol Location
- ------------------- - -------- - -------- ---------------
J an 19 2005 08:23:48 B ob Serial
J an 19 2005 08:29:29 R obert H TTP 172.16.0.8
J an 19 2005 08:42:31 J ohn S SH 172.16.0.1
J an 19 2005 08:49:52 B etty T elnet 172.16.1.7
login authentication
Use this command to specify the login authentication method list for a line (console, telnet, or
SSH). The default configuration uses the default set with the command aaa
authentication login.
Format login authentication {default | list-name}
Mode Line Configuration
Parameter Description
default Uses the default list created with the aaa authentication login command.
list-name Uses the indicated list created with the aaa authentication login command.
Command example:
The following example specifies the default authentication method for a console:
(NETGEAR Switch) (config)# line console
(NETGEAR Switch) (config-line)# login authentication default
Management Commands 111

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no login authentication
Use this command to return to the default specified by the authentication login
command.
Format no login authentication {default | list-name}
Mode Line Configuration
password (Line Configuration)
Use the password command in Line Configuration mode to specify a password on a line, or
allow it to be copied from a script file or configuration file. The default configuration is that no
password is specified.
Script files or configuration files with password commands that include plain text passwords
do not work.
Format password [encryption-type encryption-type] | password [encryption-type
encryption-type] [encrypted]]
Mode Line Config
Parameter Definition
password The password in encrypted format.
encrypted The password that is entered or copied from another switch configuration is already encrypted. For
SHA-256 salted hash, the password must be 63 characters in length. For SHA-512 salted hash (the
default), the password must be 106 characters in length.
encryption-type The encryption algorithm type, which can be SHA-512 (the default) or SHA-256.
Command example:
The following example configures a plain text password with the SHA-256 encryption type on
a line:
(NETGEAR Switch)(Config-line)#password encryption-type sha256
Enter new password:********
Confirm new password:********
Command example:
The following example configures a plain text password with the SHA-512 encryption type on
a line:
(NETGEAR Switch)(Config-line)#password encryption-type sha512
Enter new password:********
Confirm new password:********
Management Commands 112

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
The following example configures an encrypted password with the SHA-256 encryption type
on a line:
(NETGEAR Switch)(Config-line)#password
$5$8XLN8qHQLKvx61X8$vsIiv0ZqnesHqX/F5yeche4laH4B9WChxyRh5b3vGPB encryption-type sha256
encrypted
Command example:
The following example configures an encrypted password with the SHA-512 encryption type
on a line:
(NETGEAR Switch)(Config-line)#password
$6$iiOcwxwa96ZKoa1F$P6NjilVODkH5suf8ic90gj2FJ34EgiK1skJGt3nLevA6C6HJSBxNVOgtz.4DktM/SmE
NiIGFzqkdvhBgX8EGF/ encryption-type sha512 encrypted
no password (Line Configuration)
Use this command to remove the password on a line.
Format no password
Mode Line Config
password (User EXEC)
This command allow a user to change the password. The user must enter this command
after the password has aged. The user is prompted to enter the old password and the new
password.
Format password
Mode User EXEC
Command example:
The following example shows the prompt sequence for executing the password command:
(NETGEAR Switch)>password
Enter old password:********
Enter new password:********
Confirm new password:********
enable password (Privileged EXEC)
Use the enable password configuration command to set a local password to control
access to the privileged EXEC mode.
Script files or configuration files with password commands that include plain text passwords
do not work.
Management Commands 113

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: In software version 12.0.11.8 and later software versions, when you
configure a user password, the password does not display in clear text.
Format enable password [encryption-type encryption-type] | [password [encryp-
tion-type encryption-type] [encrypted]]
Mode Privileged EXEC
Parameter Description
encryption-type The encryption algorithm type, which can be SHA-512 (the default) or SHA-256.
password The password in encrypted format.
encrypted The password that is entered or copied from another switch configuration is already encrypted.
For SHA-256 salted hash, the password must be 63 characters in length. For SHA-512 salted
hash (the default), the password must be 106 characters in length.
Command example:
The following example configures a plain text password with the SHA-256 encryption type:
(NETGEAR Switch)#enable password encryption-type sha256
Enter old password:********
Enter new password:********
Confirm new password:********
Command example:
The following example configures a plain text password with the SHA-512 encryption type:
(NETGEAR Switch)#enable password encryption-type sha512
Enter old password:********
Enter new password:********
Confirm new password:********
Command example:
The following example configures an encrypted password with the SHA-256 encryption:
(NETGEAR Switch)#enable password
$5$8XLN8qHQLKvx61X8$vsIiv0ZqnesHqX/F5yeche4laH4B9WChxyRh5b3vGPB encryption-type sha256
encrypted
Command example:
The following example configures an encrypted password with the SHA-512 encryption type:
(NETGEAR Switch)#enable password
$6$Zhe76BxSM7ZOh8/.$.acXOoNVZMbXJuG/L7Ilcfd5iLHL7dd8Gt79bpQacL6UBSdD4GvEudGgP/eaT/wW.Xu
wT3j0o9qKFgLhGZoXz/ encryption-type sha512 encrypted
Management Commands 114

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no enable password (Privileged EXEC)
Use the no enable password command to remove the password requirement.
Format no enable password
Mode Privileged EXEC
passwords min-length
Use this command to enforce a minimum password length for local users. The value also
applies to the enable password. The length argument is a number in the range 8–64.
Default 8
Format passwords min-length length
Mode Global Config
no passwords min-length
Use this command to set the minimum password length to the default value.
Format no passwords min-length
Mode Global Config
passwords history
Use this command to set the number of previous passwords that can be stored for each user
account. When a local user changes his or her password, the user is not be able to reuse any
password stored in password history. This ensures that users do not reuse their passwords
often. The number argument is a number in the range 0–10.
Default 0
Format passwords history number
Mode Global Config
no passwords history
Use this command to set the password history to the default value.
Format no passwords history
Mode Global Config
Management Commands 115

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
passwords aging
Use this command to implement aging on passwords for local users. When a user’s
password expires, the user is prompted to change it before logging in again. The days
argument is a number in the range 1–365 days. The default is 0, or no aging.
Default 0
Format passwords aging days
Mode Global Config
no passwords aging
Use this command to set the password aging to the default value.
Format no passwords aging
Mode Global Config
passwords lock-out
Use this command to strengthen the security of the switch by locking user accounts that have
failed login due to wrong passwords. When a lockout count is configured, a user that is
logged in must enter the correct password within that count. Otherwise the user will be locked
out from further switch access. Only a user with read/write access can reactivate a locked
user account. Password lockout does not apply to logins from the serial console. The
number argument is a number in the range 1–5. The default is 0, or no lockout count
enforced.
Default 0
Format passwords lock-out number
Mode Global Config
no passwords lock-out
Use this command to set the password lock-out count to the default value.
Format no passwords lock-out
Mode Global Config
Management Commands 116

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
passwords strength-check
Use this command to enable the password strength feature. It is used to verify the strength of
a password during configuration.
Default Disable
Format passwords strength-check
Mode Global Config
no passwords strength-check
Use this command to set the password strength checking to the default value.
Format no passwords strength-check
Mode Global Config
passwords strength maximum consecutive-characters
Use this command to set the maximum number of consecutive characters to be used in
password strength. The number argument is a number in the range 0–15. The default is 0.
Minimum of 0 means no restriction on that set of characters.
Default 0
Format passwords strength maximum consecutive-characters number
Mode Global Config
passwords strength maximum repeated-characters
Use this command to set the maximum number of repeated characters to be used in
password strength. The number argument is a number in the range 0–15. The default is 0.
Minimum of 0 means no restriction on that set of characters.
Default 0
Format passwords strength maximum repeated-characters number
Mode Global Config
passwords strength minimum uppercase-letters
Use this command to enforce a minimum number of uppercase letters that a password
should contain. The number argument is a number in the range 0–16. The default is 2.
Minimum of 0 means no restriction on that set of characters.
Management Commands 117

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default 2
Format passwords strength minimum uppercase-letters number
Mode Global Config
no passwords strength minimum uppercase-letters
Use this command to reset the minimum uppercase letters required in a password to the
default value.
Format no passwords minimum uppercase-letter
Mode Global Config
passwords strength minimum lowercase-letters
Use this command to enforce a minimum number of lowercase letters that a password should
contain. The number argument is a number in the range 0–16. The default is 2. Minimum of
0 means no restriction on that set of characters.
Default 2
Format passwords strength minimum lowercase-letters number
Mode Global Config
no passwords strength minimum lowercase-letters
Use this command to reset the minimum lower letters required in a password to the default
value.
Format no passwords minimum lowercase-letter
Mode Global Config
passwords strength minimum numeric-characters
Use this command to enforce a minimum number of numeric characters that a password
should contain. The number argument is a number in the range 0–16. T The default is 2.
Minimum of 0 means no restriction on that set of characters.
Default 2
Format passwords strength minimum numeric-characters number
Mode Global Config
Management Commands 118

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no passwords strength minimum numeric-characters
Use this command to reset the minimum numeric characters required in a password to the
default value.
Format no passwords minimum numeric-characters
Mode Global Config
passwords strength minimum special-characters
Use this command to enforce a minimum number of special characters that a password
should contain. The number argument is a number in the range 0–16. The default is 2.
Minimum of 0 means no restriction on that set of characters.
Default 2
Format passwords strength minimum special-characters number
Mode Global Config
no passwords strength minimum special-characters
Use this command to reset the minimum special characters required in a password to the
default value.
Format no passwords minimum special-characters
Mode Global Config
passwords strength minimum character-classes
Use this command to enforce a minimum number of characters classes that a password
should contain. Character classes are uppercase letters, lowercase letters, numeric
characters and special characters. The number argument is a number in the range 0–4. The
default is 4.
Default 4
Format passwords strength minimum character-classes number
Mode Global Config
Management Commands 119

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no passwords strength minimum character-classes
Use this command to reset the minimum number of character classes required in a password
to the default value.
Format no passwords minimum character-classes
Mode Global Config
passwords strength exclude-keyword
Use this command to exclude the specified keyword while configuring the password. The
password does not accept the keyword in any form (in between the string, case in-sensitive
and reverse) as a substring. You can configure up to a maximum of three keywords.
Format passwords strength exclude-keyword keyword
Mode Global Config
no passwords strength exclude-keyword
Use this command to reset the restriction for the specified keyword or all the keywords
configured.
Format no passwords exclude-keyword [keyword]
Mode Global Config
passwords unlock timer
Use this command to configure the time after which a locked user account is unlocked (that
is, the unlock time) and password authentication can be attempted again. By default, the
period for the minutes argument is 5 minutes and the range is from 1 to 60 minutes.
Default 5
Format passwords unlock timer minutes
Mode Global Config
no passwords unlock timer
Use this command to reset the unlock time to the default time.
Format no passwords unlock timer
Mode Global Config
Management Commands 120

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
passwords unlock timer mode
Use this command to configure the password unlock timer mode. If the user account is
locked, the timer mode is enabled (which it is by default), and the unlock time expires, the
user account is unlocked. If the timer mode is disabled and the unlock time expires, the user
account remains locked.
Default Enabled
Format passwords unlock timer mode {enabled | disabled}
Mode Global Config
no passwords unlock timer mode
Use this command to reset the unlock timer mode to its default.
Format no passwords unlock timer mode
Mode Global Config
show passwords configuration
Use this command to display the configured password management settings.
Format show passwords configuration
Mode Privileged EXEC
Term Definition
Minimum Password Length The minimum number of characters that the password must include.
Password Aging (day) The length in days that a password is valid.
Password History The number of passwords to store for reuse prevention.
Lockout Attempts The number of failed password login attempts allowed before lockout occurs.
Password Strength Check Indicates if the password strength check is enabled.
Minimum Password The minimum number of uppercase characters that the password must include.
Uppercase Letters
Minimum Password The minimum number of lowercase characters that the password must include.
Lowercase Letters
Minimum Password Numeric The minimum number of numeric characters that the password must include.
Characters
Minimum Password Special The minimum number of special characters that the password must include.
Characters
Maximum Password The maximum number of repeated characters that the password can include.
Repeated Characters
Management Commands 121

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Maximum Password The maximum number of consecutive repeated characters that the password can include.
Consecutive Characters
Minimum Password The minimum number of character classes (uppercase, lowercase, numeric and special)
Character Classes that the password must include.
Password Exclude-Keywords The set of keywords to be excluded from the configured password when strength checking
is enabled.
Unlock Timer Mode Indicates if the unlock timer mode is enabled.
Unlock Time (mins) The time after which a locked user account is unlocked
show passwords result
Use this command to display the last password set result information.
Format show passwords result
Mode Privileged EXEC
Term Definition
Last User Whose Password Shows the name of the user with the most recently set password.
Is Set
Password Strength Check Shows whether password strength checking is enabled.
Last Password Set Result Shows whether the attempt to set a password was successful. If the attempt failed, the
reason for the failure is included.
aaa ias-user username
The Internal Authentication Server (IAS) database is a dedicated internal database used for
local authentication of users for network access through the IEEE 802.1X feature.
Use the aaa ias-user username command in Global Config mode to add the specified
user to the internal user database. This command also changes the mode to AAA User
Config mode.
Format aaa ias-user username user
Mode Global Config
no aaa ias-user username
Use this command to remove the specified user from the internal user database.
Format no aaa ias-user username user
Mode Global Config
Management Commands 122

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #
(NETGEAR Switch) #configure
(NETGEAR Switch) (Config)#aaa ias-user username client-1
((NETGEAR Switch)(Config-aaa-ias-User)#exit
(NETGEAR Switch) (Config)#no aaa ias-user username client-1
(NETGEAR Switch) (Config)#
aaa session-id
Use this command in Global Config mode to specify if the same session-id is used for
Authentication, Authorization and Accounting service type within a session.
Default common
Format aaa session-id [common | unique]
Mode Global Config
Parameter Description
common Use the same session-id for all AAA Service types.
unique Use a unique session-id for all AAA Service types.
no aaa session-id
Use this command in Global Config mode to reset the aaa session-id behavior to the default.
Format no aaa session-id [unique]
Mode Global Config
aaa accounting
Use this command in Global Config mode to create an accounting method list for user EXEC
sessions, user-executed commands, or DOT1X. This list is identified by the default
keyword or by a user-specified list-name. Accounting records, when enabled for a
line-mode, can be sent at both the beginning and at the end (start-stop) or only at the end
(stop-only). If none is specified, accounting is disabled for the specified list. If tacacs is
specified as the accounting method, accounting records are notified to a TACACS+ server. If
radius is the specified accounting method, accounting records are notified to a RADIUS
server.
Note the following:
• A maximum of five Accounting Method lists can be created for each exec and commands
type.
• Only the default Accounting Method list can be created for DOT1X. There is no provision
to create more.
Management Commands 123

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
• The same list-name can be used for both exec and commands accounting type
• AAA Accounting for commands with RADIUS as the accounting method is not supported.
• Start-stop or None are the only supported record types for DOT1X accounting. Start-stop
enables accounting and None disables accounting.
• RADIUS is the only accounting method type supported for DOT1X accounting.
Format aaa accounting {exec | commands | dot1x} {default | list-name} {start-stop |
stop-only |none} method1 [method2…]
Mode Global Config
Parameter Description
exec Provides accounting for a user EXEC terminal sessions.
commands Provides accounting for all user executed commands.
dot1x Provides accounting for DOT1X user commands.
default The default list of methods for accounting services.
list-name Character string used to name the list of accounting methods.
start-stop Sends a start accounting notice at the beginning of a process and a stop accounting notice at the
beginning of a process and a stop accounting notice at the end of a process.
stop-only Sends a stop accounting notice at the end of the requested user process.
none Disables accounting services on this line.
method Use either TACACS or radius server for accounting purposes.
Command example:
(NETGEAR Switch) #
(NETGEAR Switch) #configure
(NETGEAR Switch) #aaa accounting commands default stop-only tacacs
(NETGEAR Switch) #aaa accounting exec default start-stop radius
(NETGEAR Switch) #aaa accounting dot1x default start-stop radius
(NETGEAR Switch) #aaa accounting dot1x default none
(NETGEAR Switch) #exit
Command example:
For the same set of accounting type and list name, the administrator can change the record
type, or the methods list, without having to first delete the previous configuration:
(NETGEAR Switch) #
(NETGEAR Switch) #configure
(NETGEAR Switch) #aaa accounting exec ExecList stop-only tacacs
(NETGEAR Switch) #aaa accounting exec ExecList start-stop tacacs
(NETGEAR Switch) #aaa accounting exec ExecList start-stop tacacs radius
Management Commands 124

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The first aaa command creates a method list for exec sessions with the name ExecList,
with record-type as stop-only and the method as tacacs. The second command changes
the record type from stop-only to start-stop for the same method list. The third
command, for the same list changes the methods list from tacacs to tacacs,radius.
no aaa accounting
This command deletes the accounting method list.
Format no aaa accounting {exec | commands | dot1x} {default | list-name}
Mode Global Config
Command example:
(NETGEAR Switch) #
(NETGEAR Switch) #configure
(NETGEAR Switch) #aaa accounting commands userCmdAudit stop-only tacacs radius
(NETGEAR Switch) #no aaa accounting commands userCmdAudit
(NETGEAR Switch) #exit
password (AAA IAS User Config)
Use this command to specify a password for a user in the IAS database. An optional
parameter encrypted is provided to indicate that the password given to the command is
already preencrypted.
Format password password [encrypted]
Mode AAA IAS User Config
Parameter Definition
password Password for this level. Range: 8-64 characters
encrypted Encrypted password to be entered, copied from another switch configuration.
Command example:
(NETGEAR Switch) #
(NETGEAR Switch) #configure
(NETGEAR Switch) (Config)#aaa ias-user username client-1
(NETGEAR Switch) (Config-aaa-ias-User)#password client123
(NETGEAR Switch) (Config-aaa-ias-User)#no password
Command example:
The following is an example of adding a MAB Client to the Internal user database:
(NETGEAR Switch) #
(NETGEAR Switch) #configure
Management Commands 125

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
(NETGEAR Switch) (Config)#aaa ias-user username 1f3ccb1157
(NETGEAR Switch) (Config-aaa-ias-User)#password 1f3ccb1157
(NETGEAR Switch) (Config-aaa-ias-User)#exit
(NETGEAR Switch) (Config)#
no password (AAA IAS User Config)
Use this command to clear the password of a user.
Format no password
Mode AAA IAS User Config
clear aaa ias-users
Use this command to remove all users from the IAS database.
Format clear aaa ias-users
Mode Privileged Exec
Command example:
(NETGEAR Switch) #clear aaa ias-users
show aaa ias-users
Use this command to display configured IAS users and their attributes. Passwords
configured are not shown in the show command output.
Format show aaa ias-users [username]
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show aaa ias-users
UserName
-------------------
Client-1
Client-2
Following are the IAS configuration commands shown in the output of show
running-config command. Passwords shown in the command output are always
encrypted.
aaa ias-user username client-1
password a45c74fdf50a558a2b5cf05573cd633bac2c6c598d54497ad4c46104918f2c encrypted
exit
Management Commands 126

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
accounting
Use this command in Line Configuration mode to apply the accounting method list to a line
config (console/telnet/ssh).
Format accounting {exec | commands} {default | list-name}
Mode Line Configuration
Parameter Description
exec Causes accounting for an EXEC session.
commands This causes accounting for each command execution attempt. If a user is enabling accounting for
exec mode for the current line-configuration type, the user will be logged out.
default The default Accounting List
listname Enter a string of not more than 15 characters.
Command example:
(NETGEAR Switch) #
(NETGEAR Switch) #configure
(NETGEAR Switch) (Config)#line telnet
(NETGEAR Switch)(Config-line)# accounting exec default
(NETGEAR Switch) #exit
no accounting
Use this command to remove accounting from a Line Configuration mode.
Format no accounting {exec | commands]
Mode Line Configuration
show accounting
Use this command to display ordered methods for accounting lists.
Format show accounting
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show accounting
Number of Accounting Notifications sent at beginning of an EXEC session: 0
Errors when sending Accounting Notifications beginning of an EXEC session: 0
Number of Accounting Notifications at end of an EXEC session: 0
Errors when sending Accounting Notifications at end of an EXEC session: 0
Number of Accounting Notifications sent at beginning of a command execution: 0
Management Commands 127

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Errors when sending Accounting Notifications at beginning of a command execution: 0
Number of Accounting Notifications sent at end of a command execution: 0
Errors when sending Accounting Notifications at end of a command execution: 0
show accounting methods
Use this command to display configured accounting method lists.
Format show accounting methods
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #
(NETGEAR Switch) #show accounting methods
Acct Type Method Name Record Type Method Type
---------- ------------ ------------ ------------
Exec dfltExecList start-stop TACACS
Commands dfltCmdsList stop-only TACACS
Commands U serCmdAudit s tart-stop TACACS
D OT1X d fltDot1xList start-stop radius
Line EXEC Method List Command Method List
------- ---------------------------------------
Console dfltExecList dfltCmdsList
Telnet dfltExecList dfltCmdsList
SSH dfltExecList UserCmdAudit
clear accounting statistics
This command clears the accounting statistics.
Format clear accounting statistics
Mode Privileged Exec
show domain-name
This command displays the configured domain-name.
Format show domain-name
Mode Privileged Exec
Management Commands 128

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #
(NETGEAR Switch) #show domain-name
Domain : Enable
Domain-name :abc
SNMP Commands
This section describes the commands that you can use to configure Simple Network
Management Protocol (SNMP) on the switch. You can configure the switch to act as an
SNMP agent so that it can communicate with SNMP managers on your network.
snmp-server
This command sets the name and the physical location of the switch and the organization
responsible for the network. The range for the name, loc and con parameters is from 1 to 31
alphanumeric characters.
Default none
Format snmp-server {sysname name | location loc | contact con}
Mode Global Config
snmp-server community
This command adds (and names) a new SNMP community. A community name is associated
with the switch and with a set of SNMP managers that manage the community with a
specified privileged level. The length of the name parameter can be up to 16 case-sensitive
characters.
Note: Community names in the SNMP Community table must be unique. If
multiple entries are made using the same community name, the first
entry is kept and processed and all duplicate entries are ignored.
Format snmp-server community name
Mode Global Config
Management Commands 129

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no snmp-server community
This command removed a community name from the table. The name parameter is the
community name that must be deleted.
Format no snmp-server community name
Mode Global Config
snmp-server community ipaddr
This command sets a client IP address for an SNMP community. The SNMP community
sends SNMP packets from this address. The address along with the client IP mask value
denotes a range of IP addresses from which SNMP clients can use the community to access
the device. A value of 0.0.0.0 allows access from any IP address. Otherwise, this value is
ANDed with the mask to determine the range of allowed client IP addresses. The name is the
applicable community name.
Default 0.0.0.0
Format snmp-server community ipaddr ipaddr name
Mode Global Config
no snmp-server community ipaddr
This command sets a client IP address for an SNMP community to 0.0.0.0. The name is the
applicable community name.
Format no snmp-server community ipaddr name
Mode Global Config
snmp-server community ipmask
This command sets a client IP mask for an SNMP community. The SNMP community sends
SNMP packets from an address with this client IP mask. The address along with the client IP
mask value denotes a range of IP addresses from which SNMP clients can use the
community to access the device. A value of 255.255.255.255 allows access from only one
computer and specifies that computer’s IP address as the client IP address. A value of
0.0.0.0 allows access from any IP address. The name is the applicable community name.
Default 0.0.0.0
Format snmp-server community ipmask ipmask name
Mode Global Config
Management Commands 130

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no snmp-server community ipmask
This command sets a client IP mask for an SNMP community to 0.0.0.0. The name is the
applicable community name.
Format no snmp-server community ipmask name
Mode Global Config
snmp-server community mode
This command activates an SNMP community. If a community is enabled, an SNMP
manager that is associated with this community manages the switch according to its access
right. If the community is disabled, no SNMP requests using this community are accepted. In
this case, the SNMP manager that is associated with this community cannot manage the
switch until the status is changed back to enabled.
Default • private and public communities - enabled
• other four - disabled
Format snmp-server community mode name
Mode Global Config
no snmp-server community mode
This command deactivates an SNMP community. If the community is disabled, no SNMP
requests using this community are accepted. In this case, the SNMP manager that is
associated with this community cannot manage the switch until the status is changed back to
enabled.
Format no snmp-server community mode name
Mode Global Config
snmp-server community ro
This command restricts access to switch information. The access mode is read-only (also
called public).
Format snmp-server community ro name
Mode Global Config
Management Commands 131

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
snmp-server community rw
This command restricts access to switch information. The access mode is read/write (also
called private).
Format snmp-server community rw name
Mode Global Config
snmp-server user
This command creates an SNMPv3 user that can access the switch.
Default No default user
Format snmp-server user username groupname [remote engineid-string] [auth-sha512
authentication-password| auth-sha512-key sha512-key] {[priv-aes128 encryp-
tion-password| priv-aes128-key aes128-key]}
Mode Global Config
Parameter Description
username The name (from 1 to 30 characters) of the SNMPv3 user.
groupname The group name (from 1 to 30 characters) of which the SNMPv3 user is a member.
engineid-string The engine-id (from 6 to 32 characters) of the remote management station that this user will be
connecting from.
auth-sha512 Indicates that you must enter a password on the basis of which the switch can generate an SHA-512
key for authentication.
authentication- The actual password (from 1 to 32 characters) that lets the switch automatically generate an SHA-512
password key for authentication.
auth-sha512-key Indicates that you must enter (or copy) the SHA-512 key for authentication.
sha512-key The actual SHA-512 key for authentication. The key can be up to 128 characters. If you do not enter a
key, the switch automatically generates a key.
priv-aes128 Indicates that you must enter a password on the basis of which the switch can generate an AES-128
HMAC-MD5-96 key for encryption.
encryption- The actual password (from 1 to 32 characters) that lets the switch automatically generate an AES-128
password HMAC-MD5-96 key for encryption.
priv-aes128-key Indicates that you must enter (or copy) the AES-128 HMAC-MD5-96 key for encryption.
aes128-key The actual AES-128 HMAC-MD5-96 key for encryption. The key can be up to 128 characters. If you do
not enter a key, the switch automatically generates a key.
Management Commands 132

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch)(Config)#snmp-server user test grp1 auth-sha512 priv-aes128
Enter Authentication Password:********
Confirm Authentication Password:********
Enter Encryption Password:********
Confirm Encryption Password:********
Command example:
(NETGEAR Switch)(Config)#snmp-server user test DefaultWrite auth-sha512-key
6991313bb623241c8f6f967fa28dff0265b4b57dfd07301be41024a791df01f412d1ad8bd8cde6ae6d66da7
61987657afe36efd788d021012564cf8ed2718351 priv-aes128-key
6991313bb623241c8f6f967fa28dff0265b4b57dfd07301be41024a791df01f412d1ad8bd8cde6ae6d66da7
61987657afe36efd788d021012564cf8ed2718351
no snmp-server user
This command removes an SNMPv3 user.
Format no snmp-server user username
Mode Global Config
snmp-server enable traps violation
This command enables the switch to send violation traps. The switch sends a violation trap if
it receives a packet with a disallowed MAC address on a locked port.
Note: For information about port security commands, see Protected Ports
Commands on page451.
Default disabled
Format snmp-server enable traps violation
Mode Interface Config
no snmp-server enable traps violation
This command prevents the switch from sending violation traps.
Format no snmp-server enable traps violation
Mode Interface Config
Management Commands 133

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
snmp-server enable traps
This command enables the Authentication Flag.
Default enabled
Format snmp-server enable traps
Mode Global Config
no snmp-server enable traps
This command disables the Authentication Flag.
Format no snmp-server enable traps
Mode Global Config
snmp-server enable traps linkmode
This command enables Link Up/Down traps for the entire switch. If enabled, the switch sends
link traps only if the Link Trap flag setting that is associated with a port is enabled. For more
information, see snmp trap link-status on page138
Default enabled
Format snmp-server enable traps linkmode
Mode Global Config
no snmp-server enable traps linkmode
This command disables Link Up/Down traps for the entire switch.
Format no snmp-server enable traps linkmode
Mode Global Config
snmp-server enable traps multiusers
This command enables multiple user traps. If the traps are enabled, the switch sends a
multiple user trap if a user logs in to the terminal interface (EIA 232 or Telnet) while an
existing terminal interface session is already established.
Default enabled
Format snmp-server enable traps multiusers
Mode Global Config
Management Commands 134

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no snmp-server enable traps multiusers
This command disables multiple user traps.
Format no snmp-server enable traps multiusers
Mode Global Config
snmp-server enable traps stpmode
This command enables the switch to send new root traps and topology change notification
traps.
Default enabled
Format snmp-server enable traps stpmode
Mode Global Config
no snmp-server enable traps stpmode
This command prevents the switch from sending new root traps and topology change
notification traps.
Format no snmp-server enable traps stpmode
Mode Global Config
snmp-server port
This command modifies the port that the switch uses to detect SNMP messages. By default,
the switch uses UDP port 161 to detect SNMP messages.
Default 161
Format snmp-server port number
Mode User EXEC
no snmp-server port
This command resets the port that the switch uses to detect SNMP messages. After you
enter this command, the switch uses UDP port 161 to detect SNMP messages.
Format no snmp-server port
Mode User EXEC
Management Commands 135

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
snmp-server trapsend
Use this command to set the UDP port to which traps are sent by the SNMP server.
Default 50505
Format snmp-server trapsend number
Mode Global Config
no snmp-server trapsend
Use this command to reset the UDP port to which traps are sent by the SNMP server to the
default port of 50505.
Format no snmp-server trapsend
Mode Global Config
snmptrap
This command adds an SNMP trap receiver. The snmpversion parameter is the version of
SNMP. The version parameter option can be snmpv1 or snmpv2. You can set the SNMP trap
address as an IPv4 or IPv6 global address.
The name parameter does not need to be unique, however; the combination of name and
ipaddr or ip6addr must be unique. Multiple entries can exist with the same name as long
as they are associated with a different ipaddr or ip6addr. The reverse scenario is also
acceptable. The name is the community name used when sending the trap to the receiver,
but the name is not directly associated with the SNMP Community table (see snmp-server
community on page129).
Default snmpv2
Format snmptrap name {ipaddr ipaddr | ip6addr ip6addr} [snmpversion snmpversion]
Mode Global Config
Command example:
(NETGEAR Switch)# snmptrap mytrap ip6addr 3099::2
no snmptrap
This command delete trap receivers for a community.
Format no snmptrap name {ipaddr ipaddr | ip6addr ip6addr}
Mode Global Config
Management Commands 136

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
snmptrap snmpversion
This command modifies the SNMP version of a trap. The maximum length of the name
parameter is 16 case-sensitive alphanumeric characters. The snmpversion parameter
options are snmpv1 or snmpv2.
Note: This command does not support a no form.
Default snmpv2
Format snmptrap snmpversion name {ipaddr | ip6addr} {snmpv1 | snmpv2}
Mode Global Config
snmptrap ipaddr
This command assigns a new IP address or host name to a community name. The name can
use up to 16 case-sensitive alphanumeric characters.
Note: IP addresses in the SNMP trap receiver table must be unique. If you
make multiple entries using the same IP address, the first entry is
retained and processed. All duplicate entries are ignored.
Format snmptrap ipaddr name ipaddrold ipaddrnew
Mode Global Config
snmptrap mode
This command activates an SNMP trap. Enabled trap receivers are active (that is, able to
receive traps).
Format snmptrap mode name {ipaddr | ip6addr}
Mode Global Config
no snmptrap mode
This command deactivates an SNMP trap. Disabled trap receivers are inactive (that is, not
able to receive traps).
Format no snmptrap mode name {ipaddr | ip6addr}
Mode Global Config
Management Commands 137

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
snmptrap source-interface
This command configures the global source interface (that is, the source IP address) for all
SNMP communication between the SNMP client and the server.
Format snmptrap source-interface {unit/slot/port | loopback loopback-id | tunnel
tunnel-id | vlan vlan-id}
Mode Global Config
Parameter Description
unit/slot/port The unit identifier that is assigned to the switch.
loopback-id The loopback interface that you want to use as the source IP address. The range of the loopback ID is
from 0 to 7.
tunnel-id The tunnel interface that you want to use as the source IP address. The range of the tunnel ID is from
0 to 7.
vlan-id The VLAN interface that you want to use as the source IP address. The range of the VLAN ID is from
1 to 4093.
no snmptrap source-interface
This command removes the global source interface for all SNMP communication between
the SNMP client and the server.
Format no snmptrap source-interface
Mode Global Config
snmp trap link-status
This command enables link status traps for an interface or for all interfaces.
Format snmp trap link-status
Mode Interface Config
no snmp trap link-status
This command disables link status traps for an interface.
Format no snmp trap link-status
Mode Interface Config
Management Commands 138

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
snmp trap link-status all
This command enables link status traps for all interfaces.
Format snmp trap link-status all
Mode Global Config
no snmp trap link-status
This command disables link status traps for all interfaces.
Format no snmp trap link-status all
Mode Global Config
show snmp-server
This command shows the UDP port to which the SNMP server is connected and on which the
switch sends SNMP traps.
Format show snmp-server
Mode User EXEC
Command example:
(NETGEAR Switch)#show snmp-server
SNMP Server Port............................... 161
SNMP Trap Send Port............................ 162
show snmpcommunity
This command displays SNMP community information. Six communities are supported. You
can add, change, or delete communities. You do not need to reset the switch for changes to
take effect.
The SNMP agent of the switch complies with SNMP Versions 1, 2, and 3. For more
information about the SNMP specification, see the SNMP RFCs. The SNMP agent sends
traps through TCP/IP to an external SNMP manager based on the SNMP configuration (the
trap receiver and other SNMP community parameters).
Format show snmpcommunity
Mode Privileged EXEC
Management Commands 139

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
SNMP The community string to which this entry grants access. A valid entry is a case-sensitive alphanumeric
Community string of up to 16 characters. Each row of this table must contain a unique community name.
Name
Client IP An IP address (or portion thereof) from which this device will accept SNMP packets with the
Address associated community. The requesting entity's IP address is ANDed with the Subnet Mask before
being compared to the IP address. Note: If the Subnet Mask is set to 0.0.0.0, an IP address of 0.0.0.0
matches all IP addresses. The default value is 0.0.0.0.
Client IP Mask A mask to be ANDed with the requesting entity's IP address before comparison with IP address. If the
result matches with IP address then the address is an authenticated IP address. For example, if the IP
address = 9.47.128.0 and the corresponding Subnet Mask = 255.255.255.0 a range of incoming IP
addresses would match, i.e. the incoming IP address could equal 9.47.128.0 - 9.47.128.255. The
default value is 0.0.0.0.
Access Mode The access level for this community string.
Status The status of this community access entry.
show snmptrap
This command displays SNMP trap receivers. Trap messages are sent across a network to
an SNMP network manager. These messages alert the manager to events occurring within
the switch or on the network. Six trap receivers are simultaneously supported.
Format show snmptrap
Mode Privileged EXEC
Term Definition
SNMP Trap The community string of the SNMP trap packet sent to the trap manager. The string is case-sensitive
Name and can be up to 16 alphanumeric characters.
IP Address The IPv4 address to receive SNMP traps from this device.
IPv6 Address The IPv6 address to receive SNMP traps from this device.
SNMP Version SNMPv2
Status The receiver's status (enabled or disabled).
Command example:
(NETGEAR Switch)#show snmptrap
Community Name IpAddress IPv6 Address Snmp Version Mode
M ytrap 0 .0.0.0 2 001::1 S NMPv2 Enable show trapflags
Management Commands 140

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show trapflags
This command displays the trap conditions. The command output shows all enabled trap
flags, including OSPFv2 and OSPFv3 trap flags.
Note: You can configure which traps the switch must generate by enabling
or disabling the trap condition. If a trap condition is enabled and the
condition is detected, the SNMP agent on the switch sends the trap to
all enabled trap receivers. Cold and warm start traps are always
generated and cannot be disabled.
Format show trapflags
Mode Privileged EXEC
Term Definition
Authentication Flag Can be enabled or disabled. The factory default is enabled. Indicates whether authentication failure
traps will be sent.
Link Up/Down Flag Can be enabled or disabled. The factory default is enabled. Indicates whether link status traps will
be sent.
Multiple Users Flag Can be enabled or disabled. The factory default is enabled. Indicates whether a trap will be sent
when the same user ID is logged into the switch more than once at the same time (either through
Telnet or the serial port).
Spanning Tree Can be enabled or disabled. The factory default is enabled. Indicates whether spanning tree traps
Flag are sent.
ACL Traps May be enabled or disabled. The factory default is disabled. Indicates whether ACL traps are sent.
DVMRP Traps Can be enabled or disabled. The factory default is disabled. Indicates whether DVMRP traps are
sent.
OSPFv2 Traps Can be enabled or disabled. The factory default is disabled. Indicates whether OSPF traps are sent.
If any of the OSPF trap flags are not enabled, then the command displays disabled. Otherwise, the
command shows all the enabled OSPF traps’ information.
OSPFv3 Traps Can be enabled or disabled. The factory default is disabled. Indicates whether OSPF traps are sent.
If any of the OSPFv3 trap flags are not enabled, then the command displays disabled. Otherwise,
the command shows all the enabled OSPFv3 traps’ information.
PIM Traps Can be enabled or disabled. The factory default is disabled. Indicates whether PIM traps are sent.
Management Commands 141

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
RADIUS Commands
This section describes the commands you use to configure the switch to use a Remote
Authentication Dial-In User Service (RADIUS) server on your network for authentication and
accounting.
The first time that you log in as an admin user, no password is required (that is, the password
is blank). As of software version 12.0.9.3, after you log in for the first time, you are required to
specify a new password that you must use each subsequent time that you log in. After you
specify the new password, you are logged out and then must log in again, using your new
password.
If you are using a RADIUS or TACAS+ server for authentication, after changing the default
password to the new password, make sure that you also change the password in the
RADIUS or TACAS+ server so that you can continue to log in to the switch.
aaa server radius dynamic-author
This command enables Change of Authorization (CoA) functionality and lets you configure
the switch from the dynamic authorization local server configuration mode.
Format aaa server radius dynamic-author
Mode Global Config
no aaa server radius dynamic-author
This command disables Change of Authorization (CoA) functionality.
Format no aaa server radius dynamic-author
Mode Global Config
auth-type
This command specifies the type of authorization that the switch uses for RADIUS clients.
The client must match the configured attributes for authorization.
Default all
Format auth-type {any | all | session-key}
Mode Dynamic Authorization
Management Commands 142

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no auth-type
Use this command to reset the type of authorization that the switch uses for RADIUS clients.
Format no auth-type
Mode Dynamic Authorization
authorization network radius
Use this command to enable the switch to accept VLAN assignments from the RADIUS
server.
Default disable
Format authorization network radius
Mode Global Config
no authorization network radius
Use this command to prevent the switch from accepting VLAN assignments from the
RADIUS server.
Format no authorization network radius
Mode Global Config
clear radius dynamic-author statistics
Use this command to clear the counters for RADIUS dynamic authorization.
Format clear radius dynamic-author statistics
Mode Privileged EXEC
client
Use this command to configure the IP address or host name of the dynamic authorization
client. Use the optional server-key keyword and key-string argument to configure the
server key at the client level.
Format client {ip-address | hostname} [server-key [0 | 7] key-string]
Mode Dynamic Authorization
Management Commands 143

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no client
Use this command to remove the configured dynamic authorization client and the key that is
associated with that client in the device.
Format no client {ip-address | hostname}
Mode Dynamic Authorization
debug aaa coa
Use this command to display debug information for the dynamic authorization server
process.
Format debug aaa coa
Mode Dynamic Authorization
debug aaa pod
Use this command to display disconnect message packets.
Format debug aaa pod
Mode Dynamic Authorization
ignore server-key
Use this command to configure the switch to ignore the server key.
Format ignore server-key
Mode Dynamic Authorization
no ignore server-key
Use this command to configure the switch not to ignore the server key. That is, this command
resets the ignore server key property on the switch.
Format no ignore server-key
Mode Dynamic Authorization
ignore session-key
Use this command to configure the switch to ignore the session key.
Format ignore session-key
Mode Dynamic Authorization
Management Commands 144
