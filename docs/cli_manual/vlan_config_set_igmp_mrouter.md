# vlan_config_set_igmp_mrouter

Pages: 574-574

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no set igmp mcrtrexpiretime
This command sets the multicast router present expiration time to 0. The time is set for the
system, on a particular interface or a VLAN.
Format no set igmp mcrtrexpiretime [vlan-id]
Mode Global Config
Interface Config
VLAN Config
set igmp mrouter
This command configures the VLAN ID that has the multicast router mode enabled.
Format set igmp mrouter vlan-id
Mode Interface Config
no set igmp mrouter
This command disables multicast router mode for a particular VLAN ID.
Format no set igmp mrouter vlan-id
Mode Interface Config
set igmp mrouter interface
This command configures the interface or range of interfaces as a multicast router interface.
When configured as a multicast router interface, the interface is treated as a multicast router
interface in all VLANs.
Default disabled
Format set igmp mrouter interface
Mode Interface Config
no set igmp mrouter interface
This command disables the status of the interface as a statically configured multicast router
interface.
Format no set igmp mrouter interface
Mode Interface Config
Switching Commands 574
