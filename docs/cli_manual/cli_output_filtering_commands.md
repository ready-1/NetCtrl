# cli_output_filtering_commands

Pages: 192-204

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
CLI Output Filtering Commands
show “command” | include “string”
The command show command (that is, you must enter a keyword of an existing show
command for the command parameter) is executed and the output is filtered to display only
lines containing the string match. All other non-matching lines in the output are
suppressed.
Command example:
(NETGEAR Switch) #show running-config | include “spanning-tree”
spanning-tree configuration name "00-02-BC-42-F9-33"
spanning-tree bpduguard
spanning-tree bpdufilter default
show “command” | include “string” exclude “string2”
The command show command (that is, you must enter a keyword of an existing show
command for the command parameter) is executed and the output is filtered to only show
lines containing the string match and not containing the string2 match. All other
non-matching lines in the output are suppressed. If a line of output contains both the include
and exclude strings then the line is not displayed.
Command example:
(NETGEAR Switch) #show running-config | include “spanning-tree” exclude “configuration”
spanning-tree bpduguard
spanning-tree bpdufilter default
show “command” | exclude “string”
The command show command (that is, you must enter a keyword of an existing show
command for the command parameter) is executed and the output is filtered to show all lines
not containing the string match. Output lines containing the string match are
suppressed.
Command example:
(NETGEAR Switch) #show interface 0/1
Packets Received Without Error................. 0
Packets Received With Error.................... 0
Broadcast Packets Received..................... 0
Receive Packets Discarded...................... 0
Packets Transmitted Without Errors............. 0
Utility Commands 192

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Transmit Packets Discarded..................... 0
Transmit Packet Errors......................... 0
Collision Frames............................... 0
Time Since Counters Last Cleared............... 281 day 4 hr 9 min 0 sec
Command example:
(NETGEAR Switch) #show interface 0/1 | exclude “Packets”
Transmit Packet Errors......................... 0
Collision Frames............................... 0
Time Since Counters Last Cleared............... 20 day 21 hr 30 min 9 sec
show “command” | begin “string”
The command show command (that is, you must enter a keyword of an existing show
command for the command parameter) is executed and the output is filtered to show all lines
beginning with and following the first line containing the string match. All prior lines are
suppressed.
Command example:
(NETGEAR Switch) #show port all | begin “1/1”
1/1 Enable Down Disable N/A N/A
1/2 Enable Down Disable N/A N/A
1/3 Enable Down Disable N/A N/A
1/4 Enable Down Disable N/A N/A
1/5 Enable Down Disable N/A N/A
1/6 Enable Down Disable N/A N/A
show “command” | section “string”
The command show command (that is, you must enter a keyword of an existing show
command for the command parameter) is executed and the output is filtered to show only
lines included within the section(s) identified by lines containing the string match and
ending with the first line containing the default end-of-section identifier (that is, exit).
Command example:
(NETGEAR Switch) #show running-config | section “interface 0/1”
interface 0/1
no spanning-tree port mode
exit
Utility Commands 193

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show “command” | section “string” “string2”
The command show command (that is, you must enter a keyword of an existing show
command for the command parameter) is executed and the output is filtered to only show
lines included within the section(s) identified by lines containing the string match and
ending with the first line containing the string2 match. If multiple sessions matching the
specified string match criteria are part of the base output, then all instances are displayed.
show “command” | section “string” include “string2”
The command show command (that is, you must enter a keyword of an existing show
command for the command parameter) is executed and the output is filtered to only show
lines included within the section(s) identified by lines containing the string match and
ending with the first line containing the default end-of-section identifier (that is, exit) and
that include the string2 match. This type of filter command could also include “exclude” or
user-defined end-of-section identifier parameters as well.
Dual Image Commands
The switch supports a dual image feature that allows the switch to have two software images
in the permanent storage. You can specify which image is the active image to be loaded in
subsequent reboots. This feature allows reduced down-time when you upgrade or
downgrade the software.
delete
This command deletes the image1 or image 2 file from the permanent storage. The optional
unit parameter is valid only for members. The unit parameter identifies the member on
which you must execute this command. When you do not enter this parameter, the command
is executed on all members in the stack.
Format delete [unit] {image1 | image2}
Mode Privileged EXEC
boot system
This command activates the specified image. It will be the active-image for subsequent
reboots and will be loaded by the boot loader. The current active-image is marked as the
backup-image for subsequent reboots. If the specified image doesn't exist on the system, this
command returns an error message. The optional unit parameter identifies the member on
which you must execute this command. When you do not enter this parameter, the command
is executed on all members in the stack.
Format boot system [unit] {image1 | image2}
Mode Privileged EXEC
Utility Commands 194

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show bootvar
This command displays the version information and the activation status for the current
images on the supplied unit of the stack. If you do not specify a unit number, the command
displays image details for all nodes in the stack. The command also displays any text
description associated with an image. This command, when used on a standalone system,
displays the switch activation status. For a standalone system, the unit parameter is not valid.
Format show bootvar [unit]
Mode Privileged EXEC
filedescr
This command associates a given text description with an image and replaces any existing
description. The command is executed on all units in a stack.
Format filedescr {image1 | image2} text-description
Mode Privileged EXEC
update bootcode
This command updates the bootcode (boot loader) on the switch. The bootcode is read from
the active image for subsequent reboots. The unit parameter identifies the member on
which this command must be executed. When this parameter is not supplied, the command
is executed on all units in a stack.
Format update bootcode [unit]
Mode Privileged EXEC
System Information and Statistics
Commands
This section describes the commands you use to view information about system features,
components, and configurations.
show arp switch (system information and statistics commands)
This command displays the contents of the Address Resolution Protocol (ARP) table that is
associated with the IP address of the switch. This IP address learns only ARP entries that are
associated with the management interfaces (network or service ports). ARP entries that are
associated with routing interfaces are not listed.
Utility Commands 195

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format show arp switch
Mode Privileged EXEC
Term Definition
IP Address IP address of the management interface or another device on the management network.
MAC Address Hardware MAC address of that device.
Interface For a service port the output is Management. For a network port, the output is the
unit/slot/port of the physical interface.
show eventlog
This command displays the event log, which contains error messages from the system. The
event log is not cleared on a system reset. The unit is the switch identifier.
Format show eventlog [unit]
Mode Privileged EXEC
Term Definition
File The file in which the event originated.
Line The line number of the event.
Task Id The task ID of the event.
Code The event code.
Time The time this event occurred.
Unit The unit for the event.
Note: Event log information is retained across a switch reset.
show hardware
This command displays inventory information for the switch.
Note: The show version command and the show hardware command
display the same information. In future releases of the software, the
show hardware command will not be available. For a description of
the command output, see the command show version on page197.
Utility Commands 196

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format show hardware
Mode Privileged EXEC
show environment
This command displays information about the temperature and status of the power supplies
and fans in the system chassis.
Format show environment
Mode Privileged EXEC
Command example:
(Netgear Switch) #show environment
Temp (C)....................................... 30
Temperature traps range: 0 to 90 degrees (Celsius)
Temperature Sensors:
Unit Sensor Description Temp (C) State Max_Temp (C)
---- ------ ---------------- ---------- -------------- --------------
1 1 System 30 Normal 31
Fans:
Unit Fan Description Type Speed Duty level State
---- --- -------------- --------- ------------- ------------- --------------
1 1 System1 Fixed 9200 39 Operational
1 2 System2 Fixed 9200 39 Operational
1 3 Power1 Fixed 9200 39 Operational
1 4 Power2 Fixed 8300 39 Operational
Power supplies:
Unit Power supply Description Type State
---- ------------ ---------------- ---------- --------------
1 1 AC-1 Removable Operational
1 2 AC-2 Removable Not present
show version
This command displays inventory information for the switch.
Note: The show version command replaces the show hardware
command in future releases of the software.
Utility Commands 197

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format show version
Mode Privileged EXEC
Term Definition
System Description Text used to identify the product name of this switch.
Machine Model The machine model as defined by the Vital Product Data
Serial Number The unique serial number for this switch.
Burned in MAC The universally assigned network address.
Address
Software Version The release version number of the code running on the switch.
Boot Code Version The version of the boot code software running on the switch.
CPLD Version The version of the CPLD firmware running on the switch.
Supported Java Plugin The software version of the Java plugin running on the switch.
Version
Current Time The current time on the running on the switch.
show platform vpd
This command displays vital product data for the switch.
Format show platform vpd
Mode User Privileged
The following information is displayed.
Term Definition
Operational Code Build Signature loaded into the switch
Image File Name
Software Version Release Version Maintenance Level and Build (RVMB) information of the switch.
Timestamp Timestamp at which the image is built
Command example:
(NETGEAR Switch) #show platform vpd
Operational Code Image File Name...............
NETGEAR-Ent-esw-xgs4-gto-BL20R-CS-6AIQHSr3v7m14b35
Software Version............................... 3.7.14.35
Timestamp...................................... Thu Mar 7 14:36:14 IST 2013
Utility Commands 198

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show interface
This command displays a summary of statistics for a specific interface or a count of all CPU
traffic based upon the argument.
Format show interface {unit/slot/port | switchport}
Mode Privileged EXEC
The display parameters, when the argument is unit/slot/port, are as follows.
Field Definition
Packets Received The total number of packets (including broadcast packets and multicast packets) received by the
Without Error processor.
Packets Received The number of inbound packets that contained errors preventing them from being deliverable to a
With Error higher-layer protocol.
Broadcast Packets The total number of packets received that were directed to the broadcast address. Note that this
Received does not include multicast packets.
Receive Packets The number of inbound packets which were chosen to be discarded even though no errors had been
Discarded detected to prevent their being deliverable to a higher-layer protocol. One possible reason for
discarding such a packet could be to free up buffered space.
Packets The total number of packets transmitted out of the interface.
Transmitted
Without Error
Transmit Packets The number of outbound packets which were chosen to be discarded even though no errors had
Discarded been detected to prevent their being deliverable to a higher-layer protocol. A possible reason for
discarding a packet could be to free up buffer space.
Transmit Packets The number of outbound packets that could not be transmitted because of errors.
Errors
Collisions Frames The best estimate of the total number of collisions on this Ethernet segment.
Number of link The number of down events for the link since the switch restarted.
down events
Load Interval The period in seconds for which data is used to compute the load statistics. You must enter a that is
a multiple of 30. The allowable range is from 30 to 600 seconds.
Received Rate The approximate number of bits per second received. This value is an exponentially-weighted
(Mbps) average and is affected by the configured load interval.
Transmitted Rate The approximate number of bits per second transmitted. This value is an exponentially-weighted
(Mbps) average and is affected by the configured load interval.
Received Error The approximate number of error bits per second received. This value is an exponentially-weighted
Rate average and is affected by the configured load interval.
Transmitted Error The approximate number of error bits per second transmitted. This value is an
Rate exponentially-weighted average and is affected by the configured load interval.
Utility Commands 199

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Definition
Packets Per The approximate number of packets per second received. This value is an exponentially-weighted
Second Received average and is affected by the configured load interval.
Packets Per The approximate number of packets per second transmitted. This value is an exponentially-weighted
Second average and is affected by the configured load interval.
Transmitted
Link Flaps The number of up and down events for the link since the switch restarted.
Time Since The elapsed time, in days, hours, minutes, and seconds since the statistics for this port were last
Counters Last cleared.
Cleared
The display parameters, when the argument is switchport are as follows.
Term Definition
Packets Received Without Error The total number of packets (including broadcast packets and multicast packets)
received by the processor.
Broadcast Packets Received The total number of packets received that were directed to the broadcast address.
Note that this does not include multicast packets.
Packets Received With Error The number of inbound packets that contained errors preventing them from being
deliverable to a higher-layer protocol.
Packets Transmitted Without Error The total number of packets transmitted out of the interface.
Broadcast Packets Transmitted The total number of packets that higher-level protocols requested to be transmitted to
the Broadcast address, including those that were discarded or not sent.
Transmit Packet Errors The number of outbound packets that could not be transmitted because of errors.
Time Since Counters Last Cleared The elapsed time, in days, hours, minutes, and seconds since the statistics for this
switch were last cleared.
show interfaces status
Use this command to display interface information, including the description, port state,
speed and autonegotiation capabilities. The command is similar to show port all but
displays additional fields like interface description and port-capability.
The description of the interface is configurable through the existing command description
name which has a maximum length of 64 characters that is truncated to 28 characters in the
output. The long form of the description can be displayed using show port description.
The interfaces displayed by this command are physical interfaces, LAG interfaces and VLAN
routing interfaces.
Format show interfaces status [unit/slot/port]
Mode Privileged EXEC
Utility Commands 200

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Description
Port The interface that is associated with the displayed information.
Name The descriptive user-configured name for the interface.
Link State Indicates whether the link is up or down.
Physical Mode The speed and duplex settings on the interface.
Physical Status Indicates the port speed and duplex mode for physical interfaces. The physical
status for LAGs is not reported. When a port is down, the physical status is unknown.
Media Type The media type of the interface.
Flow Control Status The 802.3x flow control status.
Flow Control The configured 802.3x flow control mode.
show interface ethernet
This command displays detailed statistics for a specific interface or for all CPU traffic based
upon the argument.
Format show interface ethernet {unit/slot/port | switchport | all}
Mode Privileged EXEC
When you specify a value for unit/slot/port, the command displays the following
information.
Term Definition
Packets Received Total Packets Received (Octets) - The total number of octets of data (including those in bad
packets) received on the network (excluding framing bits but including Frame Check Sequence
(FCS) octets). This object can be used as a reasonable estimate of Ethernet utilization. If greater
precision is desired, the etherStatsPkts and etherStatsOctets objects should be sampled before and
after a common interval. The result of this equation is the value Utilization which is the percent
utilization of the Ethernet segment on a scale of 0 to 100 percent.
Packets Received 64 Octets - The total number of packets (including bad packets) received that
were 64 octets in length (excluding framing bits but including FCS octets).
Packets Received 65–127 Octets - The total number of packets (including bad packets) received
that were between 65 and 127 octets in length inclusive (excluding framing bits but including FCS
octets).
Packets Received 128–255 Octets - The total number of packets (including bad packets) received
that were between 128 and 255 octets in length inclusive (excluding framing bits but including FCS
octets).
Packets Received 256–511 Octets - The total number of packets (including bad packets) received
that were between 256 and 511 octets in length inclusive (excluding framing bits but including FCS
octets).
Packets Received 512–1023 Octets - The total number of packets (including bad packets)
received that were between 512 and 1023 octets in length inclusive (excluding framing bits but
including FCS octets).
Utility Commands 201

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Packets Received Packets Received 1024–1518 Octets - The total number of packets (including bad packets)
(continued) received that were between 1024 and 1518 octets in length inclusive (excluding framing bits but
including FCS octets).
Packets Received > 1518 Octets - The total number of packets received that were longer than
1522 octets (excluding framing bits, but including FCS octets) and were otherwise well formed.
Packets RX and TX 64 Octets - The total number of packets (including bad packets) received and
transmitted that were 64 octets in length (excluding framing bits but including FCS octets).
Packets RX and TX 65–127 Octets - The total number of packets (including bad packets) received
and transmitted that were between 65 and 127 octets in length inclusive (excluding framing bits but
including FCS octets).
Packets RX and TX 128–255 Octets - The total number of packets (including bad packets)
received and transmitted that were between 128 and 255 octets in length inclusive (excluding
framing bits but including FCS octets).
Packets RX and TX 256–511 Octets - The total number of packets (including bad packets) received
and transmitted that were between 256 and 511 octets in length inclusive (excluding framing bits but
including FCS octets).
Packets RX and TX 512–1023 Octets - The total number of packets (including bad packets)
received and transmitted that were between 512 and 1023 octets in length inclusive (excluding
framing bits but including FCS octets).
Packets RX and TX 1024–1518 Octets - The total number of packets (including bad packets)
received and transmitted that were between 1024 and 1518 octets in length inclusive (excluding
framing bits but including FCS octets).
Packets RX and TX 1519–2047 Octets - The total number of packets received and transmitted that
were between 1519 and 2047 octets in length inclusive (excluding framing bits, but including FCS
octets) and were otherwise well formed.
Packets RX and TX 1523–2047 Octets - The total number of packets received and transmitted that
were between 1523 and 2047 octets in length inclusive (excluding framing bits, but including FCS
octets) and were otherwise well formed.
Packets RX and TX 2048–4095 Octets - The total number of packets received that were between
2048 and 4095 octets in length inclusive (excluding framing bits, but including FCS octets) and were
otherwise well formed.
Packets RX and TX 4096–9216 Octets - The total number of packets received that were between
4096 and 9216 octets in length inclusive (excluding framing bits, but including FCS octets) and were
otherwise well formed.
Packets Received Total Packets Received Without Error - The total number of packets received that were without
Successfully errors.
Unicast Packets Received - The number of subnetwork-unicast packets delivered to a higher-layer
protocol.
Multicast Packets Received - The total number of good packets received that were directed to a
multicast address. Note that this number does not include packets directed to the broadcast
address.
Broadcast Packets Received - The total number of good packets received that were directed to the
broadcast address. Note that this does not include multicast packets.
Receive Packets The number of inbound packets which were chosen to be discarded even though no errors had been
Discarded detected to prevent their being deliverable to a higher-layer protocol. One possible reason for
discarding such a packet could be to free up buffer space.
Utility Commands 202

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Packets Received Total Packets Received with MAC Errors - The total number of inbound packets that contained
with MAC Errors errors preventing them from being deliverable to a higher-layer protocol.
Jabbers Received - The total number of packets received that were longer than 1518 octets
(excluding framing bits, but including FCS octets), and had either a bad Frame Check Sequence
(FCS) with an integral number of octets (FCS Error) or a bad FCS with a non-integral number of
octets (Alignment Error). Note that this definition of jabber is different than the definition in
IEEE-802.3 section 8.2.1.5 (10BASE5) and section 10.3.1.4 (10BASE2). These documents define
jabber as the condition where any packet exceeds 20 ms. The allowed range to detect jabber is
between 20 ms and 150 ms.
Fragments/Undersize Received - The total number of packets received that were less than 64
octets in length (excluding framing bits but including FCS octets).
Alignment Errors - The total number of packets received that had a length (excluding framing bits,
but including FCS octets) of between 64 and 1518 octets, inclusive, but had a bad Frame Check
Sequence (FCS) with a non-integral number of octets.
FCS Errors - The total number of packets received that had a length (excluding framing bits, but
including FCS octets) of between 64 and 1518 octets, inclusive, but had a bad Frame Check
Sequence (FCS) with an integral number of octets.
Overruns - The total number of frames discarded as this port was overloaded with incoming
packets, and could not keep up with the inflow.
Received Packets Total Received Packets Not Forwarded - A count of valid frames received which were discarded
Not Forwarded (in other words, filtered) by the forwarding process
802.3x Pause Frames Received - A count of MAC Control frames received on this interface with an
opcode indicating the PAUSE operation. This counter does not increment when the interface is
operating in half-duplex mode.
Unacceptable Frame Type - The number of frames discarded from this port due to being an
unacceptable frame type.
Packets Total Packets Transmitted (Octets) - The total number of octets of data (including those in bad
Transmitted Octets packets) received on the network (excluding framing bits but including FCS octets). This object can
be used as a reasonable estimate of Ethernet utilization. If greater precision is desired, the
etherStatsPkts and etherStatsOctets objects should be sampled before and after a common interval.
-----
Packets Transmitted 64 Octets - The total number of packets (including bad packets) received that
were 64 octets in length (excluding framing bits but including FCS octets).
Packets Transmitted 65-127 Octets - The total number of packets (including bad packets)
received that were between 65 and 127 octets in length inclusive (excluding framing bits but
including FCS octets).
Packets Transmitted 128-255 Octets - The total number of packets (including bad packets)
received that were between 128 and 255 octets in length inclusive (excluding framing bits but
including FCS octets).
Packets Transmitted 256-511 Octets - The total number of packets (including bad packets)
received that were between 256 and 511 octets in length inclusive (excluding framing bits but
including FCS octets).
Packets Transmitted 512-1023 Octets - The total number of packets (including bad packets)
received that were between 512 and 1023 octets in length inclusive (excluding framing bits but
including FCS octets).
Utility Commands 203

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Packets Packets Transmitted 1024-1518 Octets - The total number of packets (including bad packets)
Transmitted Octets received that were between 1024 and 1518 octets in length inclusive (excluding framing bits but
(continued) including FCS octets).
Packets Transmitted > 1518 Octets - The total number of packets transmitted that were longer
than 1518 octets (excluding framing bits, but including FCS octets) and were otherwise well formed.
Max Frame Size - The maximum size of the Info (non-MAC) field that this port will receive or
transmit.
Packets Total Packets Transmitted Successfully- The number of frames that have been transmitted by
Transmitted this port to its segment.
Successfully Unicast Packets Transmitted - The total number of packets that higher-level protocols requested
be transmitted to a subnetwork-unicast address, including those that were discarded or not sent.
Multicast Packets Transmitted - The total number of packets that higher-level protocols requested
be transmitted to a Multicast address, including those that were discarded or not sent.
Broadcast Packets Transmitted - The total number of packets that higher-level protocols
requested be transmitted to the Broadcast address, including those that were discarded or not sent.
Transmit Packets The number of outbound packets which were chosen to be discarded even though no errors had
Discarded been detected to prevent their being deliverable to a higher-layer protocol. A possible reason for
discarding a packet could be to free up buffer space.
Transmit Errors Total Transmit Errors - The sum of Single, Multiple, and Excessive Collisions.
FCS Errors - The total number of packets transmitted that had a length (excluding framing bits, but
including FCS octets) of between 64 and 1518 octets, inclusive, but had a bad Frame Check
Sequence (FCS) with an integral number of octets.
Underrun Errors - The total number of frames discarded because the transmit FIFO buffer became
empty during frame transmission.
Transmit Discards Total Transmit Packets Discards - The sum of single collision frames discarded, multiple collision
frames discarded, and excessive frames discarded.
Single Collision Frames - A count of the number of successfully transmitted frames on a particular
interface for which transmission is inhibited by exactly one collision.
Multiple Collision Frames - A count of the number of successfully transmitted frames on a
particular interface for which transmission is inhibited by more than one collision.
Excessive Collisions - A count of frames for which transmission on a particular interface fails due
to excessive collisions.
Port Membership Discards - The number of frames discarded on egress for this port due to egress
filtering being enabled.
Utility Commands 204
