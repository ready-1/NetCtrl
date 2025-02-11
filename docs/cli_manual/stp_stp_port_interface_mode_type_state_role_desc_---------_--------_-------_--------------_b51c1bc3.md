# stp_stp_port_interface_mode_type_state_role_desc_---------_--------_-------_--------------_b51c1bc3

Pages: 415-420

## Content

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
