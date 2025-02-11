# ip_multicast_commands_1016

Pages: 1016-1016

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip mroute
This command removes the configured IPv4 multicast static route.
Format no ip mroute src-ip-addr
Mode Global Config
set ip mroute static-multicast
This command configures a static multicast route for a multicast group IP address and a list
of VLANs that are enabled for routing.
Default No default static routes
Format set ip mroute static-multicast group-ip-address vlan-list
Mode Global Config
Parameters Description
group-ip-address A multicast group IP address.
vlan-list A list of VLANs in the range of 1 to 4093. Each VLAN ID must be separated by a comma.
Note the following requirements:
• All VLANs that you specify in the list must be enabled for routing with an IP address
configured.
• You cannot configure two static multicast routes with the same group IP address, even
though the VLAN lists differ. If you must change the VLAN list for a static route, delete the
existing static route and create a new one with an updated VLAN list.
Command example:
To install a static route for multicast group address 224.0.1.129 for VLANs 1, 2, 3, and 4,
enter the following command:
(config)#ip mroute static-multicast 224.0.1.129 1,2,3,4
no ip mroute static-multicast
This command removes a static multicast route for a group IP address.
The group-ip-address argument represents the multicast group IP address.
Format no set ip mroute static-multicast group-ip-address
Mode Global Config
IP Multicast Commands 1016
