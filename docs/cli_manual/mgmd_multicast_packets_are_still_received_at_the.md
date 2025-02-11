# mgmd_multicast_packets_are_still_received_at_the

Pages: 1127-1128

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Multicast
Table 62. IGMP/MLD Log Messages
Component Message Cause
IGMP/MLD MGMD Protocol Heap Memory Init Failed; Family MGMD Heap memory initialization Failed for the
– xxx. specified address family. This message appears
when trying to enable MGMD Protocol.
IGMP/MLD MGMD Protocol Heap Memory De-Init Failed; MGMD Heap memory de-initialization Failed for
Family – xxx. the specified address family. This message
appears when trying to disable MGMD
(IGMP/MLD) Protocol. As a result of this, the
subsequent attempts to enable/disable MGMD
will also fail.
IGMP/MLD MGMD Protocol Initialization Failed; Family – MGMD protocol initialization sequence Failed.
xxx. This could be due to the non-availability of some
resources. This message appears when trying to
enable MGMD Protocol.
IGMP/MLD MGMD All Routers Address - xxx Set to the DTL This message appears when trying to
Mcast List Failed; Mode – xxx, intf – xxx. enable/disable MGMD Protocol.
IGMP/MLD MGMD All Routers Address - xxx Add to the DTL MGMD All Routers Address addition to the local
Mcast List Failed. multicast list Failed. As a result of this, MGMD
Multicast packets with this address will not be
received at the application.
IGMP/MLD MGMD All Routers Address – xxx Delete from MGMD All Routers Address deletion from the
the DTL Mcast List Failed. local multicast list Failed. As a result of this,
MGMD Multicast packets are still received at the
application though MGMD is disabled.
IGMP/MLD MLDv2 GroupAddr-[FF02::16] Enable with Registration of this Group address with the
Interpeak Stack Failed; rtrIfNum - xxx, intf – xxx. Interpeak stack failed. As a result of this, MLDv2
packets will not be received at the application.
IGMP/MLD MGMD Group Entry Creation Failed; grpAddr - The specified Group Address registration on the
xxx, rtrIfNum – xxx. specified router interface failed.
IGMP/MLD MGMD Socket Creation/Initialization Failed for MGMD Socket Creation/options Set Failed. As a
addrFamily – xxx. result of this, the MGMD Control packets cannot
be sent out on an interface.
Switch Software Log Messages 1127

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 63. IGMP-Proxy Log Messages
Component Message Cause
IGMP-Proxy/MLD- MGMD-Proxy Protocol Initialization Failed; MGMD-Proxy protocol initialization sequence
Proxy Family – xxx. Failed. This could be due to the non-availability
of some resources. This message appears when
trying to enable MGMD-Proxy Protocol.
IGMP-Proxy/MLD- MGMD-Proxy Protocol Heap Memory De-Init MGMD-Proxy Heap memory de-initialization is
Proxy Failed; Family – xxx. Failed for the specified address family. This
message appears when trying to disable
MGMD-Proxy Protocol. As a result of this, the
subsequent attempts to enable/disable
MGMD-Proxy will also fail.
IGMP-Proxy/MLD- MGMD Proxy Route Entry Creation Failed; Registration of the Multicast Forwarding entry for
Proxy grpAddr - xxx, srcAddr – xxx, rtrIfNum – xxx. the specified Source and Group Address Failed
when MGMD-Proxy is used.
Table 64. PIM-SM Log Messages
Component Message Cause
PIMSM Non-Zero SPT/Data Threshold Rate – xxx is This message appears when the user tries to
currently Not Supported on this platform. configure the PIMSM SPT threshold value.
PIMSM PIMSM Protocol Heap Memory Init Failed; PIMSM Heap memory initialization Failed for the
Family – xxx. specified address family. This message appears
when trying to enable PIMSM Protocol.
PIMSM PIMSM Protocol Heap Memory De-Init Failed; PIMSM Heap memory de-initialization Failed for
Family –xxx. the specified address family. This message
appears when trying to disable PIMSM Protocol.
As a result of this, the subsequent attempts to
enable/disable PIMSM will also fail.
PIMSM PIMSM Protocol Initialization Failed; Family –xxx. PIMSM protocol initialization sequence Failed.
This could be due to the non-availability of some
resources. This message appears when trying to
enable PIMSM Protocol.
PIMSM PIMSM Protocol De-Initialization Failed; Family – PIMSM protocol de-initialization sequence
xxx. Failed. This message appears when trying to
disable PIMSM Protocol.
PIMSM PIMSM SSM Range Table is Full. PIMSM SSM Range Table is Full. This message
appears when the protocol cannot accommodate
new SSM registrations.
PIMSM PIM All Routers Address – xxx Delete from the PIM All Routers Address deletion from the local
DTL Mcast List Failed for intf – xxx. multicast list Failed. As a result of this, PIM
Multicast packets are still received at the
application though PIM is disabled.
Switch Software Log Messages 1128
