# nas-ip-address_attribute_to_be_used_in_radius_requests

Pages: 146-151

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no server-key
Use this command to remove the global shared secret key configuration.
Format no server-key
Mode Dynamic Authorization
radius accounting mode
This command is used to enable the RADIUS accounting function.
Default disabled
Format radius accounting mode
Mode Global Config
no radius accounting mode
This command is used to set the RADIUS accounting function to the default value - i.e. the
RADIUS accounting function is disabled.
Format no radius accounting mode
Mode Global Config
radius server attribute 4
This command specifies the RADIUS client to use the NAS-IP Address attribute in the
RADIUS requests. If the specific IP address is configured while enabling this attribute, the
RADIUS client uses that IP address while sending NAS-IP-Address attribute in RADIUS
communication.
Format radius server attribute 4 [ipaddr]
Mode Global Config
Term Definition
4 NAS-IP-Address attribute to be used in RADIUS requests.
ipaddr The IP address of the server.
Management Commands 146

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no radius server attribute 4
The no radius server attribute 4 command disables the NAS-IP-Address attribute
global parameter for RADIUS client. When this parameter is disabled, the RADIUS client
does not send the NAS-IP-Address attribute in RADIUS requests.
Format no radius server attribute 4 [ipaddr]
Mode Global Config
Command example:
(NETGEAR Switch) (Config) #radius server attribute 4 192.168.37.60
(NETGEAR Switch) (Config) #radius server attribute 4
radius server host
This command configures the IP address or DNS name to use for communicating with the
RADIUS server of a selected server type. While configuring the IP address or DNS name for
the authenticating or accounting servers, you can also configure the port number and server
name. If the authenticating and accounting servers are configured without a name, the
command uses the Default_RADIUS_Auth_Server and Default_RADIUS_Acct_Server as the
default names, respectively. The same name can be configured for more than one
authenticating servers and the name should be unique for accounting servers. The RADIUS
client allows the configuration of a maximum 32 authenticating and accounting servers.
If you use the auth parameter, the command configures the IP address or host name to use
to connect to a RADIUS authentication server. You can configure up to three servers per
RADIUS client. If the maximum number of configured servers is reached, the command fails
until you remove one of the servers by issuing the no form of the command. If you use the
optional port parameter, the command configures the UDP port number to use when
connecting to the configured RADIUS server. For the port keyword, the number argument
must be a value in the range 0–65535, with 1813 being the default.
Note: To reconfigure a RADIUS authentication server to use the default
UDP port, set the number argument to 1812.
If you use the acct token, the command configures the IP address or host name to use for
the RADIUS accounting server. You can only configure one accounting server. If an
accounting server is currently configured, use the no form of the command to remove it from
the configuration. The IP address or host name you specify must match that of a previously
configured accounting server. If you use the optional port parameter, the command
configures the UDP port to use when connecting to the RADIUS accounting server. If a port
is already configured for the accounting server, the new port replaces the previously
configured port. For the port keyword, the number argument must be a value in the range
0–65535, with 1813 being the default.
Management Commands 147

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: To reconfigure a RADIUS accounting server to use the default UDP
port, set the number argument to 1813.
Format radius server host {auth | acct} {ipaddr | dnsname} [name servername] [port
number] [type server-type]
Mode Global Config
Field Description
ipaddr The IP address of the server.
dnsname The DNS name of the server.
0-65535 The port number that is used to connect to the specified RADIUS server.
servername The alias name to identify the server.
server-type Enter one of the following options:
• 0. Specifies a standard server.
• 1. Specifies a NETGEAR server.
no radius server host
The no radius server host command deletes the configured server entry from the list
of configured RADIUS servers. If the RADIUS authenticating server being removed is the
active server in the servers that are identified by the same server name, then the RADIUS
client selects another server for making RADIUS transactions. If the 'auth' token is used, the
previously configured RADIUS authentication server is removed from the configuration.
Similarly, if the 'acct' token is used, the previously configured RADIUS accounting server is
removed from the configuration. The ipaddr or dnsname argument must match the IP
address or DNS name of the previously configured RADIUS authentication or accounting
server.
Format no radius server host {auth | acct} {ipaddr | dnsname}
Mode Global Config
Command example:
(NETGEAR Switch) (Config) #radius server host acct 192.168.37.60
(NETGEAR Switch) (Config) #radius server host acct 192.168.37.60 port 1813
(NETGEAR Switch) (Config) #radius server host auth 192.168.37.60 name Network1_RS port

(NETGEAR Switch) (Config) #radius server host acct 192.168.37.60 name Network2_RS
(NETGEAR Switch) (Config) #no radius server host acct 192.168.37.60
Management Commands 148

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
radius server key
This command configures the key to be used in RADIUS client communication with the
specified server. Depending on whether the auth or acct token is used, the shared secret is
configured for the RADIUS authentication or RADIUS accounting server. The IP address or
hostname provided must match a previously configured server. When this command is
executed, the secret is prompted.
Text-based configuration supports Radius server’s secrets in encrypted and non-encrypted
format. When you save the configuration, these secret keys are stored in encrypted format
only. If you want to enter the key in encrypted format, enter the key along with the encrypted
keyword. In the output of the show running-config command (for information about the
command, see show running-config on page216), these secret keys are displayed in
encrypted format. You cannot show these keys in plain text format.
Note: The secret must be an alphanumeric value not exceeding 16
characters.
Format radius server key {auth | acct} {ipaddr | dnsname} encrypted password
Mode Global Config
Field Description
ipaddr The IP address of the server.
dnsname The DNS name of the server.
password The password in encrypted format.
Command example:
(NETGEAR Switch) (Config) #radius server key acct 10.240.4.10 encrypted encrypt-string
radius server msgauth
This command enables the message authenticator attribute to be used for the specified
RADIUS Authenticating server.
Format radius server msgauth [ipaddr | dnsname]
Mode Global Config
Field Description
ip addr The IP address of the server.
dnsname The DNS name of the server.
Management Commands 149

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no radius server msgauth
The no version of this command disables the message authenticator attribute to be used for
the specified RADIUS Authenticating server.
Format no radius server msgauth [ipaddr | dnsname]
Mode Global Config
radius server primary
This command specifies a configured server that should be the primary server in the group of
servers which have the same server name. Multiple primary servers can be configured for
each number of servers that have the same name. When the RADIUS client has to perform
transactions with an authenticating RADIUS server of specified name, the client uses the
primary server that has the specified server name by default. If the RADIUS client fails to
communicate with the primary server for any reason, the client uses the backup servers
configured with the same server name. These backup servers are identified as the
Secondary type.
Format radius server primary {ipaddr | dnsname}
Mode Global Config
Field Description
ip addr The IP address of the RADIUS Authenticating server.
dnsname The DNS name of the server.
radius server retransmit
This command configures the global parameter for the RADIUS client that specifies the
number of transmissions of the messages to be made before attempting the fall back server
upon unsuccessful communication with the current RADIUS authenticating server. When the
maximum number of retries are exhausted for the RADIUS accounting server and no
response is received, the client does not communicate with any other server.
Default 4
Format radius server retransmit retries
Mode Global Config
Field Description
retries The maximum number of transmission attempts in the range of 1 to 15.
Management Commands 150

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no radius server retransmit
The no version of this command sets the value of this global parameter to the default value.
Format no radius server retransmit
Mode Global Config
radius source-interface
Use this command to specify the physical or logical interface to use as the RADIUS client
source interface (Source IP address). If configured, the address of source Interface is used
for all RADIUS communications between the RADIUS server and the RADIUS client. The
selected source-interface IP address is used for filling the IP header of RADIUS management
protocol packets. This allows security devices (firewalls) to identify the source packets
coming from the specific switch.
If a source-interface is not specified, the primary IP address of the originating (outbound)
interface is used as the source address. If the configured interface is down, the RADIUS
client falls back to its default behavior.
Format radius source-interface {unit/slot/port | loopback loopback-id | vlan vlan-id
| serviceport}
Mode Global Config
Parameter Description
unit/slot/port The unit identifier assigned to the switch.
loopback-id Configures the loopback interface. The range of the loopback ID is 0 to 7.
vlan-id Configures the VLAN interface to use as the source IP address. The range of the VLAN ID is 1 to
4093.
no radius source-interface
Use this command to reset the RADIUS source interface to the default settings.
Format no radius source-interface
Mode Global Config
radius server timeout
This command configures the global parameter for the RADIUS client that specifies the
time-out value (in seconds) after which a request must be retransmitted to the RADIUS
server if no response is received. The time-out value is an integer in the range of 1 to 30
seconds.
Management Commands 151
