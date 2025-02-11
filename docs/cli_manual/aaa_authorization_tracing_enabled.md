# aaa_authorization_tracing_enabled

Pages: 289-293

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #debug aaa authorization
Tacacs authorization receive packet tracing enabled.
(NETGEAR Switch) #debug tacacs authorization packet transmit
authorization tracing enabled.
(NETGEAR Switch) #no debug aaa authorization
AAA authorization tracing enabled
(NETGEAR Switch) #
debug arp
Use this command to enable ARP debug protocol messages.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug arp
Mode Privileged EXEC
no debug arp
Use this command to disable ARP debug protocol messages.
Format no debug arp
Mode Privileged EXEC
debug authentication
This command displays either the debug trace for either a single event or all events for an
interface.
Note: To display the debug trace, enable the debug console command.
Default none
Format debug authentication packet {all | event} interface unit/slot/port
Mode Privileged EXEC
Utility Commands 289

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
debug auto-voip
Use this command to enable Auto VoIP debug messages. Use the optional parameters to
trace H323, SCCP, SIP, OUI packets respectively.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug auto-voip [H323 | SCCP |SIP | oui]
Mode Privileged EXEC
no debug auto-voip
Use this command to disable Auto VOIP debug messages.
Format no debug auto-voip
Mode Privileged EXEC
debug clear
This command disables all previously enabled “debug” traces.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug clear
Mode Privileged EXEC
debug console
This command enables the display of “debug” trace output on the login session in which it is
executed. Debug console display must be enabled in order to view any trace output. The
output of debug trace commands will appear on all login sessions for which debug console
has been enabled. The configuration of this command remains in effect for the life of the login
session. The effect of this command is not persistent across resets.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug console
Mode Privileged EXEC
Utility Commands 290

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no debug console
This command disables the display of “debug” trace output on the login session in which it is
executed.
Format no debug console
Mode Privileged EXEC
debug crashlog
Use this command to view information contained in the crash log file that the system
maintains when it experiences an unexpected reset. The crash log file contains the following
information:
• Call stack information in both primitive and verbose forms
• Log Status
• Buffered logging
• Event logging
• Persistent logging
• System Information (output of sysapiMbufDump)
• Message Queue Debug Information
• Memory Debug Information
• Memory Debug Status
• OS Information (output of osapiShowTasks)
• process information (meminfo, cpuinfo, interrupts, version and net/sockstat)
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug crashlog {proc |verbose | deteteall | [kernel] crashlog-number [upload
url]| data crashlog-number [download url | upload url | component-id
item-number additional-parameter]} [unit unit]
Mode Privileged EXEC
Parameter Description
kernel View the crash log file for the kernel
crashlog-number Specifies the file number to view. The system maintains up to four copies, and the valid range
i s 1– 4.
upload url To upload the crash log (or crash dump) to a TFTP server, use the upload keyword and
specify the required TFTP server information.
proc View the application process crashlog.
Utility Commands 291

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
verbose Enable the verbose crashlog.
deleteall Delete all crash log files on the system.
data Crash log data recorder.
crashdump-number Specifies the crash dump number to view. T he valid range is 0– 2.
download url To download a crash dump to the switch, use the download keyword and specify the
required TFTP server information.
component-id The ID of the component that caused the crash.
item-number The item number.
additional-parameter Additional parameters to include.
unit The unit number for the unit on which the crashlog is located.
debug debug-config
Use this command to download or upload the debug-config.ini file. The debug-config. ini file
executes CLI commands (including devshell and drivshell commands) on specific predefined
events. The debug config file is created manually and downloaded to the switch.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug debug-config {download url | upload url}
Mode Privileged EXEC
debug dhcp packet
This command displays “debug” information about DHCPv4 client activities and traces
DHCPv4 packets to and from the local DHCPv4 client.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug dhcp packet [transmit | receive]
Mode Privileged EXEC
Utility Commands 292

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no debug dhcp
This command disables the display of “debug” trace output for DHCPv4 client activity.
Format no debug dhcp packet [transmit | receive]
Mode Privileged EXEC
debug dot1x packet
Use this command to enable dot1x packet debug trace.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug dot1x
Mode Privileged EXEC
no debug dot1x packet
Use this command to disable dot1x packet debug trace.
Format no debug dot1x
Mode Privileged EXEC
debug igmpsnooping packet
This command enables tracing of IGMP Snooping packets received and transmitted by the
switch.
Note: To display the debug trace, enable the debug console command.
Default disabled
Format debug igmpsnooping packet
Mode Privileged EXEC
no debug igmpsnooping packet
This command disables tracing of IGMP Snooping packets.
Format no debug igmpsnooping packet
Mode Privileged EXEC
Utility Commands 293
