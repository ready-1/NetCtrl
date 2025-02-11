# vrrp_this_router_is_the_ip_address_owner_for_virtual_this_message_appears_when_the_address

Pages: 1126-1126

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 58. Routing T able Manager Log Messages
Component Message Cause
RTO RTO is no longer full. Routing table contains xxx When the number of best routes drops below full
best routes, xxx total routes, xxx reserved local capacity, RTO logs this notice. The number of
routes. bad adds may give an indication of the number of
route adds that failed while RTO was full, but a
full routing table is only one reason why this
count is incremented.
RTO RTO is full. Routing table contains xxx best The routing table manager, also called “RTO,”
routes, xxx total routes, xxx reserved local stores a limited number of best routes, based on
routes. The routing table manager stores a hardware capacity. When the routing table
limited number of best routes. The count of total becomes full, RTO logs this alert. The count of
routes includes alternate routes, which are not total routes includes alternate routes, which are
installed in hardware. not installed in hardware.
Table 59. VRRP Log Messages
Component Message Cause
VRRP VRRP packet of size xxx dropped. Min VRRP This message appears when there is flood of
packet size is xxx; VRRP messages in the network.
Max VRRP packet size is xxx.
VRRP VR xxx on interface xxx started as xxx. This message appears when the Virtual router is
started in the role of a Master or a Backup.
VRRP This router is the IP address owner for virtual This message appears when the address
router xxx on interface xxx. Setting the virtual ownership status for a specific VR is updated. If
router priority to xxx. this router is the address owner for the VR, set
the VR's priority to MAX priority (as per RFC
3768). If the router is no longer the address
owner, revert the priority.
Table 60. ARP Log Message
Component Message Cause
ARP IP address conflict on interface xxx for IP When an address conflict is detected for any IP
address yyy. Conflicting host MAC address is address on the switch upon reception of ARP
zzz. packet from another host or router.
Table 61. RIP Log Message
Component Message Cause
RIP RIP: discard response from xxx via unexpected When RIP response is received with a source
interface address not matching the incoming interface’s
subnet.
Switch Software Log Messages 1126
