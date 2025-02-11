# ip_multicast_commands_1034

Pages: 1034-1034

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip pim rp-candidate
Use this command to configure the router to advertise itself as a PIM candidate rendezvous
point (RP) to the bootstrap router (BSR) for a specific multicast group range.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
Note: This command takes effect only when PIM-SM is configured as the
PIM mode.
Default Disabled
Format ip pim rp-candidate interface {unit/slot/port | vlan vland-id} group-address
group-mask [interval interval]
Mode Global Config
Parameter Description
unit/slot/port or The interface type in the unit/slot/port format or the VLAN ID is advertised as a candidate RP
vland-id address. This interface or VLAN must be enabled with PIM.
group-address The multicast group address that is advertised in association with the RP address.
group-mask The multicast group prefix that is advertised in association with the RP address.
interval [Optional] Indicates the RP candidate advertisement interval. The range is from 1 to 16383 seconds.
The default value is 60 seconds.
Command example: The following shows examples of the command.
(NETGEAR) (Config) #ip pim rp-candidate interface 1/0/1 224.1.2.0 255.255.255.0
(NETGEAR) (Config) #ip pim rp-candidate interface 1/0/1 224.1.2.0 255.255.255.0 interval

no ip pim rp-candidate
Use this command to remove the configured PIM candidate Rendezvous point (RP) for a
specific multicast group range.
Format no ip pim rp-candidate interface {unit/slot/port | vlan vland-id}
group-address group-mask
Mode Global Config
IP Multicast Commands 1034
