# root_id_priority_32768

Pages: 403-406

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
