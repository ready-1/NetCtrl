# ssh_dfltexeclist_usercmdaudit_clear_accounting_statistics

Pages: 128-128

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Errors when sending Accounting Notifications at beginning of a command execution: 0
Number of Accounting Notifications sent at end of a command execution: 0
Errors when sending Accounting Notifications at end of a command execution: 0
show accounting methods
Use this command to display configured accounting method lists.
Format show accounting methods
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #
(NETGEAR Switch) #show accounting methods
Acct Type Method Name Record Type Method Type
---------- ------------ ------------ ------------
Exec dfltExecList start-stop TACACS
Commands dfltCmdsList stop-only TACACS
Commands U serCmdAudit s tart-stop TACACS
D OT1X d fltDot1xList start-stop radius
Line EXEC Method List Command Method List
------- ---------------------------------------
Console dfltExecList dfltCmdsList
Telnet dfltExecList dfltCmdsList
SSH dfltExecList UserCmdAudit
clear accounting statistics
This command clears the accounting statistics.
Format clear accounting statistics
Mode Privileged Exec
show domain-name
This command displays the configured domain-name.
Format show domain-name
Mode Privileged Exec
Management Commands 128
