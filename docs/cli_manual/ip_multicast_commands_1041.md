# ip_multicast_commands_1041

Pages: 1041-1041

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR) #show ip pim neighbor
Neighbor Addr Interface Uptime Expiry Time DR
(hh:mm:ss) (hh:mm:ss) Priority
--------------- --------- ----------- ----------- --------
192.168.10.2 1/0/1 00:02:55 00:01:15 1
192.168.20.2 1/0/2 00:03:50 00:02:10 1
Command example:
If no neighbors were learned on any of the interfaces, the following message is displayed:
No neighbors exist on the router.
show ip pim bsr-router
This command displays the bootstrap router (BSR) information.
Format show ip pim bsr-router {candidate | elected}
Mode Privileged EXEC
User EXEC
Parameter Definition
BSR Address IP address of the BSR.
BSR Priority Priority as configured in the ip pim bsr-candidate command.
BSR Hash Mask Length Length of a mask (maximum 32 bits) that is to be ANDed with the group address before the
hash function is called. This value is configured in the ip pim bsr-candidate command.
C-BSR Advertisement Indicates the configured C-BSR Advertisement interval with which the router, acting as a
Interval C-BSR, will periodically send the C-BSR advertisement messages.
Next Bootstrap Time (in hours, minutes, and seconds) in which the next bootstrap message is due from this
Message BSR.
Command example:
(NETGEAR) #show ip pim bsr-router elected
BSR Address................................... 192.168.10.1
BSR Priority................................ 0
BSR Hash Mask Length........................ 30
Next Bootstrap message (hh:mm:ss)........... 00:00:24
IP Multicast Commands 1041
