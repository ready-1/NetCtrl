# ip_access_control_list_commands

Pages: 970-982

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Redirect Interface........................0/34
Committed Rate...........................32
Committed Burst Size..................16
ACL hit count ...............................0
IP Access Control List Commands
This section describes the commands you use to configure IP Access Control List (ACL)
settings. IP ACLs ensure that only authorized users have access to specific resources and
block any unwarranted attempts to reach network resources.
The following rules apply to IP ACLs:
• The maximum number of ACLs you can create is hardware dependent. The limit applies
to all ACLs, regardless of type.
• The maximum number of rules per IP ACL is hardware dependent.
• If you configure a MAC ACL on an interface, you cannot configure an IP ACL on the same
interface.
• Wildcard masking for ACLs operates differently from a subnet mask. A wildcard mask is
in essence the inverse of a subnet mask. With a subnet mask, the mask has ones (1's) in
the bit positions that are used for the network address, and has zeros (0's) for the bit
positions that are not used. In contrast, a wildcard mask has (0’s) in a bit position that
must be checked. A 1 in a bit position of the ACL mask indicates the corresponding bit
can be ignored.
access-list
This command creates an IP Access Control List (ACL) that is identified by the access list
number, which is 1-99 for standard ACLs or 100-199 for extended ACLs. The table with
parameters and descriptions on page 971 describes the parameters for the access-list
command.
IP Standard ACL:
Format access-list 1-99 {remark comment} | {[sequence-number]}] {deny | permit}
{every | srcip srcmask | host srcip} [time-range time-range-name] [log]
[assign-queue queue-id] [{mirror | redirect} {unit/slot/port | lag
lag-group-id}] [rate-limit rate burst-size]
Mode Global Config
Quality of Service Commands 970

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
IP Extended ACL:
Format access-list 100-199 {remark comment} | {[sequence-number]} [rule 1-1023]
{deny | permit} {every | {{eigrp | gre | icmp | igmp | ip | ipinip | ospf |
pim | tcp | udp | 0 -255} {srcip srcmask |any | host srcip} [range {portkey |
startport} {portkey | endport} {eq | neq | lt | gt} {portkey | 0-65535}
{dstip dstmask | any | host dstip} [{range {portkey | startport} {portkey |
endport} | {eq | neq | lt | gt} {portkey | 0-65535}] [flag [+fin | -fin]
[+syn | -syn] [+rst | -rst] [+psh | -psh] [+ack | -ack] [+urg | -urg]
[established]] [icmp-type icmp-type [icmp-code icmp-code] | icmp-message
icmp-message] [igmp-type igmp-type] [fragments] [precedence precedence | tos
tos [tosmask] | dscp dscp]}} [time-range time-range-name] [log] [assign-queue
queue-id] [{mirror | redirect} {unit/slot/port | lag lag-group-id}]
[rate-limit rate burst-size]
Mode Global Config
IPv4 extended ACLs have the following limitations for egress ACLs:
• Match on port ranges is not supported.
• The rate-limit command is not supported.
Parameter Description
remark comment Use the remark keyword and comment parameter to add a comment
(remark) to an IP standard or IP extended ACL. The remarks make the ACL
easier to understand and scan. Each remark is limited to 100 characters. A
remark can consist of characters in the range A–Z, a–z, and 0–9, and of
special characters: space, hyphen, underscore. Remarks are displayed
only in the output of the show running configuration command. For
each IP standard or IP extended ACL rule, you can add one remark. You
can remove only remarks that are not associated with a rule. Remarks that
are associated with a rule are removed when the rule is removed.
sequence-number The sequence-number parameter specifies the sequence number for the
ACL rule. Either you define the sequence number or is it is generated.
If no sequence number exists for a rule, a sequence number that is 10
greater than the last sequence number in the ACL is used and the rule is
placed at the end of the list. If this is the first ACL rule in the ACL, a
sequence number of 10 is assigned. If the calculated sequence number
exceeds the maximum sequence number value, the creation of the ACL
rule fails. You cannot create a rule that duplicates an already existing one
and you cannot configure a rule with a sequence number that is already
used for another rule.
For example, if you add new ACL rule to the ACL without specifying a
sequence number, the rule is placed at the bottom of the list. By changing
the sequence number, you can move the ACL rule to a different position in
the ACL.
1-99 or 100-199 Range 1 to 99 is the access list number for an IP standard ACL. Range 100
to 199 is the access list number for an IP extended ACL.
Quality of Service Commands 971

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
{deny | permit} Specifies whether the IP ACL rule permits or denies an action.
Note: For 5630x and 5650x-based systems, assign-queue, redirect, and
mirror attributes are configurable for a deny rule, but they have no
operational effect.
every Match every packet.
{eigrp | gre | icmp | igmp | ip | Specifies the protocol to filter for an extended IP ACL rule.
ipinip | ospf | pim | tcp | udp |
0-255}
srcip srcmask | any | host scrip Specifies a source IP address and source netmask for match condition of
the IP ACL rule.
Specifying any specifies srcip as 0.0.0.0 and srcmask as
255.255.255.255.
Specifying host A.B.C.D specifies srcip as A.B.C.D and srcmask as
0.0.0.0.
Note: This option is available only if the protocol is TCP or UDP.
[{range {portkey | startport}
{portkey | endport} | {eq | neq | Specifies the source layer 4 port match condition for the IP ACL rule. You
lt | gt} {portkey | 0-65535}] can use the port number, which ranges from 0-65535, or you specify the
portkey, which can be one of the following keywords:
• For TCP: domain, echo, ftp, ftp-data, http, smtp, telnet, www,
pop2, or pop3.
• For UDP: domain, echo, ntp, rip, snmp, tftp, time, or who.
For both TCP and UDP, each of these keywords translates into its
equivalent port number, which is used as both the start and end of a port
range.
If range is specified, the IP ACL rule matches only if the layer 4 port
number falls within the specified portrange. The startport and endport
parameters identify the first and last ports that are part of the port range.
They have values from 0 to 65535. The ending port must have a value
equal or greater than the starting port. The starting port, ending port, and all
ports in between will be part of the layer 4 port range.
When eq is specified, the IP ACL rule matches only if the layer 4 port
number is equal to the specified port number or portkey.
When lt is specified, IP ACL rule matches if the layer 4 port number is less
than the specified port number or portkey. It is equivalent to specifying the
range as 0 to <specified port number – 1>.
When gt is specified, the IP ACL rule matches if the layer 4 port number is
greater than the specified port number or portkey. It is equivalent to
specifying the range as <specified port number + 1> to 65535.
When neq is specified, IP ACL rule matches only if the layer 4 port number
is not equal to the specified port number or portkey.
Two rules are added in the hardware one with range equal to 0 to
<specified port number - 1> and one with range equal to <specified port
number + 1 to 65535>.
Note: Port number matches only apply to unfragmented or first fragments.
Quality of Service Commands 972

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
dstip dstmask |any | host dstip Specifies a destination IP address and netmask for match condition of the
IP ACL rule.
Specifying any implies specifying dstip as 0.0.0.0 and dstmask as
255.255.255.255.
Specifying host A.B.C.D implies dstip as A.B.C.D and dstmask as
0.0.0.0.
[precedence precedence | tos tos Specifies the TOS for an IP ACL rule depending on a match of precedence
[tosmask] | dscp dscp] or DSCP values using the parameters precedence, tos or dscp.
tosmask is an optional parameter.
Note: This option is available only if the protocol is tcp.
flag [+fin | -fin] [+syn | -syn]
[+rst | -rst] [+psh | -psh] [+ack Specifies that the IP ACL rule matches on the TCP flags.
| -ack] [+urg | -urg]
When +<tcpflagname> is specified, a match occurs if the specified
[established]
<tcpflagname> flag is set in the TCP header.
When -<tcpflagname> is specified, a match occurs if the specified
<tcpflagname> flag is not set in the TCP header.
When established is specified, a match occurs if the specified RST or ACK
bits are set in the TCP header. Two rules are installed in the hardware
when the established option is specified.
Note: This option is available only if the protocol is icmp.
[icmp-type icmp-type [icmp-code
icmp-code] | icmp-message Specifies a match condition for ICMP packets.
icmp-message]
When icmp-type is specified, the IP ACL rule matches on the specified
I CMP message type, a number from0 to255.
When icmp-code is specified, the IP ACL rule matches on the specified
I CMP message code, a number from0 to255.
Specifying icmp-message implies that both icmp-type and icmp-code
are specified. The following icmp-message options are supported: echo,
echo-reply, host-redirect, mobile-redirect, net-redirect,
net-unreachable, redirect, packet-too-big,
port-unreachable, source-quench, router-solicitation,
router-advertisement, time-exceeded, ttl-exceeded, and
unreachable.
igmp-type igmp-type This option is available only if the protocol is igmp.
When igmp-type is specified, the IP ACL rule matches on the specified
I GMP message type, a number from0 to255.
fragments Specifies that the IP ACL rule matches on fragmented IP packets.
[log] Specifies that this rule is to be logged.
[time-range time-range-name] Allows imposing time limitation on the ACL rule as defined by the
parameter time-range-name. If a time range with the specified name
does not exist and the ACL containing this ACL rule is applied to an
interface or bound to a VLAN, then the ACL rule is applied immediately. If a
time range with specified name exists and the ACL containing this ACL rule
is applied to an interface or bound to a VLAN, the ACL rule is applied when
the time-range with specified name becomes active. The ACL rule is
removed when the time-range with specified name becomes inactive. For
information about configuring time ranges, see Time Range Commands for
Time-Based ACLs on page995.
Quality of Service Commands 973

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
[assign-queue queue-id] Specifies the assign-queue, which is the queue identifier to which packets
matching this rule are assigned.
[{mirror | redirect} Specifies the mirror or redirect interface that is the unit/slot/port or
{unit/slot/port | lag lag-group-id to which packets matching this rule are copied or
lag-group-id}] forwarded.
[rate-limit rate burst-size] Specifies the allowed rate of traffic as per the configured rate in kbps, and
burst-size in kbytes.
no access-list
This command deletes an IP ACL that is identified by the parameter accesslistnumber
from the system. The range for accesslistnumber is 1–99 for standard access lists and
100–199 for extended access lists.
Format no access-list accesslistnumber
Mode Global Config
ip access-list
This command creates an extended IP Access Control List (ACL) identified by name,
consisting of classification fields defined for the IP header of an IPv4 frame. The name
parameter is a case-sensitive alphanumeric string from 1 to 31 characters uniquely
identifying the IP access list. The rate-limit attribute configures the committed rate and the
committed burst size.
If an IP ACL by this name already exists, this command enters IPv4-Access_List config mode
to allow updating the existing IP ACL.
Note: The CLI mode changes to IPv4-Access-List Config mode when you
successfully execute this command.
Format ip access-list name
Mode Global Config
no ip access-list
This command deletes the IP ACL identified by name from the system.
Format no ip access-list name
Mode Global Config
Quality of Service Commands 974

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip access-list resequence
Use this command to renumber the sequence of the entries for a specified IP access list with
a specified increment value, starting from a specified sequence number. That is, with this
command you can change the sequence numbers of ACL rules in the ACL and, therefore,
change the order in which entries are applied. This command is not saved in the startup
configuration and does not display in the running configuration.
Note: If the generated sequence number exceeds the maximum sequence
number, the ACL rule creation fails and an informational message
displays.
Default 10
Format ip access-list resequence {name | id} starting-sequence-number increment
Mode Global Config
Parameter Description
name The name of the access control list.
id The ID of the access control list.
starting-sequence- The sequence number from which to start the renumbering. The range is 1–2147483647. The
number default is 10.
increment The value with which the sequence numbers must be incremented. The range is 1–2147483647.
The default is 10.
ip access-list rename
This command changes the name of an IP Access Control List (ACL). The name parameter
is the names of an existing IP ACL. The newname parameter is a case-sensitive
alphanumeric string from 1 to 31 characters uniquely identifying the IP access list.
This command fails is an IP ACL by the name that is defined by newname already exists.
Format ip access-list rename name newname
Mode Global Config
[sequence-number] {deny | permit} (IP ACL)
This command creates a new rule for the current IP access list. Each rule is appended to the
list of configured rules for the list. A rule may either deny or permit traffic according to the
specified classification fields. At a minimum, either the every keyword or the protocol, source
address, and destination address values must be specified. The source and destination IP
address fields may be specified using the keyword any to indicate a match on any value in
that field. The remaining command parameters are all optional, but the most frequently used
parameters appear in the same relative order as shown in the command format.
Quality of Service Commands 975

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format [sequence-number] {deny | permit} {every | {{eigrp | gre | icmp | igmp | ip | ipinip | ospf | pim | tcp | udp
| 0-255} {srcip srcmask | any | host srcip} [{range {portkey | startport} {portkey | endport}
| {eq | neq | lt | gt} {portkey | 0-65535}] {dstip dstmask | any | host dstip} [{range {portkey |
startport} {portkey | endport} | {eq | neq | lt | gt} {portkey | 0-65535}] [flag [+fin | -fin] [+syn |
-syn] [+rst | -rst] [+psh | -psh] [+ack | -ack] [+urg | -urg] [established]] [icmp-type icmp-type [icmp-code
icmp-code] | icmp-message icmp-message] [igmp-type igmp-type] [fragments] [precedence
precedence | tos tos [tosmask] | dscp dscp]}} [time-range time-range-name] [log] [assign-queue
queue-id] [{mirror | redirect} {unit/slot/port | lag lag-group-id}] [rate-limit rate
burst-size]
Mode Ipv4-Access-List Config
Note: An implicit deny all IP rule always terminates the access list.
Note: The mirror parameter allows the traffic matching this rule to be
copied to the specified unit/slot/port, while the redirect
parameter allows the traffic matching this rule to be forwarded to the
specified unit/slot/port. The assign-queue and redirect
parameters are only valid for a permit rule.
For IPv4, the following are not supported for egress ACLs:
• A match on port ranges.
• The rate-limit command.
The time-range parameter allows imposing time limitation on the IP ACL rule as defined by
the specified time range. If a time range with the specified name does not exist and the ACL
containing this ACL rule is applied to an interface or bound to a VLAN, then the ACL rule is
applied immediately. If a time range with specified name exists and the ACL containing this
ACL rule is applied to an interface or bound to a VLAN, then the ACL rule is applied when the
time-range with specified name becomes active. The ACL rule is removed when the
time-range with specified name becomes inactive. For information about configuring time
ranges, see Time Range Commands for Time-Based ACLs on page995.
The assign-queue parameter allows specification of a particular hardware queue for
handling traffic that matches this rule. The allowed queue-id value is 0-(n-1), in which n is
the number of user configurable queues available for the hardware platform. The
assign-queue parameter is valid only for a permit rule.
Quality of Service Commands 976

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The permit command’s optional attribute rate-limit allows you to permit only the
allowed rate of traffic as per the configured rate in kbps, and burst-size in kbytes.
Table 14. IP ACL command parameters
Parameter Description
sequence-number The sequence-number parameter specifies the sequence
number for the ACL rule. Either you define the sequence number
or is it is generated.
If no sequence number exists for a rule, a sequence that is 10
greater than the last sequence number in the ACL is used and the
rule is placed at the end of the list. If this is the first ACL rule in the
ACL, a sequence number of 10 is assigned. If the calculated
sequence number exceeds the maximum sequence number
value, the creation of the ACL rule fails. You cannot create a rule
that duplicates an already existing one and you cannot configure
a rule with a sequence number that is already used for another
rule.
For example, if you add new ACL rule to the ACL without
specifying a sequence number, the rule is placed at the bottom of
the list. By changing the sequence number, you can move the
ACL rule to a different position in the ACL.
{deny | permit} Specifies whether the IP ACL rule permits or denies the matching
traffic.
every Match every packet.
{eigrp | gre | icmp | igmp | ip | ipinip Specifies the protocol to match for the IP ACL rule.
| ospf | pim | tcp | udp | 0-255}
srcip srcmask | any | host srcip Specifies a source IP address and source netmask to match for
the IP ACL rule.
Specifying “any” implies specifying srcip as “0.0.0.0” and
srcmask as “255.255.255.255”.
Specifying “host A.B.C.D” implies srcip as “A.B.C.D” and
srcmask as “0.0.0.0”.
Quality of Service Commands 977

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 14. IP ACL command parameters (continued)
Parameter Description
Note: This option is available only if the protocol is tcp or udp.
[{range {portkey | startport} {portkey |
endport} | {eq | neq | lt | gt} {portkey Specifies the layer 4 port match condition for the IP ACL rule. Port
| 0-65535}] number can be used, which ranges from 0-65535, or the portkey,
which can be one of the following keywords:
For tcp protocol: domain, echo, ftp, ftp-data, http, smtp,
telnet, www, pop2, or pop3.
For udp protocol: domain, echo, ntp, rip, snmp, tftp, time,
or who.
Each of these keywords translates into its equivalent port number.
When range is specified, the IP ACL rule matches only if the
layer 4 port number falls within the specified port range. The
startport and endport parameters identify the first and last
ports that are part of the port range. They have values from 0 to
65535. The ending port must have a value equal to or greater
than the starting port. The starting port, ending port, and all ports
in between will be part of the layer 4 port range.
When eq is specified, IP ACL rule matches only if the layer 4 port
number is equal to the specified port number or portkey.
When lt is specified, IP ACL rule matches if the layer 4 port
number is less than the specified port number or portkey. It is
equivalent to specifying the range as 0 to <specified port number
– 1>.
When gt is specified, IP ACL rule matches if the layer 4 port
number is greater than the specified port number or portkey. It is
equivalent to specifying the range as <specified port number + 1>
to 65535.
When neq is specified, IP ACL rule matches only if the layer 4
port number is not equal to the specified port number or port key.
Two rules are added in the hardware one with range equal to 0 to
<specified port number - 1> and one with range equal to
<specified port number + 1 to 65535>.
Note: Port number matches only apply to unfragmented or first
fragments.
dstip dstmask | any | host dstip Specifies a destination IP address and netmask for match
condition of the IP ACL rule.
Specifying any implies specifying dstip as 0.0.0.0 and dstmask
as 255.255.255.255.
Specifying host A.B.C.D implies dstip as A.B.C.D and dstmask
as 0.0.0.0.
[precedence precedence | tos tos Specifies the TOS for an IP ACL rule depending on a match of
[tosmask] | dscp dscp] precedence or DSCP values using the parameters precedence,
tos or dscp. tosmask is an optional parameter.
Quality of Service Commands 978

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 14. IP ACL command parameters (continued)
Parameter Description
flag [+fin | -fin] [+syn | -syn] [+rst | Specifies that the IP ACL rule matches on the tcp flags.
-rst] [+psh | -psh] [+ack | -ack] [+urg When +<tcpflagname> is specified, a match occurs if specified
| -urg] [established] <tcpflagname> flag is set in the TCP header.
When -<tcpflagname> is specified, a match occurs if specified
<tcpflagname> flag is NOT set in the TCP header.
When established is specified, a match occurs if either the
specified RST or ACK bits are set in the TCP header. Two rules
are installed in hardware to when the established option is
specified.
This option is available only if protocol is tcp.
Note: This option is available only if the protocol is ICMP.
[icmp-type icmp-type [icmp-code
icmp-code] | icmp-message icmp-message] Specifies a match condition for ICMP packets.
When icmp-type is specified, IP ACL rule matches on the
specified ICMP message type, a number from0 to255.
When icmp-code is specified, IP ACL rule matches on the
specified ICMP message code, a number from0 to255.
Specifying icmp-message implies both icmp-type and
icmp-code are specified. The following icmp-message options
are supported: echo, echo-reply, host-redirect,
mobile-redirect, net-redirect, net-unreachable,
redirect, packet-too-big, port-unreachable,
source-quench, router-solicitation,
router-advertisement, time-exceeded, ttl-exceeded,
and unreachable.
The ICMP message is decoded into corresponding ICMP type
and ICMP code within that ICMP type.
Note: This option is visible only if the protocol is IGMP.
igmp-type igmp-type
When igmp-type is specified, the IP ACL rule matches on the
specified IGMP message type, a number from0 to255.
fragments Specifies that the IP ACL rule matches on noninitial fragmented
packets where the fragment extension header contains a nonzero
fragment offset. The fragments keyword is an option only if the
protocol is ipv6 and the operator port-number arguments are not
specified.
log Specifies that this rule is to be logged.
time-range time-range-name Allows imposing a time limitation on the ACL rule as defined by
the parameter time-range-name. If a time range with the
specified name does not exist and the ACL containing this ACL
rule is applied to an interface or bound to a VLAN, the ACL rule is
applied immediately. If a time range with specified name exists
and the ACL containing this ACL rule is applied to an interface or
bound to a VLAN, the ACL rule is applied when the time-range
with specified name becomes active. The ACL rule is removed
when the time-range with specified name becomes inactive.
assign-queue queue-id Specifies the assign-queue, which is the queue identifier to which
packets matching this rule are assigned.
Quality of Service Commands 979

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 14. IP ACL command parameters (continued)
Parameter Description
[{mirror | redirect} {unit/slot/port | Specifies the mirror or redirect interface that is the
lag lag-group-id}] unit/slot/port or lag-group-id to which packets matching
this rule are copied or forwarded.
rate-limit rate burst-size Specifies the allowed rate of traffic as per the configured rate in
kbps, and burst-size in kbytes.
Command example:
(NETGEAR Switch) (Config)#ip access-list ip1
(NETGEAR Switch) (Config-ipv4-acl)#permit icmp any any rate-limit 32 16
(NETGEAR Switch) (Config-ipv4-acl)#exit
no sequence-number (IP ACL)
Use this command to remove the ACL rule with the specified sequence number from the
ACL.
Format no sequence-number
Modes MAC-Access-List Config
ip access-group
This command either attaches a specific IP Access Control List (ACL) identified by
accesslistnumber or name to an interface, range of interfaces, or all interfaces; or
associates it with a VLAN ID in a given direction. The parameter name is the name of the
Access Control List.
An optional sequence number may be specified to indicate the order of this IP access list
relative to other IP access lists already assigned to this interface and direction. A lower
number indicates higher precedence order. If a sequence number is already in use for this
interface and direction, the specified access list replaces the currently attached IP access list
using that sequence number. If the sequence number is not specified for this command, a
sequence number that is one greater than the highest sequence number currently in use for
this interface and direction is used.
An optional control-plane is specified to apply the ACL on CPU port. The IPv4 control packets
like RADIUS and TACACS+ are also dropped because of the implicit deny all rule added
at the end of the list. To overcome this, permit rules must be added to allow the IPv4 control
packets.
Quality of Service Commands 980

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: The control-plane keyword is available only in Global Config
mode.
Note: Depending on the platform, the out option might not be available.
Default none
Format ip access-group {accesslistnumber | name} {{control-plane| in | out} | vlan
vlan-id {in | out}} [sequence 1-4294967295]
Modes Interface Config
Global Config
Parameter Description
accesslistnumber Identifies a specific IP ACL. The range is 1 to 199.
name The name of the Access Control List.
vlan-id A VLAN ID associated with a specific IP ACL in a given direction.
sequence A optional sequence number that indicates the order of this IP access list relative to the other IP
access lists already assigned to this interface and direction. The range is 1 to 4294967295.
(NETGEAR Switch) (Config)#ip access-group ip1 control-plane
no ip access-group
This command removes a specified IP ACL from an interface.
Default none
Format no ip access-group {accesslistnumber | name} {{control-plane | in | out}|
vlan vlan-id {in | out}}
Mode Interface Config
Global Config
Command example:
(NETGEAR Switch)(Config)#no ip access-group ip1 control-plane
Quality of Service Commands 981

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
acl-trapflags
This command enables the ACL trap mode.
Default disabled
Format acl-trapflags
Mode Global Config
no acl-trapflags
This command disables the ACL trap mode.
Format no acl-trapflags
Mode Global Config
show ip access-lists
Use this command to view summary information about all IP ACLs that are configured on the
switch. To view more detailed information about a specific access list, specify the ACL
number or name that is used to identify the IP ACL. The command output displays the
committed rate, committed burst size, and the number of packets that match a configured
ACL rule within an ACL (referred to as ACL hit count).
Format show ip access-lists [accesslistnumber | name]
Mode Privileged EXEC
Term Definition
ACL ID/Name Identifies the configured ACL number or name.
Rules Identifies the number of rules configured for the ACL.
Direction Shows whether the ACL is applied to traffic coming into the interface (ingress) or
leaving the interface (egress).
Interface(s) Identifies the interface(s) to which the ACL is applied (ACL interface bindings).
VLAN(s) Identifies the VLANs to which the ACL is applied (ACL VLAN bindings).
If you specify an IP ACL number or name, the following information displays:
Note: Only the access list fields that you configure are displayed. Thus, the
command output varies based on the match criteria configured within
the rules of an ACL.
Quality of Service Commands 982
