# pim_mode_sparse_interface_i_nterface-mode_operational-status_---------_--------------_----_6208f554

Pages: 1038-1038

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
PIM Mode Sparse
Interface I nterface-Mode Operational-Status
--------- -------------- ------------------
1/0/1 Enabled Operational
1/0/3 Disabled Non-Operational
Command example:
The following example shows that PIM is not configured:
(NETGEAR) #show ip pim
PIM Mode None
None of the routing interfaces are enabled for PIM.
show ip pim ssm
This command displays the configured source specific IP multicast addresses.
Format show ip pim ssm
Modes Privileged EXEC
User EXEC
Term Definition
Group Address The IP multicast address of the SSM group.
Prefix Length The network prefix length.
Command example:
(NETGEAR) #show ip pim ssm
Group Address/Prefix Length
----------------------------
232.0.0.0/8
Command example:
If no SSM group range is configured, the command displays the following message:
No SSM address range is configured.
show ip pim interface
This command displays the PIM interface status parameters.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
IP Multicast Commands 1038
