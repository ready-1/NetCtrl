# ip_multicast_commands_1047

Pages: 1047-1047

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip igmp version
This command configures the version of IGMP for an interface or range of interfaces. The
value for version is either 1, 2 or 3.
Default 3
Format ip igmp version version
Modes Interface Config
no ip igmp version
This command resets the version of IGMP to the default value.
Format no ip igmp version
Modes Interface Config
ip igmp last-member-query-count
This command sets the number of Group-Specific Queries sent by the interface or range of
interfaces before the router assumes that there are no local members on the interface. The
range for count is from 1 to 20.
Format ip igmp last-member-query-count count
Modes Interface Config
no ip igmp last-member-query-count
This command resets the number of Group-Specific Queries to the default value.
Format no ip igmp last-member-query-count
Modes Interface Config
ip igmp last-member-query-interval
This command configures the Maximum Response Time inserted in Group-Specific Queries
which are sent in response to Leave Group messages. The range for deciseconds is 0 to
255 tenths of a second. This value can be configured on one interface or a range of
interfaces
Default 10 tenths of a second (1 second)
Format ip igmp last-member-query-interval deciseconds
Modes Interface Config
IP Multicast Commands 1047
