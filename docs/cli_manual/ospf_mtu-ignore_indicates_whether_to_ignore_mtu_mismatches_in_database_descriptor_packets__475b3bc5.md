# ospf_mtu-ignore_indicates_whether_to_ignore_mtu_mismatches_in_database_descriptor_packets__475b3bc5

Pages: 768-770

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Authentication The OSPF Authentication Type for the specified interface are: none, simple, and encrypt.
Type
Metric Cost The cost of the OSPF interface.
Passive Status Shows whether the interface is passive or not.
OSPF MTU-ignore Indicates whether to ignore MTU mismatches in database descriptor packets sent from neighboring
routers.
Flood Blocking Indicates whether flood blocking is enabled on the interface.
The information below displays only if OSPF is enabled.
Term Definition
OSPF Interface Type Broadcast LANs, such as Ethernet and IEEE 802.5, take the value broadcast. The
OSPF Interface Type will be 'broadcast'.
State The OSPF Interface States are: down, loopback, waiting, point-to-point, designated
router, and backup designated router.
Designated Router The router ID representing the designated router.
Backup Designated Router The router ID representing the backup designated router.
Number of Link Events The number of link events.
Local Link LSAs The number of Link Local Opaque LSAs in the link-state database.
Local Link LSA Checksum The sum of LS Checksums of Link Local Opaque LSAs in the link-state database.
Prefix-suppression Displays whether prefix-suppression is enabled, disabled, or unconfigured on the given
interface.
Command example:
The following output displays when the OSPF Admin Mode is disabled:
(NETGEAR Switch) #show ip ospf interface 1/0/1
IP Address..................................... 0.0.0.0
Subnet Mask.................................... 0.0.0.0
Secondary IP Address(es).......................
OSPF Admin Mode................................ Disable
OSPF Area ID................................... 0.0.0.0
OSPF Network Type.............................. Broadcast
Router Priority................................ 1
Retransmit Interval............................ 5
Hello Interval................................. 10
Dead Interval.................................. 40
LSA Ack Interval............................... 1
Transmit Delay................................. 1
Routing Commands 768

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Authentication Type............................ None
Metric Cost.................................... 1 (computed)
Passive Status................................. Non-passive interface
OSPF Mtu-ignore................................ Disable
Flood Blocking................................. Disable
OSPF is not enabled on this interface.
show ip ospf interface brief
This command displays brief information for the physical interface or virtual interface tables.
Format show ip ospf interface brief
Mode Privileged EXEC
User EXEC
Term Definition
Interface unit/slot/port
OSPF Admin Mode States whether OSPF is enabled or disabled on a router interface.
OSPF Area ID The OSPF Area Id for the specified interface.
Router Priority A number representing the OSPF Priority for the specified interface.
Cost The metric cost of the OSPF interface.
Hello Interval A number representing the OSPF Hello Interval for the specified interface.
Dead Interval A number representing the OSPF Dead Interval for the specified interface.
Retransmit Interval A number representing the OSPF Retransmit Interval for the specified interface.
Interface Transmit A number representing the OSPF Transmit Delay for the specified interface.
Delay
LSA Ack Interval A number representing the OSPF LSA Acknowledgment Interval for the specified interface.
show ip ospf interface stats
This command displays the statistics for a specific interface. The argument
unit/slot/port corresponds to a physical routing interface or VLAN routing interface.
The vlan keyword and vlan-id parameter are used to specify the VLAN ID of the routing
VLAN directly instead of in a unit/slot/port format. The vlan-id can be a number from
1–4093.
Format show ip ospf interface stats {unit/slot/port | vlan vland-id}
Modes Privileged EXEC
User EXEC
Routing Commands 769

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
OSPF Area ID The area id of this OSPF interface.
Area Border Router The total number of area border routers reachable within this area. This is initially zero, and is
Count calculated in each SPF pass.
AS Border Router The total number of Autonomous System border routers reachable within this area.
Count
Area LSA Count The total number of link-state advertisements in this area's link-state database, excluding AS
External LSAs.
IP Address The IP address associated with this OSPF interface.
OSPF Interface The number of times the specified OSPF interface has changed its state, or an error has occurred.
Events
Virtual Events The number of state changes or errors that occurred on this virtual link.
Neighbor Events The number of times this neighbor relationship has changed state, or an error has occurred.
Sent Packets The number of OSPF packets transmitted on the interface.
Received Packets The number of valid OSPF packets received on the interface.
Discards The number of received OSPF packets discarded because of an error in the packet or an error in
processing the packet.
Bad Version The number of received OSPF packets whose version field in the OSPF header does not match the
version of the OSPF process handling the packet.
Source Not On The number of received packets discarded because the source IP address is not within a subnet
Local Subnet configured on a local interface.
Note: This field applies only to OSPFv2.
Virtual Link Not The number of received OSPF packets discarded where the ingress interface is in a nonbackbone
Found area and the OSPF header identifies the packet as belonging to the backbone, but OSPF does not
have a virtual link to the packet’s sender.
Area Mismatch The number of OSPF packets discarded because the area ID in the OSPF header is not the area ID
configured on the ingress interface.
Invalid Destination The number of OSPF packets discarded because the packet’s destination IP address is not the
Address address of the ingress interface and is not the AllDrRouters or AllSpfRouters multicast addresses.
Wrong The number of packets discarded because the authentication type specified in the OSPF header
Authentication does not match the authentication type configured on the ingress interface.
Type
Note: This field applies only to OSPFv2.
Authentication The number of OSPF packets dropped because the sender is not an existing neighbor or the
Failure sender’s IP address does not match the previously recorded IP address for that neighbor.
Note: This field applies only to OSPFv2.
Routing Commands 770
