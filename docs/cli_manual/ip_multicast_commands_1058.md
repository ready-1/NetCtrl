# ip_multicast_commands_1058

Pages: 1058-1058

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show ip igmp-proxy groups
Interface Index................................ 1/0/1
G roup Address Last Reporter Up Time Member State F ilter Mode Sources
- ------------ - ------------- - --------- - ------------ - ------------ -------
2 25.4.4.4 5 .5.5.48 0 0:02:21 D ELAY_MEMBER I nclude 3
2 26.4.4.4 5.5.5.48 0 0:02:21 DELAY_MEMBER I nclude 3
2 27.4.4.4 5 .5.5.48 0 0:02:21 D ELAY_MEMBER E xclude 0
2 28.4.4.4 5 .5.5.48 0 0:02:21 DELAY_MEMBER I nclude 3
show ip igmp-proxy groups detail
This command displays complete information about multicast groups that IGMP Proxy
reported. It displays a table of entries with the following as the fields of each column.
Format show ip igmp-proxy groups detail
Modes Privileged EXEC
User EXEC
Term Definition
Interface The interface number of the IGMP Proxy.
Group Address The IP address of the multicast group.
Last Reporter The IP address of host that last sent a membership report for the current group, on the network
attached to the IGMP-Proxy interface (upstream interface).
Up Time (in secs) The time elapsed since last created.
Member State The status of the entry. Possible values are IDLE_MEMBER or DELAY_MEMBER.
• IDLE_MEMBER - interface has responded to the latest group membership query for this group.
• DELAY_MEMBER - interface is going to send a group membership report to respond to a group
membership query for this group.
Filter Mode Possible values are Include or Exclude.
Sources The number of sources attached to the multicast group.
Group Source List The list of IP addresses of the sources attached to the multicast group.
Expiry Time Time left before a source is deleted.
IP Multicast Commands 1058
