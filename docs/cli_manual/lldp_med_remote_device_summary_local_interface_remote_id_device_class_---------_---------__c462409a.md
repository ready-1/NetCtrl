# lldp_med_remote_device_summary_local_interface_remote_id_device_class_---------_---------__c462409a

Pages: 624-635

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show lldp med remote-device all
LLDP MED Remote Device Summary
Local
Interface Remote ID Device Class
--------- --------- ------------
1/0/8 1 Class I
1 /0/9 2 Not Defined
1 /0/10 3 Class II
1/0/11 4 Class III
1/0/12 5 Network Con
show lldp med remote-device detail
Use this command to display detailed information about remote devices that transmit current
LLDP MED data to an interface on the system.
Format show lldp med remote-device detail unit/slot/port
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show lldp med remote-device detail 1/0/8
LLDP MED Remote Device Detail
Local Interface: 1/0/8
Remote Identifier: 18
Capabilities
MED Capabilities Supported: capabilities, networkpolicy, location, extendedpse
MED Capabilities Enabled: capabilities, networkpolicy
Device Class: Endpoint Class I
Network Policies
Media Policy Application Type : voice
Vlan ID: 10
Priority: 5
DSCP: 1
Unknown: False
Tagged: True
Media Policy Application Type : streamingvideo
Vlan ID: 20
Priority: 1
Switching Commands 624

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
DSCP: 2
Unknown: False
Tagged: True
Inventory
Hardware Rev: xxx xxx xxx
Firmware Rev: xxx xxx xxx
Software Rev: xxx xxx xxx
Serial Num: xxx xxx xxx
Mfg Name: xxx xxx xxx
Model Name: xxx xxx xxx
Asset ID: xxx xxx xxx
Location
Subtype: elin
Info: xxx xxx xxx
Extended POE
Device Type: pseDevice
Extended POE PSE
Available: 0.3 Watts
Source: primary
Priority: critical
Extended POE PD
Required: 0.2 Watts
Source: local
Priority: low
Switching Commands 625

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Denial of Service Commands
This section describes the commands you use to configure Denial of Service (DoS) Control.
The switch provides support for classifying and blocking specific types of Denial of Service
attacks. You can configure your system to monitor and block these types of attacks:
• SIP = DIP. Source IP address = Destination IP address.
• First Fragment. TCP Header size smaller then configured value.
• TCP Fragment. Allows the device to drop packets that have a TCP payload where the IP
payload length minus the IP header size is less than the minimum allowed TCP header
size.
• TCP Flag. TCP Flag SYN set and Source Port < 1024 or TCP Control Flags = 0 and TCP
Sequence Number = 0 or TCP Flags FIN, URG, and PSH set and TCP Sequence
Number = 0 or TCP Flags SYN and FIN set.
• L4 Port. Source TCP/UDP Port = Destination TCP/UDP Port.
• ICMP. Limiting the size of ICMP Ping packets.
• SMAC = DMAC. Source MAC address = Destination MAC address.
• TCP Port. Source TCP Port = Destination TCP Port.
• UDP Port. Source UDP Port = Destination UDP Port.
• TCP Flag & Sequence. TCP Flag SYN set and Source Port < 1024 or TCP Control Flags
= 0 and TCP Sequence Number = 0 or TCP Flags FIN, URG, and PSH set and TCP
Sequence Number = 0 or TCP Flags SYN and FIN set.
• TCP Offset. Allows the device to drop packets that have a TCP header Offset set to 1.
• TCP SYN. TCP Flag SYN set.
• TCP SYN & FIN. TCP Flags SYN and FIN set.
• TCP FIN & URG & PSH. TCP Flags FIN and URG and PSH set and TCP Sequence
Number = 0.
• ICMP V6. Limiting the size of ICMPv6 Ping packets.
• ICMP Fragment. Checks for fragmented ICMP packets.
dos-control all
This command enables Denial of Service protection checks globally.
Default disabled
Format dos-control all
Mode Global Config
Switching Commands 626

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dos-control all
This command disables Denial of Service prevention checks globally.
Format no dos-control all
Mode Global Config
dos-control sipdip
This command enables Source IP address = Destination IP address (SIP = DIP) Denial of
Service protection. If the mode is enabled, Denial of Service prevention is active for this type
of attack. If packets ingress with SIP = DIP, the packets will be dropped if the mode is
enabled.
Default disabled
Format dos-control sipdip
Mode Global Config
no dos-control sipdip
This command disables Source IP address = Destination IP address (SIP = DIP) Denial of
Service prevention.
Format no dos-control sipdip
Mode Global Config
dos-control firstfrag
This command enables Minimum TCP Header Size Denial of Service protection. If the mode
is enabled, Denial of Service prevention is active for this type of attack. If packets ingress
having a TCP Header Size smaller then the configured value, the packets will be dropped if
the mode is enabled. The default is disabled. The range is 0–255. If you enable dos-control
firstfrag, but do not provide a Minimum TCP Header Size, the system sets that value to 20.
Default disabled (20)
Format dos-control firstfrag [size]
Mode Global Config
Switching Commands 627

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dos-control firstfrag
This command sets Minimum TCP Header Size Denial of Service protection to the default
value of disabled.
Format no dos-control firstfrag
Mode Global Config
dos-control tcpfrag
This command enables TCP Fragment Denial of Service protection. If the mode is enabled,
Denial of Service prevention is active for this type of attack and packets that have a TCP
payload in which the IP payload length minus the IP header size is less than the minimum
allowed TCP header size are dropped.
Default disabled
Format dos-control tcpfrag
Mode Global Config
no dos-control tcpfrag
This command disables TCP Fragment Denial of Service protection.
Format no dos-control tcpfrag
Mode Global Config
dos-control tcpflag
This command enables TCP Flag Denial of Service protections. If the mode is enabled,
Denial of Service prevention is active for this type of attacks. If packets ingress having TCP
Flag SYN set and a source port less than 1024 or having TCP Control Flags set to 0 and TCP
Sequence Number set to 0 or having TCP Flags FIN, URG, and PSH set and TCP Sequence
Number set to 0 or having TCP Flags SYN and FIN both set, the packets will be dropped if
the mode is enabled.
Default disabled
Format dos-control tcpflag
Mode Global Config
Switching Commands 628

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dos-control tcpflag
This command sets disables TCP Flag Denial of Service protections.
Format no dos-control tcpflag
Mode Global Config
dos-control l4port
This command enables L4 Port Denial of Service protections. If the mode is enabled, Denial
of Service prevention is active for this type of attack. If packets ingress having Source
TCP/UDP Port Number equal to Destination TCP/UDP Port Number, the packets will be
dropped if the mode is enabled.
Note: Some applications mirror source and destination L4 ports - RIP for
example uses 520 for both. If you enable dos-control l4port,
applications such as RIP may experience packet loss which would
render the application inoperable.
Default Disabled
Format dos-control l4port
Mode Global Config
no dos-control l4port
This command disables L4 Port Denial of Service protections.
Format no dos-control l4port
Mode Global Config
dos-control smacdmac
This command enables Source MAC address = Destination MAC address (SMAC = DMAC)
Denial of Service protection. If the mode is enabled, Denial of Service prevention is active for
this type of attack. If packets ingress with SMAC = DMAC, the packets will be dropped if the
mode is enabled.
Default disabled
Format dos-control smacdmac
Mode Global Config
Switching Commands 629

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dos-control smacdmac
This command disables Source MAC address = Destination MAC address (SMAC = DMAC)
DoS protection.
Format no dos-control smacdmac
Mode Global Config
dos-control tcpport
This command enables TCP L4 source = destination port number (Source TCP Port =
Destination TCP Port) Denial of Service protection. If the mode is enabled, Denial of Service
prevention is active for this type of attack. If packets ingress with Source TCP Port =
Destination TCP Port, the packets will be dropped if the mode is enabled.
Default Disabled
Format dos-control tcpport
Mode Global Config
no dos-control tcpport
This command disables TCP L4 source = destination port number (Source TCP Port =
Destination TCP Port) Denial of Service protection.
Format no dos-control tcpport
Mode Global Config
dos-control udpport
This command enables UDP L4 source = destination port number (Source UDP Port =
Destination UDP Port) DoS protection. If the mode is enabled, Denial of Service prevention is
active for this type of attack. If packets ingress with Source UDP Port = Destination UDP Port,
the packets will be dropped if the mode is enabled.
Default Disabled
Format dos-control udpport
Mode Global Config
Switching Commands 630

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dos-control udpport
This command disables UDP L4 source = destination port number (Source UDP Port =
Destination UDP Port) Denial of Service protection.
Format no dos-control udpport
Mode Global Config
dos-control tcpflagseq
This command enables TCP Flag and Sequence Denial of Service protections. If the mode is
enabled, Denial of Service prevention is active for this type of attack. If packets ingress
having TCP Flag SYN set and a source port less than 1024 or having TCP Control Flags set
to 0 and TCP Sequence Number set to 0 or having TCP Flags FIN, URG, and PSH set and
TCP Sequence Number set to 0 or having TCP Flags SYN and FIN both set, the packets will
be dropped if the mode is enabled.
Default Disabled
Format dos-control tcpflagseq
Mode Global Config
no dos-control tcpflagseq
This command sets disables TCP Flag and Sequence Denial of Service protection.
Format no dos-control tcpflagseq
Mode Global Config
dos-control tcpoffset
This command enables TCP Offset Denial of Service protection. If the mode is enabled,
Denial of Service prevention is active for this type of attack. If packets ingress having TCP
Header Offset equal to one (1), the packets will be dropped if the mode is enabled.
Default Disabled
Format dos-control tcpoffset
Mode Global Config
no dos-control tcpoffset
This command disabled TCP Offset Denial of Service protection.
Format no dos-control tcpoffset
Mode Global Config
Switching Commands 631

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
dos-control tcpsyn
This command enables TCP SYN and L4 source = 0-1023 Denial of Service protection. If the
mode is enabled, Denial of Service prevention is active for this type of attack. If packets
ingress having TCP flag SYN set and an L4 source port from 0 to 1023, the packets will be
dropped if the mode is enabled.
Default Disabled
Format dos-control tcpsyn
Mode Global Config
no dos-control tcpsyn
This command sets disables TCP SYN and L4 source = 0-1023 Denial of Service protection.
Format no dos-control tcpsyn
Mode Global Config
dos-control tcpsynfin
This command enables TCP SYN and FIN Denial of Service protection. If the mode is
enabled, Denial of Service prevention is active for this type of attack. If packets ingress
having TCP flags SYN and FIN set, the packets will be dropped if the mode is enabled.
Default Disabled
Format dos-control tcpsynfin
Mode Global Config
no dos-control tcpsynfin
This command sets disables TCP SYN & FIN Denial of Service protection.
Format no dos-control tcpsynfin
Mode Global Config
dos-control tcpfinurgpsh
This command enables TCP FIN and URG and PSH and SEQ = 0 checking Denial of Service
protections. If the mode is enabled, Denial of Service prevention is active for this type of
attack. If packets ingress having TCP FIN, URG, and PSH all set and TCP Sequence
Number set to 0, the packets will be dropped if the mode is enabled.
Switching Commands 632

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default Disabled
Format dos-control tcpfinurgpsh
Mode Global Config
no dos-control tcpfinurgpsh
This command sets disables TCP FIN and URG and PSH and SEQ = 0 checking Denial of
Service protections.
Format no dos-control tcpfinurgpsh
Mode Global Config
dos-control icmpv4
This command enables Maximum ICMPv4 Packet Size Denial of Service protections. If the
mode is enabled, Denial of Service prevention is active for this type of attack. If ICMPv4 Echo
Request (PING) packets ingress with a size greater than the configured value, the packets
are dropped if the mode is enabled. The value for the size is from 0–16376.
Default Disabled (512)
Format dos-control icmpv4 [size]
Mode Global Config
no dos-control icmpv4
This command disables Maximum ICMP Packet Size Denial of Service protections.
Format no dos-control icmpv4
Mode Global Config
dos-control icmpv6
This command enables Maximum ICMPv6 Packet Size Denial of Service protections. If the
mode is enabled, Denial of Service prevention is active for this type of attack. If ICMPv6 Echo
Request (PING) packets ingress having a size greater than the configured value, the packets
will be dropped if the mode is enabled. The value for the size is from 0–16376.
Default Disabled (512)
Format dos-control icmpv6 [size]
Mode Global Config
Switching Commands 633

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dos-control icmpv6
This command disables Maximum ICMP Packet Size Denial of Service protections.
Format no dos-control icmpv6
Mode Global Config
dos-control icmpfrag
This command enables ICMP Fragment Denial of Service protection. If the mode is enabled,
Denial of Service prevention is active for this type of attack. If packets ingress having
fragmented ICMP packets, the packets will be dropped if the mode is enabled.
Default disabled
Format dos-control icmpfrag
Mode Global Config
no dos-control icmpfrag
This command disabled ICMP Fragment Denial of Service protection.
Format no dos-control icmpfrag
Mode Global Config
show dos-control
This command displays Denial of Service configuration information.
Format show dos-control
Mode Privileged EXEC
Term Definition
First Fragment Mode The administrative mode of First Fragment DoS prevention. When enabled, this causes the
switch to drop packets that have a TCP header smaller then the configured Min TCP Hdr
Size.
Min TCP Hdr Size The minimum TCP header size the switch will accept if First Fragment DoS prevention is
enabled.
ICMPv4 Mode The administrative mode of ICMPv4 DoS prevention. When enabled, this causes the switch
to drop ICMP packets that have a type set to ECHO_REQ (ping) and a size greater than the
configured ICMPv4 Payload Size.
Max ICMPv4 Payload Size The maximum ICMPv4 payload size to accept when ICMPv4 DoS protection is enabled.
Switching Commands 634

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
ICMPv6 Mode The administrative mode of ICMPv6 DoS prevention. When enabled, this causes the switch
to drop ICMP packets that have a type set to ECHO_REQ (ping) and a size greater than the
configured ICMPv6 Payload Size.
Max ICMPv6 Payload Size The maximum ICMPv6 payload size to accept when ICMPv6 DoS protection is enabled.
ICMPv4 Fragment Mode The administrative mode of ICMPv4 Fragment DoS prevention. When enabled, this causes
the switch to drop fragmented ICMPv4 packets.
TCP Port Mode The administrative mode of TCP Port DoS prevention. When enabled, this causes the
switch to drop packets that have the TCP source port equal to the TCP destination port.
UDP Port Mode The administrative mode of UDP Port DoS prevention. When enabled, this causes the
switch to drop packets that have the UDP source port equal to the UDP destination port.
SIPDIP Mode The administrative mode of SIP=DIP DoS prevention. Enabling this causes the switch to
drop packets that have a source IP address equal to the destination IP address. The factory
default is disabled.
SMACDMAC Mode The administrative mode of SMAC=DMAC DoS prevention. Enabling this causes the switch
to drop packets that have a source MAC address equal to the destination MAC address.
TCP FIN&URG& PSH The administrative mode of TCP FIN & URG & PSH DoS prevention. Enabling this causes
Mode the switch to drop packets that have TCP flags FIN, URG, and PSH set and TCP Sequence
Number = 0.
TCP Flag & Sequence The administrative mode of TCP Flag DoS prevention. Enabling this causes the switch to
Mode drop packets that have TCP control flags set to 0 and TCP sequence number set to 0.
TCP SYN Mode The administrative mode of TCP SYN DoS prevention. Enabling this causes the switch to
drop packets that have TCP Flags SYN set.
TCP SYN & FIN Mode The administrative mode of TCP SYN & FIN DoS prevention. Enabling this causes the
switch to drop packets that have TCP Flags SYN and FIN set.
TCP Fragment Mode The administrative mode of TCP Fragment DoS prevention. Enabling this causes the switch
to drop packets that have a TCP payload in which the IP payload length minus the IP
header size is less than the minimum allowed TCP header size.
TCP Offset Mode The administrative mode of TCP Offset DoS prevention. Enabling this causes the switch to
drop packets that have a TCP header Offset equal to 1.
auto-dos
This command enables Auto-DoS on the switch. By default, Auto-Dos is disabled.
When you enable Auto-DoS, all denial of service (DoS) checks are activated. If the switch
detects a DoS attack, the offending packets are copied to the CPU and Auto-DoS shuts down
the port and moves the port to the diagnostically disabled state. To use the port again, you
must manually reenable the port.
Format auto-dos
Mode Global Config
Switching Commands 635
