# mvr_commands

Pages: 562-562

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
MVR Commands
Internet Group Management Protocol (IGMP) Layer 3 is widely used for IPv4 network
multicasting. In Layer 2 networks, IGMP uses resources inefficiently. For example, a Layer 2
switch multicast traffic to all ports, even if there are receivers connected to only a few ports.
To address this problem, the IGMP Snooping protocol was developed. The problem still
appears, though, when receivers are in different VLANs.
MVR is intended to solve the problem of receivers in different VLANs. It uses a dedicated
manually configured VLAN, called the multicast VLAN, to forward multicast traffic over a
Layer 2 network with IGMP snooping.
mvr
This command enables MVR.
Default Disabled
Format mvr
Mode Global Config
Interface Config
no mvr
This command disables MVR.
Format no mvr
Mode Global Config
Interface Config
mvr group
This command adds an MVR membership group. A.B.C.D is the IP multicast group being
added.
The count is the number of incremental multicast groups being added (the first multicast
group is A.B.C.D). If a count is not specified, only one multicast group is added.
Format mvr group A.B.C.D [count]
Mode Global Config
Switching Commands 562
