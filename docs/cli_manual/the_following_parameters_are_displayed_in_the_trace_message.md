# the_following_parameters_are_displayed_in_the_trace_message

Pages: 295-303

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
debug igmpsnooping packet receive
This command enables tracing of IGMP Snooping packets received by the switch. Snooping
should be enabled on the device and the interface in order to monitor packets for a particular
interface.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug igmpsnooping packet receive
Mode Privileged EXEC
The following sample shows the output of the trace message.
<15> JAN 01 02:45:06 192.168.17.29-1 IGMPSNOOP[185429992]: igmp_snooping_debug.c(116)
908 % Pkt RX - Intf: 1/0/20(20), Vlan_Id:1 Src_Mac: 00:03:0e:00:00:10 Dest_Mac:
01:00:5e:00:00:05 Src_IP: 11.1.1.1 Dest_IP: 225.0.0.5 Type: Membership_Query Group:
225.0.0.5
The following parameters are displayed in the trace message.
Parameter Definition
RX A packet received by the device.
Intf The interface that the packet went out on.
Src_Mac Source MAC address of the packet.
Dest_Mac Destination multicast MAC address of the packet.
Src_IP The source IP address in the ip header in the packet.
Dest_IP The destination multicast ip address in the packet.
Type The type of IGMP packet. Type can be one of the following:
• Membership_Query. IGMP Membership Query
• V1_Membership_Report. IGMP Version 1 Membership Report
• V2_Membership_Report. IGMP Version 2 Membership Report
• V3_Membership_Report. IGMP Version 3 Membership Report
• V2_Leave_Group. IGMP Version 2 Leave Group
Group Multicast group address in the IGMP header.
no debug igmpsnooping receive
This command disables tracing of received IGMP Snooping packets.
Format no debug igmpsnooping receive
Mode Privileged EXEC
Utility Commands 295

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
debug ip acl
Use this command to enable debug of IP Protocol packets matching the ACL criteria.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug ip acl number
Mode Privileged EXEC
no debug ip acl
Use this command to disable debug of IP Protocol packets matching the ACL criteria.
Format no debug ip acl number
Mode Privileged EXEC
debug ip dvmrp packet
Use this command to trace DVMRP packet reception and transmission. The receive
keyword traces only received DVMRP packets and transmit keyword traces only
transmitted DVMRP packets. When neither keyword is used in the command, then all
DVMRP packet traces are dumped. Vital information such as source address, destination
address, control packet type, packet length, and the interface on which the packet is received
or transmitted is displayed on the console.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug ip dvmrp packet [receive | transmit]
Mode Privileged EXEC
no debug ip dvmrp packet
Use this command to disable debug tracing of DVMRP packet reception and transmission.
Format no debug ip dvmrp packet [receive | transmit]
Mode Privileged EXEC
debug ip igmp packet
Use this command to trace IGMP packet reception and transmission. The receive keyword
traces only received IGMP packets and the transmit keyword traces only transmitted
IGMP packets. When neither keyword is used in the command, then all IGMP packet traces
Utility Commands 296

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
are dumped. Vital information such as source address, destination address, control packet
type, packet length, and the interface on which the packet is received or transmitted is
displayed on the console.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug ip igmp packet [receive | transmit]
Mode Privileged EXEC
no debug ip igmp packet
Use this command to disable debug tracing of IGMP packet reception and transmission.
Format no debug ip igmp packet [receive | transmit]
Mode Privileged EXEC
debug ip mcache packet
Use this command for tracing MDATA packet reception and transmission. The receive
keyword traces only received MDATA packets and the transmit keyword traces only
transmitted MDATA packets. When neither keyword is used in the command, then all data
packet traces are dumped. Vital information such as source address, destination address,
packet length, and the interface on which the packet is received or transmitted is displayed
on the console.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug ip mcache packet [receive | transmit]
Mode Privileged EXEC
no debug ip mcache packet
Use this command to disable debug tracing of MDATA packet reception and transmission.
Format no debug ip mcache packet [receive | transmit]
Mode Privileged EXEC
debug ip pimdm packet
Use this command to trace PIMDM packet reception and transmission. The receive
keyword traces only received PIMDM packets and the transmit keyword traces only
transmitted PIMDM packets. When neither keyword is used in the command, then all PIMDM
Utility Commands 297

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
packet traces are dumped. Vital information such as source address, destination address,
control packet type, packet length, and the interface on which the packet is received or
transmitted is displayed on the console.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug ip pimdm packet [receive | transmit]
Mode Privileged EXEC
no debug ip pimdm packet
Use this command to disable debug tracing of PIMDM packet reception and transmission.
Format no debug ip pimdm packet [receive | transmit]
Mode Privileged EXEC
debug ip pimsm packet
Use this command to trace PIMSM packet reception and transmission. The receive
keyword traces only received PIMSM packets and the transmit keyword traces only
transmitted PIMSM packets. When neither keyword is used in the command, then all PIMSM
packet traces are dumped. Vital information such as source address, destination address,
control packet type, packet length, and the interface on which the packet is received or
transmitted is displayed on the console.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug ip pimsm packet [receive | transmit]
Mode Privileged EXEC
no debug ip pimsm packet
Use this command to disable debug tracing of PIMSM packet reception and transmission.
Format no debug ip pimsm packet [receive | transmit]
Mode Privileged EXEC
Utility Commands 298

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
debug ip vrrp
Use this command to enable VRRP debug protocol messages.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug ip vrrp
Mode Privileged EXEC
no debug ip vrrp
Use this command to disable VRRP debug protocol messages.
Format no debug ip vrrp
Mode Privileged EXEC
debug ipv6 dhcp
This command displays “debug” information about DHCPv6 client activities and traces
DHCPv6 packets to and from the local DHCPv6 client.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug ipv6 dhcp
Mode Privileged EXEC
no debug ipv6 dhcp
This command disables the display of “debug” trace output for DHCPv6 client activity.
Format no debug ipv6 dhcp
Mode Privileged EXEC
debug ipv6 mcache packet
Use this command for tracing MDATAv6 packet reception and transmission. The receive
keyword traces only received MDATAv6 packets and the transmit keyword traces only
transmitted MDATAv6 packets. When neither keyword is used in the command, then all data
packet traces are dumped. Vital information such as source address, destination address,
packet length, and the interface on which the packet is received or transmitted is displayed
on the console.
Utility Commands 299

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug ipv6 mcache packet [receive | transmit]
Mode Privileged EXEC
no debug ipv6 mcache packet
Use this command to disable debug tracing of MDATAv6 packet reception and transmission.
Format no debug ipv6 mcache packet [receive | transmit]
Mode Privileged EXEC
debug ipv6 mld packet
Use this command to trace MLDv6 packet reception and transmission. The receive
keyword traces only received MLDv6 packets and the transmit keyword traces only
transmitted MLDv6 packets. When neither keyword is used in the command, then all MLDv6
packet traces are dumped. Vital information such as source address, destination address,
control packet type, packet length, and the interface on which the packet is received or
transmitted is displayed on the console.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug ipv6 mld packet [receive | transmit]
Mode Privileged EXEC
no debug ipv6 mld packet
Use this command to disable debug tracing of MLDv6 packet reception and transmission.
Format no debug ipv6 mld packet [receive | transmit]
Mode Privileged EXEC
Utility Commands 300

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
debug ipv6 ospfv3 packet
Use this command to enable IPv6 OSPFv3 packet debug trace.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug ipv6 ospfv3 packet
Mode Privileged EXEC
no debug ipv6 ospfv3 packet
Use this command to disable tracing of IPv6 OSPFv3 packets.
Format no debug ipv6 ospfv3 packet
Mode Privileged EXEC
debug ipv6 pimdm packet
Use this command to trace PIMDMv6 packet reception and transmission. The receive
keyword traces only received PIMDMv6 packets and the transmit keyword traces only
transmitted PIMDMv6 packets. If neither keyword is used in the command, all PIMDMv6
packet traces are dumped. Vital information such as source address, destination address,
control packet type, packet length, and the interface on which the packet is received or
transmitted is displayed on the console.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug ipv6 pimdm packet [receive | transmit]
Mode Privileged EXEC
no debug ipv6 pimdm packet
Use this command to disable debug tracing of PIMDMv6 packet reception and transmission.
Format no debug ipv6 pimdm packet [receive | transmit]
Mode Privileged EXEC
debug ipv6 pimsm packet
Use this command to trace PIMSMv6 packet reception and transmission. The receive
keyword traces only received PIMSMv6 packets and the transmit keyword traces only
transmitted PIMSMv6 packets. If neither keyword is used in the command, all PIMSMv6
packet traces are dumped. Vital information such as source address, destination address,
Utility Commands 301

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
control packet type, packet length, and the interface on which the packet is received or
transmitted is displayed on the console.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug ipv6 pimsm packet [receive | transmit]
Mode Privileged EXEC
no debug ipv6 pimsm packet
Use this command to disable debug tracing of PIMSMv6 packet reception and transmission.
Format no debug ipv6 pimsm packet [receive | transmit]
Mode Privileged EXEC
debug lacp packet
This command enables tracing of LACP packets received and transmitted by the switch.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug lacp packet
Mode Privileged EXEC
The following sample shows the output of the trace message.
<15> JAN 01 14:04:51 10.254.24.31-1 DOT3AD[183697744]: dot3ad_debug.c(385) 58 %%
Pkt TX - Intf: 1/0/1(1), Type: LACP, Sys: 00:11:88:14:62:e1, State: 0x47, Key: 0x36
no debug lacp packet
This command disables tracing of LACP packets.
Format no debug lacp packet
Mode Privileged EXEC
debug mldsnooping packet
Use this command to trace MLD snooping packet reception and transmission. The receive
keyword traces only received MLD packets and the transmit keyword traces only
transmitted MLD snooping packets. When neither keyword is used in the command, then all
MLD snooping packet traces are dumped. Vital information such as source address,
Utility Commands 302

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
destination address, control packet type, packet length, and the interface on which the packet
is received or transmitted is displayed on the console.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug mldsnooping packet [receive | transmit]
Mode Privileged EXEC
no debug mldsnooping packet
Use this command to disable debug tracing of MLD snooping packet reception and
transmission.
Format no debug mldsnooping packet [receive | transmit]
Mode Privileged EXEC
debug ospf packet
This command enables tracing of OSPF packets received and transmitted by the switch.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug ospf packet
Mode Privileged EXEC
The following samples show the output of the trace message.
<15> JAN 02 11:03:31 10.50.50.1-2 OSPF[46300472]: ospf_debug.c(297) 25430 % Pkt RX -
Intf:2/0/48 Src
Ip:192.168.50.2 DestIp:224.0.0.5 AreaId:0.0.0.0 Type:HELLO NetMask:255.255.255.0 D
esigRouter:0.0.0.0 Backup:0.0.0.0
<15> JAN 02 11:03:35 10.50.50.1-2 OSPF[46300472]: ospf_debug.c(293) 25431 % Pkt TX -
Intf:2/0/48 Src
Ip:10.50.50.1 DestIp:192.168.50.2 AreaId:0.0.0.0 Type:DB_DSCR Mtu:1500 Options:E
Flags: I/M/MS Seq:126166
<15> JAN 02 11:03:36 10.50.50.1-2 OSPF[46300472]: ospf_debug.c(297) 25434 % Pkt RX -
Intf:2/0/48 Src
Ip:192.168.50.2 DestIp:192.168.50.1 AreaId:0.0.0.0 Type:LS_REQ Length: 1500
<15> JAN 02 11:03:36 10.50.50.1-2 OSPF[46300472]: ospf_debug.c(293) 25435 % Pkt TX -
Intf:2/0/48 Src
Ip:10.50.50.1 DestIp:192.168.50.2 AreaId:0.0.0.0 Type:LS_UPD Length: 1500
Utility Commands 303
