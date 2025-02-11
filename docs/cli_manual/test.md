# test

Pages: 168-169

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default none
Format copy <tftp://<ipaddr>/<filepath>/<filename>> nvram:clibanner
copy nvram:clibanner <tftp://<ipaddr>/<filepath>/<filename>>
Mode Privileged EXEC
set prompt
This command changes the name of the prompt. The length of name may be up to 64
alphanumeric characters.
Format set prompt prompt-string
Mode Privileged EXEC
hostname
This command sets the system host name. It also changes the prompt. The length of name
may be up to 64 alphanumeric, case-sensitive characters.
Format hostname hostname
Mode Privileged EXEC
show clibanner
Use this command to display the configured prelogin CLI banner. The prelogin banner is the
text that displays before displaying the CLI prompt.
Default No contents to display before displaying the login prompt.
Format show clibanner
Mode Privileged Exec
Command example:
(NETGEAR Switch) #show clibanner
Banner Message configured:
=========================
--------------------------
TEST
--------------------------
Management Commands 168

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
set clibanner
Use this command to configure the prelogin CLI banner before displaying the login prompt.
Format set clibanner line
Mode Global Config
Parameter Description
line Banner text where ““ (double quote) is a delimiting character. The banner message can be up to
2000 characters.
no set clibanner
Use this command to unconfigure the prelogin CLI banner.
Format no set clibanner
Mode Global Config
OpenFlow Commands
OpenFlow commands enable you to manage the switch from a centralized OpenFlow
controller, using the OpenFlow protocol.
openflow enable
This command enables OpenFlow.
Default Disabled
Format openflow enable
Mode Global Config
no openflow enable
This command disables OpenFlow.
Format no openflow enable
Mode Global Config
openflow static-ip
This command specifies the static IP address that must be used for OpenFlow. This static IP
address is applied only when the static IP mode is enabled. For the static IP address to be
used for OpenFlow, the switch must include an operational IP interface with the specified
Management Commands 169
