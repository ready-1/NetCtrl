# ip_address_ip_port_connection_mode_role_------------_-------_---------------_----

Pages: 174-180

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
IP Address The IPv4 address of the controller.
IP Port The IPv4 port number on the switch for the controller connection.
Connection Mode The SSL or TCP Controller Connection mode.
Role The role of the controller: Master, Equal, or Slave
Command example:
(NETGEAR Switch) #show openflow configured controller
IP Address IP Port Connection Mode Role
------------ ------- --------------- ----
172.21.4.217 6633 SSL Master
show openflow installed flows
This command displays the list of configured flows on the switch.
Format show openflow installed flows [dest_ip ip-address | dest_ip_port 1–65535 |
dest_mac macaddr | dscp 0–63 | ether_type 0–0xFFFF | ingress_port slot/port |
ip_proto 0–255 | priority 1–65535 | source_ip ip-address | source_ip_port
1–65535 | source_mac macaddr | table {4 | 24 | 25 | 60} | vlan 1–4093 |
vlan_prio 0–7]
Mode Privileged Exec
Paramater Definition
dest_ip The IP address of the destination.
dest_ip_port The port number of the destination in the range 1–65535.
dest_mac The MAC address of the destination.
dscp The DSCP value in the range 0–63.
ether_type The EtherType value in the range 0–0xFFFF.
ingress_port The slot and port for the incoming traffic.
ip_proto The IP protocol in the range 0–255.
priority The priority of the flow. This is a value in the range 1–65535.
source_ip The IP address of the source.
source_ip_port The port number of the source in the range 1–65535.
source_mac The MAC address of the source.
table The table number, which can be 4, 24, 25, or 60.
Management Commands 174

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Paramater Definition
vlan The VLAN in the range 1–4093.
vlan_prio The VLAN priority in the range 0–7.
The following table describes the terms in the command output.
Term Definition
Flow Type The type of flow. For example, 1.0 or Layer 2 match.
Flow Table The hardware table in which the flow is installed.
Flow Priority The priority of the flow in relation to other flows.
Match Criteria The match criteria that are specified by the flow.
Ingress Port The port on which the flow is active.
Action The action that is specified by the flow.
Idle The time since the flow was active.
Installed in hardware Whether the flow is installed in the hardware.
Command example:
(NETGEAR Switch) #show openflow installed flows
Flow 00000000 type "1DOT0"
Match criteria:
Flow table 24 : Priority 1
Ingress port 0/0
Actions:
Action: Drop
Status:
Duration 2 : Idle 0 : installed in hardware 1
Flow 00000000 type "1DOT0"
Match criteria:
Flow table 24 : Priority 102
Ingress port 0/0 : Ether type 88CC
Actions:Status:
Duration 5 5 : Idle 4 5 : installed in hardware 1
Command example:
(NETGEAR Switch) # show openflow installed flows
Flow 000000E1 type "1DOT3"
Management Commands 175

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Match criteria:
Flow table 60 : Priority 10
Ingress port 0/1 : Src MAC 00:00:02:37:38:01 : Dst MAC 00:00:18:37:22:01
VLAN 1 : VLAN prio 1 : Ether type 0x0800
IP proto 17 : Src IP 100.0.0.225 : Dst IP 192.0.0.225
Src IP port 1 : Dst IP port 1 : TOS 32(DSCP: 8)
Actions:
New Src IP 3.3.3.3 : New SrcIP Mask 255.255.255.255 : New Dst IP 4.4.4.4
New DstIP Mask 255.255.255.255 : Egress port 0/1
Status:
Duration 5 : Idle 2 : installed in hardware 1
Flow 000001F9 type "1DOT3"
Match criteria:
Flow table 60 : Priority 10
Ingress port 0/1 : Src MAC 00:00:1A:38:38:01 : Dst MAC 00:00:30:38:22:01
VLAN 1 : VLAN prio 1 : Ether type 0x0800
IP proto 17 : Src IP 100.0.1.249 : Dst IP 192.0.1.249
Src IP port 1 : Dst IP port 1 : TOS 32(DSCP: 8)
Actions:
Egress port 0/1
Status:
Duration 2 : Idle 0 : installed in hardware 1
show openflow installed groups
This command displays the list of configured groups on the switch.
Format show openflow installed groups
Mode Privileged Exec
Term Definition
Group Type The type of group. For example, “Indirect,” “All,” “Select,” or another type of group.
Group Id The unique identifier of the group.
Reference Count The Group Reference Count is used only for “Indirect” groups. This count indicates how many
“Select” groups are referring to the current “Indirect” group.
Duration The time since the group was created.
Management Commands 176

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Bucket Count The number of buckets in the group.
Reference Group Id The “Indirect” group ID that is associated with the “Select” group.
Command example:
(NETGEAR Switch) # show openflow installed groups
Max Indirect Group Entries......................................... 1234
Current Indirect Group Entries in database......................... 123
Max All Group Entries.............................................. 1234
Current All Group Entries in database.............................. 123
Max Select Group Entries........................................... 1234
Current Select Group Entries in database........................... 123
Group Id 12345678 type "Indirect"
=================================
Ref Count 1 : Duration 8 : Bucket Count 1
Bucket Entry List:
------------------
Bucket Index 25 : Output Port 1
Src MAC 00:00:00:00:00:AB : Dst MAC 00:00:00:00:00:CD
VLAN 101 : Reference Group Id NA
Group Id 23456789 type "All"
============================
Ref Count NA : Duration 10 : Bucket Count 2
Bucket Entry List:
------------------
Bucket Index 26 : Output Port 2
Src MAC NA : Dst MAC NA
VLAN 102 : Reference Group Id NA
Bucket Index 27 : Output Port 3
Src MAC NA : Dst MAC NA
VLAN 103 : Reference Group Id NA
Group Id 34567890 type "Select"
===============================
Ref Count NA : Duration 10 : Bucket Count 3
Management Commands 177

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Bucket Entry List:
------------------
Bucket Index 28 : Output Port NA
Src MAC NA : Dst MAC NA
VLAN NA : Reference Group Id 12345678
Bucket Index 29 : Output Port NA
Src MAC NA : Dst MAC NA
VLAN NA : Reference Group Id 12345678
Bucket Index 30 : Output Port NA
Src MAC NA : Dst MAC NA
VLAN NA : Reference Group Id 12345678
show openflow table-status
This command displays the supported OpenFlow tables and reports usage information for
the tables.
Format show openflow table-status {openflow10 | openflow13}
Mode Privileged Exec
Term Definition
Flow Table The OpenFlow table identifier. The range is 0–255.
Flow Table Name The name of the table.
Flow Table Description The description of the table.
Maximum Size The platform-dependent maximum size for the flow table.
Number of Entries The total number of entries in the table, including the entries that are pending to be deleted.
Hardware Entries The number of entries that are currently inserted into the hardware.
Software-Only Entries The number of entries that are not installed in the hardware. This number includes entries that
are pending to be inserted, entries that cannot be inserted because of a missing interface, and
entries that cannot be inserted because the table is full.
Waiting for Space The number of entries that are not in the hardware because the attempt to insert them failed.
Entries
Flow Insertion Count The total number of flows that were added to the table since the switch powered up.
Flow Deletion Count The total number of flows that were deleted from the table since the switch powered up.
Insertion Failure Count The total number of hardware insertion attempts that were rejected because of lack of space
since the switch powered up.
Management Commands 178

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show openflow table-status openflow10
Flow Table...............................1
Flow Table Name.......................... Forwarding Database
Maximum Size.............................64
Number of Entries........................8
Hardware Entries.........................7
Software-Only Entries....................1
Waiting for Space Entries................0
Flow Insertion Count.....................1
Flow Deletion Count......................0
Insertion Failure Count..................0
Flow Table Description:
The forwarding database maps non-multicast MAC addresses and the ports on which these
addresses are located.
Example: The following shows example CLI display output for the command.
(NETGEAR Switch) #show openflow table-status openflow13
Flow Table..................................... 60
Flow Table Name................................ Openflow 1.3
Maximum Size................................... 1920
Number of Entries............................. 0
Hardware Entries............................... 0
Software-Only Entries.......................... 0
Waiting for Space Entries...................... 0
Flow Insertion Count........................... 0
Flow Deletion Count............................ 0
Insertion Failure Count........................ 0
Flow Table Description......................... The Openflow 1.3 table matches on the
packet layer-2 header, including DA-MAC, SA-MAC, VLAN, Vlan priority ether type; layer-3
header, including SRC-IP, DST-IP, IP protocol, IP-TOS; layer-4 header, including UDP/TCP
source and dest port, ICMP type, and code; SRC-IPv6, DST_IPv6, IPv6 Flow Label,ECN,
ICMPv6 type and code, source L4 Port for TCP / UDP / SCTP and input port including
physical port and LAG port.
Management Commands 179

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Cloud Managed Commands
Cloud managed commands enable you to manage the interaction of the switch with a cloud
management agent.
The switch maintains several configuration parameters for a cloud management agent.
These parameters are handled like any other configuration parameters but are not used by
the switch itself. The following table lists these parameters.
T able 9. Parameters for a cloud management agent
Parameter Description Range Default
Mode Overall administrative mode 0
• 0. Disabled
for cloud managed
• 1. Enabled
operation.
Proxy IP Address The IPv4 or IPv6 address of Any valid IPv4 or IPv6 host address. 0.0.0.0
a proxy server used to Address family:
access the public network.
• 0. None 0
• 1. INET
• 2. INET6
An IP address of 0.0.0.0 with an address
family type of None implies that this
parameter is not set.
Proxy IP Port Number The TCP/UDP port number 1–65535 0
that is used with the IP The value 0 is used to designate this
Address to access the parameter is not currently set.
proxy server.
Proxy Username A user name for logging into An ASCII string from 1 to 64 characters. “”
the proxy server. The empty string “” is used to specify that
this parameter is not set.
Proxy Password Encrypt The type of encryption that • 0. None 0
Type is used to store user • 1. AES
passwords securely.
• 2. MD5 (not used)
A password is stored and retrieved only in
its encrypted form. The switch supports
AES encryption only.
An encryption type of None is used to
specify that this parameter is not set.
Management Commands 180
