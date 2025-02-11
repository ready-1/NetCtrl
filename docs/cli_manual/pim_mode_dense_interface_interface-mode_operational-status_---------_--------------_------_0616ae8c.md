# pim_mode_dense_interface_interface-mode_operational-status_---------_--------------_------_0616ae8c

Pages: 1072-1072

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
default Defines the SSM range access list FF3x::/32.
no ipv6 pim ssm
Use this command to remove the Source Specific Multicast (SSM) range of IP multicast
addresses on the router.
Format no ipv6 pim ssm {default | group-address group-mask}
Mode Global Config
show ipv6 pim
This command displays the system-wide information for PIM-DM or PIM-SM.
Format show ipv6 pim
Modes Privileged EXEC
User EXEC
Note: If the PIM mode is PIM-DM (dense), some of the fields in the following
table do not display in the command output because they are
applicable only to PIM-SM.
Term Definition
PIM Mode Indicates whether the PIM mode is dense (PIM-DM) or sparse (PIM-SM)
Interface unit/slot/port
Interface Mode Indicates whether PIM is enabled or disabled on this interface.
Operational Status The current state of PIM on this interface: Operational or Non-Operational.
The following example displays PIM Mode - Dense:
(NETGEAR) #show ipv6 pim
PIM Mode Dense
Interface Interface-Mode Operational-Status
--------- -------------- ------------------
1/0/1 Enabled Operational
1/0/3 Disabled Non-Operational
IPv6 Multicast Commands 1072
