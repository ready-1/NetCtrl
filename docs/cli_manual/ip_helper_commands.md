# ip_helper_commands

Pages: 717-717

## Content

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
