# oui_status_description_-_--------_----------_---------

Pages: 1002-1005

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
0/4 Disabled Down
0/5 Disabled Down
show auto-voip oui-table
Use this command to display the VoIP OUI table information.
Format show auto-voip oui-table
Mode Privileged EXEC
Parameter Description
OUI OUI of the source MAC address.
Status Default or configured entry.
OUI Description Description of the OUI.
Command example:
(NETGEAR Switch)# show auto-voip oui-table
OUI Status Description
- -------- ---------- ---------
00:01:E3 Default SIEMENS
0 0:03:6B Default CISCO1
0 0:01:01 Configured VoIP phone
iSCSI Optimization Commands
This section describes commands you use to monitor iSCSI sessions and prioritize iSCSI
packets. iSCSI Optimization provides a means of giving traffic between iSCSI initiator and
target systems special Quality of Service (QoS) treatment. This is accomplished by
monitoring traffic to detect packets used by iSCSI stations to establish iSCSI sessions and
connections. Data from these exchanges is used to create classification rules that assign the
traffic between the stations to a configured traffic class. Packets in the flow are queued and
scheduled for egress on the destination port based on these rules.
iscsi aging time
This command sets the aging time for iSCSI sessions. Behavior when changing aging time:
• When aging time is increased, current sessions will be timed out according to the new
value.
• When aging time is decreased, any sessions that have been dormant for a time
exceeding the new setting will be immediately deleted from the table. All other sessions
will continue to be monitored against the new time out value.
Quality of Service Commands 1002

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default 10 minutes
Format iscsi aging time time
Mode Global Config
Parameter Description
time The number of minutes a session must be inactive prior to its removal. Range: 1-43,200.
Command example:
The following example sets the aging time for iSCSI sessions to 100 minutes:
(NETGEAR Switch)(config)#iscsi aging time 100
no iscsi aging time
Use the no iscsi aging time command to reset the aging time value to the default
value.
Format no iscsi aging time
Mode Global Config
iscsi cos
This command sets the quality of service profile that will be applied to iSCSI flows. iSCSI
flows are assigned by default to the highest VPT or DSCP mapped to the highest queue not
used for switch management. Take care that you configure the relevant Class of Service
parameters for the queue in order to complete the setting.
Setting the VPT or DSCP sets the QoS profile which determines the egress queue to which
the frame is mapped. The switch default setting for egress queues scheduling is Weighted
Round Robin (WRR).
You can complete the QoS setting by configuring the relevant ports to work in other
scheduling and queue management modes via the Class of Service settings. Depending on
the platform, these choices may include strict priority for the queue used for iSCSI traffic. The
downside of strict priority is that, in certain circumstances (under heavy high priority traffic),
other lower priority traffic may get starved. In WRR the queue to which the flow is assigned to
can be set to get the required percentage.
iSCSI optimization is best applied to mixed-traffic networks in which iSCSI packets constitute
a portion of overall traffic. In these cases, the assignment of iSCSI packets to nondefault
queues can provide flows with lower latency and prevent queue resource contention.
If iSCSI frames comprise most of the traffic passing through the switch, the system provides
optimal throughput if all traffic is assigned to the default queue. An example of this situation is
a Storage Area Network (SAN) in which the switch is dedicated to interconnecting iSCSI
Quality of Service Commands 1003

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
targets with initiators. Using the default queue for this homogenous traffic provides the best
performance in traffic-burst handling and the most accurate 802.3x Flow Control Pause
Frame generation. In these cases, iSCSI Flow Acceleration, which can assign iSCSI frames
to queues other than the default queue, might result in lower overall throughput or increased
packet loss.
Format iscsi cos {vpt vpt | dscp dscp} [remark]
Mode Global Config
Parameter Description
vpt or dscp The VLAN Priority Tag or DSCP to assign iSCSI session packets.
remark Mark the iSCSI frames with the configured VPT or DSCP when egressing the switch.
Command example:
The following example sets the quality of service profile that is applied to iSCSI flows:
(NETGEAR Switch)(config)#iscsi cos vpt 5 remark
no iscsi cos
Use the no iscsi cos command to return to the default.
Format no iscsi cos
Mode Global Config
iscsi cos enable
This command enables the assignment of iSCSI flows that you can configure with the iscsi
cos command.
Format iscsi cos enable
Mode Global Config
no iscsi cos enable
This command disables the assignment of iSCSI flows.
Format no iscsi cos enable
Mode Global Config
Quality of Service Commands 1004

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
iscsi enable
This command globally enables iSCSI awareness.
Default disabled
Format iscsi enable
Mode Global Config
Command example:
The following example enables iSCSI awareness:
(NETGEAR Switch)(config) #iscsi enable
no iscsi enable
This command disables iSCSI awareness. When you use the no iscsi enable
command, iSCSI resources are released.
Format no iscsi enable
Mode Global Config
iscsi target port
This command configures an iSCSI target port and, optionally, a target system’s IP address
and IQN name. When working with private iSCSI ports (not IANA-assigned ports 3260/860),
it is recommended to specify the target IP address as well, so that the switch will only snoop
frames with which the TCP destination port is one of the configured TCP ports, and the
destination IP is the target’s IP address. This way the CPU will not be falsely loaded by
non-iSCSI flows (if by chance other applications also choose to use these un-reserved ports.
When a port is already defined and not bound to an IP address, and you want to bind it to an
IP address, first remove it by using the no form of the command and then add it again, this
time together with the relevant IP address.
Target names are only for display when using the show iscsi command. These names are
not used to match with the iSCSI session information acquired by snooping.
A maximum of 16 TCP ports can be configured either bound to IP or not.
Default iSCSI well-known ports 3260 and 860 are configured as default but can be removed as any other
configured target.
Format iscsi target port tcp-port-1 [tcp-port-2...tcp-port-16] [address ip-address]
[name targetname]
Mode Global Config
Quality of Service Commands 1005
