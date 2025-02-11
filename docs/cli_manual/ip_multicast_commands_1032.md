# ip_multicast_commands_1032

Pages: 1032-1032

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip pim dr-priority
Use this command to set the priority value for which a router is elected as the designated
router (DR). The priority argument is a value in the range of 0–2147483647.
Note: This command takes effect only when Sparse mode is enabled in the
Global mode.
Default 1
Format ip pim dr-priority priority
Mode Interface Config
Command example:
(NETGEAR) (Interface 1/0/1) #ip pim dr-priority 10
no ip pim dr-priority
Use this command to return the DR Priority on the specified interface to its default value.
Format no ip pim dr-priority
Mode Interface Config
ip pim join-prune-interval
Use this command to configure the frequency of PIM Join/Prune messages on a specified
interface. The join/prune interval is specified in seconds. The seconds argument can be
configured as a value from 0 to 18000 seconds.
Note: This command takes effect only when PIM-SM is configured as the
PIM mode.
Default 60
Format ip pim join-prune-interval seconds
Mode Interface Config
Command example:
(NETGEAR) (Interface 1/0/1) #ip pim join-prune-interval 90
IP Multicast Commands 1032
