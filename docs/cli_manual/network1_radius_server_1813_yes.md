# network1_radius_server_1813_yes

Pages: 155-155

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show radius servers 192.168.37.58
Server Name............................ Default_RADIUS_Server
Host Address........................... 192.168.37.58
Secret Configured...................... No
Message Authenticator ................. Enable
Number of Retransmits.................. 4
Time Duration.......................... 10
RADIUS Accounting Mode................. Disable
RADIUS Attribute 4 Mode................ Enable
RADIUS Attribute 4 Value .............. 192.168.37.60
show radius accounting
This command displays a summary of configured RADIUS accounting servers.
Format show radius accounting name [servername]
Mode Privileged EXEC
Field Description
servername An alias name to identify the server.
RADIUS A global parameter to indicate whether the accounting mode for all the servers is enabled or not.
Accounting Mode
If you do not specify any parameters, then only the accounting mode and the RADIUS
accounting server details are displayed.
Term Definition
Host Address The IP address of the host.
Server Name The name of the accounting server.
Port The port used for communication with the accounting server.
Secret Configured Yes or No Boolean value indicating whether this server is configured with a secret.
Command example:
(NETGEAR Switch) #show radius accounting name
Host Address Server Name Port Secret
Configured
----------------------- --------------------------------- -------- -----------
192.168.37.200 Network1_RADIUS_Server 1813 Yes
192.168.37.201 Network2_RADIUS_Server 1813 No
Management Commands 155
