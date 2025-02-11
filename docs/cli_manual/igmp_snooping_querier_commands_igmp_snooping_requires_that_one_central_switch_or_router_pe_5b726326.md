# igmp_snooping_querier_commands_igmp_snooping_requires_that_one_central_switch_or_router_pe_5b726326

Pages: 583-583

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show igmpsnooping ssm
This command displays information about Source Specific Multicasting (SSM) by entry,
group, or statistics. SSM delivers multicast packets to receivers that originated from a source
address specified by the receiver. SSM is only available with IGMPv3 and MLDv2.
Format show igmpsnooping ssm {entries | groups | stats}
Mode Privileged EXEC
show mac-address-table igmpsnooping
This command displays the IGMP Snooping entries in the MFDB table.
Format show mac-address-table igmpsnooping
Mode Privileged EXEC
Term Definition
VLAN ID The VLAN in which the MAC address is learned.
MAC Address A multicast MAC address for which the switch has forwarding or filtering information. The format is 6
two-digit hexadecimal numbers that are separated by colons, for example 01:23:45:67:89:AB.
Type The type of the entry, which is either static (added by the user) or dynamic (added to the table as a
result of a learning process or protocol).
Description The text description of this multicast table entry.
Interfaces The list of interfaces that are designated for forwarding (Fwd:) and filtering (Flt:).
IGMP Snooping Querier Commands
IGMP Snooping requires that one central switch or router periodically query all end-devices
on the network to announce their multicast memberships. This central device is the “IGMP
Querier”. The IGMP query responses, known as IGMP reports, keep the switch updated with
the current multicast group membership on a port-by-port basis. If the switch does not
receive updated membership information in a timely fashion, it will stop forwarding multicasts
to the port where the end device is located.
This section describes commands used to configure and display information on IGMP
Snooping Queriers on the network and, separately, on VLANs.
Switching Commands 583
