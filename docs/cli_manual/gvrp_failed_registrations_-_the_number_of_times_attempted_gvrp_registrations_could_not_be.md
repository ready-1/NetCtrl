# gvrp_failed_registrations_-_the_number_of_times_attempted_gvrp_registrations_could_not_be

Pages: 205-212

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Protocol Statistics 802.3x Pause Frames Transmitted - A count of MAC Control frames transmitted on this interface
with an opcode indicating the PAUSE operation. This counter does not increment when the interface
is operating in half-duplex mode.
GVRP PDUs Received - The count of GVRP PDUs received in the GARP layer.
GVRP PDUs Transmitted - The count of GVRP PDUs transmitted from the GARP layer.
GVRP Failed Registrations - The number of times attempted GVRP registrations could not be
completed.
GMRP PDUs Received - The count of GMRP PDUs received in the GARP layer.
GMRP PDUs Transmitted - The count of GMRP PDUs transmitted from the GARP layer.
GMRP Failed Registrations - The number of times attempted GMRP registrations could not be
completed.
STP BPDUs Transmitted - Spanning Tree Protocol Bridge Protocol Data Units sent.
STP BPDUs Received - Spanning Tree Protocol Bridge Protocol Data Units received.
RST BPDUs Transmitted - Rapid Spanning Tree Protocol Bridge Protocol Data Units sent.
RSTP BPDUs Received - Rapid Spanning Tree Protocol Bridge Protocol Data Units received.
MSTP BPDUs Transmitted - Multiple Spanning Tree Protocol Bridge Protocol Data Units sent.
MSTP BPDUs Received - Multiple Spanning Tree Protocol Bridge Protocol Data Units received.
Dot1x Statistics EAPOL Frames Transmitted - The number of EAPOL frames of any type that have been
transmitted by this authenticator.
EAPOL Start Frames Received - The number of valid EAPOL start frames that have been received
by this authenticator.
Time Since The elapsed time, in days, hours, minutes, and seconds since the statistics for this port were last
Counters Last cleared.
Cleared
If you use the switchport keyword, the following information displays.
Term Definition
Packets Received Without The total number of packets (including broadcast packets and multicast packets) received by
Error the processor.
Broadcast Packets The total number of packets received that were directed to the broadcast address. Note that
Received this does not include multicast packets.
Packets Received With The total number of packets with errors (including broadcast packets and multicast packets)
Error received by the processor.
Packets Transmitted The total number of packets transmitted out of the interface.
without Errors
Broadcast Packets The total number of packets that higher-level protocols requested be transmitted to the
Transmitted Broadcast address, including those that were discarded or not sent.
Transmit Packet Errors The number of outbound packets that could not be transmitted because of errors.
Number of Port Link Down The number of occurrences that a port link went down.
Events
Utility Commands 205

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Link Flaps The number of link flaps per interface.
Time Since Counters Last The elapsed time, in days, hours, minutes, and seconds, since the statistics for this switch
Cleared were last cleared.
If you use the all keyword, the following information displays for all interfaces on the switch.
Term Definition
Port The Interface ID.
Bytes Tx The total number of bytes transmitted by the interface.
Bytes Rx The total number of bytes transmitted by the interface.
Packets Tx The total number of packets transmitted by the interface.
Packets Rx The total number of packets transmitted by the interface.
show interface ethernet switchport
This command displays the private VLAN mapping information for the switch interfaces.
Format show interface ethernet interface-id switchport
Mode Privileged EXEC
Parameter Description
interface-id The unit/slot/port of the switch.
The command displays the following information.
Term Definition
Private-vlan The VLAN association for the private-VLAN host ports.
host-association
Private-vlan mapping The VLAN mapping for the private-VLAN promiscuous ports.
show interface lag
Use this command to display configuration information about the specified LAG interface.
Format show interface lag lag-intf-num
Mode Privileged EXEC
Utility Commands 206

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Definition
Packets Received Without The total number of packets (including broadcast packets and multicast packets) received
Error on the LAG interface
Packets Received With The number of inbound packets that contained errors preventing them from being
Error deliverable to a higher-layer protocol.
Broadcast Packets The total number of packets received that were directed to the broadcast address. Note
Received that this does not include multicast packets.
Receive Packets Discarded The number of inbound packets which were chosen to be discarded even though no errors
had been detected to prevent their being deliverable to a higher-layer protocol. One
possible reason for discarding such a packet could be to free up buffer space.
Packets Transmitted The total number of packets transmitted out of the LAG.
Without Error
Transmit Packets Discarded The number of outbound packets which were chosen to be discarded even though no
errors had been detected to prevent their being deliverable to a higher-layer protocol. A
possible reason for discarding a packet could be to free up buffer space.
Transmit Packets Errors The number of outbound packets that could not be transmitted because of errors.
Collisions Frames The best estimate of the total number of collisions on this Ethernet segment.
Time Since Counters Last The elapsed time, in days, hours, minutes, and seconds since the statistics for this LAG
Cleared were last cleared.
show fiber-ports optics
This command displays the diagnostics information of the SFP like Temp, Voltage, Current,
Input Power, Output Power, Tx Fault, and LOS. The values are derived from the SFP’s A2
(Diagnostics) table using the I2C interface.
Format show fiber-ports optics {all | unit/slot/port}
Mode Privileged EXEC
Field Description
Temp Internally measured transceiver temperature.
Voltage Internally measured supply voltage.
Current Measured TX bias current.
Output Power Measured optical output power relative to 1mW.
Input Power Measured optical power received relative to 1mW.
TX Fault Transmitter fault.
LOS Loss of signal.
Utility Commands 207

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show fiber-ports optics all
Output Input
Port Temp Voltage Current Power Power TX LOS
[C] [Volt] [mA] [dBm] [dBm] Fault
-------- ---- ------- ------- ------- ------- ----- ---
0/49 39.3 3.256 5.0 -2.234 -2.465 No No
0/50 33.9 3.260 5.3 -2.374 -40.000 No Yes
0/51 32.2 3.256 5.6 -2.300 -2.897 No No
show fiber-ports optics-diag
This command displays the diagnostics information of the SFP in raw data.
Format show fiber-ports optics-diag {all | unit/slot/port}
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show fiber-ports optics-diag all
Port 2/0/5
diag data =
52 00 f8 00 50 00 f9 00 89 1c 79 18 88 86 79 ae R...P.....y...y.
96 64 08 ca 88 b8 0a be 31 2d 05 45 2b d4 05 ea .d......1-.E+...
3d e9 00 b6 37 2d 00 e5 00 00 00 00 00 00 00 00 =...7-..........
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
00 00 00 00 3f 80 00 00 00 00 00 00 01 00 00 00 ....?...........
01 00 00 00 01 00 00 00 01 00 00 00 00 00 00 50 ...............P
1d 7d 80 15 2c 15 16 08 00 00 00 00 00 00 02 00 .}..,...........
00 40 00 00 00 40 00 00 00 00 00 20 20 20 20 00 .@...@..... .
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
Utility Commands 208

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show fiber-ports optics-eeprom
This command displays the Electrically Erasable Programmable Read-Only Memory
(EEPROM) of the SFP.
Format show fiber-ports optics-eeprom {unit/slot/port | all}
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show fiber-ports optics-eeprom 1/0/3
Port 1/0/3
vendor_name = NETGEAR
vendor_sn = A7N2018312
date_code = 100625
vend_pn = AXM761
vend_rev = 10
eeprom data = 03 04 07 10 00 00 00 00 00 00 00 03 67 00 00 00 ............g...
08 03 00 1e 4e 45 54 47 45 41 52 20 20 20 20 20 ....NETGEAR
20 20 20 20 00 00 1f 22 41 58 4d 37 36 31 20 20 ..."AXM761
20 20 20 20 20 20 20 20 31 30 20 20 03 52 00 d2 10 .R..
00 1a 00 00 41 37 4e 32 30 31 38 33 31 32 20 20 ....A7N2018312
20 20 20 20 31 30 30 36 32 35 20 20 68 f0 03 ca 100625 h...
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
show fiber-ports optics-info
This command displays the SFP vendor related information like Vendor Name, Serial
Number of the SFP, Part Number of the SFP. The values are derived from the SFP’s A0 table
using the I2C interface.
Format show fiber-ports optics-info {all | slot/port}
Mode Privileged EXEC
Utility Commands 209

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Description
Vendor Name The vendor name is a 16 character field that contains ASCII characters, left-aligned
and padded on the right with ASCII spaces (20h). The vendor name shall be the full
name of the corporation, a commonly accepted abbreviation of the name of the
corporation, the SCSI company code for the corporation, or the stock exchange code
for the corporation.
Length (50um, OM2) This value specifies link length that is supported by the transceiver while operating in
compliance with applicable standards using 50 micron multimode OM2 [500MHz*km
at 850nm] fiber. A value of zero means that the transceiver does not support 50
micron multimode fiber or that the length information must be determined from the
transceiver technology.
Length (62.5um, OM1) This value specifies link length that is supported by the transceiver while operating in
compliance with applicable standards using 62.5 micron multimode OM1 [200
MHz*km at 850nm, 500 MHz*km at 1310nm] fiber. A value of zero means that the
transceiver does not support 62.5 micron multimode fiber or that the length
information must determined from the transceiver technology
Vendor SN The vendor serial number (vendor SN) is a 16 character field that contains ASCII
characters, left-aligned and padded on the right with ASCII spaces (20h), defining
the vendor's serial number for the transceiver. A value of all zero in the 16-byte field
indicates that the vendor SN is unspecified.
Vendor PN The vendor part number (vendor PN) is a 16-byte field that contains ASCII
characters, left aligned and added on the right with ASCII spaces (20h), defining the
vendor part number or product name. A value of all zero in the 16-byte field indicates
that the vendor PN is unspecified.
BR, nominal The nominal bit (signaling) rate (BR, nominal) is specified in units of 100 MBd,
rounded off to the nearest 100 MBd. The bit rate includes those bits necessary to
encode and delimit the signal as well as those bits carrying data information. A value
of 0 indicates that the bit rate is not specified and must be determined from the
transceiver technology. The actual information transfer rate will depend on the
encoding of the data, as defined by the encoding value.
Vendor Rev The vendor revision number (vendor rev) contains ASCII characters, left aligned and
padded on the right with ASCII spaces (20h), defining the vendor's product revision
number. A value of all zero in this field indicates that the vendor revision is
unspecified.
Command example:
(NETGEAR Switch) #show fiber-ports optics-info all
Link Link Nominal
Length Length Bit
50um 62.5um Rate
Port Vendor Name [m] [m] Serial Number Part Number [Mbps] Rev
-------- ---------------- --- ---- ---------------- ---------------- ----- ----
0/49 NETGEAR 8 3 A7N2018414 AXM761 10300 10
0 /51 N ETGEAR 8 3 A7N2018472 AXM761 10300 10
0/52 N ETGEAR 8 3 A7N2018501 AXM761 10300 10
Utility Commands 210

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show mac-addr-table
This command displays the forwarding database entries. These entries are used by the
transparent bridging function to determine how to forward a received frame.
Enter all or no parameter to display the entire table. Enter a MAC Address and VLAN ID to
display the table entry for the requested MAC address on the specified VLAN. Enter the
count parameter to view summary information about the forwarding database table. Use
the interface unit/slot/port parameter to view MAC addresses on a specific
interface.
Instead of unit/slot/port, lag lag-intf-num can be used as an alternate way to
specify the LAG interface, in whichlag-intf-num is the LAG port number. Use the vlan
vlan-id parameter to display information about MAC addresses on a specified VLAN.
Format show mac-addr-table [macaddr vlan-id | all | count | interface unit/slot/port
| vlan vlan-id]
Mode Privileged EXEC
The following information displays if you do not enter a parameter, the keyword all, or the
MAC address and VLAN ID.
Term Definition
VLAN ID The VLAN in which the MAC address is learned.
MAC Address A unicast MAC address for which the switch has forwarding and or filtering information. The format is 6
two-digit hexadecimal numbers that are separated by colons, for example 01:23:45:67:89:AB.
Interface The port through which this address was learned.
Interface Index This object indicates the ifIndex of the interface table entry associated with this port.
Status The status of this entry. The meanings of the values are:
• Static. The value of the corresponding instance was added by the system or a user when a static
MAC filter was defined. It cannot be relearned.
• Learned. The value of the corresponding instance was learned by observing the source MAC
addresses of incoming traffic, and is currently in use.
• Management. The value of the corresponding instance (system MAC address) is also the value of
an existing instance of dot1dStaticAddress. It is identified with interface 0/1. and is currently used
when enabling VLANs for routing.
• Self. The value of the corresponding instance is the address of one of the switch’s physical
interfaces (the system’s own MAC address).
• GMRP Learned. The value of the corresponding was learned via GMRP and applies to Multicast.
• Other. The value of the corresponding instance does not fall into one of the other categories.
If you enter vlan vlan-id, only the MAC Address, Interface, and Status fields appear. If
you enter the interface unit/slot/port parameter, in addition to the MAC Address
and Status fields, the VLAN ID field also appears.
Utility Commands 211

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The following information displays if you enter the count parameter.
Term Definition
Dynamic Address Number of MAC addresses in the forwarding database that were automatically learned.
count
Static Address Number of MAC addresses in the forwarding database that were manually entered by a user.
(User-defined)
count
Total MAC Number of MAC addresses currently in the forwarding database.
Addresses in use
Total MAC Number of MAC addresses the forwarding database can handle.
Addresses
available
process cpu threshold
Use this command to configure the CPU utilization thresholds. The Rising and Falling
thresholds are specified as a percentage of CPU resources. The utilization monitoring time
period can be configured from 5 seconds to 86400 seconds in multiples of 5 seconds. The
CPU utilization threshold configuration is saved across a switch reboot. Configuring the
falling utilization threshold is optional. If the falling CPU utilization parameters are not
configured, then they take the same value as the rising CPU utilization parameters.
Format process cpu threshold type total rising threshold interval seconds [falling
threshold interval seconds]
Mode Global Config
Term Description
rising threshold The percentage of CPU resources that, when exceeded for the configured rising interval, triggers a
notification. The range is 1 to 100. The default is 0 (disabled).
rising interval The duration of the CPU rising threshold violation, in seconds, that must be met to trigger a
seconds notification. The range is 5 to 86400. The default is 0 (disabled).
falling threshold The percentage of CPU resources that, when usage falls below this level for the configured interval,
triggers a notification. The range is 1 to 100. The default is 0 (disabled).
A notification is triggered when the total CPU utilization falls below this level for a configured period
of time. The falling utilization threshold notification is made only if a rising threshold notification was
previously done. The falling utilization threshold must always be equal or less than the rising
threshold value. The CLI does not allow setting the falling threshold to be greater than the rising
threshold.
falling interval The duration of the CPU falling threshold, in seconds, that must be met to trigger a notification. The
seconds range is 5 to 86400. The default is 0 (disabled).
Utility Commands 212
