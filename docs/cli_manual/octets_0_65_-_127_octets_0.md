# octets_0_65_-_127_octets_0

Pages: 359-402

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Description
HC Overflow Pkts Total number of HC overflow packets.
HC Overflow Octets Total number of HC overflow octets.
HC Overflow Pkts 64 Octets Total number of HC overflow packets which are 64 octets in length
HC Overflow Pkts 65 - 127 Total number of HC overflow packets which are between 65 and 127 octets in length.
Octets
HC Overflow Pkts 128 - 255 Total number of HC overflow packets which are between 128 and 255 octets in length.
Octets
HC Overflow Pkts 256 - 511 Total number of HC overflow packets which are between 256 and 511 octets in length.
Octets
HC Overflow Pkts 512 - 1023 Total number of HC overflow packets which are between 512 and 1023 octets in
Octets length.
HC Overflow Pkts 1024 - 1518 Total number of HC overflow packets which are between 1024 and 1518 octets in
Octets length.
Command example:
(NETGEAR Switch) # show rmon statistics interfaces 1/0/1
Port: 1/0/1
Dropped: 0
Octets: 0 Packets: 0
Broadcast: 0 Multicast: 0
CRC Align Errors: 0 Collisions: 0
Undersize Pkts: 0 Oversize Pkts: 0
Fragments: 0 Jabbers: 0
64 Octets: 0 65 - 127 Octets: 0
128 - 255 Octets: 0 256 - 511 Octets: 0
512 - 1023 Octets: 0 1024 - 1518 Octets: 0
HC Overflow Pkts: 0 HC Pkts: 0
HC Overflow Octets: 0 HC Octets: 0
HC Overflow Pkts 64 Octets: 0 HC Pkts 64 Octets: 0
HC Overflow Pkts 65 - 127 Octets: 0 HC Pkts 65 - 127 Octets: 0
HC Overflow Pkts 128 - 255 Octets: 0 HC Pkts 128 - 255 Octets: 0
HC Overflow Pkts 256 - 511 Octets: 0 HC Pkts 256 - 511 Octets: 0
HC Overflow Pkts 512 - 1023 Octets: 0 HC Pkts 512 - 1023 Octets: 0
HC Overflow Pkts 1024 - 1518 Octets: 0 HC Pkts 1024 - 1518 Octets: 0
show rmon hcalarms
This command displays all entries or a specific entry in the RMON high-capacity alarm table.
Format show rmon {hcalarms | hcalarm alarm-index}
Mode Privileged Exec
Utility Commands 359

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Description
High Capacity Alarm Index An arbitrary integer index value used to uniquely identify the high capacity alarm entry. The
range is 1 to 65535.
High Capacity Alarm The object identifier of the particular variable to be sampled. Only variables that resolve to an
Variable ASN.1 primitive type of integer.
High Capacity Alarm The interval in seconds over which the data is sampled and compared with the rising and
Interval falling thresholds. The range is 1 to 2147483647. The default is 1.
High Capacity Alarm The method of sampling the selected variable and calculating the value to be compared
Sample Type against the thresholds. Possible types are Absolute Value or Delta Value. The default is
Absolute Value.
High Capacity Alarm The absolute value (that is, the unsigned value) of the hcAlarmVariable statistic during the
Absolute Value last sampling period. The value during the current sampling period is not made available until
the period is complete. This object is a 64-bit unsigned value that is Read-Only.
High Capacity Alarm This object indicates the validity and sign of the data for the high capacity alarm absolute
Absolute Alarm Status value object (hcAlarmAbsValueobject). Possible status types are valueNotAvailable,
valuePositive, or valueNegative. The default is valueNotAvailable.
High Capacity Alarm High capacity alarm startup alarm that may be sent. Possible values are rising, falling, or
Startup Alarm rising-falling. The default is rising-falling.
High Capacity Alarm The lower 32 bits of the absolute value for threshold for the sampled statistic. The range is 0
Rising-Threshold Absolute to 4294967295. The default is 1.
Value Low
High Capacity Alarm The upper 32 bits of the absolute value for threshold for the sampled statistic. The range is 0
Rising-Threshold Absolute to 4294967295. The default is 0.
Value High
High Capacity Alarm This object indicates the sign of the data for the rising threshold, as defined by the objects
Rising-Threshold Value hcAlarmRisingThresAbsValueLow and hcAlarmRisingThresAbsValueHigh. Possible values
Status are valueNotAvailable, valuePositive, or valueNegative. The default is valuePositive.
High Capacity Alarm The lower 32 bits of the absolute value for threshold for the sampled statistic. The range is 0
Falling-Threshold to 4294967295. The default is 1.
Absolute Value Low
High Capacity Alarm The upper 32 bits of the absolute value for threshold for the sampled statistic. The range is 0
Falling-Threshold to 4294967295. The default is 0.
Absolute Value High
High Capacity Alarm This object indicates the sign of the data for the falling threshold, as defined by the objects
Falling-Threshold Value hcAlarmFallingThresAbsValueLow and hcAlarmFallingThresAbsValueHigh. Possible values
Status are valueNotAvailable, valuePositive, or valueNegative. The default is valuePositive.
High Capacity Alarm The index of the eventEntry that is used when a rising threshold is crossed. The range is 1 to
Rising Event Index 65535. The default is 1.
High Capacity Alarm The index of the eventEntry that is used when a falling threshold is crossed. The range is 1 to
Falling Event Index 65535. The default is 2.
Utility Commands 360

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Description
High Capacity Alarm The number of times the associated hcAlarmVariable instance was polled on behalf of thie
Failed Attempts hcAlarmEntry (while in the active state) and the value was not available. This object is a
32-bit counter value that is read-only.
High Capacity Alarm The owner string associated with the alarm entry. The default is monitorHCAlarm.
Owner
High Capacity Alarm The type of non-volatile storage configured for this entry. This object is read-only. The default
Storage Type is volatile.
Command example:
(NETGEAR Switch) #show rmon hcalarms
Index OID Owner
----------------------------------------------
1 alarmInterval.1 MibBrowser
2 alarmInterval.1 MibBrowser
Command example:
(NETGEAR Switch) #show rmon hcalarm 1
Alarm 1
----------
OID: alarmInterval.1
Last Sample Value: 1
Interval: 1
Sample Type: absolute
Startup Alarm: rising-falling
Rising Threshold High: 0
Rising Threshold Low: 1
Rising Threshold Status: Positive
Falling Threshold High: 0
Falling Threshold Low: 1
Falling Threshold Status: Positive
Rising Event: 1
Falling Event: 2
Startup Alarm: Rising-Falling
Owner: MibBrowser
Utility Commands 361

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Statistics Application Commands
The statistics application gives you the ability to query for statistics on port utilization,
flow-based and packet reception on programmable time slots. The statistics application
collects the statistics at a configurable time range. You can specify the port number(s) or a
range of ports for statistics to be displayed. The configured time range applies to all ports.
Detailed statistics are collected between a specified time range in date and time format. You
can define the time range as having an absolute time entry and/or a periodic time. For
example, you can specify the statistics to be collected and displayed between 9:00 12 NOV
2011 (START) and 21:00 12 NOV 2012 (END) or schedule it on every Mon, Wed, and Fri
9:00 (START) to 21:00 (END).
You can receive the statistics in the following ways:
• User requests through the CLI for a set of counters.
• Configuring the device to display statistics using syslog or email alert. The syslog or email
alert messages are sent by the statistics application at END time.
You can configure the device to display statistics on the console. The collected statistics are
presented on the console at END time.
stats group (Global Config)
This command creates a new group with the specified id or name and configures the time
range and the reporting mechanism for that group.
Format stats group group-id | name timerange time-range name reporting
list-of-reporting-methods
Mode Global Config
Parameter Description
group ID, name Name of the group of statistics or its identifier to apply on the interface. The range is:
• 1. received
• 2. received-errors
• 3. transmitted
• 4. transmitted-errors
• 5. received-transmitted
• 6. port-utilization
• 7. congestion
The default is None.
Utility Commands 362

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
time range name Name of the time range for the group or the flow-based rule. The range is 1 to 31 alphanumeric
characters. The default is None.
list of reporting Report the statistics to the configured method. The range is:
methods • 0. none
• 1. console
• 2. syslog
• 3. e-mail
The default is None.
Command example:
(NETGEAR Switch) (Config)# stats group received timerange test reporting console email
syslog
(NETGEAR Switch) (Config)# stats group received-errors timerange test reporting email
syslog
(NETGEAR Switch) (Config)# stats group received- transmitted timerange test reporting
none
no stats group
This command deletes the configured group.
Format no stats group [group-id | name]
Mode Global Config
Command example:
(NETGEAR Switch) (Config)# no stats group received
(NETGEAR Switch) (Config)# no stats group received-errors
(NETGEAR Switch) (Config)# no stats group received-transmitted
stats flow-based (Global Config)
This command configures flow based statistics rules for the given parameters over the
specified time range. Only an IPv4 address is allowed as source and destination IP address
Format stats flow-based rule-id timerange time-range-name [{srcip ip-address} {dstip
ip-address} {srcmac mac-address} {dstmac mac-address} {srctcpport portid}
{dsttcpport portid} {srcudpport portid} {dstudpport portid}]
Mode Global Config
Utility Commands 363

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
rule ID The flow-based rule ID. The range is 1 to 16. The default is None.
time range name Name of the time range for the group or the flow-based rule. The range is 1 to 31 alphanumeric
characters. The default is None.
srcip ip-address The source IP address.
dstip ip-address The destination IP address.
srcmac The source MAC address.
mac-address
dstmac The destination MAC address.
mac-address
srctcpport portid The source TCP port number.
dsttcpport portid The destination TCP port number.
srcudpport portid The source UDP port number.
dstudpport portid The destination UDP port number.
Command example:
(NETGEAR Switch) (Config)#stats flow-based 1 timerange test srcip 1.1.1.1 dstip 2.2.2.2
srcmac 1234 dstmac 1234 srctcpport 123 dsttcpport 123 srcudpport 123 dstudpport 123
(NETGEAR Switch) (Config)#stats flow-based 2 timerange test srcip 1.1.1.1 dstip 2.2.2.2
srctcpport 123 dsttcpport 123 srcudpport 123 dstudpport 123
no stats flow-based
This command deletes flow-based statistics.
Format stats flow-based rule-id
Mode Global Config
Command example:
(NETGEAR Switch) (Config)# no stats flow-based 1
(NETGEAR Switch) (Config)# no stats flow-based 2
Utility Commands 364

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
stats flow-based reporting
This command configures the reporting mechanism for all the flow-based rules configured on
the system. There is no per flow-based rule reporting mechanism. Setting the reporting
method as none resets all the reporting methods.
Format stats flow-based reporting list-of-reporting-methods
Mode Global Config
Command example:
(NETGEAR Switch) (Config)# stats flow-based reporting console email syslog
(NETGEAR Switch) (Config)# stats flow-based reporting email syslog
(NETGEAR Switch) (Config)# stats flow-based reporting none
stats group (Interface Config)
This command applies the group specified on an interface or interface-range.
Format stats group [group-id | name]
Mode Interface Config
Parameter Description
group id The unique identifier for the group.
name The name of the group.
Command example:
(NETGEAR Switch) (Interface 1/0/1-1/0/10)# stats group 1
(NETGEAR Switch) (Interface 1/0/1-1/0/10)# stats group 2
no stats group
This command deletes the interface or interface-range from the group specified.
Format no stats group [group-id | name]
Mode Interface Config
Command example: .
(NETGEAR Switch) (Interface 1/0/1-1/0/10)# no stats group 1
(NETGEAR Switch) (Interface 1/0/1-1/0/10)# no stats group 2
Utility Commands 365

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
stats flow-based (Interface Config)
This command applies the flow-based rule specified by the ID on an interface or
interface-range.
Format stats flow-based rule-id
Mode Interface Config
Parameter Description
rule-id The unique identifier for the flow-based rule.
Command example:
(NETGEAR Switch) (Interface 1/0/1-1/0/10)# stats flow-based 1
(NETGEAR Switch) (Interface 1/0/1-1/0/10)# stats flow-based 2
no stats flow-based
This command deletes the interface or interface-range from the flow-based rule specified.
Format no stats flow-based rule-id
Mode Interface Config
Command example:
(NETGEAR Switch) (Interface 1/0/1-1/0/10)# no stats flow-based 1
(NETGEAR Switch) (Interface 1/0/1-1/0/10)# no stats flow-based 2
show stats group
This command displays the configured time range and the interface list for the group
specified and shows collected statistics for the specified time-range name on the interface list
after the time-range expiry.
Format show stats group [group-id | name]
Mode Privileged EXEC
Parameter Description
group id The unique identifier for the group.
name The name of the group.
Utility Commands 366

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show stats group received
Group: received
Time Range: test
Interface List
-----------------
1/0/2, 1/0/4, lag 1
Counter ID Interface Counter Value
------------------------- --------- ------------
R x Total 1 /0/2 951600
R x Total 1/0/4 304512
Rx Total l ag 1 0
R x 64 1 /0/2 0
R x 64 1/0/4 4758
Rx 64 l ag 1 0
R x 65to128 1 /0/2 0
R x 65to128 1 /0/4 0
Rx 65to128 l ag 1 0
Rx 128to255 1 /0/2 4758
R x 128to255 1 /0/4 0
R x 128to255 l ag 1 0
Rx 256to511 1 /0/2 0
Command example:
(NETGEAR Switch) #show stats group port-utilization
Group: port-utilization
Time Range: test
Interface List
--------------
1/0/2, 1/0/4, lag 1
Interface Utilization (%)
--------- ---------------
1/0/2 0
1/0/4 0
lag 1 0
Utility Commands 367

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show stats flow-based
This command displays the configured time range, flow-based rule parameters, and the
interface list for the flow specified.
Format show stats flow-based [rule-id | all]
Mode Privileged EXEC
Parameter Description
rule-id The unique identifier for the flow-based rule.
Command example:
(NETGEAR Switch) #show stats flow-based all
Flow based rule Id............................. 1
Time Range..................................... test
Source IP...................................... 1.1.1.1
Source MAC..................................... 1234
Source TCP Port................................ 123
Source UDP Port................................ 123
Destination IP................................. 2.2.2.2
Destination MAC................................ 1234
Destination TCP Port........................... 123
Destination UDP Port........................... 123
Interface List
--------------
1/0/1 - 1/0/2
Interface Hit Count
--------- ---------
1/0/1 100
1/0/2 0
Flow based rule Id............................. 2
Time Range..................................... test
Source IP...................................... 1.1.1.1
Source TCP Port................................ 123
Source UDP Port................................ 123
Destination IP................................. 2.2.2.2
Destination TCP Port........................... 123
Destination UDP Port........................... 123
Interface List
--------------
1/0/1 - 1/0/2
Utility Commands 368

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Interface Hit Count
--------- ---------
1/0/1 100
1/0/2 0
Command example:
(NETGEAR Switch) #show stats flow-based 2
Flow based rule Id............................. 2
Time Range..................................... test
Source IP...................................... 1.1.1.1
Source TCP Port................................ 123
Source UDP Port................................ 123
Destination IP................................. 2.2.2.2
Destination TCP Port........................... 123
Destination UDP Port........................... 123
Interface List
--------------
1/0/1 - 1/0/2
Interface Hit Count
--------- ---------
1/0/1 100
1/0/2 0
Utility Commands 369

Switching Commands

This chapter describes the switching commands.
The Switching Commands chapter includes the following sections:
• Port Configuration Commands
• Port Link Flap Commands
• Spanning Tree Protocol Commands
• Loop Protection Commands
• VLAN Commands
• Switch Port Commands
• Double VLAN Commands
• Private VLAN Commands
• Voice VLAN Commands
• Precision Time Protocol Commands
• Provisioning (IEEE 802.1p) Commands
• Asymmetric Flow Control
• Protected Ports Commands
• Private Group Commands
• GARP Commands
• GVRP Commands
• GMRP Commands
• Port-Based Network Access Control Commands
• 802.1X Supplicant Commands
• Storm-Control Commands
• Link Dependency Commands
• Link Local Protocol Filtering Commands
• MRP Commands
• MMRP Commands
• MVRP Commands

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
• Port-Channel/LAG (802.3ad) Commands
• Port Mirroring Commands
• Static MAC Filtering Commands
• DHCP L2 Relay Agent Commands
• DHCP Client Commands
• DHCP Snooping Configuration Commands
• Dynamic ARP Inspection Commands
• MVR Commands
• IGMP Snooping Configuration Commands
• IGMP Snooping Querier Commands
• MLD Snooping Commands
• MLD Snooping Querier Commands
• Port Security Commands
• LLDP (802.1AB) Commands
• LLDP-MED Commands
• Denial of Service Commands
• MAC Database Commands
• ISDP Commands
• Interface Error Disabling and Auto Recovery Commands
• UniDirectional Link Detection Commands
• Link Debounce Commands
The commands in this chapter are in one of three functional groups:
• Show commands. Display switch settings, statistics, and other information.
• Configuration commands. Configure features and options of the switch. For every
configuration command, there is a show command that displays the configuration setting.
• Clear commands. Clear some or all of the settings to factory defaults.
Switching Commands 371

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Port Configuration Commands
This section describes the commands you use to view and configure port settings.
interface (Global Config)
This command gives you access to the Interface Config mode, which allows you to enable or
modify the operation of an interface (port).
You can also specify a range of ports to configure at the same time by specifying the starting
unit/slot/port and ending unit/slot/port, separated by a hyphen.
Format interface {unit/slot/port | unit/slot/port-unit/slot/port}
Mode Global Config
Command example:
The following example enters Interface Config mode for port 1/0/1:
(NETGEAR Switch) #configure
(NETGEAR Switch) (config)#interface 1/0/1
(NETGEAR Switch) (interface 1/0/1)#
Command example:
The following example enters Interface Config mode for ports 1/0/1 through 1/0/4:
(NETGEAR Switch) #configure
(NETGEAR Switch) (config)#interface 1/0/1-1/0/4
(NETGEAR Switch) (interface 1/0/1-1/0/4)#
auto-negotiate
This command enables automatic negotiation on a port or range of ports.
Default enabled
Format auto-negotiate
Mode Interface Config
Switching Commands 372

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no auto-negotiate
This command disables automatic negotiation on a port.Automatic sensing is disabled when
automatic negotiation is disabled.
Format no auto-negotiate
Mode Interface Config
auto-negotiate all
This command enables automatic negotiation on all ports.
Default enabled
Format auto-negotiate all
Mode Global Config
no auto-negotiate all
This command disables automatic negotiation on all ports.
Format no auto-negotiate all
Mode Global Config
description (Interface Config)
Use this command to create an alpha-numeric description of an interface or range of
interfaces.
Format description description
Mode Interface Config
mtu
Use the mtu command to set the maximum transmission unit (MTU) size, in bytes, for frames
that ingress or egress the interface. You can use the mtu command to configure jumbo frame
support for physical and port-channel (LAG) interfaces. The MTU size is a valid integer
between 1522–9216 for tagged packets and a valid integer between 1518 - 9216 for
untagged packets.
Switching Commands 373

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: To receive and process packets, the Ethernet MTU must include any
extra bytes that Layer-2 headers might require. To configure the IP
MTU size, which is the maximum size of the IP packet (IP Header + IP
payload), see ip mtu on page673.
Default 9198 (untagged)
Format mtu size
Mode Interface Config
no mtu
This command sets the default MTU size (in bytes) for the interface.
Format no mtu
Mode Interface Config
shutdown (Interface Config)
This command disables a port or range of ports.
Note: You can use the shutdown command on physical and port-channel
(LAG) interfaces, but not on VLAN routing interfaces.
Default enabled
Format shutdown
Mode Interface Config
no shutdown
This command enables a port.
Format no shutdown
Mode Interface Config
shutdown all
This command disables all ports.
Switching Commands 374

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: You can use the shutdown all command on physical and
port-channel (LAG) interfaces, but not on VLAN routing interfaces.
Default enabled
Format shutdown all
Mode Global Config
no shutdown all
This command enables all ports.
Format no shutdown all
Mode Global Config
speed
Use this command to enable or disable auto-negotiation and set the speed that will be
advertised by that port. The duplex parameter allows you to set the advertised speed for both
half as well as full duplex mode.
Use the auto keyword to enable auto-negotiation on the port. Use the command without the
auto keyword to ensure auto-negotiation is disabled and to set the port speed and mode
according to the command values. If auto-negotiation is disabled, the speed and duplex
mode must be set.
Default Auto-negotiation is enabled.
Format speed {auto {10G | 5G | 2.5G | 1000 | 100} [half-duplex | full-duplex] | {10G
| 5G | 2.5G | 1000 | 100} {half-duplex | full-duplex}}
Mode Interface Config
speed all 100
This command sets the speed to 100 Mbps and sets the duplex setting for all interfaces.
Format speed all 100 {half-duplex | full-duplex}
Mode Global Config
Switching Commands 375

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show port
This command displays port information.
Format show port {intf-range | all}
Mode Privileged EXEC
Term Definition
Interface unit/slot/port
Type If not blank, this field indicates that this port is a special type of port. The possible values are:
• Mirror. The port is a monitoring port. For more information, see Port Mirroring Commands on
p age528.
• PC Mbr. The port is a member of a port-channel (LAG).
• Probe. The port is a probe port.
Admin Mode The Port control administration state. The port must be enabled in order for it to be allowed into the
network. May be enabled or disabled. The factory default is enabled.
Admin Status If the Admin Mode indicates that a port is disabled, this field states the reason why the port is
disabled.
Physical Mode The desired port speed and duplex mode. If auto-negotiation support is selected, then the duplex
mode and speed is set from the auto-negotiation process. Note that the maximum capability of the
port (full duplex -100M) is advertised. Otherwise, this object determines the port's duplex mode and
transmission rate. The factory default is Auto.
Physical Status The port speed and duplex mode.
Link Status The Link is up or down.
Link Trap This object determines whether or not to send a trap when link status changes. The factory default is
enabled.
LACP Mode LACP is enabled or disabled on this port.
Command example:
The following example shows output for all ports:
(NETGEAR Switch) #show port all
Admin Physical Physical Link Link LACP Actor
Intf Type Mode Mode Status Status Trap Mode Timeout
--------- ------ --------- ---------- ---------- ------ ------- ------ --------
0/1 Enable Auto 100 Full Up Enable Enable long
0/2 Enable Auto 100 Full Up Enable Enable long
0/3 Enable Auto Down Enable Enable long
0/4 Enable Auto 100 Full Up Enable Enable long
0/5 Enable Auto 100 Full Up Enable Enable long
0/6 Enable Auto 100 Full Up Enable Enable long
0/7 Enable Auto 100 Full Up Enable Enable long
0/8 Enable Auto 100 Full Up Enable Enable long
Switching Commands 376

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
1/1 Enable Down Disable N/A N/A
1/2 Enable Down Disable N/A N/A
1/3 Enable Down Disable N/A N/A
1/4 Enable Down Disable N/A N/A
1/5 Enable Down Disable N/A N/A
1/6 Enable Down Disable N/A N/A
Command example:
The following example shows output for a range of ports:
(NETGEAR Switch) #show port 0/1-1/6
Admin Physical Physical Link Link LACP Actor
Intf Type Mode Mode Status Status Trap Mode Timeout
--------- ------ --------- ---------- ---------- ------ ------- ------ --------
0/1 Enable Auto 100 Full Up Enable Enable long
0/2 Enable Auto 100 Full Up Enable Enable long
0/3 Enable Auto Down Enable Enable long
0/4 Enable Auto 100 Full Up Enable Enable long
0/5 Enable Auto 100 Full Up Enable Enable long
0/6 Enable Auto 100 Full Up Enable Enable long
0/7 Enable Auto 100 Full Up Enable Enable long
0/8 Enable Auto 100 Full Up Enable Enable long
1/1 Enable Down Disable N/A N/A
1/2 Enable Down Disable N/A N/A
1/3 Enable Down Disable N/A N/A
1/4 Enable Down Disable N/A N/A
1/5 Enable Down Disable N/A N/A
1/6 Enable Down Disable N/A N/A
show port advertise
Use this command to display the local administrative link advertisement configuration, local
operational link advertisement, and the link partner advertisement for an interface. It also
displays priority resolution for speed and duplex as per 802.3 Annex 28B.3. It displays the
auto-negotiation state, physical master/slave clock configuration, and link state of the port.
If the link is down, the clock is displayed as No Link, and a dash is displayed against the Oper
Peer advertisement, and Priority Resolution. If auto-negotiation is disabled, then the admin
Local Link advertisement, operational local link advertisement, operational peer
advertisement, and Priority resolution fields are not displayed.
If this command is executed without the optional unit/slot/port parameter, then it
displays the auto-negotiation state and operational Local link advertisement for all the ports.
Operational link advertisement will display speed only if it is supported by both local as well
as link partner. If auto-negotiation is disabled, then operational local link advertisement is not
displayed.
Switching Commands 377

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format show port advertise [unit/slot/port]
Mode Privileged EXEC
Command example:
The following example shows output with an optional parameter:
(NETGEAR switch)#show port advertise 0/1
Port: 0/1
Type: Gigabit - Level
Link State: Down
Auto Negotiation: Enabled
Clock: Auto
1000f 1000h 100f 100h 10f 10h
----- ----- ---- ---- --- ---
Admin Local Link Advertisement no no yes no yes no
Oper Local Link Advertisement no no yes no yes no
Oper Peer Advertisement no no yes yes yes yes
Priority Resolution - - yes - - -
Command example:
The following example shows output without an optional parameter:
(NETGEAR switch)#show port advertise
P ort Type N eg Operational Link Advertisement
- -------- ------------------------------ ----------- ------------------------------
0 /1 Gigabit - Level E nabled 1000f, 100f, 100h, 10f, 10h
0 /2 G igabit - Level E nabled 1000f, 100f, 100h, 10f, 10h
0 /3 G igabit - Level E nabled 1000f, 100f, 100h, 10f, 10h
show port description
This command displays the interface description. Instead of unit/slot/port, lag
lag-intf-num can be used as an alternate way to specify the LAG interface, in which
lag-intf-num is the LAG port number.
Format show port description [unit/slot/port | lag lag-intf-num]
Mode Privileged EXEC
Term Definition
Interface unit/slot/port
ifIndex The interface index number associated with the port.
Switching Commands 378

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Description The alpha-numeric description of the interface created by the command description (Interface
Config) on page373.
MAC address The MAC address of the port. The format is 6 two-digit hexadecimal numbers that are separated by
colons, for example 01:23:45:67:89:AB.
Bit Offset Val The bit offset value.
Command example:
(NETGEAR switch) #show port description 0/1
Interface...........0/1
ifIndex.............1
Description.........
MAC address.........00:10:18:82:0C:10
Bit Offset Val......1
show port status
This command displays the status for and the state of all or specified networking ports.
Format show port status [unit/slot/port | all | lag]
Mode Privileged EXEC
Term Definition
Intf The interface in the unit/slot/port format.
Media Type • auto-select. The media type is automatically selected. The preferred media type is
displayed.
• RJ45. The media type is RJ45.
• SFP. The media type is SFP.
STP Mode Indicates whether spanning tree mode is enabled or disabled.
Physical Mode The port speed and duplex mode. The maximum capability of the port is advertised. If
autonegotiation support is enabled, the duplex mode and speed are set through the
autonegotiation process.
Physical Status The port speed and duplex mode.
Link Status Indicates whether the link is up or down.
Loop Status Indicates whether a loop was diagnosed.
Partner Flow Control Indicates whether flow control at the remote end is enabled or disabled.
Switching Commands 379

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
debug dynamic ports
This command enables debug messages that are related to dynamic ports, that is, combo
ports that are capable of detecting the media type (SFP [fiber] or Ethernet [copper]).
Format debug dynamic ports
Mode Privileged EXEC
no debug dynamic ports
This command disables debug messages that are related to dynamic ports, that is, combo
ports that are capable of detecting the media type (SFP [fiber] or Ethernet [copper]).
Format no debug dynamic ports
Mode Privileged EXEC
Expandable Port Configuration Commands for 40G Ports
on the APM402XL Port Card
This section describes the commands that you can use to view and configure expandable
port settings.
By default, the 40G ports on the APM402XL port card (that is, port 1 and port 5) are active,
which means that they are in the attached state, can be detected, and you can use them. The
expandable 10G ports on the APM402XL port card (that is, ports 2–4 on the first 40G port
and ports 6–8 on the second 40G port) are nonactive, which means that they are in the
detached state and you cannot use them.
In the following example, the output of the show port all command for the APM402XL
port card displays the following:
• The first 40G port is configured as four expendable 10G ports with port numbers 1/1/1 to
1/1/4, the ports are in the active state, and the link status for each port is up.
• The second 40G port is in its default configuration, the 40G port number is 1/1/5, the port
is in the active state, and the link status is down. The expandable 10G ports 1/1/6 to 1/1/8
are in the nonactive state, which means that they are in the detached state and you
cannot use them.
(Netgear Switch) #show port all
Admin Physical Physical Link Link LACP Flow
Intf Type Mode Mode Status Status Trap Mode Mode
--------- ------ --------- ---------- ---------- ------ ------- ------ -------
1/1/1 Enable 10G Full 10G Full Up Enable Enable Disable
1/1/2 Enable 10G Full 10G Full Up Enable Enable Disable
1/1/3 Enable 10G Full 10G Full Up Enable Enable Disable
1/1/4 Enable 10G Full 10G Full Up Enable Enable Disable
Switching Commands 380

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
1/1/5 Enable 40G Full Down Enable Enable Disable
1/1/6 Enable 10G Full Detach Enable Enable Disable
1/1/7 Enable 10G Full Detach Enable Enable Disable
1/1/8 Enable 10G Full Detach Enable Enable Disable
hardware profile portmode
This command configures a 40G QSFP port on the APM402XL port card either in the 4x10G
or mode or the 1x40G mode.
You can execute this command only on interfaces that support the expandable port feature.
Entering the command on any other type of interface yields an error.
The configuration that you make to a 40G port or to an expanded 40G port (four 10G ports) is
retained whether the port status is attached or detached. However, a configuration change is
applied only when the port is in the attached state.
For example, if you change the configuration on the four 10G ports with port numbers 5 to 8
and then return the port to a single 40G port with port number 5, the configuration for ports 5
to 8 is retained in the running configuration but is not applied. The configuration is applied
only after you expand port 5 again to four 10G ports with port numbers 5 to 8. Similarly, when
you change the configuration in 40G mode, the configuration is retained in the running
configuration, but is applied only when the port is functioning in 40G mode.
The possible values for the mode argument are the following:
• 1x40G. Configures the port as a single 40G port.
• 4x10G. Configures the port as four 10G ports.
Note: This command cannot operate in the interface range mode.
Default The default mode of QSFP port is 1x40G
Format hardware profile portmode mode
Mode Interface Config
no hardware profile portmode
This command sets the ports on the APM402XL port card to their default mode, that is, to the
1x40G mode.
Format no hardware profile portmode
Mode Interface Config
Switching Commands 381

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show interfaces hardware profile
This command displays the hardware profile information for the ports that support the
expandable port feature. The command displays the 40G ports and the corresponding 10G
ports.
As an option, you can specify an interface.
Format show interfaces hardware profile [interface]
Mode Privileged EXEC
Port Configuration for the Third-Party TPM404H HDMI Port
Card
Model M4300-96X running release 12.0.8.15 or a later release supports the third-party
TPM404H HDMI port card. This port card provides four HDMI ports that are mapped to four
10G ports in the M4300-96X chassis. The HDMI ports are input ports, which means that they
convert an incoming HDMI signal to Ethernet frames. The Ethernet frames are then
forwarded like any other Ethernet frame in the switch.
Because of thermal restrictions, you can install a TPM404H HDMI port card only in the upper
slots (1–6) of the M4300-96X chassis. If you install the port card in a lower slot (7–12), the
following occurs:
• The following error message shows on the console and a similar message is also
generated and logged in buffered logs:
TPM404H card can only be installed in the slots on the top row.
• The port card is neither programmed nor initialized.
• The port card remains nonfunctional and does not show in the output of the show slot
command.
In the output of the show port command, the link state for the TPM404H HDMI port card
shows as Up, even if the HDMI cable is not connected. The output of the show port
command also shows that the physical mode and physical status of an HDMI port are set to
10G Full (for full duplex), and autonegotiation is not enabled. If you try to configure a different
speed for an HDMI port or enable autonegotiation, an error is generated.
The following example shows the output of the show port command when a TPM404H
HDMI port card is installed in slot 5 of the M4300-96X chassis:
(M4300-96X) #show port 1/5/1-1/5/4
Admin Physical Physical Link Link LACP Flow Stack
Intf Type Mode Mode Status Status Trap Mode Mode Capable
--------- ------ --------- ---------- ---------- ------ ------- ------ ------- --------
1/5/1 Enable 10G Full 10G Full Up Enable Enable Disable Yes
1/5/2 Enable 10G Full 10G Full Up Enable Enable Disable Yes
1/5/3 Enable 10G Full 10G Full Up Enable Enable Disable Yes
1/5/4 Enable 10G Full 10G Full Up Enable Enable Disable Yes
Switching Commands 382

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The output of the show slot number command for a slot in which a TPM404H HDMI port
card is installed displays information about the port card, as shown in the following example:
(M4300-96X) #show slot 1/5
Slot.............................. 1/5
Slot Status....................... Full
Admin State....................... Enable
Power State....................... Enable
Inserted Card:
Model Identifier............... TPM404H
Card Description............... TPM404H HDMI 4-port card
Configured Card:
Model Identifier............... TPM404H
Card Description............... TPM404H HDMI 4-port card
Power Down........................ Yes
Serial Number..................... HZ80K800001A
Vendor Name....................... ZeeVee
Manufacturer ID................... 1
FPGA Version...................... 4.0.0.106.0.0.0.0
Software Version.................. 1.0.6.0
Board Revision ID................. 2
Product Name...................... Z4KNGENC4
Product Description............... 4-HDMI Interfaces In with 4 IR Out and 1 IR In
Note: In the previous example for model M4300-96X, a third-party HDMI
port card is shown in slot 1/5. You can insert a third-party HDMI port
card in any of the upper slots (1–6), but not in the lower slots.
Port Link Flap Commands
The switch can detect the number of link-flaps that occur on all ports. If the number of
link-flaps on a port exceeds a configured threshold during a configured period, the port can
be placed in the D-Disable state.
By enabling auto-recovery, the port can automatically be activated again. You can also
activate the port manually.
Switching Commands 383

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
link-flap d-disable
This command enables the link-flap feature on the switch. When enabled, the switch counts
the number of link flaps on a port during a configured period. If the number of link flaps on a
port exceeds a configured threshold, the port is placed in the D-Disable state.
Default enabled
Format link-flap d-disable
Mode Global Config
no link-flap d-disable
This command disables the link-flap feature on the switch.
Format no link-flap d-disable
Mode Global Config
link-flap d-disable duration
This command configures the maximum period that a port is allowed to flap before the port is
placed in the D-Disable state.
The duration argument can be from 3 to 200 seconds. The default is 10 seconds.
Default 10 seconds
Format link-flap d-disable duration duration
Mode Global Config
no link-flap d-disable duration
This command sets the link-flap duration to its defaults of 10 seconds.
Format no link-flap d-disable duration
Mode Global Config
link-flap d-disable max-count
This command configures the maximum number of flaps that are allowed before the port is
placed in the D-Disable state.
The count argument can be a number from 2 to 100. The default number is 5.
Default 5
Format link-flap d-disable max-count count
Mode Global Config
Switching Commands 384

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no link-flap d-disable max-count
This command sets the maximum number of allowed link flaps to its defaults of 5.
Format no link-flap d-disable max-count
Mode Global Config
show link-flap d-disable
This command displays the link-flap settings.
Format show link-flap d-disable
Mode Global Config
Term Definition
Admin State Shows whether the link-flap feature is enabled or not.
Duration (in seconds) The maximum period that link flaps are allowed.
Max-Count The maximum number of link flaps that are allowed.
Spanning Tree Protocol Commands
This section describes the commands you use to configure Spanning Tree Protocol (STP).
STP helps prevent network loops, duplicate messages, and network instability.
Note: STP is enabled on the switch and on all ports and LAGs by default.
If STP is disabled, the system does not forward BPDU messages.
spanning-tree
This command sets the spanning-tree operational mode to enabled.
Default enabled
Format spanning-tree
Mode Global Config
Switching Commands 385

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no spanning-tree
This command sets the spanning-tree operational mode to disabled. While disabled, the
spanning-tree configuration is retained and can be changed, but is not activated.
Format no spanning-tree
Mode Global Config
spanning-tree auto-edge
Use this command to allow the interface to become an edge port if it does not receive any
BPDUs within a given amount of time.
Default Enabled
Format spanning-tree auto-edge
Mode Interface Config
no spanning-tree auto-edge
This command resets the auto-edge status of the port to the default value.
Format no spanning-tree auto-edge
Mode Interface Config
spanning-tree backbonefast
Use this command to enable the detection of indirect link failures and accelerate spanning
tree convergence on PVSTP configured switches.
Backbonefast accelerates finding an alternate path when an indirect link to the root port goes
down.
Backbonefast can be configured even if the switch is configured for MST(RSTP) or PVST
mode. It only has an effect when the switch is configured for the PVST mode.
If a backbonefast-enabled switch receives an inferior BPDU from its designated switch on a
root or blocked port, it sets the maximum aging time on the interfaces on which it received the
inferior BPDU if there are alternate paths to the designated switch. This allows a blocked port
to immediately move to the listening state where the port can be transitioned to the
forwarding state in the normal manner.
On receipt of an inferior BPDU from a designated bridge, backbonefast enabled switches
send a Root Link Query (RLQ) request to all non-designated ports except the port from which
it received the inferior BPDU. This check validates that the switch can receive packets from
the root on ports where it expects to receive BPDUs. The port from which the original inferior
BPDU was received is excluded because it has already encountered a failure. Designated
ports are excluded as they do not lead to the root.
Switching Commands 386

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
On receipt of an RLQ response, if the answer is negative, the receiving port has lost
connection to the root and its BPDU is immediately aged out. If all nondesignated ports have
already received a negative answer, the whole bridge has lost the root and can start the STP
calculation from scratch.
If the answer confirms the switch can access the root bridge on a port, it can immediately age
out the port on which it initially received the inferior BPDU.
A bridge that sends an RLQ puts its bridge ID in the PDU. This ensures that it does not flood
the response on designated ports.
A bridge that receives an RLQ and has connectivity to the root forwards the query toward the
root through its root port.
A bridge that receives a RLQ request and does not have connectivity to the root (switch
bridge ID is different from the root bridge ID in the query) or is the root bridge immediately
answers the query with its root bridge ID.
RLQ responses are flooded on designated ports.
Default NA
Format spanning-tree backbonefast
Mode Global Config
no spanning-tree backbonefast
This command disables backbonefast.
Note: PVRSTP embeds support for FastBackbone and FastUplink. Even if
FastUplink and FastBackbone are configured, they are effective only
in PVSTP mode.
Format no spanning-tree backbonefast
Mode Global Config
spanning-tree bpdufilter
Use this command to enable BPDU Filter on an interface or range of interfaces.
Default Disabled
Format spanning-tree bpdufilter
Mode Interface Config
Switching Commands 387

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no spanning-tree bpdufilter
Use this command to disable BPDU Filter on the interface or range of interfaces.
Default Disabled
Format no spanning-tree bpdufilter
Mode Interface Config
spanning-tree bpdufilter default
Use this command to enable BPDU Filter on all the edge port interfaces.
Default Disabled
Format spanning-tree bpdufilter default
Mode Global Config
no spanning-tree bpdufilter default
Use this command to disable BPDU Filter on all the edge port interfaces.
Default Disabled
Format no spanning-tree bpdufilter default
Mode Global Config
spanning-tree bpduflood
Use this command to enable BPDU Flood on an interface or range of interfaces.
Default Disabled
Format spanning-tree bpduflood
Mode Interface Config
no spanning-tree bpduflood
Use this command to disable BPDU Flood on the interface or range of interfaces.
Default Disabled
Format no spanning-tree bpduflood
Mode Interface Config
Switching Commands 388

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
spanning-tree bpduguard
Use this command to enable BPDU Guard on the switch.
Default Disabled
Format spanning-tree bpduguard
Mode Global Config
no spanning-tree bpduguard
Use this command to disable BPDU Guard on the switch.
Default Disabled
Format no spanning-tree bpduguard
Mode Global Config
spanning-tree bpdumigrationcheck
Use this command to force a transmission of rapid spanning tree (RSTP) and multiple
spanning tree (MSTP) BPDUs. Use the unit/slot/port parameter to transmit a BPDU
from a specified interface, or use the all keyword to transmit RST or MST BPDUs from all
interfaces. This command forces the BPDU transmission when you execute it, so the
command does not change the system configuration or have a no version.
Format spanning-tree bpdumigrationcheck {unit/slot/port | all}
Mode Global Config
spanning-tree configuration name
This command sets the Configuration Identifier Name for use in identifying the configuration
that this switch is currently using. The name parameter is a string of up to 32 characters.
Default base MAC address in hexadecimal notation
Format spanning-tree configuration name name
Mode Global Config
no spanning-tree configuration name
This command resets the Configuration Identifier Name to its default.
Format no spanning-tree configuration name
Mode Global Config
Switching Commands 389

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
spanning-tree configuration revision
This command sets the Configuration Identifier Revision Level for use in identifying the
configuration that this switch is currently using. The Configuration Identifier Revision Level is
a number in the range of 0 to 65535.
Default 0
Format spanning-tree configuration revision number
Mode Global Config
no spanning-tree configuration revision
This command sets the Configuration Identifier Revision Level for use in identifying the
configuration that this switch is currently using to the default value.
Format no spanning-tree configuration revision
Mode Global Config
spanning-tree cost
Use this command to configure the external path cost for port used by a MST instance. When
the auto keyword is used, the path cost from the port to the root bridge is automatically
determined by the speed of the interface. To configure the cost manually, specify a cost
value from 1–200000000.
Default auto
Format spanning-tree cost {cost | auto}
Mode Interface Config
no spanning-tree cost
This command resets the auto-edge status of the port to the default value.
Format no spanning-tree cost
Mode Interface Config
spanning-tree edgeport
This command specifies that an interface (or range of interfaces) is an Edge Port within the
common and internal spanning tree. This allows this port to transition to Forwarding State
without delay.
Format spanning-tree edgeport
Mode Interface Config
Switching Commands 390

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no spanning-tree edgeport
This command specifies that this port is not an Edge Port within the common and internal
spanning tree.
Format no spanning-tree edgeport
Mode Interface Config
spanning-tree forward-time
This command sets the Bridge Forward Delay parameter to a new value for the common and
internal spanning tree. The forward-time value is in seconds within a range of 4 to 30, with
the value being greater than or equal to “(Bridge Max Age / 2) + 1”.
Default 15
Format spanning-tree forward-time value
Mode Global Config
no spanning-tree forward-time
This command sets the Bridge Forward Delay parameter for the common and internal
spanning tree to the default value.
Format no spanning-tree forward-time
Mode Global Config
spanning-tree guard
This command selects whether loop guard or root guard is enabled on an interface or range
of interfaces. If neither is enabled, then the port operates in accordance with the multiple
spanning tree protocol.
Default none
Format spanning-tree guard {none | root | loop}
Mode Interface Config
no spanning-tree guard
This command disables loop guard or root guard on the interface.
Format no spanning-tree guard
Mode Interface Config
Switching Commands 391

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
spanning-tree max-age
This command sets the Bridge Max Age parameter to a new value for the common and
internal spanning tree. The max-age value is in seconds within a range of 6 to 40, with the
value being less than or equal to 2 x (Bridge Forward Delay - 1).
Default 20
Format spanning-tree max-age value
Mode Global Config
no spanning-tree max-age
This command sets the Bridge Max Age parameter for the common and internal spanning
tree to the default value.
Format no spanning-tree max-age
Mode Global Config
spanning-tree max-hops
This command sets the Bridge Max Hops parameter to a new value for the common and
internal spanning tree. The max-hops value is a range from 6 to 40.
Default 20
Format spanning-tree max-hops value
Mode Global Config
no spanning-tree max-hops
This command sets the Bridge Max Hops parameter for the common and internal spanning
tree to the default value.
Format no spanning-tree max-hops
Mode Global Config
spanning-tree mode
This command configures the global spanning tree mode. On a switch, only one mode can be
enabled at a time.
When PVSTP or rapid PVSTP (PVRSTP) is enabled, MSTP/RSTP/STP is operationally
disabled. To reenable MSTP/RSTP/STP, disable PVSTP/PVRSTP. By default, a NETGEAR
managed switch is enabled for RSTP. In PVSTP or PVRSTP mode, BPDUs contain
per-VLAN information instead of the common spanning-tree information (MST/RSTP).
Switching Commands 392

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
PVSTP maintains independent spanning tree information about each configured VLAN.
P VSTP uses IEEE 802.1Q trunking and allows a trunked VLAN to maintain blocked or
forwarding state per port on a per-VLAN basis. This allows a trunk port to be forwarded on
some VLANs and blocked on other VLANs.
P VRSTP is based on the IEEE 8012.1w standard. It supports fast convergence IEEE
802.1D. PVRSTP is compatible with I EEE 802.1D spanning tree. PVRSTP sends BPDUs on
all ports, instead of only the root bridge sending BPDUs, and supports the discarding,
learning, and forwarding states.
When the mode is changed to PVRSTP, version 0 STP BPDUs are no longer transmitted and
version 2 PVRSTP BPDUs that carry per-VLAN information are transmitted on the VLANs
enabled for spanning-tree. If a version 0 BPDU is seen, PVRSTP reverts to sending version 0
BPDUs.
Per VLAN Rapid Spanning Tree Protocol (PVRSTP) embeds support for PVSTP
FastBackbone and FastUplink. There is no provision to enable or disable these features in
PVRSTP.
Default Disabled
Format spanning-tree mode {mst | pvst | rapid-pvst | rstp | stp}
Mode Global Config
spanning-tree mst
This command sets the Path Cost or Port Priority for this port within the multiple spanning
tree instance or in the common and internal spanning tree. If you specify an mstid
parameter that corresponds to an existing multiple spanning tree instance, the configurations
are done for that multiple spanning tree instance. If you specify 0 (defined as the default
CIST ID) as the mstid, the configurations are done for the common and internal spanning
tree instance.
If you specify the cost option, the command sets the path cost for this port within a multiple
spanning tree instance or the common and internal spanning tree instance, depending on the
mstid parameter. You can set the path cost as a number in the range of 1 to 200000000 or
auto. If you select auto the path cost value is set based on Link Speed.
If you specify the port-priority option, this command sets the priority for this port within
a specific multiple spanning tree instance or the common and internal spanning tree
instance, depending on the mstid parameter. The port-priority value is a number in the
range of 0 to 240 in increments of 16.
Default cost—auto
port-priority—128
Format spanning-tree mst mstid {{cost number | auto} | port-priority number}
Mode Interface Config
Switching Commands 393

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no spanning-tree mst
This command sets the Path Cost or Port Priority for this port within the multiple spanning
tree instance, or in the common and internal spanning tree to the respective default values. If
you specify an mstid parameter that corresponds to an existing multiple spanning tree
instance, you are configuring that multiple spanning tree instance. If you specify 0 (defined as
the default CIST ID) as the mstid, you are configuring the common and internal spanning
tree instance.
If the you specify cost, this command sets the path cost for this port within a multiple
spanning tree instance or the common and internal spanning tree instance, depending on the
mstid parameter, to the default value, i.e., a path cost value based on the Link Speed.
If you specify port-priority, this command sets the priority for this port within a specific
multiple spanning tree instance or the common and internal spanning tree instance,
depending on the mstid parameter, to the default value.
Format no spanning-tree mst mstid {cost | port-priority}
Mode Interface Config
spanning-tree mst instance
This command adds a multiple spanning tree instance to the switch. The parameter mstid is
a number within a range of 1 to 4094, that corresponds to the new instance ID to be added.
The maximum number of multiple instances supported by the switch is 4.
Default none
Format spanning-tree mst instance mstid
Mode Global Config
no spanning-tree mst instance
This command removes a multiple spanning tree instance from the switch and reallocates all
VLANs allocated to the deleted instance to the common and internal spanning tree. The
parameter mstid is a number that corresponds to the desired existing multiple spanning tree
instance to be removed.
Format no spanning-tree mst instance mstid
Mode Global Config
spanning-tree mst priority
This command sets the bridge priority for a specific multiple spanning tree instance. The
parameter mstid is a number that corresponds to the desired existing multiple spanning tree
instance. The priority value is a number within a range of 0 to 4094.
Switching Commands 394

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If you specify 0 (defined as the default CIST ID) as the mstid, this command sets the Bridge
Priority parameter to a new value for the common and internal spanning tree. The bridge
priority value is a number within a range of 0 to 4094. The twelve least significant bits are
masked according to the 802.1s specification. This causes the priority to be rounded down to
the next lower valid priority.
Default 32768
Format spanning-tree mst priority mstid value
Mode Global Config
no spanning-tree mst priority
This command sets the bridge priority for a specific multiple spanning tree instance to the
default value. The parameter mstid is a number that corresponds to the desired existing
multiple spanning tree instance.
If 0 (defined as the default CIST ID) is passed as the mstid, this command sets the Bridge
Priority parameter for the common and internal spanning tree to the default value.
Format no spanning-tree mst priority mstid
Mode Global Config
spanning-tree mst vlan
This command adds an association between a multiple spanning tree instance and one or
more VLANs so that the VLAN(s) are no longer associated with the common and internal
spanning tree. The parameter mstid is a multiple spanning tree instance identifier, in the
range of 0 to 4094, that corresponds to the desired existing multiple spanning tree instance.
The vlanid can be specified as a single VLAN, a list, or a range of values. To specify a list
of VLANs, enter a list of VLAN IDs in the range 1 to 4093, each separated by a comma with
no spaces in between. To specify a range of VLANs, separate the beginning and ending
VLAN ID with a dash (-). Spaces and zeros are not permitted. The VLAN IDs may or may not
exist in the system.
Format spanning-tree mst vlan mstid vlanid
Mode Global Config
no spanning-tree mst vlan
This command removes an association between a multiple spanning tree instance and one
or more VLANs so that the VLAN(s) are again associated with the common and internal
spanning tree.
Format no spanning-tree mst vlan mstid vlanid
Mode Global Config
Switching Commands 395

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
spanning-tree port mode
This command sets the Administrative Switch Port State for this port to enabled for use by
spanning tree.
Default enabled
Format spanning-tree port mode
Mode Interface Config
no spanning-tree port mode
This command sets the Administrative Switch Port State for this port to disabled, disabling
the port for use by spanning tree.
Format no spanning-tree port mode
Mode Interface Config
spanning-tree port mode all
This command sets the Administrative Switch Port State for all ports to enabled.
Default enabled
Format spanning-tree port mode all
Mode Global Config
no spanning-tree port mode all
This command sets the Administrative Switch Port State for all ports to disabled.
Format no spanning-tree port mode all
Mode Global Config
spanning-tree port-priority
Use this command to change the priority value of the port to allow the operator to select the
relative importance of the port in the forwarding process. The value range is 0–240. Set this
value to a lower number to prefer a port for forwarding of frames.
All LAN ports have 128 as priority value by default. PVSTP/PVRSTP puts the LAN port with
the lowest LAN port number in the forwarding state and blocks other LAN ports.
The application uses the port priority value when the LAN port is configured as an edge port.
Switching Commands 396

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default enabled
Format spanning-tree port-priority value
Mode Interface Config
spanning-tree tcnguard
Use this command to enable TCN guard on the interface. When enabled, TCN Guard
restricts the interface from propagating any topology change information received through
that interface.
Default Enabled
Format spanning-tree tcnguard
Mode Interface Config
no spanning-tree tcnguard
This command resets the TCN guard status of the port to the default value.
Format no spanning-tree tcnguard
Mode Interface Config
spanning-tree transmit
This command sets the Bridge Transmit Hold Count parameter.
Default 6
Format spanning-tree transmit hold-count
Mode Global Config
Parameter Description
hold-count The Bridge Tx hold-count parameter. The value in an integer between 1 and 10.
spanning-tree uplinkfast
Use this command to configure the rate at which gratuitous frames are sent (in packets per
second) after switchover to an alternate port on PVSTP configured switches and enables
uplinkfast on PVSTP switches. The range is 0-32000; the default is 150. This command has
the effect of accelerating spanning-tree convergence after switchover to an alternate port.
Uplinkfast can be configured even if the switch is configured for MST(RSTP) mode, but it only
has an effect when the switch is configured for PVST mode. Enabling FastUplink increases
Switching Commands 397

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
the priority by 3000. Path costs less than 3000 have an additional 3000 added when
uplinkfast is enabled. This reduces the probability that the switch will become the root switch.
Uplinkfast immediately changes to an alternate root port on detecting a root port failure and
changes the new root port directly to the fowarding state. A TCN is sent for this event.
After a switchover to an alternate port (new root port), uplinkfast multicasts a gratuitous frame
on the new root port on behalf of each attached machine so that the rest of the network
knows to use the secondary link to reach that machine.
PVRSTP embeds support for backbonefast and uplinkfast. There is no provision to enable or
disable these features in PVRSTP configured switches.
Default 150
Format spanning-tree uplinkfast [max-update-rate packets]
Mode Global Config
no spanning-tree uplinkfast
This command disables uplinkfast on PVSTP configured switches. All switch priorities and
path costs that have not been modified from their default values are set to their default
values.
Format no spanning-tree uplinkfast [max-update-rate]
Mode Global Config
spanning-tree vlan
Use this command to enable/disable spanning tree on a VLAN.
Default None
Format spanning-tree vlan vlan-list
Mode Global Config
Parameter Description
vlan-list The VLANs to which to apply this command.
Switching Commands 398

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
spanning-tree vlan cost
Use this command to set the path cost for a port in a VLAN. The valid path cost values are in
the range of 1 to 200000000 or auto. If auto is selected, the path cost value is set based on
the link speed.
Default None
Format spanning-tree vlan vlan-id cost {auto | value}
Mode Interface Config
spanning-tree vlan forward-time
Use this command to configure the spanning tree forward delay time for a VLAN or a set of
VLANs. The default is 15 seconds. Set this value to a lower number to accelerate the
transition to forwarding. Take into account the end-to-end BPDU propagation delay, the
maximum frame lifetime, the maximum transmission halt delay, and the message age
overestimate values specific to their network when configuring this parameter.
Default 15 seconds
Format spanning-tree vlan vlan-list forward-time seconds
Mode Global Config
Parameter Description
vlan-list The VLANs to which to apply this command.
forward-time The spanning tree forward delay time. The range is 4-30 seconds.
spanning-tree vlan hello-time
Use this command to configure the spanning tree hello time for a specified VLAN or a range
of VLANs. The default is 2 seconds. Set this value to a lower number to accelerate the
discovery of topology changes.
Default 2 seconds
Format spanning-tree vlan vlan-list hello-time seconds
Mode Global Config
Parameter Description
vlan-list The VLANs to which to apply this command.
hello-time The spanning tree forward hello time. The range is 1-10 seconds.
Switching Commands 399

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
spanning-tree vlan max-age
Use this command to configure the spanning tree maximum age time for a set of VLANs. The
default is 20 seconds.
Set this value to a lower number to accelerate the discovery of topology changes. The
network operator must take into account the end-to-end BPDU propagation delay and
message age overestimate for their specific topology when configuring this value.
The default setting of 20 seconds is suitable for a network of diameter 7, lost message value
of 3, transit delay of 1, hello interval of 2 seconds, overestimate per bridge of 1 second, and a
BPDU delay of 1 second. For a network of diameter 4, a setting of 16 seconds is appropriate
if all other timers remain at their default values.
Default 20 seconds
Format spanning-tree vlan vlan-list max-age seconds
Mode Global Config
Parameter Description
vlan-list The VLANs to which to apply this command.
max-age The spanning tree maximum age time for a set of VLANs. The range is from 6–40 seconds.
spanning-tree vlan root
Use this command to configure the switch to become the root bridge or standby root bridge
by modifying the bridge priority from the default value of 32768 to a lower value calculated to
ensure the bridge is the root (or standby) bridge.
The logic takes care of setting the bridge priority to a value lower (primary) or next lower
(secondary) than the lowest bridge priority for the specified VLAN or a range of VLANs.
Default 32768
Format spanning-tree vlan vlan-list root {primary | secondary}
Mode Global Config
Parameter Description
vlan-list The VLANs to which to apply this command.
spanning-tree vlan port-priority
Use this command to change the VLAN port priority value of the VLAN port to allow the
operator to select the relative importance of the VLAN port in the forwarding selection
process when the port is configured as a point-to-point link type. Set this value to a lower
number to prefer a port for forwarding of frames.
Switching Commands 400

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default None
Format spanning-tree vlan vlan-id port-priority priority
Mode Interface Config
Parameter Description
vlan-list The VLANs to which to apply this command.
priority The VLAN port priority. The range is 0-255.
spanning-tree vlan priority
Use this command to configure the bridge priority of a VLAN. The default value is 32768.
If the value configured is not among the specified values, it will be rounded off to the nearest
valid value.
Default 32768
Format spanning-tree vlan vlan-list priority priority
Mode Global Config
Parameter Description
vlan-list The VLANs to which to apply this command.
priority The VLAN bridge priority. Valid values are 0, 4096, 8192, 12288, 16384, 20480, 24576, 28672,
32768, 36864, 40960, 45056, 49152, 53248, 57344, and 61440.
show spanning-tree
This command displays spanning tree settings for the common and internal spanning tree.
The following details are displayed.
Format show spanning-tree
Mode Privileged EXEC
User EXEC
Term Definition
Bridge Priority Specifies the bridge priority for the Common and Internal Spanning tree (CST). The value lies
between 0 and 61440. It is displayed in multiples of 4096.
Bridge Identifier The bridge identifier for the CST. It is made up using the bridge priority and the base MAC address of
the bridge.
Time Since Time in seconds.
Topology Change
Switching Commands 401

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Topology Change Number of times changed.
Count
Topology Change Boolean value of the Topology Change parameter for the switch indicating if a topology change is in
in Progress progress on any port assigned to the common and internal spanning tree.
Designated Root The bridge identifier of the root bridge. It is made up from the bridge priority and the base MAC
address of the bridge.
Root Path Cost Value of the Root Path Cost parameter for the common and internal spanning tree.
Root Port Identifier Identifier of the port to access the Designated Root for the CST
Bridge Max Age Derived value.
Bridge Max Hops Bridge max-hops count for the device.
Root Port Bridge Derived value.
Forward Delay
Hello Time Configured value of the parameter for the CST.
Bridge Hold Time Minimum time between transmission of Configuration Bridge Protocol Data Units (BPDUs).
CST Regional Root Bridge Identifier of the CST Regional Root. It is made up using the bridge priority and the base MAC
address of the bridge.
Regional Root Path Path Cost to the CST Regional Root.
Cost
Associated FIDs List of forwarding database identifiers currently associated with this instance.
Associated VLANs List of VLAN IDs currently associated with this instance.
Command example:
(NETGEAR switch) #show spanning-tree
Bridge Priority................................ 32768
Bridge Identifier.............................. 80:00:00:10:18:48:FC:07
Time Since Topology Change..................... 8 day 3 hr 22 min 37 sec
Topology Change Count.......................... 0
Topology Change in progress.................... FALSE
Designated Root................................ 80:00:00:10:18:48:FC:07
Root Path Cost................................. 0
Root Port Identifier........................... 00:00
Bridge Max Age................................. 20
Bridge Max Hops................................ 20
Bridge Tx Hold Count........................... 6
Bridge Forwarding Delay........................ 15
Hello Time..................................... 2
Bridge Hold Time............................... 6
CST Regional Root.............................. 80:00:00:10:18:48:FC:07
Switching Commands 402
