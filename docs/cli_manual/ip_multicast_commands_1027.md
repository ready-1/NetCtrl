# ip_multicast_commands_1027

Pages: 1027-1027

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Received Routes The number of routes received from the neighbor.
Rcvd Bad Pkts The number of invalid packets received from this neighbor.
Rcvd Bad Routes The number of correct packets received with invalid routes.
show ip dvmrp nexthop
This command displays the next hop information on outgoing interfaces for routing multicast
datagrams.
Format show ip dvmrp nexthop
Modes Privileged EXEC
User EXEC
Term Definition
Source IP The sources for which this entry specifies a next hop on an outgoing interface.
Source Mask The IP Mask for the sources for which this entry specifies a next hop on an outgoing interface.
Next Hop Interface The interface in unit/slot/port format for the outgoing interface for this next hop.
Type The network is a LEAF or a BRANCH.
show ip dvmrp prune
This command displays the table listing the router’s upstream prune information.
Format show ip dvmrp prune
Modes Privileged EXEC
User EXEC
Term Definition
Group IP The multicast Address that is pruned.
Source IP The IP address of the source that has pruned.
Source Mask The network Mask for the prune source. It should be all 1s or both the prune source and prune mask
must match.
Expiry Time (secs) The expiry time in seconds. This is the time remaining for this prune to age out.
IP Multicast Commands 1027
