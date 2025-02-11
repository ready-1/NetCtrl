# ip_multicast_commands_1030

Pages: 1030-1030

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip pim hello-interval
This command configures the transmission frequency of PIM hello messages the specified
interface. The seconds argument is a value in a range of 0 to 18000 seconds.
Default 30
Format ip pim hello-interval seconds
Mode Interface Config
Command example:
(NETGEAR) (Interface 1/0/1) #ip pim hello-interval 50
no ip pim hello-interval
This command resets the transmission frequency of hello messages between PIM enabled
neighbors to the default value.
Format no ip pim hello-interval
Mode Interface Config
ip pim bsr-border
Use this command to prevent bootstrap router (BSR) messages from being sent or received
on the specified interface.
Note: This command takes effect only when Sparse mode in enabled in the
Global mode.
Default disabled
Format ip pim bsr-border
Mode Interface Config
(NETGEAR) (Interface 1/0/1) #ip pim bsr-border
no ip pim bsr-border
Use this command to disable the specified interface from being the BSR border.
Format no ip pim bsr-border
Mode Interface Config
IP Multicast Commands 1030
