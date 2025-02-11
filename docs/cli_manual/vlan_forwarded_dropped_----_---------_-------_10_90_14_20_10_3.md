# vlan_forwarded_dropped_----_---------_-------_10_90_14_20_10_3

Pages: 560-560

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
ACL Drops The number of packets dropped due to ARP ACL rule match failure.
DHCP Permits The number of packets permitted due to DHCP snooping binding database match.
ACL Permits The number of packets permitted due to ARP ACL rule match.
Bad Src MAC The number of packets dropped due to Source MAC validation failure.
Bad Dest MAC The number of packets dropped due to Destination MAC validation failure.
Invalid IP The number of packets dropped due to invalid IP checks.
Command example:
The output of the show ip arp inspection statistics command lists the summary
of forwarded and dropped ARP packets on all DAI-enabled VLANs:
VLAN Forwarded Dropped
---- --------- -------
10 90 14
20 10 3
Command example:
(NETGEAR Switch) #show ip arp inspection statistics vlan vlan-list
VLAN DHCP ACL DHCP ACL Bad Src Bad Dest Invalid
D rops D rops Permits Permits MAC MAC IP
----- -------- --------- ----------- --------- ---------- ----------- ---------
10 11 1 6 5 25 1 1 0
20 1 0 8 2 0 1 1
clear ip arp inspection statistics
Use this command to reset the statistics for Dynamic ARP Inspection on all VLANs.
Default none
Format clear ip arp inspection statistics
Mode Privileged EXEC
show ip arp inspection interfaces
Use this command to display the Dynamic ARP Inspection configuration on all the
DAI-enabled interfaces. An interface is said to be enabled for DAI if at least one VLAN, that
the interface is a member of, is enabled for DAI. Given a unit/slot/port interface
Switching Commands 560
