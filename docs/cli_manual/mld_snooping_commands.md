# mld_snooping_commands

Pages: 589-589

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
MLD Snooping Commands
This section describes commands used for MLD Snooping. In IPv4, Layer 2 switches can
use IGMP Snooping to limit the flooding of multicast traffic by dynamically configuring Layer 2
interfaces so that multicast traffic is forwarded only to those interfaces associated with IP
multicast addresses. In IPv6, MLD Snooping performs a similar function. With MLD
Snooping, IPv6 multicast data is selectively forwarded to a list of ports that want to receive
the data, instead of being flooded to all ports in a VLAN. This list is constructed by snooping
IPv6 multicast control packets.
Note: This note clarifies the prioritization of MGMD Snooping
Configurations. Many of the IGMP/MLD Snooping commands are
available both in the Interface and VLAN modes. Operationally the
system chooses or prefers the VLAN configured values over the
Interface configured values for most configurations when the interface
participates in the VLAN.
set mld
This command enables MLD Snooping on the system (Global Config Mode) or an interface
(Interface Config Mode). This command also enables MLD Snooping on a particular VLAN
and enables MLD Snooping on all interfaces participating in a VLAN.
If an interface has MLD Snooping enabled and you enable this interface for routing or enlist it
as a member of a port-channel (LAG), MLD Snooping functionality is disabled on that
interface. MLD Snooping functionality is re-enabled if you disable routing or remove port
channel (LAG) membership from an interface that has MLD Snooping enabled.
MLD Snooping supports the following activities:
• Validation of address version, payload length consistencies and discarding of the frame
upon error.
• Maintenance of the forwarding table entries based on the MAC address versus the IPv6
address.
• Filters out unknown IPv6 multicast packets on a VLAN if MLD snooping is enabled, with
the exception of group addresses in the range ffx2::/16 and FF05::X. These control
packets are always flooded to all ports in the VLAN.
Default Enabled for VLAN 1; Disabled for other VLANs.
Format set mld vlan-id
Mode Global Config
Interface Config
VLAN Mode
Switching Commands 589
