# vlan_config_no_set_igmp_fast-leave

Pages: 571-571

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no set igmp interfacemode
This command disables IGMP Snooping on all interfaces on the switch at the same time. It is
disabled by default. This command does not take effect on the interface where routing is
enabled or is a member of a port-channel (LAG). Disable routingon the interface before
setting IGMP Snooping. The interface that is a member of a port-channel (LAG) must be
removed before setting IGMP Snooping
Default Disabled
Format no set igmp interfacemode
Mode Global Config
set igmp fast-leave
This command enables or disables IGMP Snooping fast-leave on a selected interface, a
range of interfaces, or a VLAN.
When you enable fast-leave, the switch immediately removes a layer 2 LAN interface from its
forwarding table if the following situation occurs:
1. The switch does not send MAC-based general queries to the layer 2 LAN interface.
2. The switch receives an IGMP leave message for the associated multicast group.
Enable fast-leave only on VLANs for which a single host is connected to each layer 2 LAN
interface. Doing so prevents the inadvertent dropping of other hosts that are connected to the
same layer 2 LAN interface but are still interested in receiving multicast traffic that is directed
to the multicast group.
Fast-leave processing is supported for IGMPv2 hosts only.
Default Enabled for VLAN 1; Disabled for other VLANs.
Format set igmp fast-leave [vlan-id]
Mode Interface Config
Interface Range
VLAN Config
no set igmp fast-leave
This command disables IGMP Snooping fast-leave admin mode on a selected interface.
Format no set igmp fast-leave [vlan-id]
Mode Interface Config
Interface Range
VLAN Config
Switching Commands 571
