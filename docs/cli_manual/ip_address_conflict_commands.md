# ip_address_conflict_commands

Pages: 284-288

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Configured host name-to-address mapping:
Host Addresses
------------------------------ ------------------------------
accounting.gm.com 176.16.8.8
Host Total Elapsed T ype Addresses
- -------------- - ------- - ----- -------- ---------------
w ww.stanford.edu 72 3 IP 171.64.14.203
IP Address Conflict Commands
The commands in this section help troubleshoot IP address conflicts.
ip address-conflict-detect run
This command triggers the switch to run active address conflict detection by sending
gratuitous ARP packets for IPv4 addresses on the switch.
Format ip address-conflict-detect run
Mode Global Config
show ip address-conflict
This command displays the status information corresponding to the last detected address
conflict.
Format show ip address-conflict
Modes Privileged EXEC
Term Definition
Address Conflict Detection Status Identifies whether the switch has detected an address conflict on any IP address.
Last Conflicting IP Address The IP Address that was last detected as conflicting on any interface.
Last Conflicting MAC Address The MAC Address of the conflicting host that was last detected on any interface.
Time Since Conflict Detected The time in days, hours, minutes and seconds since the last address conflict was
detected.
Utility Commands 284

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
clear ip address-conflict-detect
This command clears the detected address conflict status information.
Format clear ip address-conflict-detect
Modes Privileged EXEC
Serviceability Packet Tracing Commands
These commands improve the capability to diagnose conditions that affect the switch.
CAUTION:
The output of debug commands can be long and may adversely affect
system performance.
capture start
Use the capture start command to manually start capturing CPU packets for packet
trace.
The packet capture operates in three modes:
• capture file
• remote capture
• capture line
The command is not persistent across a reboot cycle.
Format capture start [all | receive | transmit]
Mode Privileged EXEC
Parameter Description
all Capture all traffic.
receive Capture only received traffic.
transmit Capture only transmitted traffic.
capture stop
Use the capture stop command to manually stop capturing CPU packets for packet trace.
Format capture stop
Mode Privileged EXEC
Utility Commands 285

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
capture {file | remote | line | usb}
Use this command to configure file capture options. The command is persistent across a
reboot cycle.
Format capture {file | remote | line | usb}
Mode Global Config
Parameter Description
file In the capture file mode, the captured packets are stored in a file on NVRAM. The maximum file size
defaults to 524288 bytes. The switch can transfer the file to a TFTP server via TFTP, SFTP, SCP via
CLI, and SNMP.
The file is formatted in pcap format, is named cpuPktCapture.pcap, and can be examined using
network analyzer tools such as Wireshark® or Ethereal®. Starting a file capture automatically
terminates any remote capture sessions and line capturing. After the packet capture is activated, the
capture proceeds until the capture file reaches its maximum size, or until the capture is stopped
manually using the CLI command capture stop.
remote In the remote capture mode, the captured packets are redirected in real time to an external PC
running the Wireshark tool for Microsoft® Windows®. A packet capture server runs on the switch
side and sends the captured packets via a TCP connection to the Wireshark tool.
The remote capture can be enabled or disabled using the CLI. There should be a Windows PC with
the Wireshark tool to display the captured file. When using the remote capture mode, the switch
does not store any captured data locally on its file system.
You can configure the IP port number for connecting Wireshark to the switch. The default port
number is 2002. If a firewall is installed between the Wireshark PC and the switch, then these ports
must be allowed to pass through the firewall. You must configure the firewall to allow the Wireshark
PC to initiate TCP connections to the switch.
If the client successfully connects to the switch, the CPU packets are sent to the client PC, then
Wireshark receives the packets and displays them. This continues until the session is terminated by
either end.
Starting a remote capture session automatically terminates the file capture and line capturing.
line In the capture line mode, the captured packets are saved into the RAM and can be displayed on the
CLI. Starting a line capture automatically terminates any remote capture session and capturing into
a file. There is a maximum 128 packets of maximum 128 bytes that can be captured and displayed
in line mode.
usb In the usb mode, the captured packets are stored in a file on USB device.
capture remote port
Use this command to configure file capture options. The command is persistent across a
reboot cycle. The id argument is a T CP port number from 1024– 49151.
Format capture remote port id
Mode Global Config
Utility Commands 286

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
capture file size
Use this command to configure file capture options. The command is persistent across a
reboot cycle. The max-file-size argument is the maximum size the pcap file can reach,
which is 2– 512 KB.
Format capture file size max file size
Mode Global Config
capture line wrap
This command enables wrapping of captured packets in line mode when the captured
packets reaches full capacity.
Format capture line wrap
Mode Global Config
no capture line wrap
This command disables wrapping of captured packets and configures capture packet to stop
when the captured packet capacity is full.
Format no capture line wrap
Mode Global Config
capture usb
This command sets a file name on a USB device as the destination for the capture of CPU
packets.
Format capture usb filename
Mode Global Config
show capture packets
Use this command to display packets captured and saved to RAM. It is possible to capture
and save into RAM, packets that are received or transmitted through the CPU. A maximum
128 packets can be saved into RAM per capturing session. A maximum 128 bytes per packet
can be saved into the RAM. If a packet holds more than 128 bytes, only the first 128 bytes
are saved; data more than 128 bytes is skipped and cannot be displayed in the CLI.
Utility Commands 287

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Capturing packets is stopped automatically when 128 packets are captured and have not yet
been displayed during a capture session. Captured packets are not retained after a reload
cycle.
Format show capture packets
Mode Privileged EXEC
debug aaa accounting
This command is useful to debug accounting configuration and functionality in User Manager
Note: To display the debug trace, enable the debug console command.
Format debug aaa accounting
Mode Privileged EXEC
no debug aaa accounting
Use this command to turn off debugging of User Manager accounting functionality.
Format no debug aaa accounting
Mode Privileged EXEC
debug aaa authorization
Use this command to enable the tracing for AAA in User Manager. This is useful to debug
authorization configuration and functionality in the User Manager. Each of the parameters are
used to configure authorization debug flags.
Note: To display the debug trace, enable the debug console command.
Format debug aaa authorization [commands | exec]
Mode Privileged EXEC
no debug aaa authorization
Use this command to turn off debugging of the User Manager authorization functionality.
Format no debug aaa authorization
Mode Privileged EXEC
Utility Commands 288
