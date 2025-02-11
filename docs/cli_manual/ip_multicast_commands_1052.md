# ip_multicast_commands_1052

Pages: 1052-1052

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format show ip igmp interface {unit/slot/port | vlan vlan-id}
Modes Privileged EXEC
User EXEC
Term Definition
Interface unit/slot/port
IGMP Admin Mode The administrative status of IGMP.
Interface Mode Indicates whether IGMP is enabled or disabled on the interface.
IGMP Version The version of IGMP running on the interface. This value can be configured to create a router
capable of running either IGMP version 1 or 2.
Query Interval The frequency at which IGMP Host-Query packets are transmitted on this interface.
Query Max The maximum query response time advertised in IGMPv2 queries on this interface.
Response Time
Robustness The tuning for the expected packet loss on a subnet. If a subnet is expected to be have a lot of loss,
the Robustness variable may be increased for that interface.
Startup Query The interval between General Queries sent by a Querier on startup.
Interval
Startup Query The number of Queries sent out on startup, separated by the Startup Query Interval.
Count
Last Member The Maximum Response Time inserted into Group-Specific Queries sent in response to Leave
Query Interval Group messages.
Last Member The number of Group-Specific Queries sent before the router assumes that there are no local
Query Count members.
show ip igmp interface membership
This command displays the list of interfaces that registered in the multicast group. The
multiipaddr argument specifies the IP address of the multicast group.
Format show ip igmp interface membership multiipaddr [detail]
Mode Privileged EXEC
Term Definition
Interface Valid unit, slot and port number separated by forward slashes.
Interface IP The IP address of the interface participating in the multicast group.
State The interface that has IGMP in Querier mode or Non-Querier mode.
IP Multicast Commands 1052
