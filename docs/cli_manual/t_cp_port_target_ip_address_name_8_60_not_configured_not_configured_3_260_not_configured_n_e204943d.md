# t_cp_port_target_ip_address_name_8_60_not_configured_not_configured_3_260_not_configured_n_e204943d

Pages: 1006-1006

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
tcp-port-n TCP port number or list of TCP port numbers on which the iSCSI target listens to requests. Up to 16
TCP ports can be defined in the system in one command or by using multiple commands.
ip-address IP address of the iSCSI target. When the no form of this command is used, and the tcp port to be
deleted is one bound to a specific IP address, the address field must be present.
targetname iSCSI name of the iSCSI target. The name can be statically configured; however, it can be obtained
from iSNS or from sendTargets response. The initiator must present both its iSCSI Initiator Name
and the iSCSI Target Name to which it wishes to connect in the first login request of a new session
or connection.
Command example:
The following example configures TCP Port 49154 to target IP address 172.16.1.20:
(NETGEAR Switch)(config)#iscsi target port 49154 address 172.16.1.20
no iscsi target port
Use the no iscsi target port command to delete an iSCSI target port, address, and
name.
Format no iscsi target port
Mode Global Config
show iscsi
This command displays the iSCSI settings.
Format show iscsi
Mode Privileged EXEC
Command example:
The following example shows the default configuration:
(NETGEAR Switch)#show iscsi
iSCSI disabled
iSCSI vpt is 5, remark
Session aging time: 10 min
Maximum number of sessions is 192
--------------------------------------------
iSCSI Targets and TCP ports:
--------------------------------------------
T CP Port Target IP Address Name
8 60 Not Configured Not Configured
3 260 Not Configured Not Configured
Quality of Service Commands 1006
