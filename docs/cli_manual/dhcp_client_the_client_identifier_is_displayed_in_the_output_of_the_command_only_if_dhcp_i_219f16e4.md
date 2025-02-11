# dhcp_client_the_client_identifier_is_displayed_in_the_output_of_the_command_only_if_dhcp_i_219f16e4

Pages: 677-678

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
ICMP Redirects Displays whether ICMP Redirects may be sent (enabled or disabled).
DHCP Client The client identifier is displayed in the output of the command only if DHCP is enabled with the
Identifier client-id option on the in-band interface. See the ip address dhcp command.
Command example:
(NETGEAR Switch) #show ip interface 1/0/2
Routing Interface Status....................... Down
Primary IP Address............................. 1.2.3.4/255.255.255.0
Method......................................... Manual
Secondary IP Address(es)....................... 21.2.3.4/255.255.255.0
............................................... 22.2.3.4/255.255.255.0
Helper IP Address.............................. 1.2.3.4
............................................... 1.2.3.5
Routing Mode................................... Disable
Administrative Mode............................ Enable
Forward Net Directed Broadcasts................ Disable
Proxy ARP...................................... Enable
Local Proxy ARP................................ Disable
Active State................................... Inactive
Link Speed Data Rate........................... Inactive
MAC Address.................................... 00:10:18:82:0C:68
Encapsulation Type............................. Ethernet
IP MTU......................................... 1500
Bandwidth...................................... 100000 kbps
Destination Unreachables....................... Enabled
ICMP Redirects................................. Enabled
Command example:
The following example enables the DHCP client on a VLAN routing interface:
(NETGEAR Switch) #show ip interface vlan 10
Routing Interface Status................. Up
Method................................... DHCP
Routing Mode............................. Enable
Administrative Mode...................... Enable
Forward Net Directed Broadcasts.......... Disable
Active State............................. Inactive
Link Speed Data Rate..................... 10 Half
MAC address.............................. 00:10:18:82:16:0E
Encapsulation Type....................... Ethernet
IP MTU................................... 1500
Bandwidth................................ 10000 kbps
Destination Unreachables................. Enabled
Routing Commands 677

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ICMP Redirects........................... Enabled
Interface Suppress Status................ Unsuppressed
DHCP Client Identifier................... 0NETGEAR-0010.1882.160E-vl10
show ip interface brief
This command displays summary information about IP configuration settings for all ports in
the router, and indicates how each IP address was assigned.
Format show ip interface brief
Modes Privileged EXEC
User EXEC
Term Definition
Interface Valid slot and port number separated by a forward slash.
State Routing operational state of the interface.
IP Address The IP address of the routing interface in 32-bit dotted decimal format.
IP Mask The IP mask of the routing interface in 32-bit dotted decimal format.
Method Indicates how each IP address was assigned. The field contains one of the following values:
• DHCP. The address is leased from a DHCP server.
• Manual. The address is manually configured.
Command example:
(alpha1) #show ip interface brief
Interface State IP Address IP Mask Method
---------- ----- --------------- --------------- --------
1/0/17 Up 192.168.75.1 255.255.255.0 DHCP
show ip load-sharing
This command displays the configured IP ECMP load balancing mode.
Format show ip load-sharing
Mode Privileged Exec
Command example:
(NETGEAR Switch) #show ip load-sharing
ip load-sharing 6 inner
Routing Commands 678
