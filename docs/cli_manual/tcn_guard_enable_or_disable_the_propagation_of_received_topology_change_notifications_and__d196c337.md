# tcn_guard_enable_or_disable_the_propagation_of_received_topology_change_notifications_and__d196c337

Pages: 407-413

## Content

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
