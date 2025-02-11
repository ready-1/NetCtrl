# eee

Pages: 342-357

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
1/0/4 Disabled Inactive Disabled
1/0/5 Disabled Inactive Disabled
1/0/6 Disabled Inactive Disabled
1/0/7 Disabled Inactive Disabled
1/0/8 Disabled Inactive Disabled
1/0/9 Disabled Inactive Disabled
If you specify the port, the command displays the information in the following table.
Term Definition
Energy Detect
Energy-detect admin mode Energy-detect mode is enabled or disabled
Energy-detect operational status Energy detect mode is currently active or inactive. The energy-detect mode may be
administratively enabled, but the operational status may be inactive. The possible
reasons for the status are described below.
Reason for Energy-detect current The energy detect mode may be administratively enabled, but the operational
operational status status may be inactive for one of the following reasons:
• Port is currently operating in the fiber mode
• Link is up.
• Admin Mode Disabled
If the energy-detect operational status is active, this field displays No energy
detected.
EEE
EEE Admin Mode EEE Admin Mode is enabled or disabled.
Transmit Idle Time It is the time for which condition to move to LPI state is satisfied, at the end of which
MAC TX transitions to LPI state. The Range is (0 to 429496729). The Default value
is 0
Transmit Wake Time It is the time for which MAC / switch has to wait to go back to ACTIVE state from LPI
state when it receives packet for transmission. The Range is (0 to 65535).The
Default value is 0.
Rx Low Power Idle Event Count This field is incremented each time MAC RX enters LP IDLE state. Shows the total
number of Rx LPI Events since EEE counters are last cleared.
Rx Low Power Idle Duration (Sec) This field indicates duration of Rx LPI state in 10 s increments. Shows the total
duration of Rx LPI since the EEE counters are last cleared.
Tx Low Power Idle Event Count This field is incremented each time MAC TX enters LP IDLE state. Shows the total
number of Tx LPI Events since EEE counters are last cleared.
Rx Low Power Idle Duration (Sec) This field indicates duration of Tx LPI state in 10 s increments. Shows the total
duration of Tx LPI since the EEE counters are last cleared.
Tw_sys_tx (Sec) Integer that indicates the value of Tw_sys that the local system can support. This
value is updated by the EEE DLL Transmitter state diagram.
Utility Commands 342

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Tw_sys Echo (Sec) Integer that indicates the remote system’s Transmit Tw_sys that was used by the
local system to compute the Tw_sys that it wants to request from the remote
system.
Tw_sys_rx (Sec) Integer that indicates the value of Tw_sys that the local system requests from the
remote system. This value is updated by the EEE Receiver L2 state diagram.
Tw_sys_rx Echo (Sec) Integer that indicates the remote systems Receive Tw_sys that was used by the
local system to compute the Tw_sys that it can support.
Fallback Tw_sys (Sec) Integer that indicates the value of fallback Tw_sys that the local system requests
from the remote system.
Remote Tw_sys_tx (Sec) Integer that indicates the value of Tw_sys that the remote system can support.
Remote Tw_sys Echo (Sec) Integer that indicates the value Transmit Tw_sys echoed back by the remote
system.
Remote Tw_sys_rx (Sec) Integer that indicates the value of Tw_sys that the remote system requests from the
local system.
Remote Tw_sys_rx Echo (Sec) Integer that indicates the value of Receive Tw_sys echoed back by the remote
system.
Remote Fallback Tw_sys (Sec) Integer that indicates the value of fallback Tw_sys that the remote system is
advertising.
Tx_dll_enabled Initialization status of the EEE transmit Data Link Layer management function on
the local system.
Tx_dll_ready Data Link Layer ready: This variable indicates that the TX system initialization is
complete and is ready to update/receive LLDPDU containing EEE TLV. This
variable is updated by the local system software.
Rx_dll_enabled Status of the EEE capability negotiation on the local system.
Rx_dll_ready Data Link Layer ready: This variable indicates that the RX system initialization is
complete and is ready to update/receive LLDPDU containing EEE TLV. This
variable is updated by the local system software.
Cumulative Energy Saving Estimated Cumulative energy saved on this port in (Watts × hours) due to all green
modes enabled
Time Since Counters Last Cleared Time Since Counters Last Cleared (since the time of power up, or after the clear
eee statistics command is executed)
Command example:
The following example shows that the system supports all green Ethernet features:
(NETGEAR Switch) #show green-mode 1/0/1
Energy Detect Admin Mode.................... Enabled
Operational Status....................... Active
Reason................................... No Energy Detected
Auto Short Reach Admin Mode................. Enabled
Utility Commands 343

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Forced Short Reach Admin Mode............... Enabled
Operational Status....................... Active
Reason................................... Forced
EEE Admin Mode.............................. Enabled
Transmit Idle Time....................... 0
Transmit Wake Time....................... 0
Rx Low Power Idle Event Count............ 0
Rx Low Power Idle Duration (uSec)........ 0
Tx Low Power Idle Event Count............ 0
Tx Low Power Idle Duration (uSec)........ 0
Tw_sys_tx (usec)......................... XX
Tw_sys_tx Echo(usec)..................... XX
Tw_sys_rx (usec)......................... XX
Tw_sys_tx Echo(usec)..................... XX
Fallback Tw_sys (usec)................... XX
Remote Tw_sys_tx (usec).................. XX
Remote Tw_sys_tx Echo(usec).............. XX
Remote Tw_sys_rx (usec).................. XX
Remote Tw_sys_tx Echo(usec).............. XX
Remote fallback Tw_sys (usec)............ XX
Tx DLL enabled........................... Yes
Tx DLL ready............................. Yes
Rx DLL enabled........................... Yes
Rx DLL ready............................. Yes
Cumulative Energy Saving (W * H).......... XX
Time Since Counters Last Cleared......... 1 day 20 hr 47 min 34 sec
clear green-mode statistics
Use this command to clear the following Green Ethernet mode statistics:
• EEE LPI event count and LPI duration
• EEE LPI history table entries
• Cumulative power-savings estimates
You can clear the statistics for a specified port or for all ports.
Utility Commands 344

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: Executing clear eee statistics clears only the EEE Transmit,
Receive LPI event count, LPI duration, and Cumulative Energy
Savings Estimates of the port. Other status parameters that display
after executing show green-mode (see show green-mode on
p age340) retain their data.
Format clear green-mode statistics {unit/slot/port | all}
Mode Privileged EXEC
show green-mode eee-lpi-history
Use this command to display interface green-mode EEE LPI history.
Format green-mode eee-lpi-history interface unit/slot/port
Mode Privileged EXEC
Term Definition
Sampling Interval Interval at which EEE LPI statistics is collected.
Total No. of Samples to Keep Maximum number of samples to keep.
Percentage LPI time per switch Percentage of total time spent in LPI mode by all port in a switch when compared to
total time since reset.
Sample No. Sample Index.
Sample Time Time since last reset.
%time spent in LPI mode since last Percentage of time spent in LPI mode on this port when compared to sampling
sample interval.
%time spent in LPI mode since last Percentage of total time spent in LPI mode on this port when compared to time since
reset reset.
Command example:
The following example shows that the system has the EEE feature enabled:
(NETGEAR Switch) #show green-mode eee-lpi-history interface 1/0/1
Sampling Interval (sec)........................ 30
Total No. of Samples to Keep................... 168
Percentage LPI time per Stack.................. 29
Percentage of Percentage of
Sample Time Since Time spent in Time spent in
No. The Sample LPI mode since LPI mode since
Was Recorded last sample last reset
Utility Commands 345

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
------ -------------------- -------------- --------------
10 0d:00:00:13 3 2
9 0d:00:00:44 3 2
8 0d:00:01:15 3 2
7 0d:00:01:46 3 2
6 0d:00:02:18 3 2
5 0d:00:02:49 3 2
4 0d:00:03:20 3 2
3 0d:00:03:51 3 1
2 0d:00:04:22 3 1
1 0d:00:04:53 3 1
Remote Monitoring Commands
Remote Monitoring (RMON) is a method of collecting a variety of data about network traffic.
RMON supports 64-bit counters (RFC 3273) and High Capacity Alarm Table (RFC 3434).
Note: There is no configuration command for ether stats and high capacity
ether stats. The data source for ether stats and high capacity ether
stats are configured during initialization.rmon alarm
rmon alarm
This command sets the RMON alarm entry in the RMON alarm MIB group.
Format rmon alarm alarm-number variable sample-interval {absolute | delta}
rising-threshold value [rising-event-index] falling-threshold value
[falling-event-index] [startup {rising | falling | rising-falling}] [owner
string]
Mode Global Config
Parameter Description
Alarm Index An index that uniquely identifies an entry in the alarm table. Each entry defines a diagnostic sample
at a particular interval for an object on the device. The range is 1 to 65535.
Alarm Variable The object identifier of the particular variable to be sampled. Only variables that resolve to an ASN.1
primitive type of integer.
Alarm Interval The interval in seconds over which the data is sampled and compared with the rising and falling
thresholds. The range is 1 to 2147483647. The default is 1.
Alarm Absolute The value of the statistic during the last sampling period. This object is a read-only, 32-bit signed
Value value.
Utility Commands 346

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
Alarm Rising The rising threshold for the sample statistics. The range is 2147483648 to 2147483647. The default
Threshold is 1.
Alarm Rising Event The index of the eventEntry that is used when a rising threshold is crossed. The range is 1 to 65535.
Index The default is 1.
Alarm Falling The falling threshold for the sample statistics. The range is 2147483648 to 2147483647. The default
Threshold is 1.
Alarm Falling Event The index of the eventEntry that is used when a falling threshold is crossed. The range is 1 to 65535.
Index The default is 2.
Alarm Startup The alarm that may be sent. Possible values are rising, falling or both rising-falling. The default is
Alarm rising-falling.
Alarm Owner The owner string associated with the alarm entry. The default is monitorAlarm.
Command example:
(NETGEAR Switch) (Config)# rmon alarm 1 ifInErrors.2 30 absolute rising-threshold 100 1
falling-threshold 10 2 startup rising owner myOwner
no rmon alarm
This command deletes the RMON alarm entry.
Format no rmon alarm alarm-number
Mode Global Config
Command example:
(NETGEAR Switch) (Config)# no rmon alarm 1
rmon hcalarm
This command sets the RMON hcalarm entry in the High Capacity RMON alarm MIB group.
Format rmon hcalarm alarm-number variable sample-interval {absolute | delta}
rising-threshold high value low value status {positive | negative}
[rising-event-index] falling-threshold high value low value status {positive
| negative} [falling-event-index] [startup {rising | falling |
rising-falling}] [owner string]
Mode Global Config
Utility Commands 347

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
High Capacity Alarm An arbitrary integer index value used to uniquely identify the high capacity alarm entry. The range
Index is 1 to 65535.
(alarm-number)
High Capacity Alarm The object identifier of the particular variable to be sampled. Only variables that resolve to an
Variable ASN.1 primitive type of integer.
(variable)
High Capacity Alarm The interval in seconds over which the data is sampled and compared with the rising and falling
Interval thresholds. The range is 1 to 2147483647. The default is 1.
(sample-interval)
High Capacity Alarm The method of sampling the selected variable and calculating the value to be compared against
Sample Type the thresholds. Possible types are absolute and delta. The default is absolute.
High Capacity Alarm The absolute value (that is, the unsigned value) of the hcAlarmVariable statistic during the last
Absolute Value sampling period. The value during the current sampling period is not made available until the
period is complete. This object is a 64-bit unsigned value that is Read-Only.
High Capacity Alarm This object indicates the validity and sign of the data for the high capacity alarm absolute value
Absolute Alarm Status object (hcAlarmAbsValueobject). Possible status types are valueNotAvailable, valuePositive, or
valueNegative. The default is valueNotAvailable.
High Capacity Alarm High capacity alarm startup alarm that may be sent. Possible values are rising, falling, or
Startup Alarm rising-falling. The default is rising-falling.
High Capacity Alarm The lower 32 bits of the absolute value for threshold for the sampled statistic. The range is 0 to
Rising-Threshold 4294967295. The default is 1.
Absolute Value Low
High Capacity Alarm The upper 32 bits of the absolute value for threshold for the sampled statistic. The range is 0 to
Rising-Threshold 4294967295. The default is 0.
Absolute Value High
High Capacity Alarm This object indicates the sign of the data for the rising threshold, as defined by the objects
Rising-Threshold hcAlarmRisingThresAbsValueLow and hcAlarmRisingThresAbsValueHigh. Possible values are
Value Status valueNotAvailable, valuePositive, or valueNegative. The default is valuePositive.
High Capacity Alarm The lower 32 bits of the absolute value for threshold for the sampled statistic. The range is 0 to
Falling-Threshold 4294967295. The default is 1.
Absolute Value Low
High Capacity Alarm The upper 32 bits of the absolute value for threshold for the sampled statistic. The range is 0 to
Falling-Threshold 4294967295. The default is 0.
Absolute Value High
High Capacity Alarm This object indicates the sign of the data for the falling threshold, as defined by the objects
Falling-Threshold hcAlarmFallingThresAbsValueLow and hcAlarmFallingThresAbsValueHigh. Possible values are
Value Status valueNotAvailable, valuePositive, or valueNegative. The default is valuePositive.
High Capacity Alarm The index of the eventEntry that is used when a rising threshold is crossed. The range is 1 to
Rising Event Index 65535. The default is 1.
High Capacity Alarm The index of the eventEntry that is used when a falling threshold is crossed. The range is 1 to
Falling Event Index 65535. The default is 2.
Utility Commands 348

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
High Capacity Alarm The number of times the associated hcAlarmVariable instance was polled on behalf of the
Failed Attempts hcAlarmEntry (while in the active state) and the value was not available. This object is a 32-bit
counter value that is read-only.
High Capacity Alarm The owner string associated with the alarm entry. The default is monitorHCAlarm.
Owner
High Capacity Alarm The type of non-volatile storage configured for this entry. This object is read-only. The default is
Storage Type volatile.
Command example:
(NETGEAR Switch) (Config)# rmon hcalarm 1 ifInOctets.1 30 absolute rising-threshold high
1 low 100 status positive 1 falling-threshold high 1 low 10 status positive startup
rising owner myOwner
no rmon hcalarm
This command deletes the rmon hcalarm entry.
Format no rmon hcalarm alarm-number
Mode Global Config
Command example:
(NETGEAR Switch) (Config)# no rmon hcalarm 1
rmon event
This command sets the RMON event entry in the RMON event MIB group.
Format rmon event event-number [description string | log | owner string | trap
community]
Mode Global Config
Parameter Description
Event number An index that uniquely identifies an entry in the event table. Each such entry defines one event that
is to be generated when the appropriate conditions occur. The range is 1 to 65535.
Description A comment describing the event entry. The default is alarmEvent.
Log Creates a log entry.
Owner The owner string that is associated with the entry. The default is monitorEvent.
Community The SNMP community, which is specified by an octet string that is used to send an SNMP trap. The
default is public.
Utility Commands 349

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) (Config)# rmon event 1 log description test
no rmon event
This command deletes the rmon event entry.
Format no rmon event event-number
Mode Global Config
Command example:
(NETGEAR Switch) (Config)# no rmon event 1
rmon collection history
This command sets the history control parameters of the RMON historyControl MIB group.
Note: This command is not supported on interface range. Each RMON
history control collection entry can be configured on only one
interface. If you try to configure on multiple interfaces, the switch
displays an error message.
Format rmon collection history index-number [buckets number | interval seconds |
owner string]
Mode Interface Config
Parameter Description
History Control An index that uniquely identifies an entry in the historyControl table. Each such entry defines a set of
Index samples at a particular interval for an interface on the device. The range is 1 to 65535.
History Control The source interface for which historical data is collected.
Data Source
History Control The requested number of discrete time intervals over which data is to be saved. The range is 1 to
Buckets Requested 65535. The default is 50.
History Control The number of discrete sampling intervals over which data shall be saved. This object is read-only.
Buckets Granted The default is 10.
History Control The interval in seconds over which the data is sampled. The range is 1 to 3600. The default is 1800.
Interval
History Control The owner string associated with the history control entry. The default is monitorHistoryControl.
Owner
Utility Commands 350

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) (Interface 1/0/1)# rmon collection history 1 buckets 10 interval 30
owner myOwner
Command example:
(NETGEAR Switch) (Interface 1/0/1-1/0/10)#rmon collection history 1 buckets 10 interval
30 owner myOwner
Error: 'rmon collection history' is not supported on range of interfaces.
no rmon collection history
This command will delete the history control group entry with the specified index number.
Format no rmon collection history index-number
Mode Interface Config
Command example:
(NETGEAR Switch) (Interface 1/0/1-1/0/10)# no rmon collection history 1
show rmon
This command displays the entries in the RMON alarm table.
Format show rmon {alarms | alarm alarm-index}
Mode Privileged Exec
Term Description
Alarm Index An index that uniquely identifies an entry in the alarm table. Each entry defines a diagnostic sample
at a particular interval for an object on the device. The range is 1 to 65535.
Alarm Variable The object identifier of the particular variable to be sampled. Only variables that resolve to an ASN.1
primitive type of integer.
Alarm Interval The interval in seconds over which the data is sampled and compared with the rising and falling
thresholds. The range is 1 to 2147483647. The default is 1.
Alarm Absolute The value of the statistic during the last sampling period. This object is a read-only, 32-bit signed
Value value.
Alarm Rising The rising threshold for the sample statistics. The range is 2147483648 to 2147483647. The default
Threshold is 1.
Alarm Rising Event The index of the eventEntry that is used when a rising threshold is crossed. The range is 1 to 65535.
Index The default is 1.
Utility Commands 351

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Description
Alarm Falling The falling threshold for the sample statistics. The range is 2147483648 to 2147483647. The default
Threshold is 1.
Alarm Falling Event The index of the eventEntry that is used when a falling threshold is crossed. The range is 1 to 65535.
Index The default is 2.
Alarm Startup The alarm that may be sent. Possible values are rising, falling or both rising-falling. The default is
Alarm rising-falling.
Alarm Owner The owner string associated with the alarm entry. The default is monitorAlarm.
Command example:
(NETGEAR Switch) #show rmon alarms
Index OID Owner
----------------------------------------------
1 alarmInterval.1 MibBrowser
2 alarmInterval.1 MibBrowser
Command example:
(NETGEAR Switch) #show rmon alarm 1
Alarm 1
----------
OID: alarmInterval.1
Last Sample Value: 1
Interval: 1
Sample Type: absolute
Startup Alarm: rising-falling
Rising Threshold: 1
Falling Threshold: 1
Rising Event: 1
Falling Event: 2
Owner: MibBrowser
show rmon collection history
This command displays the entries in the RMON history control table.
Format show rmon collection history [interfaces unit/slot/port]
Mode Privileged Exec
Utility Commands 352

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Description
History Control An index that uniquely identifies an entry in the historyControl table. Each such entry defines a set of
Index samples at a particular interval for an interface on the device. The range is 1 to 65535.
History Control The source interface for which historical data is collected.
Data Source
History Control The requested number of discrete time intervals over which data is to be saved. The range is 1 to
Buckets Requested 65535. The default is 50.
History Control The number of discrete sampling intervals over which data shall be saved. This object is read-only.
Buckets Granted The default is 10.
History Control The interval in seconds over which the data is sampled. The range is 1 to 3600. The default is 1800.
Interval
History Control The owner string associated with the history control entry. The default is monitorHistoryControl.
Owner
Command example:
(NETGEAR Switch) #show rmon collection history
Index Interface Interval Requested Granted Owner
Samples Samples
----------------------------------------------------------------------
1 1/0/1 30 10 10 myowner
2 1/0/1 1800 50 10 monitorHistoryControl
3 1/0/2 30 50 10 monitorHistoryControl
4 1/0/2 1800 50 10 monitorHistoryControl
5 1/0/3 30 50 10 monitorHistoryControl
6 1/0/3 1800 50 10 monitorHistoryControl
7 1/0/4 30 50 10 monitorHistoryControl
8 1/0/4 1800 50 10 monitorHistoryControl
9 1/0/5 30 50 10 monitorHistoryControl
10 1/0/5 1800 50 10 monitorHistoryControl
11 1/0/6 30 50 10 monitorHistoryControl
12 1/0/6 1800 50 10 monitorHistoryControl
13 1/0/7 30 50 10 monitorHistoryControl
14 1/0/7 1800 50 10 monitorHistoryControl
15 1/0/8 30 50 10 monitorHistoryControl
16 1/0/8 1800 50 10 monitorHistoryControl
17 1/0/9 30 50 10 monitorHistoryControl
18 1/0/9 1800 50 10 monitorHistoryControl
19 1/0/10 30 50 10 monitorHistoryControl
--More-- or (q)uit
(NETGEAR Switch) #show rmon collection history interfaces 1/0/1
Utility Commands 353

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Index Interface Interval Requested Granted Owner
Samples Samples
----------------------------------------------------------------------
1 1/0/1 30 10 10 myowner
2 1/0/1 1800 50 10 monitorHistoryControl
show rmon events
This command displays the entries in the RMON event table.
Format show rmon events
Mode Privileged Exec
Term Description
Event Index An index that uniquely identifies an entry in the event table. Each such entry defines one event that
is to be generated when the appropriate conditions occur. The range is 1 to 65535.
Event Description A comment describing the event entry. The default is alarmEvent.
Event Type The type of notification that the probe makes about the event. Possible values are None, Log, SNMP
Trap, Log and SNMP Trap. The default is None.
Event Owner Owner string associated with the entry. The default is monitorEvent.
Event Community The SNMP community specific by this octet string which is used to send an SNMP trap. The default
is public.
Owner Event owner. The owner string associated with the entry.
Last time sent The last time over which a log or a SNMP trap message is generated.
Command example:
(NETGEAR Switch) # show rmon events
Index Description Type Community Owner Last time sent
-------------------------------------------------------------------------------
1 test log public MIB 0 days 0 h:0 m:0 s
show rmon history
This command displays the specified entry in the RMON history table.
Format show rmon history index {errors [period seconds] | other [period seconds] |
throughput [period seconds]}
Mode Privileged Exec
Utility Commands 354

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Description
History Control Index An index that uniquely identifies an entry in the historyControl table. Each such entry defines a
set of samples at a particular interval for an interface on the device. The range is 1 to 65535.
History Control Data The source interface for which historical data is collected.
Source
History Control The requested number of discrete time intervals over which data is to be saved. The range is 1 to
Buckets Requested 65535. The default is 50.
History Control The number of discrete sampling intervals over which data shall be saved. This object is
Buckets Granted read-only. The default is 10.
History Control Interval The interval in seconds over which the data is sampled. The range is 1 to 3600. The default is
1800.
History Control Owner The owner string associated with the history control entry. The default is monitorHistoryControl.
Maximum Table Size Maximum number of entries that the history table can hold.
Time Time at which the sample is collected, displayed as period seconds.
CRC Align Number of CRC align errors.
Undersize Packets Total number of undersize packets. Packets are less than 64 octets long (excluding framing bits,
including FCS octets).
Oversize Packets Total number of oversize packets. Packets are longer than 1518 octets (excluding framing bits,
including FCS octets).
Fragments Total number of fragment packets. Packets are not an integral number of octets in length or had
a bad Frame Check Sequence (FCS), and are less than 64 octets in length (excluding framing
bits, including FCS octets).
Jabbers Total number of jabber packets. Packets are longer than 1518 octets (excluding framing bits,
including FCS octets), and are not an integral number of octets in length or had a bad Frame
Check Sequence (FCS).
Octets Total number of octets received on the interface.
Packets Total number of packets received (including error packets) on the interface.
Broadcast Total number of good Broadcast packets received on the interface.
Multicast Total number of good Multicast packets received on the interface.
Util Port utilization of the interface associated with the history index specified.
Dropped Collisions Total number of dropped collisions.
Command example:
(NETGEAR Switch) #show rmon history 1 errors
Sample set: 1 Owner: myowner
Interface: 1/0/1 Interval: 30
Requested Samples: 10 Granted Samples: 10
Maximum table size: 1758
Utility Commands 355

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Time CRC Align Undersize Oversize Fragments Jabbers
--------------------- ---------- --------- --------- ---------- -------
Jan 01 1970 21:41:43 0 0 0 0 0
Jan 01 1970 21:42:14 0 0 0 0 0
Jan 01 1970 21:42:44 0 0 0 0 0
Jan 01 1970 21:43:14 0 0 0 0 0
Jan 01 1970 21:43:44 0 0 0 0 0
Jan 01 1970 21:44:14 0 0 0 0 0
Jan 01 1970 21:44:45 0 0 0 0 0
Jan 01 1970 21:45:15 0 0 0 0 0
Jan 01 1970 21:45:45 0 0 0 0 0
Jan 01 1970 21:46:15 0 0 0 0 0
(NETGEAR Switch) #show rmon history 1 throughput
Sample set: 1 Owner: myowner
Interface: 1/0/1 Interval: 30
Requested Samples: 10 Granted Samples: 10
Maximum table size: 1758
Time Octets Packets Broadcast Multicast Util
-------------------- ---------- --------- --------- ---------- --------
Jan 01 1970 21:41:43 0 0 0 0 1
Jan 01 1970 21:42:14 0 0 0 0 1
Jan 01 1970 21:42:44 0 0 0 0 1
Jan 01 1970 21:43:14 0 0 0 0 1
Jan 01 1970 21:43:44 0 0 0 0 1
Jan 01 1970 21:44:14 0 0 0 0 1
Jan 01 1970 21:44:45 0 0 0 0 1
Jan 01 1970 21:45:15 0 0 0 0 1
Jan 01 1970 21:45:45 0 0 0 0 1
Jan 01 1970 21:46:15 0 0 0 0 1
(NETGEAR Switch) #show rmon history 1 other
Sample set: 1 Owner: myowner
Interface: 1/0/1 Interval: 30
Requested Samples: 10 Granted Samples: 10
Maximum table size: 1758
Time Dropped Collisions
-------------------- ------- ----------
Jan 01 1970 21:41:43 0 0
Utility Commands 356

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Jan 01 1970 21:42:14 0 0
Jan 01 1970 21:42:44 0 0
Jan 01 1970 21:43:14 0 0
Jan 01 1970 21:43:44 0 0
Jan 01 1970 21:44:14 0 0
Jan 01 1970 21:44:45 0 0
Jan 01 1970 21:45:15 0 0
Jan 01 1970 21:45:45 0 0
Jan 01 1970 21:46:15 0 0
show rmon log
This command displays the entries in the RMON log table.
Format show rmon log [event-index]
Mode Privileged Exec
Term Description
Maximum table size Maximum number of entries that the log table can hold.
Event Event index for which the log is generated.
Description A comment describing the event entry for which the log is generated.
Time Time at which the event is generated.
Command example:
(NETGEAR Switch) #show rmon log
Event Description Time
------------------------------------------------
Command example:
(NETGEAR Switch) #show rmon log 1
Maximum table size: 10
Event Description Time
------------------------------------------------
Utility Commands 357
