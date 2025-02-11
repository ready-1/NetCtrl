# network3_radius_server_1813_yes

Pages: 156-167

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
192.168.37.202 Network3_RADIUS_Server 1813 Yes
192.168.37.203 Network4_RADIUS_Server 1813 No
Command example:
(NETGEAR Switch) #show radius accounting name Default_RADIUS_Server
Server Name............................ Default_RADIUS_Server
Host Address........................... 192.168.37.200
RADIUS Accounting Mode................. Disable
Port .................................. 1813
Secret Configured ..................... Yes
show radius accounting statistics
This command displays a summary of statistics for the configured RADIUS accounting
servers.
Format show radius accounting statistics {ipaddr | dnsname | name servername}
Mode Privileged EXEC
Term Definition
ipaddr The IP address of the server.
dnsname The DNS name of the server.
servername The alias name to identify the server.
RADIUS Accounting Server Name The name of the accounting server.
Server Host Address The IP address of the host.
Round Trip Time The time interval, in hundredths of a second, between the most recent
Accounting-Response and the Accounting-Request that matched it from this
RADIUS accounting server.
Requests The number of RADIUS Accounting-Request packets sent to this server. This
number does not include retransmissions.
Retransmission The number of RADIUS Accounting-Request packets retransmitted to this
RADIUS accounting server.
Responses The number of RADIUS packets received on the accounting port from this
server.
Malformed Responses The number of malformed RADIUS Accounting-Response packets received
from this server. Malformed packets include packets with an invalid length.
Bad authenticators or signature attributes or unknown types are not included
as malformed accounting responses.
Bad Authenticators The number of RADIUS Accounting-Response packets containing invalid
authenticators received from this accounting server.
Management Commands 156

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Pending Requests The number of RADIUS Accounting-Request packets sent to this server that
have not yet timed out or received a response.
Timeouts The number of accounting timeouts to this server.
Unknown Types The number of RADIUS packets of unknown types, which were received from
this server on the accounting port.
Packets Dropped The number of RADIUS packets received from this server on the accounting
port and dropped for some other reason.
Command example:
(NETGEAR Switch) #show radius accounting statistics 192.168.37.200
RADIUS Accounting Server Name................. Default_RADIUS_Server
Host Address.................................. 192.168.37.200
Round Trip Time............................... 0.00
Requests...................................... 0
Retransmissions............................... 0
Responses..................................... 0
Malformed Responses........................... 0
Bad Authenticators............................ 0
Pending Requests.............................. 0
Timeouts...................................... 0
Unknown Types................................. 0
Packets Dropped............................... 0
Command example:
(NETGEAR Switch) #show radius accounting statistics name Default_RADIUS_Server
RADIUS Accounting Server Name................. Default_RADIUS_Server
Host Address.................................. 192.168.37.200
Round Trip Time............................... 0.00
Requests...................................... 0
Retransmissions............................... 0
Responses..................................... 0
Malformed Responses........................... 0
Bad Authenticators............................ 0
Pending Requests.............................. 0
Timeouts...................................... 0
Unknown Types................................. 0
Packets Dropped............................... 0
Management Commands 157

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show radius source-interface
Use this command in Privileged EXEC mode to display the configured RADIUS client
source-interface (Source IP address) information.
Format show radius source-interface
Mode Privileged Exec
Command example:
(NETGEAR Switch)# show radius source-interface
RADIUS Client Source Interface.............. (not configured)
show radius statistics
This command displays the summary statistics of configured RADIUS Authenticating servers.
Format show radius statistics {ipaddr | dnsname | name servername}
Mode Privileged EXEC
Term Definition
ipaddr The IP address of the server.
dnsname The DNS name of the server.
servername The alias name to identify the server.
RADIUS Server The name of the authenticating server.
Name
Server Host The IP address of the host.
Address
Access Requests The number of RADIUS Access-Request packets sent to this server. This number does not include
retransmissions.
Access The number of RADIUS Access-Request packets retransmitted to this RADIUS authentication
Retransmissions server.
Access Accepts The number of RADIUS Access-Accept packets, including both valid and invalid packets, that were
received from this server.
Access Rejects The number of RADIUS Access-Reject packets, including both valid and invalid packets, that were
received from this server.
Access Challenges The number of RADIUS Access-Challenge packets, including both valid and invalid packets, that
were received from this server.
Malformed Access The number of malformed RADIUS Access-Response packets received from this server. Malformed
Responses packets include packets with an invalid length. Bad authenticators or signature attributes or
unknown types are not included as malformed access responses.
Management Commands 158

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Bad Authenticators The number of RADIUS Access-Response packets containing invalid authenticators or signature
attributes received from this server.
Pending Requests The number of RADIUS Access-Request packets destined for this server that have not yet timed out
or received a response.
Timeouts The number of authentication timeouts to this server.
Unknown Types The number of packets of unknown type that were received from this server on the authentication
port.
Packets Dropped The number of RADIUS packets received from this server on the authentication port and dropped for
some other reason.
Command example:
(NETGEAR Switch) #show radius statistics 192.168.37.200
RADIUS Server Name............................ Default_RADIUS_Server
Server Host Address........................... 192.168.37.200
Access Requests............................... 0.00
Access Retransmissions........................ 0
Access Accepts................................ 0
Access Rejects................................ 0
Access Challenges............................. 0
Malformed Access Responses.................... 0
Bad Authenticators............................ 0
Pending Requests.............................. 0
Timeouts...................................... 0
Unknown Types................................. 0
Packets Dropped............................... 0
Command example:
(NETGEAR Switch) #show radius statistics name Default_RADIUS_Server
RADIUS Server Name............................ Default_RADIUS_Server
Server Host Address........................... 192.168.37.200
Access Requests............................... 0.00
Access Retransmissions........................ 0
Access Accepts................................ 0
Access Rejects................................ 0
Access Challenges............................. 0
Malformed Access Responses.................... 0
Bad Authenticators............................ 0
Pending Requests.............................. 0
Timeouts...................................... 0
Unknown Types................................. 0
Packets Dropped............................... 0
Management Commands 159

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
TACACS+ Commands
TACACS+ provides access control for networked devices via one or more centralized
servers. Similar to RADIUS, this protocol simplifies authentication by making use of a single
database that can be shared by many clients on a large network. TACACS+ is based on the
TACACS protocol (described in RFC1492) but additionally provides for separate
authentication, authorization, and accounting services. The original protocol was UDP based
with messages passed in clear text over the network; TACACS+ uses TCP to ensure reliable
delivery and a shared key configured on the client and server to encrypt all messages.
The first time that you log in as an admin user, no password is required (that is, the password
is blank). As of software version 12.0.9.3, after you log in for the first time, you are required to
specify a new password that you must use each subsequent time that you log in. After you
specify the new password, you are logged out and then must log in again, using your new
password.
If you are using a RADIUS or TACAS+ server for authentication, after changing the default
password to the new password, make sure that you also change the password in the
RADIUS or TACAS+ server so that you can continue to log in to the switch.
tacacs-server host
Use the tacacs-server host command in Global Configuration mode to configure a
TACACS+ server. This command enters into the TACACS+ configuration mode. The
ip-address or hostname argument is the IP address or host name of the TACACS+
server. To specify multiple hosts, multiple tacacs-server host commands can be used.
Format tacacs-server host {ip-address | hostname}
Mode Global Config
no tacacs-server host
Use the no tacacs-server host command to delete the specified hostname or IP
address. The ip-address or hostname argument is the IP address or host name of the
TACACS+ server.
Format no tacacs-server host {ip-address | hostname}
Mode Global Config
tacacs-server key
Use the tacacs-server key command to set the authentication and encryption key for all
TACACS+ communications between the switch and the TACACS+ daemon. The
key-string parameter has a range of 0–128 characters and specifies the authentication
and encryption key for all TACACS communications between the switch and the TACACS+
server. This key must match the key used on the TACACS+ daemon.
Management Commands 160

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Text-based configuration supports TACACS server’s secrets in encrypted and non-encrypted
format. When you save the configuration, these secret keys are stored in encrypted format
only. If you want to enter the key in encrypted format, enter the key along with the encrypted
keyword. In the output of the show running-config command (for information about the
command, see show running-config on page216), these secret keys are displayed in
encrypted format. You cannot show these keys in plain text format.
Format tacacs-server key [key-string | encrypted key-string]
Mode Global Config
no tacacs-server key
Use the no tacacs-server key command to disable the authentication and encryption
key for all TACACS+ communications between the switch and the TACACS+ daemon. The
key-string parameter has a range of 0–128 characters This key must match the key used
on the TACACS+ daemon.
Format no tacacs-server key key-string
Mode Global Config
tacacs-server keystring
Use the tacacs-server keystring command to set the global authentication encryption
key used for all TACACS+ communications between the TACACS+ server and the client.
Format tacacs-server keystring
Mode Global Config
Command example:
(NETGEAR Switch)(Config)#tacacs-server keystring
Enter tacacs key:********Re-enter tacacs key:********
tacacs-server source-interface
Use this command in Global Configuration mode to configure the source interface (Source IP
address) for TACACS+ server configuration. The selected source-interface IP address is
used for filling the IP header of management protocol packets. This allows security devices
(firewalls) to identify the source packets coming from the specific switch.
If a source-interface is not specified, the primary IP address of the originating (outbound)
interface is used as the source address.
Format tacacs-server source-interface {unit/slot/port | loopback loopback-id |
vlan vlan-id}
Mode Global Config
Management Commands 161

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
unit/slot/port The unit identifier assigned to the switch, in unit/slot/port format.
loopback-id The loopback interface. The range of the loopback ID is 0 to 7.
vlan-id Configures the VLAN interface to use as the source IP address. The range of the VLAN ID is 1 to
4093.
Command example:
(Config)#tacacs-server source-interface loopback 0
(Config)#tacacs-server source-interface 1/0/1
(Config)#no tacacs-server source-interface
no tacacs-server source-interface
Use this command in Global Configuration mode to remove the global source interface
(Source IP selection) for all TACACS+ communications between the TACACS+ client and
the server.
Format no tacacs-server source-interface
Mode Global Config
tacacs-server timeout
Use the tacacs-server timeout command to set the time-out value in seconds for
communication with the TACACS+ servers. The seconds argument is a number in the range
of 1–30 seconds. If you do not specify a time-out value, the command sets the global
time-out to the default value. TACACS+ servers that do not use the global time-out will retain
their configured time-out values.
Default 5
Format tacacs-server timeout seconds
Mode Global Config
no tacacs-server timeout
Use the no tacacs-server timeout command to restore the default timeout value for all
TACACS servers.
Format no tacacs-server timeout
Mode Global Config
Management Commands 162

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
key (TACACS Config)
Use the key command in TACACS Configuration mode to specify the authentication and
encryption key for all TACACS communications between the device and the TACACS server.
This key must match the key used on the TACACS daemon. The key-string argument
specifies the key name. For an empty string use “ ”. (Range: 0 - 128 characters).
Text-based configuration supports TACACS server’s secrets in encrypted and non-encrypted
format. When you save the configuration, these secret keys are stored in encrypted format
only. If you want to enter the key in encrypted format, enter the key along with the encrypted
keyword. In the output of the show running-config command (for information about the
command, see show running-config on page216), these secret keys are displayed in
encrypted format. You cannot show these keys in plain text format.
Format key [key-string | encrypted key-string]
Mode TACACS Config
keystring (TACACS Config)
Use the keystring command in TACACS Server Configuration mode to set the TACACS+
server-specific authentication encryption key used for all TACACS+ communications
between the TACACS+ server and the client.
Format keystring
Mode TACACS Server Config
Command example:
(NETGEAR Switch)(Config)#tacacs-server host 1.1.1.1
(NETGEAR Switch)(Tacacs)#keystring
Enter tacacs key:********
Re-enter tacacs key:********
port (TACACS Config)
Use the port command in TACACS Configuration mode to specify a server port number.
The server port-number argument is a number in the range 0–65535.
Default 49
Format port port-number
Mode TACACS Config
Management Commands 163

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
priority (TACACS Config)
Use the priority command in TACACS Configuration mode to specify the order in which
servers are used, where 0 (zero) is the highest priority. The priority argument specifies
the priority for servers. The highest priority is 0 (zero), and the range is 0–65535.
Default 0
Format priority priority
Mode TACACS Config
timeout (TACACS Config)
Use the timeout command in TACACS Configuration mode to specify the time-out value in
seconds. If no time-out value is specified, the global value is used. The seconds argument is
a number in the range 1–30 seconds as specifies the time-out.
Format timeout seconds
Mode TACACS Config
show tacacs
Use the show tacacs command to display the configuration, statistics, and source interface
details of the TACACS+ client.
Format show tacacs [ip-address | hostname | client | server]
Mode Privileged EXEC
Term Definition
Host address The IP address or hostname of the configured TACACS+ server.
Port The configured TACACS+ server port number.
TimeOut The timeout in seconds for establishing a TCP connection.
Priority The preference order in which TACACS+ servers are contacted. If a server connection fails, the next
highest priority server is contacted.
show tacacs source-interface
Use the show tacacs source-interface command in Global Config mode to display
the configured global source interface details used for a TACACS+ client. The IP address of
the selected interface is used as source IP for all communications with the server.
Format show tacacs source-interface
Mode Privileged EXEC
Management Commands 164

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(Config)# show tacacs source-interface
TACACS Client Source Interface : loopback 0
TACACS Client Source IPv4 Address : 1.1.1.1 [UP]
Configuration Scripting Commands
Configuration Scripting allows you to generate text-formatted script files representing the
current configuration of a system. You can upload these configuration script files to a PC or
UNIX system and edit them. Then, you can download the edited files to the system and apply
the new configuration. You can apply configuration scripts to one or more switches with no or
minor modifications.
Use the show running-config command (see show running-config on page216) to
capture the running configuration into a script. Use the copy command (see copy on
p age250) to transfer the configuration script to or from the switch.
Use the show command to view the configuration stored in the startup-config, backup-config,
or factory-defaults file (see show (Privileged EXEC) on page218).
Use scripts on systems with default configurations; however, you are not prevented from
applying scripts on systems with non-default configurations.
Scripts must conform to the following rules:
• Script files are not distributed across the stack and remain only in the unit that is the
master at the time of the file download.
• The file extension must be “.scr”.
• A maximum of ten scripts are allowed on the switch.
• The combined size of all script files on the switch shall not exceed 2048 KB.
• The maximum number of configuration file command lines is 2000.
You can type single-line annotations at the command prompt to use when you write test or
configuration scripts to improve script readability. The exclamation point (!) character flags
the beginning of a comment. The comment flag character can begin a word anywhere on the
command line, and all input following this character is ignored. Any command line that begins
with the “!” character is recognized as a comment line and ignored by the parser.
The following lines show an example of a script:
! Script file for displaying management access
show telnet !Displays the information about remote connections
! Display information about direct connections
Management Commands 165

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show serial
! End of the script file!
To specify a blank password for a user in the configuration script, you must specify it as a
space within quotes. For example, to change the password for user jane from a blank
password to hello, the script entry is as follows:
users passwd jane
" "
hello
hello
script apply
This command applies the commands in the script to the switch. The scriptname argument
is the name of the script to apply.
Format script apply scriptname
Mode Privileged EXEC
script delete
This command deletes a specified script where the scriptname argument is the name of
the script to delete. The all option deletes all the scripts present on the switch.
Format script delete {scriptname | all}
Mode Privileged EXEC
script list
This command lists all scripts present on the switch as well as the remaining available space.
Format script list
Mode Privileged EXEC
Term Definition
Configuration Script Name of the script.
Size Privileged EXEC
Management Commands 166

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
script show
This command displays the contents of a script file, which you specify with the scriptname
argument.
Format script show scriptname
Mode Privileged EXEC
Term Definition
Output Format line number: line contents
script validate
This command validates a script file by parsing each line in the script file, in which
scriptname is the name of the script to validate.The validate option is intended to be used
as a tool for script development. Validation identifies potential problems. It might not identify
all problems with a given script on any given device.
Format script validate scriptname
Mode Privileged EXEC
Prelogin Banner, System Prompt, and Host
Name Commands
This section describes the commands you use to configure the prelogin banner and the
system prompt. The prelogin banner is the text that displays before you login at the User:
prompt.
copy (pre-login banner)
The copy command includes the option to upload or download the CLI Banner to or from the
switch. You can specify local URLs by using FTP, TFTP, SFTP, SCP, or Xmodem.
Note: The ip6address argument is also a valid parameter for routing
packages that support IPv6.
Management Commands 167
