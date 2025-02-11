# vlan_config_no_set_igmp

Pages: 570-570

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
(VLAN Config Mode) and can enable IGMP snooping on all interfaces participating in a
VLAN.
If an interface has IGMP Snooping enabled and you enable this interface for routing or enlist
it as a member of a port-channel (LAG), IGMP Snooping functionality is disabled on that
interface. IGMP Snooping functionality is re-enabled if you disable routing or remove
port-channel (LAG) membership from an interface that has IGMP Snooping enabled.
The IGMP application supports the following activities:
• Validation of the IP header checksum (as well as the IGMP header checksum) and
discarding of the frame upon checksum error.
• Maintenance of the forwarding table entries based on the MAC address versus the IP
address.
• Filters unknown IPv4 multicast packets on a VLAN if IGMP snooping is enabled, with the
exception of group addresses in the range 224.0.0.x. These control packets are always
flooded to all ports in the VLAN.
Default Enabled for VLAN 1; Disabled for other VLANs.
Format set igmp [vlan-id]
Mode Global Config
Interface Config
VLAN Config
no set igmp
This command disables IGMP Snooping on the system, an interface, a range of interfaces, or
a VLAN.
Format no set igmp [vlan-id]
Mode Global Config
Interface Config
VLAN Config
set igmp interfacemode
This command enables IGMP Snooping on all interfaces. If an interface has IGMP Snooping
enabled and you enable this interface for routing or enlist it as a member of a port-channel
(LAG), IGMP Snooping functionality is disabled on that interface. IGMP Snooping
functionality is re-enabled if you disable routing or remove port-channel (LAG) membership
from an interface that has IGMP Snooping enabled.
Default Disabled
Format set igmp interfacemode
Mode Global Config
Switching Commands 570
