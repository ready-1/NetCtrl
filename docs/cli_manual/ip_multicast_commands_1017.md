# ip_multicast_commands_1017

Pages: 1017-1017

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip multicast
This command sets the administrative mode of the IP multicast forwarder in the router to
active.
Default disabled
Format ip multicast
Mode Global Config
no ip multicast
This command sets the administrative mode of the IP multicast forwarder in the router to
inactive.
Format no ip multicast
Mode Global Config
ip multicast ttl-threshold
This command is specific to IPv4. Use this command to apply the given Time-to-Live
threshold value to a routing interface or range of interfaces. The ttlvalue is the TTL
threshold which is to be applied to the multicast Data packets which are to be forwarded from
the interface. This command sets the Time-to-Live threshold value such that any data
packets forwarded over the interface having TTL value above the configured value are
dropped. The value for ttlvalue ranges from 0 to 255.
Default 1
Format ip multicast ttl-threshold ttlvalue
Mode Interface Config
no ip multicast ttl-threshold
This command applies the default TTL threshold to a routing interface. The TTL threshold is
the TTL threshold which is to be applied to the multicast Data packets which are to be
forwarded from the interface.
Format no ip multicast ttl-threshold
Mode Interface Config
IP Multicast Commands 1017
