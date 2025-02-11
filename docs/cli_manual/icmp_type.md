# icmp_type

Pages: 983-984

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Rule Number The number identifier for each rule that is defined for the IP ACL.
Action The action associated with each rule. The possible values are Permit or Deny.
Match All Indicates whether this access list applies to every packet. Possible values are True or
False.
Protocol The protocol to filter for this rule.
Note: This is shown only if the protocol is ICMP.
ICMP Type
The ICMP message type for this rule.
Starting Source L4 port The starting source layer 4 port.
Ending Source L4 port The ending source layer 4 port.
Starting Destination L4 port The starting destination layer 4 port.
Ending Destination L4 port The ending destination layer 4 port.
Note: This is shown only if the protocol is ICMP.
ICMP Code
The ICMP message code for this rule.
Fragments If the ACL rule matches on fragmented IP packets.
Committed Rate The committed rate defined by the rate-limit attribute.
Committed Burst Size The committed burst size defined by the rate-limit attribute.
Source IP Address The source IP address for this rule.
Source IP Mask The source IP Mask for this rule.
Source L4 Port Keyword The source port for this rule.
Destination IP Address The destination IP address for this rule.
Destination IP Mask The destination IP Mask for this rule.
Destination L4 Port Keyword The destination port for this rule.
IP DSCP The value specified for IP DSCP.
IP Precedence The value specified IP Precedence.
IP TOS The value specified for IP TOS.
Log Displays when you enable logging for the rule.
Assign Queue The queue identifier to which packets matching this rule are assigned.
Mirror Interface The unit/slot/port to which packets matching this rule are copied.
Redirect Interface The unit/slot/port to which packets matching this rule are forwarded.
Time Range Name Displays the name of the time-range if the IP ACL rule has referenced a time range.
Quality of Service Commands 983

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Rule Status Status (Active/Inactive) of the IP ACL rule.
ACL Hit Count The number of packets that match a configured ACL rule within an ACL (referred to as
ACL hit count). The counter resets to 0 when the maximum value is reached. A
dedicated counter exists for each ACL rule. ACL counters do not interact with PBR
counters.
For an ACL with multiple rules, if a match occurs for a specific rule, the counter that is
associated with this rule increments. For example, if an ACL includes three rules,
when a match occurs for rule 2, the counter for rule 3 does not increment.
For ACL counters, if an ACL rule is configured without a rate limit condition, the
counter shows the number of forwarded and or discarded packets. (For example, for a
burst of 100 packets, the counter shows 100.)
If the ACL rule is configured with a rate limit condition, the counter shows the number
of packets that match the condition:
• If the packets are sent at a rate that is lower than the configured rate limit, the
counter displays the number of packets that match the condition.
• If the packets are sent at a rate that exceeds the configured rate limit, the counter
still displays the number of packets that match the condition, even though packets
are dropped beyond the configured limit. In this situation, the number of packets
that match the condition equals the rate at which the packets are sent.
For example, if the rate limit condition is 10 kbps but the matching traffic is sent at
100 kbps, the counter increments with 100 kbps.
Either way, only the number of packets that match the condition is reflected in the
counter, irrespective of whether they are dropped or forwarded.
ACL counters do not interact with diffserv policies.
(NETGEAR Switch) #show ip access-lists ip1
ACL Name: ip1
Inbound Interface(s): 1/0/30
Rule Number: 1
Action......................................... permit
Match All...................................... FALSE
Protocol....................................... 1(icmp)
Committed Rate................................. 32
Committed Burst Size........................... 16
ACL hit count ...............................0
show access-lists
This command displays IP ACLs, IPv6 ACLs, and MAC access control lists information for a
designated interface and direction. The unit/slot/port parameter specifies a valid
interface for the system. Instead of unit/slot/port, lag lag-intf-num can be used as
an alternate way to specify the LAG interface, in which lag-intf-num is the LAG port
number.
Quality of Service Commands 984
