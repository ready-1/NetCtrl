# vlan_mode_no_set_mld_maxresponse

Pages: 592-593

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default 10 seconds
Format set mld maxresponse seconds
Mode Global Config
Interface Config
VLAN Mode
no set mld maxresponse
Use this command to set the max response time (on the interface or VLAN) to the default
value.
Format no set mld maxresponse
Mode Global Config
Interface Config
VLAN Mode
set mld mcrtexpiretime
Use this command to set the multicast router present expiration time. The time is set for the
system, on a particular interface or VLAN. This is the amount of time in seconds that a switch
waits for a query to be received on an interface before the interface is removed from the list of
interfaces with multicast routers attached. The range is 0 to 3600 seconds. A value of 0
indicates an infinite time-out, that is, no expiration.
Default 0
Format set mld mcrtexpiretime vlan-id seconds
Mode Global Config
Interface Config
no set mld mcrtexpiretime
Use this command to set the multicast router present expiration time to 0. The time is set for
the system, on a particular interface or a VLAN.
Format no set mld mcrtexpiretime vlan-id
Mode Global Config
Interface Config
Switching Commands 592

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
set mld mrouter
Use this command to configure the VLAN ID for the VLAN that has the multicast router
attached mode enabled.
Format set mld mrouter vlan-id
Mode Interface Config
no set mld mrouter
Use this command to disable multicast router attached mode for a VLAN with a particular
VLAN ID.
Format no set mld mrouter vlan-id
Mode Interface Config
set mld mrouter interface
Use this command to configure the interface as a multicast router-attached interface. When
configured as a multicast router interface, the interface is treated as a multicast
router-attached interface in all VLANs.
Default disabled
Format set mld mrouter interface
Mode Interface Config
no set mld mrouter interface
Use this command to disable the status of the interface as a statically configured multicast
router-attached interface.
Format no set mld mrouter interface
Mode Interface Config
set mld exclude-mrouter-intf
Use this command to control whether unknown multicast data is sent to an mrouter interface.
If either IGMP Snooping or MLD Snooping is enabled on a VLAN, by default, dynamic
mrouter mode is enabled on the interface that receives MLD PDUs from the upstream router.
When the mrouter mode is enabled on the interface, unknown multicast data is sent to that
interface.
If you enter the command, the switch blocks all unknown multicast data through the mrouter
port, whether the port is configured dynamically or statically. Only MLD PDUs are allowed to
pass through the mrouter port to the upstream router interface.
Switching Commands 593
