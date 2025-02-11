# ip_event_dampening_commands_dampening

Pages: 752-753

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
IP Event Dampening Commands
dampening
Use this command to enable IP event dampening on a routing interface.
Format dampening [half-life period] [reuse-threshold suppress-threshold
max-suppress-time [restart restart-penalty]]
Mode Interface Config
Parameter Description
Half-life period The number of seconds it takes for the penalty to reduce by half. The configurable range is 1-30
seconds. Default value is 5 seconds.
Reuse Threshold The value of the penalty at which the dampened interface is restored. The configurable range is
1-20,000. Default value is 1000.
Suppress The value of the penalty at which the interface is dampened. The configurable range is 1-20,000.
Threshold Default value is 2000.
Max Suppress The maximum amount of time (in seconds) an interface can be in suppressed state after it stops
Time flapping. The configurable range is 1-255 seconds. The default value is four times of half-life period.
If half-period value is allowed to default, the maximum suppress time defaults to 20 seconds.
Restart Penalty Penalty applied to the interface after the device reloads. The configurable range is 1-20,000. Default
value is 2000.
no dampening
This command disables IP event dampening on a routing interface.
Format no dampening
Mode Interface Config
show dampening interface
This command summarizes the number of interfaces configured with dampening and the
number of interfaces being suppressed.
Format show dampening interface
Mode Privileged EXEC
Command example:
(NETGEAR Switch)# show dampening interface
2 interfaces are configured with dampening.
1 interface is being suppressed.
Routing Commands 752

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show interface dampening
This command displays the status and configured parameters of the interfaces configured
with dampening.
Format show interface dampening
Mode Privileged EXEC
Parameter Description
Flaps The number times the link state of an interface changed from UP to DOWN.
Penalty Accumulated Penalty.
Supp Indicates if the interface is suppressed or not.
ReuseTm Number of seconds until the interface is allowed to come up again.
HalfL Configured half-life period.
ReuseV Configured reuse-threshold.
SuppV Configured suppress threshold.
MaxSTm Configured maximum suppress time in seconds.
MaxP Maximum possible penalty.
Restart Configured restart penalty.
Note: The command clear counters on page244 resets the flap count to zero.
Note: Any change in the dampening configuration resets the current penalty, reuse time and suppressed state to their
default values, meaning 0, 0, and False respectively.
Command example:
Router# show interface dampening
Interface 0/2
Flaps Penalty Supp ReuseTm HalfL ReuseV SuppV MaxSTm MaxP Restart
0 0 F ALSE 0 5 1 000 2 000 2 0 1 6000 0
Interface 0/3
Flaps Penalty Supp ReuseTm HalfL ReuseV SuppV MaxSTm MaxP Restart
6 1 865 T RUE 1 8 2 0 1 000 2 001 3 0 2 828 1500
Routing Commands 753
