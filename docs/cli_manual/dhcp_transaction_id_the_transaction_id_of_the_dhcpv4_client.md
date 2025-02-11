# dhcp_transaction_id_the_transaction_id_of_the_dhcpv4_client

Pages: 674-676

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
encapsulation
This command configures the link layer encapsulation type for the packet on an interface or
range of interfaces. The encapsulation type can be ethernet or snap.
Default ethernet
Format encapsulation {ethernet | snap}
Mode Interface Config
Note: Routed frames are always ethernet encapsulated when a frame is
routed to a VLAN.
show dhcp lease
This command displays a list of IPv4 addresses currently leased from a DHCP server on a
specific in-band interface or all in-band interfaces. This command does not apply to service
or network ports.
Format show dhcp lease [interface unit/slot/port]
Modes Privileged EXEC
Term Definition
IP address, Subnet mask The IP address and network mask leased from the DHCP server
DHCP Lease server The IPv4 address of the DHCP server that leased the address.
State State of the DHCPv4 Client on this interface
DHCP transaction ID The transaction ID of the DHCPv4 Client
Lease The time (in seconds) that the IP address was leased by the server
Renewal The time (in seconds) when the next DHCP renew Request is sent by DHCPv4 Client to
renew the leased IP address
Rebind The time (in seconds) when the DHCP Rebind process starts
Retry count Number of times the DHCPv4 client sends a DHCP REQUEST message before the
server responds
Routing Commands 674

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ip brief
This command displays all the summary information of the IP, including the ICMP rate limit
configuration and the global ICMP Redirect configuration.
Format show ip brief
Modes Privileged EXEC
User EXEC
Term Definition
Default Time to Live The computed TTL (Time to Live) of forwarding a packet from the local router to the final
destination.
Routing Mode Shows whether the routing mode is enabled or disabled.
Maximum Next Hops The maximum number of next hops the packet can travel.
Maximum Routes The maximum number of routes the packet can travel.
ICMP Rate Limit Interval Shows how often the token bucket is initialized with burst-size tokens. Burst-interval is from 0
to 2147483647 milliseconds. The default burst-interval is 1000 msec.
ICMP Rate Limit Burst Shows the number of ICMPv4 error messages that can be sent during one burst-interval. The
Size range is from 1 to 200 messages. The default value is 100 messages.
ICMP Echo Replies Shows whether ICMP Echo Replies are enabled or disabled.
ICMP Redirects Shows whether ICMP Redirects are enabled or disabled.
Command example:
(NETGEAR Switch) #show ip brief
Default Time to Live........................... 64
Routing Mode................................... Disabled
Maximum Next Hops.............................. 4
Maximum Routes................................. 128
ICMP Rate Limit Interval....................... 1000 msec
ICMP Rate Limit Burst Size..................... 100 messages
ICMP Echo Replies.............................. Enabled
ICMP Redirects................................. Enabled
show ip interface
This command displays all pertinent information about the IP interface. The argument
unit/slot/port corresponds to a physical routing interface or VLAN routing interface.
The keyword vlan is used to specify the VLAN ID of the routing VLAN directly instead of in a
unit/slot/port format.
Routing Commands 675

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The vlan-id is a number in the range 1–4093. The loopback number is in the range 0–7.
Format show ip interface {unit/slot/port | vlan vland-id | loopback number}
Modes Privileged EXEC
User EXEC
Term Definition
Routing Interface Determine the operational status of IPv4 routing Interface. The possible values are Up or Down.
Status
Primary IP Address The primary IP address and subnet masks for the interface. This value appears only if you configure
it.
Method Shows whether the IP address was configured manually or acquired from a DHCP server.
Secondary IP One or more secondary IP addresses and subnet masks for the interface. This value appears only if
Address you configure it.
Helper IP Address The helper IP addresses configured by the command ip helper-address (Interface Config) on
p age721.
Routing Mode The administrative mode of router interface participation. The possible values are enable or disable.
This value is configurable.
Administrative The administrative mode of the specified interface. The possible values of this field are enable or
Mode disable. This value is configurable.
Forward Net Displays whether forwarding of network-directed broadcasts is enabled or disabled. This value is
Directed configurable.
Broadcasts
Proxy ARP Displays whether Proxy ARP is enabled or disabled on the system.
Local Proxy ARP Displays whether Local Proxy ARP is enabled or disabled on the interface.
Active State Displays whether the interface is active or inactive. An interface is considered active if its link is up
and it is in forwarding state.
Link Speed Data An integer representing the physical link data rate of the specified interface. This is measured in
Rate Megabits per second (Mbps).
MAC Address The burned in physical address of the specified interface. The format is 6 two-digit hexadecimal
numbers that are separated by colons.
Encapsulation The encapsulation type for the specified interface. The types are: Ethernet or SNAP.
Type
IP MTU The maximum transmission unit (MTU) size of a frame, in bytes.
Bandwidth Shows the bandwidth of the interface.
Destination Displays whether ICMP Destination Unreachables may be sent (enabled or disabled).
Unreachables
Routing Commands 676
