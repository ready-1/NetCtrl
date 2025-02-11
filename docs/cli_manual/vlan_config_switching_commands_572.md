# vlan_config_switching_commands_572

Pages: 572-572

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
set igmp fast-leave auto-assignment
This command globally enables or disables the automatic assignment of fast-leave for all
ports and LAGs.
On the switch, Rapid Spanning Tree Protocol (RSTP) is the default network protocol for STP.
RSTP functions at port level. Each port starts up as an edge port and functions in that
capacity until it receives an RSTP BPDU from a neighbor device. An edge port does not
participate in STP and is meant to be connected to end devices or hosts on which STP is not
enabled. However, if a port receives an RSTP BPDU, the port stops functioning as an edge
port and starts participating in STP.
Consequently, as long as the port functions as an edge port, IGMP Snooping fast-leave is
enabled. If a port receives an RSTP BPDU and stops functioning as an edge port, IGMP
Snooping fast-leave is also disabled on the port.
The set igmp fast-leave auto-assignment command controls the fast-leave
operational state, but not the configured value. On a port, a dynamically-assigned operational
value for fast-leave overrides a configured value for fast-leave.
The set igmp fast-leave auto-assignment command does the following:
• It overrides the configured port level fast-leave mode, which is disabled by default.
• It does not modify the VLAN configuration for fast-leave mode.
Between a port and a VLAN that is configured for that port, IGMP Snooping gives
precedence to the fast-leave mode for the port.
You can display the operational status of IGMP Snooping fast-leave at port level by using the
show igmpsnooping fast-leave command (see show igmpsnooping fast-leave on
p age580).
Default Enabled
Format set igmp fast-leave auto-assignment
Mode Global Config
set igmp groupmembership-interval
This command sets the IGMP group membership interval time on a VLAN, one interface, a
range of interfaces, or all interfaces. The group membership interval time is the amount of
time in seconds that a switch waits for a report from a particular group on a particular
interface before deleting the interface from the entry. This value must be greater than the
IGMPv3 maximum response time value. The range is 2 to 3600 seconds.
Default 260 seconds
Format set igmp groupmembership-interval [vlan-id] seconds
Mode Interface Config
Global Config
VLAN Config
Switching Commands 572
