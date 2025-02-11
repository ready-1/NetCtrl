# mld_snooping_querier_commands

Pages: 599-599

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show mac-address-table mldsnooping
Use this command to display the MLD Snooping entries in the Multicast Forwarding
Database (MFDB) table.
Format show mac-address-table mldsnooping
Mode Privileged EXEC
Term Definition
VLAN ID The VLAN in which the MAC address is learned.
MAC Address A multicast MAC address for which the switch has forwarding or filtering information. The format is 6
two-digit hexadecimal numbers that are separated by colons, for example 01:23:45:67:89:AB.
Type The type of entry, which is either static (added by the user) or dynamic (added to the table as a result
of a learning process or protocol.)
Description The text description of this multicast table entry.
Interfaces The list of interfaces that are designated for forwarding (Fwd:) and filtering (Flt:).
clear mldsnooping
Use this command to delete all MLD snooping entries from the MFDB table.
Format clear mldsnooping
Mode Privileged EXEC
MLD Snooping Querier Commands
In an IPv6 environment, MLD Snooping requires that one central switch or router periodically
query all end-devices on the network to announce their multicast memberships. This central
device is the MLD Querier. The MLD query responses, known as MLD reports, keep the
switch updated with the current multicast group membership on a port-by-port basis. If the
switch does not receive updated membership information in a timely fashion, it will stop
forwarding multicasts to the port where the end device is located.
This section describes the commands you use to configure and display information on MLD
Snooping queries on the network and, separately, on VLANs.
Switching Commands 599
