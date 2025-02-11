# isdp_commands_this_section_describes_the_commands_you_use_to_configure_the_industry_standa_a167856f

Pages: 639-644

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ISDP Commands
This section describes the commands you use to configure the industry standard Discovery
Protocol (ISDP).
isdp run
This command enables ISDP on the switch.
Default Enabled
Format isdp run
Mode Global Config
no isdp run
This command disables ISDP on the switch.
Format no isdp run
Mode Global Config
isdp holdtime
This command configures the hold time for ISDP packets that the switch transmits. The hold
time specifies how long a receiving device should store information sent in the ISDP packet
before discarding it. The period is in the range 10–255 seconds.
Default 180 seconds
Format isdp holdtime seconds
Mode Global Config
isdp timer
This command sets the period of time between sending new ISDP packets. The period is in
the range 5–254 seconds.
Default 60 seconds
Format isdp timer seconds
Mode Global Config
Switching Commands 639

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
isdp advertise-v2
This command enables the sending of ISDP version 2 packets from the device.
Default Enabled
Format isdp advertise-v2
Mode Global Config
no isdp advertise-v2
This command disables the sending of ISDP version 2 packets from the device.
Format no isdp advertise-v2
Mode Global Config
isdp enable
This command enables ISDP on an interface or range of interfaces.
Note: ISDP must be enabled both globally and on the interface in order for
the interface to transmit ISDP packets. If ISDP is globally disabled on
the switch, the interface will not transmit ISDP packets, regardless of
the ISDP status on the interface. To enable ISDP globally, use the
command isdp run on page639.
Default Enabled
Format isdp enable
Mode Interface Config
no isdp enable
This command disables ISDP on the interface.
Format no isdp enable
Mode Interface Config
clear isdp counters
This command clears ISDP counters.
Format clear isdp counters
Mode Privileged EXEC
Switching Commands 640

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
clear isdp table
This command clears entries in the ISDP table.
Format clear isdp table
Mode Privileged EXEC
show isdp
This command displays global ISDP settings.
Format show isdp
Mode Privileged EXEC
Term Definition
Timer The frequency with which this device sends ISDP packets. This value is given in seconds.
Hold Time The length of time the receiving device should save information sent by this device. This value is
given in seconds.
Version 2 The setting for sending ISDPv2 packets. If disabled, version 1 packets are transmitted.
Advertisements
Neighbors table The amount of time that has passed since the ISPD neighbor table changed.
time since last
change
Device ID The Device ID advertised by this device. The format of this Device ID is characterized by the value of
the Device ID Format object.
Device ID Format Indicates the Device ID format capability of the device.
Capability • serialNumber indicates that the device uses a serial number as the format for its Device ID.
• macAddress indicates that the device uses a Layer 2 MAC address as the format for its Device
ID.
• other indicates that the device uses its platform-specific format as the format for its Device ID.
Device ID Format Indicates the Device ID format of the device.
• serialNumber indicates that the value is in the form of an ASCII string containing the device
serial number.
• macAddress indicates that the value is in the form of a Layer 2 MAC address.
• other indicates that the value is in the form of a platform specific ASCII string containing info
that identifies the device. For example, ASCII string contains serialNumber
appended/prepended with system name.
Command example:
(NETGEAR Switch) #show isdp
Timer.......................................... 30
Hold Time...................................... 180
Version 2 Advertisements....................... Enabled
Switching Commands 641

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Neighbors table time since last change......... 0 days 00:00:00
Device ID...................................... 1114728
Device ID format capability.................... Serial Number, Host Name
Device ID format............................... Serial Number
show isdp interface
This command displays ISDP settings for the specified interface.
Format show isdp interface {all | unit/slot/port}
Mode Privileged EXEC
Term Definition
Interface The unit/slot/port of the specified interface.
Mode ISDP mode enabled/disabled status for the interface(s).
Command example:
(NETGEAR Switch) #show isdp interface 0/1
Interface Mode
--------------- ----------
0/1 Enabled
Command example:
(NETGEAR Switch) #show isdp interface all
I nterface Mode
- -------------- ----------
0/1 Enabled
0/2 Enabled
0/3 Enabled
0/4 Enabled
0/5 Enabled
0/6 Enabled
0/7 Enabled
0/8 Enabled
Switching Commands 642

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show isdp entry
This command displays ISDP entries. If the device-id is specified, then only entries for
that device are shown.
Format show isdp entry {all | device-id}
Mode Privileged EXEC
Term Definition
Device ID The device ID associated with the neighbor which advertised the information.
IP Addresses The IP address(es) associated with the neighbor.
Capability ISDP Functional Capabilities advertised by the neighbor.
Platform The hardware platform advertised by the neighbor.
Interface The interface (unit/slot/port) on which the neighbor's advertisement was received.
Port ID The port ID of the interface from which the neighbor sent the advertisement.
Hold Time The hold time advertised by the neighbor.
Version The software version that the neighbor is running.
Advertisement The version of the advertisement packet received from the neighbor.
Version
Entry Last The time when the entry was last changed.
Changed Time
Command example:
(NETGEAR Switch) #show isdp entry Switch
D evice ID Switch
Address(es):
IP Address: 172.20.1.18
I P Address: 172.20.1.18
C apability Router IGMP
P latform Netgear XCM8900
I nterface 0/1
P ort ID GigabitEthernet1/1
Holdtime 64
A dvertisement Version 2
E ntry last changed time 0 days 00:13:50
Switching Commands 643

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show isdp neighbors
This command displays the list of neighboring devices.
Format show isdp neighbors [unit/slot/port | detail]
Mode Privileged EXEC
Term Definition
Device ID The device ID associated with the neighbor which advertised the information.
IP Addresses The IP addresses associated with the neighbor.
Capability ISDP functional capabilities advertised by the neighbor.
Platform The hardware platform advertised by the neighbor.
Interface The interface (unit/slot/port) on which the neighbor's advertisement was received.
Port ID The port ID of the interface from which the neighbor sent the advertisement.
Hold Time The hold time advertised by the neighbor.
Advertisement The version of the advertisement packet received from the neighbor.
Version
Entry Last Time when the entry was last modified.
Changed Time
Version The software version that the neighbor is running.
Command example:
(NETGEAR Switch) #show isdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge,
S - Switch, H - Host, I - IGMP, r - Repeater
D evice ID Intf H oldtime C apability Platform Port ID
- --------------- - ---- - -------- ----------- - ------------- -------------------
S witch 0/1 165 R I c isco WS-C4948 GigabitEthernet1/1
Command example:
(NETGEAR Switch) #show isdp neighbors detail
D evice ID 0001f45f1bc0
Address(es):
I P Address: 10.27.7.57
C apability Router Trans Bridge Switch IGMP
P latform SecureChassis C2
I nterface 0/48
P ort ID ge.3.14
Switching Commands 644
