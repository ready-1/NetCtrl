# pimdm_pim_all_routers_address_-_xxx_add_to_the_dtl_pim_all_routers_address_addition_to_the_local

Pages: 1130-1130

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 65. PIM-DM Log Messages (continued)
Component Message Cause
PIMDM PIMDM Protocol Initialization Failed; Family PIMDM protocol initialization sequence Failed. This
–xxx. could be due to the non-availability of some
resources. This message appears when trying to
enable PIMDM Protocol.
PIMDM PIMDM Protocol De-Initialization Failed; Family – PIMDM protocol de-initialization sequence Failed.
xxx. This message appears when trying to disable PIMDM
Protocol.
PIMDM PIM All Routers Address – xxx Delete from the PIM All Routers Address deletion from the local
DTL Mcast List Failed for intf – xxx. multicast list Failed. As a result of this, PIM Multicast
packets are still received at the application though
PIM is disabled.
PIMDM PIM All Routers Address - xxx Add to the DTL PIM All Routers Address addition to the local
Mcast List Failed for intf – xxx. multicast list Failed. As a result of this, PIM Multicast
packets with this address will not be received at the
application.
PIMDM Mcast Forwarding Mode Disable Failed for intf – Multicast Forwarding Mode Disable Failed. As a
xxx. result of this, Multicast packets are still received at
the application though no protocol is enabled.
PIMDM Mcast Forwarding Mode Enable Failed for intf – Multicast Forwarding Mode Enable Failed. As a result
xxx. of this, Multicast packets will not be received at the
application though a protocol is enabled.
PIMDM PIMDMv6 Socket Memb'ship Enable Failed for PIMDMv6 Socket Creation/options Set with Kernel IP
rtrIfNum - xxx. Stack Failed. As a result of this, the PIM Control
packets cannot be received on the interface.
PIMDM PIMDMv6 Socket Memb'ship Disable Failed for PIMDMv6 Socket Creation/options Disable with
rtrIfNum – xxx. Kernel IP Stack Failed. As a result of this, the PIM
Control packets are still received on the interface at
the application though no protocol is enabled.
PIMDM PIMDM FSM Action Invoke Failed; rtrIfNum - xxx The PIMDM FSM Action invocation Failed due to
Out of Bounds for Event – xxx. invalid Routing interface number. In such cases, the
FSM Action routine can never be invoked which may
result in abnormal behavior. The failed FSM-name
can be identified from the specified Event name.
PIMDM PIMDM Socket Initialization Failed for addrFamily PIMDM Socket Creation/options Set Failed. As a
- xxx. result of this, the PIM Control packets cannot be sent
out on an interface.
PIMDM PIMDMv6 Socket Memb'ship Enable Failed for Socket options Set to enable the reception of PIMv6
rtrIfNum - xxx. packets Failed. As a result of this, the PIMv6 packets
will not be received by the application.
Switch Software Log Messages 1130
