# ip_helper_is_enabled_routing_commands_723

Pages: 723-723

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default disabled
Format ip helper enable
Mode Global Config
Command example:
(NETGEAR Switch)(config)#ip helper enable
no ip helper enable
Use the no form of this command to disable relay of all UDP packets.
Format no ip helper enable
Mode Global Config
show ip helper-address
Use this command to display the IP helper address configuration. The argument
unit/slot/port corresponds to a physical routing interface or VLAN routing interface.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vlan-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in a unit/slot/port format. The vlan-id can
be a number from 1–4093.
Format show ip helper-address [unit/slot/port | vlan vlan-id]
Mode Privileged EXEC
Parameter Description
interface The relay configuration is applied to packets that arrive on this interface. This field is set to any for
global IP helper entries.
UDP Port The relay configuration is applied to packets whose destination UDP port is this port. Entries whose
UDP port is identified as any are applied to packets with the destination UDP ports listed in Table 4.
Discard If Yes, packets arriving on the given interface with the given destination UDP port are discarded
rather than relayed. Discard entries are used to override global IP helper address entries which
otherwise might apply to a packet.
Hit Count The number of times the IP helper entry has been used to relay or discard a packet.
Server Address The IPv4 address of the server to which packets are relayed.
Command example:
(NETGEAR Switch) #show ip helper-address
IP helper is enabled
Routing Commands 723
