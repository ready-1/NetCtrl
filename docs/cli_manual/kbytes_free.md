# kbytes_free

Pages: 59-62

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
