# t_cp_port_target_ip_address_name_8_60_configured_not_configured_3_260_configured_not_configured

Pages: 1007-1007

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
The following example enable iSCSI:
(NETGEAR Switch)#configure
(NETGEAR Switch)(config)#iscsi enable
Command example:
The following examples shows that iSCSI sessions and connections are established using
TCP ports 3260 or 860. Packets sent on detected iSCSI TCP connections are assigned to
traffic class 2 (see the CoS configuration shown below). Because remark is enabled, the
packets are marked with IEEE 802.1p priority to 5 before transmission.
(NETGEAR Switch)#show iscsi
iscsi enabled
iSCSI vpt is 5, remark
Session aging time: 10 min
Maximum number of sessions is 192
--------------------------------------------
iSCSI Targets and TCP ports:
--------------------------------------------
T CP Port Target IP Address Name
8 60 Configured Not Configured
3 260 Configured Not Configured
(NETGEAR Switch)#show classofservice dot1p-mapping
User Priority Traffic Class
------------- -------------
0 1
1 0
2 0
3 1
4 2
5 2
6 3
6 3
show iscsi sessions
This command displays the iSCSI sessions.
Default If not specified, sessions are displayed in short mode (not detailed).
Format show iscsi sessions [detailed]
Mode Privileged EXEC
Quality of Service Commands 1007
