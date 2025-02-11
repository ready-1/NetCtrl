# ip_multicast_commands_1048

Pages: 1048-1048

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip igmp last-member-query-interval
This command resets the Maximum Response Time to the default value.
Format no ip igmp last-member-query-interval
Modes Interface Config
ip igmp query-interval
This command configures the query interval for the specified interface or range of interfaces.
The query interval determines how fast IGMP Host-Query packets are transmitted on this
interface. The range for the seconds argument is 1 to 3600 seconds.
Default 125 seconds
Format ip igmp query-interval seconds
Modes Interface Config
no ip igmp query-interval
This command resets the query interval for the specified interface to the default value. This is
the frequency at which IGMP Host-Query packets are transmitted on this interface.
Format no ip igmp query-interval
Modes Interface Config
ip igmp query-max-response-time
This command configures the maximum response time interval for the specified interface or
range of interfaces, which is the maximum query response time advertised in IGMPv2
queries on this interface. The deciseconds argument is the time interval, specified in 0 to
255 tenths of a second.
Default 100
Format ip igmp query-max-response-time desciseconds
Mode Interface Config
no ip igmp query-max-response-time
This command resets the maximum response time interval for the specified interface, which
is the maximum query response time advertised in IGMPv2 queries on this interface to the
default value. The maximum response time interval is reset to the default time.
Format no ip igmp query-max-response-time
Mode Interface Config
IP Multicast Commands 1048
