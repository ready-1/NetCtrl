# ip_multicast_commands_1033

Pages: 1033-1033

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip pim join-prune-interval
Use this command to set the join/prune interval on the specified interface to the default value.
Format no ip pim join-prune-interval
Mode Interface Config
ip pim rp-address
This command defines the address of a PIM Rendezvous point (RP) for a specific multicast
group range.
Note: This command takes effect only when PIM-SM is configured as the
PIM mode.
Default 0
Format ip pim rp-address rp-address group-address group-mask [override]
Mode Global Config
Parameter Description
rp-address The IP address of the RP.
group-address The group address supported by the RP.
group-mask The group mask for the group address.
override [Optional] Indicates that if there is a conflict, the RP configured with this command prevails over the
RP learned by BSR.
Command example:
(NETGEAR) (Config) #ip pim rp-address 192.168.10.1
224.1.2.0 255.255.255.0
no ip pim rp-address
Use this command to remove the address of the configured PIM Rendezvous point (RP) for
the specified multicast group range.
Format no ip pim rp-address rp-address group-address group-mask [override]
Mode Global Config
IP Multicast Commands 1033
