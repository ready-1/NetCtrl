# vlan_mode_no_set_mld_querier

Pages: 600-602

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: This note clarifies the prioritization of MGMD Snooping
Configurations. Many of the IGMP/MLD Snooping commands are
available both in the Interface and VLAN modes. Operationally the
system chooses or prefers the VLAN configured values over the
Interface configured values for most configurations when the interface
participates in the VLAN.
set mld querier
Use this command to enable MLD Snooping Querier on the system (Global Config Mode) or
on a VLAN. Using this command, you can specify the IP address that the snooping querier
switch should use as a source address while generating periodic queries.
If a VLAN has MLD Snooping Querier enabled and MLD Snooping is operationally disabled
on it, MLD Snooping Querier functionality is disabled on that VLAN. MLD Snooping
functionality is re-enabled if MLD Snooping is operational on the VLAN.
The MLD Snooping Querier sends periodic general queries on the VLAN to solicit
membership reports.
Default disabled
Format set mld querier [vlan-id] [address ipv6-address]
Mode Global Config
VLAN Mode
no set mld querier
Use this command to disable MLD Snooping Querier on the system. Use the optional
parameter address to reset the querier address.
Format no set mld querier [vlan-id] [address]
Mode Global Config
VLAN Mode
set mld querier query_interval
Use this command to set the MLD querier query interval time. It is the time in seconds, from
1–1800 seconds, that the switch waits before sending another general query.
Default disabled
Format set mld querier query_interval seconds
Mode Global Config
Switching Commands 600

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no set mld querier query_interval
Use this command to set the MLD Querier Query Interval time to its default value.
Format no set mld querier query-interval
Mode Global Config
set mld querier timer expiry
Use this command to set the MLD querier timer expiration period. It is the period in seconds,
from 60–300 seconds, that the switch remains in non-querier mode after it has discovered a
multicast querier in the network.
Default 60 seconds
Format set mld querier timer expiry seconds
Mode Global Config
no set mld querier timer expiry
Use this command to set the MLD querier timer expiration period to its default value.
Format no set mld querier timer expiry
Mode Global Config
set mld querier election participate
Use this command to enable the Snooping Querier to participate in the Querier Election
process when it discovers the presence of another Querier in the VLAN. When this mode is
enabled, if the Snooping Querier finds that the other Querier’s source address is better (less)
than the Snooping Querier’s address, it stops sending periodic queries. If the Snooping
Querier wins the election, then it will continue sending periodic queries.
Default disabled
Format set mld querier election participate
Mode VLAN Config
no set mld querier election participate
Use this command to set the snooping querier not to participate in querier election but go into
a non-querier mode as soon as it discovers the presence of another querier in the same
VLAN.
Format no set mld querier election participate
Mode VLAN Config
Switching Commands 601

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show mldsnooping querier
Use this command to display MLD Snooping Querier information. Configured information is
displayed whether or not MLD Snooping Querier is enabled.
Format show mldsnooping querier [detail | vlan vlan-id]
Mode Privileged EXEC
When you do not specify a value for vlan-id, the command displays the following
information.
Field Description
Admin Mode Indicates whether or not MLD Snooping Querier is active on the switch.
Admin Version Indicates the version of MLD that will be used while sending out the queries. This is defaulted to
MLD v1 and it cannot be changed.
Querier Address Shows the IP address which will be used in the IPv6 header while sending out MLD queries. It can
be configured using the appropriate command.
Query Interval Shows the amount of time in seconds that a Snooping Querier waits before sending out the periodic
general query.
Querier Timeout Displays the amount of time to wait in the Non-Querier operational state before moving to a Querier
state.
When you specify a value for vlan-id, the following information displays.
Field Description
VLAN Admin Mode Indicates whether MLD Snooping Querier is active on the VLAN.
VLAN Operational Indicates whether MLD Snooping Querier is in “Querier” or “Non-Querier” state. When the switch is
State in Querier state, it will send out periodic general queries. When in Non-Querier state, it will wait for
moving to Querier state and does not send out any queries.
VLAN Operational Indicates the time to wait before removing a Leave from a host upon receiving a Leave request. This
Max Response value is calculated dynamically from the Queries received from the network. If the Snooping Switch
Time is in Querier state, then it is equal to the configured value.
Querier Election Indicates whether the MLD Snooping Querier participates in querier election if it discovers the
Participate presence of a querier in the VLAN.
Querier VLAN The IP address will be used in the IPv6 header while sending out MLD queries on this VLAN. It can
Address be configured using the appropriate command.
Operational This version of IPv6 will be used while sending out MLD queriers on this VLAN.
Version
Last Querier Indicates the IP address of the most recent Querier from which a Query was received.
Address
Last Querier Indicates the MLD version of the most recent Querier from which a Query was received on this
Version VLAN.
Switching Commands 602
