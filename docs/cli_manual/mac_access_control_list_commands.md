# mac_access_control_list_commands

Pages: 961-969

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The following information is repeated for each class instance within this policy:
Term Definition
Class Name The name of this class instance.
In Discarded A count of the packets discarded for this class instance for any reason due to DiffServ treatment of
Packets the traffic class.
show service-policy
This command displays a summary of policy-oriented statistics information for all interfaces
in the specified direction.
Format show service-policy {in | out}
Mode Privileged EXEC
The following information is repeated for each interface and direction (only those interfaces
configured with an attached policy are shown):
Term Definition
Interface unit/slot/port
Operational Status The current operational status of this DiffServ service interface.
Policy Name The name of the policy attached to the interface.
MAC Access Control List Commands
This section describes the commands you use to configure MAC Access Control List (ACL)
settings. MAC ACLs ensure that only authorized users have access to specific resources and
block any unwarranted attempts to reach network resources.
The following rules apply to MAC ACLs:
• The maximum number of ACLs you can create is hardware dependent. The limit applies
to all ACLs, regardless of type.
• The system supports only Ethernet II frame types.
• The maximum number of rules per MAC ACL is hardware dependent.
mac access-list extended
This command creates a MAC Access Control List (ACL) identified by name, consisting of
classification fields defined for the Layer 2 header of an Ethernet frame. The name parameter
is a case-sensitive alphanumeric string from 1 to 31 characters uniquely identifying the MAC
access list. The rate-limit attribute configures the committed rate and the committed burst
size.
Quality of Service Commands 961

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If a MAC ACL by this name already exists, this command enters Mac-Access-List config
mode to allow updating the existing MAC ACL.
Note: The CLI mode changes to Mac-Access-List Config mode when you
successfully execute this command.
Format mac access-list extended name
Mode Global Config
no mac access-list extended
This command deletes a MAC ACL identified by name from the system.
Format no mac access-list extended name
Mode Global Config
mac access-list extended rename
This command changes the name of a MAC Access Control List (ACL). The name parameter
is the name of an existing MAC ACL. The newname parameter is a case-sensitive
alphanumeric string from 1 to 31 characters uniquely identifying the MAC access list.
This command fails if a MAC ACL by the name newname already exists.
Format mac access-list extended rename name newname
Mode Global Config
mac access-list resequence
Use this command to renumber the sequence of the entries for a specified MAC access list
with a specified increment value, starting from a specified sequence number. That is, with this
command you can change the sequence numbers of ACL rules in the ACL and, therefore,
change the order in which entries are applied. This command is not saved in the startup
configuration and does not display in the running configuration.
Note: If the generated sequence number exceeds the maximum sequence
number, the ACL rule creation fails and an informational message
displays.
Default 10
Format mac access-list resequence {name | id} starting-sequence-number increment
Mode Global Config
Quality of Service Commands 962

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
name The name of the access control list.
id The ID of the access control list.
starting-sequence- The sequence number from which to start the renumbering. The range is 1–2147483647. The
number default is 10.
increment The value with which the sequence numbers must be incremented. The range is 1–2147483647.
The default is 10.
[sequence-number] {deny | permit} (MAC ACL)
This command creates a new rule for the current MAC access list. Each rule is appended to
the list of configured rules for the list. A rule may either deny or permit traffic according to the
specified classification fields. At a minimum, the source (srcmac) and destination (dstmac)
MAC value must be specified, each of which may be substituted using the keyword any to
indicate a match on any value in that field. The remaining command parameters are all
optional, but the most frequently used parameters appear in the same relative order as
shown in the command format.
Format [sequence-number] {deny | permit} {srcmac | any} {dstmac | any} [ethertypekey
| 0x0600-0xFFFF] [vlan {eq 0-4095}] [cos 0-7] [[log] [time-range
time-range-name] [assign-queue queue-id]] [{mirror | redirect}
unit/slot/port] [rate-limit rate burst-size]
Mode Mac-Access-List Config
Note: An implicit deny all MAC rule always terminates the access list.
The sequence number specifies the sequence number for the ACL rule. Either you define the
sequence number or is it is generated.
If no sequence number exists for a rule, a sequence number that is 10 greater than the last
sequence number in the ACL is used and the rule is placed at the end of the list. If this is the
first ACL rule in the ACL, a sequence number of 10 is assigned. If the calculated sequence
number exceeds the maximum sequence number value, the creation of the ACL rule fails.
You cannot create a rule that duplicates an already existing one and you cannot configure a
rule with a sequence number that is already used for another rule.
For example, if you add new ACL rule to the ACL without specifying a sequence number, the
rule is placed at the bottom of the list. By changing the sequence number, you can move the
ACL rule to a different position in the ACL.
You can specify the Ethertype as either a keyword or a four-digit hexadecimal value from
0x0600-0xFFFF. The currently supported ethertypekey values are: appletalk, arp,
ibmsna, ipv4, ipv6, ipx, mplsmcast, mplsucast, netbios, novell, pppoe, and
rarp. Each of these translates into its equivalent Ethertype value(s).
Quality of Service Commands 963

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 13. Ethertype keyword and 4-digit hexadecimal value
Ethertype Keyword Corresponding Value
appletalk 0x809B
arp 0x0806
ibmsna 0x80D5
ipv4 0x0800
ipv6 0x86DD
ipx 0x8037
mplsmcast 0x8848
mplsucast 0x8847
netbios 0x8191
novell 0x8137, 0x8138
pppoe 0x8863, 0x8864
rarp 0x8035
The vlan and cos parameters refer to the VLAN identifier and 802.1p user priority fields,
respectively, of the VLAN tag. For packets containing a double VLAN tag, this is the first (or
outer) tag.
The time-range parameter allows imposing time limitation on the MAC ACL rule as defined
by the parameter time-range-name. If a time range with the specified name does not exist
and the MAC ACL containing this ACL rule is applied to an interface or bound to a VLAN,
then the ACL rule is applied immediately. If a time range with specified name exists and the
MAC ACL containing this ACL rule is applied to an interface or bound to a VLAN, then the
ACL rule is applied when the time-range with specified name becomes active. The ACL rule
is removed when the time-range with specified name becomes inactive. For information
about configuring time ranges, see Time Range Commands for Time-Based ACLs on
p age995.
The assign-queue parameter allows specification of a particular hardware queue for
handling traffic that matches this rule. The allowed queue-id value is 0-(n-1), in which n is
the number of user configurable queues available for the hardware platform. The
assign-queue parameter is valid only for a permit rule.
The mirror parameter allows the traffic matching this rule to be copied to the specified
unit/slot/port, while the redirect parameter allows the traffic matching this rule to be
forwarded to the specified unit/slot/port. The assign-queue and redirect
parameters are only valid for a permit rule.
Quality of Service Commands 964

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: The special command form {deny | permit} any any is used to
match all Ethernet layer 2 packets, and is the equivalent of the IP
access list “match every” rule.
The permit command’s optional attribute rate-limit allows you to permit only the
allowed rate of traffic as per the configured rate in kbps, and burst-size in kbytes.
Command example:
(NETGEAR Switch) (Config)#mac access-list extended mac1
(NETGEAR Switch) (Config-mac-access-list)#permit 00:00:00:00:aa:bb ff:ff:ff:ff:00:00 any
rate-limit 32 16
(NETGEAR Switch) (Config-mac-access-list)#exit
no sequence-number (MAC ACL)
Use this command to remove the ACL rule with the specified sequence number from the
ACL.
Format no sequence-number
Modes MAC-Access-List Config
mac access-group
This command either attaches a specific MAC Access Control List (ACL) identified by name
to an interface or range of interfaces, or associates it with a VLAN ID, in a given direction.
The name parameter must be the name of an existing MAC ACL.
An optional sequence number may be specified to indicate the order of this mac access list
relative to other mac access lists already assigned to this interface and direction. A lower
number indicates higher precedence order. If a sequence number is already in use for this
interface and direction, the specified mac access list replaces the currently attached mac
access list using that sequence number. If the sequence number is not specified for this
command, a sequence number that is one greater than the highest sequence number
currently in use for this interface and direction is used.
This command specified in Interface Config mode only affects a single interface, whereas the
Global Config mode setting is applied to all interfaces. The vlan keyword and vlan-id
argument are valid only in the Global Config mode. The Interface Config mode command is
only available on platforms that support independent per-port class of service queue
configuration.
An optional control-plane is specified to apply the MAC ACL on CPU port. The control
packets like BPDU are also dropped because of the implicit deny all rule added to the end of
the list. To overcome this, permit rules must be added to allow the control packets.
Quality of Service Commands 965

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: The control-plane keyword is available only in Global Config
mode.
Note: Depending on the platform, the out option might not be available.
Format mac access-group name {{control-plane | in | out} vlan vlan-id {in | out}}
[sequence 1–4294967295]
Modes Global Config
Interface Config
Parameter Description
name The name of the Access Control List.
vlan-id A VLAN ID associated with a specific IP ACL in a given direction.
sequence A optional sequence number that indicates the order of this IP access list relative to the other IP
access lists already assigned to this interface and direction. The range is 1 to 4294967295.
(NETGEAR Switch)(Config)#mac access-group mac1 control-plane
no mac access-group
This command removes a MAC ACL identified by name from the interface in a given
direction.
Format no mac access-group name {{control-plane | in | out} vlan vlan-id {in | out}}
Modes Global Config
Interface Config
Command example:
(NETGEAR Switch)(Config)#no mac access-group mac1 control-plane
remark
This command adds a new comment to an ACL rule.
Use the remark keyword to add comments (remarks) to an ACL rule entry that belongs to an
IPv4, IPv6, MAC, or ARP ACL. You can add up to 10 * (maximum number of ACL rules per
list) remarks per ACL and up to 10 remarks per ACL rule. For all QoS ACLs (IPv4, IPv6, and
MAC ACLs) together, you can up to add 2 * (maximum number of ACL rules).
Quality of Service Commands 966

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
You can only add a remark before you create a rule. Remarks are associated with the ACL
rule that is created immediately after the remarks are created. If you add 10 remarks, each
one is linked to the rule that is created immediately afterwards.
If the ACL rule is removed, the associated remarks are also deleted. Remarks are shown
only in output of the show running-config command and not in the output of the
s how [ip | mac | arp] access-lists command.
The total length of a single remark cannot exceed 100 characters. A remark can contain
characters in the ranges A-Z, a-z, and 0-9, and special characters such as a space, hyphen,
and underscore.
Format remark comment
Modes IPv4-Access-List Config
IPv6-Access-List-Config
MAC-Access-List Config
ARP-Access-List Config
Command example:
(Config)#arp access-list new
(Config-arp-access-list)#remark "test1"
(Config-arp-access-list)#permit ip host 1.1.1.1 mac host 00:01:02:03:04:05
(Config-arp-access-list)#remark "test1"
(Config-arp-access-list)#remark "test2"
(Config-arp-access-list)#remark "test3"
(Config-arp-access-list)#permit ip host 1.1.1.2 mac host 00:03:04:05:06:07
(Config-arp-access-list)#permit ip host 2.1.1.2 mac host 00:03:04:05:06:08
(Config-arp-access-list)#remark "test4"
(Config-arp-access-list)#remark "test5"
(Config-arp-access-list)#permit ip host 2.1.1.3 mac host 00:03:04:05:06:0
no remark
Use this command to remove a remark from an ACL.
When you enter this command, the first occurrence of the remark in the ACL is deleted. Each
time that you repeat the command with the same remark, the remark is deleted from the next
ACL rule with which the remark is associated.
If all occurrences of the remark are deleted and you enter the command, an error message
displays.
Format no remark comment
Modes IPv4-Access-List Config
IPv6-Access-List-Config
MAC-Access-List Config
ARP-Access-List Config
Quality of Service Commands 967

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show mac access-lists
This command displays summary information for all MAC access lists and shows the number
of packets that match a configured ACL rule within an ACL (referred to as ACL hit count).
To view more detailed information about a specific access list, specify the ACL name that is
used to identify the MAC ACL.
Note: The command output varies based on the match criteria configured
within the rules of an ACL.
Format show mac access-lists [name]
Mode Privileged EXEC
Term Definition
Rule Number The ordered rule number identifier defined within the MAC ACL.
Action The action associated with each rule. The possible values are Permit or Deny.
Source MAC The source MAC address for this rule.
Address
Source MAC Mask The source MAC mask for this rule.
Committed Rate The committed rate defined by the rate-limit attribute.
Committed Burst The committed burst size defined by the rate-limit attribute.
Size
Destination MAC The destination MAC address for this rule.
Address
Ethertype The Ethertype keyword or custom value for this rule.
VLAN ID The VLAN identifier value or range for this rule.
COS The COS (802.1p) value for this rule.
Log Displays when you enable logging for the rule.
Assign Queue The queue identifier to which packets matching this rule are assigned.
Mirror Interface The unit/slot/port to which packets matching this rule are copied.
Redirect Interface The unit/slot/port to which packets matching this rule are forwarded.
Time Range Name Displays the name of the time-range if the MAC ACL rule has referenced a time range.
Quality of Service Commands 968

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Rule Status Status (Active/Inactive) of the MAC ACL rule.
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
(NETGEAR Switch) #show mac access-lists mac1
ACL Name: mac1
Outbound Interface(s): control-plane
Sequence Number: 10
Action........................................permit
Source MAC Address................ 00:00:00:00:AA:BB
Source MAC Mask....................FF:FF:FF:FF:00:00
Committed Rate.......................32
Committed Burst Size...............16
ACL hit count ............................0
Sequence Number: 25
Action..........................................permit
Source MAC Address...................00:00:00:00:AA:BB
Source MAC Mask.......................FF:FF:FF:FF:00:00
Destination MAC Address...........01:80:C2:00:00:00
Destination MAC Mask................00:00:00:FF:FF:FF
Ethertype.....................................ipv6
VLAN............................................36
CoS Value.....................................7
Assign Queue...............................4
Quality of Service Commands 969
