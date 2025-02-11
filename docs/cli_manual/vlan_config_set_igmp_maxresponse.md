# vlan_config_set_igmp_maxresponse

Pages: 573-573

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no set igmp groupmembership-interval
This command sets the IGMPv3 group membership interval time to the default value.
Format no set igmp groupmembership-interval [vlan-id]
Mode Interface Config
Global Config
VLAN Config
set igmp maxresponse
This command sets the IGMP maximum response time for the system, on a particular
interface or VLAN, or on a range of interfaces. The maximum response time is the amount of
time in seconds that a switch will wait after sending a query on an interface because it did not
receive a report for a particular group in that interface. This value must be less than the IGMP
query Interval time value. The range is 1 to 300 seconds.
Default 600 seconds
Format set igmp maxresponse [vlan-id] seconds
Mode Global Config
Interface Config
VLAN Config
no set igmp maxresponse
This command sets the max response time (on the interface or VLAN) to the default value.
Format no set igmp maxresponse [vlan-id]
Mode Global Config
Interface Config
VLAN Config
set igmp mcrtrexpiretime
This command sets the multicast router present expiration time. The time is set for the
system, on a particular interface or VLAN, or on a range of interfaces. This is the amount of
time in seconds that a switch waits for a query to be received on an interface before the
interface is removed from the list of interfaces with multicast routers attached. The range is 0
to 3600 seconds. A value of 0 indicates an infinite time-out, that is, no expiration.
Default 0
Format set igmp mcrtrexpiretime [vlan-id] seconds
Mode Global Config
Interface Config
VLAN Config
Switching Commands 573
