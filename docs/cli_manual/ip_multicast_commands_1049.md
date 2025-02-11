# ip_multicast_commands_1049

Pages: 1049-1049

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip igmp robustness
This command configures the robustness that allows tuning of the interface or range of
interfaces. The robustness is the tuning for the expected packet loss on a subnet. If a subnet
is expected to have a lot of loss, the Robustness variable may be increased for the interface.
The number argument specifies the packet loss number in the range from 1 to 255.
Default 2
Format ip igmp robustness number
Mode Interface Config
no ip igmp robustness
This command sets the robustness value to default.
Format no ip igmp robustness
Mode Interface Config
ip igmp startup-query-count
This command sets the number of Queries sent out on startup, separated by the Startup
Query Interval on the interface or range of interfaces. The range for the number argument is
1 to 20.
Default 2
Format ip igmp startup-query-count number
Mode Interface Config
no ip igmp startup-query-count
This command resets the number of Queries sent out on startup, separated by the Startup
Query Interval on the interface to the default value.
Format no ip igmp startup-query-count
Mode Interface Config
ip igmp startup-query-interval
This command sets the interval between General Queries sent on startup on the interface or
range of interfaces. The time interval value is in seconds. The range for the seconds
argument is 1 to 300 seconds.
IP Multicast Commands 1049
