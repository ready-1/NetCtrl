# igmp_snooping_configuration_commands

Pages: 569-569

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no debug mvr trace
This command disables MVR debug tracing.
Format no debug mvr trace
Mode Privileged EXEC
debug mvr packet
This command enables debug tracing of MVR packets on the receiving side, transmitting
side, or both sides. By default, debug tracing of MVR packets is enabled.
Format debug mvr packet [receive | transmit]
Mode Privileged EXEC
no debug mvr packet
This command disables debug tracing of MVR packets on the receiving side, transmitting
side, or both sides.
Format no debug mvr packet [receive | transmit]
Mode Privileged EXEC
IGMP Snooping Configuration Commands
This section describes the commands you use to configure IGMP snooping. The switch
supports IGMP Versions 1, 2, and 3. The IGMP snooping feature can help conserve
bandwidth because it allows the switch to forward IP multicast traffic only to connected hosts
that request multicast traffic. IGMPv3 adds source filtering capabilities to IGMP versions 1
and 2.
Note: This note clarifies the prioritization of MGMD Snooping
Configurations. Many of the IGMP/MLD Snooping commands are
available both in the Interface and VLAN modes. Operationally the
system chooses or prefers the VLAN configured values over the
Interface configured values for most configurations when the interface
participates in the VLAN.
set igmp
This command enables IGMP Snooping on the system (Global Config Mode), an interface, or
a range of interfaces. This command also enables IGMP snooping on a particular VLAN
Switching Commands 569
