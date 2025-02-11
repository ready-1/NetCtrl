# a_cl_type_a_cl_id_sequence_number_--------_-------------------------------_---------------_778195a2

Pages: 985-1001

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Use the control-plane keyword to display the ACLs applied on the CPU port.
Format show access-lists interface {unit/slot/port {in | out | control-plane}}
Mode Privileged EXEC
Term Definition
ACL Type Type of access list (IP, IPv6, or MAC).
ACL ID Access List name for a MAC or IPv6 access list or the numeric identifier for an IP access list.
Sequence Number A sequence number indicates the order of the access list relative to other access lists already
assigned to this interface and direction.
in or out • in – Display Access List information for a particular interface and the in direction.
• out – Display Access List information for a particular interface and the out direction.
Command example:
(NETGEAR Switch) #show access-lists interface control-plane
A CL Type A CL ID Sequence Number
-------- ------------------------------- ---------------
I Pv6 i p61 1
show access-lists vlan
This command displays Access List information for a particular VLAN ID. The vlan-id
parameter is the VLAN ID of the VLAN with the information to view. The in and out options
specify the direction of the VLAN ACL information to view.
Format show access-lists vlan vlan-id [in | out]
Mode Privileged EXEC
Term Definition
ACL Type Type of access list (IP, IPv6, or MAC).
ACL ID Access List name for a MAC or IPv6 access list or the numeric identifier for an IP access list.
Sequence Number A sequence number indicates the order of the access list relative to other access lists already
assigned to this interface and direction.
in or out • in – Display Access List information for a particular interface and the in direction.
• out – Display Access List information for a particular interface and the out direction.
Quality of Service Commands 985

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
IPv6 Access Control List Commands
This section describes the commands you use to configure IPv6 Access Control List (ACL)
settings. IPv6 ACLs ensure that only authorized users have access to specific resources and
block any unwarranted attempts to reach network resources.
The following rules apply to IPv6 ACLs:
• The maximum number of ACLs you create is 100, regardless of type.
• The system supports only Ethernet II frame types.
• The maximum number of rules per IPv6 ACL is hardware dependent.
ipv6 access-list
This command creates an IPv6 Access Control List (ACL) identified by name, consisting of
classification fields defined for the IP header of an IPv6 frame. The name parameter is a
case-sensitive alphanumeric string from 1 to 31 characters uniquely identifying the IPv6
access list. The rate-limit attribute configures the committed rate and the committed burst
size.
If an IPv6 ACL by this name already exists, this command enters IPv6-Access-List config
mode to allow updating the existing IPv6 ACL.
Note: The CLI mode changes to IPv6-Access-List Config mode when you
successfully execute this command.
Format ipv6 access-list name
Mode Global Config
no ipv6 access-list
This command deletes the IPv6 ACL identified by name from the system.
Format no ipv6 access-list name
Mode Global Config
ipv6 access-list rename
This command changes the name of an IPv6 ACL. The name parameter is the name of an
existing IPv6 ACL. The newname parameter is a case-sensitive alphanumeric string from 1 to
31 characters uniquely identifying the IPv6 access list.
This command fails is an IPv6 ACL by the name that is specified by the newname argument
already exists.
Quality of Service Commands 986

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format ipv6 access-list rename name newname
Mode Global Config
ipv6 access-list resequence
Use this command to renumber the sequence of the entries for a specified IPv6 access list
with a specified increment value, starting from a specified sequence number. That is, with
this command you can change the sequence numbers of ACL rules in the ACL and,
therefore, change the order in which entries are applied. This command is not saved in the
startup configuration and does not display in the running configuration.
Note: If the generated sequence number exceeds the maximum sequence
number, the ACL rule creation fails and an informational message
displays.
Default 10
Format ipv6 access-list resequence {name | id} starting-sequence-number increment
Mode Global Config
Parameter Description
name The name of the access control list.
id The ID of the access control list.
starting-sequence- The sequence number from which to start the renumbering. The range is 1–2147483647. The
number default is 10.
increment The value with which the sequence numbers must be incremented. The range is 1–2147483647.
The default is 10.
[sequence-number] {deny | permit} (IPv6 ACL)
This command creates a new rule for the current IPv6 access list. Each rule is appended to
the list of configured rules for the list. A rule may either deny or permit traffic according to the
specified classification fields. At a minimum, either the every keyword or the protocol,
source address, and destination address values must be specified. The source and
destination IPv6 address fields may be specified using the keyword any to indicate a match
on any value in that field. The remaining command parameters are all optional, but the most
frequently used parameters appear in the same relative order as shown in the command
format.
Quality of Service Commands 987

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format [sequence-number] {deny | permit} {every | {{icmpv6 | ipv6 | tcp | udp | 0-255}
{source-ipv6-prefix/prefix-length | any | host source-ipv6-address} [eq {portkey |
0-65535}] {destination-ipv6-prefix/prefix-length | any | host
destination-ipv6-address} [eq {portkey | 0-65535}] [flag [+fin | -fin] [+syn | -syn] [+rst | -rst]
[+psh | -psh] [+ack | -ack] [+urg | -urg] [established]] [flow-label value] [icmp-type icmp-type
[icmp-code icmp-code] | icmp-message icmp-message] [routing] [fragments] [sequence
sequence-number] [dscp dscp]}} [log] [assign-queue queue-id] [{mirror | redirect}
unit/slot/port] [rate-limit rate burst-size]
Mode IPv6-Access-List Config
Note: An implicit deny all IPv6 rule always terminates the access list.
The time-range parameter allows imposing time limitation on the IPv6 ACL rule as defined
by the parameter time-range-name. If a time range with the specified name does not exist
and the IPv6 ACL containing this ACL rule is applied to an interface or bound to a VLAN, then
the ACL rule is applied immediately. If a time range with specified name exists and the IPv6
ACL containing this ACL rule is applied to an interface or bound to a VLAN, then the ACL rule
is applied when the time-range with specified name becomes active. The ACL rule is
removed when the time-range with specified name becomes inactive. For information about
configuring time ranges, see Time Range Commands for Time-Based ACLs on page995.
The assign-queue parameter allows specification of a particular hardware queue for
handling traffic that matches this rule. The allowed queue-id value is 0-(n-1), in which n is
the number of user configurable queues available for the hardware platform. The
assign-queue parameter is valid only for a permit rule.
The mirror parameter allows the traffic matching this rule to be copied to the specified
unit/slot/port, while the redirect parameter allows the traffic matching this rule to be
forwarded to the specified unit/slot/port. The assign-queue and redirect
parameters are only valid for a permit rule.
The permit command’s optional attribute rate-limit allows you to permit only the allowed
rate of traffic as per the configured rate in kbps, and burst-size in kbytes.
IPv6 ACLs have the following limitations:
• Port ranges are not supported for egress IPv6 ACLs.
• The rate-limit command is not supported for egress IPv6 ACLs.
Quality of Service Commands 988

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 15. IPv6 ACL command parameters
Parameter Description
sequence-number The sequence-number parameter specifies the sequence
number for the ACL rule. Either you define the sequence number
or is it is generated.
If no sequence number exists for a rule, a sequence number that
is 10 greater than the last sequence number in the ACL is used
and the rule is placed at the end of the list. If this is the first ACL
rule in the ACL, a sequence number of 10 is assigned. If the
calculated sequence number exceeds the maximum sequence
number value, the creation of the ACL rule fails. You cannot
create a rule that duplicates an already existing one and you
cannot configure a rule with a sequence number that is already
used for another rule.
For example, if you add new ACL rule to the ACL without
specifying a sequence number, the rule is placed at the bottom of
the list. By changing the sequence number, you can move the
ACL rule to a different position in the ACL.
{deny | permit} Specifies whether the IPv6 ACL rule permits or denies the
matching traffic.
every Specifies to match every packet.
{protocolkey | number} Specifies the protocol to match for the IPv6 ACL rule. The current
list is: icmpv6, ipv6, tcp, and udp.
source-ipv6-prefix/prefix-length | any For source-ipv6-prefix/prefix-length, specify a source
| host source-ipv6-address IPv6 source address and prefix length to match for the IPv6 ACL
rule.
Specifying any implies specifying ::/0
Specifying host source-ipv6-address implies matching the
specified IPv6 address.
The source-ipv6-address argument must be in the form
documented in RFC 2373 where the address is specified in
hexadecimal using 16-bit values between colons.
Note: This option is available only if the protocol is TCP or UDP.
[eq {portkey | 0-65535}]
Specifies the layer 4 port match condition for the IPv6 ACL rule. A
port number can be used, in the range 0-65535, or the portkey,
which can be one of the following keywords:
For TCP: domain, echo, ftp, ftp-data, http, smtp, telnet,
www, pop2, or pop3.
For UDP: domain, echo, ntp, rip, snmp, tftp, time, or who.
Each of these keywords translates into its equivalent port number.
When eq is specified, the IPv6 ACL rule matches only if the
l ayer4 port number is equal to the specified port number or
portkey.
Two rules are added in the hardware one with range equal to 0 to
<specified port number - 1> and one with range equal to
<specified port number + 1 to 65535>
Quality of Service Commands 989

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 15. IPv6 ACL command parameters (continued)
Parameter Description
destination-ipv6-prefix/prefix-length | For destination-ipv6-prefix/prefix-length, specify a
any | host destination-ipv6-address destination IPv6 source address and prefix length to match for the
IPv6 ACL rule.
Specifying any implies specifying ::/0
Specifying host destination-ipv6-address implies
matching the specified IPv6 address.
This destination-ipv6-address argument must be in the
form documented in RFC 2373 where the address is specified in
hexadecimal using 16-bit values between colons.
[dscp dscp] Specifies the dscp value to match for the IPv6 rule.
flag [+fin | -fin] [+syn | -syn] [+rst | Specifies that the IPv6 ACL rule matches on the tcp flags.
-rst] [+psh | -psh] [+ack | -ack] [+urg When +<tcpflagname> is specified, a match occurs if specified
| -urg] [established] <tcpflagname> flag is set in the TCP header.
When “-<tcpflagname>” is specified, a match occurs if specified
<tcpflagname> flag is not set in the TCP header.
When established is specified, a match occurs if specified either
RST or ACK bits are set in the TCP header.
Two rules are installed in hardware to when “established” option is
specified.
This option is visible only if protocol is tcp.
Note: This option is available only if the protocol is icmpv6.
[icmp-type icmp-type [icmp-code
icmp-code] | icmp-message icmp-message] Specifies a match condition for ICMP packets.
When icmp-type is specified, IPv6 ACL rule matches on the
s pecified ICMP message type, a number from0 to255.
When icmp-code is specified, IPv6 ACL rule matches on the
s pecified ICMP message code, a number from0 to255.
Specifying icmp-message implies both icmp-type and
icmp-code are specified. The following icmp-message options
are supported: destination-unreachable, echo-reply,
echo-request, header, hop-limit, mld-query,
mld-reduction, mld-report, nd-na, nd-ns, next-header,
no-admin, no-route, packet-too-big,
port-unreachable, router-solicitation,
router-advertisement, router-renumbering,
time-exceeded, and unreachable.
The ICMP message is decoded into the corresponding ICMP type
and ICMP code within that ICMP type.
fragments Specifies that IPv6 ACL rule matches on fragmented IPv6 packets
(Packets that have the next header field is set to 44).
routing Specifies that IPv6 ACL rule matches on IPv6 packets that have
routing extension headers (the next header field is set to 43).
log Specifies that this rule is to be logged.
Quality of Service Commands 990

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 15. IPv6 ACL command parameters (continued)
Parameter Description
time-range time-range-name Allows imposing a time limitation on the ACL rule as defined by
the parameter time-range-name. If a time range with the
specified name does not exist and the ACL containing this ACL
rule is applied to an interface or bound to a VLAN, the ACL rule is
applied immediately. If a time range with the specified name exists
and the ACL containing this ACL rule is applied to an interface or
bound to a VLAN, the ACL rule is applied when the time-range
with the specified name becomes active. The ACL rule is removed
when the time-range with specified name becomes inactive.
assign-queue queue-id Specifies the assign-queue, which is the queue identifier
(queue-id) to which packets matching this rule are assigned.
{mirror | redirect} unit/slot/port Specifies the mirror or redirect interface that is the unit/slot/port to
which packets matching this rule are copied or forwarded,
respectively.
rate-limit rate burst-size Specifies the allowed rate of traffic as per the configured rate in
kbps, and burst-size in kbytes.
Command example:
(NETGEAR Switch) (Config)#ipv6 access-list ip61
(NETGEAR Switch) (Config-ipv6-acl)#permit udp any any rate-limit 32 16
(NETGEAR Switch) (Config-ipv6-acl)#exit
no sequence-number (IPv6 ACL)
Use this command to remove the ACL rule with the specified sequence number from the
ACL.
Format no sequence-number
Modes MAC-Access-List Config
ipv6 traffic-filter
This command either attaches a specific IPv6 ACL identified by name to an interface or
range of interfaces, or associates it with a VLAN ID in a given direction. The name parameter
must be the name of an existing IPv6 ACL.
An optional sequence number may be specified to indicate the order of this mac access list
relative to other IPv6 access lists already assigned to this interface and direction. A lower
number indicates higher precedence order. If a sequence number is already in use for this
interface and direction, the specified IPv6 access list replaces the currently attached IPv6
access list using that sequence number. If the sequence number is not specified for this
command, a sequence number that is one greater than the highest sequence number
currently in use for this interface and direction is used.
Quality of Service Commands 991

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
This command specified in Interface Config mode only affects a single interface, whereas the
Global Config mode setting is applied to all interfaces. The vlan keyword and vlan-id
argument are valid only in the Global Config mode. The Interface Config mode command is
only available on platforms that support independent per-port class of service queue
configuration.
An optional control-plane is specified to apply the ACL on CPU port. The IPv6 control packets
like IGMPv6 are also dropped because of the implicit deny all rule added at the end of the
list. To overcome this, permit rules must be added to allow the IPv6 control packets.
Note: The control-plane keyword is available only in Global Config
mode.
Note: Depending on the platform, the out option might not be available.
Format ipv6 traffic-filter name {{control-plane |in | out} |vlan vlan-id {in | out}}
[sequence 1-4294967295]
Modes Global Config
Interface Config
(NETGEAR Switch)(Config)#ipv6 traffic-filter ip61 control-plane
no ipv6 traffic-filter
This command removes an IPv6 ACL identified by name from the interface(s) in a given
direction.
Format no ipv6 traffic-filter name {{control-plane | in | out} | vlan vlan-id {in |
out}}
Modes Global Config
Interface Config
Command example:
(NETGEAR Switch) (Config)#no ipv6 traffic-filter ip61 control-plane
show ipv6 access-lists
Use this command to view summary information about all IPv6 ACLs that are configured on
the switch. To view more detailed information about a specific access list, specify the ACL
name that is used to identify the IP ACL. The command output displays the ICMP type, ICMP
code, fragments, routing, and TCP flags attributes, the source and destination L4 port
Quality of Service Commands 992

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ranges, and the number of packets that match a configured ACL rule within an ACL (referred
to as ACL hit count).
Format show ipv6 access-lists [name]
Mode Privileged EXEC
Note: Only the access list fields that you configure are displayed. Thus, the
command output varies based on the match criteria configured within
the rules of an ACL.
Term Definition
Action The action associated with each rule. The possible values are Permit or Deny.
Match All Indicates whether this access list applies to every packet. Possible values are True or False.
Protocol The protocol to filter for this rule.
Committed Rate The committed rate defined by the rate-limit attribute.
Committed Burst The committed burst size defined by the rate-limit attribute.
Size
Source IP Address The source IP address for this rule.
Source L4 Port The source port for this rule.
Keyword
Destination IP The destination IP address for this rule.
Address
Destination L4 Port The destination port for this rule.
Keyword
IP DSCP The value specified for IP DSCP.
Flow Label The value specified for IPv6 Flow Label.
Log Displays when you enable logging for the rule.
Assign Queue The queue identifier to which packets matching this rule are assigned.
Mirror Interface The unit/slot/port to which packets matching this rule are copied.
Redirect Interface The unit/slot/port to which packets matching this rule are forwarded.
Time Range Name Displays the name of the time-range if the IPv6 ACL rule has referenced a time range.
Quality of Service Commands 993

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Rule Status Status (Active/Inactive) of the IPv6 ACL rule.
ACL Hit Count The number of packets that match a configured ACL rule within an ACL (referred to as ACL hit
count). The counter resets to 0 when the maximum value is reached. A dedicated counter exists for
each ACL rule. ACL counters do not interact with PBR counters.
For an ACL with multiple rules, if a match occurs for a specific rule, the counter that is associated
with this rule increments. For example, if an ACL includes three rules, when a match occurs for
r ule2, the counter for rule 3 does not increment.
For ACL counters, if an ACL rule is configured without a rate limit condition, the counter shows the
number of forwarded or discarded packets. (For example, for a burst of 100 packets, the counter
shows 100.)
If the ACL rule is configured with a rate limit condition, the counter shows the number of packets that
match the condition:
• If the packets are sent at a rate that is lower than the configured rate limit, the counter displays
the number of packets that match the condition.
• If the packets are sent at a rate that exceeds the configured rate limit, the counter still displays
the number of packets that match the condition, even though packets are dropped beyond the
configured limit. In this situation, the number of packets that match the condition equals the rate
at which the packets are sent.
For example, if the rate limit condition is 10 kbps but the matching traffic is sent at 100 kbps, the
counter increments with 100 kbps.
Either way, only the number of packets that match the condition is reflected in the counter,
irrespective of whether they are dropped or forwarded.
ACL counters do not interact with diffserv policies.
Command example:
(NETGEAR Switch) #show ipv6 access-lists ip61
ACL Name: ip61
Outbound Interface(s): control-plane
Rule Number: 1
Action......................................... permit
Match Every.................................... FALSE
Protocol....................................... 17(udp)
Committed Rate................................. 32
Committed Burst Size........................... 16
ACL hit count ...............................0
Quality of Service Commands 994

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Time Range Commands for Time-Based
ACLs
Time-based ACLs allow one or more rules within an ACL to be based on time. Each ACL rule
within an ACL except for the implicit deny all rule can be configured to be active and
operational only during a specific time period. The time range commands allow you to define
specific times of the day and week in order to implement time-based ACLs. The time range is
identified by a name and can then be referenced by an ACL rule defined with in an ACL.
time-range
Use this command to create a time range identified by name, consisting of one absolute time
entry and/or one or more periodic time entries. The name parameter is a case-sensitive,
alphanumeric string from 1 to 31 characters that uniquely identifies the time range. An
alpha-numeric string is defined as consisting of only alphabetic, numeric, dash, underscore,
or space characters.
If a time range by this name already exists, this command enters Time-Range config mode to
allow updating the time range entries
Note: When you successfully execute this command, the CLI mode changes
to Time-Range Config mode.
Format time-range name
Mode Global Config
no time-range
This command deletes a time-range identified by name.
Format no time-range name
Mode Global Config
absolute
Use this command to add an absolute time entry to a time range. Only one absolute time
entry is allowed per time-range. The time parameter is based on the currently configured
time zone.
The optional start time date parameters indicate the time and date at which the
configuration that referenced the time range starts going into effect. The time is expressed in
a 24-hour clock, in the form of hours:minutes. For example, 8:00 is 8:00 am and 20:00 is 8:00
Quality of Service Commands 995

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
pm. The date is expressed in the format day month year. If no start time and date are
specified, the configuration statement is in effect immediately.
The optional end time date parameters indicate the time and date at which the
configuration that referenced the time range is no longer in effect. The end time and date
must be after the start time and date. If no end time and date are specified, the configuration
statement is in effect indefinitely.
Format absolute [start time date] [end time date]
Mode Time-Range Config
no absolute
This command deletes the absolute time entry in the time range.
Format no absolute
Mode Time-Range Config
periodic
Use this command to add a periodic time entry to a time range. The time parameter is based
off of the currently configured time zone.
The first occurrence of the days-of-the-week argument is the starting day(s) from which
the configuration that referenced the time range starts going into effect. The second
occurrence is the ending day or days from which the configuration that referenced the time
range is no longer in effect. If the end days-of-the-week are the same as the start, they can
be omitted
This argument can be any single day or combinations of days: Monday, Tuesday,
Wednesday, Thursday, Friday, Saturday, Sunday. Other possible values are:
• daily— Monday through Sunday
• weekdays— Monday through Friday
• weekend— Saturday and Sunday
If the ending days of the week are the same as the starting days of the week, they can be
omitted.
The first occurrence of the time argument is the starting hours:minutes which the
configuration that referenced the time range starts going into effect. The second occurrence
of the time argument is the ending hours:minutes at which the configuration that referenced
the time range is no longer in effect.
Quality of Service Commands 996

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The hours:minutes are expressed in a 24-hour clock. For example, 8:00 is 8:00 am and 20:00
is 8:00 pm.
Format periodic days-of-the-week time to time
Mode Time-Range Config
no periodic
This command deletes a periodic time entry from a time range.
Format no periodic days-of-the-week time to time
Mode Time-Range Config
show time-range
Use this command to display a time range and all the absolute/periodic time entries that are
defined for the time range. Use the name parameter to identify a specific time range to
display. When name is not specified, all the time ranges defined in the system are displayed.
Format show time-range [name]
Mode Privileged EXEC
The information in the following table displays when no time range name is specified.
Term Definition
Admin Mode The administrative mode of the time range feature on the switch
Current number of all Time The number of time ranges currently configured in the system.
Ranges
Maximum number of all Time The maximum number of time ranges that can be configured in the system.
Ranges
Time Range Name Name of the time range.
Status Status of the time range (active/inactive)
Periodic Entry count The number of periodic entries configured for the time range.
Absolute Entry Indicates whether an absolute entry has been configured for the time range (Exists).
Quality of Service Commands 997

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Auto-Voice over IP Commands
This section describes the commands you use to configure Auto-Voice over IP (VoIP)
commands. The Auto-VoIP feature explicitly matches VoIP streams in Ethernet switches and
provides them with a better class-of-service than ordinary traffic. When you enable the
Auto-VoIP feature on an interface, the interface scans incoming traffic for the following
call-control protocols:
• Session Initiation Protocol (SIP)
• H.323
• Skinny Client Control Protocol (SCCP)
When a call-control protocol is detected, the switch assigns the traffic in that session to the
highest CoS queue, which is generally used for time-sensitive traffic.
auto-voip
Use this command to configure auto VoIP mode. The supported modes are protocol-based
and oui-based. Protocol-based auto VoIP prioritizes the voice data based on the layer 4 port
used for the voice session. OUI based auto VoIP prioritizes the phone traffic based on the
known OUI of the phone.
When both modes are enabled, if the connected phone OUI is one of the configured OUI,
then the voice data is prioritized using OUI Auto VoIP, otherwise protocol-based Auto VoIP is
used to prioritize the voice data.
Active sessions are cleared if protocol-based auto VoIP is disabled on the port.
Default oui-based
Format auto-voip [protocol-based | oui-based]
Mode Global Config
Interface Config
no auto-voip
Use the no form of the command to set the default mode.
auto-voip oui
Use this command to configure an OUI for Auto VoIP. The traffic from the configured OUI will
get the highest priority over the other traffic. The oui-prefix is a unique OUI that identifies
the device manufacturer or vendor. The OUI is specified in three octet values (each octets
represented as two hexadecimal digits) separated by colons. The string is a description of
the OUI that identifies the manufacturer or vendor associated with the OUI.
Quality of Service Commands 998

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default A list of known OUIs is present.
Format auto-voip oui oui-prefix desc string
Mode Global Config
Command example:
The following example adds an OUI to the table:
(NETGEAR Switch) (Config)#auto-voip oui 00:03:6B desc "Cisco VoIPPhone"
no auto-voip oui
Use the no auto-voip oui command to remove a configured OUI prefix from the table.
Format no auto-voip oui oui-prefix
Mode Global Config
auto-voip oui-based priority
Use this command to configure the global OUI based auto VoIP priority. If the phone OUI
matches one of the configured OUIs, the priority of traffic from the phone is changed to the
OUI priority configured through this command. The priority-value is the 802.1p priority
used for traffic that matches a value in the known OUI list. If the interface detects an OUI
match, the switch assigns the traffic in that session to the traffic class mapped to this priority
value. Traffic classes with a higher value are generally used for time-sensitive traffic.
Default Highest available priority.
Format auto-voip oui-based priority priority-value
Mode Global Config
no auto-voip oui-based priority
Use the no auto-voip oui-based priority command to reset the global OUI based
auto VoIP priority to its default.
Format no auto-voip oui-based priority
Mode Global Config
auto-voip protocol-based
Use this command to configure the global protocol-based auto VoIP remarking priority or
traffic-class. If remark priority is configured, the voice data of the session is remarked with the
priority configured through this command. The remark-priority is the 802.1p priority
used for protocol-based VoIP traffic. If the interface detects a call-control protocol, the device
Quality of Service Commands 999

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
marks traffic in that session with the specified 802.1p priority value to ensure voice traffic
always gets the highest priority throughout the network path.
The tc value is the traffic class used for protocol-based VoIP traffic. If the interface detects a
call-control protocol, the device assigns the traffic in that session to the configured Class of
Service (CoS) queue. Traffic classes with a higher value are generally used for time-sensitive
traffic. The CoS queue associated with the specified traffic class should be configured with
the appropriate bandwidth allocation to allow priority treatment for VoIP traffic.
Note: You must enable tagging on auto VoIP enabled ports to remark the
voice data upon egress.
Default Traffic class 7
Format auto-voip protocol-based {remark remark-priority | traffic-class tc}
Mode Global Config
no auto-voip protocol-based
Use this command to reset the global protocol based auto VoIP remarking priority or
traffic-class to the default.
Format no auto-voip protocol-based {remark remark-priority | traffic-class tc}
Mode Global Config
auto-voip vlan
Use this command to configure the global Auto VoIP VLAN ID. The VLAN behavior is depend
on the configured auto VoIP mode. The auto-VoIP VLAN is the VLAN used to segregate VoIP
traffic from other non-voice traffic. All VoIP traffic that matches a value in the known OUI list
gets assigned to this VoIP VLAN.
Default None
Format auto-voip vlan vlan-id
Mode Global Config
no auto-voip vlan
Use the no form of the command to reset the auto-VoIP VLAN ID to the default value.
Format no auto-voip vlan
Mode Global Config
Quality of Service Commands 1000

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show auto-voip
Use this command to display the auto VoIP settings on one particular interface or on all
interfaces of the switch.
Format show auto-voip {protocol-based | oui-based} interface {unit/slot/port | all}
Mode Privileged EXEC
Field Description
VoIP VLAN ID The global VoIP VLAN ID.
Prioritization Type The type of prioritization used on voice traffic.
Class Value • If the Prioritization Type is configured as traffic-class, then this value is the queue value.
• If the Prioritization Type is configured as remark, then this value is 802.1p priority used to
remark the voice traffic.
Priority The 802.1p priority. This field is valid for OUI auto VoIP.
AutoVoIP Mode The Auto VoIP mode on the interface.
Command example:
(NETGEAR Switch)# show auto-voip protocol-based interface all
VoIP VLAN Id................................... 2
Prioritization Type............................ traffic-class
Class Value.................................... 7
Interface A uto VoIP Operational Status
Mode
--------- -------------- -----------------
0/1 Disabled Down
0/2 Disabled Down
0/3 Disabled Down
0/4 Disabled Down
Command example:
(NETGEAR Switch)# show auto-voip oui-based interface all
VoIP VLAN Id................................... 2
Priority....................................... 7
Interface Auto VoIP Operational Status
Mode
--------- -------------- ------------------
0/1 Disabled Down
0/2 Disabled Down
0/3 Disabled Down
Quality of Service Commands 1001
