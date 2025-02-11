# ip_multicast_commands_1057

Pages: 1057-1057

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Leaves Rcvd Number of IGMP leaves received. Valid for version 2 only.
Leaves Sent Number of IGMP leaves sent on the Proxy interface. Valid for version 2 only.
Command example:
(NETGEAR Switch) #show ip igmp-proxy interface
Interface Index................................ 1/0/1
Ver Query Rcvd Report Rcvd Report Sent Leave Rcvd Leave Sent
------------------------------------------------------------------
1 0 0 0
2 0 0 0 0 0
3 0 0 0
show ip igmp-proxy groups
This command displays information about the subscribed multicast groups that IGMP Proxy
reported. It displays a table of entries with the following as the fields of each column.
Format show ip igmp-proxy groups
Modes Privileged EXEC
User EXEC
Term Definition
Interface The interface number of the IGMP Proxy.
Group Address The IP address of the multicast group.
Last Reporter The IP address of host that last sent a membership report for the current group on the network
attached to the IGMP Proxy interface (upstream interface).
Up Time (in secs) The time elapsed since last created.
Member State The status of the entry. Possible values are IDLE_MEMBER or DELAY_MEMBER.
• IDLE_MEMBER - interface has responded to the latest group membership query for this group.
• DELAY_MEMBER - interface is going to send a group membership report to respond to a group
membership query for this group.
Filter Mode Possible values are Include or Exclude.
Sources The number of sources attached to the multicast group.
IP Multicast Commands 1057
