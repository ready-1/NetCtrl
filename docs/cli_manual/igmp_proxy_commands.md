# igmp_proxy_commands

Pages: 1054-1054

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Number of Joins The number of times a group membership has been added on this interface.
Number of Groups The current number of membership entries for this interface.
IGMP Proxy Commands
The IGMP Proxy is used by IGMP Router (IPv4 system) to enable the system to issue IGMP
host messages on behalf of hosts that the system discovered through standard IGMP router
interfaces. With IGMP Proxy enabled, the system acts as proxy to all the hosts residing on its
router interfaces.
ip igmp-proxy
This command enables the IGMP Proxy on the an interface or range of interfaces. To enable
the IGMP Proxy on an interface, you must enable multicast forwarding. Also, make sure that
there are no multicast routing protocols enabled on the router.
Format ip igmp-proxy
Mode Interface Config
no ip igmp-proxy
This command disables the IGMP Proxy on the router.
Format no ip igmp-proxy
Mode Interface Config
ip igmp-proxy unsolicit-rprt-interval
This command sets the unsolicited report interval for the IGMP Proxy interface or range of
interfaces. This command is valid only when you enable IGMP Proxy on the interface or
range of interfaces. The value for the seconds argument is a number in the range 1–260
seconds.
Default 1
Format ip igmp-proxy unsolicit-rprt-interval seconds
Mode Interface Config
IP Multicast Commands 1054
