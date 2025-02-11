# mmrp_commands

Pages: 499-501

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
jointime seconds The interval between the transmission of MRP PDUs registering (or reregistering) membership for
an attribute. There is an instance of this timer on a per-port, per-MRP participant basis.
Permissible values are 10 to 100 centiseconds (0.1 to 1.0 seconds). The factory default is
20centiseconds (0.2 seconds). The finest granularity of specification is one centisecond
( 0.01seconds).
leavetime seconds The period of time to wait after receiving an unregister request for an attribute before deleting the
attribute. You can consider this a buffer time for another station to assert registration for the same
attribute in order to maintain uninterrupted service. There is an instance of this timer on a
per-Port, per-MRP participant basis. Permissible values are 20 to 600 centiseconds (0.2 to
6.0seconds). The factory default is 300 centiseconds (3.0 seconds).
leavealltime seconds The LeaveAllTime controls how frequently LeaveAll PDUs are generated. A LeaveAll PDU
indicates that all registrations are shortly to be deregistered. Participants must to rejoin in order to
maintain registration. There is an instance of this timer on a per-port, per-MRP participant basis.
The Leave All Period Timer is set to a random value in the range of LeaveAllTime to
1.5*LeaveAllTime. Permissible values are 200 to 6000 centiseconds (2 to 60 seconds). The
factory default is 2000 centiseconds (20 seconds).
show mrp
This command displays MRP leave, join, and leaveall intervals configured on interfaces. If
you specify the summary parameter, the output shows interval values for all interfaces. If you
specify the unit/slot/port parameter, the output shows the MRP intervals for the
specified interface.
Format show mrp interface {summary | unit/slot/port}
Mode Privileged Exec
MMRP Commands
mmrp (Global Config)
Use this command in Global Config mode to enable MMRP. MMRP must also be enabled on
the individual interfaces.
Default Disabled
Format mmrp
Mode Global Config
Switching Commands 499

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no mmrp (Global Config)
Use this command in Global Config mode to disable MMRP.
Format no mmrp
Mode Global Config
mmrp periodic state machine
Use this command in Global Config mode to enable MMRP periodic state machine.
Default Disabled
Format mmrp periodic state machine
Mode Global Config
no mmrp periodic state machine
Use this command in Global Config mode to disable MMRP periodic state machine.
Format no mmrp periodic state machine
Mode Global Config
mmrp (Interface Config)
Use this command in Interface Config mode on the interface. MMRP can be enabled on
physical interfaces or LAG interfaces. When configured on a LAG member port, MMRP is
operationally disabled. Enabling MMRP on an interface automatically enables dynamic
MFDB entries creation.
Default Disabled
Format mmrp
Mode Interface Config
no mmrp (Interface Config)
Use this command in Interface Config mode to disable MMRP mode on the interface.
Format no mmrp
Mode Global Config
Switching Commands 500

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
clear mmrp statistics
Use this command in Privileged EXEC mode to clear MMRP statistics of one or all interfaces.
Format clear mmrp statistics [unit/slot/port | all]
Mode Privileged EXEC
Parameter Description
unit/slot/port If used with unit/slot/port parameter, the command clears MMRP statistics for the given
interface.
all If the all parameter is specified, the command clears MMRP statistics for all the interfaces.
show mmrp
Use this command in Privileged EXEC mode to display the status of the MMRP mode.
Format show mmrp [summary | interface [unit/slot/port | summary]]
Mode Privileged EXEC
Parameter Description
summary If used with the summary parameter, the command displays global MMRP information.
interface If interface is specified for a particular unit/slot/port, the command displays the MMRP
mode of that interface.
summary If interface is specified with the summary parameter, the command shows a table containing
MMRP global mode for all interfaces.
Command example:
(NETGEAR switch) #show mmrp summary
MMRP Global Admin Mode......................... Disabled
MMRP Periodic State Machine.................... Disabled
Command example:
(NETGEAR switch) #show mmrp interface 0/12
MMRP Interface Admin Mode...................... Disabled
Command example:
(NETGEAR switch) #show mmrp interface summary
Intf Mode
--------- ---------
0/1 Disabled
0/2 Disabled
0/3 Disabled
0/4 Disabled
0/5 Disabled
Switching Commands 501
