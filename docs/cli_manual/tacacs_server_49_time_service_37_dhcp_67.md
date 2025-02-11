# tacacs_server_49_time_service_37_dhcp_67

Pages: 718-722

## Content

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
