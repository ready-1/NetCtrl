# arp_access_list_h2

Pages: 561-561

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
argument, the command displays the values for that interface whether the interface is
enabled for DAI or not.
Format show ip arp inspection interfaces [unit/slot/port]
Mode Privileged EXEC
User EXEC
Term Definition
Interface The interface ID for each displayed row.
Trust State Whether the interface is trusted or untrusted for DAI.
Rate Limit The configured rate limit value in packets per second.
Burst Interval The configured burst interval value in seconds.
Command example:
(NETGEAR Switch) #show ip arp inspection interfaces
Interface T rust State Rate Limit Burst Interval
(pps) (seconds)
--------------- ----------- ---------- ---------------
0/1 Untrusted 15 1
0/2 Untrusted 10 10
show arp access-list
Use this command to display the configured ARP ACLs with the rules. Giving an ARP ACL
name as the argument displays only the rules in that ARP ACL.
Format show arp access-list [acl-name]
Mode Privileged EXEC
User EXEC
Command example:
(NETGEAR Switch) #show arp access-list
ARP access list H2
permit ip host 1.1.1.1 mac host 00:01:02:03:04:05
permit ip host 1.1.1.2 mac host 00:03:04:05:06:07
ARP access list H3
ARP access list H4
permit ip host 2.1.1.2 mac host 00:03:04:05:06:08
Switching Commands 561
