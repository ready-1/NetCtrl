# ascii_characters

Pages: 181-191

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
