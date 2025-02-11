# icmp_throttling_commands_this_section_describes_the_commands_you_use_to_configure_options__4e1faa7c

Pages: 788-854

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ICMP Throttling Commands
This section describes the commands you use to configure options for the transmission of
various types of ICMP messages.
ip unreachables
Use this command to enable the generation of ICMP Destination Unreachable messages on
an interface or range of interfaces. By default, the generation of ICMP Destination
Unreachable messages is enabled.
Default enable
Format ip unreachables
Mode Interface Config
no ip unreachables
Use this command to prevent the generation of ICMP Destination Unreachable messages.
Format no ip unreachables
Mode Interface Config
ip redirects
Use this command to enable the generation of ICMP Redirect messages by the router. By
default, the generation of ICMP Redirect messages is enabled. You can use this command to
configure an interface, a range of interfaces, or all interfaces.
Default enable
Format ip redirects
Mode Global Config
Interface Config
no ip redirects
Use this command to prevent the generation of ICMP Redirect messages by the router.
Format no ip redirects
Mode Global Config
Interface Config
Routing Commands 788

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ipv6 redirects
Use this command to enable the generation of ICMPv6 Redirect messages by the router. By
default, the generation of ICMP Redirect messages is enabled. You can use this command to
configure an interface, a range of interfaces, or all interfaces.
Default enable
Format ipv6 redirects
Mode Interface Config
no ipv6 redirects
Use this command to prevent the generation of ICMPv6 Redirect messages by the router.
Format no ipv6 redirects
Mode Interface Config
ip icmp echo-reply
Use this command to enable the generation of ICMP Echo Reply messages by the router. By
default, the generation of ICMP Echo Reply messages is enabled.
Default enable
Format ip icmp echo-reply
Mode Global Config
no ip icmp echo-reply
Use this command to prevent the generation of ICMP Echo Reply messages by the router.
Format no ip icmp echo-reply
Mode Global Config
ip icmp error-interval
Use this command to limit the rate at which IPv4 ICMP error messages are sent. The rate
limit is configured as a token bucket, with two configurable parameters, burst-size and
burst-interval.
The burst-interval specifies how often the token bucket is initialized with burst-size
tokens. burst-interval is from 0 to 2147483647 milliseconds (msec). The burst-size is the
number of ICMP error messages that can be sent during one burst-interval. The range is
from 1 to 200 messages. To disable ICMP rate limiting, set the burst-interval to zero (0).
Routing Commands 789

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default burst-interval of 1000 msec.
burst-size of 100 messages
Format ip icmp error-interval burst-interval [burst-size]
Mode Global Config
no ip icmp error-interval
Use the no ip icmp error-interval command to return the burst-interval and
burst-size to their default values.
Format no ip icmp error-interval
Mode Global Config
Routing Commands 790

Captive Portal Commands

This section describes the CLI commands that you can use to manage the captive portal
features on the switch. The chapter contains the following sections:
• Captive Portal Global Commands
• Captive Portal Configuration Commands
• Captive Portal Status Commands
• Captive Portal Client Connection Commands
• Captive Portal Interface Commands
• Captive Portal Local User Commands
• Captive Portal User Group Commands

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Captive Portal Global Commands
The commands in this section enable you to configure the captive portal settings that affect
the captive portal feature on the switch and all captive portal instances.
captive-portal
Use this command to enter the Captive Portal Configuration Mode.
Format captive-portal
Mode Global Config
enable (Captive Portal Config Mode)
This command globally enables the captive portal feature on the switch.
Default Disable
Format enable
Mode Captive Portal Config
no enable (Captive Portal Config Mode)
The no enable command disables the captive portal functionality.
Format no enable
Mode Captive Portal Config
http port
This command configures an additional HTTP port. Valid port numbers are in the range of
0-65535, excluding port numbers 80 and 443 which are reserved. The HTTP port default is 0
which denotes no additional port and the default port (80) is used.
Default 0
Format http port port-number
Mode Captive Portal Config
Command example:
(NETGEAR Switch) (Config-CP) #http port 8080
(NETGEAR Switch) (Config-CP) #no http port
Captive Portal Commands 792

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no http port
This command removes the specified additional HTTP port.
Format no http port port-number
Mode Captive Portal Config
https port
This command configures an additional HTTPS secure port. The HTTPS secure port default
is 0 which denotes no additional port and the default port (443) is used. Port number 80 is
reserved.
Default 0
Format https port port-number
Mode Captive Portal Config
Parameter Description
port-num Port number in the range of 0-65535.
Command example:
(NETGEAR Switch) (Config-CP) #https port 60000
(NETGEAR Switch) (Config-CP) #no https port
no https port
This command set the HTTPS secure port to the default.
Format no https port port-number
Mode Captive Portal Config
snmp-server enable traps captive-portal
This command globally enables the captive portal traps. The specific captive portal traps are
configured using the trapflags command in Captive Portal Config Mode.
Default Disable
Format snmp-server enable traps captive-portal
Mode Global Config
Captive Portal Commands 793

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no snmp-server enable traps captive-portal
This command globally disables all the captive portal traps.
Format no snmp-server enable traps captive-portal
Mode Global Config
trapflags (Captive Portal Config Mode)
This command enables captive portal SNMP traps. If no parameters are specified, then all
traps are enabled. SNMP traps can also be enabled individually by supplying the optional
parameters.
The client-auth-failure option allows the SNMP agent to send a trap when a client
attempts to authenticate with a captive portal but is unsuccessful.
The client-connect option allows the SNMP agent to send a trap when a client
authenticates with and connects to a captive portal.
The client-db-full option allows the SNMP agent to send a trap each time an entry
cannot be added to the client database because it is full.
The client-disconnect option allows the SNMP agent to send a trap when a client
disconnects from a captive portal.
Default Disabled
Format trapflags [client-auth-failure | client-connect | client-db-full |
client-disconnect]
Mode Captive Portal Config
no trapflags
This command disables all captive portal SNMP traps when no parameters are specified. The
optional parameters specify individual traps to disable.
Format no trapflags [client-auth-failure | client-connect | client-db-full |
client-disconnect]
Mode Captive Portal Config
authentication timeout
This command configures the authentication time-out. If the captive portal user does not
enter valid credentials within this time limit, the authentication page needs to be served again
in order for the client to gain access to the network. The seconds variable is the
authentication time-out and is a number in the range of 60-600 seconds.
Captive Portal Commands 794

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default 300
Format authentication timeout seconds
Mode Captive Portal Config
no authentication timeout
This command sets the authentication timeout to the default value.
Format no authentication timeout
Mode Captive Portal Config
show captive-portal
This command reports status of the captive portal feature.
Format show captive-portal
Mode Privileged EXEC
Term Description
Administrative Shows whether the CP is enabled.
Mode
Operational Status Indicates whether the CP operational status is enabled or disabled.
Disable Reason If CP is disabled, this field displays the reason, which can be None, Administratively
Disabled, No IPv4 Address, or Routing Enabled, but no IPv4 routing interface.
Captive Portal IP Shows the IP address that the captive portal feature uses.
Address
show captive-portal status
This command reports status of all captive portal instances in the system.
Format show captive-portal status
Mode Privileged EXEC
Term Description
Additional HTTP Displays the port number of the additional HTTP port configured for traffic. A value of 0 indicates that
Port only port 80 is configured for HTTP traffic.
Additional HTTP Displays the port number of the additional HTTPS secure port. A value of 0 indicates no additional
Secure Port port and the default port (443) is used.
Captive Portal Commands 795

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Description
Peer Switch Displays the interval at which statistics are reported in the Cluster Controller. The reporting interval is
Statistics Reporting in the range of 0, 15-3600 seconds where 0 disables statistical reporting.
Interval
Authentication Displays the number of seconds to keep the authentication session open with the client. When the
Timeout timeout expires, the switch disconnects any active TCP or SSL connection with the client.
Supported Captive Shows the number of supported captive portals in the system.
Portals
Configured Captive Shows the number of captive portals configured on the switch.
Portals
Active Captive Shows the number of captive portal instances that are operationally enabled.
Portals
Local Supported Shows the number of users that can be added and configured using the local user database.
Users
Configured Local Shows the number of users that are configured from the local user database.
Users
System Supported Shows the total number of authenticated users that the system can support.
Users
Authenticated Shows the number of users currently authenticated to all captive portal instances on this switch.
Users
Command example:
(NETGEAR Switch) #show captive-portal status
Additional HTTP Port........................... 0
Additional HTTP Secure Port.................... 0
Peer Switch Statistics Reporting Interval...... 120
Authentication Timeout......................... 300
Supported Captive Portals...................... 10
Configured Captive Portals..................... 1
Active Captive Portals......................... 0
Local Supported Users.......................... 128
Configured Local Users......................... 0
System Supported Users......................... 1024
Authenticated Users............................ 0
Captive Portal Commands 796

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show captive-portal trapflags
This command shows which captive portal SNMP traps are enabled. The show trapflags
command shows the global captive portal traps configuration. For more information, see the
sample output of show trapflags on page141.
Format show captive-portal trapflags
Mode Privileged EXEC
Term Description
Client Shows whether the SNMP agent sends a trap when a client attempts to authenticate with a captive
Authentication portal but is unsuccessful.
Failure Traps
Client Connection Shows whether the SNMP agent sends a trap when a client authenticates with and connects to a
Traps captive portal.
Client Database Shows whether the SNMP agent sends a trap each time an entry cannot be added to the client
Full Traps database because it is full.
Client Shows whether the SNMP agent sends a trap when a client disconnects from a captive portal.
Disconnection
Traps
Captive Portal Configuration Commands
The commands in this section are related to captive portal configurations.
configuration (for captive portal)
Use this command to enter the Captive Portal Instance Mode.
The captive portal configuration, identified by CP ID 1, is the default CP configuration. You
can create up to nine additional captive portal configurations. The system supports a total of
ten CP configurations. The Captive Portal ID cp-id variable is a number in the range of
1-10.
Format configuration cp-id
Mode Captive Portal Config
Captive Portal Commands 797

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no configuration
This command deletes a captive portal configuration. The command fails if interfaces are
associated to this configuration. The default captive portal configuration cannot be deleted.
The Captive Portal ID cp-id variable is a number in the range of 1-10.
Format no configuration cp-id
Mode Captive Portal Config
enable (Captive Portal Instance)
This command enables a captive portal configuration.
Default Enable
Format enable
Mode Captive Portal Instance
no enable
This command disables a captive portal configuration.
Format no enable
Mode Captive Portal Instance
name
This command configures the name for a captive portal configuration. The cp-name can
contain up to 32 alphanumeric characters.
Format name cp-name
Mode Captive Portal Instance
protocol
This command configures the protocol mode for a captive portal configuration. The CP can
use HTTP or HTTPS protocols.
Default https
Format protocol {http | https}
Mode Captive Portal Instance
Captive Portal Commands 798

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
verification
This command configures the verification mode for a captive portal configuration. The type of
user verification to perform can be one of the following:
• guest. The user does not need to be authenticated by a database.
• local. The switch uses a local database to authenticated users.
• radius. The switch uses a database on a remote RADIUS server to authenticate users.
Default guest
Format verification {guest | local | radius}
Mode Captive Portal Instance
group
This command assigns a group ID to a captive portal configuration. Each Captive Portal
configuration must contain at least one group ID. The group-id can have a number in the
1–1024 range. Group ID 1 is the default.
Default group-ID 1
Format group group-id
Mode Captive Portal Instance
radius-auth-server
Use this command to configure a captive portal configuration RADIUS authentication server.
Default Disable
Format radius-auth-server server-name
Mode Captive Portal Instance
no radius-auth-server
This command disables a captive portal configuration RADIUS authentication server.
Format no radius-auth-server
Mode Captive Portal Instance
Captive Portal Commands 799

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
redirect
This command enables the redirect mode for a captive portal configuration.
Default Disable
Format redirect
Mode Captive Portal Instance
no redirect
This command disables the redirect mode for a captive portal configuration.
Format no redirect
Mode Captive Portal Instance
redirect-url
Use this command to specify the URL to which the newly authenticated client is redirected if
the URL Redirect Mode is enabled. This command is only available if the redirect mode is
enabled.
Format redirect-url url
Mode Captive Portal Instance
max-bandwidth-up
This command configures the maximum rate at which a client can send data into the network.
Default 0
Format max-bandwidth-up rate
Mode Captive Portal Config
Parameter Description
rate Rate in bps. 0 indicates limit not enforced.
no max-bandwidth-up
This command sets the maximum rate at which a client can send data into the network to the
default.
Format no max-bandwidth-up
Mode Captive Portal Instance
Captive Portal Commands 800

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
max-bandwidth-down
This command configures the maximum rate at which a client can receive data from the
network.
Default 0
Format max-bandwidth-down rate
Mode Captive Portal Instance
Parameter Description
rate Rate in bps. 0 indicates limit not enforced.
no max-bandwidth-down
This command sets to the default the maximum rate at which a client can receive data from
the network.
Format no max-bandwidth-down
Mode Captive Portal Instance
max-input-octets
This command configures the maximum number of octets the user is allowed to transmit.
After this limit has been reached the user will be disconnected. If the value is set to 0 then the
limit is not enforced.
Default 0
Format max-input-octets bytes
Mode Captive Portal Instance
Parameter Description
bytes Input octets in bytes. 0 indicates limit not enforced.
no max-input-octets
This command sets to the default the maximum number of octets the user is allowed to
transmit.
Format no max-input-octets
Mode Captive Portal Instance
Captive Portal Commands 801

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
max-output-octets
This command configures the maximum number of octets the user is allowed to receive. After
this limit has been reached the user will be disconnected. If the value is set to 0 then the limit
is not enforced.
Default 0
Format max-output-octets bytes
Mode Captive Portal Instance
Parameter Description
bytes Output octets in bytes. 0 indicates limit not enforced.
no max-output-octets
This command sets to the default the maximum number of octets the user is allowed to
receive.
Format no max-output-octets
Mode Captive Portal Instance
max-total-octets
This command configures the maximum number of octets the user is allowed to transfer, i.e.,
the sum of octets transmitted and received. After this limit has been reached the user will be
disconnected. If the value is set to 0, then the limit is not enforced.
Default 0
Format max-total-octets bytes
Mode Captive Portal Instance
Parameter Description
bytes Total octets in bytes. 0 indicates limit not enforced.
no max-total-octets
This command sets to the default the maximum number of octets the user is allowed to
transfer, that is, the sum of octets transmitted and received.
Format no max-total-octets
Mode Captive Portal Instance
Captive Portal Commands 802

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
session-timeout (Captive Portal Instance)
This command configures the session time-out for a captive portal configuration. The
timeout variable is a number that represents the session time-out in seconds. Use 0 to
indicate that the time-out is not enforced.
Default 0
Format session-timeout timeout
Mode Captive Portal Instance
no session-timeout
Use this command to set the session time-out for a captive portal configuration to the default
value.
Format no session-timeout
Mode Captive Portal Instance
idle-timeout
This command configures the idle time-out for a captive portal configuration. The timeout
variable is a number that represents the idle time-out in seconds. Use 0 to indicate that the
time-out is not enforced.
Default 0
Format idle-timeout timeout
Mode Captive Portal Instance
no idle-timeout
Use this command to set the idle time-out for a captive portal configuration to the default
value.
Format no idle-timeout
Mode Captive Portal Instance
locale
This command is not intended to be a user command. The administrator must use the WEB
user interface to create and customize captive portal web content. The command is primarily
used by the show running config command and process as it provides the ability to
save and restore configurations using a text-based format.
Captive Portal Commands 803

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format locale web-id
Mode Captive Portal Instance
do (Captive Portal Instance mode)
Use this command to run Privileged Exec mode commands.
Format do
Mode Captive Portal Instance
script-text
Use this command to specify, in UTF-16 byte stream format, the text that is displayed if
javascript is disabled in the users browser.
Format script-text UTF-16
Mode Captive Portal Instance
show (Captive Portal Instance)
Use this command to display the switches options and settings.
Format show
Mode Captive Portal Instance
wip-msg
Use this command to specify, in UTF-16 byte stream format, the message displayed when
authentication is in progress.
Format wip-msg UTF-16
Mode Captive Portal Instance
interface (Captive Portal Instance)
This command associates an interface to a captive portal configuration or removes the
interface captive portal association.
Format interface unit/slot/port
Mode Captive Portal Instance
Captive Portal Commands 804

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no interface
This command removes the association between an interface and a captive portal
configuration.
Format no interface unit/slot/port
Mode Captive Portal Instance
block
This command blocks all traffic for a captive portal configuration.
Format block
Mode Captive Portal Instance
no block
This command unblocks all traffic for a captive portal configuration.
Format no block
Mode Captive Portal Instance
clear (Captive Portal Instance Config)
This command sets the configuration for this instance to the default values.
Format clear
Mode Captive Portal Instance
user-logout
This command enables the ability for an authenticated user to de-authenticate from the
network. This command is configurable for a captive portal configuration.
Format user-logout
Mode Captive Portal Instance
no user-logout
This command removes the association between an interface and a captive portal
configuration.
Format no user-logout
Mode Captive Portal Instance
Captive Portal Commands 805

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
background-color
Use this command to customize the background color of the Captive Portal authentication
page using a well-known color name or RGB value. For example, red or RGB hex-code, that
is, #FF0000. The range of color-code is 1-32 characters.
Default #BFBFBF
Format background-color color-code
Mode Captive Portal Instance
foreground-color
Use this command to customize the foreground color of the Captive Portal authentication
page using a well-known color name or RGB value. For example, red or RGB hex-code, that
is, #FF0000. The range of color-code is 1-32 characters.
Default #999999
Format foreground-color color-code
Mode Captive Portal Instance
separator-color
Use this command to customize the separator bar color of the Captive Portal authentication
page using a well-known color name or RGB value. For example, red or RGB hex-code; that
is, #FF0000.The range of color-code is 1-32 characters.
Default #BFBFBF
Format separator-color color-code
Mode Captive Portal Instance
Captive Portal Commands 806

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Captive Portal Status Commands
Use the commands in this section to view information about the status of one or more captive
portal instances.
show captive-portal configuration
This command displays the operational status of each captive portal configuration. The
cp-id variable is the captive portal ID, which ranges from 1-10.
Format show captive-portal configuration cp-id
Mode Privileged EXEC
Term Description
CP ID Shows the captive portal ID.
CP Name Shows the captive portal name.
Operational Status Shows whether the captive portal is enabled or disabled.
Disable Reason If the captive portal is disabled, this field indicates the reason.
Blocked Status Shows the blocked status, which is Blocked or Not Blocked.
Authenticated Shows the number of authenticated users connected to the network through this captive portal.
Users
Configured Locales Shows the number of locales defined for this captive portal.
show captive-portal configuration interface
This command displays information for all interfaces assigned to a captive portal
configuration or a specific interface assigned to a captive portal configuration. The cp-id
variable is the captive portal ID, which ranges from 1-10.
Format show captive-portal configuration cp-id interface [unit/slot/port]
Mode Privileged EXEC
Term Description
CP ID Shows the captive portal ID.
CP Name Shows the captive portal name.
Interface unit/slot/port
Interface Describes the interface.
Description
Operational Status Shows whether the captive portal is enabled or disabled
Captive Portal Commands 807

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Description
Block Status Shows the blocked status, which is Blocked or Not Blocked.
If you include the optional unit/slot/port information, the following additional information appears:
Disable Reason If the captive portal is disabled, this field indicates the reason.
Authenticated Shows the number of authenticated users connected to the network through this captive portal.
Users
show captive-portal configuration status
This command displays information of all configured captive portal configurations or a
specific captive portal configuration. The cp-id variable is the captive portal ID, which
ranges from 1-10.
Format show captive-portal configuration cp-id status
Mode Privileged EXEC
Term Description
CP ID Shows the captive portal ID.
CP Name Shows the captive portal name.
CP Mode Shows whether the CP is enabled or disabled.
Protocol Mode Shows the current connection protocol, which is either HTTP or HTTPS.
Verification Mode Shows the current account type, which is Guest, Local, or RADIUS.
URL Redirect Indicates whether the Redirect URL Mode is enabled or disabled.
Mode
Max Bandwidth Up The maximum rate in bytes per second (bps) at which a client can send data into the network.
(bytes/sec)
Max Bandwidth The maximum rate in bps at which a client can receive data from the network.
Down (bytes/sec)
Max Input Octets The maximum number of octets the user is allowed to transmit.
(bytes)
Max Output Octets The maximum number of octets the user is allowed to receive.
(bytes)
Max Total Octets The maximum number of octets the user is allowed to transfer, i.e., the sum of octets transmitted
(bytes) and received.
Session Timeout Shows the number of seconds a user is permitted to remain connected to the network. Once the
(seconds) Session Timeout value is reached, the user is logged out automatically. A value of 0 means that the
user does not have a session Timeout limit.
Idle Timeout Shows the number of seconds the user can remain idle before the switch automatically logs the user
(seconds) out. A value of 0 means that the user will not be logged out automatically.
Captive Portal Commands 808

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show captive-portal configuration locales
This command displays locales associated with a specific captive portal configuration. The
cp-id variable is the captive portal ID, which ranges from 1-10.
Format show captive-portal configuration cp-id locales
Mode Privileged EXEC
Term Description
Locale Code Two-letter abbreviation for languages.
Locale Link The names of the languages.
Captive Portal Client Connection
Commands
Use the commands in this section to view information about the clients connected to the
captive portals configured on the switch.
show captive-portal client status
This command displays client connection details or a connection summary for connected
captive portal users. Use the optional macaddr keyword, which is the MAC address of a
client, to view additional information about that client.
Format show captive-portal client [macaddr] status
Mode Privileged EXEC
Term Description
Client MAC Identifies the MAC address of the wireless client (if applicable).
Address
Client IP Address Identifies the IP address of the wireless client (if applicable).
Protocol Mode Shows the current connection protocol, which is either HTTP or HTTPS.
Verification Mode Shows the current account type, which is Guest, Local, or RADIUS.
Session Time Shows the amount of time that has passed since the client was authorized.
If you specify a client MAC address, the following additional information displays:
CP ID Shows the captive portal ID the connected client is using.
CP Name Shows the name of the captive portal the connected client is using.
Captive Portal Commands 809

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Description
Interface Valid slot and port number separated by a forward slash.
Interface Describes the interface.
Description
User Name Displays the user name (or Guest ID) of the connected client.
If cluster support is available, the following fields display:
Switch MAC Identifies the MAC address of the switch (if applicable).
Address
Switch IP Address Identifies the IP address of the switch (if applicable).
Switch Type (local Shows the current switch type, which is local or peer.
or peer)
show captive-portal client statistics
This command displays the statistics for a specific captive portal client.
Format show captive-portal client macaddr statistics
Mode Privileged EXEC
Term Description
Client MAC Identifies the MAC address of the wireless client (if applicable).
Address
Bytes Received Total bytes the client has received.
Bytes Transmitted Total bytes the client has transmitted.
Packets Total packets the client has transmitted.
Transmitted
Packets Received Total packets the client has received.
show captive-portal interface client status
This command displays information about clients authenticated on all interfaces or a specific
interface.
Format show captive-portal interface [unit/slot/port] client status
Mode Privileged EXEC
Captive Portal Commands 810

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Description
Interface Valid unit, slot and port number.
Interface Describes the interface.
Description
Client MAC Identifies the MAC address of the wireless client (if applicable).
Address
If you use the optional unit/slot/port information, the following additional information appears:
Client IP Address Identifies the IP address of the wireless client (if applicable).
CP ID Shows the captive portal ID the connected client is using.
CP Name Shows the name of the captive portal the connected client is using.
Protocol Shows the current connection protocol, which is either HTTP or HTTPS.
Verification Shows the current account type, which is Guest, Local, or RADIUS.
User Name Displays the user name (or Guest ID) of the connected client.
show captive-portal configuration client status
This command displays the clients authenticated to all captive portal configurations or a
specific configuration. The optional cp-id variable is the captive portal ID, which ranges
from 1-10.
Format show captive-portal configuration [cp-id] client status
Mode Privileged EXEC
Term Description
CP ID Shows the captive portal ID the connected client is using.
CP Name Shows the name of the captive portal the connected client is using.
Client MAC Identifies the MAC address of the wireless client (if applicable).
Address
If you use the optional cp-id information, the following additional information appears:
Client IP Address Identifies the IP address of the wireless client (if applicable).
Interface Valid slot and port number separated by a forward slash.
Interface Describes the interface.
Description
captive-portal client deauthenticate
This command deauthenticates a specific captive portal client. You can specify a captive
portal configuration ID to indicate the captive portal configuration that the client is
deauthenticating from. The optional cp-id variable is the captive portal ID, which ranges
Captive Portal Commands 811

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
from 1-10. If no value is entered, then the specified clients (or all clients) are deauthenticated
from all captive portal configurations.
You can use the optional macaddr variable to specify the MAC address of the client to
deauthenticate. If no value is specified, then all clients are deauthenticated from the specified
captive portal configuration (or all configurations).
Format captive-portal client deauthenticate [cp-id] [macaddr]
Mode Privileged EXEC
Captive Portal Interface Commands
Use the commands in this section to view information about the interfaces on the switch that
are associated with captive portals or that are capable of supporting a captive portal.
show captive-portal interface configuration status
This command displays the interface to configuration assignments for all captive portal
configurations or a specific configuration. The optional cp-id variable is the captive portal
ID, which ranges from 1-10.
Format show captive-portal interface configuration [cp-id] status
Mode Privileged EXEC
Term Description
CP ID Shows the captive portal ID the connected client is using.
CP Name Shows the name of the captive portal the connected client is using.
Interface Valid slot and port number separated by a forward slash.
Interface Describes the interface.
Description
Type Shows the type of interface.
show captive-portal interface capability
This command displays all the captive portal eligible interfaces or the interface capabilities for
a specific captive portal interface.
Format show captive-portal interface capability [unit/slot/port]
Mode Privileged EXEC
Captive Portal Commands 812

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Description
Interface Valid slot and port number separated by a forward slash.
Interface Describes the interface.
Description
Type Shows the type of interface.
If you use the optional unit/slot/port information, the following additional information appears:
Session Timeout Indicates whether or not this field is supported by the specified captive portal interface.
Idle Timeout Indicates whether or not this field is supported by the specified captive portal interface.
Bytes Received Indicates whether or not this field is supported by the specified captive portal interface.
Counter
Bytes Transmitted Indicates whether or not this field is supported by the specified captive portal interface.
Counter
Packets Received Indicates whether or not this field is supported by the specified captive portal interface.
Counter
Packets Indicates whether or not this field is supported by the specified captive portal interface.
Transmitted
Counter
Roaming Indicates whether or not this field is supported by the specified captive portal interface.
Captive Portal Local User Commands
Use these commands to view and configure captive portal users in the local database.
user (Captive Portal Config Mode)
This command is used to create a local user. The user-id variable is the user ID, which can
be a number between 1 and 128. The username variable is the name of the user and can
have up to 32 alphanumeric characters. The password variable is 8-64 characters.
Two ways exist to create a user: with the user name command or with the user password
command. If the user is created with the user name command, you must assign the
password with the user password command. If the user is created with the user
password command, you can assign the name with the user name command at a later
time.
You can also modify the password after you created a user by using the user password
command with the user ID and a new password.
Format user user-id name username
Mode Captive Portal Config
Captive Portal Commands 813

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format user user-id password password
Mode Captive Portal Config
Command example:
The following example uses name to create the user.
(NETGEAR Switch)(Config-CP) #user 1 name test
Command example:
The following example uses password to create the user:
(NETGEAR Switch)(Config-CP) #user 1 password test1234
no user
This command deletes a user from the local user database. If the user has an existing
session, it is disconnected. The user-id variable is the user ID, which can be a number
between 1 and 128.
Format no user user-id
Mode Captive Portal Config
Command example:
(NETGEAR Switch)(Config-CP) #no user 1
user name (Captive Portal Config)
This command assigns a name to the User ID. This name is used at the client station for
authentication. The user-id variable is the local user ID created with the user command
and can be from 1 to 128 characters. The username variable is the name of the user and
can have up to 32 alphanumeric characters.
Format user user-id name username
Mode Captive Portal Config
Command example:
(NETGEAR Switch)(Config-CP) #user 1 name johnsmith
user password (Captive Portal Config)
This command sets or modifies the password for the associated captive portal user. The
user-id variable is the local user ID created with the user command and can be from 1 to
Captive Portal Commands 814

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
128 characters. The password variable is the user id’s password and can have from 8 to 64
alphanumeric characters.
Format user user-id password password
Mode Captive Portal Config
Command example:
(NETGEAR Switch)(Config-CP) #user 1 password
Enter Password (8 - 64 characters):
Re-enter password:
user password encrypted
This command modifies the password for the associated captive portal user. The command
accepts the password in an encrypted format. This command is used primarily by the show
running config command process.
The user-id variable is the local user ID created with the user command. The
encrypted-pwd variable is the password in encrypted format, which can be up to 128
hexadecimal characters.
Format user user-id password encrypted encrypted-pwd
Mode Captive Portal Config
Command example:
(NETGEAR Switch)(Config-CP) #user 1 password encrypted 42 65 74 74 65 72 20 73 61 66 65
20 74 68 61 6e 20 73 6f 72 72 79
user group (captive portal local user commands)
This command assigns/modifies the group name for the associated captive portal user. The
user-id variable is the user ID, which is a number in the range of 1 to 128. The
group-name variable is a name up to 32 characters.
Format user user-id group group-name
Mode Captive Portal Config
Command example:
(NETGEAR Switch)(Config-CP) #user 1 group 123
user session-timeout
This command sets the session timeout value for the associated captive portal user. The
user-id variable is the ID of a user configured in the local database, and is a number in the
Captive Portal Commands 815

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
range of 1 to 128. The timeout variable is a number that represents the session time-out in
seconds. Use 0 to indicate that the time-out is not enforced.
Default 0
Format user user-id session-timeout timeout
Mode Captive Portal Config
Command example:
(NETGEAR Switch)(Config-CP) #user 1 session-timeout 86400
no user session-timeout
This command sets the session timeout value for the associated captive portal user to the
default value. The user-id variable is the ID of a user configured in the local database, and
is a number in the range of 1 to 128.
Format no user user-id session-timeout
Mode Captive Portal Config
Command example:
(NETGEAR Switch)(Config-CP) #no user 1 session-timeout
user idle-timeout
This command sets the session idle timeout value for the associated captive portal user. The
user-id variable is the ID of a user configured in the local database, and is a number in the
range of 1 to 128. The timeout variable is a number that represents the idle time-out in
seconds. Use 0 to indicate that the time-out is not enforced.
Default 0
Format user user-id idle-timeout timeout
Mode Captive Portal Config
Command example:
(NETGEAR Switch)(Config-CP) #user 1 idle-timeout 600
Captive Portal Commands 816

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no user idle-timeout
This command sets the session idle timeout value for the associated captive portal user to
the default value. The user-id variable is the ID of a user configured in the local database,
and is a number in the range of 1 to 128.
Format no user user-id idle-timeout
Mode Captive Portal Config
Command example:
(NETGEAR Switch)(Config-CP) #no user 1 idle-timeout
user max-bandwidth-up
This command is used to configure the bandwidth in bytes per second (bps, with the bps
variable) at which the client can send data into the network. 0 denotes using the default value
configured for the captive portal. The user-id variable is the ID of a user configured in the
local database, and is a number in the range of 1 to 128.
Default 0
Format user user-id max-bandwidth-up bps
Mode Captive Portal Config
Parameter Description
user-id User ID from 1 to 128 characters.
bps Client transmit rate in bytes per second (bps). 0 denotes unlimited bandwidth.
no user max-bandwidth-up
Use this command to set to the default the bandwidth at which the client can send data into
the network. The user-id variable is the ID of a user configured in the local database, and
is a number in the range of 1 to 128.
Format no user user-id max-bandwidth-up
Mode Captive Portal Config
user max-bandwidth-down
This command is used configure the bandwidth in bytes per second (bps, with the variable) at
which the client can receive data from the network. 0 denotes using the default value
configured for the captive portal. The user-id variable is the ID of a user configured in the
local database, and is a number in the range of 1 to 128.
Captive Portal Commands 817

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default 0
Format user user-id max-bandwidth-down bps
Mode Captive Portal Config
Parameter Description
user-id User ID from 1 to 128 characters.
bps Client receive rate in bps. 0 denotes unlimited bandwidth.
no user max-bandwidth down
Use this command to set to the default value the bandwidth at which the client can receive
data from the network. The user-id variable is the ID of a user configured in the local
database, and is a number in the range of 1 to 128.
Format no user user-id max-bandwidth-down
Mode Captive Portal Config
user max-input-octets
This command is used to limit the number of octets in bytes that the user is allowed to
transmit. After this limit has been reached, the user will be disconnected. 0 octets denote
unlimited transmission. The user-id variable is the ID of a user configured in the local
database, and is a number in the range of 1 to 128.
Default 0
Format user user-id max-input-octets octets
Mode Captive Portal Config
Parameter Description
user-id User ID from 1 to 128 characters.
octets Number of bytes.
no user max-input-octets
Use this command to set to the default the number of octets in bytes that the user is allowed
to transmit. The user-id variable is the ID of a user configured in the local database, and is
a number in the range of 1 to 128.
Format no user user-id max-input-octets
Mode Captive Portal Config
Captive Portal Commands 818

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
user max-output-octets
This command is used to limit the number of octets in bytes that the user is allowed to
receive. After this limit has been reached, the user will be disconnected. 0 octets denote
unlimited transmission. The user-id variable is the ID of a user configured in the local
database, and is a number in the range of 1 to 128.
Default 0
Format user user-id max-output-octets octets
Mode Captive Portal Config
Parameter Description
user-id User ID from 1 to 128 characters.
octets Number of bytes.
no user max-output-octets
Use this command to set to the default the number of octets in bytes that the user is allowed
to receive. The user-id variable is the ID of a user configured in the local database, and is
a number in the range of 1 to 128.
Format no user user-id max-output-octets
Mode Captive Portal Config
user max-total-octets
This command is used to limit the number of octets in bytes that the user is allowed to
transmit and receive. The maximum number of octets is the sum of octets transmitted and
received. After this limit has been reached, the user will be disconnected. 0 octets denote
unlimited transmission. The user-id variable is the ID of a user configured in the local
database, and is a number in the range of 1 to 128.
Default 0
Format user user-id max-total-octets octets
Mode Captive Portal Config
Parameter Description
user-id User ID from 1 to 128 characters.
octets Number of bytes.
Captive Portal Commands 819

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no user max-total-octets
Use this command to set to the default the number of octets in bytes that the user is allowed
to transmit and receive. The user-id variable is the ID of a user configured in the local
database, and is a number in the range of 1 to 128.
Format no user user-id max-total-octets
Mode Captive Portal Config
show captive-portal user
This command displays all configured users or a specific user in the captive portal local user
database. Enter the optional user ID to view information about the specified user. The
optional user-id variable is the ID of a user configured in the local database, and is a
number in the range of 1 to 128. Enter the group keyword or the group keyword and
group-id variable to view the user information organized by groups.
Format show captive-portal user [user-id] [group [group-id]]
Mode Privileged EXEC
Field Description
User ID Displays the ID of the user.
User Name Displays the user name.
Session Timeout Displays the number of seconds the user can remain in a session before being disconnected from
the Captive Portal.
Idle Timeout Displays the number of seconds the user can remain idle before being disconnected from the
Captive Portal.
Group ID Displays the group identifier for the group to which the user belongs.
When you include the [user-id] variable, the following information also displays:
Password Indicates whether a password has been configured for the user.
Configured
Max Bandwidth Up The maximum rate in bytes per second (bps) at which a client can send data into the network.
(bps)
Max Bandwidth The maximum rate in bps at which a client can receive data from the network.
Down (bps)
Max Bandwidth The maximum number of octets the user is allowed to transmit.
Input Octets (bytes)
Captive Portal Commands 820

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Description
Max Bandwidth The maximum number of octets the user is allowed to receive.
Output Octets
(bytes)
Max Bandwidth The maximum number of octets the user is allowed to transfer, i.e., the sum of octets transmitted
Total Octets (bytes) and received.
clear captive-portal users
This command deletes all captive portal user entries.
Format clear captive-portal users
Mode Privileged EXEC
Captive Portal User Group Commands
Use the following commands to configure CP user groups.
user group (captive portal user group commands)
Use this command to create a user group. The group-id variable is a number in the range
of 1–10.
Format user group group-id
Mode Captive Portal Config
no user group
Use this command to delete a user group. The group-id variable is a number in the range
of 1–10.
Format no user group group-id
Mode Captive Portal Config
user group name
Use this command to configure a group name. The group-id variable is a number in the
range of 1–10. The name variable can be up to 32 alphanumeric characters.
Format user group group-id name name
Mode Captive Portal Config
Captive Portal Commands 821

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
user group moveusers
This command moves existing users from one user group to another. Note that the
destination group must already exist before a move can be successful. The group-id and
destination-group-id variables are each a number in the range of 1-10.
Format user group group-id moveusers destination-group-id
Mode Captive Portal Config
Command example:
(NETGEAR Switch)(Config-CP) #user group 2 moveusers 3
Captive Portal Commands 822

IPv6 Commands

This chapter describes the IPv6 commands. The chapter contains the following sections:
• Tunnel Interface Commands
• Loopback Interface Commands
• IPv6 Routing Commands
• OSPFv3 Commands
• DHCPv6 Commands
The commands in this chapter are in one of three functional groups:
• Show commands. Display switch settings, statistics, and other information.
• Configuration commands. Configure features and options of the switch. For every
configuration command, there is a show command that displays the configuration setting.
• Clear commands. Clear some or all of the settings to factory defaults.
Note: For information about IPv6 management commands, see IPv6
Management Commands.

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Tunnel Interface Commands
The commands in this section describe how to create, delete, and manage tunnel
interfaces.Several different types of tunnels provide functionality to facilitate the transition of
IPv4 networks to IPv6 networks. These tunnels are divided into two classes: configured and
automatic. The distinction is that configured tunnels are explicitly configured with a
destination or endpoint of the tunnel. Automatic tunnels, in contrast, infer the endpoint of the
tunnel from the destination address of packets routed into the tunnel. To assign an IP
address to the tunnel interface, see ip address on page665. To assign an IPv6 address to
the tunnel interface, see ipv6 address on page828.
interface tunnel
Use this command to enter the Interface Config mode for a tunnel interface. The tunnel-id
range is 0 to 7.
Format interface tunnel tunnel-id
Mode Global Config
no interface tunnel
This command removes the tunnel interface and associated configuration parameters for the
specified tunnel interface.
Format no interface tunnel tunnel-id
Mode Global Config
tunnel source
This command specifies the source transport address of the tunnel, either explicitly or by
reference to an interface.
Format tunnel source {ipv4-address | ethernet unit/slot/port}
Mode Interface Config
tunnel destination
This command specifies the destination transport address of the tunnel.
Format tunnel destination ipv4-address
Mode Interface Config
IPv6 Commands 824

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
tunnel mode ipv6ip
This command specifies the mode of the tunnel. With the optional 6to4 argument, the tunnel
mode is set to 6to4 automatic. Without the optional 6to4 argument, the tunnel mode is
configured.
Format tunnel mode ipv6ip [6to4]
Mode Interface Config
show interface tunnel
This command displays the parameters related to tunnel such as tunnel mode, tunnel source
address and tunnel destination address.
Format show interface tunnel [tunnel-id]
Mode Privileged EXEC
If you do not specify a tunnel ID, the command shows the following information for each
configured tunnel.
Term Definition
Tunnel ID The tunnel identification number.
Interface The name of the tunnel interface.
Tunnel Mode The tunnel mode.
Source Address The source transport address of the tunnel.
Destination The destination transport address of the tunnel.
Address
If you specify a tunnel ID, the command shows the following information for the tunnel.
Term Definition
Interface Link Shows whether the link is up or down.
Status
MTU Size The maximum transmission unit for packets on the interface.
IPv6 If you enable IPv6 on the interface and assign an address, the IPv6 address and prefix display.
Address/Length
IPv6 Commands 825

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Loopback Interface Commands
The commands in this section describe how to create, delete, and manage loopback
interfaces. A loopback interface is always expected to be up. This interface can provide the
source address for sent packets and can receive both local and remote packets. The
loopback interface is typically used by routing protocols.
To assign an IP address to the loopback interface, see ip address on page665. To assign
an IPv6 address to the loopback interface, see ipv6 address on page828.
interface loopback
Use this command to enter the Interface Config mode for a loopback interface. The range of
the loopback ID is 0 to 7.
Format interface loopback loopback-id
Mode Global Config
no interface loopback
This command removes the loopback interface and associated configuration parameters for
the specified loopback interface.
Format no interface loopback loopback-id
Mode Global Config
show interface loopback
This command displays information about configured loopback interfaces.
Format show interface loopback [loopback-id]
Mode Privileged EXEC
If you do not specify a loopback ID, the following information appears for each loopback
interface on the system.
Term Definition
Loopback ID The loopback ID associated with the rest of the information in the row.
Interface The interface name.
IP Address The IPv4 address of the interface.
IPv6 Commands 826

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If you specify a loopback ID, the following information appears.
Term Definition
Interface Link Shows whether the link is up or down.
Status
IP Address The IPv4 address of the interface.
MTU size The maximum transmission size for packets on this interface, in bytes.
IPv6 Routing Commands
This section describes the IPv6 commands you use to configure IPv6 on the system and on
the interfaces. This section also describes IPv6 management commands and show
commands.
ipv6 hop-limit
This command defines the unicast hop count used in ipv6 packets originated by the node.
The value is also included in router advertisements. Valid values for hops are 1-255
inclusive. The default “not configured” means that a value of zero is sent in router
advertisements and a value of 64 is sent in packets originated by the node. Note that this is
not the same as configuring a value of 64.
Default not configured
Format ipv6 hop-limit hops
Mode Global Config
no ipv6 hop-limit
This command returns the unicast hop count to the default.
Format no ipv6 hop-limit
Mode Global Config
ipv6 unicast-routing
Use this command to enable the forwarding of IPv6 unicast datagrams.
Default disabled
Format ipv6 unicast-routing
Mode Global Config
IPv6 Commands 827

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ipv6 unicast-routing
Use this command to disable the forwarding of IPv6 unicast datagrams.
Format no ipv6 unicast-routing
Mode Global Config
ipv6 enable
Use this command to enable IPv6 routing on an interface or range of interfaces, including
tunnel and loopback interfaces, that has not been configured with an explicit IPv6 address.
When you use this command, the interface is automatically configured with a link-local
address. You do not need to use this command if you configured an IPv6 global address on
the interface.
Default disabled
Format ipv6 enable
Mode Interface Config
no ipv6 enable
Use this command to disable IPv6 routing on an interface.
Format no ipv6 enable
Mode Interface Config
ipv6 address
Use this command to configure an IPv6 address on an interface or range of interfaces,
including tunnel and loopback interfaces, and to enable IPv6 processing on this interface.
You can assign multiple globally reachable addresses to an interface by using this command.
You do not need to assign a link-local address by using this command since one is
automatically created. The prefix field consists of the bits of the address to be configured.
The prefix_length designates how many of the high-order contiguous bits of the address
make up the prefix.
You can express IPv6 addresses in eight blocks. Also of note is that instead of a period, a
colon now separates each block. For simplification, leading zeros of each 16 bit block can be
omitted. One sequence of 16 bit blocks containing only zeros can be replaced with a double
colon “::”, but not more than one at a time (otherwise it is no longer a unique representation).
• Dropping zeros: 3ffe:ffff:100:f101:0:0:0:1 becomes 3ffe:ffff:100:f101::1
• Local host: 0000:0000:0000:0000:0000:0000:0000:0001 becomes ::1
• Any host: 0000:0000:0000:0000:0000:0000:0000:0000 becomes ::
The hexadecimal letters in the IPv6 addresses are not case-sensitive. An example of an IPv6
prefix and prefix length is 3ffe:1::1234/64.
IPv6 Commands 828

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The optional eui-64 field designates that IPv6 processing on the interfaces was enabled
using an EUI-64 interface ID in the low order 64 bits of the address. If you use this option, the
value of prefix_length must be 64 bits.
Format ipv6 address prefix/prefix_length [eui64]
Mode Interface Config
no ipv6 address
Use this command to remove all IPv6 addresses on an interface or specified IPv6 address.
The prefix parameter consists of the bits of the address to be configured. The
prefix_length designates how many of the high-order contiguous bits of the address
comprise the prefix.The optional eui-64 field designates that IPv6 processing on the
interfaces was enabled using an EUI-64 interface ID in the low order 64 bits of the address.
If you do not supply any parameters, the command deletes all the IPv6 addresses on an
interface.
Format no ipv6 address [prefix/prefix_length] [eui64]
Mode Interface Config
ipv6 address autoconfig
Use this command to allow an in-band interface to acquire an IPv6 address through IPv6
Neighbor Discovery Protocol (NDP) and through the use of Router Advertisement messages.
Default disabled
Format ipv6 address autoconfig
Mode Interface Config
no ipv6 address autoconfig
This command the IPv6 autoconfiguration status on an interface to the default value.
Format no ipv6 address autoconfig
Mode Interface Config
IPv6 Commands 829

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ipv6 address dhcp
This command enables the DHCPv6 client on an in-band interface so that it can acquire
network information, such as the IPv6 address, from a network DHCP server.
Default disabled
Format ipv6 address dhcp
Mode Interface Config
no ipv6 address dhcp
This command releases a leased address and disables DHCPv6 on an interface.
Format no ipv6 address dhcp
Mode Interface Config
ipv6 route
Use this command to configure an IPv6 static route. The ipv6-prefix is the IPv6 network
that is the destination of the static route. The prefix_length is the length of the IPv6
prefix—a decimal value (usually 0-64) that shows how many of the high-order contiguous bits
of the address comprise the prefix (the network portion of the address). A slash mark must
precede the prefix_length. The next-hop-address is the IPv6 address of the next hop
that can be used to reach the specified network. Specifying Null0 as nexthop parameter
adds a static reject route.
The preference parameter is a value the router uses to compare this route with routes from
other route sources that have the same destination. The range for preference is 1–255,
and the default value is 1.
You can specify a unit/slot/port or vlan-id or tunnel_id interface to identify direct
static routes from point-to-point and broadcast interfaces.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id
parameter is a number in the range of 1–4093.
The interface must be specified when using a link-local address as the next hop. A route with
a preference of 255 cannot be used to forward traffic.
Default disabled
Format ipv6 route ipv6-prefix/prefix_length {next-hop-address | Null0 | interface
{unit/slot/port | vlan vlan-id | tunnel tunnel_id} next-hop-address}
[preference]
Mode Global Config
IPv6 Commands 830

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ipv6 route
Use this command to delete an IPv6 static route. Use the command without the optional
parameters to delete all static routes to the specified destination. Use the preference
parameter to revert the preference of a route to the default preference.
Format no ipv6 route ipv6-prefix/prefix_length [{next-hop-address | Null0 |
interface {unit/slot/port| vlan vland-id | tunnel tunnel_id}
next-hop-address} [preference]]
Mode Global Config
ipv6 route distance
This command sets the default distance (preference) for IPv6 static routes. Lower route
distance values are preferred when determining the best route. The ipv6 route
distance command lets you optionally set the distance (preference) of an individual static
route. The default distance is used when no distance is specified in this command. The
preference can be a number in the range 1–255.
Changing the default distance does not update the distance of existing static routes, even if
they were assigned the original default distance. The new default distance will only be
applied to static routes created after entering the ipv6 route distance command.
Default 1
Format ipv6 route distance preference
Mode Global Config
no ipv6 route distance
This command resets the default static route preference value in the router to the original
default preference. Lower route preference values are preferred when determining the best
route.
Format no ipv6 route distance
Mode Global Config
ipv6 route net-prototype
This command adds net prototype IPv6 routes to the hardware.
Use the prefix/prefix-length argument to specify the The destination network and
mask for the route.
Use the nexthopip argument to specify the next-hop IP address, which must belong to an
active routing interface but it does not need to be resolved. The routes are added starting
from the specified prefix and prefix-length.
IPv6 Commands 831

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Use the num-routes argument to specify the number of routes that you want to add to the
hardware.
Format ipv6 route net-prototype prefix/prefix-length nexthopip num-routes
Mode Global Config
no ipv6 route net-prototype
This command removes all net prototype IPv6 routes from the hardware.
Format no ipv6 route net-prototype
Mode Global Config
ipv6 mtu
This command sets the maximum transmission unit (MTU) size, in bytes, of IPv6 packets on
an interface or range of interfaces. This command replaces the default or link MTU with a
new MTU value. The size variable is a number in the range 1280–1500.
Note: The default MTU value for a tunnel interface is 1480. You cannot change
this value.
Default 0 or link speed (MTU value (1500))
Format ipv6 mtu size
Mode Interface Config
no ipv6 mtu
This command resets maximum transmission unit value to default value.
Format no ipv6 mtu
Mode Interface Config
IPv6 Commands 832

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ipv6 nd dad attempts
This command sets the number of duplicate address detection probes transmitted on an
interface or range of interfaces. Duplicate address detection verifies that an IPv6 address on
an interface is unique. The number variable is a number in the range 0–600.
Default 1
Format ipv6 nd dad attempts number
Mode Interface Config
no ipv6 nd dad attempts
This command resets to number of duplicate address detection value to default value.
Format no ipv6 nd dad attempts
Mode Interface Config
ipv6 nd managed-config-flag
This command sets the managed address configuration flag in router advertisements on the
interface or range of interfaces. When the value is true, end nodes use DHCPv6. When the
value is false, end nodes automatically configure addresses.
Default false
Format ipv6 nd managed-config-flag
Mode Interface Config
no ipv6 nd managed-config-flag
This command resets the “managed address configuration” flag in router advertisements to
the default value.
Format no ipv6 nd managed-config-flag
Mode Interface Config
ipv6 nd mtu
This command sets the MTU value for IPv6 router advertisements on an interface. The mtu
argument is a number in the range from 1280 to the maximum MTU that the interface is
capable of minus 18.
Default 0
Format ipv6 nd mtu mtu
Mode Interface Config
IPv6 Commands 833

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ipv6 nd mtu
This command resets the MTU value for IPv6 router advertisements on an interface to 0.
Format no ipv6 nd mtu
Mode Interface Config
ipv6 nd ns-interval
This command sets the interval between router advertisements for advertised neighbor
solicitations, in milliseconds. An advertised value of 0 means the interval is unspecified. This
command can configure a single interface or a range of interfaces. The milliseconds
variable is a period in milliseconds in the range of 1000–4294967295.
Default 0
Format ipv6 nd ns-interval {milliseconds | 0}
Mode Interface Config
no ipv6 nd ns-interval
This command resets the neighbor solicit retransmission interval of the specified interface to
the default value.
Format no ipv6 nd ns-interval
Mode Interface Config
ipv6 nd other-config-flag
This command sets the other stateful configuration flag in router advertisements sent from
the interface.
Default false
Format ipv6 nd other-config-flag
Mode Interface Config
no ipv6 nd other-config-flag
This command resets the “other stateful configuration” flag back to its default value in router
advertisements sent from the interface.
Format no ipv6 nd other-config-flag
Mode Interface Config
IPv6 Commands 834

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ipv6 nd ra-interval
This command sets the transmission interval between router advertisements on the interface
or range of interfaces. The seconds variable is a number in the range 4–1800 seconds.
Default 600
Format ipv6 nd ra-interval-max seconds
Mode Interface Config
no ipv6 nd ra-interval
This command sets router advertisement interval to the default.
Format no ipv6 nd ra-interval-max
Mode Interface Config
ipv6 nd ra-lifetime
This command sets the value, in seconds, that is placed in the Router Lifetime field of the
router advertisements sent from the interface or range of interfaces. The lifetime variable
can be zero, or it must be an integer between the value of the router advertisement
transmission interval and 9000. A value of zero means this router is not to be used as the
default router.
Default 1800
Format ipv6 nd ra-lifetime lifetime
Mode Interface Config
no ipv6 nd ra-lifetime
This command resets router lifetime to the default value.
Format no ipv6 nd ra-lifetime
Mode Interface Config
ipv6 nd raguard attach-policy
This command enables the IPv6 RA guard host mode on the configured interface. All router
advertisement (RAs) and router redirect packets that are received on this interface are
dropped.
Format ipv6 nd raguard attach-policy
Mode Interface Config
IPv6 Commands 835

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ipv6 nd raguard attach-policy
This command disables the IPv6 RA guard host mode on the configured interface.
Format no ipv6 nd raguard attach-policy
Mode Interface Config
ipv6 nd ra hop-limit unspecified
This command configures the router to send Router Advertisements on an interface with an
unspecified (0) Current Hop Limit value. This tells the hosts on that link to ignore the Hop
Limit from this router.
Default Disable
Format ipv6 nd ra hop-limit unspecified
Mode Interface Config
no ipv6 nd ra hop-limit unspecified
This command configures the router to send Router Advertisements on an interface with the
global configured Hop Limit value.
Format no ipv6 nd ra hop-limit unspecified
Mode Interface Config
ipv6 nd reachable-time
This command sets the router advertisement time to consider a neighbor reachable after
neighbor discovery confirmation. Reachable time is specified in milliseconds in a range of
0–4294967295 milliseconds. A value of zero means the time is unspecified by the router.
This command can configure a single interface or a range of interfaces.
Default 0
Format ipv6 nd reachable-time milliseconds
Mode Interface Config
no ipv6 nd reachable-time
This command means reachable time is unspecified for the router.
Format no ipv6 nd reachable-time
Mode Interface Config
IPv6 Commands 836

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ipv6 nd router-preference
Use this command to configure default router preferences that the interface advertises in
router advertisement messages.
Default medium
Format ipv6 nd router-preference {low | medium | high}
Mode Interface Config
no ipv6 nd router-preference
This command resets the router preference advertised by the interface to the default value.
Format no ipv6 nd router-preference
Mode Interface Config
ipv6 nd suppress-ra
This command suppresses router advertisement transmission on an interface or range of
interfaces.
Default disabled
Format ipv6 nd suppress-ra
Mode Interface Config
no ipv6 nd suppress-ra
This command enables router transmission on an interface.
Format no ipv6 nd suppress-ra
Mode Interface Config
ipv6 nd prefix
Use the ipv6 nd prefix command to configure parameters associated with prefixes the
router advertises in its router advertisements. The first optional parameter is the valid lifetime
of the router, in seconds in the range of 0–4294967295 seconds.You can specify a value or
indicate that the lifetime value is infinite. The second optional parameter is the preferred
lifetime of the router in seconds in the range of 0–4294967295 seconds.
This command can be used to configure a single interface or a range of interfaces.
The router advertises its global IPv6 prefixes in its router advertisements (RAs). An RA only
includes the prefixes of the IPv6 addresses configured on the interface where the RA is
transmitted. Addresses are configured using the ipv6 address interface configuration
command. Each prefix advertisement includes information about the prefix, such as its
IPv6 Commands 837

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
lifetime values and whether hosts should use the prefix for on-link determination or address
auto-configuration. Use the ipv6 nd prefix command to configure these values.
The ipv6 nd prefix command allows you to preconfigure RA prefix values before you
configure the associated interface address. In order for the prefix to be included in RAs, you
must configure an address that matches the prefix using the ipv6 address command.
Prefixes specified using ipv6 nd prefix without associated interface address will not be
included in RAs and will not be committed to the device configuration.
Default valid-lifetime—2592000
preferred-lifetime— 604800
autoconfig—enabled
on-link—enabled
Format ipv6 nd prefix prefix/prefix_length [{seconds | infinite} {seconds |
infinite}] [no-autoconfig off-link]
Mode Interface Config
no ipv6 nd prefix
This command sets prefix configuration to default values.
Format no ipv6 nd prefix prefix/prefix_length
Mode Interface Config
ipv6 neighbor
Configures a static IPv6 neighbor with the given IPv6 address and MAC address on a routing
or host interface.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id
parameter is a number in the range of 1–4093.
Format ipv6 neighbor ipv6address {unit/slot/port | vlan vland-id} macaddr
Mode Global Config
Parameter Definition
ipv6address The IPv6 address of the neighbor.
unit/slot/port The unit/slot/port for the interface.
vlan-id The VLAN for the interface.
macaddr The MAC address for the neighbor.
IPv6 Commands 838

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ipv6 neighbor
Removes a static IPv6 neighbor with the given IPv6 address on a routing or host interface.
Format no ipv6 neighbor ipv6address {unit/slot/port | vlan vland-id}
Mode Global Config
ipv6 neighbors dynamicrenew
Use this command to automatically renew the IPv6 neighbor entries. Enables/disables the
periodic NUD (neighbor unreachability detection) to be run on the existing IPv6 neighbor
entries based on the activity of the entries in the hardware. If the setting is disabled, only
those entries that are actively used in the hardware are triggered for NUD at the end of
STALE timeout of 1200 seconds. If the setting is enabled, periodically every 40 seconds a set
of 300 entries are triggered for NUD irrespective of their usage in the hardware.
Default Disabled
Format ipv6 neighbors dynamicrenew
Mode Global Config
no ipv6 neighbors dynamicrenew
Disables automatic renewing of IPv6 neighbor entries.
Format no ipv6 neighbors dynamicrenew
Mode Global Config
ipv6 nud
Use this command to configure Neighbor Unreachability Detection (NUD). NUD verifies that
communication with a neighbor exists.
Format ipv6 nud {backoff-multiple | max-multicast-solicits | max-unicast-solicits}
Mode Global Config
Term Definition
backoff-multiple Sets the exponential backoff multiple to calculate time outs in NS transmissions during NUD. The
value ranges from 1 to 5. 1 is the default. The next timeout value is limited to a maximum value of 60
seconds if the value with exponential backoff calculation is greater than 60 seconds.
max-multicast-solici Sets the maximum number of multicast solicits sent during Neighbor Unreachability Detection. The
ts value ranges from 3 to 255. 3 is the default.
max-unicast-solicits Sets the maximum number of unicast solicits sent during Neighbor Unreachability Detection. The
value ranges from 3 to 10. 3 is the default.
IPv6 Commands 839

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ipv6 prefix-list (IPv6 routing commands)
To create a prefix list or add a prefix list entry, use the ipv6 prefix-list command in Global
Configuration mode. Prefix lists allow matching of route prefixes with those specified in the
prefix list. Each prefix list includes a sequence of prefix list entries ordered by their sequence
numbers. A router sequentially examines each prefix list entry to determine if the route’s
prefix matches that of the entry. An empty or nonexistent prefix list permits all prefixes. An
implicit deny is assume if a given prefix does not match any entries of a prefix list. Once a
match or deny occurs the router does not go through the rest of the list.
Up to 128 prefix lists may be configured. The maximum number of statements allowed in
prefix list is 64.
Default No prefix lists are configured by default. When neither the ge nor the le option is configured, the
destination prefix must match the network/length exactly. If the ge option is configured without the le
option, any prefix with a network mask greater than or equal to the ge value is considered a match.
Similarly, if the le option is configured without the ge option, a prefix with a network mask less than or
equal to the le value is considered a match.
Format ip prefix-list list-name {[seq number] {permit | deny}
ipv6-prefix/prefix-length [ge length] [le length] | renumber
renumber-interval first-statement-number}
Mode Global Configuration
Parameter Description
list-name The text name of the prefix list. Up to 32 characters.
seq number (Optional) The sequence number for this prefix list statement. Prefix list statements are ordered
from lowest sequence number to highest and applied in that order. If you do not specify a
sequence number, the system will automatically select a sequence number five larger than the
last sequence number in the list. Two statements may not be configured with the same
sequence number. The value range for number is from 1 to 4,294,967,294.
permit Permit routes whose destination prefix matches the statement.
deny Deny routes whose destination prefix matches the statement.
ipv6-prefix/prefix-length Specifies the match criteria for routes being compared to the prefix list statement. The
ipv6-prefix can be any valid IP prefix. The length is any IPv6 prefix length from 0 to 32.
ge length (Optional) If this option is configured, then a prefix is only considered a match if its network
mask length is greater than or equal to this value. This value must be longer than the network
length and less than or equal to 32.
le length (Optional) If this option is configured, then a prefix is only considered a match if its network
mask length is less than or equal to this value. This value must be longer than the ge length and
less than or equal to 32.
renumber (Optional) Provides the option to renumber the sequence numbers of the IP prefix list
statements with a given interval starting from a particular sequence number. The valid range for
renumber-interval i s 1– 100, and the valid range for first-statement-number is
1 – 1000.
IPv6 Commands 840

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip prefix-list
To delete a prefix list or a statement in a prefix list, use the no ip prefix-list command.
The no ip prefix-list list-name command deletes the entire prefix list. To remove
an individual statement from a prefix list, you must specify the statement exactly, with all its
options.
Format no ip prefix-list list-name [[seq number] {permit | deny} network/length [ge
length] [le length]]
Mode Global Configuration
ipv6 unreachables
Use this command to enable the generation of ICMPv6 Destination Unreachable messages
on the interface or range of interfaces. By default, the generation of ICMPv6 Destination
Unreachable messages is enabled.
Default enable
Format ipv6 unreachables
Mode Interface Config
no ipv6 unreachables
Use this command to prevent the generation of ICMPv6 Destination Unreachable messages.
Format no ipv6 unreachables
Mode Interface Config
ipv6 unresolved-traffic
Use this command to control the rate at which IPv6 data packets come into the CPU. By
default, rate limiting is disabled. When enabled, the rate, expressed by the seconds
variable, can range from 50 to 1024 packets per second.
Default enable
Format ipv6 unresolved-traffic rate-limit seconds
Mode Global Config
IPv6 Commands 841

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ipv6 unresolved-traffic
Use this command to disable the rate limiting.
Format no ipv6 unresolved-traffic rate-limit
Mode Global Config
ipv6 icmp error-interval
Use this command to limit the rate at which ICMPv6 error messages are sent. The rate limit is
configured as a token bucket, with two configurable parameters, burst-size and burst-interval.
The burst-interval specifies how often the token bucket is initialized with burst-size
tokens. burst-interval is from 0 to 2147483647 milliseconds (msec).
The burst-size is the number of ICMPv6 error messages that can be sent during one
burst-interval. The range is from 1 to 200 messages.
To disable ICMP rate limiting, set burst-interval to zero (0).
Default burst-interval of 1000 msec.
burst-size of 100 messages
Format ipv6 icmp error-interval burst-interval [burst-size]
Mode Global Config
no ipv6 icmp error-interval
Use the no ipv6 icmp error-interval command to return the burst-interval and
burst-size to their default values.
Format no ipv6 icmp error-interval
Mode Global Config
show ipv6 brief
Use this command to display the IPv6 status of forwarding mode and IPv6 unicast routing
mode.
Format show ipv6 brief
Mode Privileged EXEC
IPv6 Commands 842

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
IPv6 Forwarding Shows whether the IPv6 forwarding mode is enabled.
Mode
IPv6 Unicast Shows whether the IPv6 unicast routing mode is enabled.
Routing Mode
IPv6 Hop Limit Shows the unicast hop count used in IPv6 packets originated by the node. For more information, see
ipv6 hop-limit on page827.
ICMPv6 Rate Limit Shows how often the token bucket is initialized with burst-size tokens. For more information, see
Error Interval ipv6 icmp error-interval on page842.
ICMPv6 Rate Limit Shows the number of ICMPv6 error messages that can be sent during one burst-interval. For more
Burst Size information, see ipv6 icmp error-interval on page842.
Maximum Routes Shows the maximum IPv6 route table size.
IPv6 Unresolved Shows the rate in packets-per-second for the number of IPv6 data packets trapped to CPU when the
Data Rate Limit packet fails to be forwarded in the hardware due to unresolved hardware address of the destined
IPv6 node.
IPv6 Neighbors Shows the dynamic renewal mode for the periodic NUD (neighbor unreachability detection) run on
Dynamic Renew the existing IPv6 neighbor entries based on the activity of the entries in the hardware.
IPv6 NUD Shows the maximum number of unicast Neighbor Solicitations sent during NUD (neighbor
Maximum Unicast unreachabililty detection) before switching to multicast Neighbor Solicitations.
Solicits
IPv6 NUD Shows the maximum number of multicast Neighbor Solicitations sent during NUD (neighbor
Maximum Multicast unreachabililty detection) when in UNREACHABLE state.
Solicits
IPv6 NUD Shows the exponential backoff multiple to be used in the calculation of the next timeout value for
Exponential Neighbor Solicitation transmission during NUD (neighbor unreachabililty detection) following the
Backoff Multiple exponential backoff algorithm.
Command example:
(NETGEAR Switch) #show ipv6 brief
IPv6 Unicast Routing Mode...................... Disable
IPv6 Hop Limit................................. 0
ICMPv6 Rate Limit Error Interval............... 1000 msec
ICMPv6 Rate Limit Burst Size................... 100 messages
Maximum Routes................................. 4096
IPv6 Unresolved Data Rate Limit................ 1024 pps
IPv6 Neighbors Dynamic Renew................... Disable
IPv6 NUD Maximum Unicast Solicits.............. 3
IPv6 NUD Maximum Multicast Solicits............ 3
IPv6 NUD Exponential Backoff Multiple.......... 1
IPv6 Commands 843

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ipv6 interface
Use this command to show the usability status of IPv6 interfaces and whether ICMPv6
Destination Unreachable messages may be sent.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id
parameter is a number in the range of 1–4093.
The loopback keyword with the number variable specifies the loopback interface directly
and is a number in the range 0–7. The tunnel keyword with the number variable specifies
the IPv6 tunnel interface and is a number in the range 0–7.
Format show ipv6 interface [brief | unit/slot/port | vlan vlan-id | loopback number
| tunnel number]
Mode Privileged EXEC
If you use the brief parameter, the following information displays for all configured IPv6
interfaces.
Term Definition
Interface The interface in unit/slot/port format.
IPv6 Operational Shows whether the mode is enabled or disabled.
Mode
IPv6 Shows the IPv6 address and length on interfaces with IPv6 enabled.
Address/Length
Method Indicates how each IP address was assigned. The field contains one of the following values:
• DHCP. The address is leased from a DHCP server.
• Manual. The address is manually configured.
Global addresses with no annotation are assumed to be manually configured.
If you specify an interface, the following information also displays.
Term Definition
Routing Mode Shows whether IPv6 routing is enabled or disabled.
IPv6 Enable Mode Shows whether IPv6 is enabled on the interface.
Administrative Mode Shows whether the interface administrative mode is enabled or disabled.
Bandwidth Shows bandwidth of the interface.
Interface Maximum Transmission The MTU size, in bytes.
Unit
Router Duplicate Address Detection The number of consecutive duplicate address detection probes to transmit.
Transmits
IPv6 Commands 844

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Address Autoconfigure Mode Shows whether the autoconfigure mode is enabled or disabled.
Address DHCP Mode Shows whether the DHCPv6 client is enabled on the interface.
IPv6 Hop Limit Unspecified Indicates if the router is configured on this interface to send Router Advertisements
with unspecified (0) as the Current Hop Limit value.
Router Advertisement NS Interval The interval, in milliseconds, between router advertisements for advertised
neighbor solicitations.
Router Advertisement Lifetime Shows the router lifetime value of the interface in router advertisements.
Router Advertisement Reachable The amount of time, in milliseconds, to consider a neighbor reachable after
Time neighbor discovery confirmation.
Router Advertisement Interval The frequency, in seconds, that router advertisements are sent.
Router Advertisement Managed Shows whether the managed configuration flag is set (enabled) for router
Config Flag advertisements on this interface.
Router Advertisement Other Config Shows whether the other configuration flag is set (enabled) for router
Flag advertisements on this interface.
Router Advertisement Router Shows the router preference.
Preference
Router Advertisement Suppress Shows whether router advertisements are suppressed (enabled) or sent (disabled).
Flag
IPv6 Destination Unreachables Shows whether ICMPv6 Destination Unreachable messages may be sent
(enabled) or not (disabled). For more information, see ipv6 unreachables on
p age841.
ICMPv6 Redirect Specifies if ICMPv6 redirect messages are sent back to the sender by the Router in
the redirect scenario is enabled on this interface.
If an IPv6 prefix is configured on the interface, the following information also displays.
Term Definition
IPv6 Prefix is The IPv6 prefix for the specified interface.
Preferred Lifetime The amount of time the advertised prefix is a preferred prefix.
Valid Lifetime The amount of time the advertised prefix is valid.
Onlink Flag Shows whether the onlink flag is set (enabled) in the prefix.
Autonomous Flag Shows whether the autonomous address-configuration flag (autoconfig) is set (enabled) in the
prefix.
IPv6 Commands 845

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show ipv6 interface brief
Oper.
Interface Mode IPv6 Address/Length
---------- -------- ---------------------------------
1/0/33 Enabled FE80::211:88FF:FE2A:3E3C/128
2033::211:88FF:FE2A:3E3C/64
2/0/17 Enabled FE80::211:88FF:FE2A:3E3C/128
2017::A42A:26DB:1049:43DD/128 [DHCP]
0/4/1 Enabled FE80::211:88FF:FE2A:3E3C/128
2001::211:88FF:FE2A:3E3C/64 [AUTO]
0/4/2 Disabled FE80::211:88FF:FE2A:3E3C/128 [TENT]
Command example:
(NETGEAR Switch) #show ipv6 interface 0/4/1
IPv6 is enabled
IPv6 Prefix is ................................ fe80::210:18ff:fe00:1105/128
2001::1/64
Routing Mode................................... Enabled
IPv6 Enable Mode............................... Enabled
Administrative Mode............................ Enabled
IPv6 Operational Mode.......................... Enabled
Bandwidth...................................... 10000 kbps
Interface Maximum Transmit Unit................ 1500
Router Duplicate Address Detection Transmits... 1
Address DHCP Mode.............................. Disabled
IPv6 Hop Limit Unspecified..................... Enabled
Router Advertisement NS Interval............... 0
Router Advertisement Lifetime.................. 1800
Router Advertisement Reachable Time............ 0
Router Advertisement Interval.................. 600
Router Advertisement Managed Config Flag....... Disabled
Router Advertisement Other Config Flag......... Disabled
Router Advertisement Router Preference......... medium
Router Advertisement Suppress Flag............. Disabled
IPv6 Destination Unreachables.................. Enabled
ICMPv6 Redirects............................... Enabled
Prefix 2001::1/64
Preferred Lifetime............................. 604800
Valid Lifetime................................. 2592000
Onlink Flag.................................... Enabled
Autonomous Flag................................ Enabled
IPv6 Commands 846

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ipv6 interface vlan
Use the show ipv6 interface vlan in Privileged EXEC mode to show to show the usability
status of IPv6 VLAN interfaces.
Format show ipv6 interface vlan vlan-id [prefix]
Mode Privileged EXEC
User EXEC
Parameter Description
vlan-id Valid VLAN ID
prefix Display IPv6 Interface Prefix Information
show ipv6 nd raguard policy
This command shows the status of the IPv6 RA guard host mode on the switch. The output
lists the ports and interfaces on which IPv6 RA guard host mode is enabled and the
associated device roles.
Format show ipv6 nd raguard policy
Modes EXEC
Command example:
(Switching) # show ipv6 nd raguard policy
Configured Interfaces
Interface Role
--------------- -------
Gi1/0/1 Host
show ipv6 neighbors
Use this command to display information about the IPv6 neighbors.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id
parameter is a number in the range of 1–4093.
IPv6 Commands 847

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The tunnel keyword with the number variable specifies the IPv6 tunnel interface and is a
number in the range 0–7.
Format show ipv6 neighbor [interface {unit/slot/port | vlan vlan-id | tunnel number
| ipv6-address]
Mode Privileged EXEC
Term Definition
Interface The interface in unit/slot/port format.
IPv6 Address IPV6 address of neighbor or interface.
MAC Address Link-layer Address.
IsRtr Shows whether the neighbor is a router. If the value is TRUE, the neighbor is known to be a router,
and FALSE otherwise. A value of FALSE might mean that routers are not always known to be
routers.
Neighbor State State of neighbor cache entry. Possible values are Incomplete, Reachable, Stale, Delay, Probe, and
Unknown.
Last Updated The time in seconds that has elapsed since an entry was added to the cache.
Type The type of neighbor entry. The type is Static if the entry is manually configured and Dynamic if
dynamically resolved.
clear ipv6 neighbors
Use this command to clear all entries IPv6 neighbor table or an entry on a specific interface.
Use the optional unit/slot/port parameter to specify an interface.
Format clear ipv6 neighbors [unit/slot/port]
Mode Privileged EXEC
show ipv6 protocols
This command lists a summary of the configuration and status for the active IPv6 routing
protocols. The command lists routing protocols that are configured and enabled. If a protocol
is selected on the command line, the display is limited to that protocol.
Format show ipv6 protocols [ospf]
Mode Privileged Exec
Parameter Description
Routing Protocol OSPFv3.
Router ID The router ID configured for OSPFv3.
OSPF Admin Mode Whether OSPF is enabled or disabled globally.
IPv6 Commands 848

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
Maximum Paths The maximum number of next hops in an OSPF route.
Default Route Whether OSPF is configured to originate a default route.
Advertise
Always Whether default advertisement depends on having a default route in the common routing table.
Metric The metric configured to be advertised with the default route.
Metric Type The metric type for the default route.
Command example:
(NETGEAR Switch) #show ipv6 protocols
Routing Protocol .............................. OSPFv3
Router ID ..................................... 1.1.1.1
OSPF Admin Mode ............................... Enable
Maximum Paths ................................. 4
Distance ...................................... Intra 110 Inter 110 Ext 110
Default Route Advertise ....................... Disabled
Always ........................................ FALSE
Metric ........................................ Not configured
Metric Type ................................... External Type 2
Number of Active Areas ........................ 0 (0 normal, 0 stub, 0 nssa)
ABR Status .................................... Disable
ASBR Status ................................... Disable
show ipv6 route
This command displays the IPv6 routing table The ipv6-address specifies a specific IPv6
address for which the best-matching route would be displayed. The
ipv6-prefix/ipv6-prefix-length specifies a specific IPv6 network for which the
matching route would be displayed.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id
parameter is a number in the range of 1–4093.
The protocol specifies the protocol that installed the routes. The protocol is one of the
following keywords: connected, ospf, or static. The all keyword specifies that all
routes including best and nonbest routes are displayed. Otherwise, only the best routes are
displayed.
IPv6 Commands 849

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: If you use the connected keyword for protocol, the all option is
not available because there are no best or nonbest connected routes.
Format show ipv6 route [ipv6-address [protocol] | {{ipv6-prefix/ipv6-prefix-length |
unit/slot/port | vlan vland-id} [protocol] | protocol | summary} [all] | all]
Modes Privileged EXEC
User EXEC
Term Definition
Route Codes The key for the routing protocol codes that might appear in the routing table output.
The show ipv6 route command displays the routing tables in the following format:
Codes: C - connected, S - static
O - OSPF Intra, OI - OSPF Inter, OE1 - OSPF Ext 1, OE2 - OSPF Ext 2
ON1 - OSPF NSSA Ext Type 1, ON2 - OSPF NSSA Ext Type 2, Truncated
The columns for the routing table display the following information.
Term Definition
Code The code for the routing protocol that created this routing entry.
Default Gateway The IPv6 address of the default gateway. When the system does not have a more specific route to a
packet's destination, it sends the packet to the default gateway.
IPv6-Prefix/IPv6-Pr The IPv6-Prefix and prefix-length of the destination IPv6 network corresponding to this route.
efix-Length
Preference/Metric The administrative distance (preference) and cost (metric) associated with this route. An example of
this output is [1/0], where 1 is the preference and 0 is the metric.
Tag The decimal value of the tag associated with a redistributed route, if it is not 0.
Next-Hop The outgoing router IPv6 address to use when forwarding traffic to the next router (if any) in the path
toward the destination.
Route-Timestamp The last updated time for dynamic routes. The format of Route-Timestamp is:
Days:Hours:Minutes if days > = 1
Hours:Minutes:Seconds if days < 1
Interface The outgoing router interface to use when forwarding traffic to the next destination. For reject routes,
the next hop interface would be Null0 interface.
T A flag appended to an IPv6 route to indicate that it is an ECMP route, but only one of its next hops
has been installed in the forwarding table. The forwarding table may limit the number of ECMP
routes or the number of ECMP groups. When an ECMP route cannot be installed because such a
limit is reached, the route is installed with a single next hop. Such truncated routes are identified by
a T after the interface name.
IPv6 Commands 850

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
To administratively control the traffic destined to a particular network and prevent it from
being forwarded through the router, you can configure a static reject route on the router. Such
traffic would be discarded and the ICMP destination unreachable message is sent back to the
source. This is typically used for preventing routing loops. The reject route added in the RTO
is of the type OSPF Inter-Area. Reject routes (routes of REJECT type installed by any
protocol) are not redistributed by OSPF/RIP. Reject routes are supported in both OSPFv2
and OSPFv3.
Command example:
(NETGEAR Switch) #show ipv6 route
IPv6 Routing Table - 3 entries
Codes: C - connected, S - static
O - OSPF Intra, OI - OSPF Inter, OE1 - OSPF Ext 1, OE2 - OSPF Ext 2
ON1 - OSPF NSSA Ext Type 1, ON2 - OSPF NSSA Ext Type 2
S 2001::/64 [10/0] directly connected, Null0
C 2003::/64 [0/0]
via ::, 0/11
S 2005::/64 [1/0]
via 2003::2, 0/11
C 5001::/64 [0/0]
via ::, 0/5
OE1 6001::/64 [110/1]
via fe80::200:42ff:fe7d:2f19, 00h:00m:23s, 0/5
OI 7000::/64 [110/6]
via fe80::200:4fff:fe35:c8bb, 00h:01m:47s, 0/11
Command example:
The following example displays a truncated route:
(NETGEAR Switch) #show ipv6 route
IPv6 Routing Table - 2 entries
Codes: C - connected, S - static, 6To4 - 6to4 Route
O - OSPF Intra, OI - OSPF Inter, OE1 - OSPF Ext 1, OE2 - OSPF Ext 2
ON1 - OSPF NSSA Ext Type 1, ON2 - OSPF NSSA Ext Type 2
C 2001:db9:1::/64 [0/0]
via ::, 0/1
OI 3000::/64 [110/1]
via fe80::200:e7ff:fe2e:ec3f, 00h:00m:11s, 0/1 T
IPv6 Commands 851

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ipv6 route ecmp-groups
This command reports all current ECMP groups in the IPv6 routing table. An ECMP group is
a set of two or more next hops used in one or more routes. The groups are numbered
arbitrarily from 1 to n. The output indicates the number of next hops in the group and the
number of routes that use the set of next hops. The output lists the IPv6 address and
outgoing interface of each next hop in each group.
Format show ipv6 route ecmp-groups
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show ipv6 route ecmp-groups
ECMP Group 1 with 2 next hops (used by 1 route)
2001:DB8:1::1 on interface 2/1
2001:DB8:2::14 on interface 2/2
ECMP Group 2 with 3 next hops (used by 1 route)
2001:DB8:4::15 on interface 2/32
2001:DB8:7::12 on interface 2/33
2001:DB8:9::45 on interface 2/34
show ipv6 route hw-failure
This command displays the routes that were not added to the hardware because of hash
errors or because the table was full.
Format show ipv6 route hw-failure
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show ipv6 route hw-failure
IPv6 Routing Table - 4 entries
Codes: C - connected, S - static, 6To4 - 6to4 Route
O - OSPF Intra, OI - OSPF Inter, OE1 - OSPF Ext 1, OE2 - OSPF Ext 2
ON1 - OSPF NSSA Ext Type 1, ON2 - OSPF NSSA Ext Type 2, K - kernel
P - Net Prototype
P 3001::/64 [0/1]
via 2001::4, 00h:00m:04s, 0/1 hw-failure
P 3001:0:0:1::/64 [0/1]
via 2001::4, 00h:00m:04s, 0/1 hw-failure
P 3001:0:0:2::/64 [0/1]
via 2001::4, 00h:00m:04s, 0/1 hw-failure
P 3001:0:0:3::/64 [0/1]
via 2001::4, 00h:00m:04s, 0/1 hw-failure
IPv6 Commands 852

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ipv6 route kernel
This command displays kernel routes, if any exist.
Format show ipv6 route kernel
Mode Privileged EXEC
show ipv6 route 6to4
This command displays IPv6-over-IPv4 tunnels that are manually configured in the switch.
Format show ipv6 route 6to4
Mode Privileged EXEC
show ipv6 route net-prototype
This command displays the net prototype routes. The output displays the net prototype
routes with a P.
Format show ipv6 route net-prototype
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show ipv6 route net-prototype
IPv6 Routing Table - 2 entries
Codes: C - connected, S - static, 6To4 - 6to4 Route
O - OSPF Intra, OI - OSPF Inter, OE1 - OSPF Ext 1, OE2 - OSPF Ext 2
ON1 - OSPF NSSA Ext Type 1, ON2 - OSPF NSSA Ext Type 2, K - kernel
P - Net Prototype
P 3001::/64 [0/1]
via 2001::4, 00h:00m:04s, 0/1
P 3001:0:0:1::/64 [0/1]
via 2001::4, 00h:00m:04s, 0/1
show ipv6 route preferences
Use this command to show the preference value associated with the type of route. Lower
numbers have a greater preference. A route with a preference of 255 cannot be used to
forward traffic.
Format show ipv6 route preferences
Mode Privileged EXEC
IPv6 Commands 853

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Local Preference of directly-connected routes.
Static Preference of static routes.
OSPF Intra Preference of routes within the OSPF area.
OSPF Inter Preference of routes to other OSPF routes that are outside of the area.
OSPF External Preference of OSPF external routes.
show ipv6 route summary
This command displays a summary of the state of the routing table. When the optional all
keyword is given, some statistics, such as the number of routes from each source, include
counts for alternate routes. An alternate route is a route that is not the most preferred route to
its destination and therefore is not installed in the forwarding table. To include only the
number of best routes, do not use the optional all keyword.
Format show ipv6 route summary [all]
Modes Privileged EXEC
User EXEC
Term Definition
Connected Routes Total number of connected routes in the routing table.
Static Routes Total number of static routes in the routing table.
OSPF Routes Total number of routes installed by OSPFv3 protocol.
Reject Routes Total number of reject routes installed by all protocols.
Net Prototype Routes The total number of net prototype routes.
Number of Prefixes Summarizes the number of routes with prefixes of different lengths.
Total Routes The total number of routes in the routing table.
Best Routes The number of best routes currently in the routing table. This number only counts the
best route to each destination.
Alternate Routes The number of alternate routes currently in the routing table. An alternate route is a
route that was not selected as the best route to its destination.
Route Adds The number of routes that have been added to the routing table.
Route Modifies The number of routes that have been changed after they were initially added to the
routing table.
Route Deletes The number of routes that have been deleted from the routing table.
IPv6 Commands 854
