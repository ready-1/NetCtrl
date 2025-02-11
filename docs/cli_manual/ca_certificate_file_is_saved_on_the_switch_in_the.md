# ca_certificate_file_is_saved_on_the_switch_in_the

Pages: 252-259

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Source Destination Description
nvram:traplog url Copies the trap log file to a server.
system:running-config nvram:startup-config Saves the running configuration to NVRAM.
system:running-config nvram:factory-defaults Saves the running configuration to NVRAM to the
factory-defaults file.
nvram:application url Saves the source application file with the name
sourcefilename specified by the sourcefilename argument.
url nvram:application Downloads the source application file to the switch
destfilename and saves it with the name specified by the
destfilename argument.
url nvram:ca-root index Downloads the CA certificate file to the switch. The
CA certificate file is saved on the switch in the
CAindex.pem format.
For example, if you enter the copy
tftp://172.26.2.21/mycertificate.pem
nvram:ca-root 3 command, the CA certificate file
is saved on switch with the name CA3.PEM.
url nvram:clibanner Downloads the CLI banner to the system.
url nvram:clientkey index Downloads the client key file to the switch. The client
key file is saved on the switch in the clientindex.key
format.
For example, if you enter the copy
tftp://172.26.2.21/client.key
nvram:clientkey 4 command, the client key file
is saved on switch with the name client4.key.
url nvram:client-ssl-cert Downloads the client certificate file to the switch. The
index client certificate file is saved on the switch in the
clientindex.pem format.
For example, if you enter the copy
tftp://172.26.2.21/client.pem
nvram:client-ssl-cert 2 command, the client
key file is saved on switch with the name
client2.pem.
url nvram:factory-defaults Downloads the file as the factory default
configuration.
url nvram:publickey-config Downloads the Public Key for Configuration Script
validation.
url nvram:publickey-image Downloads Public Key for Image validation.
url nvram:script Downloads a configuration script file to the system.
destfilename During the download of a configuration script, the
copy command validates the script. In case of any
error, the command lists all the lines at the end of the
validation process and prompts you to confirm before
copying the script file.
Utility Commands 252

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Source Destination Description
url nvram:script When you use this option, the copy command does
destfilename noval not validate the downloaded script file. An example
of the CLI command follows:
(NETGEAR Switch) #copy
tftp://1.1.1.1/file.scr nvram:script
file.scr noval
url nvram:sshkey-dsa Downloads an SSH key file. For more information,
see Secure Shell Commands on page77.
url nvram:sshkey-rsa2 Downloads an SSH key file.
url nvram:sslpem-dhweak Downloads an HTTP secure-server certificate.
url nvram:sslpem-dhstrong Downloads an HTTP secure-server certificate.
url nvram:sslpem-root Downloads an HTTP secure-server certificate. For
more information, see Hypertext Transfer Protocol
Commands on page85.
url nvram:sslpem-server Downloads an HTTP secure-server certificate.
url nvram:startup-config Downloads the startup configuration file to the
system.
url ias-users Downloads an IAS users database file to the system.
When the IAS users file is downloaded, the switch
IAS user’s database is replaced with the users and
their attributes available in the downloaded file.
url {image1 | image2} Download an image from the remote server to either
image. The downloaded image is distributed to the
stack members.
url nvram:tech-support-cmds Download the tech-support-cmds file to the switch.
You can prepare a list of commands in this file. The
tech-support infrastructure reads this file and
displays the output of these additional commands if
you issue the show tech-support command. This
method is not supported under a subtree command
such as the show tech-suport dot3ad
command and the show tech-support ospf
command.
{image1 | image2} url Upload either image to the remote server.
{image1 | image2} unit://unit/{image1 | Copy an image from the master to a specific member
image2} in a stack. Use the unit parameter to specify the
member to which the image must be copied.
{image1 | image2} unit://*/{image1 | Copy an image from the master to all of members in
image2} a stack.
Utility Commands 253

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
The following example shows an ias users file that is downloaded and applied.
(NETGEAR Switch) #copy tftp://10.131.17.104/aaa_users.txt ias-users
Mode........................................... TFTP
Set Server IP.................................. 10.131.17.104
Path........................................... ./
Filename....................................... aaa_users.txt
Data Type...................................... IAS Users
Management access will be blocked for the duration of the transfer
Are you sure you want to start? (y/n) y
File transfer operation completed successfully.
Validating and updating the users to the IAS users database.
Updated IAS users database successfully.
file verify
This command enables digital signature verification while an image and/or configuration file
is downloaded to the switch.
Format file verify {all | image | none | script}
Mode Global Config
Parameter Description
All Verifies the digital signature of both image and configuration files.
Image Verifies the digital signature of image files only.
None Disables digital signature verification for both images and configuration files.
Script Verifies the digital signature of configuration files.
no file verify
Resets the configured digital signature verification value to the factory default value.
Format no file verify
Mode Global Config
Utility Commands 254

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
write memory
Use this command to save running configuration changes to NVRAM so that the changes
you make will persist across a reboot. This command is the same as copy
system:running-config nvram:startup-config. Use the confirm keyword to
directly save the configuration to NVRAM without prompting for a confirmation.
Format write memory [confirm]
Mode Privileged EXEC
Simple Network Time Protocol Commands
This section describes the commands you use to automatically configure the system time
and date by using Simple Network Time Protocol (SNTP).
sntp broadcast client poll-interval
This command sets the poll interval for SNTP broadcast clients in seconds as a power of two
where poll-interval can be a value from 6 to 10.
Default 6
Format sntp broadcast client poll-interval poll-interval
Mode Global Config
no sntp broadcast client poll-interval
This command resets the poll interval for SNTP broadcast client back to the default value.
Format no sntp broadcast client poll-interval
Mode Global Config
sntp client mode
This command enables Simple Network Time Protocol (SNTP) client mode and may set the
mode to either broadcast or unicast.
Default disabled
Format sntp client mode [broadcast | unicast]
Mode Global Config
Utility Commands 255

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no sntp client mode
This command disables Simple Network Time Protocol (SNTP) client mode.
Format no sntp client mode
Mode Global Config
sntp client port
This command sets the SNTP client port ID to a value in the range 1025–65535, represented
by the portid argument. The default value is 0, which means that the SNTP port is not
configured by the user. In the default case, the actual client port value used in SNTP packets
is assigned by the underlying OS.
Default 0
Format sntp client port portid
Mode Global Config
no sntp client port
This command resets the SNTP client port back to its default value.
Format no sntp client port
Mode Global Config
sntp unicast client poll-interval
This command sets the poll interval for SNTP unicast clients in seconds as a power of two
where poll-interval can be a value from 6 to 10.
Default 6
Format sntp unicast client poll-interval poll-interval
Mode Global Config
no sntp unicast client poll-interval
This command resets the poll interval for SNTP unicast clients to its default value.
Format no sntp unicast client poll-interval
Mode Global Config
Utility Commands 256

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
sntp unicast client poll-timeout
This command sets the poll time-out for SNTP unicast clients to a value from 1–30 seconds,
as represented by the poll-timeout argument.
Default 5
Format sntp unicast client poll-timeout poll-timeout
Mode Global Config
no sntp unicast client poll-timeout
This command will reset the poll timeout for SNTP unicast clients to its default value.
Format no sntp unicast client poll-timeout
Mode Global Config
sntp unicast client poll-retry
This command sets the poll retry for SNTP unicast clients to a value from 0 to 10, as
represented by the poll-retry argument.
Default 1
Format sntp unicast client poll-retry poll-retry
Mode Global Config
no sntp unicast client poll-retry
This command will reset the poll retry for SNTP unicast clients to its default value.
Format no sntp unicast client poll-retry
Mode Global Config
sntp server
This command configures an SNTP server (a maximum of three). The server address can be
either an IPv4 address or an IPv6 address. The optional priority can be a value of 1–3,
the version a value of 1–4, and the portid a value of 1–65535.
Format sntp server {ipaddress | ipv6address | hostname} [priority [version
[portid]]]
Mode Global Config
Utility Commands 257

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no sntp server
This command deletes an server from the configured SNTP servers.
Format no sntp server remove {ipaddress | ipv6address | hostname}
Mode Global Config
sntp source-interface
Use this command to specify the physical or logical interface to use as the source interface
(source IP address) for SNTP unicast server configuration. If configured, the address of
source Interface is used for all SNTP communications between the SNTP server and the
SNTP client. The selected source-interface IP address is used for filling the IP header of
management protocol packets. This allows security devices (firewalls) to identify the source
packets coming from the specific switch. If a source-interface is not specified, the primary IP
address of the originating (outbound) interface is used as the source address. If the
configured interface is down, the SNTP client falls back to its default behavior.
Format sntp source-interface {unit/slot/port | loopback loopback-id | vlan vlan-id}
Mode Global Config
Parameter Description
unit/slot/port The unit identifier assigned to the switch.
loopback-id Configures the loopback interface. The range of the loopback ID is 0 to 7.
tunnel-id Configures the IPv6 tunnel interface. The range of the tunnel ID is 0 to 7.
vlan-id Configures the VLAN interface to use as the source IP address. The range of the VLAN ID is 1 to
4093.
no sntp source-interface
Use this command to reset the SNTP source interface to the default settings.
Format no sntp source-interface
Mode Global Config
show sntp
This command is used to display SNTP settings and status.
Format show sntp
Mode Privileged EXEC
Utility Commands 258

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Last Update Time Time of last clock update.
Last Attempt Time Time of last transmit query (in unicast mode).
Last Attempt Status Status of the last SNTP request (in unicast mode) or unsolicited message (in broadcast mode).
Broadcast Count Current number of unsolicited broadcast messages that have been received and processed by the
SNTP client since last reboot.
show sntp client
This command is used to display SNTP client settings.
Format show sntp client
Mode Privileged EXEC
Term Definition
Client Supported Modes Supported SNTP Modes (Broadcast or Unicast).
SNTP Version The highest SNTP version the client supports.
Port SNTP Client Port. The field displays the value 0 if it is default value. When the client port
value is 0, if the client is in broadcast mode, it binds to port 123; if the client is in unicast
mode, it binds to the port assigned by the underlying OS.
Client Mode Configured SNTP Client Mode.
show sntp server
This command is used to display SNTP server settings and configured servers.
Format show sntp server
Mode Privileged EXEC
Term Definition
Server Host Address IP address or hostname of configured SNTP Server.
Server Type Address type of server (IPv4, IPv6, or DNS).
Server Stratum Claimed stratum of the server for the last received valid packet.
Server Reference ID Reference clock identifier of the server for the last received valid packet.
Server Mode SNTP Server mode.
Server Maximum Entries Total number of SNTP Servers allowed.
Server Current Entries Total number of SNTP configured.
Utility Commands 259
