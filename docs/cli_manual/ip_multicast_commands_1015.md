# ip_multicast_commands_1015

Pages: 1015-1015

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Multicast Commands
This section describes the commands you use to configure IP Multicast and to view IP
Multicast settings and statistics.
ip mcast boundary
This command adds an administrative scope multicast boundary specified by groupipaddr
and mask for which this multicast administrative boundary is applicable. groupipaddr is a
group IP address and mask is a group IP mask. This command can be used to configure a
single interface or a range of interfaces.
Format ip mcast boundary groupipaddr mask
Mode Interface Config
no ip mcast boundary
This command deletes an administrative scope multicast boundary specified by
groupipaddr and mask for which this multicast administrative boundary is applicable.
groupipaddr is a group IP address and mask is a group IP mask.
Format no ip mcast boundary groupipaddr mask
Mode Interface Config
ip mroute
This command configures an IPv4 multicast static route for a source.
Default No MRoute is configured on the system.
Format ip mroute src-ip-addr src-mask rpf-addr preference
Mode Global Config
Parameter Description
src-ip-addr The IP address of the multicast source network.
src-mask The IP mask of the multicast data source.
rpf-ip-addr The IP address of the RPF next-hop router toward the source.
preference The administrative distance for this Static MRoute, that is, the preference value. The range is 1 to
255.
IP Multicast Commands 1015
