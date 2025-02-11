# http_port_the_insecure_http_server_port_number

Pages: 92-101

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip http secure-session soft-timeout
This command restores the soft time-out for secure HTTP sessions to the default value.
Format no ip http secure-session soft-timeout
Mode Privileged EXEC
ip http secure-port
This command is used to set the SSL port where port can be 1025-65535 and the default is
port 443.
Default 443
Format ip http secure-port portid
Mode Privileged EXEC
no ip http secure-port
This command is used to reset the SSL port to the default value.
Format no ip http secure-port
Mode Privileged EXEC
show ip http
This command displays the http settings for the switch.
Format show ip http
Mode Privileged EXEC
Term Definition
HTTP Mode (Unsecure) The insecure HTTP server administrative mode.
HTTP Port The insecure HTTP server port number
Maximum Allowable HTTP The number of allowable un-secure http sessions.
Sessions
HTTP Session Hard Timeout The hard time-out for insecure http sessions in hours.
HTTP Session Soft Timeout The soft time-out for insecure http sessions in minutes.
HTTP Mode (Secure) The secure HTTP server administrative mode.
Secure Port The secure HTTP server port number.
Secure Protocol Level(s) The protocol level can be SSL3 or TSL 1.2.
Management Commands 92

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Maximum Allowable HTTPS The number of allowable secure http sessions.
Sessions
HTTPS Session Hard The hard time-out for secure http sessions in hours.
Timeout
HTTPS Session Soft The soft time-out for secure http sessions in minutes.
Timeout
Certificate Present Indicates if the secure-server certificate files are present on the switch.
Certificate Generation in Indicates if certificate generation is in progress.
Progress
Access Commands
Use the commands in this section to close remote connections or to view information about
connections to the system.
disconnect
Use the disconnect command to close HTTP, HTTPS, Telnet or SSH sessions. Use all to
close all active sessions, or use session-id to specify the session ID to close. To view the
possible values for session-id, use the show loginsession command.
Format disconnect {session_id | all}
Mode Privileged EXEC
show loginsession
This command displays current Telnet, SSH and serial port connections to the switch. This
command displays truncated user names. Use the show loginsession long command
to display the complete usernames.
Format show loginsession
Mode Privileged EXEC
Term Definition
ID Login Session ID.
User Name The name the user entered to log on to the system.
Connection From IP address of the remote client machine or EIA-232 for the serial port connection.
Idle Time Time this session has been idle.
Management Commands 93

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Session Time Total time this session has been connected.
Session Type Shows the type of session, which can be HTTP, HTTPS, telnet, serial, or SSH.
show loginsession long
This command displays the complete user names of the users currently logged in to the
switch.
Format show loginsession long
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show loginsession long
User Name
------------
admin
test1111test1111test1111test1111test1111test1111test1111test1111
User Account Commands
This section describes the commands you use to add, manage, and delete switch users. The
switch provides two default users: admin and guest. The admin user can view and configure
the switch settings. The guest user can view the switch settings only.
The first time that you log in as an admin user, no password is required (that is, the password
is blank). As of software version 12.0.9.3, after you log in for the first time, you are required to
specify a new password that you must use each subsequent time that you log in. After you
specify the new password, you are logged out and then must log in again, using your new
password.
The default guest user cannot log in until the admin user specifies a password for the guest
user.
You cannot reset the new password to the default password. For example, if you enter the
username admin nopassword command or clear password command, the password
is not reset to the default password.
However, if you enter the clear-config command, the passwords for the default admin
user and default guest user are reset to defaults. In such a situation, the admin user must
again specify a new password after logging in for the first time. Similarly, the admin user must
again specify a password for the default guest user.
Management Commands 94

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: You cannot delete the admin user, which is the only user with
read/write privileges on the switch. You can configure up to five
read-only users (that is, guest users) on the switch.
aaa authentication login
Note: In software version 12.0.11.8 and later software versions, a user with
privilege level 1 cannot enter in Privilege Exec Mode and cannot
execute Privilege Exec commands.
Use this command to set authentication at login. The default and optional list names created
with the command are used with the aaa authentication login command. Create a list
by entering the aaa authentication login list-name method command, where
list-name is any character string used to name this list. The method argument identifies
the list of methods that the authentication algorithm tries, in the given sequence.
The additional methods of authentication are used only if the previous method returns an
error, not if there is an authentication failure. To ensure that the authentication succeeds
even if all methods return an error, specify none as the final method in the command line.
For example, if none is specified as an authentication method after radius, no
authentication is used if the RADIUS server is down.
If you configure local as the first method in the list, the switch tries no other methods.
Default • defaultList. Used by the console and only contains the method none.
• networkList. Used by telnet and SSH and only contains the method local.
Format aaa authentication login {default | list-name} method1 [method2...]
Mode Global Config
Parameter Definition
default Uses the listed authentication methods that follow this argument as the default list of methods when
a user logs in.
list-name Character string of up to 15 characters used to name the list of authentication methods activated
when a user logs in.
method1... At least one from the following:
[method2...] • enable. Uses the enable password for authentication.
• line. Uses the line password for authentication.
• local. Uses the local username database for authentication.
• none. Uses no authentication.
• radius. Uses the list of all RADIUS servers for authentication.
• tacacs. Uses the list of all TACACS servers for authentication.
Management Commands 95

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch)(config)# aaa authentication login default radius local enable none
no aaa authentication login
This command returns to the default.
Format aaa authentication login {default | list-name}
Mode Global Config
aaa authentication enable
Use this command to set authentication for accessing higher privilege levels. The default
enable list is enableList. It is used by console, and contains the method as enable
followed by none.
A separate default enable list, enableNetList, is used for Telnet and SSH users instead of
enableList. This list is applied by default for Telnet and SSH, and contains enable
followed by deny methods. By default, the enable password is not configured. That means
that, by default, Telnet and SSH users will not get access to Privileged EXEC mode. On the
other hand, with default conditions, a console user always enter the Privileged EXEC mode
without entering the enable password.
The default and optional list names created with the aaa authentication enable
command are used with the enable authentication command. Create a list by entering
the aaa authentication enable list-name method command where list-name
is any character string used to name this list. The method argument identifies the list of
methods that the authentication algorithm tries in the given sequence.
The user manager returns ERROR (not PASS or FAIL) for enable and line methods if no
password is configured, and moves to the next configured method in the authentication list.
The method none reflects that there is no authentication needed.
The user will only be prompted for an enable password if one is required. The following
authentication methods do not require passwords:
• none
• deny
• enable (if no enable password is configured)
• line (if no line password is configured)
See the examples below.
1. aaa authentication enable default enable none
2. aaa authentication enable default line none
3. aaa authentication enable default enable radius none
4. aaa authentication enable default line tacacs none
Management Commands 96

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Examples 1 and 2 do not prompt for a password, however because examples 3 and 4
contain the radius and tacacs methods, the password prompt is displayed.
If the login methods include only enable, and there is no enable password configured, the
switch does not prompt for a user name. In such cases, the switch prompts only for a
password. The switch supports configuring methods after the local method in authentication
and authorization lists. If the user is not present in the local database, then the next
configured method is tried.
The additional methods of authentication are used only if the previous method returns an
error, not if it fails. To ensure that the authentication succeeds even if all methods return an
error, specify none as the final method in the command line.
Use the command show authorization methods on page101 to display information about
the authentication methods.
Note: Requests sent by the switch to a RADIUS or TACACS server include
the username $enabx$, in which x is the requested privilege level.
The login user ID is also sent to a TACACS+ server.
Default default
Format aaa authentication enable {default | list-name} method1 [method2...]
Mode Global Config
Parameter Description
default Uses the listed authentication methods that follow this argument as the default list of methods, when
using higher privilege levels.
list-name Character string used to name the list of authentication methods activated, when using access
higher privilege levels. Range: 1-15 characters.
method1 Specify at least one from the following:
[method2...] • deny. Used to deny access.
• enable. Uses the enable password for authentication.
• line. Uses the line password for authentication.
• none. Uses no authentication.
• radius. Uses the list of all RADIUS servers for authentication.
• tacacs. Uses the list of all TACACS+ servers for authentication.
Command example:
The following example sets authentication to access higher privilege levels:
(NETGEAR Switch)(config)# aaa authentication enable default enable
Management Commands 97

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no aaa authentication enable
Use this command to return to the default configuration.
Format no aaa authentication enable {default | list-name}
Mode Global Config
aaa authorization
Use this command to configure command and exec authorization method lists. This list is
identified by default or a user-specified list-name. If tacacs is specified as the
authorization method, authorization commands are notified to a TACACS+ server. If none is
specified as the authorization method, command authorization is not applicable. A maximum
of five authorization method lists can be created for the commands type.
Note: The local method is not supported for command authorization.
Command authorization with RADIUS functions only if the applied
authentication method is also RADIUS.
Format aaa authorization {exec | commands} {default | list-name} method1
[method2…]
Mode Global Config
Term Definition
exec Provides authorization for user EXEC terminal sessions.
commands Provides authorization for all user-executed commands.
default The default list of methods for authorization services.
list-name Character string used to name the list of authorization methods.
method1 [method2…] Use either tacacs or radius for authorization purpose.
no aaa authorization
This command deletes the authorization method list.
Format no aaa authorization {exec | commands} {default | <list-name>}
<method1> [<method2>…]
Mode Global Config
Management Commands 98

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Per-Command Authorization
When authorization is configured for a line mode, the user manager sends information about
an entered command to the AAA server. The AAA server validates the received command,
and responds with either a PASS or FAIL response. If approved, the command is executed.
Otherwise, the command is denied and an error message is shown to the user. The various
utility commands such as tftp, ping, and outbound telnet should also pass command
authorization. Applying the script is treated as a single command apply script, which also
goes through authorization. Startup-config commands applied on device boot-up are not an
object of the authorization process.
The per-command authorization usage scenario is this:
1. Configure Authorization Method List
aaa authorization commands listname tacacs radius none
2. Apply AML to an Access Line Mode (console, telnet, SSH)
authorization commands listname
3. Commands entered by the user will go through command authorization via TACACS+ or
RADIUS server and will be accepted or denied.
Exec Authorization
When exec authorization is configured for a line mode, the user may not be required to use
the enable command to enter Privileged EXEC mode. If the authorization response indicates
that the user has sufficient privilege levels for Privileged EXEC mode, then the user bypasses
User EXEC mode entirely.
The exec authorization usage scenario is as follows:
1. Configure Authorization Method List
aaa authorization exec listname method1 [method2....]
2. Apply AML to an Access Line Mode (console, telnet, SSH)
authorization exec listname
3. When the user logs in, in addition to authentication, authorization will be performed to
determine if the user is allowed direct access to Privileged EXEC mode.
Format aaa authorization {commands | exec} {default | list-name} method1 [method2]
Mode Global Config
Parameter Description
commands Provides authorization for all user-executed commands.
exec Provides exec authorization.
default The default list of methods for authorization services.
Management Commands 99

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
list-name Alphanumeric character string used to name the list of authorization methods.
method TACACS+, RADIUS, Local, and none are supported.
(NETGEAR Switch) #
(NETGEAR Switch) #configure
(NETGEAR Switch) (Config)#aaa authorization exec default tacacs+ none
(NETGEAR Switch) (Config)#aaa authorization commands default tacacs+ none
no aaa authorization
This command deletes the authorization method list.
Format no aaa authorization {commands | exec} {default | list-name}
Mode Global Config
authorization commands
This command applies a command authorization method list to an access method (console,
telnet, ssh). For usage scenarios on per command authorization, see the command aaa
authorization on page98.
Format authorization commands [default | list-name]
Mode Line console, Line telnet, Line SSH
Parameter Description
commands This causes command authorization for each command execution attempt.
no authorization commands
This command removes command authorization from a line config mode.
Format no authorization {commands | exec}
Mode Line console, Line telnet, Line SSH
Command example:
(NETGEAR Switch) (Config)#line console
(NETGEAR Switch) (Config-line)#authorization commands list2
(NETGEAR Switch) (Config-line)#
(NETGEAR Switch) (Config-line)#exit
Management Commands 100

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
authorization exec
This command applies a command authorization method list to an access method so that the
user may not be required to use the enable command to enter Privileged EXEC mode. For
usage scenarios on exec authorization, see the command aaa authorization on page98.
Format authorization exec list-name
Mode Line console, Line telnet, Line SSH
Parameter Description
list-name The command authorization method list.
no authorization exec
This command removes command authorization from a line config mode.
Format no authorization exec
Mode Line console, Line telnet, Line SSH
authorization exec default
This command applies a default command authorization method list to an access method so
that the user may not be required to use the enable command to enter Privileged EXEC
mode. For usage scenarios on exec authorization, see the command aaa authorization on
p age98.
Format authorization exec default
Mode Line console, Line telnet, Line SSH
no authorization exec default
This command removes command authorization from a line config mode.
Format no authorization exec default
Mode Line console, Line telnet, Line SSH
show authorization methods
This command displays the configured authorization method lists.
Format show authorization methods
Mode Privileged EXEC
Management Commands 101
