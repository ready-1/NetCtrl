# ospf_advertises_the_ip_mtu_in_the_database_description_packets_it_sends_to_its_neighbors

Pages: 673-673

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip netdirbcast
This command disables the forwarding of network-directed broadcasts. When disabled,
network directed broadcasts are dropped.
Format no ip netdirbcast
Mode Interface Config
ip mtu
This command sets the IP Maximum Transmission Unit (MTU) on a routing interface or range
of interfaces. The IP MTU is the size of the largest IP packet that can be transmitted on the
interface without fragmentation. Forwarded packets are dropped if they exceed the IP MTU
of the outgoing interface. The MTU size is a number in the range 68–12270.
OSPF advertises the IP MTU in the Database Description packets it sends to its neighbors
during database exchange. If two OSPF neighbors advertise different IP MTUs, they will not
form an adjacency (unless OSPF has been instructed to ignore differences in IP MTU with
the ip ospf mtu-ignore command.)
Note: The IP MTU size refers to the maximum size of the IP packet (IP
Header + IP payload). It does not include any extra bytes that may be
required for Layer-2 headers. To receive and process packets, the
Ethernet MTU (see mtu on p age373) must take into account the size
of the Ethernet header.
Default 1500 bytes
Format ip mtu size
Mode Interface Config
no ip mtu
This command resets the ip mtu to the default value.
Format no ip mtu
Mode Interface Config
Routing Commands 673
