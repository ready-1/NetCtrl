# s_tack_mbr_p_latform_v1_p_latform_v1_s_tm_mismatch_1017158

Pages: 38-47

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show switch
M anagement S tandby P reconfig P lugged-in S witch Code
S W S witch S tatus M odel I D M odel I D S tatus Version
--- ---------- --------- ------------- ------------- ------------- -----------
1 S tack Mbr P latform v1 P latform v1 S TM Mismatch 10.17.15.8
2 M gmt Sw P latform v2 P latform v2 O K 10.17.15.8
If you specify a value for unit, the following information displays:
Term Definition
Management Indicates whether the switch is the Primary Management Unit, a stack member, or the
Status status is unassigned.
Hardware The hardware management preference of the switch. The hardware management
Management preference can be disabled or unassigned.
Preference
Admin The administrative management preference value assigned to the switch. This
Management preference value indicates how likely the switch is selected as the Primary
Preference Management Unit.
Switch Type The 32-bit numeric switch type.
Model Identifier The model identifier for this switch. The model identifier is a 32-character field that is
assigned by the device manufacturer to identify the device.
Switch Status The switch status. Possible values are OK, Unsupported, Code Mismatch, Config
Mismatch, or Not Present.
Switch Description The switch description.
Expected Code The expected firmware version.
Version
Detected Code The version of firmware that is running on this switch. If the switch is not present and
Version the data is from the preconfiguration, the firmware version is None.
Detected Code in The version of the firmware that is currently stored in flash memory on the switch. The
Flash firmware executes after the switch is reset. If the switch is not present and the data is
from the preconfiguration, the firmware version is None.
SFS Last Attempt The stack firmware synchronization status in the last attempt for the specified unit.
Status
Stack Template ID The ID of the stack template. For example: 3.
Stack Template The stack template description. For example: v1 and v2 Mix.
Description
Up Time The system up time.
Stacking Commands 38

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(Netgear Switch) #show switch 1
Switch............................ 1
Management Status................. Management Switch
Hardware Management Preference.... Unassigned
Admin Management Preference....... Unassigned
Switch Type....................... 0xd6064004
Preconfigured Model Identifier.... M4300-52G-PoE+
Plugged-in Model Identifier....... M4300-52G-PoE+
Switch Status..................... OK
Switch Description................ M4300-52G-PoE+ ProSafe 48-port Copper 1G PoE+ L3
Switch with 2-port 10G Copper and 2-port 10G Fiber
Detected Code in Flash............ 12.0.0.2
CPLD version...................... 0x1
SFS Last Attempt Status........... None
Serial Number..................... 4G115B5UF0026
Up Time........................... 2 days 3 hrs 24 mins 33 secs
show supported switchtype (for stack configuration)
Use this command to display information about all supported switch types or about a specific
switch type.
Format show supported switchtype [switchindex]
Modes User EXEC
Privileged EXEC
If you do not supply a value for switchindex, the following output displays:
Term Definition
Switch Index (SID) The index in the database of supported switch types. This index is used when you
preconfigure a member to be added to the stack.
Model Identifier The model identifier for the supported switch type.
Management The management preference value of the switch type.
Preference
Code Version The firmware load target identifier of the switch type.
If you supply a value for switchindex, the following output displays:
Term Definition
Switch Type The 32-bit numeric switch type for the supported switch.
Stacking Commands 39

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Model Identifier The model identifier for the supported switch type.
Switch Description The description for the supported switch type.
Stack Port Commands
This section describes the commands you use to view and configure stack port information.
stack-port
Use this command to set stacking for a specified port to either stack or ethernet mode.
Default stack
Format stack-port unit/slot/port {ethernet | stack}
Mode Stack Global Config
show stack-port
Use this command to display summary stack-port information for all interfaces.
Format show stack-port
Mode Privileged EXEC
For each interface:
Term Definition
Unit The unit number.
Interface The slot and port numbers.
Configured Stack Stack or Ethernet.
Mode
Running Stack Stack or Ethernet.
Mode
Link Status The status of the link.
Link Speed The speed (in Gbps) of the stack port link.
Stacking Commands 40

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show stack-port counters
Use this command to display summary data counter information for all interfaces.
Use the following optional keywords to specify the command output:
• number. The output displays for a specific unit in the stack. The value for number can be
from 1 to 8.
• all. The output displays for all units in the stack.
Format show stack-port counters [number | all]
Mode Privileged EXEC
Term Definition
Unit The unit number.
Interface The slot and port numbers.
Tx Data Rate The trashing data rate in megabits per second on the stacking port.
Tx Error Rate The platform-specific number of transmit errors per second.
Tx Total Error The platform-specific number of total transmit errors since power-up.
Rx Data Rate The received data rate in megabits per second on the stacking port.
Rx Error Rate The platform-specific number of received errors per second.
Rx Total Errors The platform-specific number of total received errors since power-up.
Link Flaps The number of up and down events for the link since the system bootup.
This example shows the stack ports and associated statistics of unit 2.
(NETGEAR Switch) #show stack-port counters 2
- -----------TX------------------- - -----------RX-------------- -------
D ata E rror D ata Error
R ate R ate T otal R ate R ate T otal Link
U nit Interface ( Mb/s) ( Errors/s) E rrors ( Mb/s) ( Errors/s) Errors Flaps
---- ----------- ---------- ----------- ---------- -------- ---------- -------- -------
2 0 /53 0 0 0 0 0 0 0
2 0 /54 0 0 0 0 0 0 0
2 0 /55 0 0 0 0 0 0 0
2 0 /56 0 0 0 0 0 0 0
Stacking Commands 41

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show stack-port diag
Note: This command is intended only for field application engineers (FAEs)
and developers.
Use this command to display front panel stacking diagnostics for each port. An FAE can
advise on the necessity to run this command and capture this information. In verbose mode,
the statistics and counters for RPC, transport, CPU, and transport RX/TX modules are
displayed.
Use the following optional keywords to specify the command output:
• number. The output displays for a specific unit in the stack. The value for number can be
from 1 to 8.
• all. The output displays for all units in the stack.
Format show stack-port diag [number | all] [verbose]
Mode Privileged EXEC
Term Definition
Unit The unit number.
Interface The slot and port numbers.
Diagnostic Entry1 80 character string used for diagnostics.
Diagnostic Entry2 80 character string used for diagnostics.
Diagnostic Entry3 80 character string used for diagnostics.
TBYT Transmitted bytes.
TPKT Transmitted packets.
TFCS Transmitted FCS error frame counter.
TERR Transmitted error (set by system) counter
RBYT Received bytes.
RPKT Received packets.
RFCS Received FCS error frame counter.
RFRG Received fragment counter.
RJBR Received jabber frame counter.
RUND Received undersized frame counter.
Stacking Commands 42

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
ROVR Received oversized frame counter.
RUNT Received RUNT frame counter.
Command example:
This example displays the stack ports and associated statistics of specified unit or all units.
(NETGEAR Switch) #show stack-port diag 1
1 - 0/53:
RBYT:27ed9a7b RPKT:bca1b TBYT:28a0739e TPKT:c93ee
RFCS:0 RFRG:0 RJBR:0 RUND:0 RUNT:0
TFCS:0 TERR:0
1 - 0/54:
RBYT:8072ed RPKT:19a66 TBYT:aecfb80 TPKT:66e4d
RFCS:6e RFRG:4414 RJBR:0 RUND:c19 RUNT:af029b1
TFCS:0 TERR:0
1 - 0/55:
RBYT:0 RPKT:0 TBYT:ae8 TPKT:23
RFCS:0 RFRG:0 RJBR:0 RUND:0 RUNT:0
TFCS:0 TERR:0
1 - 0/56:
RBYT:0 RPKT:0 TBYT:ae8 TPKT:23
RFCS:0 RFRG:0 RJBR:0 RUND:0 RUNT:0
TFCS:0 TERR:0
Command example:
This example displays a dump of the RPC, Transport (ATP, Next Hop, and RLink), and CPU
Transport Rx/Tx module statistics for Unit 2.
(NETGEAR Switch) #show stack-port diag 2 verbose
-----------------------------------------
HPC RPC statistics/counters from unit..2
-----------------------------------------
Registered Functions........................... 58
Client Requests.............................. 0
Server Requests................................ 0
Server Duplicate Requests...................... 0
Server Replies................................. 0
Client Remote Tx............................... 0
Client Remote Retransmit Count................. 0
Tx without Errors.............................. 0
Tx with Errors................................. 0
Stacking Commands 43

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Rx Timeouts.................................... 0
Rx Early Exits................................. 0
Rx Out of Sync................................. 0
No Buffer...................................... 0
Collect Sem Wait Count......................... 0
Collect Sem Dispatch Count..................... 0
-------------------------------------
RPC statistics/counters from unit..2
-------------------------------------
Client RPC Requests Count...................... 3
Client RPC Reply Count......................... 0
Client RPC Fail to xmit Count.................. 0
Client RPC Response Timedout Count............. 3
Client RPC Missing Requests.................... 0
Client RPC Detach/Remove Count................. 0
Client RPC Current Sequence Number............. 3
Server RPC Request Count....................... 0
Server RPC Reply Count......................... 0
Server RPC Processed Transactions.............. 0
Server RPC Received Wrong Version Req.......... 0
Server RPC No Handlers......................... 0
Server RPC Retry Transmit Count................ 0
Server RPC Repetitive Tx Errors................ 0
-------------------------------------
ATP statistics/counters from unit..2
-------------------------------------
Transmit Pending Count......................... 2
Current number of TX waits..................... 2
Rx transactions created........................ 145
Rx transactions freed.......................... 145
Rx transactions freed(raw)..................... 0
Tx transactions created........................ 290
BET Rx Dropped Pkts Count...................... 0
ATP Rx Dropped Pkts Count...................... 0
Failed to Add Key Pkt Count.................... 0
Source Lookup Failure Count.................... 0
Old Rx transactions Pkts drop Count............ 0
Nr of CPUs found in ATP communication.......... 2
-----------------------------------------------
CPU Transport statistics/counters from unit..2
-----------------------------------------------
State Initialization........................... Done
Rx Setup....................................... Done
Stacking Commands 44

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Tx Setup....................................... Done
Tx CoS[0] Reserve.............................. 100
Tx CoS[1] Reserve.............................. 100
Tx CoS[2] Reserve.............................. 100
Tx CoS[3] Reserve.............................. 100
Tx CoS[4] Reserve.............................. 60
Tx CoS[5] Reserve.............................. 40
Tx CoS[6] Reserve.............................. 20
Tx CoS[7] Reserve.............................. 0
Tx Pkt Pool Size............................... 200
Tx Available Pkt Pool Size..................... 198
Tx failed/error Count.......................... 0
Rx Pkt Pool Size............................... 8
------------------------------------------
Next Hop statistics/counters from unit..2
------------------------------------------
State Initialization........................... Done
Component Setup................................ Done
Thread Priority................................ 100
Rx Priority.................................... 105
Local CPU Key.................................. 00:24:81:d0:0f:c7
MTU Size....................................... 2048
Vlan Id........................................ 4094
CoS Id......................................... 7
Internal Priority for pkt transmission......... 7
Rx Pkt Queue Size.............................. 256
Tx Pkt Queue Size.............................. 64
Rx Pkt Dropped Count........................... 0
Tx Failed Pkt Count............................ 0
---------------------------------------
RLink statistics/counters from unit..2
---------------------------------------
State Initialization........................... Done
L2 Notify In Pkts.............................. 0
L2 Notify In Pkts discarded.................... 0
L2 Notify Out Pkts ............................ 0
L2 Notify Out Pkts discarded................... 0
Linkscan In Pkts............................... 0
Linkscan In Pkts discarded..................... 0
Linkscan Out Pkts ............................. 0
Linkscan Out Pkts discarded.................... 0
Auth/Unauth In Callbacks....................... 0
Auth/Unauth In Callbacks discarded............. 0
Auth/Unauth Out Callbacks...................... 0
Auth/Unauth Out Callbacks discarded............ 0
Stacking Commands 45

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
RX Tunnelling In Pkts.......................... 0
RX Tunnelling In Pkts discarded................ 0
RX Tunnelling Out Pkts......................... 0
RX Tunnelling Out Pkts discarded............... 0
OAM Events In.................................. 0
OAM Events In discarded........................ 0
OAM Events Out................................. 0
OAM Events Out discarded....................... 0
BFD Events In.................................. 0
BFD Events In discarded........................ 0
BFD Events Out................................. 0
BFD Events Out discarded....................... 0
Fabric Events In............................... 0
Fabric Events In discarded..................... 0
Fabric Events Out.............................. 0
Fabric Events Out discarded.................... 0
Scan Add Requests In........................... 0
Scan Del Requests In........................... 0
Scan Notify(Run Handlers) Out.................. 0
Scan Notify(Traverse Processing)............... 0
show stack-port stack-path
Use this command to display the route that a packet takes to reach its destination. This
command lets you display the stack path to see if an error or packets loss occurs.
Use the following optional keywords to specify the command output:
• source-unit. The output displays for a specific source unit in the stack. The value for
source-unit can be from 1 to 8.
• all. The output displays for all units in the stack.
• destination-unit. The output displays for a specific source unit in the stack. The
value for destination-unit can be from 1 to 8.
Format show stack-port stack-path [source-unit | all] [destination-unit]
Mode Privileged EXEC
Stacking Commands 46

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Stack Firmware Synchronization
Commands
Stack firmware synchronization (SFS) provides an automatic mechanism to synchronize the
firmware on all stack members whose firmware version differs from the version running on
the stack manager. This operation can result in either an upgrade or downgrade of firmware
on the mismatched stack member. However, this operation does not attempt to synchronize
the stack to the latest firmware in the stack.
boot auto-copy-sw (for stack firmware synchronization)
Use this command to enable stack firmware synchronization.
Default Disabled
Format boot auto-copy-sw
Mode Privileged EXEC
no boot auto-copy-sw
Use this command to disable stack firmware synchronization.
Format no boot auto-copy-sw
Mode Privileged EXEC
boot auto-copy-sw trap (for stack firmware synchronization)
Use this command to send SNMP traps related to stack firmware synchronization.
Default Enabled
Format boot auto-copy-sw trap
Mode Privileged EXEC
no boot auto-copy-sw trap
Use this command to disable sending SNMP traps related to stack firmware synchronization.
Format no boot auto-copy-sw trap
Mode Privileged EXEC
Stacking Commands 47
