# m_ac_address_ip_address_type_vlan_interface_-_----------------_---------------_-----------_afa78cec

Pages: 927-957

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
VLAN VLAN for the entry.
Interface IP address of the interface in unit/slot/port format.
Command example:
(NETGEAR Switch) #show ipv6 source binding
M AC Address IP Address Type Vlan Interface
- ---------------- --------------- ------------- ----- -------------
0 0:00:00:00:00:08 2000::1 dhcp-snooping 2 1/0/1
0 0:00:00:00:00:09 3 000::1 dhcp-snooping 3 1/0/1
0 0:00:00:00:00:0A 4000::1 dhcp-snooping 4 1/0/1
IPv6 Commands 927

Quality of Service Commands

This chapter describes the Quality of Service (QoS) commands.
The chapter contains the following sections:
• Class of Service Commands
• Differentiated Services Commands
• DiffServ Class Commands
• DiffServ Policy Commands
• DiffServ Service Commands
• DiffServ Show Commands
• MAC Access Control List Commands
• IP Access Control List Commands
• IPv6 Access Control List Commands
• Time Range Commands for Time-Based ACLs
• Auto-Voice over IP Commands
• iSCSI Optimization Commands
The commands in this chapter are in one of two functional groups:
• Show commands. Display switch settings, statistics, and other information.
• Configuration commands. Configure features and options of the switch. For every
configuration command, there is a show command that displays the configuration setting.

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Class of Service Commands
This section describes the commands you use to configure and view Class of Service (CoS)
settings for the switch. The commands in this section allow you to control the priority and
transmission rate of traffic.
Note: Commands you issue in the Interface Config mode only affect a single
interface. Commands you issue in the Global Config mode affect all
interfaces.
classofservice dot1p-mapping
This command maps an 802.1p priority to an internal traffic class. The userpriority
values can range from 0-7. The trafficclass values range from 0-6, although the actual
number of available traffic classes depends on the platform.
Format classofservice dot1p-mapping userpriority trafficclass
Modes Global Config
Interface Config
no classofservice dot1p-mapping
This command maps each 802.1p priority to its default internal traffic class value.
Format no classofservice dot1p-mapping
Modes Global Config
Interface Config
classofservice ip-dscp-mapping
This command maps an IP DSCP value to an internal traffic class. The ipdscp value is
specified as either an integer from 0 to 63, or symbolically through one of the following
keywords: af11, af12, af13, af21, af22, af23, af31, af32, af33, af41, af42, af43, be, cs0, cs1,
cs2, cs3, cs4, cs5, cs6, cs7, ef.
The trafficclass values can range from 0-6, although the actual number of available
traffic classes depends on the platform.
Format classofservice ip-dscp-mapping ipdscp trafficclass
Mode Global Config
Quality of Service Commands 929

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no classofservice ip-dscp-mapping
This command maps each IP DSCP value to its default internal traffic class value.
Format no classofservice ip-dscp-mapping
Mode Global Config
dante
This command sets the IGMP snooping querier interval to 30 seconds and configures the
following class of service parameters:
• set igmp querier query-interval 30
• classofservice ip-dscp-mapping 46 5
• classofservice ip-dscp-mapping 48 5
• classofservice ip-dscp-mapping 56 6
Default Disabled
Format dante
Modes Global Config
no dante
This command sets the following commands to the default values:
• set igmp querier query-interval
• classofservice ip-dscp-mapping
Format no dante
Modes Global Config
dante vlan
This command configures the following class of service parameters for all member ports of a
particular VLAN:
• classofservice trust ip-dscp
• cos-queue strict 5 6
The vlan argument can be a VLAN from 1 to 4093.
This command applies the class of service parameters to all member ports of the specified
VLAN. However, if a port is a member of multiple VLANs and one of those VLANs is
configured for Dante but other VLANs are not, the Dante configuration takes precedence and
is applied to the port.
Quality of Service Commands 930

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default Disabled
Format dante vlan
Modes Global Config
no dante vlan
This command sets the following commands for all member ports of a particular VLAN to the
default values:
• classofservice trust
• cos-queue strict
The vlan argument can be a VLAN from 1 to 4093.
Format no dante vlan
Modes Global Config
classofservice trust
This command sets the class of service trust mode of an interface or range of interfaces. You
can set the mode to trust one of the Dot1p (802.1p), IP DSCP, or IP Precedence packet
markings. You can also set the interface mode to untrusted. If you configure an interface to
use Dot1p, the mode does not appear in the output of the show running-config command
because Dot1p is the default.
Default dot1p
Format classofservice trust {dot1p | ip-dscp | untrusted}
Modes Global Config
Interface Config
no classofservice trust
This command sets the interface mode to the default value.
Format no classofservice trust
Modes Global Config
Interface Config
cos-queue min-bandwidth
This command specifies the minimum transmission bandwidth (bw) guarantee for each
interface queue on an interface, a range of interfaces, or all interfaces. The total number of
queues supported per interface is platform specific. A value from 0-100 (percentage of link
rate) must be specified for each supported queue, with 0 indicating no guaranteed minimum
bandwidth. The sum of all values entered must not exceed 100.
Quality of Service Commands 931

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format cos-queue min-bandwidth bw-0 bw-1 … bw-n
Modes Global Config
Interface Config
no cos-queue min-bandwidth
This command restores the default for each queue's minimum bandwidth value.
Format no cos-queue min-bandwidth
Modes Global Config
Interface Config
cos-queue random-detect
This command activates weighted random early discard (WRED) for each specified queue on
the interface. Specific WRED parameters are configured using the random-detect
queue-parms and the random-detect exponential-weighting-constant
commands.
Format cos-queue random-detect queue-id-1 [queue-id-2 … queue-id-n]
Modes Global Config
Interface Config
When specified in Interface Config mode, this command affects a single interface only,
whereas in Global Config mode, it applies to all interfaces.
At least one, but no more than n queue-id values are specified with this command.
Duplicate queue-id values are ignored. Each queue-id value ranges from 0 to (n–1), in
which n is the total number of queues supported per interface. In the queue-id-n argument,
the number n = 7 and corresponds to the number of supported queues (traffic classes).
no cos-queue random-detect
Use this command to disable WRED, thereby restoring the default tail drop operation for the
specified queues on the interface.
Format no cos-queue random-detect queue-id-1 [queue-id-2 … queue-id-n]
Modes Global Config
Interface Config
Quality of Service Commands 932

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
cos-queue strict
This command activates the strict priority scheduler mode for each specified queue for an
interface queue on an interface, a range of interfaces, or all interfaces.
Format cos-queue strict queue-id-1 [queue-id-2 … queue-id-n]
Modes Global Config
Interface Config
no cos-queue strict
This command restores the default weighted scheduler mode for each specified queue.
Format no cos-queue strict queue-id-1 [queue-id-2 … queue-id-n]
Modes Global Config
Interface Config
random-detect
This command is used to enable WRED for the interface as a whole, and is available only
when per-queue WRED activation control is not supported by the device. Specific WRED
parameters are configured using the random-detect queue-parms and the
random-detect exponential-weighting-constant commands.
Format random-detect
Modes Global Config
Interface Config
When specified in Interface Config mode, this command affects a single interface only,
whereas in Global Config mode, it applies to all interfaces. The Interface Config mode
command is available only on platforms that support independent per-port class of service
queue configuration.
no random-detect
Use this command to disable WRED, thereby restoring the default tail drop operation for all
queues on the interface.
Format no random-detect
Modes Global Config
Interface Config
Quality of Service Commands 933

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
random-detect exponential weighting-constant
This command is used to configure the WRED decay exponent for a CoS queue interface.
The number argument is a value in the range of 0–15.
Format random-detect exponential-weighting-constant number
Modes Global Config
Interface Config
no random-detect exponential-weighting-constant
Use this command to set the WRED decay exponent back to the default.
Format no random-detect exponential-weighting-constant
Modes Global Config
Interface Config
random-detect queue-parms
This command is used to configure WRED parameters for each drop precedence level
supported by a queue. It is used only when per-COS queue configuration is enabled (using
the cos-queue random-detect command).
Format random-detect queue-parms queue-id-1 [queue-id-2 … queue-id-n] min-thresh
thresh-prec-1 … thresh-prec-n max-thresh thresh-prec-1 … thresh-prec-n
drop-probability prob-prec-1 … prob-prec-n
Modes Global Config
Interface Config
Each parameter is specified for each possible drop precedence (color of TCP traffic). The last
precedence applies to all non-TCP traffic. For example, in a three-color system, three colors
and one non-TCP precedence are specified for each parameter: green TCP, yellow TCP, red
TCP, and non-TCP, respectively.
Term Definition
min-thresh The minimum threshold the queue depth (as a percentage) where WRED starts marking and
dropping traffic.
max-thresh The maximum threshold is the queue depth (as a percentage) above which WRED marks/drops all
traffic.
drop-probability The percentage probability that WRED will mark/drop a packet, when the queue depth is at the
maximum threshold. (The drop probability increases linearly from 0 just before the minimum
threshold, to this value at the maximum threshold, then goes to 100% for larger queue depths).
Quality of Service Commands 934

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no random-detect queue-parms
Use this command to set the WRED configuration back to the default.
Format no random-detect queue-parms queue-id-1 [queue-id-2 … queue-id-n]
Modes Global Config
Interface Config
traffic-shape
This command specifies the maximum transmission bandwidth (bw) limit for the interface as
a whole. The bandwidth values are from 0-100 in increments of 1. You can also specify this
value for a range of interfaces or all interfaces. Also known as rate shaping, traffic shaping
has the effect of smoothing temporary traffic bursts over time so that the transmitted traffic
rate is bounded.
Format traffic-shape bw
Modes Global Config
Interface Config
no traffic-shape
This command restores the interface shaping rate to the default value.
Format no traffic-shape
Modes Global Config
Interface Config
show classofservice dot1p-mapping
This command displays the current Dot1p (802.1p) priority mapping to internal traffic classes
for a specific interface. The unit/slot/port parameter is optional and is only valid on
platforms that support independent per-port class of service mappings. If specified, the
802.1p mapping table of the interface is displayed. If omitted, the most recent global
configuration settings are displayed. For more information, see Voice VLAN Commands on
p age445.
Format show classofservice dot1p-mapping [unit/slot/port]
Mode Privileged EXEC
The following information is repeated for each user priority.
Term Definition
User Priority The 802.1p user priority value.
Traffic Class The traffic class internal queue identifier to which the user priority value is mapped.
Quality of Service Commands 935

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show classofservice ip-dscp-mapping
This command displays the current IP DSCP mapping to internal traffic classes for the global
configuration settings.
Format show classofservice ip-dscp-mapping
Mode Privileged EXEC
The following information is repeated for each user priority.
Term Definition
IP DSCP The IP DSCP value.
Traffic Class The traffic class internal queue identifier to which the IP DSCP value is mapped.
show classofservice trust
This command displays the current trust mode setting for a specific interface. The
unit/slot/port parameter is optional and is only valid on platforms that support
independent per-port class of service mappings. If you specify an interface, the command
displays the port trust mode of the interface. If you do not specify an interface, the command
displays the most recent global configuration settings.
Format show classofservice trust [unit/slot/port]
Mode Privileged EXEC
Term Definition
Class of Service Trust Mode The the trust mode, which is either Dot1P, IP DSCP, or Untrusted.
Non-IP Traffic Class (IP DSCP mode only) The traffic class used for non-IP traffic.
Untrusted Traffic Class (Untrusted mode only) The traffic class used for all untrusted traffic.
show interfaces cos-queue
This command displays the class-of-service queue configuration for the specified interface.
The unit/slot/port parameter is optional and is only valid on platforms that support
independent per-port class of service mappings. If specified, the class-of-service queue
configuration of the interface is displayed. If omitted, the most recent global configuration
settings are displayed.
Format show interfaces cos-queue [unit/slot/port]
Mode Privileged EXEC
Quality of Service Commands 936

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Interface Shaping Rate The global interface shaping rate value.
WRED Decay Exponent The global WRED decay exponent value.
Queue Id An interface supports n queues numbered 0 to (n-1). The specific n value is platform
dependent.
Minimum Bandwidth The minimum transmission bandwidth guarantee for the queue, expressed as a
percentage. A value of 0 means bandwidth is not guaranteed and the queue operates
using best-effort. This is a configured value.
Maximum Bandwidth The maximum transmission bandwidth guarantee for the queue, expressed as a
percentage. A value of 0 means bandwidth is not guaranteed and the queue operates
using best-effort. This is a configured value.
Scheduler Type Indicates whether this queue is scheduled for transmission using a strict priority or a
weighted scheme. This is a configured value.
Queue Management Type The queue depth management technique used for this queue (tail drop).
If you specify the interface, the command also displays the following information.
Term Definition
Interface The unit/slot/port of the interface. If displaying the global configuration, this output line
is replaced with a Global Config indication.
Interface Shaping Rate The maximum transmission bandwidth limit for the interface as a whole. It is independent of
any per-queue maximum bandwidth value(s) in effect for the interface. This is a configured
value.
WRED Decay Exponent The configured WRED decay exponent for a CoS queue interface.
Differentiated Services Commands
This section describes the commands you use to configure QOS Differentiated Services
(DiffServ).
You configure DiffServ in several stages by specifying three DiffServ components:
1. Class
a. Creating and deleting classes.
b. Defining match criteria for a class.
2. Policy
a. Creating and deleting policies
b. Associating classes with a policy
c. Defining policy statements for a policy/class combination
Quality of Service Commands 937

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
3. Service
a. Adding and removing a policy to/from an inbound interface
The DiffServ class defines the packet filtering criteria. The attributes of a DiffServ policy
define the way the switch processes packets. You can define policy attributes on a per-class
instance basis. The switch applies these attributes when a match occurs.
Packet processing begins when the switch tests the match criteria for a packet. The switch
applies a policy to a packet when it finds a class match within that policy.
The following rules apply when you create a DiffServ class:
• Each class can contain a maximum of one referenced (nested) class
• Class definitions do not support hierarchical service policies
A given class definition can contain a maximum of one reference to another class. You can
combine the reference with other match criteria. The referenced class is truly a reference and
not a copy since additions to a referenced class affect all classes that reference it. Changes
to any class definition currently referenced by any other class must result in valid class
definitions for all derived classes, otherwise the switch rejects the change. You can remove a
class reference from a class definition.
The only way to remove an individual match criterion from an existing class definition is to
delete the class and re-create it.
Note: The mark possibilities for policing include CoS, IP DSCP, and IP
Precedence. While the latter two are only meaningful for IP packet
types, CoS marking is allowed for both IP and non-IP packets, since it
updates the 802.1p user priority field contained in the VLAN tag of the
layer 2 packet header.
diffserv
This command sets the DiffServ operational mode to active. While disabled, the DiffServ
configuration is retained and can be changed, but it is not activated. When enabled, DiffServ
services are activated.
Format diffserv
Mode Global Config
Quality of Service Commands 938

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no diffserv
This command sets the DiffServ operational mode to inactive. While disabled, the DiffServ
configuration is retained and can be changed, but it is not activated. When enabled, DiffServ
services are activated.
Format no diffserv
Mode Global Config
DiffServ Class Commands
Use the DiffServ class commands to define traffic classification. To classify traffic, you
specify Behavior Aggregate (BA), based on DSCP and Multi-Field (MF) classes of traffic
(name, match criteria)
This set of commands consists of class creation/deletion and matching, with the class match
commands specifying Layer 3, Layer 2, and general match criteria. The class match criteria
are also known as class rules, with a class definition consisting of one or more rules to
identify the traffic that belongs to the class.
Note: After you create a class match criterion for a class, you cannot change
or delete the criterion. To change or delete a class match criterion,
you must delete and re-create the entire class.
The CLI command root is class-map.
class-map
This command defines a DiffServ class of type match-all. When used without any match
condition, this command enters the class-map mode. The class-map-name is a case
sensitive alphanumeric string from 1 to 31 characters uniquely identifying an existing DiffServ
class.
Note: The class-map-name default is reserved. Do not use it.
The class type of match-all indicates all of the individual match conditions must be true for
a packet to be considered a member of the class.This command may be used without
specifying a class type to enter the Class-Map Config mode for an existing DiffServ class.
Quality of Service Commands 939

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: The optional keywords ipv4 and ipv6 specify the Layer 3 protocol
for this class. If not specified, this parameter defaults to ipv4. This
maintains backward compatibility for configurations defined on
systems before IPv6 match items were supported.
Note: The CLI mode is changed to Class-Map Config or IPv6-Class-Map
Config when this command is successfully executed depending on
whether you specify the ipv4 or ipv6 keyword.
Format class-map match-all class-map-name [ipv4 | ipv6]
Mode Global Config
no class-map
This command eliminates an existing DiffServ class. The class-map-name is the name of
an existing DiffServ class. (The class name default is reserved and is not allowed here.)
This command may be issued at any time; if the class is currently referenced by one or more
policies or by any other class, the delete action fails.
Format no class-map class-map-name
Mode Global Config
class-map rename
This command changes the name of a DiffServ class. The class-map-name parameter is
the name of an existing DiffServ class. The new-class-map-name parameter is a
case-sensitive alphanumeric string from 1 to 31 characters uniquely identifying the class.
Default none
Format class-map rename class-map-name new-class-map-name
Mode Global Config
match ethertype
This command adds to the specified class definition a match condition based on the value of
the ethertype. The ethertype value is specified as a keyword argument that can be one of
the following types: appletalk, arp, ibmsna, ipv4, ipv6, ipx, mplsmcast, mplsucast,
netbios, novell, pppoe, or rarp or as a range argument that represents an EtherType
value in the range of 0x0600-0xFFFF. Use the not option to negate the match condition.
Quality of Service Commands 940

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format match [not] ethertype {keyword | custom range}
Mode Class-Map Config
Ipv6-Class-Map Config
match any
This command adds to the specified class definition a match condition whereby all packets
are considered to belong to the class. Use the not option to negate the match condition.
Default none
Format match [not] any
Mode Class-Map Config
Ipv6-Class-Map Config
match class-map
This command adds to the specified class definition the set of match conditions defined for
another class. The refclassname is the name of an existing DiffServ class whose match
conditions are being referenced by the specified class definition.
Default none
Format match class-map refclassname
Mode Class-Map Config
Ipv6-Class-Map Config
The requirements for the match class-map command are as follows:
• The parameters refclassname and class-map-name can not be the same.
• Only one other class may be referenced by a class.
• Any attempts to delete the refclassname class while the class is still referenced by any
class-map-name fails.
• The combined match criteria of class-map-name and refclassname must be an
allowed combination based on the class type.
• Any subsequent changes to the refclassname class match criteria must maintain this
validity, or the change attempt fails.
• The total number of class rules formed by the complete reference class chain (including
both predecessor and successor classes) must not exceed a platform-specific maximum.
In some cases, each removal of a refclass rule reduces the maximum number of
available rules in the class definition by one.
Quality of Service Commands 941

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no match class-map
This command removes from the specified class definition the set of match conditions
defined for another class. The refclassname is the name of an existing DiffServ class
whose match conditions are being referenced by the specified class definition.
Format no match class-map refclassname
Mode Class-Map Config
Ipv6-Class-Map Config
match cos
This command adds to the specified class definition a match condition for the Class of
Service value (the only tag in a single tagged packet or the first or outer 802.1Q tag of a
double VLAN tagged packet). The value argument can be from 0 to 7. Use the not option to
negate the match condition.
Default none
Format match [not] cos value
Mode Class-Map Config
Ipv6-Class-Map Config
match secondary-cos
This command adds to the specified class definition a match condition for the secondary
Class of Service value (the inner 802.1Q tag of a double VLAN tagged packet). The value
argument can be from 0 to 7. Use the not option to negate the match condition.
Default none
Format match [not] secondary-cos value
Mode Class-Map Config
Ipv6-Class-Map Config
match destination-address mac
This command adds to the specified class definition a match condition based on the
destination MAC address of a packet. The macaddr parameter is any layer 2 MAC address
formatted as six, two-digit hexadecimal numbers separated by colons (e.g.,
00:11:22:dd:ee:ff). The macmask parameter is a layer 2 MAC address bit mask, which need
not be contiguous, and is formatted as six, two-digit hexadecimal numbers separated by
colons (e.g., ff:07:23:ff:fe:dc). Use the not option to negate the match condition.
Quality of Service Commands 942

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default none
Format match [not] destination-address mac macaddr macmask
Mode Class-Map Config
Ipv6-Class-Map Config
match dstip
This command adds to the specified class definition a match condition based on the
destination IP address of a packet. The ipaddr parameter specifies an IP address. The
ipmask parameter specifies an IP address bit mask and must consist of a contiguous set of
leading 1 bits. Use the not option to negate the match condition.
Default none
Format match [not] dstip ipaddr ipmask
Mode Class-Map Config
match dstip6
This command adds to the specified class definition a match condition based on the
destination IPv6 address of a packet. Use the not option to negate the match condition.
Default none
Format match [not] dstip6 destination-ipv6-prefix/prefix-length
Mode Ipv6-Class-Map Config
match dstl4port
This command adds to the specified class definition a match condition based on the
destination layer 4 port of a packet using a single keyword or numeric notation. To specify the
match condition as a single keyword, the value for portkey is one of the supported port
name keywords. The portkey argument can be: domain, echo, ftp, ftpdata, http,
smtp, snmp, telnet, tftp, or www. Each of these translates into its equivalent port number.
To specify the match condition using a numeric notation, one layer 4 port number is required.
The port-number argument is an integer from 0 to 65535. Use the not option to negate the
match condition.
Default none
Format match [not] dstl4port {portkey | port-number}
Mode Class-Map Config
Ipv6-Class-Map Config
Quality of Service Commands 943

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
match ip dscp
This command adds to the specified class definition a match condition based on the value of
the IP DiffServ Code Point (DSCP) field in a packet, which is defined as the high-order six
bits of the Service Type octet in the IP header (the low-order two bits are not checked).
The dscpval value is specified as either an integer from 0 to 63, or symbolically through one
of the following keywords: af11, af12, af13, af21, af22, af23, af31, af32, af33, af41,
af42, af43, be, cs0, cs1, cs2, cs3, cs4, cs5, cs6, cs7, or ef. Use the not option to
negate the match condition.
Note: The IP DSCP, IP Precedence, and IP ToS match conditions are
alternative ways to specify a match criterion for the same Service
Type field in the IP header, but with a slightly different user notation.
Default none
Format match [not] ip dscp dscpval
Mode Class-Map Config
Ipv6-Class-Map Config
match ip precedence
This command adds to the specified class definition a match condition based on the value of
the IP Precedence field in a packet, which is defined as the high-order three bits of the
Service Type octet in the IP header (the low-order five bits are not checked). The precedence
value argument is an integer from 0 to 7. Use the not option to negate the match condition.
Note: The IP DSCP, IP Precedence, and IP ToS match conditions are
alternative ways to specify a match criterion for the same Service
Type field in the IP header, but with a slightly different user notation.
Default none
Format match [not] ip precedence value
Mode Class-Map Config
match ip tos
This command adds to the specified class definition a match condition based on the value of
the IP TOS field in a packet, which is defined as all eight bits of the Service Type octet in the
IP header. The value of the tosbits argument is a two-digit hexadecimal number from 00 to
ff. The value of tosmask argument is a two-digit hexadecimal number from 00 to ff. The
tosmask denotes the bit positions in tosbits that are used for comparison against the IP
Quality of Service Commands 944

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ToS field in a packet. For example, to check for an IP TOS value having bits 7 and 5 set and
bit 1 clear, where bit 7 is most significant, use a tosbits value of a0 (hex) and a tosmask of
a2 (hex). Use the not option to negate the match condition.
Note: The IP DSCP, IP Precedence, and IP ToS match conditions are
alternative ways to specify a match criterion for the same Service
Type field in the IP header, but with a slightly different user notation.
Note: This free form version of the IP DSCP/Precedence/ToS match
specification gives the user complete control when specifying which
bits of the IP Service Type field are checked.
Default none
Format match [not] ip tos tosbits tosmask
Mode Class-Map Config
match ip6flowlbl
Use this command to enter an IPv6 flow label value. Use the not option to negate the match
condition. The value argument can be in the range of 0–1048575.
Default none
Format match [not] ip6flowlbl label value
Mode IPv6-Class-Map Config
match protocol
This command adds to the specified class definition a match condition based on the value of
the IP Protocol field in a packet using a single keyword notation or a numeric value notation.
To specify the match condition using a single keyword notation, the value for
protocol-name is one of the supported protocol name keywords. The currently supported
values are: icmp, igmp, ip, tcp, udp. A value of ip matches all protocol number values.
To specify the match condition using a numeric value notation, the protocol number
argument is a standard value assigned by IANA and is interpreted as an integer from 0 to
255. Use the [not] option to negate the match condition.
Note: This command does not validate the protocol number value against
the current list defined by IANA.
Quality of Service Commands 945

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default none
Format match [not] protocol {protocol-name | number}
Mode Class-Map Config
Ipv6-Class-Map Config
match source-address mac
This command adds to the specified class definition a match condition based on the source
MAC address of a packet. The address parameter is any layer 2 MAC address formatted as
six, two-digit hexadecimal numbers separated by colons (e.g., 00:11:22:dd:ee:ff). The
macmask parameter is a layer 2 MAC address bit mask, which may not be contiguous, and
is formatted as six, two-digit hexadecimal numbers separated by colons (that is,
ff:07:23:ff:fe:dc). Use the not option to negate the match condition.
Default none
Format match [not] source-address mac address macmask
Mode Class-Map Config
Ipv6-Class-Map Config
match srcip
This command adds to the specified class definition a match condition based on the source
IP address of a packet. The ipaddr parameter specifies an IP address. The ipmask
parameter specifies an IP address bit mask and must consist of a contiguous set of leading 1
bits. Use the not option to negate the match condition.
Default none
Format match [not] srcip ipaddr ipmask
Mode Class-Map Config
match srcip6
This command adds to the specified class definition a match condition based on the source
IP address of a packet. Use the not option to negate the match condition.
Default none
Format match [not] srcip6 source-ipv6-prefix/prefix-length
Mode Ipv6-Class-Map Config
Quality of Service Commands 946

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
match srcl4port
This command adds to the specified class definition a match condition based on the source
layer 4 port of a packet using a single keyword or numeric notation. To specify the match
condition as a single keyword notation, the value for portkey is one of the supported port
name keywords (listed below). The currently supported portkey values are: domain, echo,
ftp, ftpdata, http, smtp, snmp, telnet, tftp, and www. Each of these translates into its
equivalent port number, which is used as both the start and end of a port range.
To specify the match condition as a numeric value, one layer 4 port number is required. The
port-number argument is an integer from 0 to 65535. Use the not option to negate the
match condition.
Default none
Format match [not] srcl4port {portkey | port-number}
Mode Class-Map Config
Ipv6-Class-Map Config
match vlan
This command adds to the specified class definition a match condition based on the value of
the layer 2 VLAN Identifier field (the only tag in a single tagged packet or the first or outer tag
of a double VLAN tagged packet). The vlan-id argument is an integer from 0 to 4093. Use
the not option to negate the match condition.
Default none
Format match [not] vlan vland-id
Mode Class-Map Config
Ipv6-Class-Map Config
match secondary-vlan
This command adds to the specified class definition a match condition based on the value of
the layer 2 secondary VLAN Identifier field (the inner 802.1Q tag of a double VLAN tagged
packet). The secondary vlan-id argument is an integer from 0 to 4093. Use the not option
to negate the match condition.
Default none
Format match [not] secondary-vlan vlan-id
Mode Class-Map Config
Ipv6-Class-Map Config
Quality of Service Commands 947

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
DiffServ Policy Commands
Use the DiffServ policy commands to specify traffic conditioning actions, such as policing and
marking, to apply to traffic classes
Use the policy commands to associate a traffic class that you define by using the class
command set with one or more QoS policy attributes. Assign the class/policy association to
an interface to form a service. Specify the policy name when you create the policy.
Each traffic class defines a particular treatment for packets that match the class definition.
You can associate multiple traffic classes with a single policy. When a packet satisfies the
conditions of more than one class, preference is based on the order in which you add the
classes to the policy. The first class you add has the highest precedence.
This set of commands consists of policy creation/deletion, class addition/removal, and
individual policy attributes.
Note: The only way to remove an individual policy attribute from a class
instance within a policy is to remove the class instance and re-add it
to the policy. The values associated with an existing policy attribute
can be changed without removing the class instance.
The CLI command root is policy-map.
assign-queue
This command modifies the queue id to which the associated traffic stream is assigned. The
queueid is an integer from 0 to n-1, in which n is the number of egress queues supported by
the device.
Format assign-queue queueid
Mode Policy-Class-Map Config
Incompatibilities Drop
drop
This command specifies that all packets for the associated traffic stream are to be dropped at
ingress.
Format drop
Mode Policy-Class-Map Config
Incompatibilities Assign Queue, Mark (all forms), Mirror, Police, Redirect
Quality of Service Commands 948

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
mirror
This command specifies that all incoming packets for the associated traffic stream are copied
to a specific egress interface (physical port or LAG).
Format mirror unit/slot/port
Mode Policy-Class-Map Config
Incompatibilities Drop, Redirect
redirect
This command specifies that all incoming packets for the associated traffic stream are
redirected to a specific egress interface (physical port or port-channel).
Format redirect unit/slot/port
Mode Policy-Class-Map Config
Incompatibilities Drop, Mirror
conform-color
Use this command to enable color-aware traffic policing and define the conform-color class
map. Used in conjunction with the police command where the fields for the conform level are
specified. The class-map-name argument is the name of an existing DiffServ class map.
Note: This command may only be used after specifying a police command
for the policy-class instance.
Format conform-color class-map-name
Mode Policy-Class-Map Config
class
This command creates an instance of a class definition within the specified policy for the
purpose of defining treatment of the traffic class through subsequent policy attribute
statements. The classname argument is the name of an existing DiffServ class.
Note: This command causes the specified policy to create a reference to the
class definition.
Quality of Service Commands 949

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: The CLI mode is changed to Policy-Class-Map Config when this
command is successfully executed.
Format class classname
Mode Policy-Map Config
no class
This command deletes the instance of a particular class and its defined treatment from the
specified policy. The classname argument is the name of an existing DiffServ class.
Note: This command removes the reference to the class definition for the
specified policy.
Format no class classname
Mode Policy-Map Config
mark cos
This command marks all packets for the associated traffic stream with the specified class of
service (CoS) value in the priority field of the 802.1p header (the only tag in a single tagged
packet or the first or outer 802.1Q tag of a double VLAN tagged packet). If the packet does
not already contain this header, one is inserted. The CoS value argument is an integer from
0 to 7.
Default 1
Format mark-cos value
Mode Policy-Class-Map Config
Incompatibilities Drop, Mark IP DSCP, IP Precedence, Police
mark cos-as-sec-cos
This command marks outer VLAN tag priority bits of all packets as the inner VLAN tag
priority, marking Cos as Secondary CoS. This essentially means that the inner VLAN tag CoS
is copied to the outer VLAN tag CoS.
Format mark cos-as-sec-cos
Mode Policy-Class-Map Config
Incompatibilities Drop, Mark IP DSCP, IP Precedence, Police
Quality of Service Commands 950

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) (Config-policy-classmap)#mark cos-as-sec-cos
mark ip-dscp
This command marks all packets for the associated traffic stream with the specified IP DSCP
value. The dscpval value is specified as either an integer from 0 to 63, or symbolically
through one of the following keywords: af11, af12, af13, af21, af22, af23, af31, af32,
af33, af41, af42, af43, be, cs0, cs1, cs2, cs3, cs4, cs5, cs6, cs7, or ef.
Format mark ip-dscp dscpval
Mode Policy-Class-Map Config
Incompatibilities Drop, Mark CoS, Mark IP Precedence, Police
mark ip-precedence
This command marks all packets for the associated traffic stream with the specified IP
Precedence value. The IP Precedence value argument is an integer from 0 to 7.
Note: This command may not be used on IPv6 classes. IPv6 does not have
a precedence field.
Format mark ip-precedence value
Mode Policy-Class-Map Config
Incompatibilities Drop, Mark CoS, Mark IP Precedence, Police
Policy Type In
police-simple
This command is used to establish the traffic policing style for the specified class. The simple
form of the police command uses a single data rate and burst size, resulting in two
outcomes: conform and violate. The conforming data rate is specified in kilobits-per-second
(Kbps) and is an integer from 1 to 4294967295. The conforming burst size is specified in
kilobytes (KB) and is an integer from 1 to 128.
For each outcome, the only possible actions are drop, set-cos-as-sec-cos, set-cos-transmit,
set-sec-cos-transmit, set-dscp-transmit, set-prec-transmit, or transmit. In this simple form of
the police command, the conform action defaults to transmit and the violate action defaults
to drop. These actions can be set with this command once the style is configured.
For set-dscp-transmit, a value is required and is specified as either an integer from 0 to
63, or symbolically through one of the following keywords: af11, af12, af13, af21, af22,
Quality of Service Commands 951

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
af23, af31, af32, af33, af41, af42, af43, be, cs0, cs1, cs2, cs3, cs4, cs5, cs6, cs7,
or ef.
For set-prec-transmit, an IP Precedence value is required and is specified as an
integer from 0-7.
For set-cos-transmit an 802.1p priority value is required and is specified as an integer
from 0-7.
Format police-simple {1-4294967295 1-128 conform-action {drop |
set-cos-as-sec-cos | set-cos-transmit 0-7 | set-sec-cos-transmit 0-7 |
set-prec-transmit 0-7 | set-dscp-transmit 0-63 | transmit}
[violate-action {drop | set-cos-as-sec-cos | set-cos-transmit 0-7 |
set-sec-cos-transmit 0-7 | set-prec-transmit 0-7 | set-dscp-transmit 0-63
| transmit}]}
Mode Policy-Class-Map Config
Incompatibilities Drop, Mark (all forms)
Command example:
(NETGEAR Switch) (Config-policy-classmap)#police-simple 1 128 conform-action transmit
violate-action drop
police-single-rate
This command is the single-rate form of the police command and is used to establish the
traffic policing style for the specified class. For each outcome, the only possible actions are
drop, set-cos-as-sec-cost, set-cos-transmit, set-sec-cos-transmit, set-dscp-transmit,
set-prec-transmit, or transmit. In this single-rate form of the police command, the conform
action defaults to send, the exceed action defaults to drop, and the violate action defaults to
drop. These actions can be set with this command once the style has been configured.
Format police-single-rate {1-4294967295 1-128 1-128 conform-action {drop |
set-cos-as-sec-cos | set-cos-transmit 0-7 | set-sec-cos-transmit 0-7 |
set-prec-transmit 0-7 | set-dscp-transmit 0-63 | transmit} exceed-action
{drop | set-cos-as-sec-cos | set-cos-transmit 0-7 | set-sec-cos-transmit
0-7 | set-prec-transmit 0-7 | set-dscp-transmit 0-63 | transmit}
[violate-action {drop | set-cos-as-sec-cos-transmit | set-cos-transmit
0-7 | set-sec-cos-transmit 0-7 | set-prec-transmit 0-7 |
set-dscp-transmit 0-63 | transmit}]}
Mode Policy-Class-Map Config
police-two-rate
This command is the two-rate form of the police command and is used to establish the
traffic policing style for the specified class. For each outcome, the only possible actions are
drop, set-cos-as-sec-cos, set-cos-transmit, set-sec-cos-transmit, set-dscp-transmit,
set-prec-transmit, or transmit. In this two-rate form of the police command, the conform
Quality of Service Commands 952

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
action defaults to send, the exceed action defaults to drop, and the violate action defaults to
drop. These actions can be set with this command once the style has been configured.
Format police-two-rate {1-4294967295 1-4294967295 1-128 1-128 conform-action
{drop | set-cos-as-sec-cos | set-cos-transmit 0-7 | set-sec-cos-transmit
0-7 | set-prec-transmit 0-7 | set-dscp-transmit 0-63 | transmit}
exceed-action {drop | set-cos-as-sec-cos | set-cos-transmit 0-7 |
set-sec-cos-transmit 0-7 | set-prec-transmit 0-7 | set-dscp-transmit 0-63
| transmit} [violate-action {drop | set-cos-as-sec-cos | set-cos-transmit
0-7 | set-sec-cos-transmit 0-7 | set-prec-transmit 0-7 |
set-dscp-transmit 0-63 | transmit}]}
Mode Policy-Class-Map Config
policy-map
This command establishes a new DiffServ policy. The policyname parameter is a
case-sensitive alphanumeric string from 1 to 31 characters uniquely identifying the policy.
The type of policy is specific to the inbound traffic direction as indicated by the in parameter,
or the outbound traffic direction as indicated by the out parameter, respectively.
Note: The CLI mode is changed to Policy-Map Config when this command is
successfully executed.
Format policy-map policyname {in | out}
Mode Global Config
no policy-map
This command eliminates an existing DiffServ policy. The policyname parameter is the
name of an existing DiffServ policy. This command may be issued at any time. If the policy is
currently referenced by one or more interface service attachments, this delete attempt fails.
Format no policy-map policyname
Mode Global Config
policy-map rename
This command changes the name of a DiffServ policy. The policyname is the name of an
existing DiffServ class. The newpolicyname parameter is a case-sensitive alphanumeric
string from 1 to 31 characters uniquely identifying the policy.
Format policy-map rename policyname newpolicyname
Mode Global Config
Quality of Service Commands 953

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
DiffServ Service Commands
Use the DiffServ service commands to assign a DiffServ traffic conditioning policy, which you
specified by using the policy commands, to an interface in the incoming direction
The service commands attach a defined policy to a directional interface. You can assign only
one policy at any one time to an interface in the inbound direction. DiffServ is not used in the
outbound direction.
This set of commands consists of service addition or removal.
The CLI command root is service-policy.
service-policy
This command attaches a policy to an interface in the inbound direction as indicated by the
in parameter, or the outbound direction as indicated by the out parameter, respectively. The
policyname parameter is the name of an existing DiffServ policy. This command causes a
service to create a reference to the policy.
Note: This command effectively enables DiffServ on an interface in the
inbound direction. There is no separate interface administrative mode
command for DiffServ.
Note: This command fails if any attributes within the policy definition exceed
the capabilities of the interface. Once a policy is successfully attached
to an interface, any attempt to change the policy definition, that would
result in a violation of the interface capabilities, causes the policy
change attempt to fail.
Format service-policy {in | out} policymapname
Modes Global Config
Interface Config
Note: Each interface can have one policy attached.
no service-policy
This command detaches a policy from an interface in the inbound direction as indicated by
the in parameter, or the outbound direction as indicated by the out parameter, respectively.
The policyname parameter is the name of an existing DiffServ policy.
Quality of Service Commands 954

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: This command causes a service to remove its reference to the policy.
This command effectively disables DiffServ on an interface in the
inbound direction or an interface in the outbound direction. There is
no separate interface administrative 'mode' command for DiffServ.
Format no service-policy {in | out} policymapname
Modes Global Config
Interface Config
DiffServ Show Commands
Use the DiffServ show commands to display configuration and status information for classes,
policies, and services. You can display DiffServ information in summary or detailed formats.
The status information is only shown when the DiffServ administrative mode is enabled.
show class-map
This command displays all configuration information for the specified class. The
class-name is the name of an existing DiffServ class.
Format show class-map class-name
Modes Privileged EXEC
User EXEC
If the class-name is specified the following fields are displayed.
Term Definition
Class Name The name of this class.
Class Type A class type of all means every match criterion defined for the class is evaluated simultaneously and
must all be true to indicate a class match.
Class Layer3 The Layer 3 protocol for this class. Possible values are IPv4 and IPv6.
Protocol
Match Criteria The Match Criteria fields are only displayed if they have been configured. Not all platforms support
all match criteria values. They are displayed in the order entered by the user. The fields are
evaluated in accordance with the class type. The possible Match Criteria fields are: Destination IP
Address, Destination Layer 4 Port, Destination MAC Address, Ethertype, Source MAC Address,
VLAN, Class of Service, Every, IP DSCP, IP Precedence, IP TOS, Protocol Keyword, Reference
Class, Source IP Address, and Source Layer 4 Port.
Values The values of the Match Criteria.
Quality of Service Commands 955

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If you do not specify the Class Name, this command displays a list of all defined DiffServ
classes. The following fields are displayed.
Term Definition
Class Name The name of this class. (Note that the order in which classes are displayed is not necessarily the
same order in which they were created.)
Class Type A class type of all means every match criterion defined for the class is evaluated simultaneously and
must all be true to indicate a class match.
Ref Class Name The name of an existing DiffServ class whose match conditions are being referenced by the
specified class definition.
show diffserv
This command displays the DiffServ General Status Group information, which includes the
current administrative mode setting as well as the current and maximum number of rows in
each of the main DiffServ private MIB tables. This command takes no options.
Format show diffserv
Mode Privileged EXEC
Term Definition
DiffServ Admin mode The current value of the DiffServ administrative mode.
Class Table Size Current/Max The current and maximum number of entries (rows) in the Class Table.
Class Rule Table Size Current/Max The current and maximum number of entries (rows) in the Class Rule Table.
Policy Table Size Current/Max The current and maximum number of entries (rows) in the Policy Table.
Policy Instance Table Size Current/Max The current and maximum number of entries (rows) in the Policy Instance
Table.
Policy Instance Table Max Current/Max The current and maximum number of entries (rows) for the Policy Instance
Table.
Policy Attribute Table Max Current/Max The current and maximum number of entries (rows) for the Policy Attribute
Table.
Service Table Size Current/Max The current and maximum number of entries (rows) in the Service Table.
show policy-map
This command displays all configuration information for the specified policy. The
policyname is the name of an existing DiffServ policy.
Format show policy-map [policyname]
Mode Privileged EXEC
Quality of Service Commands 956

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If the Policy Name is specified the following fields are displayed.
Term Definition
Policy Name The name of this policy.
Policy Type The policy type (only inbound policy definitions are supported for this platform.)
Class Members The class that is a member of the policy.
The following information is repeated for each class associated with this policy (only those
policy attributes actually configured are displayed).
Term Definition
Assign Queue Directs traffic stream to the specified QoS queue. This allows a traffic classifier to specify which one
of the supported hardware queues are used for handling packets belonging to the class.
Class Name The name of this class.
Committed Burst The committed burst size, used in simple policing.
Size (KB)
Committed Rate The committed rate, used in simple policing.
(Kbps)
Conform Action The current setting for the action taken on a packet considered to conform to the policing
parameters. This is not displayed if policing is not in use for the class under this policy.
Conform Color The current setting for the color mode. Policing uses either color blind or color aware mode. Color
Mode blind mode ignores the coloration (marking) of the incoming packet. Color aware mode takes into
consideration the current packet marking when determining the policing outcome.
Conform COS The CoS mark value if the conform action is set-cos-transmit.
Conform DSCP The DSCP mark value if the conform action is set-dscp-transmit.
Value
Conform IP The IP Precedence mark value if the conform action is set-prec-transmit.
Precedence Value
Drop Drop a packet upon arrival. This is useful for emulating access control list operation using DiffServ,
especially when DiffServ and ACL cannot co-exist on the same interface.
Exceed Action The action taken on traffic that exceeds settings that the network administrator specifies.
Exceed Color The current setting for the color of exceeding traffic that the user may optionally specify.
Mode
Mark CoS The class of service value that is set in the 802.1p header of inbound packets. This is not displayed
if the mark cos was not specified.
Mark CoS as The secondary 802.1p priority value (second/inner VLAN tag. Same as CoS (802.1p) marking, but
Secondary CoS the dot1p value used for remarking is picked from the dot1p value in the secondary (i.e. inner) tag of
a double-tagged packet.
Mark IP DSCP The mark/re-mark value used as the DSCP for traffic matching this class. This is not displayed if
mark ip description is not specified.
Quality of Service Commands 957
