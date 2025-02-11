# 225.0.0.1
The following parameters are displayed in the trace message.

Pages: 294-294

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
debug igmpsnooping packet transmit
This command enables tracing of IGMP Snooping packets transmitted by the switch.
Snooping should be enabled on the device and the interface in order to monitor packets for a
particular interface.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug igmpsnooping packet transmit
Mode Privileged EXEC
The following sample shows the output of the trace message.
<15> JAN 01 02:45:06 192.168.17.29-1 IGMPSNOOP[185429992]: igmp_snooping_debug.c(116)
908 % Pkt TX - Intf: 1/0/20(20), Vlan_Id:1 Src_Mac: 00:03:0e:00:00:00 Dest_Mac:
01:00:5e:00:00:01 Src_IP: 9.1.1.1 Dest_IP: 225.0.0.1 Type: V2_Membership_Report Group:
225.0.0.1
The following parameters are displayed in the trace message.
Parameter Definition
TX A packet transmitted by the device.
Intf The interface that the packet left from. Format used is unit/slot/port (internal interface number). Unit
is always shown as 1 for interfaces on a standalone device.
Src_Mac Source MAC address of the packet.
Dest_Mac Destination multicast MAC address of the packet.
Src_IP The source IP address in the IP header in the packet.
Dest_IP The destination multicast IP address in the packet.
Type The type of IGMP packet. Type can be one of the following:
• Membership Query. GMP Membership Query
• V1_Membership_Report. IGMP Version 1 Membership Report
• V2_Membership_Report. IGMP Version 2 Membership Report
• V3_Membership_Report. IGMP Version 3 Membership Report
• V2_Leave_Group. IGMP Version 2 Leave Group
Group Multicast group address in the IGMP header.
no debug igmpsnooping transmit
This command disables tracing of transmitted IGMP snooping packets.
Format no debug igmpsnooping transmit
Mode Privileged EXEC
Utility Commands 294
