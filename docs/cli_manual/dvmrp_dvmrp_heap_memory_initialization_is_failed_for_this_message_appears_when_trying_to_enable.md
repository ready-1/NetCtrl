# dvmrp_dvmrp_heap_memory_initialization_is_failed_for_this_message_appears_when_trying_to_enable

Pages: 1131-1131

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 65. PIM-DM Log Messages (continued)
Component Message Cause
PIMDM PIMDMv6 Socket Memb'ship Disable Failed for PIMDMv6 Socket Creation/options Disable with
rtrIfNum – xxx. Kernel IP Stack Failed. As a result of this, the PIMv6
Control packets are still received on the interface at
the application though no protocol is enabled.
PIMDM PIMDM MRT Table Max Limit - xxx Reached; PIMDM Multicast Route table (S,G) has reached
Cannot accommodate any further routes. maximum capacity and cannot accommodate new
registrations anymore.
Table 66. DVMRP Log Messages
Component Message Cause
DVMRP DVMRP Heap memory initialization is Failed for This message appears when trying to enable
the specified address family. DVMRP Protocol
DVMRP DVMRP Heap memory de-initialization is Failed This message appears when trying to disable
for the specified address family. DVMRP Protocol. As a result of this, the subsequent
attempts to enable/disable DVMRP will also fail.
DVMRP DVMRP protocol initialization sequence Failed. This could be due to the non-availability of some
resources. This message appears when trying to
enable DVMRP Protocol.
DVMRP DVMRP All Routers Address - xxx Delete from DMVRP All Routers Address deletion from the local
the DTL Mcast List Failed for intf – xxx. multicast list Failed. As a result of this, DVMRP
Multicast packets are still received at the application
though DVMRP is disabled.
DVMRP Mcast Forwarding Mode Disable Failed for intf – The Multicast Forwarding mode Disable Failed for
xxx. this routing interface.
DVMRP DVMRP All Routers Address - xxx Add to the DMVRP All Routers Address addition to the local
DTL Mcast List Failed for intf – xxx. multicast list Failed. As a result of this, DVMRP
Multicast packets with this address will not be
received at the application.
DVMRP Mcast Forwarding Mode Enable Failed for intf – The Multicast Forwarding mode Enable Failed for
xxx. this routing interface. As a result of this, the ability to
forward Multicast packets does not function on this
interface.
DVMRP DVMRP Probe Control message Send Failed on DVMRP Probe control message send failed. This
rtrIfNum – xxx. could mostly be because of a Failure return status of
the socket call sendto(). As a result of this, the
DVMRP neighbor could be lost in the neighboring
DVMRP routers.
Switch Software Log Messages 1131
