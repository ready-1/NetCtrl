# 1 S tack Mbr P latform v1 P latform v1 S TM Mismatch 10.17.15.8

Pages: 38-58

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

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
boot auto-copy-sw allow-downgrade (for stack firmware synchronization)
Use this command to enable downgrading of the firmware version on the stack member if the
firmware version on the manager is older than the firmware version on the member.
Default Enabled
Format boot auto-copy-sw allow-downgrade
Mode Privileged EXEC
no boot auto-copy-sw allow-downgrade
Use this command to prevent downgrading of the firmware version on the stack member if
the firmware version on the manager is older than the firmware version on the member.
Format no boot auto-copy-sw allow-downgrade
Mode Privileged EXEC
show auto-copy-sw (for stack firmware synchronization)
Use this command to display the stack firmware synchronization configuration status.
Format show auto-copy-sw
Mode Privileged EXEC
Term Definition
Synchronization Shows whether the SFS feature is enabled.
SNMP Trap Status Shows whether the stack sends traps for SFS events
Allow Downgrade Shows wether the stack manager is permitted to downgrade the firmware version of a
stack member.
Nonstop Forwarding Commands for Stack
Configuration
You can describe a switch in terms of three semi-independent functions: the forwarding
plane, the control plane, and the management plane. The forwarding plane forwards data
packets. The forwarding plane is implemented in hardware. The control plane is the set of
protocols that determines how the forwarding plane must forward packets, which data
packets can be forwarded, and where the data packets must be forwarded to.
Stacking Commands 48

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Application software on the management unit functions as the control plane. The
management plane is also application software that runs on the management unit and that
provides interfaces, allowing you to configure and monitor the device.
Nonstop forwarding (NSF) allows the forwarding plane of stack units to continue to forward
packets while the control and management planes restart as a result of a power failure,
hardware failure, or software fault on the management unit.
You can also manually initiate a nonstop forwarding failover by issuing the initiate
failover command. If the management unit fails, traffic flows that enter and exit the stack
through physical ports on a unit other than the management unit continue with at most a
subsecond interruption.
To prepare the backup management unit for a failover, applications on the management unit
continuously checkpoint (that is, forward) information to the backup unit. Changes to the
running configuration are automatically copied to the backup unit. MAC addresses stay the
same across a nonstop forwarding failover so that neighbors do not need to relearn them.
When a nonstop forwarding failover occurs, the control plane on the backup unit starts from a
partially-initialized state and applies the checkpointed (that is, forwarded) information. While
the control plane is initializing, the stack cannot react to external changes, such as network
topology changes. When the control plane is fully operational on the new management unit,
the control plane ensures that the hardware state is updated as necessary. The control plane
failover time depends on the size of the stack, the complexity of the configuration, and the
speed of the CPU.
The management plane restarts when a failover occurs. Management connections must be
reestablished.
For NSF to be effective, adjacent networking devices must not reroute traffic around the
restarting device.
The switch uses three protocol techniques to prevent traffic from being rerouted:
• A protocol can distribute a part of its control plane to stack units so that the protocol can
give the appearance that it is still functional during the restart. Spanning tree and port
channels use this technique.
• A protocol can enlist the cooperation of its neighbors through a technique known as
graceful restart. OSPF uses graceful restart if it is enabled (see “IP Event Dampening
Commands on page752).
• A protocol can simply restart after the failover if neighbors react slowly enough that they
do not detect the outage. The IP multicast routing protocols are a good example of this
behavior.
To take full advantage of nonstop forwarding, layer 2 connections to neighbors must be
configured over port channels that span two or more stack units and layer 3 routes must be
configured over ECMP routes with next hops over physical ports on two or more units. The
hardware can quickly move traffic flows from port channel members or ECMP paths on a
failed unit to a surviving unit.
Stacking Commands 49

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
nsf (Stack Global Config)
Use this command to enable nonstop forwarding on the stack. When nonstop forwarding is
enabled, if the management unit of a stack fails, the backup unit takes over as the master
without clearing the hardware tables of any of the surviving units. Data traffic continues to be
forwarded in hardware while the management functions initialize on the backup unit.
NSF is enabled by default on platforms that support it. You can disable NSF to redirect the
CPU resources that are consumed by data checkpointing (that is, data forwarding).
If a unit that does not support NSF is connected to the stack, NSF is disabled on all stack
members. If a unit that does not support NSF is disconnected from the stack, all other units
do support NSF, and NSF is administratively enabled, NSF operation resumes.
Default Enabled
Format nsf
Mode Stack Global Config
no nsf
Use this command to disable nonstop forwarding on the stack.
Format no nsf
Mode Stack Global Config
show nsf (for stack configuration)
Use this command to display global and per-unit information for the nonstop forwarding
configuration on the stack.
Format show nsf
Mode Privileged EXEC
Term Definition
NSF Administrative Indicates whether nonstop forwarding is administratively enabled or disabled. The
Status default is Enabled.
NSF Operational Status Indicates whether NSF is enabled on the stack.
Stacking Commands 50

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Last Startup Reason The type of activation that caused the software to start the last time:
• “Power-On” means that the switch rebooted. A reboot can be caused by a
power cycle or an administrative “Reload” command.
• “Administrative Move” means that someone issued the movemanagement
command for the stand-by manager to take over.
• “Warm-Auto-Restart” means that the primary management card restarted
because of a failure, and the system executed a nonstop forwarding failover.
• “Cold-Auto-Restart” means that the system switched from the active manager
to the backup manager and was unable to maintain user data traffic. This is
usually caused by multiple failures occurring in a short period.
Time Since Last The time since the current management unit became the active management unit.
Restart Time
Restart in progress Indicates whether a restart is in progress.
Warm Restart Ready Indicates whether the system is ready to perform a nonstop forwarding failover
from the management unit to the backup unit.
Copy of Running Indicates whether the running configuration on the backup unit includes all
Configuration to changes made on the management unit. Displays as Current or Stale.
Backup Unit: Status
Time Since Last Copy The time when the running configuration was last copied from the management
unit to the backup unit.
Time Until Next Copy The number of seconds until the running configuration is copied to the backup
unit. This line only appears when the running configuration on the backup unit is
Stale.
NSF Support (Per Unit Indicates whether a unit supports NSF.
Status Parameter)
initiate failover (for stack configuration)
Use this command to force the backup unit to take over as the management unit and perform
a “warm restart” of the stack. On a warm restart, the backup unit becomes the management
unit without clearing its hardware tables (on a cold restart, hardware tables are cleared).
Applications apply checkpointed data (that is, forwarded data) from the former management
unit. The original management unit reboots. If the system is not ready for a warm restart, for
example because no backup unit was elected or one or more members of the stack do not
support nonstop forwarding, the command fails with a warning message.
The movemanagement command (see movemanagement (Stack Global Config) on
p age29) also transfers control from the current management unit. However, the hardware is
cleared and all units reinitialize.
Default None
Format initiate failover
Mode Stack Global Config
Stacking Commands 51

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show checkpoint statistics (for stack configuration)
Use this command to display general information about the checkpoint service operation.
Format show checkpoint statistics
Mode Privileged EXEC
Term Description
Messages The number of checkpoint messages that are transmitted to the backup unit.
Checkpointed Range: Integer. Default: 0
Bytes The number of bytes transmitted to the backup unit. Range: Integer. Default: 0
Checkpointed
Time Since The number of days, hours, minutes and seconds since the counters were reset to
Counters Cleared zero. The counters are cleared when a unit becomes manager or when you issue the
clear checkpoint statistics command.
Range: Time Stamp. Default: 0d00:00:00
Checkpoint The average number of checkpoint messages per second. The average is computed
Message Rate over the period since the counters were cleared. Range: Integer. Default: 0
Average
Last 10-second The average number of checkpoint messages per second in the last 10-second
Message Rate interval. This average is updated once every 10 seconds. Range: Integer. Default: 0
Average
Highest 10-second The highest rate recorded over a 10-second interval since the counters were cleared.
Message Rate Range: Integer. Default: 0
Command example:
(Switch)#show checkpoint statistics
Messages Checkpointed.....................6708
Bytes Checkpointed........................894305
Time Since Counters Cleared...............3d 01:05:09
Checkpoint Message Rate Average...........0.025 msg/sec
Last 10-second Message Rate Average.......0 msg/sec
Highest 10-second Message Rate............8 msg/sec
clear checkpoint statistics (for stack configuration)
Use this command to clear the statistics for the checkpointing process.
Format clear checkpoint statistics
Mode Privileged EXEC
Stacking Commands 52

Management Commands

This chapter describes the management commands.
The chapter contains the following sections:
• Configure the Switch Management CPU
• CPU Queue Commands
• Management Interface Commands
• IPv6 Management Commands
• Console Port Access Commands
• Telnet Commands
• Secure Shell Commands
• Management Security Commands
• Management Access Control List Commands
• Hypertext Transfer Protocol Commands
• Access Commands
• User Account Commands
• SNMP Commands
• RADIUS Commands
• TACACS+ Commands
• Configuration Scripting Commands
• Prelogin Banner, System Prompt, and Host Name Commands
• OpenFlow Commands
• Cloud Managed Commands
• Application Commands
The commands in this chapter are in one of three functional groups:
• Show commands. Display switch settings, statistics, and other information.
• Configuration commands. Configure features and options of the switch. For every
configuration command, there is a show command that displays the configuration setting.
• Clear commands. Clear some or all of the settings to factory defaults.

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Configure the Switch Management CPU
To manage the switch over the web management interface or Telnet, you must assign an IP
address to the switch management CPU. You can accomplish this task through CLI
commands or you can use the ezconfig tool, which simplifies the task. The tool lets you
configure the following settings:
• The administrator user password and administrator-enable password
• The management CPU IP address and network mask
• The system name and location information
The tool is interactive and uses questions to guide you through the configuration steps. At the
end of the configuration session, the tool lets you save the information. To see which
information was changed by the ezconfig tool after a configuration session, issue the show
running-config command.
ezconfig
This command sets the IP address, subnet mask, and gateway of the switch. The IP address
and the gateway must be on the same subnet.
Format ezconfig
Mode Privileged EXEC
(NETGEAR Switch) #ezconfig
EZ Configuration Utility
--------------------------------
Hello and Welcome!
This utility will walk you thru assigning the IP address for the switch
management CPU. It will allow you to save the changes at the end. After
the session, simply use the newly assigned IP address to access the Web
GUI using any public domain Web browser.
Admin password is not defined.
D o y ou w ant t o a ssign t he a dmin p assword ( password l ength m ust b e i n r ange o f 8-64
characters) (Y/N/Q)? y
Enter new password:********
Confirm new password:********
The 'enable' password required for switch configuration via the command
line interface is currently not configured.
D o y ou w ant t o a ssign i t ( password l ength m ust b e i n r ange o f 8-64 characters) (Y/N/Q)?
y
Management Commands 54

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Enter new password:********
Confirm new password:********
Current IPv4 Management Interface: vlan 1
Do you want to set new Management VLAN ID (Y/N/Q)?y
VLAN ID: 1
Assigning an IPv4 address to your switch management
Current IPv4 Address Configuration
----------------------------------
Management VLAN ID: vlan 1
IPv4 Address Assignment Mode: None
IPv4 Address: 0.0.0.0
Subnet Mask: 0.0.0.0
Gateway: 0.0.0.0
Routing Mode: Enable
IPv4 address is not assigned. What do you want to do?
C - Configure IPv4 address manually.
D - Assign IPv4 address for the switch using DHCP Mode(current IPv4 address will be
lost).
N - Skip this option and go to the next question.
Q - Quit.
? - Help.
(C/D/N/Q/?)? c
IPv4 Address: 192.168.1.1
Network Mask: 255.255.255.0
Gateway: 192.168.254
Incorrect input! Gateway must be a valid IP address.
Try again (Y/N/Q)? y
Gateway: 192.168.1.254
Do you want to enable global routing (Y/N)?y
Current IPv6 Management Interface: (not configured)
Do you want to set new IPv6 Management VLAN ID (Y/N/Q)?y
VLAN ID: 1
Assigning management IPv6 address.
Current IPv6 Address Configuration
----------------------------------
IPv6 Address: fe80::abd:43ff:fe71:73c0/64
IPv6 Current state: TENT
Address DHCP Mode: Disabled
Address Autoconfigure Mode: Disabled
EUI64 : Enabled
Management Commands 55

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Routing Mode: Enable
IPv6 address has been assigned manually. What do you want to do?
C - Add IPv6 address.
D - Assign IPv6 address for the switch using DHCP Mode.
A - Assign IPv6 address for the switch using Auto Mode.
N - Skip this option and go to the next question.
Q - Quit.
? - Help.
(C/D/A/N/Q/?)? c
IPv6 Address: 2001:1::1
IPv6 Prefix-length: 64
IPv6 EUI64 flag (Y/N): n
IPv6 Gateway: 2001:1::fffe
Current Out of Band(service port) IPv4 Address Configuration
--------------------------------
IP Address Assignment Mode: DHCP
IP Address: 172.26.2.104
Subnet Mask: 255.255.255.0
Default Router: 172.26.2.1
IPv4 address will be assigned automatically by the DHCP server in your network. You
can disable DHCP mode and use static(fixed) IPv4 address. If fixed IPv4 Address Mode
is selected, DHCP Protocol Mode will be disabled, and you will be prompted to
set the values for the four fields above.
Do you want to assign IPv4 address manually? (Y/N/Q/?) y
IPv4 Address: 172.26.2.1
Network Mask: 255.255.255.0
Gateway: 172.26.2.254
Current Out of Band(Serviceport) IPv6 Address Configuration
--------------------------------
Service port IPv6 Address Mode: None
IPv6 Administrative Mode: Enabled
Service port IPv6 Address Mode autoconfigure: Disabled
IPv6 Address: fe80::abd:43ff:fe71:73be/64
Service port IPv6 address gateway:
EUI Flag: False
IPv6 address has been assigned manually. What do you want to do?
A - Assign IPv6 address for the switch using Auto Mode.
D - Assign IPv6 address for the switch using DHCP Mode.
Management Commands 56

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
G - Assign IPv6 Gateway.
C - Add IPv6 address.
N - Skip this option and go to the next question.
Q - Quit.
? - Help.
(A/D/G/C/N/Q/?)? c
Current Management Interface Configuration
--------------------------------
Management Interface: L3 Management VLAN
Current management interface is L3 Management VLAN. What do you want to do?
O - Change to Out of Band port(service port).
V - Change to L3 Management VLAN.
N - Skip this option and go to the next question.
Q - Quit.
? - Help.
(O/V/N/Q/?)?n
Assigning System Name, System Location and System Contact to your switch management
Current Configuration
--------------------------------
System Name:
System Location:
System Contact:
Do you want to assign switch name and location information? (Y/N/Q)
CPU Queue Commands
You can send all packets with a specified destination address to a higher priority queue (5)
than the default queue for data packets and unicast packets to the CPU.
ip cpu-priority
This command sends all packets with a specified destination IPv4 address to a higher priority
queue (5) than the default queue for data packets and unicast packets to the CPU.
Format ip cpu-priority ip-address
Mode Privileged EXEC
Management Commands 57

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip cpu-priority
This command removes all packets with a specified destination IPv4 address from the higher
priority queue.
Format no ip cpu-priority ip-address
Mode Privileged EXEC
ipv6 cpu-priority
The command allows all packets with a specified destination IPv6 address into a higher
priority queue (5) than the default queue for data packets and unicast packets to the CPU.
Format ip cpu-priority ipv6-address
Mode Privileged EXEC
no ipv6 cpu-priority
This command removes all packets with a specified destination IPv6 address from the higher
priority queue.
Format no ip cpu-priority ipv6-address
Mode Privileged EXEC
Management Interface Commands
This section describes the commands you use to configure a logical IPv4 interface for
management access.
enable (Privileged EXEC access)
This command gives you access to the Privileged EXEC mode. From the Privileged EXEC
mode, you can configure the network interface.
Format enable
Mode User EXEC
Management Commands 58
