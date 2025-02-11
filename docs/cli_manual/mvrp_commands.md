# mvrp_commands

Pages: 503-506

## Content

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
