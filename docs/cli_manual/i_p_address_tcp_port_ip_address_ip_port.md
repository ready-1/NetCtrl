# i_p_address_tcp_port_ip_address_ip_port

Pages: 1008-1013

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) # show iscsi sessions
Target: iqn.1993-11.com.disk-vendor:diskarrays.sn.45678
-----------------------------------------------------------
Initiator: iqn.1992-04.com.os-vendor.plan9:cdrom.12
ISID: 11
Initiator: iqn.1995-05.com.os-vendor.plan9:cdrom.10
ISID: 222
-----------------------------------------------------------
Target: iqn.103-1.com.storage-vendor:sn.43338.
storage.tape:sys1.xyz
Session 3:
Initiator: iqn.1992-04.com.os-vendor.plan9:cdrom.12
Session 4:
Initiator: iqn.1995-05.com.os-vendor.plan9:cdrom.10
-----------------------------------------------------------
Command example:
(NETGEAR Switch)# show iscsi sessions detailed
Target: iqn.1993-11.com.disk-vendor:diskarrays.sn.45678
-----------------------------------------------------------
Session 1:
Initiator: iqn.1992-04.com.os
vendor.plan9:cdrom.12.storage:sys1.xyz
-----------------------------------------------------------
Time started: 17-Jul-2008 10:04:50
Time for aging out: 10 min
ISID: 11
Initiator Initiator T arget Target
I P address TCP port IP address IP port
172.16.1.3 4 9154 1 72.16.1.20 30001
1 72.16.1.4 4 9155 1 72.16.1.21 30001
1 72.16.1.5 4 9156 1 72.16.1.22 30001
Session 2:
-----------------------------------------------------------
Initiator: iqn.1995-05.com.os-vendor.plan9:cdrom.10
Time started: 17-Aug-2008 21:04:50
Time for aging out: 2 min
ISID: 22
Initiator Initiator T arget Target
I P address TCP port IP address IP port
1 72.16.1.30 4 9200 1 72.16.1.20 30001
1 72.16.1.30 4 9201 1 72.16.1.21 30001
Quality of Service Commands 1008

Data Center Commands

Data center commands allow you to deploy lossless Ethernet capabilities in support of a
converged network with fiber channel and Ethernet data, as specified by the FC-BB-5 working
group of ANSI T11. This capability allows you to deploy networks at a lower cost while
maintaining the same network management operations.
This chapter contains the following section:
• Priority-Based Flow Control Commands
The commands in this chapter are in one of two functional groups:
• Show commands. Display switch settings, statistics, and other information.
• Configuration commands. Configure features and options of the switch. For every
configuration command, there is a show command that displays the configuration setting.

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Priority-Based Flow Control Commands
If flow control is enabled on a physical link, it applies to all traffic on the link. If congestion
occurs, the hardware sends pause frames that temporarily suspend the traffic flow. Pausing
traffic helps to prevent buffer overflow and dropped frames.
Priority-based flow control (PFC) provides a way to distinguish which traffic on physical link is
paused when congestion occurs, based on the priority of the traffic. You can configure an
interface to pause high priority traffic only (that is, loss-sensitive traffic) when necessary to
prevent dropped frames, while allowing traffic with greater loss tolerance to continue to flow
on the interface.
Priorities are differentiated by the priority field in the IEEE 802.1Q VLAN header, which
identifies an IEEE 802.1p priority value. These priority values must be mapped to internal
class-of-service (CoS) values on the switch.
To enable priority-based flow control for a particular CoS value on an interface, do the
following:
1. Ensure that VLAN tagging is enabled on the interface so that the 802.1p priority values
are carried through the network (see Provisioning (IEEE 802.1p) Commands on
p age449).
2. Ensure that 802.1p priority values are mapped to CoS values on the switch (see
classofservice dot1p-mapping on p age929).
If priority flow control is disabled, the interface defaults to the IEEE 802.3x flow control setting
for the interface. If priority based flow control is enabled, the interface does not pause CoS
unless at least one no-drop priority is configured.
priority-flow-control mode
Use the priority-flow-control mode on command in Datacenter-Bridging Config
mode to enable Priority-Flow-Control (PFC) on the given interface.
PFC must be enabled before FIP snooping can operate over the interface. VLAN tagging
(trunk or general mode) must be enabled on the interface to carry the dot1p value through the
network. Additionally, mapping between dot1p and the queues must be set to one-to-one.
If PFC is enabled on an interface, the normal pause control mechanism is operationally
disabled.
Default off
Format priority-flow-control mode {on | off}
Mode Datacenter-Bridging Config mode
Data Center Commands 1010

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
The following example enables PFC on an interface:
(NETGEAR Switch) (config) #interface te1/0/1
(NETGEAR Switch) (config-if-Te1/0/1) #datacenter-bridging
(NETGEAR Switch) (config-if-dcb) #priority-flow-control mode on
no priority-flow-control mode
Use this command to disable PFC.
Format no priority-flow-control mode
Mode Datacenter-Bridging Config mode
priority-flow-control priority
Use this command to enable the priority group for lossless (no-drop) or lossy (drop) behavior
on an interface. You can enable up to two lossless priorities on an interface. You must
configure the same no-drop priorities across the network to ensure end-to-end lossless
behavior.
The command does not take effect on interfaces on which PFC is not enabled. VLAN tagging
must be enabled on the interface to carry the dot1p value through the network. Additionally,
mapping between dot1p and the queues must be set to one-to-one.
Default drop
Format priority-flow-control priority priority-list {drop | no-drop}
Mode Datacenter-Bridging Config mode
Command example:
The following example sets priority 3 to no drop behavior:
(NETGEAR Switch) (config) #interface te1/0/1
(NETGEAR Switch) (config-if-Te1/0/1) #datacenter-bridging
(NETGEAR Switch) (config-if-dcb) #priority-flow-control mode on
(NETGEAR Switch) (config-if-dcb) #priority-flow-control priority 1 no-drop
no priority-flow-control priority
Use this command to enable lossy behavior for all priorities on the interface. The command
does not take effect on interfaces on which PFC is not enabled or for which lossy (drop)
priorities are configured.
Format no priority-flow-control priority
Mode Datacenter-Bridging Config mode
Data Center Commands 1011

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
clear priority-flow-control statistics
Use this command to clear all global and interface PFC statistics.
Format clear priority-flow-control statistics
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #clear priority-flow-control statistics
show interface priority-flow-control
Use this command in to display the PFC information for all interfaces or for a specified
interface. If you do not specify an interface, the command output provides information about
all interfaces.
Format show interface [unit/slot/port] priority-flow-control
Mode Privileged EXEC
Parameter Description
Interface Detail The interface for which data is displayed.
PFC Operational Status The operational status of the interface.
PFC Configured State The administrative mode of PFC on the interface.
Configured Drop Priorities The 802.1p priority values that are configured with a drop priority on the interface. Drop
priorities do not participate in traffic pausing.
Configured No-Drop The 802.1p priority values that are configured with a no-drop priority on the interface. If an
Priorities 802.1p priority that is designated as no-drop is congested, the priority is paused.
Operational Drop The 802.1p priority values that the switch is using with a drop priority. If the interface accepted
Priorities different priorities from a peer device, the operational drop priorities might not be the same as
the configured priorities.
Configured No-Drop The 802.1p priority values that the switch is using with a no-drop priority. If the interface
Priorities accepted different priorities from a peer device, the operational drop priorities might not be
the same as the configured priorities.
Delay Allowance The link delay allowance on the interface, measured in bit times.
Peer Configuration Indicates whether the switch accepted a compatible configuration from a peer switch.
Compatible
Compatible Configuration The number of received configurations that were accepted and processed as valid. This
Count number does not include duplicate configurations.
Incompatible The number of received configurations that were not accepted from a peer device because
Configuration Count they were incompatible.
Priority The 802.1p priority value.
Data Center Commands 1012

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
Received PFC Frames The number of PFC frames that were received by the interface with the associated 802.1p
priority.
Transmitted PFC Frames The number of PFC frames that were transmitted by the interface with the associated 802.1p
priority.
Command example:
(NETGEAR Switch) #show interface 0/1 priority-flow-control
Interface Detail: 0/1
PFC Configured State: Disabled
PFC Operational State: Enabled
Configured Drop Priorities: 2-7
Operational Drop Priorities: 2-7
Configured No-Drop Priorities: 0-1
O perational No-Drop Priorities: 0-1
Delay Allowance: 32456 bit times
Peer Configuration Compatible: True
Compatible Configuration Count: 3
Incompatible Configuration Count: 1
P riority R eceived PFC Frames Transmitted PFC Frames
- ------- - -------------------- ----------------------
0 0 0
1 0 0
2 0 0
3 0 0
4 0 0
5 0 0
6 0 0
7 0 0
Command example:
(NETGEAR Switch) #show interface priority-flow-control
Port Drop No-Drop Oper
P riorities P riorities State
- ----- ---------- ---------- -------
1/0/1 1 -4,7 5,6 Enabled
1/0/2 1-4,6-7 5 Enabled
1 /0/48 1-4,7 5 ,6 Enabled
Data Center Commands 1013
