# ra_redir_-------_-------_0_0_show_ipv6_vlan

Pages: 857-858

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(Switching) # clear ipv6 snooping counters
show ipv6 snooping counters
This command displays the counters that are associated with the IPv6 RA guard host mode.
The output displays the number of router advertisements and router redirect packets that are
dropped globally because of the IPv6 RA guard host mode.
Format show ipv6 snooping counters
Modes EXEC
Global Config
Command example:
(Swtiching) # show ipv6 snooping counters
IPv6 Dropped Messages
RA (Router Advertisement - ICMP type 134): 431
REDIR (Router Redirect - ICMP type 137): 6599
RA Redir
------- -------
0 0
show ipv6 vlan
This command displays IPv6 VLAN routing interface addresses.
Format show ipv6 vlan
Modes Privileged EXEC
User EXEC
Term Definition
MAC Address used by Routing VLANs Shows the MAC address.
The rest of the output for this command is displayed in a table with the following column
headings.
Column Headings Definition
VLAN ID The VLAN ID of a configured VLAN.
Logical Interface The interface in unit/slot/port format that is associated with the VLAN ID.
IPv6 The IPv6 prefix and prefix length associated with the VLAN ID.
Address/Prefix
Length
IPv6 Commands 857

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ipv6 traffic
Use this command to show traffic and statistics for IPv6 and ICMPv6. Specify a logical,
loopback, or tunnel interface to view information about traffic on a specific interface.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id
parameter is a number in the range of 1–4093.
If you do not specify an interface, the command displays information about traffic on all
interfaces.
Format show ipv6 traffic [{unit/slot/port | vlan vlan-id | loopback loopback-id |
tunnel tunnel-id}]
Mode Privileged EXEC
Term Definition
Total Datagrams Received Total number of input datagrams received by the interface, including those received
in error.
Received Datagrams Locally Total number of datagrams successfully delivered to IPv6 user-protocols (including
Delivered ICMP). This counter increments at the interface to which these datagrams were
addressed, which might not necessarily be the input interface for some of the
datagrams.
Received Datagrams Discarded Number of input datagrams discarded due to errors in their IPv6 headers, including
Due To Header Errors version number mismatch, other format errors, hop count exceeded, errors
discovered in processing their IPv6 options, etc.
Received Datagrams Discarded Number of input datagrams that could not be forwarded because their size
Due To MTU exceeded the link MTU of outgoing interface.
Received Datagrams Discarded Number of input datagrams discarded because no route could be found to transmit
Due To No Route them to their destination.
Received Datagrams With Number of locally-addressed datagrams received successfully but discarded
Unknown Protocol because of an unknown or unsupported protocol. This counter increments at the
interface to which these datagrams were addressed, which might not be necessarily
the input interface for some of the datagrams.
Received Datagrams Discarded Number of input datagrams discarded because the IPv6 address in their IPv6
Due To Invalid Address header's destination field was not a valid address to be received at this entity. This
count includes invalid addresses (for example, ::0) and unsupported addresses
(for example, addresses with unallocated prefixes). Forentities which are not IPv6
routers and therefore do not forward datagrams, this counter includes datagrams
discarded because the destination address was not a local address.
Received Datagrams Discarded Number of input datagrams discarded because datagram frame didn't carry enough
Due To Truncated Data data.
IPv6 Commands 858
