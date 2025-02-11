# mtu_mtu

Pages: 304-316

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
<15> JAN 02 11:03:37 10.50.50.1-2 OSPF[46300472]: ospf_debug.c(293) 25441 % Pkt TX -
Intf:2/0/48 Src
Ip:10.50.50.1 DestIp:224.0.0.6 AreaId:0.0.0.0 Type:LS_ACK Length: 1500
The following parameters are displayed in the trace message.
Parameter Definition
TX/RX TX refers to a packet transmitted by the device. RX refers to packets received by the device.
Intf The interface that the packet came in or went out on. Format used is unit/slot/port (internal interface
number).
SrcIp The source IP address in the IP header of the packet.
DestIp The destination IP address in the IP header of the packet.
AreaId The area ID in the OSPF header of the packet.
Type Could be one of the following:
• HELLO. Hello packet
• DB_DSCR. Database descriptor
• LS_REQ. LS Request
• LS_UPD. LS Update
• LS_ACK. LS Acknowledge
The remaining fields in the trace are specific to the type of OSPF Packet.
HELLO packet field definitions.
Parameter Definition
Netmask The netmask in the hello packet.
DesignRouter Designated Router IP address.
Backup Backup router IP address.
DB_DSCR packet field definitions.
Field Definition
MTU MTU
Options Options in the OSPF packet.
Flags Could be one or more of the following:
• I. Init
• M. More
• MS. Master/Slave
Seq Sequence Number of the DD packet.
Utility Commands 304

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
LS_REQ packet field definitions.
Field Definition
Length Length of packet
LS_UPD packet field definitions.
Field Definition
Length Length of packet
LS_ACK packet field definitions.
Field Definition
Length Length of packet
no debug ospf packet
This command disables tracing of OSPF packets.
Format no debug ospf packet
Mode Privileged EXEC
debug ping packet
This command enables tracing of ICMP echo requests and responses. The command traces
pings on the network port/ service port for switching packages. For routing packages, pings
are traced on the routing ports as well.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug ping packet
Mode Privileged EXEC
The following sample shows the output of the trace message.
<15> JAN 01 00:21:22 192.168.17.29-1 SIM[181040176]: sim_debug.c(128) 20 % Pkt TX - Intf:
1/0/1(1),
SRC_IP:10.50.50.2, DEST_IP:10.50.50.1, Type:ECHO_REQUEST
<15> JAN 01 00:21:22 192.168.17.29-1 SIM[182813968]: sim_debug.c(82) 21 % Pkt RX - Intf:
1/0/1(1), S
RC_IP:10.50.50.1, DEST_IP:10.50.50.2, Type:ECHO_REPLY
Utility Commands 305

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The following parameters are displayed in the trace message.
Parameter Definition
TX/RX TX refers to a packet transmitted by the device. RX refers to packets received by the device.
Intf The interface that the packet came in or went out on.
SRC_IP The source IP address in the IP header in the packet.
DEST_IP The destination IP address in the IP header in the packet.
Type Type determines whether or not the ICMP message is a REQUEST or a RESPONSE.
no debug ping packet
This command disables tracing of ICMP echo requests and responses.
Format no debug ping packet
Mode Privileged EXEC
debug rip packet
This command turns on tracing of RIP requests and responses. This command takes no
options. The output is directed to the log file.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug rip packet
Mode Privileged EXEC
The following sample shows the output of the trace message.
<15> JAN 01 00:35:15 192.168.17.29-1 RIP[181783160]: rip_map_debug.c(96) 775 %
Pkt RX on Intf: 1/0/1(1), Src_IP:43.1.1.1 Dest_IP:43.1.1.2
Rip_Version: RIPv2 Packet_Type:RIP_RESPONSE
ROUTE 1): Network: 10.1.1.0 Mask: 255.255.255.0 Metric: 1
ROUTE 2): Network: 40.1.0.0 Mask: 255.255.0.0 Metric: 1
ROUTE 3): Network: 10.50.50.0 Mask: 255.255.255.0 Metric: 1
ROUTE 4): Network: 41.1.0.0 Mask: 255.255.0.0 Metric: 1
ROUTE 5): Network:42.0.0.0 Mask:255.0.0.0 Metric:1
Another 6 routes present in packet not displayed.
Utility Commands 306

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The following parameters are displayed in the trace message.
Parameter Definition
TX/RX TX refers to a packet transmitted by the device. RX refers to packets received by the device.
Intf The interface that the packet came in or went out on.
Src_IP The source IP address in the IP header of the packet.
Dest_IP The destination IP address in the IP header of the packet.
Rip_Version RIP version used: RIPv1 or RIPv2.
Packet_Type Type of RIP packet: RIP_REQUEST or RIP_RESPONSE.
Routes Up to 5 routes in the packet are displayed in the following format:
• Network. a.b.c.d
• Mask. a.b.c.d
• Next Hop. a.b.c.d
• Metric. a
The next hop is only displayed if it is different from 0.0.0.0.
For RIPv1 packets, Mask is always 0.0.0.0.
Number of routes Only the first five routes present in the packet are included in the trace. There is another notification
not printed of the number of additional routes present in the packet that were not included in the trace.
no debug rip packet
This command disables tracing of RIP requests and responses.
Format no debug rip packet
Mode Privileged EXEC
debug sflow packet
Use this command to enable sFlow debug packet trace.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug sflow packet
Mode Privileged EXEC
Utility Commands 307

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no debug sflow packet
Use this command to disable sFlow debug packet trace.
Format no debug sflow packet
Mode Privileged EXEC
debug spanning-tree bpdu
This command enables tracing of spanning tree BPDUs received and transmitted by the
switch.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug spanning-tree bpdu
Mode Privileged EXEC
no debug spanning-tree bpdu
This command disables tracing of spanning tree BPDUs.
Format no debug spanning-tree bpdu
Mode Privileged EXEC
debug spanning-tree bpdu receive
This command enables tracing of spanning tree BPDUs received by the switch. Spanning
tree should be enabled on the device and on the interface in order to monitor packets for a
particular interface.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug spanning-tree bpdu receive
Mode Privileged EXEC
The following sample shows the output of the trace message.
<15> JAN 01 01:02:04 192.168.17.29-1 DOT1S[191096896]: dot1s_debug.c(1249) 101 % Pkt RX
- Intf: 1/0/9(9), Source_Mac: 00:11:88:4e:c2:10 Version: 3, Root Mac: 00:11:88:4e:c2:00,
Root Priority: 0x8000 Path Cost: 0
Utility Commands 308

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The following parameters are displayed in the trace message.
Parameter Definition
RX A packet received by the device.
Intf The interface that the packet came in on.
Source_Mac Source MAC address of the packet.
Version Spanning tree protocol version (0-3). 0 refers to STP, 2 RSTP and 3 MSTP.
Root_Mac MAC address of the CIST root bridge.
Root_Priority Priority of the CIST root bridge. The value is between 0 and 61440. It is displayed in hex in multiples
of 4096.
Path_Cost External root path cost component of the BPDU.
no debug spanning-tree bpdu receive
This command disables tracing of received spanning tree BPDUs.
Format no debug spanning-tree bpdu receive
Mode Privileged EXEC
debug spanning-tree bpdu transmit
This command enables tracing of spanning tree BPDUs transmitted by the switch. Spanning
tree should be enabled on the device and on the interface in order to monitor packets on a
particular interface.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug spanning-tree bpdu transmit
Mode Privileged EXEC
The following sample shows the output of the trace message.
<15> JAN 01 01:02:04 192.168.17.29-1 DOT1S[191096896]: dot1s_debug.c(1249) 101 % Pkt TX
- Intf: 1/0/7(7), Source_Mac: 00:11:88:4e:c2:00 Version: 3, Root_Mac: 00:11:88:4e:c2:00,
Root_Priority: 0x8000 Path_Cost: 0
Utility Commands 309

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The following parameters are displayed in the trace message.
Parameter Definition
TX A packet transmitted by the device.
Intf The interface that the packet went out on.
Source_Mac Source MAC address of the packet.
Version Spanning tree protocol version (0-3). 0 refers to STP, 2 RSTP and 3 MSTP.
Root_Mac MAC address of the CIST root bridge.
Root_Priority Priority of the CIST root bridge. The value is between 0 and 61440. It is displayed in hex in multiples
of 4096.
Path_Cost External root path cost component of the BPDU.
no debug spanning-tree bpdu transmit
This command disables tracing of transmitted spanning tree BPDUs.
Format no debug spanning-tree bpdu transmit
Mode Privileged EXEC
debug tacacs
Use the debug tacacs packet command to turn on TACACS+ debugging.
Note: To display the debug trace, enable the debug console command.
Format debug tacacs {packet [receive | transmit] | accounting | authentication}
Mode Global Config
Parameter Description
packet receive Turn on TACACS+ receive packet debugs.
packet transmit Turn on TACACS+ transmit packet debugs.
accounting Turn on TACACS+ authentication debugging.
authentication Turn on TACACS+ authorization debugging.
Utility Commands 310

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
debug transfer
This command enables debugging for file transfers.
Note: To display the debug trace, enable the debug console command.
Format debug transfer
Mode Privileged EXEC
no debug transfer
This command disables debugging for file transfers.
Format no debug transfer
Mode Privileged EXEC
debug udld events
This command enables debugging for the UDLD events.
Note: To display the debug trace, enable the debug console command.
Default Disabled
Format debug udld events
Mode Privileged EXEC
debug udld packet receive
This command enables debugging on the received UDLD PDUs.
Note: To display the debug trace, enable the debug console command.
Default Disabled
Format debug udld packet receive
Mode Privileged EXEC
Utility Commands 311

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
debug udld packet transmit
This command enables debugging on the transmitted UDLD PDUs.
Note: To display the debug trace, enable the debug console command.
Default Disabled
Format debug udld packet transmit
Mode Privileged EXEC
show debugging
Use the show debugging command to display enabled packet tracing configurations.
Format show debugging
Mode Privileged EXEC
Command example:
console# debug arp
Arp packet tracing enabled.
console# show debugging
Arp packet tracing enabled.
no show debugging
Use the no show debugging command to disable packet tracing configurations.
Format no show debugging
Mode Privileged EXEC
exception protocol
Use this command to specify the protocol used to store the core dump file.
Default usb
Format exception protocol {nfs | tftp | ftp| usb | none}
Mode Global Config
Utility Commands 312

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no exception protocol
Use this command to reset the exception protocol configuration to its factory default value.
Format no exception protocol
Mode Global Config
exception dump ftp-server
Use this command to configure the IP address of a remote FTP server as an external server
to which you can dump core files. If you do not specify the user name and password, the
switch uses anonymous FTP. (The FTP server must be configured to accept anonymous
FTP.)
Default None
Format exception dump ftp-server ip-address [{username user-name password password}]
Mode Global Config
no exception dump ftp-server
This command resets the remote FTP server configuration that is used for exception dumps
to the default value (which is none). This command also resets the FTP user name and
password to empty strings.
Format exception dump ftp-server
Mode Global Config
exception dump tftp-server
Use this command to configure the IP address of a remote TFTP server in order to dump
core files to an external server.
Default None
Format exception dump tftp-server {ip-address}
Mode Global Config
no exception dump tftp-server
Use this command to reset the exception dump remote server configuration to its factory
default value.
Format no exception dump tftp-server
Mode Global Config
Utility Commands 313

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Use this command to configure an NFS mount point in order to dump core file to the NFS file
system.
Default None
Format exception dump nfs ip-address/dir
Mode Global Config
no exception dump nfs
Use this command to reset the exception dump NFS mount point configuration to its factory
default value.
Format no exception dump nfs
Mode Global Config
exception dump filepath
Use this command to configure a file-path to dump core file to a TFTP server, FTP server,
NFS mount, or USB device subdirectory.
Default None
Format exception dump filepath dir
Mode Global Config
no exception dump filepath
Use this command to reset the exception dump filepath configuration to its factory default
value.
Format no exception dump filepath
Mode Global Config
exception dump compression
Use this command to enable compression mode.
Default Enabled
Format exception dump compression
Mode Global Config
Utility Commands 314

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no exception dump compression
This command disables compression mode.
Format no exception dump compression
Mode Global Config
exception dump stack-ip-address protocol
This command configures the protocol (DHCP or static) that is used to configure the service
port after a unit crashed. If you specify dhcp, the unit receives its IP address from a DHCP
server that must be available in the network.
Default dhcp
Format exception dump stack-ip-address protocol {dhcp | static}
Mode Global Config
no exception dump stack-ip-address protocol
This command resets the stack IP protocol configuration to its default value (dhcp).
Format no exception dump stack-ip-address protocol
Mode Global Config
exception dump stack-ip-address add
Use this command to add a static IP address that is assigned to an individual unit’s service
port in a stack after the unit crashed. This IP address is used to perform the core dump.
Default None
Format exception dump stack-ip-address add ip-address netmask [gateway]
Mode Global Config
exception dump stack-ip-address remove
Use this command to remove a stack IP address configuration. If this IP address is assigned
to any unit in a stack then, the IP address is removed from the unit.
Format no exception dump stack-ip-address remove ip-address netmask
Mode Global Config
exception core-file
Use this command to configure a prefix for a core-file name. The core file name is generated
with the prefix as follows:
Utility Commands 315

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If hostname is selected:
file-name-prefix_hostname_Time_Stamp.bin
If hostname is not selected:
file-name-prefix_MAC_Address_Time_Stamp.bin
If hostname is configured the core file name takes the host name, otherwise the core-file
names uses the MAC address when generating a core dump file. The prefix length is 15
characters.
Default Core
Format exception core-file {file-name-prefix | [hostname] | [time-stamp]}
Mode Global Config
no exception core-file
Use this command to reset the exception core file prefix configuration to its factory default
value. The hostname and time-stamp are disabled.
Format no exception core-file
Mode Global Config
exception switch-chip-register
Use this command to enable or disable the switch-chip-register dump in case of an
exception. The switch-chip-register dump occurs only for the master and not for members.
Default Disable
Format exception switch-chip-register {enable | disable}
Mode Global Config
write core
Use this command to generate a core dump file on demand. The write core test
command is helpful when testing the core dump setup. For example, if the TFTP protocol is
configured, write core test communicates with the TFTP server and informs the user if
the TFTP server can be contacted. Similarly, if the protocol is configured as nfs, this
command mounts and unmounts the file system and informs the user of the status.
Note: The write core command reloads the switch which is useful when
the device malfunctions, but has not crashed.
Utility Commands 316
