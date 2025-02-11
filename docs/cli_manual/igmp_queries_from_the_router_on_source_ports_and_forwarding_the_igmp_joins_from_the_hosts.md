# igmp_queries_from_the_router_on_source_ports_and_forwarding_the_igmp_joins_from_the_hosts

Pages: 563-565

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no mvr group
This command removes the MVR membership group.
Format no mvr group A.B.C.D [count]
Mode Global Config
mvr mode
This command changes the MVR mode type. If the mode is set to compatible, the switch
does not learn multicast groups; they need to be configured by the operator as the protocol
does not forward joins from the hosts to the router. To operate in this mode, the IGMP router
needs to be statically configured to transmit all required multicast streams to the MVR switch.
If the mode is set to dynamic, the switch learns existing multicast groups by snooping the
IGMP queries from the router on source ports and forwarding the IGMP joins from the hosts
to the IGMP router on the multicast VLAN (with appropriate translation of the VLAN ID).
Default Compatible
Format mvr mode {compatible | dynamic}
Mode Global Config
no mvr mode
This command sets the mode type to the default value.
Format no mvr mode
Mode Global Config
mvr querytime
This command sets the MVR query response time in deciseconds. The time is in the range
1–100 deciseconds (one decisecond is one tenth of a second).
Default 5
Format mvr querytime deciseconds
Mode Global Config
no mvr querytime
This command sets the MVR query response time to the default value.
Format no mvr querytime
Mode Global Config
Switching Commands 563

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
mvr vlan
This command sets the MVR multicast VLAN.
Default 1
Format mvr vlan vlan-id
Mode Global Config
no mvr vlan
This command sets the MVR multicast VLAN to the default value.
Format no mvr vlan
Mode Global Config
mvr immediate
This command enables MVR immediate leave mode. MVR provides two modes of operating
with the IGMP Leave messages: normal leave and immediate leave.
• In normal leave mode, when a leave is received, the general IGMP query is sent from a
Layer 2 switch to the receiver port, where the leave was received. Then reports are
received from other interested hosts that are also connected to that port, for example,
using hub.
• In immediate leave mode, when a leave is received, the switch is immediately
reconfigured not to forward a specific multicast stream to the port where a message is
received. This mode is used only for ports where only one client might be connected.
Default Disabled
Format mvr immediate
Mode Interface Config
no mvr immediate
This command sets the MVR multicast VLAN to the default value.
Format no mvr immediate
Mode Interface Config
Switching Commands 564

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
mvr type
This command sets the MVR port type. When a port is set as source, it is the port to which
the multicast traffic flows using the multicast VLAN. When a port is set to receiver, it is the
port where a listening host is connected to the switch.
Default none
Format mvr type {receiver | source}
Mode Interface Config
no mvr type
Use this command to set the MVR port type to none.
Format no mvr type
Mode Interface Config
mvr vlan group
Use this command to include the port in the specific MVR group. mVLAN is the multicast
VLAN, and A.B.C.D is the IP multicast group.
Format mvr vlan mVLAN group A.B.C.D
Mode Interface Config
no mvr vlan
Use this command to exclude the port from the specific MVR group.
Format no mvr vlan mVLAN group A.B.C.D
Mode Interface Config
show mvr
This command displays global MVR settings.
Format show mvr
Mode Privileged EXEC
The following table explains the output parameters.
Term Definition
MVR Running MVR running state. It can be enabled or disabled.
MVR multicast VLAN Current MVR multicast VLAN. It can be in the range from 1 to 4094.
Switching Commands 565
