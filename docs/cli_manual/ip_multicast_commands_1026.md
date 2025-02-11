# ip_multicast_commands_1026

Pages: 1026-1026

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Interface Mode Indicates whether DVMRP is enabled or disabled on the specified interface.
Metric The metric of this interface. This is a configured value.
Local Address The IP address of the interface.
The following field is displayed only when DVMRP is operational on the interface.
Term Definition
Generation ID The Generation ID value for the interface. This is used by the neighboring routers to detect that the
DVMRP table should be resent.
The following fields are displayed only if DVMRP is enabled on this interface.
Term Definition
Received Bad The number of invalid packets received.
Packets
Received Bad The number of invalid routes received.
Routes
Sent Routes The number of routes that have been sent on this interface.
show ip dvmrp neighbor
This command displays the neighbor information for DVMRP.
Format show ip dvmrp neighbor
Modes Privileged EXEC
User EXEC
Term Definition
IfIndex The value of the interface used to reach the neighbor.
Nbr IP Addr The IP address of the DVMRP neighbor for which this entry contains information.
State The state of the neighboring router. The possible value for this field are ACTIVE or DOWN.
Up Time The time since this neighboring router was learned.
Expiry Time The time remaining for the neighbor to age out. This field is not applicable if the State is DOWN.
Generation ID The Generation ID value for the neighbor.
Major Version The major version of DVMRP protocol of neighbor.
Minor Version The minor version of DVMRP protocol of neighbor.
Capabilities The capabilities of neighbor.
IP Multicast Commands 1026
