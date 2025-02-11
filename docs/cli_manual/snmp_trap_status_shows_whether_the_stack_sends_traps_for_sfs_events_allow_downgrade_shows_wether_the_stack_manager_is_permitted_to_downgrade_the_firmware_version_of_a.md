# snmp_trap_status_shows_whether_the_stack_sends_traps_for_sfs_events_allow_downgrade_shows_wether_the_stack_manager_is_permitted_to_downgrade_the_firmware_version_of_a

Pages: 48-53

## Content

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
