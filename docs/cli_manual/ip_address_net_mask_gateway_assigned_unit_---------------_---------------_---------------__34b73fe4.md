# ip_address_net_mask_gateway_assigned_unit_---------------_---------------_---------------__34b73fe4

Pages: 317-324

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
For write core test, the destination file name is used for the TFTP test. Optionally, you
can specify the destination file name when the protocol is configured as TFTP.
Default None
Format write core [test [dest_file_name]]
Mode Privileged EXEC
debug exception
Use this command to display core dump features support.
Default None
Format debug exception
Mode Privileged EXEC
show exception
Use this command to display the configuration parameters for generating a core dump file.
Default None
Format show exception
Mode Privileged EXEC
Command example:
(Netgear Switch) #show exception
Coredump file name............................. core
Coredump filename uses hostname................ False
Coredump filename uses time-stamp.............. TRUE
NFS mount point................................
TFTP server IP.................................
FTP server IP..................................
FTP user name..................................
FTP password...................................
File path......................................
Protocol....................................... usb
Switch-chip-register........................... False
Compression mode............................... TRUE
Stack IP Address Protocol...................... dhcp
Stack IP Address:
IP Address Net Mask Gateway Assigned Unit
--------------- --------------- --------------- ---------------
Utility Commands 317

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
mbuf
Use this command to configure memory buffer (MBUF) threshold limits and generate
notifications when MBUF limits have been reached.
Format mbuf {falling-threshold | rising threshold | severity}
Mode Global Config
Field Description
Rising Threshold The percentage of the memory buffer resources that, when exceeded for the configured rising
interval, triggers a notification. The range is 1 to 100. The default is 0 (disabled).
Falling Threshold The percentage of memory buffer resources that, when usage falls below this level for the
configured interval, triggers a notification. The range is 1 to 100. The default is 0 (disabled).
Severity The severity level at which Mbuf logs messages. The range is 1 to 7. The default is 5
(L7_LOG_SEVERITY_NOTICE).
show mbuf
Use this command to display the memory buffer (MBUF) Utilization Monitoring parameters.
Format show mbuf
Mode Privileged EXEC
Field Description
Rising Threshold The percentage of the memory buffer resources that, when exceeded for the configured rising
interval, triggers a notification. The range is 1 to 100. The default is 0 (disabled).
Falling Threshold The percentage of memory buffer resources that, when usage falls below this level for the
configured interval, triggers a notification. The range is 1 to 100. The default is 0 (disabled).
Severity The severity level.
show mbuf total
Use this command to display memory buffer (MBUF) information.
Format show mbuf total
Mode Privileged EXEC
Field Description
Mbufs Total Total number of message buffers in the system.
Mbufs Free Number of message buffers currently available.
Mbufs Rx Used Number of message buffers currently in use.
Utility Commands 318

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Description
Total Rx Norm Number of times the system tried to allocate a message buffer allocation of class RX Norm.
Alloc Attempts
Total Rx Mid2 Alloc Number of times the system tried to allocate a message buffer allocation of class RX Mid2.
Attempts
Total Rx Mid1 Alloc Number of times the system tried to allocate a message buffer allocation of class RX Mid1.
Attempts
Total Rx Mid0 Alloc Number of times the system tried to allocate a message buffer allocation of class RX Mid0.
Attempts
Total Rx High Alloc Number of times the system tried to allocate a message buffer allocation of class RX High.
Attempts
Total Tx Alloc Number of times the system tried to allocate a message buffer allocation of class TX.
Attempts
Total Rx Norm Number of message buffer allocation failures for RX Norm class of message buffer.
Alloc Failures
Total Rx Mid2 Alloc Number of message buffer allocation failures for RX Mid2 class of message buffer.
Failures
Total Rx Mid1 Alloc Number of message buffer allocation failures for RX Mid1 class of message buffer.
Failures
Total Rx Mid0 Alloc Number of message buffer allocation failures for RX Mid0 class of message buffer.
Failures
Total Rx High Alloc Number of message buffer allocation failures for RX High class of message buffer.
Failures
Total Tx Alloc Number of message buffer allocation failures for TX class of message buffer.
Failures
show msg-queue
Use this command to display the message queues.
Default None
Format show msg-queue
Mode Privileged Exec
session start
Use this command to initiate a console session from the stack master to another unit in the
stack, or from a member unit to a manager or another member unit. During the session, you
can issue troubleshooting and debugging commands on the member unit, and the output
displays the relevant information from the member unit specified in the session. Commands
are displayed on the member unit using the user help option ?.
Utility Commands 319

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Use the unit keyword and unit-number parameter to specify the unit that must connect to
the stack master.
Use the manager keyword to connect directly to the manager unit from any member unit
without entering the manager’s unit number.
Default Disabled
Format session start {unit unit-number | manager}
Mode Privileged Exec
session stop
Use this command to terminate a session that was started with the session start
command. The session can be from a manager to a member, from member to a member, or
from a member to a manager.
Use the unit keyword and unit-number argument to specify the unit that must disconnect
from the stack master.
Use the manager keyword to disconnect directly from the manager unit from any member
unit without entering the manager’s unit number.
Default Disabled
Format session stop {unit unit-number | manager}
Mode Global Config
sw reset
Use this command to reboot the switch after a serious error occurred.
Default Enabled
Format sw reset
Mode Global Config
no sw reset
Use this command to prevent the switch from rebooting after a serious error occurred.
Preventing the switch from rebooting can be useful for the purpose of debugging.
Format no sw reset
Mode Global Config
Utility Commands 320

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show sw reset
Use this command to show whether the sw reset command is enabled.
Format show sw reset
Mode User EXEC
Support Mode Commands
Support mode is hidden and available when the techsupport enable command is
executed. The tech support mode is disabled by default. Configurations related to support
mode are shown in the show tech-support command. They can be persisted by using
the command save in support mode. Support configurations are stored in a separate binary
config file, which cannot be uploaded or downloaded.
techsupport enable
Use this command to allow access to Support mode.
Default Disabled
Format techsupport enable
Mode Privileged Exec
console
Use this command to enable the display of support debug for this session.
Default Disabled
Format console
Mode Support
save
Use this command to save the trace configuration to non-volatile storage.
Format save
Mode Support
snapshot ospf
Use this command in Support mode to dump a set of OSPF debug information to capture the
current state of OSPF. The output is written to the console and can be extensive.
Utility Commands 321

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
snapshot routing
Use this command in Support mode to dump a set of routing debug information to capture the
current state of routing on the switch. The output is written to the console and can be
extensive.
Format snapshot routing
Mode Support
snapshot multicast
Use this command in Support mode to dump a set of IP multicast debug information to
capture the current state of multicast on the switch. The output is written to the console and
can be extensive.
Format snapshot multicast
Mode Support
snapshot system
Use this command in Support mode to dump a set of system debug information to capture
the current state of the device. The output is written to the console and can be extensive.
Format snapshot system
Mode Support
telnetd
Use this command in Support mode to start or stop the Telnet daemon on the switch.
Format telnetd {start | stop}
Mode Support
Cable Test Command
The cable test feature enables you to determine the cable connection status on a selected
port.
Note: The cable test feature is supported only for copper cable. It is not
supported for optical fiber cable.
Utility Commands 322

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If the port has an active link while the cable test is run, the link can go down for the duration
of the test.
cablestatus
This command returns the status of the specified port.
Format cablestatus unit/slot/port
Mode Privileged EXEC
Field Description
Cable Status One of the following statuses is returned:
• Normal. The cable is working correctly.
• Open. The cable is disconnected or there is a faulty connector.
• Short. There is an electrical short in the cable.
• Cable Test Failed. The cable status could not be determined. The cable may in fact be
working.
Cable Length If this feature is supported by the PHY for the current link speed, the cable length is displayed as a
range between the shortest estimated length and the longest estimated length. Note that if the link is
down and a cable is attached to a 10/100 Ethernet adapter, then the cable status may display as
Open or Short because some Ethernet adapters leave unused wire pairs unterminated or grounded.
Unknown is displayed if the cable length could not be determined.
Power Management Commands
power auto-rebalance
Note: This command applies to switch model M4300-96X only.
This command enables the switch to automatically readjust the power allocation to the ports
on an APM408P port card if the power budget changes or powered devices (PD) change. If
the power budget is insufficient, ports with a lower priority (that is, ports with a higher port
number) are automatically shut down and ports with a higher priority (that is, ports with a
lower port number) are powered. If a PoE port is shut down, slot priority is also taken into
consideration. Lower-numbered slots receive higher priority than higher-numbered slots. For
example, slot 1 receives higher priority than slot 2, which, in turn, receives higher priority than
slot 3, and so on through slot 6, which receives the lowest slot priority.
Default Enabled
Format power auto-rebalance
Mode Global Config
Utility Commands 323

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no power auto-rebalance
Note: This command applies to switch model M4300-96X only.
This command prevents the switch from automatically readjusting the power allocation to the
ports on an APM408P port card
Format no power auto-rebalance
Mode Global Config
power redundancy
This command enables the N+1 power redundancy feature on a switch with a dual PSU
configuration. If this feature is enabled, only one PSU provides 56V PoE power to the unit. If
the PSU fails, the redundant PSU seamlessly takes over the supply of 56V PoE power to the
unit. If this command is disabled, N+1 is also disabled and both PSUs provide 56V PoE
power to the unit at the same time. In this situation, the PoE budget for the unit increases.
The unit-number argument specifies the PSU in the switch.
Default Disabled
Format power redundancy [unit-number]
Mode Global Config
Note: If the total available power minus the total consumed power is less
than what one PSU can supply, the switch does not enable the N+1
feature. Instead, it generates the following error message on the
console and in the logging buffer:
Not enough power to enable N+1 feature. Total
available power: <X>. Total consumption power: <Y>
no power redundancy
This command disables the N+1 power redundancy feature.
Format no power redundancy
Mode Global Config
Utility Commands 324
