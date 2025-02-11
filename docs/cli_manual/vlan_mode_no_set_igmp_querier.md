# vlan_mode_no_set_igmp_querier

Pages: 584-587

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: This note clarifies the prioritization of MGMD Snooping
Configurations. Many of the IGMP/MLD Snooping commands are
available both in the Interface and VLAN modes. Operationally the
system chooses or prefers the VLAN configured values over the
Interface configured values for most configurations when the interface
participates in the VLAN.
set igmp querier
Use this command to enable IGMP Snooping Querier on the system, using Global Config
mode, or on a VLAN. Using this command, you can specify the IP Address that the Snooping
Querier switch should use as the source address while generating periodic queries.
If a VLAN has IGMP Snooping Querier enabled and IGMP Snooping is operationally disabled
on it, IGMP Snooping Querier functionality is disabled on that VLAN. IGMP Snooping
functionality is re-enabled if IGMP Snooping is operational on the VLAN.
Note: The Querier IP Address assigned for a VLAN takes preference over
global configuration.
The IGMP Snooping Querier application supports sending periodic general queries on the
VLAN to solicit membership reports.
Default Enabled in Global Config mode with default VLAN 1
Format set igmp querier [vlan-id] [address ipaddress]
Mode Global Config
VLAN Mode
no set igmp querier
Use this command to disable IGMP Snooping Querier on the system. Use the optional
address parameter to reset the querier address to 0.0.0.0.
Format no set igmp querier [vlan-id] [address]
Mode Global Config
VLAN Mode
Switching Commands 584

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
set igmp querier query-interval
Use this command to set the IGMP querier query interval time. It is the period in seconds,
from 1–1800 seconds, that the switch waits before sending another general query.
Default 60 seconds
Format set igmp querier query-interval seconds
Mode Global Config
no set igmp querier query-interval
Use this command to set the IGMP querier query interval time to its default value.
Format no set igmp querier query-interval
Mode Global Config
set igmp querier timer expiry
Use this command to set the IGMP querier timer expiration period in seconds, from 60–300
seconds. This is the period that the switch remains in non-querier mode after it has
discovered a multicast querier in the network.
Default 60 seconds
Format set igmp querier timer expiry seconds
Mode Global Config
no set igmp querier timer expiry
Use this command to set the IGMP querier timer expiration period to its default value.
Format no set igmp querier timer expiry
Mode Global Config
set igmp querier version
Use this command to set the IGMP version of the query that the snooping switch sends
periodically.
Default 1
Format set igmp querier version {1 | 2}
Mode Global Config
Switching Commands 585

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no set igmp querier version
Use this command to set the IGMP Querier version to its default value.
Format no set igmp querier version
Mode Global Config
set igmp querier election participate
Use this command to enable the Snooping Querier to participate in the Querier Election
process when it discovers the presence of another Querier in the VLAN. When this mode is
enabled, if the Snooping Querier finds that the other Querier’s source address is better (less)
than the Snooping Querier’s address, it stops sending periodic queries. If the Snooping
Querier wins the election, then it will continue sending periodic queries.
Default disabled
Format set igmp querier election participate
Mode VLAN Config
no set igmp querier election participate
Use this command to set the Snooping Querier not to participate in querier election but go
into non-querier mode as soon as it discovers the presence of another querier in the same
VLAN.
Format no set igmp querier election participate
Mode VLAN Config
show igmpsnooping querier
Use this command to display IGMP Snooping Querier information. Configured information is
displayed whether or not IGMP Snooping Querier is enabled.
Format show igmpsnooping querier [detail | vlan vlan-id]
Mode Privileged EXEC
When the optional argument vlan-id is not used, the command displays the following
information.
Field Description
Admin Mode Indicates whether or not IGMP Snooping Querier is active on the switch.
Admin Version The version of IGMP that will be used while sending out the queries.
Switching Commands 586

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Description
Querier Address The IP Address which will be used in the IPv4 header while sending out IGMP queries. It can be
configured using the appropriate command.
Query Interval The amount of time in seconds that a Snooping Querier waits before sending out the periodic
general query.
Querier Timeout The amount of time to wait in the Non-Querier operational state before moving to a Querier state.
When you specify a value for vlan-id, the following additional information displays.
Field Description
VLAN Admin Mode Indicates whether iGMP Snooping Querier is active on the VLAN.
VLAN Operational Indicates whether IGMP Snooping Querier is in “Querier” or “Non-Querier” state. When the switch is
State in Querier state, it will send out periodic general queries. When in Non-Querier state, it will wait for
moving to Querier state and does not send out any queries.
VLAN Operational Indicates the time to wait before removing a Leave from a host upon receiving a Leave request. This
Max Response value is calculated dynamically from the Queries received from the network. If the Snooping Switch
Time is in Querier state, then it is equal to the configured value.
Querier Election Indicates whether the IGMP Snooping Querier participates in querier election if it discovers the
Participation presence of a querier in the VLAN.
Querier VLAN The IP address will be used in the IPv4 header while sending out IGMP queries on this VLAN. It can
Address be configured using the appropriate command.
Operational The version of IPv4 will be used while sending out IGMP queries on this VLAN.
Version
Last Querier Indicates the IP address of the most recent Querier from which a Query was received.
Address
Last Querier Indicates the IGMP version of the most recent Querier from which a Query was received on this
Version VLAN.
When the optional argument detail is used, the command shows the global information
and the information for all Querier-enabled VLANs.
set igmp proxy-querier
If a non-querier switch receives an IGMP leave message, the non-querier switch can send
queries with 0::0 as source IP addresses. This command enables the switch to send such
proxy queries through different command modes in the following ways:
• in Global Config mode, on the entire switch
• in Interface Config mode, on an interface
• in VLAN Config mode, on a particular VLAN and all interfaces participating in the VLAN.
Switching Commands 587
