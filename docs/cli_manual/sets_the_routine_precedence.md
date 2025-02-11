# sets_the_routine_precedence

Pages: 698-703

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
0 Sets the routine precedence
1 Sets the priority precedence
2 Sets the immediate precedence
3 Sets the Flash precedence
4 Sets the Flash override precedence
5 Sets the critical precedence
6 Sets the internetwork control precedence
7 Sets the network control precedence
no set ip precedence
Use this command to reset the three IP precedence bits in the IP packet header to the
default.
Format no set ip precedence
Mode Route Map Configuration
show ip policy
This command lists the route map associated with each interface.
Format show ip policy
Mode Privileged Exec
Term Definition
Interface The interface.
Route-map The route map
show route-map
To display a route map, use the show route-map command in Privileged EXEC mode.
Format show route-map [map-name]
Mode Privileged EXEC
Parameter Description
map-name (Optional) Name of a specific route map.
Routing Commands 698

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) # show route-map test
route-map test, permit, sequence 10
Match clauses:
ip address prefix-lists: orange
Set clauses:
set metric 50
Router Discovery Protocol Commands
This section describes the commands you use to view and configure Router Discovery
Protocol settings on the switch. The Router Discovery Protocol enables a host to discover the
IP address of routers on the subnet.
ip irdp
This command enables Router Discovery on an interface or range of interfaces.
Default disabled
Format ip irdp
Mode Interface Config
no ip irdp
This command disables Router Discovery on an interface.
Format no ip irdp
Mode Interface Config
ip irdp address
This command configures the address that the interface uses to send the router discovery
advertisements. The valid values for ipaddr are 224.0.0.1, which is the all-hosts IP
multicast address, and 255.255.255.255, which is the limited broadcast address.
Default 224.0.0.1
Format ip irdp address ipaddr
Mode Interface Config
Routing Commands 699

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip irdp address
This command configures the default address used to advertise the router for the interface.
Format no ip irdp address
Mode Interface Config
ip irdp holdtime
This command configures the value of the holdtime field of the router advertisement sent
from this interface. The seconds argument holdtime value is in the range of 4 to 9000
seconds.
Default 3 * maxinterval
Format ip irdp holdtime seconds
Mode Interface Config
no ip irdp holdtime
This command resets the default value of the holdtime field of the router advertisement sent
from this interface.
Format no ip irdp holdtime
Mode Interface Config
ip irdp maxadvertinterval
This command configures the maximum time allowed between sending router
advertisements from the interface. The range for the seconds argument is 4 to 1800
seconds.
Default 600
Format ip irdp maxadvertinterval seconds
Mode Interface Config
no ip irdp maxadvertinterval
This command resets the default maximum time.
Format no ip irdp maxadvertinterval
Mode Interface Config
Routing Commands 700

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip irdp minadvertinterval
This command configures the minimum time allowed between sending router advertisements
from the interface. The range for seconds argument is 3–1800 seconds.
Default 0.75 * maxadvertinterval
Format ip irdp minadvertinterval seconds
Mode Interface Config
no ip irdp minadvertinterval
This command resets the default minimum time to the default.
Format no ip irdp minadvertinterval
Mode Interface Config
ip irdp multicast
This command configures the destination IP address for router advertisements as 224.0.0.1,
which is the default address. The no form of the command configures the IP address as
255.255.255.255 to instead send router advertisements to the limited broadcast address.
Format ip irdp multicast ip address
Mode Interface Config
no ip irdp multicast
By default, router advertisements are sent to 224.0.0.1. To instead send router
advertisements to the limited broadcast address, 255.255.255.255, use the no form of this
command.
Format no ip irdp multicast
Mode Interface Config
ip irdp preference
This command configures the preferability of the address as a default router address, relative
to other router addresses on the same subnet. The preference number can be a number
from -2147483648 to 2147483647.
Default 0
Format ip irdp preference number
Mode Interface Config
Routing Commands 701

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip irdp preference
This command configures the default preferability of the address as a default router address,
relative to other router addresses on the same subnet.
Format no ip irdp preference
Mode Interface Config
show ip irdp
This command displays the router discovery information for all interfaces, a specified
interface, or specified VLAN. The argument unit/slot/port corresponds to a physical
routing interface or VLAN routing interface. The vlan keyword and vland-id argument are
used to specify the VLAN ID of the routing VLAN directly instead of in a unit/slot/port
format. The vland-id argument can be a number from 1–4093.
Format show ip irdp {unit/slot/port | vlan vland-id | all}
Modes Privileged EXEC
User EXEC
Term Definition
Interface The unit/slot/port that corresponds to a physical routing interface or VLAN routing interface.
vlan Use this keyword to specify the VLAN ID of the routing VLAN directly instead of in a
unit/slot/port format.
Ad Mode The advertise mode, which indicates whether router discovery is enabled or disabled on this
interface.
Dest Address The destination IP address for router advertisements.
Max Int The maximum advertise interval, which is the maximum time, in seconds, allowed between sending
router advertisements from the interface.
Min Int The minimum advertise interval, which is the minimum time, in seconds, allowed between sending
router advertisements from the interface.
Hold Time The amount of time, in seconds, that a system should keep the router advertisement before
discarding it.
Preference The preference of the address as a default router address, relative to other router addresses on the
same subnet.
Routing Commands 702

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Virtual LAN Routing Commands
This section describes the commands you use to view and configure VLAN routing and to
view VLAN routing status information.
vlan routing
This command enables routing on a VLAN. The vlanid value has a range from 1 to 4093.
The interface-id value has a range from 1 to 128. Typically, you do not supply the
interface ID argument, and the system automatically selects the interface ID. However, if you
specify an interface ID, the interface ID becomes the port number in the unit/slot/port
for the VLAN routing interface.
If you select an interface ID that is already in use, the CLI displays an error message and
does not create the VLAN interface. For products that use text-based configuration, including
the interface ID in the vlan routing command for the text configuration ensures that the
unit/slot/port for the VLAN interface stays the same across a restart. Keeping the
unit/slot/port the same ensures that the correct interface configuration is applied to
each interface when the system restarts.
Format vlan routing vlanid [interface-id]
Mode VLAN Config
no vlan routing
This command deletes routing on a VLAN.
Format no vlan routing vlanid
Mode VLAN Config
Command example:
The following example specifies a VLAN ID value. The interface ID argument is not used.
(NETGEAR Switch)(Vlan)#vlan 14
(NETGEAR Switch)(Vlan)#vlan routing 14 ?
<cr> Press enter to execute the command.
<1-24> Enter interface ID
Typically, you press Enter without supplying the Interface ID value; the system automatically
selects the interface ID.
Command example:
The following example specifies interface ID 51 for VLAN 14 interface. The interface ID
becomes the port number in the unit/slot/port for the VLAN routing interface. In this
example, unit/slot/port is 4/51 for VLAN 14 interface.
Routing Commands 703
