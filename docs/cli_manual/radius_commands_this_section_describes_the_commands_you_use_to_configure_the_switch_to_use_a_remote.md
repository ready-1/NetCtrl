# radius_commands_this_section_describes_the_commands_you_use_to_configure_the_switch_to_use_a_remote

Pages: 142-144

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
RADIUS Commands
This section describes the commands you use to configure the switch to use a Remote
Authentication Dial-In User Service (RADIUS) server on your network for authentication and
accounting.
The first time that you log in as an admin user, no password is required (that is, the password
is blank). As of software version 12.0.9.3, after you log in for the first time, you are required to
specify a new password that you must use each subsequent time that you log in. After you
specify the new password, you are logged out and then must log in again, using your new
password.
If you are using a RADIUS or TACAS+ server for authentication, after changing the default
password to the new password, make sure that you also change the password in the
RADIUS or TACAS+ server so that you can continue to log in to the switch.
aaa server radius dynamic-author
This command enables Change of Authorization (CoA) functionality and lets you configure
the switch from the dynamic authorization local server configuration mode.
Format aaa server radius dynamic-author
Mode Global Config
no aaa server radius dynamic-author
This command disables Change of Authorization (CoA) functionality.
Format no aaa server radius dynamic-author
Mode Global Config
auth-type
This command specifies the type of authorization that the switch uses for RADIUS clients.
The client must match the configured attributes for authorization.
Default all
Format auth-type {any | all | session-key}
Mode Dynamic Authorization
Management Commands 142

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no auth-type
Use this command to reset the type of authorization that the switch uses for RADIUS clients.
Format no auth-type
Mode Dynamic Authorization
authorization network radius
Use this command to enable the switch to accept VLAN assignments from the RADIUS
server.
Default disable
Format authorization network radius
Mode Global Config
no authorization network radius
Use this command to prevent the switch from accepting VLAN assignments from the
RADIUS server.
Format no authorization network radius
Mode Global Config
clear radius dynamic-author statistics
Use this command to clear the counters for RADIUS dynamic authorization.
Format clear radius dynamic-author statistics
Mode Privileged EXEC
client
Use this command to configure the IP address or host name of the dynamic authorization
client. Use the optional server-key keyword and key-string argument to configure the
server key at the client level.
Format client {ip-address | hostname} [server-key [0 | 7] key-string]
Mode Dynamic Authorization
Management Commands 143

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no client
Use this command to remove the configured dynamic authorization client and the key that is
associated with that client in the device.
Format no client {ip-address | hostname}
Mode Dynamic Authorization
debug aaa coa
Use this command to display debug information for the dynamic authorization server
process.
Format debug aaa coa
Mode Dynamic Authorization
debug aaa pod
Use this command to display disconnect message packets.
Format debug aaa pod
Mode Dynamic Authorization
ignore server-key
Use this command to configure the switch to ignore the server key.
Format ignore server-key
Mode Dynamic Authorization
no ignore server-key
Use this command to configure the switch not to ignore the server key. That is, this command
resets the ignore server key property on the switch.
Format no ignore server-key
Mode Dynamic Authorization
ignore session-key
Use this command to configure the switch to ignore the session key.
Format ignore session-key
Mode Dynamic Authorization
Management Commands 144
