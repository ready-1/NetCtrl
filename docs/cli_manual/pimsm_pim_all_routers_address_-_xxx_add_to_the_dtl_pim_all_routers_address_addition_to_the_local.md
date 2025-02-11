# pimsm_pim_all_routers_address_-_xxx_add_to_the_dtl_pim_all_routers_address_addition_to_the_local

Pages: 1129-1129

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 64. PIM-SM Log Messages (continued)
Component Message Cause
PIMSM PIM All Routers Address - xxx Add to the DTL PIM All Routers Address addition to the local
Mcast List Failed for intf – xxx. multicast list Failed. As a result of this, PIM
Multicast packets with this address will not be
received at the application.
PIMSM Mcast Forwarding Mode Disable Failed for intf – Multicast Forwarding Mode Disable Failed. As a
xxx. result of this, Multicast packets are still received
at the application though no protocol is enabled.
PIMSM Mcast Forwarding Mode Enable Failed for intf – Multicast Forwarding Mode Enable Failed. As a
xxx. result of this, Multicast packets will not be
received at the application though a protocol is
enabled.
PIMSM PIMSMv6 Socket Memb'ship Enable Failed for PIMSMv6 Socket Creation/options Set with
rtrIfNum - xxx. Kernel IP Stack Failed. As a result of this, the
PIM Control packets cannot be received on the
interface.
PIMSM PIMSMv6 Socket Memb'ship Disable Failed for PIMSMv6 Socket Creation/options Disable with
rtrIfNum – xxx. Kernel IP Stack Failed. As a result of this, the
PIM Control packets are still received on the
interface at the application though no protocol is
enabled.
PIMSM PIMSM (S,G,RPt) Table Max Limit – xxx PIMSM Multicast Route table (S,G,RPt) has
Reached; Cannot accommodate any further reached maximum capacity and cannot
routes. accommodate new registrations anymore.
PIMSM PIMSM (S,G) Table Max Limit - xxx Reached; PIMSM Multicast Route table (S,G) has reached
Cannot accommodate any further routes. maximum capacity and cannot accommodate
new registrations anymore.
PIMSM PIMSM (*,G) Table Max Limit - xxx Reached; PIMSM Multicast Route table (*,G) has reached
Cannot accommodate any further routes. maximum capacity and cannot accommodate
new registrations anymore.
Table 65. PIM-DM Log Messages
Component Message Cause
PIMDM PIMDM Protocol Heap Memory Init Failed; PIMDM Heap memory initialization Failed for the
Family – xxx. specified address family. This message appears
when trying to enable PIMDM Protocol.
PIMDM PIMDM Protocol Heap Memory De-Init Failed; PIMDM Heap memory de-initialization Failed for the
Family –xxx. specified address family. This message appears
when trying to disable PIMDM Protocol. As a result of
this, the subsequent attempts to enable/disable
PIMDM will also fail.
Switch Software Log Messages 1129
