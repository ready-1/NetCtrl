# ip_multicast_commands_1040

Pages: 1040-1040

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Neighbor Count..................................1
Designated Router...............................192.168.10.1
Command example:
If none of the interfaces are enabled for PIM, the following message is displayed:
None of the routing interfaces are enabled for PIM.
show ip pim neighbor
This command displays PIM neighbors discovered by PIMv2 Hello messages.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
If the interface number is not specified, the command displays the status parameters of all
PIM-enabled interfaces.
Format show ip pim neighbor [unit/slot/port | vlan vlan-id]
Modes Privileged EXEC
User EXEC
Term Definition
Neighbor Address The IP address of the PIM neighbor on an interface.
Interface unit/slot/port
Up Time The time since this neighbor has become active on this interface.
Expiry Time Time remaining for the neighbor to expire.
DR Priority The DR Priority configured on this Interface (PIM-SM only).
Note: DR Priority is applicable only when sparse-mode configured routers are neighbors.
Otherwise, NA is displayed in this field.
Command example:
(NETGEAR) #show ip pim neighbor 1/0/1
Neighbor Addr Interface Uptime Expiry Time DR
(hh:mm:ss) (hh:mm:ss) Priority
--------------- --------- ----------- ----------- --------
192.168.10.2 1/0/1 00:02:55 00:01:15 NA
IP Multicast Commands 1040
