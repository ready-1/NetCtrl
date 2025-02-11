# ip_multicast_commands_1035

Pages: 1035-1035

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip pim ssm
Use this command to define the Source Specific Multicast (SSM) range of IP multicast
addresses on the router.
Note: This command takes effect only when PIM-SM is configured as the
PIM mode.
Default disabled
Format ip pim ssm {default | group-address group-mask}
Mode Global Config
Parameter Description
default Defines the SSM range access list to 232/8.
Command example:
(NETGEAR) (Config) #ip pim ssm default
(NETGEAR) (Config) #ip pim ssm 232.1.2.0 255.255.255.0
no ip pim ssm
Use this command to remove the Source Specific Multicast (SSM) range of IP multicast
addresses on the router.
Format no ip pim ssm {default | group-address group-mask}
Mode Global Config
ip pim-trapflags
This command enables the PIM trap mode for both Sparse Mode (SM) and Dense Mode.
(DM).
Default disabled
Format ip pim-trapflags
Mode Global Config
IP Multicast Commands 1035
