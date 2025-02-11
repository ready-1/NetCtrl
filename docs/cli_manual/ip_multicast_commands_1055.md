# ip_multicast_commands_1055

Pages: 1055-1055

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip igmp-proxy unsolicit-rprt-interval
This command resets the unsolicited report interval of the IGMP Proxy router to the default
value.
Format no ip igmp-proxy unsolicit-rprt-interval
Mode Interface Config
ip igmp-proxy reset-status
This command resets the host interface status parameters of the IGMP Proxy interface (or
range of interfaces). This command is valid only when you enable IGMP Proxy on the
interface.
Format ip igmp-proxy reset-status
Mode Interface Config
show ip igmp-proxy
This command displays a summary of the host interface status parameters. It displays the
following parameters only when you enable IGMP Proxy.
Format show ip igmp-proxy
Modes Privileged EXEC
User EXEC
Term Definition
Interface index The interface number of the IGMP Proxy.
Admin Mode States whether the IGMP Proxy is enabled or not. This is a configured value.
Operational Mode States whether the IGMP Proxy is operationally enabled or not. This is a status parameter.
Version The present IGMP host version that is operational on the proxy interface.
Number of The number of multicast groups that are associated with the IGMP Proxy interface.
Multicast Groups
Unsolicited Report The time interval at which the IGMP Proxy interface sends unsolicited group membership report.
Interval
Querier IP Address The IP address of the Querier, if any, in the network attached to the upstream interface (IGMP-Proxy
on Proxy Interface interface).
Older Version 1 The interval used to timeout the older version 1 queriers.
Querier Timeout
IP Multicast Commands 1055
