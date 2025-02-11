# 10 Enabled Enabled H2 Enabled

Pages: 559-566

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
IP Address Displays whether IP Address Validation is enabled or disabled.
Validation
VLAN The VLAN ID for each displayed row.
Configuration Displays whether DAI is enabled or disabled on the VLAN.
Log Invalid Displays whether logging of invalid ARP packets is enabled on the VLAN.
ACL Name The ARP ACL Name, if configured on the VLAN.
Static Flag If the ARP ACL is configured static on the VLAN.
Command example:
(NETGEAR Switch) #show ip arp inspection vlan 10-12
Source Mac Validation : Disabled
Destination Mac Validation : Disabled
IP Address Validation : Disabled
Vlan Configuration Log Invalid ACL Name Static flag
---- ------------- ----------- --------- ----------
10 Enabled Enabled H2 Enabled
11 Disabled Enabled
12 Enabled Disabled
show ip arp inspection statistics
Use this command to display the statistics of the ARP packets that are processed by
Dynamic ARP Inspection (DAI). For the vlan-list argument, you can enter a list of VLANs
(for example, 12-18 or 12,14) to display the statistics on all DAI-enabled VLANs in the list, or
enter a single VLAN to display the statistics for only that VLAN. If you do not include the
vlan keyword and vlan-list argument, the command output displays a summary of the
forwarded and dropped ARP packets.
Format show ip arp inspection statistics [vlan vlan-list]
Mode Privileged EXEC
User EXEC
Term Definition
VLAN The VLAN ID for each displayed row.
Forwarded The total number of valid ARP packets forwarded in this VLAN.
Dropped The total number of not valid ARP packets dropped in this VLAN.
DHCP Drops The number of packets dropped due to DHCP snooping binding database match failure.
Switching Commands 559

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
ACL Drops The number of packets dropped due to ARP ACL rule match failure.
DHCP Permits The number of packets permitted due to DHCP snooping binding database match.
ACL Permits The number of packets permitted due to ARP ACL rule match.
Bad Src MAC The number of packets dropped due to Source MAC validation failure.
Bad Dest MAC The number of packets dropped due to Destination MAC validation failure.
Invalid IP The number of packets dropped due to invalid IP checks.
Command example:
The output of the show ip arp inspection statistics command lists the summary
of forwarded and dropped ARP packets on all DAI-enabled VLANs:
VLAN Forwarded Dropped
---- --------- -------
10 90 14
20 10 3
Command example:
(NETGEAR Switch) #show ip arp inspection statistics vlan vlan-list
VLAN DHCP ACL DHCP ACL Bad Src Bad Dest Invalid
D rops D rops Permits Permits MAC MAC IP
----- -------- --------- ----------- --------- ---------- ----------- ---------
10 11 1 6 5 25 1 1 0
20 1 0 8 2 0 1 1
clear ip arp inspection statistics
Use this command to reset the statistics for Dynamic ARP Inspection on all VLANs.
Default none
Format clear ip arp inspection statistics
Mode Privileged EXEC
show ip arp inspection interfaces
Use this command to display the Dynamic ARP Inspection configuration on all the
DAI-enabled interfaces. An interface is said to be enabled for DAI if at least one VLAN, that
the interface is a member of, is enabled for DAI. Given a unit/slot/port interface
Switching Commands 560

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
argument, the command displays the values for that interface whether the interface is
enabled for DAI or not.
Format show ip arp inspection interfaces [unit/slot/port]
Mode Privileged EXEC
User EXEC
Term Definition
Interface The interface ID for each displayed row.
Trust State Whether the interface is trusted or untrusted for DAI.
Rate Limit The configured rate limit value in packets per second.
Burst Interval The configured burst interval value in seconds.
Command example:
(NETGEAR Switch) #show ip arp inspection interfaces
Interface T rust State Rate Limit Burst Interval
(pps) (seconds)
--------------- ----------- ---------- ---------------
0/1 Untrusted 15 1
0/2 Untrusted 10 10
show arp access-list
Use this command to display the configured ARP ACLs with the rules. Giving an ARP ACL
name as the argument displays only the rules in that ARP ACL.
Format show arp access-list [acl-name]
Mode Privileged EXEC
User EXEC
Command example:
(NETGEAR Switch) #show arp access-list
ARP access list H2
permit ip host 1.1.1.1 mac host 00:01:02:03:04:05
permit ip host 1.1.1.2 mac host 00:03:04:05:06:07
ARP access list H3
ARP access list H4
permit ip host 2.1.1.2 mac host 00:03:04:05:06:08
Switching Commands 561

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
MVR Commands
Internet Group Management Protocol (IGMP) Layer 3 is widely used for IPv4 network
multicasting. In Layer 2 networks, IGMP uses resources inefficiently. For example, a Layer 2
switch multicast traffic to all ports, even if there are receivers connected to only a few ports.
To address this problem, the IGMP Snooping protocol was developed. The problem still
appears, though, when receivers are in different VLANs.
MVR is intended to solve the problem of receivers in different VLANs. It uses a dedicated
manually configured VLAN, called the multicast VLAN, to forward multicast traffic over a
Layer 2 network with IGMP snooping.
mvr
This command enables MVR.
Default Disabled
Format mvr
Mode Global Config
Interface Config
no mvr
This command disables MVR.
Format no mvr
Mode Global Config
Interface Config
mvr group
This command adds an MVR membership group. A.B.C.D is the IP multicast group being
added.
The count is the number of incremental multicast groups being added (the first multicast
group is A.B.C.D). If a count is not specified, only one multicast group is added.
Format mvr group A.B.C.D [count]
Mode Global Config
Switching Commands 562

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no mvr group
This command removes the MVR membership group.
Format no mvr group A.B.C.D [count]
Mode Global Config
mvr mode
This command changes the MVR mode type. If the mode is set to compatible, the switch
does not learn multicast groups; they need to be configured by the operator as the protocol
does not forward joins from the hosts to the router. To operate in this mode, the IGMP router
needs to be statically configured to transmit all required multicast streams to the MVR switch.
If the mode is set to dynamic, the switch learns existing multicast groups by snooping the
IGMP queries from the router on source ports and forwarding the IGMP joins from the hosts
to the IGMP router on the multicast VLAN (with appropriate translation of the VLAN ID).
Default Compatible
Format mvr mode {compatible | dynamic}
Mode Global Config
no mvr mode
This command sets the mode type to the default value.
Format no mvr mode
Mode Global Config
mvr querytime
This command sets the MVR query response time in deciseconds. The time is in the range
1–100 deciseconds (one decisecond is one tenth of a second).
Default 5
Format mvr querytime deciseconds
Mode Global Config
no mvr querytime
This command sets the MVR query response time to the default value.
Format no mvr querytime
Mode Global Config
Switching Commands 563

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
mvr vlan
This command sets the MVR multicast VLAN.
Default 1
Format mvr vlan vlan-id
Mode Global Config
no mvr vlan
This command sets the MVR multicast VLAN to the default value.
Format no mvr vlan
Mode Global Config
mvr immediate
This command enables MVR immediate leave mode. MVR provides two modes of operating
with the IGMP Leave messages: normal leave and immediate leave.
• In normal leave mode, when a leave is received, the general IGMP query is sent from a
Layer 2 switch to the receiver port, where the leave was received. Then reports are
received from other interested hosts that are also connected to that port, for example,
using hub.
• In immediate leave mode, when a leave is received, the switch is immediately
reconfigured not to forward a specific multicast stream to the port where a message is
received. This mode is used only for ports where only one client might be connected.
Default Disabled
Format mvr immediate
Mode Interface Config
no mvr immediate
This command sets the MVR multicast VLAN to the default value.
Format no mvr immediate
Mode Interface Config
Switching Commands 564

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
mvr type
This command sets the MVR port type. When a port is set as source, it is the port to which
the multicast traffic flows using the multicast VLAN. When a port is set to receiver, it is the
port where a listening host is connected to the switch.
Default none
Format mvr type {receiver | source}
Mode Interface Config
no mvr type
Use this command to set the MVR port type to none.
Format no mvr type
Mode Interface Config
mvr vlan group
Use this command to include the port in the specific MVR group. mVLAN is the multicast
VLAN, and A.B.C.D is the IP multicast group.
Format mvr vlan mVLAN group A.B.C.D
Mode Interface Config
no mvr vlan
Use this command to exclude the port from the specific MVR group.
Format no mvr vlan mVLAN group A.B.C.D
Mode Interface Config
show mvr
This command displays global MVR settings.
Format show mvr
Mode Privileged EXEC
The following table explains the output parameters.
Term Definition
MVR Running MVR running state. It can be enabled or disabled.
MVR multicast VLAN Current MVR multicast VLAN. It can be in the range from 1 to 4094.
Switching Commands 565

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
MVR Max Multicast Groups The maximum number of multicast groups supported by MVR.
MVR Current multicast groups The current number of MVR groups allocated.
MVR Query response time The current MVR query response time.
MVR Mode The current MVR mode. It can be compatible or dynamic.
Command example:
(NETGEAR Switch)#show mvr
MVR Running…........................... TRUE
MVR multicast VLAN….................... 1200
MVR Max Multicast Groups….............. 256
MVR Current multicast groups….......... 1
MVR Global query response time…........ 10 (tenths of sec)
MVR Mode….............................. compatible
show mvr members
This command displays the MVR membership groups allocated. A.B.C.D is a valid multicast
address in IPv4 dotted notation.
Format show mvr members [A.B.C.D]
Mode Privileged EXEC
The following table describes the output parameters.
Term Definition
MVR Group IP MVR group multicast IP address.
Status The status of the specific MVR group. It can be active or inactive.
Members The list of ports that participates in the specified MVR group.
Command example:
(NETGEAR Switch)#show mvr members
MVR Group IP Status Members
------------------ --------------- ---------------------
2 24.1.1.1 INACTIVE 0/1, 0/2, 0/3
(switch)#show mvr members 224.1.1.1
MVR Group IP Status Members
------------------ --------------- ---------------------
2 24.1.1.1 INACTIVE 0/1, 0/2, 0/3
Switching Commands 566
