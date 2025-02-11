# id_name_pid_status_restart_status_----_----------------_-----_---------_---------_-------__d9bd7a5a

Pages: 213-214

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show process app-list
This command displays the user and system applications.
Format show process app-list
Mode Privileged EXEC
Field Description
ID The application identifier.
Name The name that identifies the process.
PID The number the software uses to identify the process.
Admin Status The administrative status of the process.
Auto Restart Indicates whether the process will automatically restart if it stops.
Running Status Indicates whether the process is currently running or stopped.
Command example:
(NETGEAR Switch) #show process app-list
Admin Auto Running
ID Name PID Status Restart Status
---- ---------------- ----- --------- --------- -------
1 dataplane 15309 Enabled Disabled Running
2 switchdrvr 15310 Enabled Disabled Running
3 syncdb 15314 Enabled Disabled Running
4 lighttpd 18718 Enabled Enabled Running
5 syncdb-test 0 Disabled Disabled Stopped
6 proctest 0 Disabled Enabled Stopped
7 user.start 0 Enabled Disabled Stopped
show process memory
This command displays memory consumption details by various software components.
Format show process memory
Mode Privileged EXEC
Field Description
Total The total available memory on the switch.
Free The free memory on the switch.
Allocated The allocated memory on the switch, excluding cache space used by the file system.
Components The internal software component.
Utility Commands 213

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Description
CurrentAllocated The amount of memory that a component is using.
Change The increase or decrease of the memory that a component consumes since the last time this
command was executed. This field shows the difference in memory allocation between two
successive executions of the command.
MaxAllocated The maximum amount of memory allocation by a component.
Allocs/Frees The number of memory allocation and free calls made by a component.
show process cpu
This command provides the percentage utilization of the CPU by different tasks. The number
argument can be a number from 1 to 8.
Note: A busy CPU might not be caused by traffic processing but by various
tasks that run simultaneously.
Format show process cpu [number | all]
Mode Privileged EXEC
Parameter Description
Free The system-wide free memory.
Alloc The system-wide allocated memory (excluding cache, file system used space).
Pid The process or thread ID.
Name The process or thread name.
5Secs The CPU utilization sampling in 5-second intervals.
60Secs The CPU utilization sampling in 60-second intervals.
300Secs The CPU utilization sampling in 300-second intervals.
Total CPU Utilization Total CPU utilization in percentage within the specified window of 5, 60, and 300 seconds.
(NETGEAR Switch) #show process cpu
Memory Utilization Report
status bytes
------ ----------
free 106450944
alloc 423227392
CPU Utilization:
Utility Commands 214
