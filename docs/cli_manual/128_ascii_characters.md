# 128 ASCII characters.

Pages: 181-214

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 9. Parameters for a cloud management agent (continued)
Parameter Description Range Default
Proxy Password The password for the An ASCII string from 1 to 64 characters in “”
designated user name. plain text (that is, unencrypted) format.
Alternatively, the user can supply an
AES-encrypted password string of exactly
128 ASCII characters.
The empty string “” is used to specify that
this parameter is not set.
Server URL A URL string that identifies An ASCII string from 1 to 150 characters “”
network access to a specific that contains the information that is
cloud server. described by the agent provider.
Note: The content of this string is not
checked by the switch. An agent performs
its own URL string validation.
The empty string “” is used to specify that
this parameter is not set.
cloud-managed
Use this command to enter Cloud Managed configuration mode, which lets you the change
the cloud managed parameters.
Format cloud managed
Mode Global Config
enable
This command administratively enables a cloud management agent to perform its intended
operation, including initiating network requests to the agent’s cloud server.
Note: Entering the cloud-managed command to enable Cloud Managed
mode does not activate a cloud management agent, which must be
independently installed and started as a process on the switch.
A running agent periodically checks if this mode is enabled before it
communicates with its cloud server.
Format enable
Mode Cloud Managed Mode
no enable
This command administratively disables a cloud management agent.
If a cloud management agent is administratively disabled, it continues to run in a quiet state
in which no network communication or parameter changes are allowed.
Management Commands 181

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format no enable
Mode Cloud Managed Mode
proxy-ip-address
This command defines the parameters that let a cloud management agent communicate
through a proxy server that is used to access a public network.
Some private or corporate networks restrict access to a public network by forcing all traffic
through a designated gateway device (also referred to as a proxy server), which is identified
by its IP address and usually by a specific TCP or UDP port number. In addition, access to
the proxy server might require valid login credentials in the form of a user name and
password.
The command syntax allows you to enter a password as either an ASCII string in plain text of
up to 64 characters or as an AES-encrypted ASCII string of precisely 128 characters.
Note: The switch stores this password internally as AES-encrypted and does
not display it unencrypted in plain text format.
Format proxy-ip-address {ipv4-address | ipv6-address} [port port-number] [username
username] [password [0 | 7] password]
Mode Cloud Managed Mode
Parameter Description
ipv4-address The IP address of the proxy server, which can be in either IPv4 or IPv6 format.
ipv6-address
port number The TCP or UDP port number that is used to access the proxy server. Valid values are from 1 to
65535. The default value is 0, which specifies that this configuration value is not set.
username The proxy server login user name that must be from 1 to 64 characters in length.
[0 | 7] This option let you specify the type of password:
• 0. unencrypted
• 7. AES-encrypted
If you do not specify this option, an AES-encrypted password is assumed.
password The password that must be entered together with the user name to log in to the proxy server. If you
enter an encrypted password, it must already be encrypted using AES.
The allowed password length depends on the type of password:
• unencrypted. 1 to 64 characters
• encrypted. 128 characters
Management Commands 182

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no proxy-ip-address
This command removes the proxy server configuration parameters from the switch and
restores the default values (see Ta ble9 on page180).
Format no proxy-ip-address
Mode Cloud Managed Mode
url
This command defines a URL string that is used by a cloud management agent to contact its
cloud server in the public network. The format of the URL string is agent-specific. The string
can be from 1 to 150 characters.
Note: The switch does not validate the contents of the specified URL string.
The cloud management agent process might perform its own validity
checking of the URL string.
Format url
Mode Cloud Managed Mode
no url
This command removes the cloud management server URL string from the switch.
Format no url
Mode Cloud Managed Mode
show cloud-managed
This command displays the cloud managed configuration parameters. A parameter
that is not configured is displayed as a series of dashes (-----).
Format show cloud-managed
Mode User EXEC
Privileged EXEC
Field Description
Administrative Indicates whether the cloud managed operation is enabled or disabled. The default is disabled.
Mode
Proxy IP Address The IPv4 or IPv6 address of the proxy server that is used to access the public network.
Management Commands 183

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Description
Proxy IP Port The TCP or UDP port number of the proxy server that is used to access the public network.
Number
Proxy User Name The user name that provides access to the proxy server.
Proxy Password Indicates AES if the password is encrypted. (This is the password that provides access to the proxy
Encryption server.) The actual password (encrypted or unencrypted) is not displayed.
Server URL The URL that the cloud management agent uses to contact its cloud server. This is a free-formatted
string that is agent-specific.
Command example:
The following example shows Cloud Managed mode enabled, a proxy server configured, and
no cloud server URL specified.
(NETGEAR Switch) #show cloud-managed
Administrative Mode ........................... Enabled
Proxy IP Address .............................. 192.168.10.5
Proxy IP Port Number .......................... 1647
Proxy User Name ............................... bob
Proxy Password Encryption ..................... AES
Server URL .................................... -----
Application Commands
Application commands enable you to manage applications that run on the switch.
application install
This command specifies how an executable file must start an application on the switch and
how the application must run on the switch. You can enter the command (that is, preconfigure
the command) for an executable file that is not yet present on the switch. The configuration
does not take into effect until the executable file is present on the switch.
Format application install filename [start-on-boot] [auto-restart] [cpu-sharing
number] [max-megabytes megabytes]
Mode Global Config
Management Commands 184

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
filename The name of the file that contains the executable or script that is started as a Linux process for the
application.
start-on-boot Starts the application each time the switch boots. When you specify this keyword, the application
start the first time that the switch boots after you saved the command.
auto-restart Automatically restarts the application’s processes if they stop running.
cpu-sharing Sets the CPU share allocated to this application. For the number argument, enter a number from 0
number to 99 that represents a percentage. If you leave the default of 0, the CPU share for the application
processes is not limited.
Max-megabytes Sets the maximum memory resource that the application processes can consume. For the
megabytes megabyytes argument, enter a number from 0 to 200 that represents MB. If you leave the default
of 0, the memory resources for the application processes are not limited.
no application install
This command removes the execution configuration for an application on the switch. If the
application is running, all processes associated with the application are stopped
automatically.
Format no application install filename
Mode Global Config
application start
This command starts the execution of a specified application. The application must be
installed on the switch before it can be started using this command.
Format application start filename
Mode Global Config
no application start
This command stops the execution of a specified application.
Format no application start filename
Mode Global Config
Management Commands 185

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
erase application
Use this command to erase an executable application file that is stored in nonvolatile memory
on the switch.
Format erase application filename
Mode Global Config
show application
This command displays the applications that are installed on the switch and execution
configurations of the applications.
Format show application
Mode Privileged EXEC
Field Description
filename The name of the application.
start-on-boot Indicates whether the application is configured to start when the switch boots:
• Yes. The application starts when the switch boots.
• No. The application does not start when the switch boots.
auto-restart Indicates whether the application is configured to restart when the application process stops:
• Yes. The application restarts when the application process stops.
• No. The application does not restart when the application process stops.
max-CPU-Util The command application CPU utilization limit expressed as a percentage. If the utilization is not
limited, None is displayed.
max-Memory The application memory usage limit in megabytes. If the memory usage is not limited, None is
displayed.
show application files
This command displays the files in the application directory of the switch file system.
Format show application files
Mode Privileged EXEC
Field Description
filename The name of the application.
file size The number of bytes that the file uses in the file system.
directory size The number of bytes that all files in the application directory use.
Management Commands 186

Utility Commands

This chapter describes the utility commands.
The chapter includes the following sections:
• AutoInstall Commands
• CLI Output Filtering Commands
• Dual Image Commands
• System Information and Statistics Commands
• Logging Commands
• Email Alerting and Mail Server Commands
• System Utility and Clear Commands
• Simple Network Time Protocol Commands
• Time Zone Commands
• DHCP Server Commands
• DNS Client Commands
• IP Address Conflict Commands
• Serviceability Packet Tracing Commands
• Cable Test Command
• Power Management Commands
• USB commands
• sFlow Commands
• Switch Database Management Template Commands
• Green Ethernet Commands
• Remote Monitoring Commands
• Statistics Application Commands

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The commands in this chapter are in one of four functional groups:
• Show commands. Display switch settings, statistics, and other information.
• Configuration commands. Configure features and options of the switch. For every
configuration command, there is a show command that displays the configuration setting.
• Copy commands. Transfer or save configuration and informational files to and from the
switch.
• Clear commands. Clear some or all of the settings to factory defaults.
AutoInstall Commands
The AutoInstall feature enables the automatic update of the image and configuration of the
switch. This feature enables touchless or low-touch provisioning to simplify switch
configuration and imaging.
AutoInstall includes the following support:
• Downloading an image from TFTP server using DHCP option 125. The image update can
result in a downgrade or upgrade of the firmware on the switch.
• Automatically downloading a configuration file from a TFTP server when the switch is
booted with no saved configuration file.
• Automatically downloading an image from a TFTP server in the following situations:
- When the switch is booted with no saved configuration found.
- When the switch is booted with a saved configuration that has AutoInstall enabled.
When the switch boots and no configuration file is found, it attempts to obtain an IP address
from a network DHCP server. The response from the DHCP server includes the IP address of
the TFTP server where the image and configuration flies are located.
After acquiring an IP address and the additional relevant information from the DHCP server,
the switch downloads the image file or configuration file from the TFTP server. A downloaded
image is automatically installed. A downloaded configuration file is saved to non-volatile
memory.
Note: AutoInstall from a TFTP server can run on any IP interface, including
the network port, service port, and in-band routing interfaces (if
supported). To support AutoInstall, the DHCP client is enabled
operationally on the service port, if it exists, or the network port, if
there is no service port.
Utility Commands 188

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
boot autoinstall
Use this command to operationally start or stop the AutoInstall process on the switch. The
command is non-persistent and is not saved in the startup or running configuration file.
Default stop
Format boot autoinstall {start | stop}
Mode Privileged EXEC
boot host retrycount
Use this command to set the number of attempts to download a configuration file from the
TFTP server. The number argument is a number in the range 1–3.
Default 3
Format boot host retrycount number
Mode Privileged EXEC
no boot host retrycount
Use this command to set the number of attempts to download a configuration file to the
default value.
Format no boot host retrycount
Mode Privileged EXEC
boot host dhcp
Use this command to enable AutoInstall on the switch for the next reboot cycle. The
command does not change the current behavior of AutoInstall and saves the command to
NVRAM.
Default enabled
Format boot host dhcp
Mode Privileged EXEC
no boot host dhcp
Use this command to disable AutoInstall for the next reboot cycle.
Format no boot host dhcp
Mode Privileged EXEC
Utility Commands 189

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
boot host autosave
Use this command to automatically save the downloaded configuration file to the
startup-config file on the switch. When autosave is disabled, you must explicitly save the
downloaded configuration to non-volatile memory by using the write memory or copy
system:running-config nvram:startup-config command. If the switch reboots
and the downloaded configuration has not been saved, the AutoInstall process begins, if the
feature is enabled.
Default disabled
Format boot host autosave
Mode Privileged EXEC
no boot host autosave
Use this command to disable automatically saving the downloaded configuration on the
switch.
Format no boot host autosave
Mode Privileged EXEC
boot host autoreboot
Use this command to allow the switch to automatically reboot after successfully downloading
an image. When auto reboot is enabled, no administrative action is required to activate the
image and reload the switch.
Default enabled
Format boot host autoreboot
Mode Privileged EXEC
no boot host autoreboot
Use this command to prevent the switch from automatically rebooting after the image is
downloaded by using the AutoInstall feature.
Format no boot host autoreboot
Mode Privileged EXEC
erase startup-config
Use this command to erase the text-based configuration file stored in non-volatile memory. If
the switch boots and no startup-config file is found, the AutoInstall process automatically
begins.
Utility Commands 190

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format erase startup-config
Mode Privileged EXEC
erase factory-defaults
This command erases the text-based factory default file that is stored in non-volatile memory.
Format erase factory-defaults
Mode Privileged EXEC
erase stack-config
This command erases the stacking configuration file This configuration file cannot be erased
using the clear config command.
Format erase stack-config
Mode Privileged EXEC
show autoinstall
This command displays the current status of the AutoInstall process.
Format show autoinstall
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show autoinstall
AutoInstall Mode............................... Stopped
AutoInstall Persistent Mode.................... Disabled
AutoSave Mode.................................. Disabled
AutoReboot Mode................................ Enabled
AutoInstall Retry Count........................ 3
Utility Commands 191

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
CLI Output Filtering Commands
show “command” | include “string”
The command show command (that is, you must enter a keyword of an existing show
command for the command parameter) is executed and the output is filtered to display only
lines containing the string match. All other non-matching lines in the output are
suppressed.
Command example:
(NETGEAR Switch) #show running-config | include “spanning-tree”
spanning-tree configuration name "00-02-BC-42-F9-33"
spanning-tree bpduguard
spanning-tree bpdufilter default
show “command” | include “string” exclude “string2”
The command show command (that is, you must enter a keyword of an existing show
command for the command parameter) is executed and the output is filtered to only show
lines containing the string match and not containing the string2 match. All other
non-matching lines in the output are suppressed. If a line of output contains both the include
and exclude strings then the line is not displayed.
Command example:
(NETGEAR Switch) #show running-config | include “spanning-tree” exclude “configuration”
spanning-tree bpduguard
spanning-tree bpdufilter default
show “command” | exclude “string”
The command show command (that is, you must enter a keyword of an existing show
command for the command parameter) is executed and the output is filtered to show all lines
not containing the string match. Output lines containing the string match are
suppressed.
Command example:
(NETGEAR Switch) #show interface 0/1
Packets Received Without Error................. 0
Packets Received With Error.................... 0
Broadcast Packets Received..................... 0
Receive Packets Discarded...................... 0
Packets Transmitted Without Errors............. 0
Utility Commands 192

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Transmit Packets Discarded..................... 0
Transmit Packet Errors......................... 0
Collision Frames............................... 0
Time Since Counters Last Cleared............... 281 day 4 hr 9 min 0 sec
Command example:
(NETGEAR Switch) #show interface 0/1 | exclude “Packets”
Transmit Packet Errors......................... 0
Collision Frames............................... 0
Time Since Counters Last Cleared............... 20 day 21 hr 30 min 9 sec
show “command” | begin “string”
The command show command (that is, you must enter a keyword of an existing show
command for the command parameter) is executed and the output is filtered to show all lines
beginning with and following the first line containing the string match. All prior lines are
suppressed.
Command example:
(NETGEAR Switch) #show port all | begin “1/1”
1/1 Enable Down Disable N/A N/A
1/2 Enable Down Disable N/A N/A
1/3 Enable Down Disable N/A N/A
1/4 Enable Down Disable N/A N/A
1/5 Enable Down Disable N/A N/A
1/6 Enable Down Disable N/A N/A
show “command” | section “string”
The command show command (that is, you must enter a keyword of an existing show
command for the command parameter) is executed and the output is filtered to show only
lines included within the section(s) identified by lines containing the string match and
ending with the first line containing the default end-of-section identifier (that is, exit).
Command example:
(NETGEAR Switch) #show running-config | section “interface 0/1”
interface 0/1
no spanning-tree port mode
exit
Utility Commands 193

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show “command” | section “string” “string2”
The command show command (that is, you must enter a keyword of an existing show
command for the command parameter) is executed and the output is filtered to only show
lines included within the section(s) identified by lines containing the string match and
ending with the first line containing the string2 match. If multiple sessions matching the
specified string match criteria are part of the base output, then all instances are displayed.
show “command” | section “string” include “string2”
The command show command (that is, you must enter a keyword of an existing show
command for the command parameter) is executed and the output is filtered to only show
lines included within the section(s) identified by lines containing the string match and
ending with the first line containing the default end-of-section identifier (that is, exit) and
that include the string2 match. This type of filter command could also include “exclude” or
user-defined end-of-section identifier parameters as well.
Dual Image Commands
The switch supports a dual image feature that allows the switch to have two software images
in the permanent storage. You can specify which image is the active image to be loaded in
subsequent reboots. This feature allows reduced down-time when you upgrade or
downgrade the software.
delete
This command deletes the image1 or image 2 file from the permanent storage. The optional
unit parameter is valid only for members. The unit parameter identifies the member on
which you must execute this command. When you do not enter this parameter, the command
is executed on all members in the stack.
Format delete [unit] {image1 | image2}
Mode Privileged EXEC
boot system
This command activates the specified image. It will be the active-image for subsequent
reboots and will be loaded by the boot loader. The current active-image is marked as the
backup-image for subsequent reboots. If the specified image doesn't exist on the system, this
command returns an error message. The optional unit parameter identifies the member on
which you must execute this command. When you do not enter this parameter, the command
is executed on all members in the stack.
Format boot system [unit] {image1 | image2}
Mode Privileged EXEC
Utility Commands 194

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show bootvar
This command displays the version information and the activation status for the current
images on the supplied unit of the stack. If you do not specify a unit number, the command
displays image details for all nodes in the stack. The command also displays any text
description associated with an image. This command, when used on a standalone system,
displays the switch activation status. For a standalone system, the unit parameter is not valid.
Format show bootvar [unit]
Mode Privileged EXEC
filedescr
This command associates a given text description with an image and replaces any existing
description. The command is executed on all units in a stack.
Format filedescr {image1 | image2} text-description
Mode Privileged EXEC
update bootcode
This command updates the bootcode (boot loader) on the switch. The bootcode is read from
the active image for subsequent reboots. The unit parameter identifies the member on
which this command must be executed. When this parameter is not supplied, the command
is executed on all units in a stack.
Format update bootcode [unit]
Mode Privileged EXEC
System Information and Statistics
Commands
This section describes the commands you use to view information about system features,
components, and configurations.
show arp switch (system information and statistics commands)
This command displays the contents of the Address Resolution Protocol (ARP) table that is
associated with the IP address of the switch. This IP address learns only ARP entries that are
associated with the management interfaces (network or service ports). ARP entries that are
associated with routing interfaces are not listed.
Utility Commands 195

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format show arp switch
Mode Privileged EXEC
Term Definition
IP Address IP address of the management interface or another device on the management network.
MAC Address Hardware MAC address of that device.
Interface For a service port the output is Management. For a network port, the output is the
unit/slot/port of the physical interface.
show eventlog
This command displays the event log, which contains error messages from the system. The
event log is not cleared on a system reset. The unit is the switch identifier.
Format show eventlog [unit]
Mode Privileged EXEC
Term Definition
File The file in which the event originated.
Line The line number of the event.
Task Id The task ID of the event.
Code The event code.
Time The time this event occurred.
Unit The unit for the event.
Note: Event log information is retained across a switch reset.
show hardware
This command displays inventory information for the switch.
Note: The show version command and the show hardware command
display the same information. In future releases of the software, the
show hardware command will not be available. For a description of
the command output, see the command show version on page197.
Utility Commands 196

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format show hardware
Mode Privileged EXEC
show environment
This command displays information about the temperature and status of the power supplies
and fans in the system chassis.
Format show environment
Mode Privileged EXEC
Command example:
(Netgear Switch) #show environment
Temp (C)....................................... 30
Temperature traps range: 0 to 90 degrees (Celsius)
Temperature Sensors:
Unit Sensor Description Temp (C) State Max_Temp (C)
---- ------ ---------------- ---------- -------------- --------------
1 1 System 30 Normal 31
Fans:
Unit Fan Description Type Speed Duty level State
---- --- -------------- --------- ------------- ------------- --------------
1 1 System1 Fixed 9200 39 Operational
1 2 System2 Fixed 9200 39 Operational
1 3 Power1 Fixed 9200 39 Operational
1 4 Power2 Fixed 8300 39 Operational
Power supplies:
Unit Power supply Description Type State
---- ------------ ---------------- ---------- --------------
1 1 AC-1 Removable Operational
1 2 AC-2 Removable Not present
show version
This command displays inventory information for the switch.
Note: The show version command replaces the show hardware
command in future releases of the software.
Utility Commands 197

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format show version
Mode Privileged EXEC
Term Definition
System Description Text used to identify the product name of this switch.
Machine Model The machine model as defined by the Vital Product Data
Serial Number The unique serial number for this switch.
Burned in MAC The universally assigned network address.
Address
Software Version The release version number of the code running on the switch.
Boot Code Version The version of the boot code software running on the switch.
CPLD Version The version of the CPLD firmware running on the switch.
Supported Java Plugin The software version of the Java plugin running on the switch.
Version
Current Time The current time on the running on the switch.
show platform vpd
This command displays vital product data for the switch.
Format show platform vpd
Mode User Privileged
The following information is displayed.
Term Definition
Operational Code Build Signature loaded into the switch
Image File Name
Software Version Release Version Maintenance Level and Build (RVMB) information of the switch.
Timestamp Timestamp at which the image is built
Command example:
(NETGEAR Switch) #show platform vpd
Operational Code Image File Name...............
NETGEAR-Ent-esw-xgs4-gto-BL20R-CS-6AIQHSr3v7m14b35
Software Version............................... 3.7.14.35
Timestamp...................................... Thu Mar 7 14:36:14 IST 2013
Utility Commands 198

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show interface
This command displays a summary of statistics for a specific interface or a count of all CPU
traffic based upon the argument.
Format show interface {unit/slot/port | switchport}
Mode Privileged EXEC
The display parameters, when the argument is unit/slot/port, are as follows.
Field Definition
Packets Received The total number of packets (including broadcast packets and multicast packets) received by the
Without Error processor.
Packets Received The number of inbound packets that contained errors preventing them from being deliverable to a
With Error higher-layer protocol.
Broadcast Packets The total number of packets received that were directed to the broadcast address. Note that this
Received does not include multicast packets.
Receive Packets The number of inbound packets which were chosen to be discarded even though no errors had been
Discarded detected to prevent their being deliverable to a higher-layer protocol. One possible reason for
discarding such a packet could be to free up buffered space.
Packets The total number of packets transmitted out of the interface.
Transmitted
Without Error
Transmit Packets The number of outbound packets which were chosen to be discarded even though no errors had
Discarded been detected to prevent their being deliverable to a higher-layer protocol. A possible reason for
discarding a packet could be to free up buffer space.
Transmit Packets The number of outbound packets that could not be transmitted because of errors.
Errors
Collisions Frames The best estimate of the total number of collisions on this Ethernet segment.
Number of link The number of down events for the link since the switch restarted.
down events
Load Interval The period in seconds for which data is used to compute the load statistics. You must enter a that is
a multiple of 30. The allowable range is from 30 to 600 seconds.
Received Rate The approximate number of bits per second received. This value is an exponentially-weighted
(Mbps) average and is affected by the configured load interval.
Transmitted Rate The approximate number of bits per second transmitted. This value is an exponentially-weighted
(Mbps) average and is affected by the configured load interval.
Received Error The approximate number of error bits per second received. This value is an exponentially-weighted
Rate average and is affected by the configured load interval.
Transmitted Error The approximate number of error bits per second transmitted. This value is an
Rate exponentially-weighted average and is affected by the configured load interval.
Utility Commands 199

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Definition
Packets Per The approximate number of packets per second received. This value is an exponentially-weighted
Second Received average and is affected by the configured load interval.
Packets Per The approximate number of packets per second transmitted. This value is an exponentially-weighted
Second average and is affected by the configured load interval.
Transmitted
Link Flaps The number of up and down events for the link since the switch restarted.
Time Since The elapsed time, in days, hours, minutes, and seconds since the statistics for this port were last
Counters Last cleared.
Cleared
The display parameters, when the argument is switchport are as follows.
Term Definition
Packets Received Without Error The total number of packets (including broadcast packets and multicast packets)
received by the processor.
Broadcast Packets Received The total number of packets received that were directed to the broadcast address.
Note that this does not include multicast packets.
Packets Received With Error The number of inbound packets that contained errors preventing them from being
deliverable to a higher-layer protocol.
Packets Transmitted Without Error The total number of packets transmitted out of the interface.
Broadcast Packets Transmitted The total number of packets that higher-level protocols requested to be transmitted to
the Broadcast address, including those that were discarded or not sent.
Transmit Packet Errors The number of outbound packets that could not be transmitted because of errors.
Time Since Counters Last Cleared The elapsed time, in days, hours, minutes, and seconds since the statistics for this
switch were last cleared.
show interfaces status
Use this command to display interface information, including the description, port state,
speed and autonegotiation capabilities. The command is similar to show port all but
displays additional fields like interface description and port-capability.
The description of the interface is configurable through the existing command description
name which has a maximum length of 64 characters that is truncated to 28 characters in the
output. The long form of the description can be displayed using show port description.
The interfaces displayed by this command are physical interfaces, LAG interfaces and VLAN
routing interfaces.
Format show interfaces status [unit/slot/port]
Mode Privileged EXEC
Utility Commands 200

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Description
Port The interface that is associated with the displayed information.
Name The descriptive user-configured name for the interface.
Link State Indicates whether the link is up or down.
Physical Mode The speed and duplex settings on the interface.
Physical Status Indicates the port speed and duplex mode for physical interfaces. The physical
status for LAGs is not reported. When a port is down, the physical status is unknown.
Media Type The media type of the interface.
Flow Control Status The 802.3x flow control status.
Flow Control The configured 802.3x flow control mode.
show interface ethernet
This command displays detailed statistics for a specific interface or for all CPU traffic based
upon the argument.
Format show interface ethernet {unit/slot/port | switchport | all}
Mode Privileged EXEC
When you specify a value for unit/slot/port, the command displays the following
information.
Term Definition
Packets Received Total Packets Received (Octets) - The total number of octets of data (including those in bad
packets) received on the network (excluding framing bits but including Frame Check Sequence
(FCS) octets). This object can be used as a reasonable estimate of Ethernet utilization. If greater
precision is desired, the etherStatsPkts and etherStatsOctets objects should be sampled before and
after a common interval. The result of this equation is the value Utilization which is the percent
utilization of the Ethernet segment on a scale of 0 to 100 percent.
Packets Received 64 Octets - The total number of packets (including bad packets) received that
were 64 octets in length (excluding framing bits but including FCS octets).
Packets Received 65–127 Octets - The total number of packets (including bad packets) received
that were between 65 and 127 octets in length inclusive (excluding framing bits but including FCS
octets).
Packets Received 128–255 Octets - The total number of packets (including bad packets) received
that were between 128 and 255 octets in length inclusive (excluding framing bits but including FCS
octets).
Packets Received 256–511 Octets - The total number of packets (including bad packets) received
that were between 256 and 511 octets in length inclusive (excluding framing bits but including FCS
octets).
Packets Received 512–1023 Octets - The total number of packets (including bad packets)
received that were between 512 and 1023 octets in length inclusive (excluding framing bits but
including FCS octets).
Utility Commands 201

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Packets Received Packets Received 1024–1518 Octets - The total number of packets (including bad packets)
(continued) received that were between 1024 and 1518 octets in length inclusive (excluding framing bits but
including FCS octets).
Packets Received > 1518 Octets - The total number of packets received that were longer than
1522 octets (excluding framing bits, but including FCS octets) and were otherwise well formed.
Packets RX and TX 64 Octets - The total number of packets (including bad packets) received and
transmitted that were 64 octets in length (excluding framing bits but including FCS octets).
Packets RX and TX 65–127 Octets - The total number of packets (including bad packets) received
and transmitted that were between 65 and 127 octets in length inclusive (excluding framing bits but
including FCS octets).
Packets RX and TX 128–255 Octets - The total number of packets (including bad packets)
received and transmitted that were between 128 and 255 octets in length inclusive (excluding
framing bits but including FCS octets).
Packets RX and TX 256–511 Octets - The total number of packets (including bad packets) received
and transmitted that were between 256 and 511 octets in length inclusive (excluding framing bits but
including FCS octets).
Packets RX and TX 512–1023 Octets - The total number of packets (including bad packets)
received and transmitted that were between 512 and 1023 octets in length inclusive (excluding
framing bits but including FCS octets).
Packets RX and TX 1024–1518 Octets - The total number of packets (including bad packets)
received and transmitted that were between 1024 and 1518 octets in length inclusive (excluding
framing bits but including FCS octets).
Packets RX and TX 1519–2047 Octets - The total number of packets received and transmitted that
were between 1519 and 2047 octets in length inclusive (excluding framing bits, but including FCS
octets) and were otherwise well formed.
Packets RX and TX 1523–2047 Octets - The total number of packets received and transmitted that
were between 1523 and 2047 octets in length inclusive (excluding framing bits, but including FCS
octets) and were otherwise well formed.
Packets RX and TX 2048–4095 Octets - The total number of packets received that were between
2048 and 4095 octets in length inclusive (excluding framing bits, but including FCS octets) and were
otherwise well formed.
Packets RX and TX 4096–9216 Octets - The total number of packets received that were between
4096 and 9216 octets in length inclusive (excluding framing bits, but including FCS octets) and were
otherwise well formed.
Packets Received Total Packets Received Without Error - The total number of packets received that were without
Successfully errors.
Unicast Packets Received - The number of subnetwork-unicast packets delivered to a higher-layer
protocol.
Multicast Packets Received - The total number of good packets received that were directed to a
multicast address. Note that this number does not include packets directed to the broadcast
address.
Broadcast Packets Received - The total number of good packets received that were directed to the
broadcast address. Note that this does not include multicast packets.
Receive Packets The number of inbound packets which were chosen to be discarded even though no errors had been
Discarded detected to prevent their being deliverable to a higher-layer protocol. One possible reason for
discarding such a packet could be to free up buffer space.
Utility Commands 202

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Packets Received Total Packets Received with MAC Errors - The total number of inbound packets that contained
with MAC Errors errors preventing them from being deliverable to a higher-layer protocol.
Jabbers Received - The total number of packets received that were longer than 1518 octets
(excluding framing bits, but including FCS octets), and had either a bad Frame Check Sequence
(FCS) with an integral number of octets (FCS Error) or a bad FCS with a non-integral number of
octets (Alignment Error). Note that this definition of jabber is different than the definition in
IEEE-802.3 section 8.2.1.5 (10BASE5) and section 10.3.1.4 (10BASE2). These documents define
jabber as the condition where any packet exceeds 20 ms. The allowed range to detect jabber is
between 20 ms and 150 ms.
Fragments/Undersize Received - The total number of packets received that were less than 64
octets in length (excluding framing bits but including FCS octets).
Alignment Errors - The total number of packets received that had a length (excluding framing bits,
but including FCS octets) of between 64 and 1518 octets, inclusive, but had a bad Frame Check
Sequence (FCS) with a non-integral number of octets.
FCS Errors - The total number of packets received that had a length (excluding framing bits, but
including FCS octets) of between 64 and 1518 octets, inclusive, but had a bad Frame Check
Sequence (FCS) with an integral number of octets.
Overruns - The total number of frames discarded as this port was overloaded with incoming
packets, and could not keep up with the inflow.
Received Packets Total Received Packets Not Forwarded - A count of valid frames received which were discarded
Not Forwarded (in other words, filtered) by the forwarding process
802.3x Pause Frames Received - A count of MAC Control frames received on this interface with an
opcode indicating the PAUSE operation. This counter does not increment when the interface is
operating in half-duplex mode.
Unacceptable Frame Type - The number of frames discarded from this port due to being an
unacceptable frame type.
Packets Total Packets Transmitted (Octets) - The total number of octets of data (including those in bad
Transmitted Octets packets) received on the network (excluding framing bits but including FCS octets). This object can
be used as a reasonable estimate of Ethernet utilization. If greater precision is desired, the
etherStatsPkts and etherStatsOctets objects should be sampled before and after a common interval.
-----
Packets Transmitted 64 Octets - The total number of packets (including bad packets) received that
were 64 octets in length (excluding framing bits but including FCS octets).
Packets Transmitted 65-127 Octets - The total number of packets (including bad packets)
received that were between 65 and 127 octets in length inclusive (excluding framing bits but
including FCS octets).
Packets Transmitted 128-255 Octets - The total number of packets (including bad packets)
received that were between 128 and 255 octets in length inclusive (excluding framing bits but
including FCS octets).
Packets Transmitted 256-511 Octets - The total number of packets (including bad packets)
received that were between 256 and 511 octets in length inclusive (excluding framing bits but
including FCS octets).
Packets Transmitted 512-1023 Octets - The total number of packets (including bad packets)
received that were between 512 and 1023 octets in length inclusive (excluding framing bits but
including FCS octets).
Utility Commands 203

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Packets Packets Transmitted 1024-1518 Octets - The total number of packets (including bad packets)
Transmitted Octets received that were between 1024 and 1518 octets in length inclusive (excluding framing bits but
(continued) including FCS octets).
Packets Transmitted > 1518 Octets - The total number of packets transmitted that were longer
than 1518 octets (excluding framing bits, but including FCS octets) and were otherwise well formed.
Max Frame Size - The maximum size of the Info (non-MAC) field that this port will receive or
transmit.
Packets Total Packets Transmitted Successfully- The number of frames that have been transmitted by
Transmitted this port to its segment.
Successfully Unicast Packets Transmitted - The total number of packets that higher-level protocols requested
be transmitted to a subnetwork-unicast address, including those that were discarded or not sent.
Multicast Packets Transmitted - The total number of packets that higher-level protocols requested
be transmitted to a Multicast address, including those that were discarded or not sent.
Broadcast Packets Transmitted - The total number of packets that higher-level protocols
requested be transmitted to the Broadcast address, including those that were discarded or not sent.
Transmit Packets The number of outbound packets which were chosen to be discarded even though no errors had
Discarded been detected to prevent their being deliverable to a higher-layer protocol. A possible reason for
discarding a packet could be to free up buffer space.
Transmit Errors Total Transmit Errors - The sum of Single, Multiple, and Excessive Collisions.
FCS Errors - The total number of packets transmitted that had a length (excluding framing bits, but
including FCS octets) of between 64 and 1518 octets, inclusive, but had a bad Frame Check
Sequence (FCS) with an integral number of octets.
Underrun Errors - The total number of frames discarded because the transmit FIFO buffer became
empty during frame transmission.
Transmit Discards Total Transmit Packets Discards - The sum of single collision frames discarded, multiple collision
frames discarded, and excessive frames discarded.
Single Collision Frames - A count of the number of successfully transmitted frames on a particular
interface for which transmission is inhibited by exactly one collision.
Multiple Collision Frames - A count of the number of successfully transmitted frames on a
particular interface for which transmission is inhibited by more than one collision.
Excessive Collisions - A count of frames for which transmission on a particular interface fails due
to excessive collisions.
Port Membership Discards - The number of frames discarded on egress for this port due to egress
filtering being enabled.
Utility Commands 204

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Protocol Statistics 802.3x Pause Frames Transmitted - A count of MAC Control frames transmitted on this interface
with an opcode indicating the PAUSE operation. This counter does not increment when the interface
is operating in half-duplex mode.
GVRP PDUs Received - The count of GVRP PDUs received in the GARP layer.
GVRP PDUs Transmitted - The count of GVRP PDUs transmitted from the GARP layer.
GVRP Failed Registrations - The number of times attempted GVRP registrations could not be
completed.
GMRP PDUs Received - The count of GMRP PDUs received in the GARP layer.
GMRP PDUs Transmitted - The count of GMRP PDUs transmitted from the GARP layer.
GMRP Failed Registrations - The number of times attempted GMRP registrations could not be
completed.
STP BPDUs Transmitted - Spanning Tree Protocol Bridge Protocol Data Units sent.
STP BPDUs Received - Spanning Tree Protocol Bridge Protocol Data Units received.
RST BPDUs Transmitted - Rapid Spanning Tree Protocol Bridge Protocol Data Units sent.
RSTP BPDUs Received - Rapid Spanning Tree Protocol Bridge Protocol Data Units received.
MSTP BPDUs Transmitted - Multiple Spanning Tree Protocol Bridge Protocol Data Units sent.
MSTP BPDUs Received - Multiple Spanning Tree Protocol Bridge Protocol Data Units received.
Dot1x Statistics EAPOL Frames Transmitted - The number of EAPOL frames of any type that have been
transmitted by this authenticator.
EAPOL Start Frames Received - The number of valid EAPOL start frames that have been received
by this authenticator.
Time Since The elapsed time, in days, hours, minutes, and seconds since the statistics for this port were last
Counters Last cleared.
Cleared
If you use the switchport keyword, the following information displays.
Term Definition
Packets Received Without The total number of packets (including broadcast packets and multicast packets) received by
Error the processor.
Broadcast Packets The total number of packets received that were directed to the broadcast address. Note that
Received this does not include multicast packets.
Packets Received With The total number of packets with errors (including broadcast packets and multicast packets)
Error received by the processor.
Packets Transmitted The total number of packets transmitted out of the interface.
without Errors
Broadcast Packets The total number of packets that higher-level protocols requested be transmitted to the
Transmitted Broadcast address, including those that were discarded or not sent.
Transmit Packet Errors The number of outbound packets that could not be transmitted because of errors.
Number of Port Link Down The number of occurrences that a port link went down.
Events
Utility Commands 205

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Link Flaps The number of link flaps per interface.
Time Since Counters Last The elapsed time, in days, hours, minutes, and seconds, since the statistics for this switch
Cleared were last cleared.
If you use the all keyword, the following information displays for all interfaces on the switch.
Term Definition
Port The Interface ID.
Bytes Tx The total number of bytes transmitted by the interface.
Bytes Rx The total number of bytes transmitted by the interface.
Packets Tx The total number of packets transmitted by the interface.
Packets Rx The total number of packets transmitted by the interface.
show interface ethernet switchport
This command displays the private VLAN mapping information for the switch interfaces.
Format show interface ethernet interface-id switchport
Mode Privileged EXEC
Parameter Description
interface-id The unit/slot/port of the switch.
The command displays the following information.
Term Definition
Private-vlan The VLAN association for the private-VLAN host ports.
host-association
Private-vlan mapping The VLAN mapping for the private-VLAN promiscuous ports.
show interface lag
Use this command to display configuration information about the specified LAG interface.
Format show interface lag lag-intf-num
Mode Privileged EXEC
Utility Commands 206

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Definition
Packets Received Without The total number of packets (including broadcast packets and multicast packets) received
Error on the LAG interface
Packets Received With The number of inbound packets that contained errors preventing them from being
Error deliverable to a higher-layer protocol.
Broadcast Packets The total number of packets received that were directed to the broadcast address. Note
Received that this does not include multicast packets.
Receive Packets Discarded The number of inbound packets which were chosen to be discarded even though no errors
had been detected to prevent their being deliverable to a higher-layer protocol. One
possible reason for discarding such a packet could be to free up buffer space.
Packets Transmitted The total number of packets transmitted out of the LAG.
Without Error
Transmit Packets Discarded The number of outbound packets which were chosen to be discarded even though no
errors had been detected to prevent their being deliverable to a higher-layer protocol. A
possible reason for discarding a packet could be to free up buffer space.
Transmit Packets Errors The number of outbound packets that could not be transmitted because of errors.
Collisions Frames The best estimate of the total number of collisions on this Ethernet segment.
Time Since Counters Last The elapsed time, in days, hours, minutes, and seconds since the statistics for this LAG
Cleared were last cleared.
show fiber-ports optics
This command displays the diagnostics information of the SFP like Temp, Voltage, Current,
Input Power, Output Power, Tx Fault, and LOS. The values are derived from the SFP’s A2
(Diagnostics) table using the I2C interface.
Format show fiber-ports optics {all | unit/slot/port}
Mode Privileged EXEC
Field Description
Temp Internally measured transceiver temperature.
Voltage Internally measured supply voltage.
Current Measured TX bias current.
Output Power Measured optical output power relative to 1mW.
Input Power Measured optical power received relative to 1mW.
TX Fault Transmitter fault.
LOS Loss of signal.
Utility Commands 207

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show fiber-ports optics all
Output Input
Port Temp Voltage Current Power Power TX LOS
[C] [Volt] [mA] [dBm] [dBm] Fault
-------- ---- ------- ------- ------- ------- ----- ---
0/49 39.3 3.256 5.0 -2.234 -2.465 No No
0/50 33.9 3.260 5.3 -2.374 -40.000 No Yes
0/51 32.2 3.256 5.6 -2.300 -2.897 No No
show fiber-ports optics-diag
This command displays the diagnostics information of the SFP in raw data.
Format show fiber-ports optics-diag {all | unit/slot/port}
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show fiber-ports optics-diag all
Port 2/0/5
diag data =
52 00 f8 00 50 00 f9 00 89 1c 79 18 88 86 79 ae R...P.....y...y.
96 64 08 ca 88 b8 0a be 31 2d 05 45 2b d4 05 ea .d......1-.E+...
3d e9 00 b6 37 2d 00 e5 00 00 00 00 00 00 00 00 =...7-..........
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
00 00 00 00 3f 80 00 00 00 00 00 00 01 00 00 00 ....?...........
01 00 00 00 01 00 00 00 01 00 00 00 00 00 00 50 ...............P
1d 7d 80 15 2c 15 16 08 00 00 00 00 00 00 02 00 .}..,...........
00 40 00 00 00 40 00 00 00 00 00 20 20 20 20 00 .@...@..... .
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
Utility Commands 208

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show fiber-ports optics-eeprom
This command displays the Electrically Erasable Programmable Read-Only Memory
(EEPROM) of the SFP.
Format show fiber-ports optics-eeprom {unit/slot/port | all}
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show fiber-ports optics-eeprom 1/0/3
Port 1/0/3
vendor_name = NETGEAR
vendor_sn = A7N2018312
date_code = 100625
vend_pn = AXM761
vend_rev = 10
eeprom data = 03 04 07 10 00 00 00 00 00 00 00 03 67 00 00 00 ............g...
08 03 00 1e 4e 45 54 47 45 41 52 20 20 20 20 20 ....NETGEAR
20 20 20 20 00 00 1f 22 41 58 4d 37 36 31 20 20 ..."AXM761
20 20 20 20 20 20 20 20 31 30 20 20 03 52 00 d2 10 .R..
00 1a 00 00 41 37 4e 32 30 31 38 33 31 32 20 20 ....A7N2018312
20 20 20 20 31 30 30 36 32 35 20 20 68 f0 03 ca 100625 h...
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ................
show fiber-ports optics-info
This command displays the SFP vendor related information like Vendor Name, Serial
Number of the SFP, Part Number of the SFP. The values are derived from the SFP’s A0 table
using the I2C interface.
Format show fiber-ports optics-info {all | slot/port}
Mode Privileged EXEC
Utility Commands 209

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Description
Vendor Name The vendor name is a 16 character field that contains ASCII characters, left-aligned
and padded on the right with ASCII spaces (20h). The vendor name shall be the full
name of the corporation, a commonly accepted abbreviation of the name of the
corporation, the SCSI company code for the corporation, or the stock exchange code
for the corporation.
Length (50um, OM2) This value specifies link length that is supported by the transceiver while operating in
compliance with applicable standards using 50 micron multimode OM2 [500MHz*km
at 850nm] fiber. A value of zero means that the transceiver does not support 50
micron multimode fiber or that the length information must be determined from the
transceiver technology.
Length (62.5um, OM1) This value specifies link length that is supported by the transceiver while operating in
compliance with applicable standards using 62.5 micron multimode OM1 [200
MHz*km at 850nm, 500 MHz*km at 1310nm] fiber. A value of zero means that the
transceiver does not support 62.5 micron multimode fiber or that the length
information must determined from the transceiver technology
Vendor SN The vendor serial number (vendor SN) is a 16 character field that contains ASCII
characters, left-aligned and padded on the right with ASCII spaces (20h), defining
the vendor's serial number for the transceiver. A value of all zero in the 16-byte field
indicates that the vendor SN is unspecified.
Vendor PN The vendor part number (vendor PN) is a 16-byte field that contains ASCII
characters, left aligned and added on the right with ASCII spaces (20h), defining the
vendor part number or product name. A value of all zero in the 16-byte field indicates
that the vendor PN is unspecified.
BR, nominal The nominal bit (signaling) rate (BR, nominal) is specified in units of 100 MBd,
rounded off to the nearest 100 MBd. The bit rate includes those bits necessary to
encode and delimit the signal as well as those bits carrying data information. A value
of 0 indicates that the bit rate is not specified and must be determined from the
transceiver technology. The actual information transfer rate will depend on the
encoding of the data, as defined by the encoding value.
Vendor Rev The vendor revision number (vendor rev) contains ASCII characters, left aligned and
padded on the right with ASCII spaces (20h), defining the vendor's product revision
number. A value of all zero in this field indicates that the vendor revision is
unspecified.
Command example:
(NETGEAR Switch) #show fiber-ports optics-info all
Link Link Nominal
Length Length Bit
50um 62.5um Rate
Port Vendor Name [m] [m] Serial Number Part Number [Mbps] Rev
-------- ---------------- --- ---- ---------------- ---------------- ----- ----
0/49 NETGEAR 8 3 A7N2018414 AXM761 10300 10
0 /51 N ETGEAR 8 3 A7N2018472 AXM761 10300 10
0/52 N ETGEAR 8 3 A7N2018501 AXM761 10300 10
Utility Commands 210

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show mac-addr-table
This command displays the forwarding database entries. These entries are used by the
transparent bridging function to determine how to forward a received frame.
Enter all or no parameter to display the entire table. Enter a MAC Address and VLAN ID to
display the table entry for the requested MAC address on the specified VLAN. Enter the
count parameter to view summary information about the forwarding database table. Use
the interface unit/slot/port parameter to view MAC addresses on a specific
interface.
Instead of unit/slot/port, lag lag-intf-num can be used as an alternate way to
specify the LAG interface, in whichlag-intf-num is the LAG port number. Use the vlan
vlan-id parameter to display information about MAC addresses on a specified VLAN.
Format show mac-addr-table [macaddr vlan-id | all | count | interface unit/slot/port
| vlan vlan-id]
Mode Privileged EXEC
The following information displays if you do not enter a parameter, the keyword all, or the
MAC address and VLAN ID.
Term Definition
VLAN ID The VLAN in which the MAC address is learned.
MAC Address A unicast MAC address for which the switch has forwarding and or filtering information. The format is 6
two-digit hexadecimal numbers that are separated by colons, for example 01:23:45:67:89:AB.
Interface The port through which this address was learned.
Interface Index This object indicates the ifIndex of the interface table entry associated with this port.
Status The status of this entry. The meanings of the values are:
• Static. The value of the corresponding instance was added by the system or a user when a static
MAC filter was defined. It cannot be relearned.
• Learned. The value of the corresponding instance was learned by observing the source MAC
addresses of incoming traffic, and is currently in use.
• Management. The value of the corresponding instance (system MAC address) is also the value of
an existing instance of dot1dStaticAddress. It is identified with interface 0/1. and is currently used
when enabling VLANs for routing.
• Self. The value of the corresponding instance is the address of one of the switch’s physical
interfaces (the system’s own MAC address).
• GMRP Learned. The value of the corresponding was learned via GMRP and applies to Multicast.
• Other. The value of the corresponding instance does not fall into one of the other categories.
If you enter vlan vlan-id, only the MAC Address, Interface, and Status fields appear. If
you enter the interface unit/slot/port parameter, in addition to the MAC Address
and Status fields, the VLAN ID field also appears.
Utility Commands 211

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The following information displays if you enter the count parameter.
Term Definition
Dynamic Address Number of MAC addresses in the forwarding database that were automatically learned.
count
Static Address Number of MAC addresses in the forwarding database that were manually entered by a user.
(User-defined)
count
Total MAC Number of MAC addresses currently in the forwarding database.
Addresses in use
Total MAC Number of MAC addresses the forwarding database can handle.
Addresses
available
process cpu threshold
Use this command to configure the CPU utilization thresholds. The Rising and Falling
thresholds are specified as a percentage of CPU resources. The utilization monitoring time
period can be configured from 5 seconds to 86400 seconds in multiples of 5 seconds. The
CPU utilization threshold configuration is saved across a switch reboot. Configuring the
falling utilization threshold is optional. If the falling CPU utilization parameters are not
configured, then they take the same value as the rising CPU utilization parameters.
Format process cpu threshold type total rising threshold interval seconds [falling
threshold interval seconds]
Mode Global Config
Term Description
rising threshold The percentage of CPU resources that, when exceeded for the configured rising interval, triggers a
notification. The range is 1 to 100. The default is 0 (disabled).
rising interval The duration of the CPU rising threshold violation, in seconds, that must be met to trigger a
seconds notification. The range is 5 to 86400. The default is 0 (disabled).
falling threshold The percentage of CPU resources that, when usage falls below this level for the configured interval,
triggers a notification. The range is 1 to 100. The default is 0 (disabled).
A notification is triggered when the total CPU utilization falls below this level for a configured period
of time. The falling utilization threshold notification is made only if a rising threshold notification was
previously done. The falling utilization threshold must always be equal or less than the rising
threshold value. The CLI does not allow setting the falling threshold to be greater than the rising
threshold.
falling interval The duration of the CPU falling threshold, in seconds, that must be met to trigger a notification. The
seconds range is 5 to 86400. The default is 0 (disabled).
Utility Commands 212

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show process app-list
This command displays the user and system applications.
Format show process app-list
Mode Privileged EXEC
Field Description
ID The application identifier.
Name The name that identifies the process.
PID The number the software uses to identify the process.
Admin Status The administrative status of the process.
Auto Restart Indicates whether the process will automatically restart if it stops.
Running Status Indicates whether the process is currently running or stopped.
Command example:
(NETGEAR Switch) #show process app-list
Admin Auto Running
ID Name PID Status Restart Status
---- ---------------- ----- --------- --------- -------
1 dataplane 15309 Enabled Disabled Running
2 switchdrvr 15310 Enabled Disabled Running
3 syncdb 15314 Enabled Disabled Running
4 lighttpd 18718 Enabled Enabled Running
5 syncdb-test 0 Disabled Disabled Stopped
6 proctest 0 Disabled Enabled Stopped
7 user.start 0 Enabled Disabled Stopped
show process memory
This command displays memory consumption details by various software components.
Format show process memory
Mode Privileged EXEC
Field Description
Total The total available memory on the switch.
Free The free memory on the switch.
Allocated The allocated memory on the switch, excluding cache space used by the file system.
Components The internal software component.
Utility Commands 213

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Description
CurrentAllocated The amount of memory that a component is using.
Change The increase or decrease of the memory that a component consumes since the last time this
command was executed. This field shows the difference in memory allocation between two
successive executions of the command.
MaxAllocated The maximum amount of memory allocation by a component.
Allocs/Frees The number of memory allocation and free calls made by a component.
show process cpu
This command provides the percentage utilization of the CPU by different tasks. The number
argument can be a number from 1 to 8.
Note: A busy CPU might not be caused by traffic processing but by various
tasks that run simultaneously.
Format show process cpu [number | all]
Mode Privileged EXEC
Parameter Description
Free The system-wide free memory.
Alloc The system-wide allocated memory (excluding cache, file system used space).
Pid The process or thread ID.
Name The process or thread name.
5Secs The CPU utilization sampling in 5-second intervals.
60Secs The CPU utilization sampling in 60-second intervals.
300Secs The CPU utilization sampling in 300-second intervals.
Total CPU Utilization Total CPU utilization in percentage within the specified window of 5, 60, and 300 seconds.
(NETGEAR Switch) #show process cpu
Memory Utilization Report
status bytes
------ ----------
free 106450944
alloc 423227392
CPU Utilization:
Utility Commands 214
