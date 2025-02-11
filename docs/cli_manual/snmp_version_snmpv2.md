# snmp_version_snmpv2

Pages: 140-141

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
SNMP The community string to which this entry grants access. A valid entry is a case-sensitive alphanumeric
Community string of up to 16 characters. Each row of this table must contain a unique community name.
Name
Client IP An IP address (or portion thereof) from which this device will accept SNMP packets with the
Address associated community. The requesting entity's IP address is ANDed with the Subnet Mask before
being compared to the IP address. Note: If the Subnet Mask is set to 0.0.0.0, an IP address of 0.0.0.0
matches all IP addresses. The default value is 0.0.0.0.
Client IP Mask A mask to be ANDed with the requesting entity's IP address before comparison with IP address. If the
result matches with IP address then the address is an authenticated IP address. For example, if the IP
address = 9.47.128.0 and the corresponding Subnet Mask = 255.255.255.0 a range of incoming IP
addresses would match, i.e. the incoming IP address could equal 9.47.128.0 - 9.47.128.255. The
default value is 0.0.0.0.
Access Mode The access level for this community string.
Status The status of this community access entry.
show snmptrap
This command displays SNMP trap receivers. Trap messages are sent across a network to
an SNMP network manager. These messages alert the manager to events occurring within
the switch or on the network. Six trap receivers are simultaneously supported.
Format show snmptrap
Mode Privileged EXEC
Term Definition
SNMP Trap The community string of the SNMP trap packet sent to the trap manager. The string is case-sensitive
Name and can be up to 16 alphanumeric characters.
IP Address The IPv4 address to receive SNMP traps from this device.
IPv6 Address The IPv6 address to receive SNMP traps from this device.
SNMP Version SNMPv2
Status The receiver's status (enabled or disabled).
Command example:
(NETGEAR Switch)#show snmptrap
Community Name IpAddress IPv6 Address Snmp Version Mode
M ytrap 0 .0.0.0 2 001::1 S NMPv2 Enable show trapflags
Management Commands 140

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show trapflags
This command displays the trap conditions. The command output shows all enabled trap
flags, including OSPFv2 and OSPFv3 trap flags.
Note: You can configure which traps the switch must generate by enabling
or disabling the trap condition. If a trap condition is enabled and the
condition is detected, the SNMP agent on the switch sends the trap to
all enabled trap receivers. Cold and warm start traps are always
generated and cannot be disabled.
Format show trapflags
Mode Privileged EXEC
Term Definition
Authentication Flag Can be enabled or disabled. The factory default is enabled. Indicates whether authentication failure
traps will be sent.
Link Up/Down Flag Can be enabled or disabled. The factory default is enabled. Indicates whether link status traps will
be sent.
Multiple Users Flag Can be enabled or disabled. The factory default is enabled. Indicates whether a trap will be sent
when the same user ID is logged into the switch more than once at the same time (either through
Telnet or the serial port).
Spanning Tree Can be enabled or disabled. The factory default is enabled. Indicates whether spanning tree traps
Flag are sent.
ACL Traps May be enabled or disabled. The factory default is disabled. Indicates whether ACL traps are sent.
DVMRP Traps Can be enabled or disabled. The factory default is disabled. Indicates whether DVMRP traps are
sent.
OSPFv2 Traps Can be enabled or disabled. The factory default is disabled. Indicates whether OSPF traps are sent.
If any of the OSPF trap flags are not enabled, then the command displays disabled. Otherwise, the
command shows all the enabled OSPF traps’ information.
OSPFv3 Traps Can be enabled or disabled. The factory default is disabled. Indicates whether OSPF traps are sent.
If any of the OSPFv3 trap flags are not enabled, then the command displays disabled. Otherwise,
the command shows all the enabled OSPFv3 traps’ information.
PIM Traps Can be enabled or disabled. The factory default is disabled. Indicates whether PIM traps are sent.
Management Commands 141
