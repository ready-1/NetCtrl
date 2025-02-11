# ROOT ID

Pages: 403-506

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Regional Root Path Cost........................ 0
Associated FIDs Associated VLANs
--------------- ----------------
show spanning-tree active
This command displays the spanning tree values on active ports for the modes xSTP and
PV(R)STP.
Format show spanning-tree active
Mode Privileged EXEC
User EXEC
Command example:
(NETGEAR switch) #show spanning-tree active
Spanning Tree: Enabled (BPDU Flooding: Disabled) Portfast BPDU Filtering: Disabled
Mode: rstp
CST Regional Root: 80:00:00:01:85:48:F0:0F
Regional Root Path Cost: 0
###### MST 0 Vlan Mapped: 3
ROOT ID
Priority 32768
Address 00:00:EE:EE:EE:EE
This Switch is the Root.
Hello Time: 2s Max Age: 20s Forward Delay: 15s
Interfaces
Name State Prio.Nbr Cost Sts Role RestrictedPort
--------- -------- --------- --------- ------------- ----- --------------
0/49 Enabled 128.49 2000 Forwarding Desg No
3/1 Enabled 96.66 5000 Forwarding Desg No
3/2 Enabled 96.67 5000 Forwarding Desg No
3/10 Enabled 96.75 0 Forwarding Desg No
Command example:
(NETGEAR switch) #show spanning-tree active
Spanning-tree enabled protocol rpvst
Switching Commands 403

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
VLAN 1
RootID Priority 32769
Address 00:00:EE:EE:EE:EE
Cost 0
Port This switch is the root
Hello Time 2 Sec Max Age 20 sec Forward Delay 15 sec
BridgeID Priority 32769 (priority 32768 sys-id-ext 1)
Address 00:00:EE:EE:EE:EE
Hello Time 2 Sec Max Age 20 sec Forward Delay 15 sec
Aging Time 300 sec
Interface State Prio.Nbr Cost Status Role
--------- --------- --------- ------- ------------- -----------
0/49 Enabled 128.49 2000 Forwarding Designated
3/1 Enabled 128.66 5000 Forwarding Designated
3/2 Enabled 128.67 5000 Forwarding Designated
3/10 Enabled 128.75 0 Forwarding Designated
VLAN 3
RootID Priority 32771
Address 00:00:EE:EE:EE:EE
Cost 0
Port This switch is the root
Hello Time 2 Sec Max Age 20 sec Forward Delay 15 sec
BridgeID Priority 32771 (priority 32768 sys-id-ext 3)
Address 00:00:EE:EE:EE:EE
Hello Time 2 Sec Max Age 20 sec Forward Delay 15 sec
Aging Time 300 sec
Interface State Prio.Nbr Cost Status Role
--------- --------- --------- ------- ------------- -----------
3/1 Enabled 128.66 5000 Forwarding Designated
3/2 Enabled 128.67 5000 Forwarding Designated
3/10 Enabled 128.75 0 Forwarding Designated
Command example:
(NETGEAR switch) #show spanning-tree active
Spanning-tree enabled protocol rpvst
VLAN 1
RootID Priority 32769
Address 00:00:EE:EE:EE:EE
Cost 0
Port 10(3/10 )
Hello Time 2 Sec Max Age 20 sec Forward Delay 15 sec
Switching Commands 404

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
BridgeID Priority 32769 (priority 32768 sys-id-ext 1)
Address 00:00:EE:EE:EE:EE
Hello Time 2 Sec Max Age 20 sec Forward Delay 15 sec
Aging Time 300 sec
Interface State Prio.Nbr Cost Status Role
--------- --------- --------- ------- ------------- -----------
0/49 Enabled 128.49 2000 Discarding Alternate
3/1 Enabled 128.66 5000 Forwarding Disabled
3/2 Enabled 128.67 5000 Forwarding Disabled
3/10 Enabled 128.75 0 Forwarding Root
VLAN 3
RootID Priority 32771
Address 00:00:EE:EE:EE:EE
Cost 0
Port 10(3/10 )
Hello Time 2 Sec Max Age 20 sec Forward Delay 15 sec
BridgeID Priority 32771 (priority 32768 sys-id-ext 3)
Address 00:00:EE:EE:EE:EE
Hello Time 2 Sec Max Age 20 sec Forward Delay 15 sec
Aging Time 300 sec
Interface State Prio.Nbr Cost Status Role
--------- --------- --------- ------- ------------- -----------
3/1 Enabled 128.66 5000 Forwarding Disabled
3/2 Enabled 128.67 5000 Forwarding Disabled
3/10 Enabled 128.75 0 Forwarding Root
show spanning-tree backbonefast
This command displays spanning tree information for backbonefast.
Format show spanning-tree backbonefast
Mode Privileged EXEC
User EXEC
Term Definition
Transitions via Backbonefast The number of backbonefast transitions.
Inferior BPDUs received (all VLANs) The number of inferior BPDUs received on all VLANs.
RLQ request PDUs received (all VLANs) The number of root link query (RLQ) requests PDUs received on all
VLANs.
RLQ response PDUs received (all VLANs) The number of RLQ response PDUs received on all VLANs.
Switching Commands 405

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
RLQ request PDUs sent (all VLANs) The number of RLQ request PDUs sent on all VLANs.
RLQ response PDUs sent (all VLANs) The number of RLQ response PDUs sent on all VLANs.
Command example:
(NETGEAR Switch)#show spanning-tree backbonefast
Backbonefast Statistics
-----------------------
Transitions via Backbonefast (all VLANs) : 0
Inferior BPDUs received (all VLANs) : 0
RLQ request PDUs received (all VLANs) : 0
RLQ response PDUs received (all VLANs) : 0
RLQ request PDUs sent (all VLANs) : 0
RLQ response PDUs sent (all VLANs) : 0
show spanning-tree brief
This command displays spanning tree settings for the bridge. The following information
appears.
Format show spanning-tree brief
Mode Privileged EXEC
User EXEC
Term Definition
Bridge Priority Configured value.
Bridge Identifier The bridge identifier for the selected MST instance. It is made up using the bridge priority and the
base MAC address of the bridge.
Bridge Max Age Configured value.
Bridge Max Hops Bridge max-hops count for the device.
Bridge Hello Time Configured value.
Bridge Forward Configured value.
Delay
Bridge Hold Time Minimum time between transmission of Configuration Bridge Protocol Data Units (BPDUs).
Switching Commands 406

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show spanning-tree brief
Bridge Priority................................ 32768
Bridge Identifier.............................. 80:00:00:10:18:48:FC:07
Bridge Max Age................................. 20
Bridge Max Hops................................ 20
Bridge Hello Time.............................. 2
Bridge Forward Delay........................... 15
Bridge Hold Time............................... 6
show spanning-tree interface
This command displays the settings and parameters for a specific switch port within the
common and internal spanning tree. The unit/slot/port is the desired switch port.
Instead of unit/slot/port, lag lag-intf-num can be used as an alternate way to
specify the LAG interface, in which lag-intf-num is the LAG port number. The following
details are displayed on execution of the command.
Format show spanning-tree interface [unit/slot/port | lag lag-intf-num]
Mode Privileged EXEC
User EXEC
Term Definition
Hello Time Admin hello time for this port.
Port Mode Enabled or disabled.
BPDU Guard Effect Enabled or disabled.
Root Guard Enabled or disabled.
Loop Guard Enabled or disabled.
TCN Guard Enable or disable the propagation of received topology change notifications and topology changes
to other ports.
BPDU Filter Mode Enabled or disabled.
BPDU Flood Mode Enabled or disabled.
Auto Edge To enable or disable the feature that causes a port that has not seen a BPDU for edge delay time, to
become an edge port and transition to forwarding faster.
Port Up Time Since Time since port was reset, displayed in days, hours, minutes, and seconds.
Counters Last
Cleared
STP BPDUs Spanning Tree Protocol Bridge Protocol Data Units sent.
Transmitted
Switching Commands 407

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
STP BPDUs Spanning Tree Protocol Bridge Protocol Data Units received.
Received
RSTP BPDUs Rapid Spanning Tree Protocol Bridge Protocol Data Units sent.
Transmitted
RSTP BPDUs Rapid Spanning Tree Protocol Bridge Protocol Data Units received.
Received
MSTP BPDUs Multiple Spanning Tree Protocol Bridge Protocol Data Units sent.
Transmitted
MSTP BPDUs Multiple Spanning Tree Protocol Bridge Protocol Data Units received.
Received
Command example:
(NETGEAR Switch) #show spanning-tree interface 0/1
Hello Time..................................... Not Configured
Port Mode...................................... Enabled
BPDU Guard Effect.............................. Disabled
Root Guard..................................... FALSE
Loop Guard..................................... FALSE
TCN Guard...................................... FALSE
BPDU Filter Mode............................... Disabled
BPDU Flood Mode................................ Disabled
Auto Edge...................................... TRUE
Port Up Time Since Counters Last Cleared....... 8 day 3 hr 39 min 58 sec
STP BPDUs Transmitted.......................... 0
STP BPDUs Received............................. 0
RSTP BPDUs Transmitted......................... 0
RSTP BPDUs Received............................ 0
MSTP BPDUs Transmitted......................... 0
MSTP BPDUs Received............................ 0
Command example:
(NETGEAR Switch) #show spanning-tree interface lag 1
Hello Time..................................... Not Configured
Port Mode...................................... Enabled
BPDU Guard Effect.............................. Disabled
Root Guard..................................... FALSE
Loop Guard..................................... FALSE
TCN Guard...................................... FALSE
BPDU Filter Mode............................... Disabled
BPDU Flood Mode................................ Disabled
Auto Edge...................................... TRUE
Port Up Time Since Counters Last Cleared....... 8 day 3 hr 42 min 5 sec
Switching Commands 408

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
STP BPDUs Transmitted.......................... 0
STP BPDUs Received............................. 0
RSTP BPDUs Transmitted......................... 0
RSTP BPDUs Received............................ 0
MSTP BPDUs Transmitted......................... 0
MSTP BPDUs Received............................ 0
show spanning-tree mst detailed
This command displays the detailed settings for an MST instance.
Format show spanning-tree mst detailed mstid
Mode Privileged EXEC
User EXEC
Parameter Description
mstid A multiple spanning tree instance identifier. The value is 0–4094.
Command example:
(NETGEAR Switch) #show spanning-tree mst detailed 0
MST Instance ID................................ 0
MST Bridge Priority............................ 32768
MST Bridge Identifier.......................... 80:00:00:10:18:48:FC:07
Time Since Topology Change..................... 8 day 3 hr 47 min 7 sec
Topology Change Count.......................... 0
Topology Change in progress.................... FALSE
Designated Root................................ 80:00:00:10:18:48:FC:07
Root Path Cost................................. 0
Root Port Identifier........................... 00:00
Associated FIDs Associated VLANs
--------------- ----------------
show spanning-tree mst port detailed
This command displays the detailed settings and parameters for a specific switch port within
a particular multiple spanning tree instance. The parameter mstid is a number that
corresponds to the desired existing multiple spanning tree instance. The unit/slot/port
is the desired switch port. Instead of unit/slot/port, lag lag-intf-num can be used
as an alternate way to specify the LAG interface, in which lag-intf-num is the LAG port
number.
Switching Commands 409

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format show spanning-tree mst port detailed mstid [unit/slot/port | lag lag-intf-num]
Mode Privileged EXEC
User EXEC
Term Definition
MST Instance ID The ID of the existing multiple spanning tree (MST) instance identifier. The value is 0–4094.
Port Identifier The port identifier for the specified port within the selected MST instance. It is made up from the port
priority and the interface number of the port.
Port Priority The priority for a particular port within the selected MST instance. The port priority is displayed in
multiples of 16.
Port Forwarding Current spanning tree state of this port.
State
Port Role Each enabled MST Bridge Port receives a Port Role for each spanning tree. The port role is one of
the following values: Root Port, Designated Port, Alternate Port, Backup Port, Master Port or
Disabled Port
Auto-Calculate Port Indicates whether auto calculation for port path cost is enabled.
Path Cost
Port Path Cost Configured value of the Internal Port Path Cost parameter.
Designated Root The Identifier of the designated root for this port.
Root Path Cost The path cost to get to the root bridge for this instance. The root path cost is zero if the bridge is the
root bridge for that instance.
Designated Bridge Bridge Identifier of the bridge with the Designated Port.
Designated Port Port on the Designated Bridge that offers the lowest cost to the LAN.
Identifier
Loop Inconsistent The current loop inconsistent state of this port in this MST instance. When in loop inconsistent state,
State the port has failed to receive BPDUs while configured with loop guard enabled. Loop inconsistent
state maintains the port in a blocking state until a subsequent BPDU is received.
Transitions Into The number of times this interface has transitioned into loop inconsistent state.
Loop Inconsistent
State
Transitions Out of The number of times this interface has transitioned out of loop inconsistent state.
Loop Inconsistent
State
If you specify 0 (defined as the default CIST ID) as the mstid, this command displays the
settings and parameters for a specific switch port within the common and internal spanning
tree. The unit/slot/port is the desired switch port. In this case, the following are
displayed
Switching Commands 410

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
.
Term Definition
Port Identifier The port identifier for this port within the CST.
Port Priority The priority of the port within the CST.
Port Forwarding The forwarding state of the port within the CST.
State
Port Role The role of the specified interface within the CST.
Auto-Calculate Port Indicates whether auto calculation for port path cost is enabled or not (disabled).
Path Cost
Port Path Cost The configured path cost for the specified interface.
Auto-Calculate Indicates whether auto calculation for external port path cost is enabled.
External Port Path
Cost
External Port Path The cost to get to the root bridge of the CIST across the boundary of the region. This means that if
Cost the port is a boundary port for an MSTP region, then the external path cost is used.
Designated Root Identifier of the designated root for this port within the CST.
Root Path Cost The root path cost to the LAN by the port.
Designated Bridge The bridge containing the designated port.
Designated Port Port on the Designated Bridge that offers the lowest cost to the LAN.
Identifier
Topology Change Value of flag in next Configuration Bridge Protocol Data Unit (BPDU) transmission indicating if a
Acknowledgement topology change is in progress for this port.
Hello Time The hello time in use for this port.
Edge Port The configured value indicating if this port is an edge port.
Edge Port Status The derived value of the edge port status. True if operating as an edge port; false otherwise.
Point To Point MAC Derived value indicating if this port is part of a point to point link.
Status
CST Regional Root The regional root identifier in use for this port.
CST Internal Root The internal root path cost to the LAN by the designated external port.
Path Cost
Loop Inconsistent The current loop inconsistent state of this port in this MST instance. When in loop inconsistent state,
State the port has failed to receive BPDUs while configured with loop guard enabled. Loop inconsistent
state maintains the port in a blocking state until a subsequent BPDU is received.
Switching Commands 411

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Transitions Into The number of times this interface has transitioned into loop inconsistent state.
Loop Inconsistent
State
Transitions Out of The number of times this interface has transitioned out of loop inconsistent state.
Loop Inconsistent
State
Command example:
The following example shows output for the command in the slot/port format:
(NETGEAR Switch) #show spanning-tree mst port detailed 0 0/1
Port Identifier................................ 80:01
Port Priority.................................. 128
Port Forwarding State.......................... Disabled
Port Role...................................... Disabled
Auto-calculate Port Path Cost.................. Enabled
Port Path Cost................................. 0
Auto-Calculate External Port Path Cost......... Enabled
External Port Path Cost........................ 0
Designated Root................................ 80:00:00:10:18:48:FC:07
Root Path Cost................................. 0
Designated Bridge.............................. 80:00:00:10:18:48:FC:07
Designated Port Identifier..................... 00:00
Topology Change Acknowledge.................... FALSE
Hello Time..................................... 2
Edge Port...................................... FALSE
Edge Port Status............................... FALSE
Point to Point MAC Status...................... TRUE
CST Regional Root.............................. 80:00:00:10:18:48:FC:07
CST Internal Root Path Cost.................... 0
Loop Inconsistent State........................ FALSE
Transitions Into Loop Inconsistent State....... 0
Transitions Out Of Loop Inconsistent State..... 0
Command example:
The following example shows output using a LAG interface number:
(NETGEAR Switch) #show spanning-tree mst port detailed 0 lag 1
Port Identifier................................ 60:42
Port Priority.................................. 96
Port Forwarding State.......................... Disabled
Port Role...................................... Disabled
Switching Commands 412

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Auto-calculate Port Path Cost.................. Enabled
Port Path Cost................................. 0
Auto-Calculate External Port Path Cost......... Enabled
External Port Path Cost........................ 0
Designated Root................................ 80:00:00:10:18:48:FC:07
Root Path Cost................................. 0
Designated Bridge.............................. 80:00:00:10:18:48:FC:07
Designated Port Identifier..................... 00:00
Topology Change Acknowledge.................... FALSE
Hello Time..................................... 2
Edge Port...................................... FALSE
Edge Port Status............................... FALSE
Point to Point MAC Status...................... TRUE
CST Regional Root.............................. 80:00:00:10:18:48:FC:07
CST Internal Root Path Cost.................... 0
Loop Inconsistent State........................ FALSE
Transitions Into Loop Inconsistent State....... 0
Transitions Out Of Loop Inconsistent State..... 0
--More-- or (q)uit
show spanning-tree mst port summary
This command displays the settings of one or all ports within the specified multiple spanning
tree instance. The parameter mstid indicates a particular MST instance. The parameter
unit/slot/port indicates the desired switch port; the keyword all indicates all ports.
Instead of unit/slot/port, lag lag-intf-num can be used as an alternate way to
specify the LAG interface, in which lag-intf-num is the LAG port number.
If you specify 0 (defined as the default CIST ID) as the mstid, the status summary displays
for one or all ports within the common and internal spanning tree.
Format show spanning-tree mst port summary mstid {unit/slot/port | lag lag-intf-num |
all}
Mode Privileged EXEC
User EXEC
Term Definition
MST Instance ID The MST instance associated with this port.
Interface The interface.
STP Mode Indicates whether spanning tree is enabled or disabled on the port.
Type Currently not used.
STP State The forwarding state of the port in the specified spanning tree instance.
Switching Commands 413

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Port Role The role of the specified port within the spanning tree.
Desc Indicates whether the port is in loop inconsistent state or not. This field is blank if the loop guard
feature is not available.
Command example:
The following example shows output in the slot/port format:
(NETGEAR Switch) #show spanning-tree mst port summary 0 0/1
MST Instance ID................................ CST
STP STP Port
Interface Mode Type State Role Desc
--------- -------- ------- ----------------- ---------- ----------
0/1 Enabled Disabled Disabled
Command example:
The following example shows output using a LAG interface number:
(NETGEAR Switch) #show spanning-tree mst port summary 0 lag 1
MST Instance ID................................ CST
STP STP Port
Interface Mode Type State Role Desc
--------- -------- ------- ----------------- ---------- ----------
3/1 Enabled Disabled Disabled
show spanning-tree mst port summary active
This command displays settings for the ports within the specified multiple spanning tree
instance that are active links.
Format show spanning-tree mst port summary mstid active
Mode Privileged EXEC
User EXEC
Term Definition
MST Instance ID The ID of the existing MST instance.
Interface The interface.
STP Mode Indicates whether spanning tree is enabled or disabled on the port.
Switching Commands 414

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Type Currently not used.
STP State The forwarding state of the port in the specified spanning tree instance.
Port Role The role of the specified port within the spanning tree.
Desc Indicates whether the port is in loop inconsistent state or not. This field is blank if the loop guard
feature is not available.
Command example:
(NETGEAR Switch) #show spanning-tree mst port summary 0 active
STP STP Port
Interface Mode Type State Role Desc
--------- -------- ------- ----------------- ---------- ---------
show spanning-tree mst summary
This command displays summary information about all multiple spanning tree instances in
the switch. On execution, the following details are displayed.
Format show spanning-tree mst summary
Mode Privileged EXEC
User EXEC
Term Definition
MST Instance ID List of multiple spanning trees IDs currently configured.
List
For each MSTID: List of forwarding database identifiers associated with this instance.
Associated FIDs List of VLAN IDs associated with this instance.
Associated VLANs
show spanning-tree summary
This command displays spanning tree settings and parameters for the switch. The following
details are displayed on execution of the command.
Format show spanning-tree summary
Mode Privileged EXEC
User EXEC
Switching Commands 415

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Spanning Tree Adminmode Enabled or disabled.
Spanning Tree Version Version of 802.1 currently supported (IEEE 802.1s, IEEE 802.1w, or IEEE 802.1d)
based upon the Force Protocol Version parameter.
BPDU Guard Mode Enabled or disabled.
BPDU Filter Mode Enabled or disabled.
Configuration Name Identifier used to identify the configuration currently being used.
Configuration Revision Level Identifier used to identify the configuration currently being used.
Configuration Digest Key A generated Key used in the exchange of the BPDUs.
Configuration Format Selector Specifies the version of the configuration format being used in the exchange of
BPDUs. The default value is zero.
MST Instances List of all multiple spanning tree instances configured on the switch.
Command example:
(NETGEAR Switch) #show spanning-tree summary
Spanning Tree Adminmode........... Enabled
Spanning Tree Version............. IEEE 802.1s
BPDU Guard Mode................... Disabled
BPDU Filter Mode.................. Disabled
Configuration Name................ ****
Configuration Revision Level...... ****
Configuration Digest Key.......... ****
Configuration Format Selector..... 0
No MST instances to display.
show spanning-tree uplinkfast
This command displays spanning tree information for uplinkfast.
Format show spanning-tree uplinkfast
Mode Privileged EXEC
User EXEC
Term Definition
Uplinkfast transitions (all VLANs) The number of uplinkfast transitions on all VLANs.
Proxy multicast addresses transmitted (all The number of proxy multicast addresses transmitted on all VLANs.
VLANs)
Switching Commands 416

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show spanning-tree uplinkfast
Uplinkfast is enabled.
BPDU update rate : 150 packets/sec
Uplinkfast Statistics
---------------------
Uplinkfast transitions (all VLANs)................. 0
Proxy multicast addresses transmitted (all VLANs).. 0
show spanning-tree vlan
This command displays spanning tree information per VLAN and also lists out the port roles
and states along with port cost. The vlan-list parameter is a list of VLANs or
VLAN-ranges separated by commas and with no embedded blank spaces. VLAN ranges are
of the form “X-Y” where X and Y are valid VLAN identifiers and X< Y. The vlanid
corresponds to an existing VLAN ID.
Format show spanning-tree vlan {vlanid | vlan-list}
Mode Privileged EXEC
User EXEC
Command example:
(NETGEAR Switch) show spanning-tree vlan 1
VLAN 1
Spanning-tree enabled protocol rpvst
RootID Priority 32769
Address 00:0C:29:D3:80:EA
Cost 0
Port This switch is the root
Hello Time 2 Sec Max Age 15 sec Forward Delay 15 sec
BridgeID Priority 32769 (priority 32768 sys-id-ext 1)
Address 00:0C:29:D3:80:EA
Hello Time 2 Sec Max Age 15 sec Forward Delay 15 sec
Aging Time 300
Interface Role Sts Cost Prio.Nbr
--------- ---------- ------------- --------- --------
1/0/1 Designated Forwarding 3000 128.1
1/0/2 Designated Forwarding 3000 128.2
1/0/3 Disabled Disabled 3000 128.3
1/0/4 Designated Forwarding 3000 128.4
1/0/5 Designated Forwarding 3000 128.5
1/0/6 Designated Forwarding 3000 128.6
1/0/7 Designated Forwarding 3000 128.7
Switching Commands 417

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
1/0/8 Designated Forwarding 3000 128.8
0/1/1 Disabled Disabled 3000 128.1026
0/1/2 Disabled Disabled 3000 128.1027
0/1/3 Disabled Disabled 3000 128.1028
0/1/4 Disabled Disabled 3000 128.1029
0/1/5 Disabled Disabled 3000 128.1030
0/1/6 Disabled Disabled 3000 128.1031
Loop Protection Commands
This section describes the commands that you can use to configure loop protection. Loop
protection detects physical and logical loops between Ethernet ports on a device. You must
enable loop protection globally before you can enable it at the interface level.
keepalive (Global Config)
This command enables loop protection globally on the switch. As an option, you can
configure the time in seconds between the transmission of keep-alive packets (that is, the
transmit interval) and the maximum number of keep-alive packets (that is, the packet count)
that the switch can receive before an action is taken.
Default Disabled
Interval is 5 seconds
Packet count is 1
Format keepalive [interval] [packet-count]
Mode Global Config
no keepalive (Global Config)
This command disables loop protection globally on the switch. This command also sets the
transmit interval and packet count to the default value.
Format no keepalive
Mode Global Config
keepalive (Interface Config)
This command enables loop protection on an interface.
Default Disabled
Format keepalive
Mode Interface Config
Switching Commands 418

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no keepalive (Interface Config)
This command disables loop protection on an interface.
Format no keepalive
Mode Interface Config
keepalive action
This command configures the action that must follow when a loop is detected on a port.
Default Disable
Format keepalive receive-action {log | disable | both}
Mode Interface Config
Parameter Description
log The message is logged to a buffer log but the interface is not brought down.
disable The interface is brought down but the message is not logged.
both The interface is brought down and the message is logged.
no keepalive action
This command returns the command to the default action of disabling an interface when a
loop is detected.
Format no keepalive receive-action
Mode Interface Config
errdisable recovery cause keep-alive
This command enables the autorecovery of interfaces on which a loop was detected.
Format errdisable recovery cause keep-alive
Mode Global Config
no errdisable recovery cause keep-alive
This command disables the autorecovery of interfaces on which a loop was detected.
Format no errdisable recovery cause keep-alive
Mode Global Config
Switching Commands 419

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show keepalive
This command displays the global keep-alive configuration.
Format show keepalive
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show keepalive
Keepalive...................................... Enabled
Transmit interval.............................. 1
Max PDU Receive................................ 1
show keepalive statistics
This command displays the keep-alive statistics for a specific interface or for all interfaces.
Format show keepalive statistics {port-number | all}
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show keepalive statistics all
Keep Loop Loop Time Since Rx Port
Port Alive Detected Count Last Loop Action Status
------ --------- ----------- -------- ------------- ------------- --------
0/1 Yes Yes 1 85 shut-down D-Disable
0/3 Yes No log-shutdown Enable
clear counters keepalive
This command clears keep-alive statistics that are associated with the interfaces, such as the
number of transmitted packets, the number of received packets, and the number of loop
packets.
Format clear counters keepalive
Mode Privileged EXEC
Switching Commands 420

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
VLAN Commands
This section describes the commands you use to configure VLAN settings.
switchport mode auto
This command globally enables the Auto-Trunk feature. If enabled, the switch can
automatically configure a port as a trunk (that is, an Auto-Trunk) with an interconnected
partner device that supports the Auto-Trunk feature.
After a port or an Auto-LAG becomes an Auto-Trunk, all VLANs on the switch become part of
the trunk, allowing automatic configuration of all VLANs on the switch and partner device with
which the trunk is established.
Default Disabled
Format switchport mode auto
Mode Global Config
no switchport mode auto
This command globally disables the Auto-Trunk feature.
Format no switchport mode auto
Mode Global Config
show interfaces switchport trunk
This command displays information for all interfaces on which the Auto-Trunk feature is
enabled. As an option, you can display the information for a single interface only.
Format show interfaces switchport trunk [unit/port]
Mode Privileged EXEC
Command example:
(Switch)#show interfaces switchport trunk
Global Auto-Trunk Mode : Enabled
Intf PVID Allowed Vlans List Auto-Trunk
--------- ----- -------------------- ---------------
0/3 1 All Yes
0/15 1 All Yes
0/29 1 All Yes
Switching Commands 421

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(Switch)#show interfaces switchport trunk 0/15
Global Auto-Trunk Mode : Enabled
Intf PVID Allowed Vlans List Auto-Trunk
--------- ----- -------------------- ---------------
0/15 1 All Yes
vlan database
This command gives you access to the VLAN Config mode, which allows you to configure
VLAN characteristics.
Format vlan database
Mode Privileged EXEC
vlan
This command creates a new VLAN and assigns it an ID. The ID is a valid VLAN
identification number (ID 1 is reserved for the default VLAN). The VLAN number is in the
range 2–4093.
Format vlan number
Mode VLAN Config
no vlan
This command deletes an existing VLAN. The ID is a valid VLAN identification number (ID 1
is reserved for the default VLAN). The VLAN number is in the range 2–4093.
Format no vlan number
Mode VLAN Config
vlan acceptframe
This command sets the frame acceptance mode on an interface or range of interfaces. For
VLAN Only mode, untagged frames or priority frames received on this interface are
discarded. For Admit All mode, untagged frames or priority frames received on this interface
are accepted and assigned the value of the interface VLAN ID for this port. For
admituntaggedonly mode, only untagged frames are accepted on this interface; tagged
frames are discarded. With any option, VLAN tagged frames are forwarded in accordance
with the IEEE 802.1Q VLAN Specification.
Switching Commands 422

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default all
Format vlan acceptframe {admituntaggedonly | vlanonly | all}
Mode Interface Config
no vlan acceptframe
This command resets the frame acceptance mode for the interface or range of interfaces to
the default value.
Format no vlan acceptframe
Mode Interface Config
vlan ingressfilter
This command enables ingress filtering on an interface or range of interfaces. If ingress
filtering is disabled, frames received with VLAN IDs that do not match the VLAN membership
of the receiving interface are admitted and forwarded to ports that are members of that
VLAN.
Default Disabled
Format vlan ingressfilter
Mode Interface Config
no vlan ingressfilter
This command disables ingress filtering. If ingress filtering is disabled, frames received with
VLAN IDs that do not match the VLAN membership of the receiving interface are admitted
and forwarded to ports that are members of that VLAN.
Format no vlan ingressfilter
Mode Interface Config
vlan internal allocation
Use this command to configure which VLAN IDs to use for port-based routing interfaces.
When a port-based routing interface is created, an unused VLAN ID is assigned internally.
Format vlan internal allocation {base vlan-id | policy ascending | policy decending}
Mode Global Config
Switching Commands 423

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
base vlan-id The first VLAN ID to be assigned to a port-based routing interface.
policy ascending VLAN IDs assigned to port-based routing interfaces start at the base and increase in value
policy descending VLAN IDs assigned to port-based routing interfaces start at the base and decrease in value
vlan makestatic
This command changes a dynamically created VLAN (created by GVRP registration) to a
static VLAN (one that is permanently configured and defined). The ID is a valid VLAN
identification number. The VLAN number is in the range is 2–4093.
Format vlan makestatic number
Mode VLAN Config
vlan name
This command changes the name of a VLAN. The name is an alphanumeric string of up to 32
characters, and the number is a valid VLAN identification number. The number is in the range
1–4093.
Default VLAN ID 1 - default
other VLANS - blank string
Format vlan name number name
Mode VLAN Config
no vlan name
This command sets the name of a VLAN to a blank string.
Format no vlan name number
Mode VLAN Config
vlan participation
This command configures the degree of participation for a specific interface or range of
interfaces in a VLAN. The number is a valid VLAN identification number in the range 1-4093,
and the interface is a valid interface number.
Format vlan participation {exclude | include | auto} number
Mode Interface Config
Switching Commands 424

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Participation options are:
Options Definition
include The interface is always a member of this VLAN. This is equivalent to registration fixed.
exclude The interface is never a member of this VLAN. This is equivalent to registration forbidden.
auto The interface is dynamically registered in this VLAN by GVRP and will not participate in this VLAN unless
a join request is received on this interface. This is equivalent to registration normal.
vlan participation all
This command configures the degree of participation for all interfaces in a VLAN. The
number is a valid VLAN identification number in the range 1–4093.
Format vlan participation all {exclude | include | auto} number
Mode Global Config
You can use the following participation options:
Participation Definition
Options
include The interface is always a member of this VLAN. This is equivalent to registration fixed.
exclude The interface is never a member of this VLAN. This is equivalent to registration forbidden.
auto The interface is dynamically registered in this VLAN by GVRP. The interface will not participate in
this VLAN unless a join request is received on this interface. This is equivalent to registration normal.
vlan port acceptframe all
This command sets the frame acceptance mode for all interfaces.
For the all mode, untagged frames or priority frames that enter on an interface are accepted
and assigned the VLAN ID of the interface. With any of the three modes, VLAN-tagged
frames are forwarded in accordance with the IEEE 802.1Q VLAN specification.
Default all
Format vlan port acceptframe all {vlanonly | admituntaggedonly | all}
Mode Global Config
The modes are defined as follows:
Mode Definition
vlanonly VLAN-only mode. Untagged frames or priority frames received on this interface are discarded.
Switching Commands 425

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Mode Definition
admituntaggedonly Admit untagged-only mode. VLAN-tagged and priority tagged frames received on this interface
are discarded.
all Admit all mode. Untagged frames or priority frames received on this interface are accepted and
assigned the value of the interface VLAN ID for this port.
no vlan port acceptframe all
This command sets the frame acceptance mode to the default mode all.
Format no vlan port acceptframe all
Mode Global Config
vlan port ingressfilter all
This command enables ingress filtering for all ports. If ingress filtering is disabled, frames
received with VLAN IDs that do not match the VLAN membership of the receiving interface
are admitted and forwarded to ports that are members of that VLAN.
Default Disabled
Format vlan port ingressfilter all
Mode Global Config
no vlan port ingressfilter all
This command disables ingress filtering for all ports. If ingress filtering is disabled, frames
received with VLAN IDs that do not match the VLAN membership of the receiving interface
are admitted and forwarded to ports that are members of that VLAN.
Format no vlan port ingressfilter all
Mode Global Config
vlan port pvid all
This command changes the VLAN ID for all interfaces. The number is a valid VLAN
identification number in the range 1–4093.
Default 1
Format vlan port pvid all number
Mode Global Config
Switching Commands 426

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no vlan port pvid all
This command sets the VLAN ID for all interfaces to 1.
Format no vlan port pvid all
Mode Global Config
vlan port tagging all
This command configures the tagging behavior for all interfaces in a VLAN to enabled. If
tagging is enabled, traffic is transmitted as tagged frames. If tagging is disabled, traffic is
transmitted as untagged frames. The number is a valid VLAN identification number in the
range 1–4093.
Format vlan port tagging all number
Mode Global Config
no vlan port tagging all
This command configures the tagging behavior for all interfaces in a VLAN to disabled. If
tagging is disabled, traffic is transmitted as untagged frames. The number is a valid VLAN
identification number in the range 1–4093.
Format no vlan port tagging all number
Mode Global Config
vlan protocol group
This command adds protocol-based VLAN groups to the system. The groupid is a unique
number from 1–128 that is used to identify the group in subsequent commands.
Format vlan protocol group groupid
Mode Global Config
vlan protocol group name
This command assigns a name to a protocol-based VLAN group. The groupname variable
can be a character string of 0 to 16 characters.
Format vlan protocol group name groupid groupname
Mode Global Config
Switching Commands 427

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no vlan protocol group name
This command removes the name from the group identified by groupid.
Format no vlan protocol group name groupid
Mode Global Config
vlan protocol group add protocol
This command adds the protocol to the protocol-based VLAN identified by groupid. A group
may have more than one protocol associated with it. Each interface and protocol combination
can only be associated with one group. If adding a protocol to a group causes any conflicts
with interfaces currently associated with the group, this command fails and the protocol is not
added to the group. The possible values for protocol-list includes the keywords ip,
arp, and ipx and hexadecimal or decimal values ranging from 0x0600 (1536) to 0xFFFF
(65535). The protocol list can accept up to 16 protocols separated by a comma.
Default none
Format vlan protocol group add protocol groupid ethertype protocol-list
Mode Global Config
no vlan protocol group add protocol
This command removes the protocols specified in the protocol-list from this
protocol-based VLAN group that is identified by this groupid.
Format no vlan protocol group add protocol groupid ethertype protocol-list
Mode Global Config
protocol group
This command attaches a vlanid to the protocol-based VLAN identified by groupid. A
group can only be associated with one VLAN at a time, however the VLAN association can
be changed.
Default none
Format protocol group groupid vlanid
Mode VLAN Config
Switching Commands 428

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no protocol group
This command removes the vlanid from this protocol-based VLAN group that is identified
by this groupid.
Format no protocol group groupid vlanid
Mode VLAN Config
protocol vlan group
This command adds a physical interface or a range of interfaces to the protocol-based VLAN
identified by groupid. You can associate multiple interfaces with a group, but you can only
associate each interface and protocol combination with one group. If adding an interface to a
group causes any conflicts with protocols currently associated with the group, this command
fails and the interface or interfaces are not added to the group.
Default none
Format protocol vlan group groupid
Mode Interface Config
no protocol vlan group
This command removes the interface from this protocol-based VLAN group that is identified
by this groupid.
Format no protocol vlan group groupid
Mode Interface Config
protocol vlan group all
This command adds all physical interfaces to the protocol-based VLAN identified by
groupid. You can associate multiple interfaces with a group, but you can only associate
each interface and protocol combination with one group. If adding an interface to a group
causes any conflicts with protocols currently associated with the group, this command will fail
and the interface or interfaces are not added to the group.
Default none
Format protocol vlan group all groupid
Mode Global Config
Switching Commands 429

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no protocol vlan group all
This command removes all interfaces from this protocol-based VLAN group that is identified
by this groupid.
Format no protocol vlan group all groupid
Mode Global Config
show port protocol
This command displays the Protocol-Based VLAN information for either the entire system, or
for the indicated group.
Format show port protocol {groupid | all}
Mode Privileged EXEC
Term Definition
Group Name The group name of an entry in the Protocol-based VLAN table.
Group ID The group identifier of the protocol group.
VLAN The VLAN associated with this Protocol Group.
Protocol(s) The type of protocol(s) for this group.
Interface(s) Lists the unit/slot/port interface(s) that are associated with this Protocol Group.
vlan pvid
This command changes the VLAN ID on an interface or range of interfaces. The number is a
valid VLAN identification number in the range 1–4093.
Default 1
Format vlan pvid number
Mode Interface Config
Interface Range Config
no vlan pvid
This command sets the VLAN ID on an interface or range of interfaces to 1.
Format no vlan pvid
Mode Interface Config
Switching Commands 430

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
vlan tagging
This command configures the tagging behavior for a specific interface or range of interfaces
in a VLAN to enabled. If tagging is enabled, traffic is transmitted as tagged frames. If tagging
is disabled, traffic is transmitted as untagged frames. The number is a valid VLAN
identification number in the range 1–4093.
Format vlan tagging number
Mode Interface Config
no vlan tagging
This command configures the tagging behavior for a specific interface or range of interfaces
in a VLAN to disabled. If tagging is disabled, traffic is transmitted as untagged frames. The
number is a valid VLAN identification number in the range 1–4093.
Format no vlan tagging number
Mode Interface Config
vlan association subnet
This command associates a VLAN to a specific IP-subnet.
Format vlan association subnet ipaddr netmask vlanid
Mode VLAN Config
no vlan association subnet
This command removes association of a specific IP-subnet to a VLAN.
Format no vlan association subnet ipaddr netmask
Mode VLAN Config
vlan association mac
This command associates a MAC address to a VLAN.
Format vlan association mac macaddr vlanid
Mode VLAN database
Switching Commands 431

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no vlan association mac
This command removes the association of a MAC address to a VLAN.
Format no vlan association mac macaddr
Mode VLAN database
remote-span
This command identifies the VLAN as the RSPAN VLAN.
Default None
Format remote-span
Mode VLAN configuration
show vlan
This command displays information about the configured private VLANs, including primary
and secondary VLAN IDs, type (community, isolated, or primary) and the ports which belong
to a private VLAN.
Format show vlan {vlan-id | private-vlan [type]}
Mode Privileged EXEC
User EXEC
Term Definition
Primary Primary VLAN identifier. The range of the VLAN ID is 1 to 4093.
Secondary Secondary VLAN identifier.
Type Secondary VLAN type (community, isolated, or primary).
Ports Ports which are associated with a private VLAN.
VLAN ID The VLAN identifier (VID) associated with each VLAN. The range of the VLAN ID is 1 to 4093.
VLAN Name A string associated with this VLAN as a convenience. It can be up to 32 alphanumeric characters
long, including blanks. The default is blank. VLAN ID 1 always has a name of Default. This field is
optional.
VLAN Type Type of VLAN, which can be Default (VLAN ID = 1) or static (one that is configured and permanently
defined), or Dynamic. A dynamic VLAN can be created by GVRP registration or during the 802.1X
authentication process (DOT1X) if a RADIUS-assigned VLAN does not exist on the switch.
Interface unit/slot/port. It is possible to set the parameters for all ports by using the selectors on the top line.
Switching Commands 432

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Current The degree of participation of this port in this VLAN. The permissible values are:
• Include - This port is always a member of this VLAN. This is equivalent to registration fixed in
the IEEE 802.1Q standard.
• Exclude - This port is never a member of this VLAN. This is equivalent to registration forbidden
in the IEEE 802.1Q standard.
• Autodetect - To allow the port to be dynamically registered in this VLAN via GVRP. The port will
not participate in this VLAN unless a join request is received on this port. This is equivalent to
registration normal in the IEEE 802.1Q standard.
Configured The configured degree of participation of this port in this VLAN. The permissible values are:
• Include - This port is always a member of this VLAN. This is equivalent to registration fixed in
the IEEE 802.1Q standard.
• Exclude - This port is never a member of this VLAN. This is equivalent to registration forbidden
in the IEEE 802.1Q standard.
• Autodetect - To allow the port to be dynamically registered in this VLAN via GVRP. The port will
not participate in this VLAN unless a join request is received on this port. This is equivalent to
registration normal in the IEEE 802.1Q standard.
Tagging The tagging behavior for this port in this VLAN.
• Tagged - Transmit traffic for this VLAN as tagged frames.
• Untagged - Transmit traffic for this VLAN as untagged frames.
show vlan internal usage
This command displays information about the VLAN ID allocation on the switch.
Format show vlan internal usage
Mode Privileged EXEC
User EXEC
Term Definition
Base VLAN ID Identifies the base VLAN ID for Internal allocation of VLANs to the routing interface.
Allocation policy Identifies whether the system allocates VLAN IDs in ascending or descending order.
show vlan port
This command displays VLAN port information.
Format show vlan port {unit/slot/port | all}
Mode Privileged EXEC
User EXEC
Switching Commands 433

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Interface It is possible to set the parameters for all ports by using the selectors on the top line.
Port VLAN ID The VLAN ID that this port will assign to untagged frames or priority tagged frames received on this
port. The value must be for an existing VLAN. The factory default is 1.
Acceptable Frame The types of frames that may be received on this port. The options are 'VLAN only' and 'Admit All'.
Types When set to 'VLAN only', untagged frames or priority tagged frames received on this port are
discarded. When set to 'Admit All', untagged frames or priority tagged frames received on this port
are accepted and assigned the value of the Port VLAN ID for this port. With either option, VLAN
tagged frames are forwarded in accordance to the 802.1Q VLAN specification.
Ingress Filtering May be enabled or disabled. When enabled, the frame is discarded if this port is not a member of the
VLAN with which this frame is associated. In a tagged frame, the VLAN is identified by the VLAN ID
in the tag. In an untagged frame, the VLAN is the Port VLAN ID specified for the port that received
this frame. When disabled, all frames are forwarded in accordance with the 802.1Q VLAN bridge
specification. The factory default is disabled.
GVRP May be enabled or disabled.
Default Priority The 802.1p priority assigned to tagged packets arriving on the port.
show vlan association subnet
This command displays the VLAN associated with a specific configured IP-Address and net
mask. If no IP address and net mask are specified, the VLAN associations of all the
configured IP-subnets are displayed.
Format show vlan association subnet [ipaddr netmask]
Mode Privileged EXEC
Term Definition
IP Address The IP address assigned to each interface.
Net Mask The subnet mask.
VLAN ID There is a VLAN Identifier (VID) associated with each VLAN.
show vlan association mac
This command displays the VLAN associated with a specific configured MAC address. If no
MAC address is specified, the VLAN associations of all the configured MAC addresses are
displayed.
Format show vlan association mac [macaddr]
Mode Privileged EXEC
Switching Commands 434

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Mac Address A MAC address for which the switch has forwarding and or filtering information. The format is 6 or 8
two-digit hexadecimal numbers that are separated by colons, for example 01:23:45:67:89:AB. In an
IVL system the MAC address will be displayed as 8 bytes.
VLAN ID There is a VLAN Identifier (VID) associated with each VLAN.
Switch Port Commands
This section describes the commands used for switch port mode.
switchport mode
Use this command to configure the mode of a switch port as access, trunk, or general:
• Trunk mode. In trunk mode, the port becomes a member of all VLANs on the switch
unless specified in the allowed list in the switchport trunk allowed vlan
command. The PVID of the port is set to the native VLAN as specified in the
switchport trunk native vlan command. This means that trunk ports accept both
tagged and untagged packets. Untagged packets are processed on the native VLAN and
tagged packets are processed on the VLAN for which the ID is contained in the packet.
MAC learning is performed on both tagged and untagged packets. Tagged packets that
are received with a VLAN ID of which the port is not a member are discarded and MAC
learning is not performed.
The trunk ports always transmit packets untagged on a native VLAN.
• Access mode. In access mode, the port becomes a member of only one VLAN. The port
sends and receives untagged traffic. The port can also receive tagged traffic. Ingress
filtering is enabled on the port. This means that when the VLAN ID of a received packet is
not identical to the access VLAN ID, the packet is discarded.
• General mode. In general mode, you can perform custom configuration of the VLAN
membership, PVID, tagging, ingress filtering, and so on. The general mode is legacy
behavior of the switch port configuration and you use legacy CLI commands to configure
the port in general mode.
Default General mode
Format switchport mode {access | trunk | general}
Mode Interface Config
Switching Commands 435

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no switchport mode
This command resets the switch port mode to its default value.
Format no switchport mode
Mode Interface Config
switchport trunk allowed vlan
Use this command to configure the list of allowed VLANs that can receive and send traffic on
this interface in tagged format when in trunking mode. The default is all.
You can modify the VLAN list by using the add and remove options and replace the VLAN
list with another list by using the all or except options. If you use the all option, all VLANs
are added to the list of allowed VLANs. The except option provides an exclusion list.
Default all
Format switchport trunk allowed vlan {vlan-list | all | {add vlan-list} |
{remove vlan-list} | {except vlan-list}}
Mode Interface Config
Parameter Description
all Specifies all VLANs from 1 to 4093. This keyword is not allowed for commands that do not
permit all VLANs in the list to be set at the same time.
add Adds the defined list of VLANs to those currently set instead of replacing the list.
remove Removes the defined list of VLANs from those currently set instead of replacing the list.
Valid IDs are from 1 to 4093. Extended-range VLAN IDs of the form XY or X,Y,Z are valid in
this command
except Lists the VLANs that must be calculated by inverting the defined list of VLANs. (VLANs are
added except the ones specified.)
van-list Either a single VLAN number from 1 to 4093 or a continuous range of VLANs described by
two VLAN numbers, the lesser one first, separated by a hyphen.
no switchport trunk allowed vlan
This command resets the list of allowed VLANs on the trunk port to its default value.
Format no switchport trunk allowed vlan
Mode Interface Config
switchport trunk native vlan
Use this command to configure the trunk port native VLAN (PVID) parameter of the switch
port. Any ingress untagged packets on the port are tagged with the value of the native VLAN.
Switching Commands 436

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The native VLAN must be in the allowed VLAN list for tagging of received untagged packets.
Otherwise, untagged packets are discarded. Packets marked with the native VLAN are
transmitted untagged from the trunk port. The default ID is 1, the default VLAN.
Default 1 (default VLAN)
Format switchport trunk native vlan vlan-id
Mode Interface Config
no switchport trunk native vlan
Use this command to reset the trunk mode native VLAN of the switch port to its default value.
Format no switchport trunk native vlan
Mode Interface Config
switchport access vlan
Use this command to configure the VLAN on the access port. You can assign one VLAN only
to the access port. The access port is member of VLAN 1 by default. You can assign the
access port to a VLAN other than VLAN 1. If you remove the access VLAN on the switch, the
access port becomes a member of VLAN 1. If you configure the access port as a member of
a VLAN that does not exist, an error occurs and the configuration does not change.
Default 1 (default VLAN)
Format switchport access vlan vlan-id
Mode Interface Config
no switchport access vlan
This command resets the switch port access mode VLAN to its default value.
Format no switchport access vlan
Mode Interface Config
show interfaces switchport
Use this command to either display the switch port status for all interfaces, for a specific
interface, or for a specific mode (access, trunk, or general). If you select a mode but do not
specify the interface for the mode, the selected mode is displayed for all interfaces.
Format show interfaces switchport {[unit/slot/port] | {access | trunk |
general} [unit/slot/port]}
Mode Privileged EXEC
Switching Commands 437

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show interfaces switchport 1/0/1
Port: 1/0/1
VLAN Membership Mode: General
Access Mode VLAN: 1 (default)
General Mode PVID: 1 (default)
General Mode Ingress Filtering: Disabled
General Mode Acceptable Frame Type: Admit all
General Mode Dynamically Added VLANs:
General Mode Untagged VLANs: 1
General Mode Tagged VLANs:
General Mode Forbidden VLANs:
Trunking Mode Native VLAN: 1 (default)
Trunking Mode Native VLAN tagging: Disable
Trunking Mode VLANs Enabled: All
Protected Port: False
Command example:
(NETGEAR Switch) #show interfaces switchport access 1/0/1
I ntf PVID
--------- ----
1 /0/1 1
Command example:
(NETGEAR Switch) #show interfaces switchport trunk 1/0/6
I ntf P VID Allowed Vlans List
--------- ----- -------------------
1 /0/6 1 All
Command example:
(NETGEAR Switch) #show interfaces switchport general 1/0/5
I ntf P VID I ngress A cceptable U ntagged T agged Forbidden Dynamic
F iltering F rame Type V lans V lans V lans Vlans
- -------- ----- ---------- ----------- --------- --------- --------- ---------
1 /0/5 1 E nabled A dmit All 7 1 0-50,55 9 ,100-200 88,96
Switching Commands 438

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show interfaces switchport general
I ntf P VID I ngress A cceptable U ntagged T agged Forbidden Dynamic
F iltering F rame Type V lans V lans V lans Vlans
--------- ----- ---------- ----------- --------- --------- --------- ---------
1 /0/1 1 E nabled A dmit All 1 ,4-7 3 0-40,55 3 ,100-200 88,96
1 /0/2 1 D isabled A dmit All 1 3 0-40,55 n one none
Double VLAN Commands
This section describes the commands you use to configure double VLAN (DVLAN). Double
VLAN tagging is a way to pass VLAN traffic from one customer domain to another through a
Metro Core in a simple and cost effective manner. The additional tag on the traffic helps
differentiate between customers in the MAN while preserving the VLAN identification of the
individual customers when they enter their own IEEE 802.1Q domain.
dvlan-tunnel ethertype (Interface Config)
This command configures the ethertype for the specified interface. The two-byte hex
ethertype is used as the first 16 bits of the DVLAN tag. The ethertype can have the values of
802.1Q, vman, or custom. If the ethertype has an optional value of custom, then it is a
custom tunnel value, and ethertype must be set to a value in the range of 1 to 65535.
Default vman
Format dvlan-tunnel ethertype {802.1Q | vman | custom value}
Mode Global Config
Parameter Description
802.1Q Configure the ethertype as 0x8100.
custom Configure the value of the custom tag in the range from 1 to 65535.
vman Represents the commonly used value of 0x88A8.
no dvlan-tunnel ethertype (Interface Config)
This command removes the ethertype value for the interface.
Format no dvlan-tunnel ethertype
Mode Global Config
Switching Commands 439

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
dvlan-tunnel ethertype primary-tpid
Use this command to create a new TPID and associate it with the next available TPID
register. If no TPID registers are empty, the system returns an error. Specifying the optional
keyword primary–tpid forces the TPID value to be configured as the default TPID at index
0. The ethertype can have the values of 802.1Q, vman, or custom. If the ethertype has an
optional value of custom, then it is a custom tunnel value, and ethertype must be set to a
value in the range of 1 to 65535.
Format dvlan-tunnel ethertype {802.1Q | vman | custom value} [primary-tpid]
Mode Global Config
Parameter Description
802.1Q Configure the ethertype as 0x8100.
custom value Configure the value of the custom tag in the range from 1 to 65535.
vman Represents the commonly used value of 0x88A8.
primary-tpid [Optional] Forces the TPID value to be configured as the default TPID at index 0.
no dvlan-tunnel ethertype primary–tpid
Use the no form of the command to reset the TPID register to 0. (At initialization, all TPID
registers will be set to their default values.)
Format no dvlan-tunnel ethertype {802.1Q | vman | custom 1–65535} [primary-tpid]
Mode Global Config
mode dot1q-tunnel
This command is used to enable Double VLAN Tunneling on the specified interface.
Default Disabled
Format mode dot1q-tunnel
Mode Interface Config
no mode dot1q-tunnel
This command is used to disable Double VLAN Tunneling on the specified interface. By
default, Double VLAN Tunneling is disabled.
Format no mode dot1q-tunnel
Mode Interface Config
Switching Commands 440

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
mode dvlan-tunnel
Use this command to enable Double VLAN Tunneling on the specified interface.
Note: When you use the mode dvlan-tunnel command on an interface, it
becomes a service provider port. Ports that do not have double VLAN
tunneling enabled are customer ports.
Default Disabled
Format mode dvlan-tunnel
Mode Interface Config
no mode dvlan-tunnel
This command is used to disable Double VLAN Tunneling on the specified interface. By
default, Double VLAN Tunneling is disabled.
Format no mode dvlan-tunnel
Mode Interface Config
show dot1q-tunnel
Use this command without the optional parameters to display all interfaces enabled for
Double VLAN Tunneling. Use the optional parameters to display detailed information about
Double VLAN Tunneling for the specified interface or all interfaces.
Format show dot1q-tunnel [interface {unit/slot/port | all}]
Mode Privileged EXEC
User EXEC
Term Definition
Interface The interface.
Mode The administrative mode through which Double VLAN Tunneling can be enabled or disabled. The
default value for this field is disabled.
EtherType A 2-byte hex EtherType to be used as the first 16 bits of the DVLAN tunnel. There are three different
EtherType tags. The first is 802.1Q, which represents the commonly used value of 0x8100. The
second is vMAN, which represents the commonly used value of 0x88A8. If EtherType is not one of
these two values, then it is a custom tunnel value, representing any value in the range of 1 to 65535.
Switching Commands 441

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show dvlan-tunnel
Use this command without the optional parameters to display all interfaces enabled for
Double VLAN Tunneling. Use the optional parameters to display detailed information about
Double VLAN Tunneling for the specified interface or all interfaces.
Format show dvlan-tunnel [interface {unit/slot/port | all | lag lag-intf-num}]
Mode Privileged EXEC
User EXEC
Term Definition
Interface The interface.
LAG Instead of unit/slot/port, lag lag-intf-num can be used as an alternate way to specify the
LAG interface, in which lag-intf-num is the LAG port number.
Mode The administrative mode through which Double VLAN Tunneling can be enabled or disabled. The
default value for this field is disabled.
EtherType A 2-byte hex EtherType to be used as the first 16 bits of the DVLAN tunnel. There are three different
EtherType tags. The first is 802.1Q, which represents the commonly used value of 0x8100. The
second is vMAN, which represents the commonly used value of 0x88A8. If EtherType is not one of
these two values, then it is a custom tunnel value, representing any value in the range of 1 to 65535.
Command example:
(NETGEAR Switch) #show dvlan-tunnel
TPIDs Configured............................... 0x88a8
Default TPID................................... 0x88a8
Interfaces Enabled for DVLAN Tunneling......... None
(NETGEAR Switch) #
(NETGEAR Switch) #show dvlan-tunnel interface 1/0/1
Interface Mode EtherType
--------- ------- ------------
1/0/1 Disable 0x88a8
Switching Commands 442

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Private VLAN Commands
This section describes the commands you use for private VLANs. Private VLANs provides
Layer 2 isolation between ports that share the same broadcast domain. In other words, it
allows a VLAN broadcast domain to be partitioned into smaller point-to-multipoint
subdomains. The ports participating in a private VLAN can be located anywhere in the
Layer 2 network.
switchport private-vlan
This command defines a private-VLAN association for an isolated or community port or a
mapping for a promiscuous port.
Format switchport private-vlan {host-association primary-vlan-id secondary-vlan-id
| mapping primary-vlan-id {add | remove} secondary-vlan-list}
Mode Interface Config
Parameter Description
host-association Defines the VLAN association for community or host ports.
mapping Defines the private VLAN mapping for promiscuous ports.
primary-vlan-id Primary VLAN ID of a private VLAN.
secondary-vlan-id Secondary (isolated or community) VLAN ID of a private VLAN.
add Associates the secondary VLAN with the primary one.
remove Deletes the secondary VLANs from the primary VLAN association.
secondary-vlan-list A list of secondary VLANs to be mapped to a primary VLAN.
no switchport private-vlan
This command removes the private-VLAN association or mapping from the port.
Format no switchport private-vlan {host-association | mapping}
Mode Interface Config
switchport mode private-vlan
This command configures a port as a promiscuous or host private VLAN port. Note that the
properties of each mode can be configured even when the switch is not in that mode.
However, they will only be applicable once the switch is in that particular mode.
Format switchport mode private-vlan {host | promiscuous}
Mode Interface Config
Switching Commands 443

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
host Configures an interface as a private VLAN host port. It can be either isolated or community port
depending on the secondary VLAN it is associated with.
promiscuous Configures an interface as a private VLAN promiscuous port. The promiscuous ports are members
of the primary VLAN.
no switchport mode private-vlan
This command removes the private-VLAN association or mapping from the port.
Format no switchport mode private-vlan
Mode Interface Config
private-vlan
This command configures the private VLANs and configures the association between the
primary private VLAN and secondary VLANs.
Format private-vlan {association [add | remove] secondary-vlan-list | community |
isolated | primary}
Mode VLAN Config
Parameter Description
association Associates the primary and secondary VLAN.
secondary-vlan-list A list of secondary VLANs to be mapped to a primary VLAN.
community Designates a VLAN as a community VLAN.
isolated Designates a VLAN as the isolated VLAN.
primary Designates a VLAN as the primary VLAN.
no private-vlan
This command restores normal VLAN configuration.
Format no private-vlan [association]
Mode VLAN Config
Switching Commands 444

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Voice VLAN Commands
This section describes the commands you use for Voice VLAN. Voice VLAN enables switch
ports to carry voice traffic with defined priority so as to enable separation of voice and data
traffic coming onto the port. The benefits of using Voice VLAN is to ensure that the sound
quality of an IP phone could be safeguarded from deteriorating when the data traffic on the
port is high.
Also the inherent isolation provided by VLANs ensures that inter-VLAN traffic is under
management control and that network- attached clients cannot initiate a direct attack on
voice components. QoS-based on IEEE 802.1P class of service (CoS) uses classification
and scheduling to sent network traffic from the switch in a predictable manner. The system
uses the source MAC of the traffic traveling through the port to identify the IP phone data
flow.
The switch can be configured to support voice VLAN on a port connecting to the VoIP phone.
When a VLAN is associated with the voice VLAN port, then the VLAN id info is passed onto
the VoIP phone using the LLDP-MED mechanism. The voice data coming from the VoIP
phone is tagged with the exchanged VLAN ID; thus, regular data arriving on the switch is
given the default PVID of the port, and the voice traffic is received on a predefined VLAN.
The two types of traffic are therefore segregated so that better service can be provided to the
voice traffic.
When a dot1p priority is associated with the voice VLAN port instead of VLAN ID, the priority
information is passed onto the VoIP phone using the LLDP-MED mechanism. Thus, the voice
data coming from the VoIP phone is tagged with VLAN 0 and with the exchanged priority.
Regular data arriving on the switch is given the default priority of the port (default 0), and the
voice traffic is received with higher priority, thus segregating both the traffic to provide better
service to the voice traffic.
The switch can be configured to override the data traffic CoS. This feature enables overriding
the 802.1P priority of the data traffic packets arriving at the port enabled for voice VLAN.
Thus, a rogue client that is also connected to the voice VLAN port does not deteriorate the
voice traffic.
When a VLAN ID is configured on the voice VLAN port, the VLAN ID information is passed
onto the VoIP phone using the LLDP-MED mechanism. The voice data coming from the VoIP
phone is tagged with the exchanged VLAN ID; thus, regular data arriving on the switch is
given the default PVID of the port, and the voice traffic is received on a predefined VLAN.
The two types of traffic are segregated so that better service can be provided to the voice
traffic.
Note: The IP phone must support LLDP-MED to accept the VLAN ID and
CoS information from the switch.
Switching Commands 445

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
voice vlan (Global Config)
Use this command to enable the Voice VLAN capability on the switch.
Default Disabled
Format voice vlan
Mode Global Config
no voice vlan (Global Config)
Use this command to disable the Voice VLAN capability on the switch.
Format no voice vlan
Mode Global Config
voice vlan (Interface Config)
Use this command to enable the Voice VLAN capability on the interface or range of
interfaces.
Default Disabled
Format voice vlan {vlan-id | dot1p priority | none | untagged}
Mode Interface Config
You can configure Voice VLAN in one of four different ways.
Parameter Description
vlan-id Configure the IP phone to forward all voice traffic through the specified VLAN. Valid VLAN ID’s are
from 1 to 4093 (the max supported by the platform).
dot1p Configure the IP phone to use 802.1p priority tagging for voice traffic and to use the default native
VLAN (VLAN 0) to carry all traffic. Valid priority range is 0 to 7.
none Allow the IP phone to use its own configuration to send untagged voice traffic.
untagged Configure the phone to send untagged voice traffic.
no voice vlan (Interface Config)
Use this command to disable the Voice VLAN capability on the interface.
Format no voice vlan
Mode Interface Config
Switching Commands 446

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
voice vlan auth
This command lets the switch accept or reject voice traffic when the port is in an
unauthorized state. By default, the switch rejects voice traffic when the port is in an
unauthorized state.
Default disable
Format voice vlan auth [disable | enable]
Mode Interface Config
voice vlan data priority
Use this command to either trust or untrust the data traffic arriving on the Voice VLAN
interface or range of interfaces being configured.
Default trust
Format voice vlan data priority {untrust | trust}
Mode Interface Config
show voice vlan
Use this command to display information about the voice VLAN.
Format show voice vlan [interface {unit/slot/port | all}]
Mode Privileged EXEC
When the interface parameter is not specified, only the global mode of the Voice VLAN is
displayed.
Term Definition
Administrative Mode The Global Voice VLAN mode.
When the interface parameter is specified..
Term Definition
Voice VLAN Mode The admin mode of the Voice VLAN on the interface.
Voice VLAN ID The Voice VLAN ID
Voice VLAN Priority The do1p priority for the Voice VLAN on the port.
Voice VLAN Untagged The tagging option for the Voice VLAN traffic.
Voice VLAN CoS Override The Override option for the voice traffic arriving on the port.
Voice VLAN Status The operational status of Voice VLAN on the port.
Switching Commands 447

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Precision Time Protocol Commands
This section describes the commands you use to configure the Precision Time Protocol
(PTP) end-to-end (E2E) transparent clock.
ptp clock e2e-transparent
This command enables the PTP E2E transparent clock at system level (that is, globaly) or for
an interface.
Default Enabled at system level and for all interfaces
Format ptp clock e2e-transparent
Mode Global Config
Interface Config
In Global Config mode, the command applies the PTP transparent clock configuration to all
physical ports and LAG on the switch. In Interface Config mode, the command provides a
next-level control so you can disable this feature selectively for an individual physical port or
LAG.
You can configure the PTP transparent clock for physical ports and LAGs, but not for a
VLAN. When you configure the PTP transparent clock on a LAG, the configuration is applied
to all member ports.
no ptp clock e2e-transparent
This command disables the PTP E2E transparent clock at system level or for an interface.
Format no ptp clock e2e-transparent
Mode Global Config
Interface Config
show ptp clock e2e-transparent
Use this command to display the operational and configuration status of the PTP E2E
transparent clock, both at system level and at interface level.
Format show ptp clock e2e-transparent
Mode Privileged Exec
Term Definition
Interface The interface on which the feature is configured.
Switching Commands 448

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Configured Mode The configuration status of the PTP E2E transparent clock on the interface
Operational Mode The operational status of the PTP E2E transparent clock on the interface.
Command example:
(NETGEAR Switch) #show ptp clock e2e-transparent
PTP TC mode.................................... Enabled
Interface Configured Mode Operational Mode
--------- --------------- ----------------
1/1/1 Enabled Disabled
1/1/2 Enabled Disabled
1/1/3 Enabled Disabled
1/1/4 Enabled Disabled
1/1/5 Enabled Disabled
1/1/6 Enabled Disabled
1/1/7 Enabled Disabled
1/1/8 Enabled Disabled
Provisioning (IEEE 802.1p) Commands
This section describes the commands you use to configure provisioning (IEEE 802.1p,)
which allows you to prioritize ports.
vlan port priority all
This command configures the port priority assigned for untagged packets for all ports
presently plugged into the device. The range for the priority is 0-7. Any subsequent per port
configuration will override this configuration setting.
Format vlan port priority all priority
Mode Global Config
vlan priority
This command configures the default 802.1p port priority assigned for untagged packets for a
specific interface. The range for the priority is 0–7.
Default 0
Format vlan priority priority
Mode Interface Config
Switching Commands 449

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Asymmetric Flow Control
When in asymmetric flow control mode, the switch responds to PAUSE frames received from
a peer by stopping packet transmission, but the switch does not initiate MAC control PAUSE
frames.
When you configure the switch in asymmetric flow control (or no flow control mode), the
device is placed in egress drop mode. Egress drop mode maximizes the throughput of the
system at the expense of packet loss in a heavily congested system, and this mode avoids
head-of-line blocking.
flowcontrol
Use this command to enable the symmetric or asymmetric flow control on the switch.
Asymmetric flow control means you can enable Rx Pause only but not Tx Pause.
Default Flow control is disabled.
Format flowcontrol {symmetric | asymmetric}
Mode Interface Config
no flowcontrol
This command disables flow control.
Format no flowcontrol
Mode Global Config
show flowcontrol
Use this command to display the IEEE 802.3 Annex 31B flow control settings and status for a
specific interface or all interfaces. The command also displays 802.3 Tx and Rx pause
counts. Priority Flow Control frames counts are not displayed. If the port is enabled for priority
flow control, operational flow control status is displayed as Inactive. Operational flow control
status for stacking ports is always displayed as N/A.
Format show flowcontrol [interface unit/slot/port]
Mode Privileged Exec
Switching Commands 450

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show flowcontrol
Admin Flow Control: Symmetric
Port Flow Control RxPause TxPause
Oper
------ ------------ -------- ---------
0/1 Active 310 611
0/2 Inactive 0 0
Command example:
(NETGEAR Switch) #show flowcontrol interface 0/1
Admin Flow Control: Symmetric
Port Flow Control RxPause TxPause
Oper
--------- ------- -------- -------
0/1 Active 310 611
Protected Ports Commands
This section describes commands you use to configure and view protected ports on a switch.
Protected ports do not forward traffic to each other, even if they are on the same VLAN.
However, protected ports can forward traffic to all unprotected ports in their group.
Unprotected ports can forward traffic to both protected and unprotected ports. Ports are
unprotected by default.
If an interface is configured as a protected port, and you add that interface to a Port Channel
or Link Aggregation Group (LAG), the protected port status becomes operationally disabled
on the interface, and the interface follows the configuration of the LAG port. However, the
protected port configuration for the interface remains unchanged. Once the interface is no
longer a member of a LAG, the current configuration for that interface automatically becomes
effective.
switchport protected (Global Config)
Use this command to create a protected port group. The groupid parameter identifies the
set of protected ports. Use the name parameter to assign a name to the protected port group.
The name can be up to 32 alphanumeric characters long, including blanks. The default is
blank.
Switching Commands 451

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: Port protection occurs within a single switch. Protected port
configuration does not affect traffic between ports on two different
switches. No traffic forwarding is possible between two protected
ports.
Default unprotected
Format switchport protected groupid name name
Mode Global Config
no switchport protected (Global Config)
Use this command to remove a protected port group. The groupid parameter identifies the
set of protected ports. The name parameter specifies the name to remove from the group.
Format no switchport protected groupid name name
Mode Global Config
switchport protected (Interface Config)
Use this command to add an interface to a protected port group. The groupid parameter
identifies the set of protected ports to which this interface is assigned. You can only configure
an interface as protected in one group.
Note: Port protection occurs within a single switch. Protected port
configuration does not affect traffic between ports on two different
switches. No traffic forwarding is possible between two protected
ports.
Default unprotected
Format switchport protected groupid
Mode Interface Config
no switchport protected (Interface Config)
Use this command to configure a port as unprotected. The groupid parameter identifies the
set of protected ports to which this interface is assigned.
Format no switchport protected groupid
Mode Interface Config
Switching Commands 452

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show switchport protected
This command displays the status of all the interfaces, including protected and unprotected
interfaces.
Format show switchport protected groupid
Mode Privileged EXEC
User EXEC
Term Definition
Group ID The number that identifies the protected port group.
Name An optional name of the protected port group. The name can be up to 32 alphanumeric characters
long, including blanks. The default is blank.
List of Physical List of ports, which are configured as protected for the group identified with groupid. If no port is
Ports configured as protected for this group, this field is blank.
show interfaces switchport (for a group ID)
This command displays the status of the interface (protected or unprotected) under the
groupid.
Format show interfaces switchport unit/slot/port groupid
Mode Privileged EXEC
User EXEC
Term Definition
Name A string associated with this group as a convenience. It can be up to 32 alphanumeric characters
long, including blanks. The default is blank. This field is optional.
Protected Indicates whether the interface is protected or not. It shows TRUE or FALSE. If the group is a
multiple groups then it shows TRUE in Group groupid.
Private Group Commands
This section describes commands that are used to configure a private group and view the
configuration information of a private group.
You can use a private group to create a group of ports that either can or cannot share traffic
with each other in the same VLAN group. The main purpose of a private group is to isolate a
group of users from another group of users without using a VLAN.
Switching Commands 453

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
switchport private-group
This command assigns one port or a range of ports to a private group. You specify the private
group by either its name or its identifier.
The ingress traffic from a port in a private group can be forwarded to other ports either in the
same private group or outside the private group but in the same VLAN.
By default, a port does not belong to any private group. A port cannot be in more than one
private group. To change the membership of a port in a private group, first remove the port
from the private group.
Format switchport private-group [privategroup-name | privategroup-id]
Mode Interface Config
no switchport private-group
This command removes a port from to a private group.
Format no switchport private-group [privategroup-name | privategroup-id]
Mode Interface Config
private-group name
This command creates a private group with a name or an identifier. The name string can be
up to 24 bytes of non-blank characters. A total number of 192 of private groups is supported.
Therefore, the group identifier can be from 1 to 192.
The private-group-id parameter is optional. If you do not specify a group identifier, the
identifier is assigned automatically.
The optional mode for the group can be either isolated or community. If the private group is in
isolated mode, the member port in the group cannot forward its egress traffic to any other
members in the same group. By default, the mode for the private group is community mode,
allowing each member port to forward traffic to other members in the same group, but not to
members in other groups.
Format private-group name privategroup-name [private-group-id] [mode {community |
isolated}]
Mode Global Config
no private-group name
This command removes a private group.
Format no private-group name privategroup-name
Mode Global Config
Switching Commands 454

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show private-group
This command displays information about a private group. If you do not specify a group
name, group identifier, or port, the command displays information about all private groups.
Format show private-group [private-group-name | private-group-id | port
unit/slot/port]
Mode Privileged EXEC
Term Description
Interface A valid slot and port number separated by forward slashes.
Port VLANID The VLAN ID that is associated with the port.
Private Group ID The identifier of the private group (from 1 to 192).
Private Group The name of the private group. The name string can be up to 24 bytes of non-blank characters.
Name
Private Group The mode of the private group. The mode can be either isolated or community.
Mode
GARP Commands
This section describes the commands you use to configure Generic Attribute Registration
Protocol (GARP) and view GARP status. The commands in this section affect both GARP
VLAN Registration Protocol (GVRP) and GARP Multicast Registration Protocol (GMRP).
GARP is a protocol that allows client stations to register with the switch for membership in
VLANS (by using GVMP) or multicast groups (by using GVMP).
set garp timer join
This command sets the GVRP join time per GARP for one interface, a range of interfaces, or
all interfaces. Join time is the interval between the transmission of GARP Protocol Data Units
(PDUs) registering (or reregistering) membership for a VLAN or multicast group. This
command has an effect only when GVRP is enabled. The time is from 10 to 100
centiseconds. The value 20 centiseconds is 0.2 seconds.
Default 20
Format set garp timer join centiseconds
Mode Interface Config
Global Config
Switching Commands 455

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no set garp timer join
This command sets the GVRP join time to the default and only has an effect when GVRP is
enabled.
Format no set garp timer join
Mode Interface Config
Global Config
set garp timer leave
This command sets the GVRP leave time for one interface, a range of interfaces, or all
interfaces or all ports and only has an effect when GVRP is enabled. Leave time is the time to
wait after receiving an unregister request for a VLAN or a multicast group before deleting the
VLAN entry. This can be considered a buffer time for another station to assert registration for
the same attribute in order to maintain uninterrupted service. The leave time is 20 to 600
centiseconds. The value 60 centiseconds is 0.6 seconds. The leave time must be greater
than or equal to three times the join time.
Default 60
Format set garp timer leave centiseconds
Mode Interface Config
Global Config
no set garp timer leave
This command sets the GVRP leave time on all ports or a single port to the default and only
has an effect when GVRP is enabled.
Format no set garp timer leave
Mode Interface Config
Global Config
set garp timer leaveall
This command sets how frequently Leave All PDUs are generated. A Leave All PDU
indicates that all registrations will be unregistered. Participants would need to rejoin in order
to maintain registration. The value applies per port and per GARP participation. The time may
range from 200 to 6000 centiseconds. The value 1000 centiseconds is 10 seconds. You can
use this command on all ports (Global Config mode), or on a single port or a range of ports
(Interface Config mode) and it only has an effect only when GVRP is enabled. The leave all
time must be greater than the leave time.
Switching Commands 456

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default 1000
Format set garp timer leaveall centiseconds
Mode Interface Config
Global Config
no set garp timer leaveall
This command sets how frequently Leave All PDUs are generated the default and only has
an effect when GVRP is enabled.
Format no set garp timer leaveall
Mode Interface Config
Global Config
show garp
This command displays GARP information.
Format show garp
Mode Privileged EXEC
User EXEC
Term Definition
GMRP Admin The administrative mode of GARP Multicast Registration Protocol (GMRP) for the system.
Mode
GVRP Admin Mode The administrative mode of GARP VLAN Registration Protocol (GVRP) for the system.
GVRP Commands
This section describes the commands you use to configure and view GARP VLAN
Registration Protocol (GVRP) information. GVRP-enabled switches exchange VLAN
configuration information, which allows GVRP to provide dynamic VLAN creation on trunk
ports and automatic VLAN pruning.
Note: If GVRP is disabled, the system does not forward GVRP messages.
Switching Commands 457

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
set gvrp adminmode
This command enables GVRP on the system.
Default Disabled
Format set gvrp adminmode
Mode Privileged EXEC
no set gvrp adminmode
This command disables GVRP.
Format no set gvrp adminmode
Mode Privileged EXEC
set gvrp interfacemode
This command enables GVRP on a single port (Interface Config mode), a range of ports
(Interface Range mode), or all ports (Global Config mode).
Default Disabled
Format set gvrp interfacemode
Mode Interface Config
Interface Range
Global Config
no set gvrp interfacemode
This command disables GVRP on a single port (Interface Config mode) or all ports (Global
Config mode). If GVRP is disabled, Join Time, Leave Time and Leave All Time have no
effect.
Format no set gvrp interfacemode
Mode Interface Config
Global Config
show gvrp configuration
This command displays Generic Attributes Registration Protocol (GARP) information for one
or all interfaces.
Format show gvrp configuration {unit/slot/port | all}
Mode Privileged EXEC
User EXEC
Switching Commands 458

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Interface unit/slot/port
Join Timer The interval between the transmission of GARP PDUs registering (or reregistering) membership for
an attribute. Current attributes are a VLAN or multicast group. There is an instance of this timer on a
per-Port, per-GARP participant basis. Permissible values are 10 to 100 centiseconds (0.1 to 1.0
seconds). The factory default is 20 centiseconds (0.2 seconds). The finest granularity of
specification is one centisecond (0.01 seconds).
Leave Timer The period of time to wait after receiving an unregister request for an attribute before deleting the
attribute. Current attributes are a VLAN or multicast group. This may be considered a buffer time for
another station to assert registration for the same attribute in order to maintain uninterrupted service.
There is an instance of this timer on a per-Port, per-GARP participant basis. Permissible values are
20 to 600 centiseconds (0.2 to 6.0 seconds). The factory default is 60 centiseconds (0.6 seconds).
LeaveAll Timer This Leave All Time controls how frequently LeaveAll PDUs are generated. A LeaveAll PDU
indicates that all registrations will shortly be deregistered. Participants will need to rejoin in order to
maintain registration. There is an instance of this timer on a per-Port, per-GARP participant basis.
The Leave All Period Timer is set to a random value in the range of LeaveAllTime to
1.5*LeaveAllTime. Permissible values are 200 to 6000 centiseconds (2 to 60 seconds). The factory
default is 1000 centiseconds (10 seconds).
Port GMRP Mode The GMRP administrative mode for the port, which is enabled or disabled (default). If this parameter
is disabled, Join Time, Leave Time and Leave All Time have no effect.
GMRP Commands
This section describes the commands you use to configure and view GARP Multicast
Registration Protocol (GMRP) information. Like IGMP snooping, GMRP helps control the
flooding of multicast packets.GMRP-enabled switches dynamically register and de-register
group membership information with the MAC networking devices attached to the same
segment. GMRP also allows group membership information to propagate across all
networking devices in the bridged LAN that support Extended Filtering Services.
Note: If GMRP is disabled, the system does not forward GMRP messages.
set gmrp adminmode
This command enables GARP Multicast Registration Protocol (GMRP) on the system.
Default Disabled
Format set gmrp adminmode
Mode Privileged EXEC
Switching Commands 459

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no set gmrp adminmode
This command disables GARP Multicast Registration Protocol (GMRP) on the system.
Format no set gmrp adminmode
Mode Privileged EXEC
set gmrp interfacemode
This command enables GARP Multicast Registration Protocol on a single interface (Interface
Config mode), a range of interfaces, or all interfaces (Global Config mode). If an interface
which has GARP enabled is enabled for routing or is enlisted as a member of a port-channel
(LAG), GARP functionality is disabled on that interface. GARP functionality is subsequently
re-enabled if routing is disabled and port-channel (LAG) membership is removed from an
interface that has GARP enabled.
Default Disabled
Format set gmrp interfacemode
Mode Interface Config
Global Config
no set gmrp interfacemode
This command disables GARP Multicast Registration Protocol on a single interface or all
interfaces. If an interface which has GARP enabled is enabled for routing or is enlisted as a
member of a port-channel (LAG), GARP functionality is disabled. GARP functionality is
subsequently re-enabled if routing is disabled and port-channel (LAG) membership is
removed from an interface that has GARP enabled.
Format no set gmrp interfacemode
Mode Interface Config
Global Config
show gmrp configuration
This command displays Generic Attributes Registration Protocol (GARP) information for one
or all interfaces.
Format show gmrp configuration {unit/slot/port | all}
Mode Privileged EXEC
User EXEC
Switching Commands 460

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Interface The unit/slot/port of the interface that this row in the table describes.
Join Timer The interval between the transmission of GARP PDUs registering (or reregistering) membership for
an attribute. Current attributes are a VLAN or multicast group. There is an instance of this timer on a
per-port, per-GARP participant basis. Permissible values are 10 to 100 centiseconds (0.1 to 1.0
seconds). The factory default is 20 centiseconds (0.2 seconds). The finest granularity of
specification is 1 centisecond (0.01 seconds).
Leave Timer The period of time to wait after receiving an unregister request for an attribute before deleting the
attribute. Current attributes are a VLAN or multicast group. This may be considered a buffer time for
another station to assert registration for the same attribute in order to maintain uninterrupted service.
There is an instance of this timer on a per-Port, per-GARP participant basis. Permissible values are
20 to 600 centiseconds (0.2 to 6.0 seconds). The factory default is 60 centiseconds (0.6 seconds).
LeaveAll Timer This Leave All Time controls how frequently LeaveAll PDUs are generated. A LeaveAll PDU
indicates that all registrations will shortly be deregistered. Participants will need to rejoin in order to
maintain registration. There is an instance of this timer on a per-Port, per-GARP participant basis.
The Leave All Period Timer is set to a random value in the range of LeaveAllTime to
1.5*LeaveAllTime. Permissible values are 200 to 6000 centiseconds (2 to 60 seconds). The factory
default is 1000 centiseconds (10 seconds).
Port GMRP Mode The GMRP administrative mode for the port. It may be enabled or disabled. If this parameter is
disabled, Join Time, Leave Time and Leave All Time have no effect.
show mac-address-table gmrp
This command displays the GMRP entries in the Multicast Forwarding Database (MFDB)
table.
Format show mac-address-table gmrp
Mode Privileged EXEC
Term Definition
VLAN ID The VLAN in which the MAC Address is learned.
MAC Address A unicast MAC address for which the switch has forwarding and or filtering information. The format is
6 two-digit hexadecimal numbers that are separated by colons, for example 01:23:45:67:89:AB.
Type The type of the entry. Static entries are those that are configured by the end user. Dynamic entries
are added to the table as a result of a learning process or protocol.
Description The text description of this multicast table entry.
Interfaces The list of interfaces that are designated for forwarding (Fwd:) and filtering (Flt:).
Switching Commands 461

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Port-Based Network Access Control
Commands
This section describes the commands you use to configure port-based network access
control (IEEE 802.1X). Port-based network access control allows you to permit access to
network services only to and devices that are authorized and authenticated.
aaa authentication dot1x default
Use this command to configure the authentication methods for port-based access to the
switch. The additional methods of authentication are used only if the previous method returns
an error, not if there is an authentication failure.
The possible methods are as follows:
• ias. Uses the internal authentication server users database for authentication.
• local. Uses the local user name database for authentication.
• none. Uses no authentication.
• radius. Uses the list of all RADIUS servers for authentication.
You can configure one method at the time.
Format aaa authentication dot1x default {ias | local | none | radius}
Mode Global Config
Command example:
(NETGEAR Switch) #
(NETGEAR Switch) #configure
(NETGEAR Switch) (Config)#aaa authentication dot1x default ias
(NETGEAR Switch) (Config)#aaa authentication dot1x default local
clear dot1x statistics
This command resets the 802.1X statistics for the specified port or for all ports.
Format clear dot1x statistics {unit/slot/port | all}
Mode Privileged EXEC
Switching Commands 462

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
clear dot1x authentication-history
This command clears the authentication history table captured during successful and
unsuccessful authentication on all interface or the specified interface.
Format clear dot1x authentication-history [unit/slot/port]
Mode Privileged EXEC
clear radius statistics
This command is used to clear all RADIUS statistics.
Format clear radius statistics
Mode Privileged EXEC
dot1x eapolflood
Use this command to enable EAPOL flood support on the switch.
Default Disabled
Format dot1x eapolflood
Mode Global Config
no dot1x eapolflood
This command disables EAPOL flooding on the switch.
Format no dot1x eapolflood
Mode Global Config
dot1x dynamic-vlan enable
Use this command to enable the switch to create VLANs dynamically when a
RADIUS-assigned VLAN does not exist in the switch.
Default Disabled
Format dot1x dynamic-vlan enable
Mode Global Config
Switching Commands 463

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dot1x dynamic-vlan enable
Use this command to prevent the switch from creating VLANs when a RADIUS-assigned
VLAN does not exist in the switch.
Format no dot1x dynamic-vlan enable
Mode Global Config
dot1x guest-vlan
This command configures VLAN as guest vlan on an interface or a range of interfaces. The
command specifies an active VLAN as an IEEE 802.1X guest VLAN. The range is 1 to the
maximum VLAN ID supported by the platform.
Default Disabled
Format dot1x guest-vlan vlan-id
Mode Interface Config
no dot1x guest-vlan
This command disables Guest VLAN on the interface.
Default Disabled
Format no dot1x guest-vlan
Mode Interface Config
dot1x initialize
This command begins the initialization sequence on the specified port. This command is only
valid if the control mode for the specified port is auto or mac-based. If the control mode is not
auto or mac-based, an error is returned.
Format dot1x initialize unit/slot/port
Mode Privileged EXEC
dot1x max-req
This command sets the maximum number of times the authenticator state machine on an
interface or range of interfaces will transmit an EAPOL EAP Request/Identity frame before
timing out the supplicant. The count parameter must be in the range 1–10.
Default 2
Switching Commands 464

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format dot1x max-req count
Mode Interface Config
no dot1x max-req
This command sets the maximum number of times the authenticator state machine on this
port will transmit an EAPOL EAP Request/Identity frame before timing out the supplicant.
Format no dot1x max-req
Mode Interface Config
dot1x max-users
Use this command to set the maximum number of clients supported on an interface or range
of interfaces when MAC-based dot1x authentication is enabled on the port. The maximum
users supported per port is dependent on the product. The count parameter must be in the
range 1–48.
Default 48
Format dot1x max-users count
Mode Interface Config
no dot1x max-users
This command resets the maximum number of clients allowed per port to its default value.
Format no dot1x max-users
Mode Interface Config
dot1x port-control
This command sets the authentication mode to use on the specified interface or range of
interfaces. Use the force-unauthorized parameter to specify that the authenticator PAE
unconditionally sets the controlled port to unauthorized. Use the force-authorized
parameter to specify that the authenticator PAE unconditionally sets the controlled port to
authorized. Use the auto parameter to specify that the authenticator PAE sets the controlled
port mode to reflect the outcome of the authentication exchanges between the supplicant,
authenticator and the authentication server. If the mac-based parameter is specified, then
MAC-based dot1x authentication is enabled on the port.
Default auto
Format dot1x port-control {force-unauthorized | force-authorized | auto | mac-based}
Mode Interface Config
Switching Commands 465

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dot1x port-control
This command sets the 802.1X port control mode on the specified port to the default value.
Format no dot1x port-control
Mode Interface Config
dot1x port-control all
This command sets the authentication mode to use on all ports. Select the
force-unauthorized parameter to specify that the authenticator PAE unconditionally sets
the controlled port to unauthorized. Select the force-authorized parameter to specify
that the authenticator PAE unconditionally sets the controlled port to authorized. Select the
auto parameter to specify that the authenticator PAE sets the controlled port mode to reflect
the outcome of the authentication exchanges between the supplicant, authenticator and the
authentication server. If the mac-based parameter is specified, then MAC-based dot1x
authentication is enabled on the port.
Default auto
Format dot1x port-control all {force-unauthorized | force-authorized | auto |
mac-based}
Mode Global Config
no dot1x port-control all
This command sets the authentication mode on all ports to the default value.
Format no dot1x port-control all
Mode Global Config
dot1x mac-auth-bypass
If the 802.1X mode on the interface is mac-based, you can optionally use this command to
enable MAC Authentication Bypass (MAB) on an interface. MAB is a supplemental
authentication mechanism that allows 802.1X unaware clients – such as printers, fax
machines, and some IP phones—to authenticate to the network using the client MAC
address as an identifier.
Default Disabled
Format dot1x mac-auth-bypass
Mode Interface Config
Switching Commands 466

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dot1x mac-auth-bypass
This command sets the MAB mode on the ports to the default value.
Format no dot1x mac-auth-bypass
Mode Interface Config
dot1x re-authenticate
This command begins the reauthentication sequence on the specified port. This command is
only valid if the control mode for the specified port is auto or mac-based. If the control mode
is not auto or mac-based, an error is returned.
Format dot1x re-authenticate unit/slot/port
Mode Privileged EXEC
dot1x re-authentication
This command enables reauthentication of the supplicant for the specified interface or range
of interfaces.
Default Disabled
Format dot1x re-authentication
Mode Interface Config
no dot1x re-authentication
This command disables reauthentication of the supplicant for the specified port.
Format no dot1x re-authentication
Mode Interface Config
dot1x system-auth-control
Use this command to enable the dot1x authentication support on the switch. While disabled,
the dot1x configuration is retained and can be changed, but is not activated.
Default Disabled
Format dot1x system-auth-control
Mode Global Config
Switching Commands 467

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dot1x system-auth-control
This command is used to disable the dot1x authentication support on the switch.
Format no dot1x system-auth-control
Mode Global Config
dot1x system-auth-control monitor
Use this command to enable the 802.1X monitor mode on the switch. The purpose of Monitor
mode is to help troubleshoot port-based authentication configuration issues without
disrupting network access for hosts connected to the switch. In Monitor mode, a host is
granted network access to an 802.1X-enabled port even if it fails the authentication process.
The results of the process are logged for diagnostic purposes.
Default Disabled
Format dot1x system-auth-control monitor
Mode Global Config
no dot1x system-auth-control monitor
This command disables the 802.1X Monitor mode on the switch.
Format no dot1x system-auth-control monitor
Mode Global Config
dot1x timeout
This command sets the value, in seconds, of the timer used by the authenticator state
machine on an interface or range of interfaces. Depending on the token used and the value
(in seconds) passed, various timeout configurable parameters are set.
The following tokens are supported:
Tokens Definition
guest-vlan-period The time, in seconds, for which the authenticator waits to see if any EAPOL packets are received on
a port before authorizing the port and placing the port in the guest vlan (if configured). The guest
vlan timer is only relevant when guest vlan has been configured on that specific port.
reauth-period The value, in seconds, of the timer used by the authenticator state machine on this port to determine
when reauthentication of the supplicant takes place. The reauth-period must be a value in the range
1 - 65535.
quiet-period The value, in seconds, of the timer used by the authenticator state machine on this port to define
periods of time in which it will not attempt to acquire a supplicant. The quiet-period must be a value
in the range 0 - 65535.
Switching Commands 468

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Tokens Definition
tx-period The value, in seconds, of the timer used by the authenticator state machine on this port to determine
when to send an EAPOL EAP Request/Identity frame to the supplicant. The quiet-period must be a
value in the range 1 - 65535.
supp-timeout The value, in seconds, of the timer used by the authenticator state machine on this port to timeout
the supplicant. The supp-timeout must be a value in the range 1 - 65535.
server-timeout The value, in seconds, of the timer used by the authenticator state machine on this port to timeout
the authentication server. The supp-timeout must be a value in the range 1 - 65535.
Default guest-vlan-period: 90 seconds
reauth-period: 3600 seconds
quiet-period: 60 seconds
tx-period: 30 seconds
supp-timeout: 30 seconds
server-timeout: 30 seconds
Format dot1x timeout {{guest-vlan-period seconds} |{reauth-period seconds} |
{quiet-period seconds} | {tx-period seconds} | {supp-timeout seconds} |
{server-timeout seconds}}
Mode Interface Config
no dot1x timeout
This command sets the value, in seconds, of the timer used by the authenticator state
machine on this port to the default values. Depending on the token used, the corresponding
default values are set.
Format no dot1x timeout {guest-vlan-period | reauth-period | quiet-period |
tx-period | supp-timeout | server-timeout}
Mode Interface Config
dot1x unauthenticated-vlan
Use this command to configure the unauthenticated VLAN associated with the specified
interface or range of interfaces. The unauthenticated VLAN ID can be a valid VLAN ID from
0 to 4093. The unauthenticated VLAN must be statically configured in the VLAN database to
be operational. By default, the unauthenticated VLAN is 0, that is, invalid and not operational.
Default 0
Format dot1x unauthenticated-vlan vlan-id
Mode Interface Config
Switching Commands 469

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dot1x unauthenticated-vlan
This command resets the unauthenticated-vlan associated with the port to its default value.
Format no dot1x unauthenticated-vlan
Mode Interface Config
dot1x user
This command adds the specified user to the list of users with access to the specified port or
all ports. The user argument must be a configured user.
Format dot1x user user {unit/slot/port | all}
Mode Global Config
no dot1x user
This command removes the user from the list of users with access to the specified port or all
ports.
Format no dot1x user user {unit/slot/port | all}
Mode Global Config
authentication enable
This command globally enables the Authentication Manager. Interface configuration takes
effect only if the Authentication Manager is enabled with this command.
Default Disabled
Format authentication enable
Mode Global Config
no authentication enable
This command disables the Authentication Manager.
Format no authentication enable
Mode Global Config
authentication order
This command sets the order of authentication methods used on a port. The available
authentication methods are Dot1x, MAB, and captive portal. Ordering sets the order of
methods that the switch attempts when trying to authenticate a new device connected to a
port. If one method is unsuccessful or timed out, the next method is attempted.
Switching Commands 470

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Each method can only be entered once. Ordering is only possible between 802.1x and MAB.
Captive portal can be configured either as a stand-alone method or as the last method in the
order.
Format authentication order {dot1x [mab [captive-portal] | captive-portal] | mab
[dot1x [captive-portal]| captive-portal] | captive-portal}
Mode Interface Config
no authentication order
This command returns the port to the default authentication order.
Format no authentication order
Mode Interface Config
authentication priority
This command sets the priority for the authentication methods used on a port. The available
authentication methods are Dot1x, MAB, and captive portal. The authentication priority
decides if a previously authenticated client is reauthenticated with a higher-priority method
when the same is received. Captive portal is always the last method in the list.
Default authentication order dot1x mab captive portal
Format authentication priority {dot1x [mab [captive portal] | captive portal] | mab
[dot1x [captive portal]| captive portal] | captive portal}
Mode Interface Config
no authentication priority
This command returns the port to the default order of priority for the authentication methods.
Format no authentication priority
Mode Interface Config
authentication restart
This command sets the time, in seconds, after which reauthentication starts. The range is
300–65535 seconds and the default time is 300 seconds. The timer restarts the
authentication only after all the authentication methods fail. At the expiration of this timer,
authentication is reinitiated for the port.
Format authentication restart seconds
Mode Interface Config
Switching Commands 471

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no authentication restart
This command sets the reauthentication value to the default value of 3600 seconds.
Format no authentication restart
Mode Interface Config
show authentication authentication-history
Use this command to display information about the authentication history for a specified
interface.
Format show authentication authentication-history unit/slot/port
Mode Privileged EXEC
Term Definition
Time Stamp The time of the authentication.
Interface The interface.
MAC-Address The MAC address for the interface.
Auth Status Method The authentication method and status for the interface.
Command example:
Time Stamp Interface MAC-Address Auth Status Method
--------------------- --------- ----------------- ------ ------------
Jul 21 1919 15:06:15 1/0/1 00:00:00:00:00:01 Authorized 802.1X
show authentication interface
Use this command to display authentication method information either for all interfaces or a
specified port.
Format show authentication interface {all | unit/slot/port}
Mode Privileged EXEC
The following information is displayed for each interface.
Term Definition
Interface The interface for which authentication configuration information is displayed.
Authentication Restart timer The time, in seconds, after which reauthentication starts.
Configured method order The order of authentication methods used on a port.
Switching Commands 472

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Enabled method order The order of authentication methods used on a port.
Configured method priority The priority for the authentication methods used on a port.
Enabled method priority The priority for the authentication methods used on a port.
Number of authenticated clients The number of authenticated clients.
Logical Interface The logical interface
Client MAC addr The MAC address for the client.
Authenticated Method The current authentication method.
Auth State If the authentication was successful.
Auth Status The current authentication status.
Command example:
(NETGEAR Switch) #show authentication interface all
Interface...................................... 1/0/1
Authentication Restart timer................... 300
Configured method order........................ dot1x mab captive-portal
Enabled method order........................... dot1x mab undefined
Configured method priority..................... undefined undefined undefined
Enabled method priority........................ undefined undefined undefined
Number of authenticated clients................ 0
Interface...................................... 1/0/2
Authentication Restart timer................... 300
Configured method order........................ dot1x mab captive-portal
Enabled method order........................... dot1x mab undefined
Configured method priority..................... undefined undefined undefined
Enabled method priority........................ undefined undefined undefined
Number of authenticated clients................ 0
Interface...................................... 1/0/3
Authentication Restart timer................... 300
Configured method order........................ dot1x mab captive-portal
Enabled method order........................... dot1x mab undefined
Configured method priority..................... undefined undefined undefined
Enabled method priority........................ undefined undefined undefined
Number of authenticated clients................ 0
Interface...................................... 1/0/4
Authentication Restart timer................... 300
Configured method order........................ dot1x mab captive-portal
Enabled method order........................... dot1x mab undefined
Configured method priority..................... undefined undefined undefined
Enabled method priority........................ undefined undefined undefined
Number of authenticated clients................ 0
Switching Commands 473

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show authentication methods
Use this command to display information about the authentication methods.
Format show authentication methods
Mode Privileged EXEC
Term Definition
Authentication Login List The authentication login listname.
Method 1 The first method in the specified authentication login list, if any.
Method 2 The second method in the specified authentication login list, if any.
Method 3 The third method in the specified authentication login list, if any.
Command example:
(NETGEAR Switch)#show authentication methods
Login Authentication Method Lists
---------------------------------
defaultList : local
networkList : local
Enable Authentication Method Lists
----------------------------------
enableList : enable none
enableNetList : enable deny
Line Login Method List Enable Method List
------- ----------------- ------------------
Console defaultList enableList
Telnet networkList enableList
SSH networkList enableList
HTTPS :local
HTTP :local
DOT1X :
show authentication statistics
Use this command to display the authentication statistics for an interface.
Format show authentication statistics unit/slot/port
Mode Privileged EXEC
Switching Commands 474

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The following information is displayed for each interface.
Term Definition
Port The port for which information is displayed.
802.1X attempts The number of Dot1x authentication attempts for the port.
802.1X failed attempts The number of failed Dot1x authentication attempts for the port.
Mab attempts The number of MAB (MAC authentication bypass) authentication attempts for the port.
Mab failed attempts The number of failed MAB authentication attempts for the port.
Captive-portal attempts The number of captive portal (Web authorization) authentication attempts for the port.
Captive-portal failed attempts The number of failed captive portal authentication attempts for the port.
Command example:
(NETGEAR Switch) #show authentication statistics 1/0/1
Port........................................... 1/0/1
802.1X attempts................................ 0
802.1X failed attempts......................... 0
Mab attempts................................... 0
Mab failed attempts............................ 0
Captive-portal attempts........................ 0
Captive-Portal failed attempts................. 0
clear authentication statistics
Use this command to clear the authentication statistics on an interface.
Format clear authentication statistics {unit/slot/port] | all}
Mode Privileged EXEC
clear authentication authentication-history
Use this command to clear the authentication history log for an interface.
Format clear authentication authentication-history {unit/slot/port | all}
Mode Privileged EXEC
show dot1x
This command is used to show a summary of the global dot1x configuration, summary
information of the dot1x configuration for a specified port or all ports, the detailed dot1x
configuration for a specified port and the dot1x statistics for a specified port, depending on
the tokens used.
Switching Commands 475

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format show dot1x [{summary {unit/slot/port | all} | detail unit/slot/port |
statistics unit/slot/port}]
Mode Privileged EXEC
If you do not use the optional parameters unit/slot/port, the command displays the
global dot1x mode, the VLAN Assignment mode, and the Dynamic VLAN Creation mode.
Term Definition
Administrative Indicates whether authentication control on the switch is enabled or disabled.
Mode
VLAN Assignment Indicates whether assignment of an authorized port to a RADIUS-assigned VLAN is allowed
Mode (enabled) or not (disabled).
Dynamic VLAN Indicates whether the switch can dynamically create a RADIUS-assigned VLAN if it does not
Creation Mode currently exist on the switch.
Monitor Mode Indicates whether the Dot1x Monitor mode on the switch is enabled or disabled.
If you use the optional parameter summary {unit/slot/port | all}, the dot1x
configuration for the specified port or all ports are displayed.
Term Definition
Interface The interface whose configuration is displayed.
Control Mode The configured control mode for this port. Possible values are force-unauthorized, force-authorized,
auto, mac-based, authorized, and unauthorized.
Operating Control The control mode under which this port is operating. Possible values are authorized and
Mode unauthorized.
Reauthentication Indicates whether reauthentication is enabled on this port.
Enabled
Port Status Indicates whether the port is authorized or unauthorized. Possible values are authorized and
unauthorized.
Command example:
(NETGEAR Switch) #show dot1x summary 0/1
Operating
Interface Control Mode Control Mode Port Status
- -------- ------------ - ---------- ------------
0/1 a uto a uto Authorized
Switching Commands 476

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If you use the optional parameter detail unit/slot/port, the detailed dot1x
configuration for the specified port is displayed.
Term Definition
Port The interface whose configuration is displayed.
Protocol Version The protocol version associated with this port. The only possible value is 1, corresponding to the first
version of the dot1x specification.
PAE Capabilities The port access entity (PAE) functionality of this port. Possible values are Authenticator or
Supplicant.
Control Mode The configured control mode for this port. Possible values are force-unauthorized, force-authorized,
auto, and mac-based.
Authenticator PAE Current state of the authenticator PAE state machine. Possible values are Initialize, Disconnected,
State Connecting, Authenticating, Authenticated, Aborting, Held, ForceAuthorized, and
ForceUnauthorized. When MAC-based authentication is enabled on the port, this parameter is
deprecated.
Backend Current state of the backend authentication state machine. Possible values are Request, Response,
Authentication Success, Fail, Timeout, Idle, and Initialize. When MAC-based authentication is enabled on the port,
State this parameter is deprecated.
Quiet Period The timer used by the authenticator state machine on this port to define periods of time in which it
will not attempt to acquire a supplicant. The value is expressed in seconds and will be in the range 0
and 65535.
Transmit Period The timer used by the authenticator state machine on the specified port to determine when to send
an EAPOL EAP Request/Identity frame to the supplicant. The value is expressed in seconds and will
be in the range of 1 and 65535.
Guest-VLAN ID The guest VLAN identifier configured on the interface.
Guest VLAN Period The time in seconds for which the authenticator waits before authorizing and placing the port in the
Guest VLAN, if no EAPOL packets are detected on that port.
Supplicant Timeout The timer used by the authenticator state machine on this port to timeout the supplicant. The value is
expressed in seconds and will be in the range of 1 and 65535.
Server Timeout The timer used by the authenticator on this port to timeout the authentication server. The value is
expressed in seconds and will be in the range of 1 and 65535.
Maximum The maximum number of times the authenticator state machine on this port will retransmit an
Requests EAPOL EAP Request/Identity before timing out the supplicant. The value will be in the range of 1
and 10.
Configured MAB The administrative mode of the MAC authentication bypass feature on the switch.
Mode
Operational MAB The operational mode of the MAC authentication bypass feature on the switch. MAB might be
Mode administratively enabled but not operational if the control mode is not MAC based.
Vlan-ID The VLAN assigned to the port by the radius server. This is only valid when the port control mode is
not Mac-based.
Switching Commands 477

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
VLAN Assigned The reason the VLAN identified in the VLAN-assigned field has been assigned to the port. Possible
Reason values are RADIUS, Unauthenticated VLAN, Guest VLAN, default, and Not Assigned. When the
VLAN Assigned Reason is Not Assigned, it means that the port has not been assigned to any VLAN
by dot1x. This only valid when the port control mode is not MAC-based.
Reauthentication The timer used by the authenticator state machine on this port to determine when reauthentication of
Period the supplicant takes place. The value is expressed in seconds and will be in the range of 1 and
65535.
Reauthentication Indicates if reauthentication is enabled on this port. Possible values are True and False.
Enabled
Key Transmission Indicates if the key is transmitted to the supplicant for the specified port. Possible values are True or
Enabled False.
EAPOL Flood Indicates whether the EAPOL flood support is enabled on the switch. Possible values are True and
Mode Enabled False.
Control Direction The control direction for the specified port or ports. Possible values are both and in.
Maximum Users The maximum number of clients that can get authenticated on the port in the MAC-based dot1x
authentication mode. This value is used only when the port control mode is not MAC-based.
Unauthenticated Indicates the unauthenticated VLAN configured for this port. This value is valid for the port only when
VLAN ID the port control mode is not MAC-based.
Session Timeout Indicates the time for which the given session is valid. The time period in seconds is returned by the
RADIUS server on authentication of the port. This value is valid for the port only when the port
control mode is not MAC-based.
Session This value indicates the action to be taken once the session timeout expires. Possible values are
Termination Action Default, Radius-Request. If the value is Default, the session is terminated the port goes into
unauthorized state. If the value is Radius-Request, then a reauthentication of the client
authenticated on the port is performed. This value is valid for the port only when the port control
mode is not MAC-based.
Command example:
(NETGEAR Switch) #show dot1x detail 1/0/3
Port........................................... 1/0/1
Protocol Version............................... 1
PAE Capabilities............................... Authenticator
Control Mode................................... auto
Authenticator PAE State........................ Initialize
Backend Authentication State................... Initialize
Quiet Period (secs)............................ 60
Transmit Period (secs)......................... 30
Guest VLAN ID.................................. 0
Guest VLAN Period (secs)....................... 90
Supplicant Timeout (secs)...................... 30
Server Timeout (secs).......................... 30
Maximum Requests............................... 2
Switching Commands 478

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Configured MAB Mode............................ Enabled
Operational MAB Mode........................... Disabled
VLAN Id........................................ 0
VLAN Assigned Reason........................... Not Assigned
Reauthentication Period (secs)................. 3600
Reauthentication Enabled....................... FALSE
Key Transmission Enabled....................... FALSE
EAPOL flood Mode Enabled....................... FALSE
Control Direction.............................. both
Maximum Users.................................. 16
Unauthenticated VLAN ID........................ 0
Session Timeout................................ 0
Session Termination Action..................... Default
For each client authenticated on the port, the show dot1x detail unit/slot/port
command displays the following MAC-based dot1x parameters if the port-control mode for
that specific port is MAC-based.
Term Definition
Supplicant The MAC-address of the supplicant.
MAC-Address
Authenticator PAE Current state of the authenticator PAE state machine. Possible values are Initialize, Disconnected,
State Connecting, Authenticating, Authenticated, Aborting, Held, ForceAuthorized, and
ForceUnauthorized.
Backend Current state of the backend authentication state machine. Possible values are Request, Response,
Authentication Success, Fail, Timeout, Idle, and Initialize.
State
VLAN-Assigned The VLAN assigned to the client by the radius server.
Logical Port The logical port number associated with the client.
If you use the optional parameter statistics unit/slot/port, the following dot1x
statistics for the specified port appear.
Term Definition
Port The interface whose statistics are displayed.
EAPOL Frames The number of valid EAPOL frames of any type that have been received by this authenticator.
Received
EAPOL Frames The number of EAPOL frames of any type that have been transmitted by this authenticator.
Transmitted
EAPOL Start The number of EAPOL start frames that have been received by this authenticator.
Frames Received
EAPOL Logoff The number of EAPOL logoff frames that have been received by this authenticator.
Frames Received
Switching Commands 479

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Last EAPOL Frame The protocol version number carried in the most recently received EAPOL frame.
Version
Last EAPOL Frame The source MAC address carried in the most recently received EAPOL frame.
Source
EAP Response/Id The number of EAP response/identity frames that have been received by this authenticator.
Frames Received
EAP Response The number of valid EAP response frames (other than resp/id frames) that have been received by
Frames Received this authenticator.
EAP Request/Id The number of EAP request/identity frames that have been transmitted by this authenticator.
Frames
Transmitted
EAP Request The number of EAP request frames (other than request/identity frames) that have been transmitted
Frames by this authenticator.
Transmitted
Invalid EAPOL The number of EAPOL frames that have been received by this authenticator in which the frame type
Frames Received is not recognized.
EAP Length Error The number of EAPOL frames that have been received by this authenticator in which the frame type
Frames Received is not recognized.
show dot1x authentication-history
This command displays 802.1X authentication events and information during successful and
unsuccessful Dot1x authentication process for all interfaces or the specified interface. Use
the optional keywords to display only failure authentication events in summary or in detail.
Format show dot1x authentication-history {unit/slot/port | all} [failed-auth-only]
[detail]
Mode Privileged EXEC
Term Definition
Time Stamp The exact time at which the event occurs.
Interface Physical Port on which the event occurs.
Mac-Address The supplicant/client MAC address.
VLAN assigned The VLAN assigned to the client/port on authentication.
VLAN assigned The type of VLAN ID assigned, which can be Guest VLAN, Unauth, Default, RADIUS Assigned, or
Reason Monitor Mode VLAN ID.
Auth Status The authentication status.
Reason The actual reason behind the successful or failed authentication.
Switching Commands 480

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show dot1x clients
This command displays 802.1X client information. This command also displays information
about the number of clients that are authenticated using Monitor mode and using 802.1X.
Format show dot1x clients {unit/slot/port | all}
Mode Privileged EXEC
Term Definition
Clients Authenticated Indicates the number of the Dot1x clients authenticated using Monitor mode.
using Monitor Mode
Clients Authenticated Indicates the number of Dot1x clients authenticated using 802.1x authentication process.
using Dot1x
Logical Interface The logical port number associated with a client.
Interface The physical port to which the supplicant is associated.
User Name The user name used by the client to authenticate to the server.
Supplicant MAC The supplicant device MAC address.
Address
Session Time The time since the supplicant is logged on.
Filter ID Identifies the Filter ID returned by the RADIUS server when the client was authenticated. This
is a configured DiffServ policy name on the switch.
VLAN ID The VLAN assigned to the port.
VLAN Assigned The reason the VLAN identified in the VLAN ID field has been assigned to the port. Possible
values are RADIUS, Unauthenticated VLAN, Monitor Mode, or Default. When the VLAN
Assigned reason is Default, it means that the VLAN was assigned to the port because the
P-VID of the port was that VLAN ID.
Session Timeout This value indicates the time for which the given session is valid. The time period in seconds is
returned by the RADIUS server on authentication of the port. This value is valid for the port
only when the port-control mode is not MAC-based.
Session Termination This value indicates the action to be taken once the session timeout expires. Possible values
Action are Default and Radius-Request. If the value is Default, the session is terminated and client
details are cleared. If the value is Radius-Request, then a reauthentication of the client is
performed.
show dot1x users
This command displays 802.1X port security user information for locally configured users.
Format show dot1x users unit/slot/port
Mode Privileged EXEC
Switching Commands 481

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Users Users configured locally to have access to the specified port.
802.1X Supplicant Commands
The switch supports 802.1X (dot1x) supplicant functionality on point-to-point ports. The
administrator can configure the user name and password used in authentication and
capabilities of the supplicant port.
dot1x pae
This command sets the port’s dot1x role. The port can serve as either a supplicant or an
authenticator.
Format dot1x pae {supplicant | authenticator}
Mode Interface Config
dot1x supplicant port-control
This command sets the ports authorization state (Authorized or Unauthorized) either
manually or by setting the port to auto-authorize upon startup. By default all the ports are
authenticators. If the port’s attribute needs to be moved from authenticator to supplicant or
from supplicant to authenticator, use this command.
Format dot1x supplicant port-control {auto | force-authorized | force-unauthorized}
Mode Interface Config
Parameter Description
auto The port is in the Unauthorized state until it presents its user name and password credentials to an
authenticator. If the authenticator authorizes the port, then it is placed in the Authorized state.
force-authorized Sets the authorization state of the port to Authorized, bypassing the authentication process.
force-unauthorized Sets the authorization state of the port to Unauthorized, bypassing the authentication process.
no dot1x supplicant port-control
This command sets the port-control mode to the default, auto.
Default auto
Format no dot1x supplicant port-control
Mode Interface Config
Switching Commands 482

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
dot1x supplicant max-start
This command configures the number of attempts that the supplicant makes to find the
authenticator before the supplicant assumes that there is no authenticator. The number of
attempts can be in a range from 1–10. The default is 3 attempts.
Default 3
Format dot1x supplicant max-start number
Mode Interface Config
no dot1x supplicant max-start
This command sets the max-start value to the default.
Format no dot1x supplicant max-start
Mode Interface Config
dot1x supplicant timeout start-period
This command configures the start period timer interval to wait for the EAP identity request
from the authenticator. The interval can be in a range from 1–65535 seconds. The default is
30 seconds.
Default 30 seconds
Format dot1x supplicant timeout start-period seconds
Mode Interface Config
no dot1x supplicant timeout start-period
This command sets the start-period value to the default.
Format no dot1x supplicant timeout start-period
Mode Interface Config
dot1x supplicant timeout held-period
This command configures the held period timer interval to wait for the next authentication on
previous authentication fail. The interval can be in a range from 1–65535 seconds. The
default is 30 seconds.
Default 60 seconds
Format dot1x supplicant timeout held-period seconds
Mode Interface Config
Switching Commands 483

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dot1x supplicant timeout held-period
This command sets the held-period value to the default value.
Format no dot1x supplicant timeout held-period
Mode Interface Config
dot1x supplicant timeout auth-period
This command configures the authentication period timer interval to wait for the next EAP
request challenge from the authenticator. The interval can be in a range from 1–65535
seconds. The default is 30 seconds.
Default 30 seconds
Format dot1x supplicant timeout auth-period seconds
Mode Interface Config
no dot1x supplicant timeout auth-period
This command sets the auth-period value to the default value.
Format no dot1x supplicant timeout auth-period
Mode Interface Config
dot1x supplicant user
Use this command to map the given user to the port.
Format dot1x supplicant user
Mode Interface Config
show dot1x statistics
This command displays the dot1x port statistics in detail.
Format show dot1x statistics unit/slot/port
Mode Privileged EXEC
User EXEC
Term Definition
EAPOL Frames Received Displays the number of valid EAPOL frames received on the port.
EAPOL Frames Transmitted Displays the number of EAPOL frames transmitted via the port.
Switching Commands 484

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
EAPOL Start Frames Transmitted Displays the number of EAPOL Start frames transmitted via the port.
EAPOL Logoff Frames Received Displays the number of EAPOL Log off frames that have been received on the
port.
EAP Resp/ID Frames Received Displays the number of EAP Respond ID frames that have been received on the
port.
EAP Response Frames Received Displays the number of valid EAP Respond frames received on the port.
EAP Req/ID Frames Transmitted Displays the number of EAP Requested ID frames transmitted via the port.
EAP Req Frames Transmitted Displays the number of EAP Request frames transmitted via the port.
Invalid EAPOL Frames Received Displays the number of unrecognized EAPOL frames received on this port.
EAP Length Error Frames Received Displays the number of EAPOL frames with an invalid Packet Body Length
received on this port.
Last EAPOL Frames Version Displays the protocol version number attached to the most recently received
EAPOL frame.
Last EAPOL Frames Source Displays the source MAC Address attached to the most recently received
EAPOL frame.
Command example:
(NETGEAR Switch) #show dot1x statistics 0/1
Port........................................... 0/1
EAPOL Frames Received.......................... 0
EAPOL Frames Transmitted....................... 0
EAPOL Start Frames Transmitted................. 3
EAPOL Logoff Frames Received................... 0
EAP Resp/Id frames transmitted................. 0
EAP Response frames transmitted................ 0
EAP Req/Id frames transmitted.................. 0
EAP Req frames transmitted..................... 0
Invalid EAPOL frames received.................. 0
EAP length error frames received............... 0
Last EAPOL Frame Version....................... 0
Last EAPOL Frame Source........................ 00:00:00:00:02:01
Switching Commands 485

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Storm-Control Commands
This section describes commands you use to configure storm-control and view storm-control
configuration information. A traffic storm is a condition that occurs when incoming packets
flood the LAN, which creates performance degradation in the network. The Storm-Control
feature protects against this condition.
The switch provides broadcast, multicast, and unicast story recovery for individual interfaces.
Unicast Storm-Control protects against traffic whose MAC addresses are not known by the
system. For broadcast, multicast, and unicast storm-control, if the rate of traffic ingressing on
an interface increases beyond the configured threshold for that type, the traffic is dropped.
To configure storm-control, you will enable the feature for all interfaces or for individual
interfaces, and you will set the threshold (storm-control level) beyond which the broadcast,
multicast, or unicast traffic will be dropped. The Storm-Control feature allows you to limit the
rate of specific types of packets through the switch on a per-port, per-type, basis.
Configuring a storm-control level also enables that form of storm-control. Disabling a
storm-control level (using the no version of the command) sets the storm-control level back to
the default value and disables that form of storm-control. Using the no version of a
storm-control command (not stating a level) disables that form of storm-control but maintains
the configured level (to be active the next time that form of storm-control is enabled.)
Note: The actual rate of ingress traffic required to activate storm-control is
based on the size of incoming packets and the hard-coded average
packet size of 512 bytes - used to calculate a packet-per-second (pps)
rate - as the forwarding-plane requires pps versus an absolute rate
kbps. For example, if the configured limit is 10 percent, this is
converted to ~25000 pps, and this pps limit is set in forwarding plane
(hardware). You get the approximate desired output when 512bytes
packets are used.
storm-control broadcast
Use this command to enable broadcast storm recovery mode for all interfaces (Global Config
mode) or one or more interfaces (Interface Config mode). If the mode is enabled, broadcast
storm recovery is active and, if the rate of L2 broadcast traffic ingressing on an interface
increases beyond the configured threshold, the traffic will be dropped. Therefore, the rate of
broadcast traffic will be limited to the configured threshold.
Default Enabled
Format storm-control broadcast
Mode Global Config
Interface Config
Switching Commands 486

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no storm-control broadcast
Use this command to disable broadcast storm recovery mode for all interfaces (Global Config
mode) or one or more interfaces (Interface Config mode).
Format no storm-control broadcast
Mode Global Config
Interface Config
storm-control broadcast action
This command configures the broadcast storm recovery action to either shut down or send
traps for one, several, or all interfaces. If you enter the command in Global Config mode, the
action applies to all interfaces. If you enter the command in Interface Config mode, the action
applies to or one or more interfaces.
If you specify the shutdown keyword, the interface that receives the broadcast packets at a
rate above the threshold is diagnostically disabled. If you specify the trap keyword, the
interface sends trap messages approximately every 30 seconds until broadcast storm control
recovers.
Format storm-control broadcast action {shutdown | trap}
Mode Global Config
Interface Config
no storm-control broadcast action
This command sets the broadcast storm recovery action to the default value for one, several,
or all interfaces. If you enter the command in Global Config mode, the action applies to all
interfaces. If you enter the command in Interface Config mode, the action applies to or one or
more interfaces.
Format no storm-control broadcast action
Mode Global Config
Interface Config
storm-control broadcast level
Use this command to configure the broadcast storm recovery threshold for all interfaces
(Global Config mode) or one or more interfaces (Interface Config mode) as a percentage of
link speed and enable broadcast storm recovery. If the mode is enabled, broadcast storm
recovery is active, and if the rate of L2 broadcast traffic ingressing on an interface increases
beyond the configured threshold, the traffic is dropped. Therefore, the rate of broadcast traffic
is limited to the configured threshold. The threshold level can be in the range from 0–100.
The default is 5.
Switching Commands 487

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default 5
Format storm-control broadcast level threshold
Mode Global Config
Interface Config
no storm-control broadcast level
This command sets the broadcast storm recovery threshold to the default value for all
interfaces (Global Config mode) or one or more interfaces (Interface Config mode) and
disables broadcast storm recovery.
Format no storm-control broadcast level
Mode Global Config
Interface Config
storm-control broadcast rate
Use this command to configure the broadcast storm recovery threshold for all interfaces
(Global Config mode) or one or more interfaces (Interface Config mode) in packets per
second. If the mode is enabled, broadcast storm recovery is active, and if the rate of L2
broadcast traffic ingressing on an interface increases beyond the configured threshold, the
traffic is dropped. Therefore, the rate of broadcast traffic is limited to the configured threshold.
The threshold rate can be in the range from 0–14880000. The default is 0.
Default 0
Format storm-control broadcast rate threshold
Mode Global Config
Interface Config
no storm-control broadcast rate
This command sets the broadcast storm recovery threshold to the default value for all
interfaces (Global Config mode) or one or more interfaces (Interface Config mode) and
disables broadcast storm recovery.
Format no storm-control broadcast rate
Mode Global Config
Interface Config
storm-control multicast
This command enables multicast storm recovery mode for all interfaces (Global Config
mode) or one or more interfaces (Interface Config mode). If the mode is enabled, multicast
Switching Commands 488

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
storm recovery is active, and if the rate of L2 multicast traffic ingressing on an interface
increases beyond the configured threshold, the traffic will be dropped. Therefore, the rate of
multicast traffic will be limited to the configured threshold.
Default Disabled
Format storm-control multicast
Mode Global Config
Interface Config
no storm-control multicast
This command disables multicast storm recovery mode for all interfaces (Global Config
mode) or one or more interfaces (Interface Config mode).
Format no storm-control multicast
Mode Global Config
Interface Config
storm-control multicast action
This command configures the multicast storm recovery action to either shut down or send
traps for one, several, or all interfaces. If you enter the command in Global Config mode, the
action applies to all interfaces. If you enter the command in Interface Config mode, the action
applies to or one or more interfaces.
If you specify the shutdown keyword, the interface that receives the multicast packets at a
rate above the threshold is diagnostically disabled. If you specify the trap keyword, the
interface sends trap messages approximately every 30 seconds until multicast storm control
recovers.
Format storm-control multicast action {shutdown | trap}
Mode Global Config
Interface Config
no storm-control multicast action
This command sets the multicast storm recovery action to the default value for one, several,
or all interfaces. If you enter the command in Global Config mode, the action applies to all
interfaces. If you enter the command in Interface Config mode, the action applies to or one or
more interfaces.
Format no storm-control multicast action
Mode Global Config
Interface Config
Switching Commands 489

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
storm-control multicast level
This command configures the multicast storm recovery threshold for all interfaces (Global
Config mode) or one or more interfaces (Interface Config mode) as a percentage of link
speed and enables multicast storm recovery mode. If the mode is enabled, multicast storm
recovery is active, and if the rate of L2 multicast traffic ingressing on an interface increases
beyond the configured threshold, the traffic will be dropped. Therefore, the rate of multicast
traffic will be limited to the configured threshold. The threshold level can be in the range from
0–100. The default is 5.
Default 5
Format storm-control multicast level 0-100
Mode Global Config
Interface Config
no storm-control multicast level
This command sets the multicast storm recovery threshold to the default value for all
interfaces (Global Config mode) or one or more interfaces (Interface Config mode) and
disables multicast storm recovery.
Format no storm-control multicast level
Mode Global Config
Interface Config
storm-control multicast rate
Use this command to configure the multicast storm recovery threshold for all interfaces
(Global Config mode) or one or more interfaces (Interface Config mode) in packets per
second. If the mode is enabled, multicast storm recovery is active, and if the rate of L2
broadcast traffic ingressing on an interface increases beyond the configured threshold, the
traffic is dropped. Therefore, the rate of multicast traffic is limited to the configured threshold.
The threshold rate can be in the range from 0–14880000. The default is 0.
Default 0
Format storm-control multicast rate threshold
Mode Global Config
Interface Config
Switching Commands 490

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no storm-control multicast rate
This command sets the multicast storm recovery threshold to the default value for all
interfaces (Global Config mode) or one or more interfaces (Interface Config mode) and
disables multicast storm recovery.
Format no storm-control multicast rate
Mode Global Config
Interface Config
storm-control unicast
This command enables unicast storm recovery mode for all interfaces (Global Config mode)
or one or more interfaces (Interface Config mode). If the mode is enabled, unicast storm
recovery is active, and if the rate of unknown L2 unicast (destination lookup failure) traffic
ingressing on an interface increases beyond the configured threshold, the traffic will be
dropped. Therefore, the rate of unknown unicast traffic will be limited to the configured
threshold.
Default Disabled
Format storm-control unicast
Mode Global Config
Interface Config
no storm-control unicast
This command disables unicast storm recovery mode for all interfaces (Global Config mode)
or one or more interfaces (Interface Config mode).
Format no storm-control unicast
Mode Global Config
Interface Config
storm-control unicast action
This command configures the unicast storm recovery action to either shut down or send traps
for one, several, or all interfaces. If you enter the command in Global Config mode, the action
applies to all interfaces. If you enter the command in Interface Config mode, the action
applies to or one or more interfaces.
If you specify the shutdown keyword, the interface that receives the unicast packets at a
rate above the threshold is diagnostically disabled. If you specify the trap keyword, the
interface sends trap messages approximately every 30 seconds until unicast storm control
recovers.
Switching Commands 491

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format storm-control unicast action {shutdown | trap}
Mode Global Config
Interface Config
no storm-control unicast action
This command sets the unicast storm recovery action to the default value for one, several, or
all interfaces. If you enter the command in Global Config mode, the action applies to all
interfaces. If you enter the command in Interface Config mode, the action applies to or one or
more interfaces.
Format no storm-control unicast action
Mode Global Config
Interface Config
storm-control unicast level
This command configures the unicast storm recovery threshold for all interfaces (Global
Config mode) or one or more interfaces (Interface Config mode) as a percentage of link
speed, and enables unicast storm recovery. If the mode is enabled, unicast storm recovery is
active, and if the rate of unknown L2 unicast (destination lookup failure) traffic ingressing on
an interface increases beyond the configured threshold, the traffic will be dropped. Therefore,
the rate of unknown unicast traffic will be limited to the configured threshold. This command
also enables unicast storm recovery mode for an interface. The threshold level can be in the
range from 0–100. The default is 5.
Default 5
Format storm-control unicast level threshold
Mode Global Config
Interface Config
no storm-control unicast level
This command sets the unicast storm recovery threshold to the default value for all interfaces
(Global Config mode) or one or more interfaces (Interface Config mode) and disables unicast
storm recovery.
Format no storm-control unicast level
Mode Global Config
Interface Config
Switching Commands 492

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
storm-control unicast rate
Use this command to configure the unicast storm recovery threshold for all interfaces (Global
Config mode) or one or more interfaces (Interface Config mode) in packets per second. If the
mode is enabled, unicast storm recovery is active, and if the rate of L2 broadcast traffic
ingressing on an interface increases beyond the configured threshold, the traffic is dropped.
Therefore, the rate of unicast traffic is limited to the configured threshold. The threshold rate
can be in the range from 0–14880000. The default is 0.
Default 0
Format storm-control unicast rate threshold
Mode Global Config
Interface Config
no storm-control unicast rate
This command sets the unicast storm recovery threshold to the default value for all interfaces
(Global Config mode) or one or more interfaces (Interface Config mode) and disables unicast
storm recovery.
Format no storm-control unicast rate
Mode Global Config
Interface Config
show storm-control
This command displays switch configuration information. If you do not use any of the optional
parameters, this command displays global storm control configuration parameters:
• Broadcast Storm Recovery Mode may be enabled or disabled. The factory default is
disabled.
• 802.3x Flow Control Mode may be enabled or disabled. The factory default is disabled.
Use the all keyword to display the per-port configuration parameters for all interfaces, or
specify the unit/slot/port to display information about a specific interface.
Format show storm-control [all | unit/slot/port]
Mode Privileged EXEC
Parameter Definition
Bcast Mode Shows whether the broadcast storm control mode is enabled or disabled. The factory default is
disabled.
Bcast Level The broadcast storm control level.
Bcast Action The broadcast storm recovery acton.
Switching Commands 493

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Definition
Mcast Mode Shows whether the multicast storm control mode is enabled or disabled.
Mcast Level The multicast storm control level.
Mcast Action The multicast storm recovery acton.
Ucast Mode Shows whether the Unknown Unicast or DLF (Destination Lookup Failure) storm control mode is
enabled or disabled.
Ucast Level The Unknown Unicast or DLF (Destination Lookup Failure) storm control level.
Ucast Action The unicast storm recovery acton.
Command example:
(NETGEAR Switch) #show storm-control
Broadcast Storm Control Mode................... Enable
Broadcast Storm Control Level.................. 5 percent
Broadcast Storm Control Action................. None
Multicast Storm Control Mode................... Disable
Multicast Storm Control Level.................. 5 percent
Multicast Storm Control Action................. None
Unicast Storm Control Mode..................... Disable
Unicast Storm Control Level.................... 5 percent
Unicast Storm Control Action................... None
Command example:
(NETGEAR Switch) #show storm-control 1/0/1
B cast B cast B cast M cast M cast M cast U cast U cast U cast F low Mode
I ntf M ode L evel A ction M ode L evel A ction M ode L evel Action
- ---- - ----- - ---- - ----- - ------ - ---- - ----- - ------ - ---- - ----- -------
1 /0/1 E nable 5 % N one D isable 5 % N one D isable 5 % N one Disable
Command example:
(NETGEAR Switch) #show storm-control all
B cast B cast B cast M cast M cast M cast U cast U cast U cast F low Mode
I ntf M ode L evel A ction M ode L evel A ction M ode L evel Action
- ---- - ----- - ---- - ----- - ------ - ---- - ----- - ------ - ---- - ----- -------
1 /0/1 E nable 5 % N one D isable 5 % N one D isable 5 % N one Disable
1 /0/2 E nable 5 % N one D isable 5 % N one D isable 5 % N one Disable
1 /0/3 E nable 5 % N one D isable 5 % N one D isable 5 % N one Disable
1 /0/4 E nable 5 % N one D isable 5 % N one D isable 5 % N one Disable
1 /0/5 E nable 5 % N one D isable 5 % N one D isable 5 % N one Disable
Switching Commands 494

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Link Dependency Commands
Link dependency allows the link status of specified ports to be dependent on the link status of
one port or many ports. Consequently, if a port on which other ports depend loses a link, the
dependent ports either become administratively disabled and are brought down or become
administratively enabled and are brought up.
link state group
Use this command to indicate if the downstream interfaces of a specified group must mirror
or invert the status of the upstream interfaces. The default configuration for a group is down.
That is, the downstream interfaces mirror the upstream link status by going down when all
upstream interfaces are down. Specifying the up keyword allows the downstream interfaces
to come up when all upstream interfaces are down.
Default down
Format link state group group-id action {up | down}
Mode Global Config
link state group downstream
Use this command to add a group of interfaces to the downstream interface list. Adding an
interface to a downstream list brings the interface down until an upstream interface is added
to the group. The link status then follows the interface that is specified in the link state
group upstream command. To prevent interfaces from being brought down, enter the
link state group upstream command before you enter the link state group
downstream command.
Format link state group group-id downstream
Mode Interface Config
no link state group downstream
Use this command to remove a group of interfaces from the downstream list.
Format no link state group group-id downstream
Mode Interface Config
Switching Commands 495

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
link state group upstream
Use this command to add a group of interfaces to the upstream interface list.
An interface that is defined as an upstream interface cannot also be defined as a downstream
interface in the same link state group or as a downstream interface in a different link state
group if either configuration creates a circular dependency between groups.
Format link state group group-id upstream
Mode Interface Config
no link state group upstream
Use this command to remove a group of interfaces from the upstream list.
Format no link state group group-id upstream
Mode Interface Config
show link state group
Use this command to display information about all configured link-dependency groups or a
specific link-dependency group.
Format show link state group [group-id]
Mode Privileged EXEC
Command example:
This example displays information about all configured link-dependency groups.
(Switching) #show link-state group
G roupId D ownstream Interfaces U pstream Interfaces L ink Action Group State
- ------ - ------------------------- - ------------------- - ---------- -----------
1 2 /0/3-2/0/7,2/0/12-2/0/17 2 /0/12-2/0/32,0/3/5 L ink Up Up
4 2 /0/18,2/0/27 2 /0/22-2/0/33,0/3/1 L ink Up Down
Command example:
This example displays information about a specific link-dependency group.
(Switching) #show link state group 1
G roupId D ownstream Interfaces U pstream Interfaces L ink Action Group State
- ------ - ------------------------- - ------------------- - ---------- -----------
1 2 /0/3-2/0/7,2/0/12-2/0/17 2 /0/12-2/0/32,0/3/5 L ink Up Up
Switching Commands 496

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show link state group detail
Use this command to display detailed information about the state of upstream and
downstream interfaces for a selected link-dependency group. The Group Transitions field
shows a count of the number of times that the downstream interface went into its action state
as a result of the upstream interfaces link state.
Format show link state group group-id detail
Mode Privileged EXEC
Command example:
(Switching) #show link state group 1 detail
GroupId: 1
Link Action: Up
Group State: Up
Downstream Interface State:
Link Up: 2/0/3
Link Down: 2/0/4-2/0/7,2/0/12-2/0/17
Upstream Interface State:
Link Up: -
Link Down: 2/0/12-2/0/32,0/3/5
Group Transitions: 0
Last Transition Time: 00:52:35 (UTC+0:00) Nov 3 2015
Link Local Protocol Filtering Commands
Link Local Protocol Filtering (LLPF) allows the switch to filter out multiple proprietary protocol
PDUs, such as Port Aggregation Protocol (PAgP), if the problems occur with proprietary
protocols running on standards-based switches. If certain protocol PDUs cause unexpected
results, LLPF can be enabled to prevent those protocol PDUs from being processed by the
switch.
llpf
Use this command to block LLPF protocol(s) on a port.
Default disable
Format llpf {blockisdp | blockvtp | blockdtp | blockudld | blockpagp | blocksstp |
blockall}
Mode Interface Config
Switching Commands 497

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no llpf
Use this command to unblock LLPF protocol(s) on a port.
Format no llpf {blockisdp | blockvtp | blockdtp | blockudld | blockpagp | blocksstp
| blockall }
Mode Interface Config
show llpf interface
Use this command to display the status of LLPF rules configured on a particular port or on all
ports..
Format show llpf interface [all | unit/slot/port]
Mode Privileged EXEC
Term Definition
Block ISDP Shows whether the port blocks ISDP PDUs.
Block VTP Shows whether the port blocks VTP PDUs.
Block DTP Shows whether the port blocks DTP PDUs.
Block UDLD Shows whether the port blocks UDLD PDUs.
Block PAGP Shows whether the port blocks PAgP PDUs.
Block SSTP Shows whether the port blocks SSTP PDUs.
Block All Shows whether the port blocks all proprietary PDUs available for the LLDP feature.
MRP Commands
Multicast Registration Protocol (MRP) replaces the Generic Attribute Registration Protocol
(GARP) functionality. MRP provides the same functionality as GARP. MRP is a generic
registration framework defined by the IEEE 802.1ak amendment to the IEEE 802.1Q
standard.
mrp
This command sets the MRP protocol timers on an interface.
Format mrp {jointime seconds | leavetime seconds | leavealltime seconds}
Mode Interface Config
Switching Commands 498

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
jointime seconds The interval between the transmission of MRP PDUs registering (or reregistering) membership for
an attribute. There is an instance of this timer on a per-port, per-MRP participant basis.
Permissible values are 10 to 100 centiseconds (0.1 to 1.0 seconds). The factory default is
20centiseconds (0.2 seconds). The finest granularity of specification is one centisecond
( 0.01seconds).
leavetime seconds The period of time to wait after receiving an unregister request for an attribute before deleting the
attribute. You can consider this a buffer time for another station to assert registration for the same
attribute in order to maintain uninterrupted service. There is an instance of this timer on a
per-Port, per-MRP participant basis. Permissible values are 20 to 600 centiseconds (0.2 to
6.0seconds). The factory default is 300 centiseconds (3.0 seconds).
leavealltime seconds The LeaveAllTime controls how frequently LeaveAll PDUs are generated. A LeaveAll PDU
indicates that all registrations are shortly to be deregistered. Participants must to rejoin in order to
maintain registration. There is an instance of this timer on a per-port, per-MRP participant basis.
The Leave All Period Timer is set to a random value in the range of LeaveAllTime to
1.5*LeaveAllTime. Permissible values are 200 to 6000 centiseconds (2 to 60 seconds). The
factory default is 2000 centiseconds (20 seconds).
show mrp
This command displays MRP leave, join, and leaveall intervals configured on interfaces. If
you specify the summary parameter, the output shows interval values for all interfaces. If you
specify the unit/slot/port parameter, the output shows the MRP intervals for the
specified interface.
Format show mrp interface {summary | unit/slot/port}
Mode Privileged Exec
MMRP Commands
mmrp (Global Config)
Use this command in Global Config mode to enable MMRP. MMRP must also be enabled on
the individual interfaces.
Default Disabled
Format mmrp
Mode Global Config
Switching Commands 499

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no mmrp (Global Config)
Use this command in Global Config mode to disable MMRP.
Format no mmrp
Mode Global Config
mmrp periodic state machine
Use this command in Global Config mode to enable MMRP periodic state machine.
Default Disabled
Format mmrp periodic state machine
Mode Global Config
no mmrp periodic state machine
Use this command in Global Config mode to disable MMRP periodic state machine.
Format no mmrp periodic state machine
Mode Global Config
mmrp (Interface Config)
Use this command in Interface Config mode on the interface. MMRP can be enabled on
physical interfaces or LAG interfaces. When configured on a LAG member port, MMRP is
operationally disabled. Enabling MMRP on an interface automatically enables dynamic
MFDB entries creation.
Default Disabled
Format mmrp
Mode Interface Config
no mmrp (Interface Config)
Use this command in Interface Config mode to disable MMRP mode on the interface.
Format no mmrp
Mode Global Config
Switching Commands 500

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
clear mmrp statistics
Use this command in Privileged EXEC mode to clear MMRP statistics of one or all interfaces.
Format clear mmrp statistics [unit/slot/port | all]
Mode Privileged EXEC
Parameter Description
unit/slot/port If used with unit/slot/port parameter, the command clears MMRP statistics for the given
interface.
all If the all parameter is specified, the command clears MMRP statistics for all the interfaces.
show mmrp
Use this command in Privileged EXEC mode to display the status of the MMRP mode.
Format show mmrp [summary | interface [unit/slot/port | summary]]
Mode Privileged EXEC
Parameter Description
summary If used with the summary parameter, the command displays global MMRP information.
interface If interface is specified for a particular unit/slot/port, the command displays the MMRP
mode of that interface.
summary If interface is specified with the summary parameter, the command shows a table containing
MMRP global mode for all interfaces.
Command example:
(NETGEAR switch) #show mmrp summary
MMRP Global Admin Mode......................... Disabled
MMRP Periodic State Machine.................... Disabled
Command example:
(NETGEAR switch) #show mmrp interface 0/12
MMRP Interface Admin Mode...................... Disabled
Command example:
(NETGEAR switch) #show mmrp interface summary
Intf Mode
--------- ---------
0/1 Disabled
0/2 Disabled
0/3 Disabled
0/4 Disabled
0/5 Disabled
Switching Commands 501

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
0/6 Disabled
0/7 Disabled
0/8 Disabled
0/9 Disabled
0/10 Disabled
0/11 Disabled
0/12 Disabled
0/13 Disabled
0/14 Disabled
0/15 Disabled
0/16 Disabled
0/17 Disabled
show mmrp statistics
Use this command in Privileged EXEC mode to display statistical information about the
MMRP PDUs sent and received on the interface.
Format show mmrp statistics {summary | [unit/slot/port | all]}
Mode Privileged EXEC
The following statistics display when the summary keyword or unit/slot/port parameter
is used. Using the summary keyword displays global statistics. The unit/slot/port
parameter displays per-interface statistics.
Parameter Description
MMRP messages received Total number of MMRP messages received.
MMRP messages received with Total number of MMRP frames with bad headers received
bad header
MMRP messages received with Total number of MMRP frames with bad PDUs body formats received
bad format
MMRP messages transmitted Total number of MMRP frames that sent
MMRP messages failed to Total number of MMRP frames that failed to be transmitted
transmit
The following statistics display when the all keyword is used.
Parameter Description
Intf The interface associated with the rest of the data in the row.
Rx Total number of MMRP messages received.
Bad Header Total number of MMRP frames with bad headers received
Switching Commands 502

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
Bad Format Total number of MMRP frames with bad PDUs body formats received
Tx Total number of MMRP frames that sent
Tx Failed Total number of MMRP frames that failed to be transmitted
MVRP Commands
mvrp (Global Config)
Use this command in Global Configuration mode to enable MVRP. MVRP must also be
enabled on the individual interfaces.
Note: If MVRP is enabled on all devices and STP is disabled, statically
created VLANs are propagated to other devices. Each device ends up
with all the VLANs and connecting ports participating in all the VLANs.
This may cause loops in the network.
Default Disabled
Format mvrp
Mode Global Config
no mvrp (Global Config)
Use this command in Global Configuration mode to disable MVRP.
Format no mvrp
Mode Global Config
mvrp periodic state machine
Use this command in Global Configuration mode to enable the MVRP periodic state
machine.
Default Disabled
Format mvrp periodic state machine
Mode Global Config
Switching Commands 503

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no mvrp periodic state machine
Use this command in Global Configuration mode to disable the MVRP periodic state
machine.
Format no mvrp periodic state machine
Mode Global Config
mvrp (Interface Config)
Use this command in Interface Configuration mode to enable MVRP mode on the interface.
The port should be configured in trunk or general mode. MVRP can be enabled on physical
interfaces or LAG interfaces. When configured on a LAG member port, MVRP is
operationally disabled. Enabling MVRP on an interface automatically enabled dynamic VLAN
creation.
Default Disabled
Format mvrp
Mode Interface Config
no mvrp (Interface Config)
Use this command in Interface Configuration mode to disable MVRP mode on the interface.
Format no mvrp
Mode Interface Config
clear mvrp
Use this command in Privileged EXEC mode to clear the MVRP statistics of one or all
interfaces.
Format clear mvrp statistics [unit/slot/port | all]
Mode Privileged EXEC
Parameter Description
unit/slot/port If used with the unit/slot/port parameter, the command clears MVRP statistics for the given
interface.
all If the all parameter is specified, the command clears MVRP statistics for all the interfaces.
Switching Commands 504

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show mvrp
Use this command in Privileged EXEC mode to display the status of the MVRP mode.
Format show mvrp [summary | interface [unit/slot/port | all]]
Mode Privileged EXEC
Parameter Description
summary If the summary parameter is used, the command shows global MVRP information.
interface If the interface is specified as unit/slot/port, the command shows MVRP mode information for
that interface.
all If the interface is specified with the all parameter, the command shows a table containing MVRP
global mode and the mode for all interfaces.
Command example:
(NETGEAR Switch) #show mvrp summary
MVRP global state.............................. Disabled
MVRP Periodic State Machine state.............. Disabled
VLANs created via MVRP......................... 20-45, 3001-3050
Command example:
(NETGEAR Switch) #show mvrp interface 0/12
MVRP interface state........................... Enabled
VLANs declared................................. 20-45, 3001-3050
VLANs registered............................... none
show mvrp statistics
Use this command in Privileged EXEC mode to display MVRP statistics.
Format show mvrp statistics [summary | unit/slot/port | all]
Mode Privileged EXEC
Parameter Description
summary If used with the summary parameter, the command shows global MVRP statistics.
interface If the unit/slot/port is specified, the command shows MVRP statistics for that interface.
all If used with the all parameter, the command shows a table containing MVRP statistics for all
interfaces on which MVRP is enabled.
Switching Commands 505

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show mvrp statistics summary
MVRP messages received......................... 45
MVRP messages received with bad header......... 0
MVRP messages received with bad format......... 0
MVRP messages transmitted...................... 16
MVRP messages failed to transmit............... 0
MVRP Message Queue Failures.................... 0
Command example:
(NETGEAR Switch) #show mvrp statistics 0/12
Port........................................... 0/12
MVRP messages received......................... 21
MVRP messages received with bad header......... 0
MVRP messages received with bad format......... 0
MVRP messages transmitted...................... 8
MVRP messages failed to transmit............... 0
MVRP failed reservations....................... 0
Port-Channel/LAG (802.3ad) Commands
This section describes the commands you use to configure port-channels, which is defined in
the 802.3ad specification, and that are also known as link aggregation groups (LAGs). Link
aggregation allows you to combine multiple full-duplex Ethernet links into a single logical link.
Network devices treat the aggregation as if it were a single link, which increases fault
tolerance and provides load sharing. The LAG feature initially load shares traffic based upon
the source and destination MAC address. Assign the port-channel (LAG) VLAN membership
after you create a port-channel. If you do not assign VLAN membership, the port-channel
might become a member of the management VLAN which can result in learning and
switching issues.
A port-channel (LAG) interface can be either static or dynamic, but not both. All members of a
port channel must participate in the same protocols.) A static port-channel interface does not
require a partner system to be able to aggregate its member ports.
Note: If you configure the maximum number of dynamic port-channels
(LAGs) that your platform supports, additional port-channels that you
configure are automatically static.
Switching Commands 506
