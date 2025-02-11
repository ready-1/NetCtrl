# stp_stp_port_interface_mode_type_state_role_desc_---------_--------_-------_--------------_8ddccb13

Pages: 414-414

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Port Role The role of the specified port within the spanning tree.
Desc Indicates whether the port is in loop inconsistent state or not. This field is blank if the loop guard
feature is not available.
Command example:
The following example shows output in the slot/port format:
(NETGEAR Switch) #show spanning-tree mst port summary 0 0/1
MST Instance ID................................ CST
STP STP Port
Interface Mode Type State Role Desc
--------- -------- ------- ----------------- ---------- ----------
0/1 Enabled Disabled Disabled
Command example:
The following example shows output using a LAG interface number:
(NETGEAR Switch) #show spanning-tree mst port summary 0 lag 1
MST Instance ID................................ CST
STP STP Port
Interface Mode Type State Role Desc
--------- -------- ------- ----------------- ---------- ----------
3/1 Enabled Disabled Disabled
show spanning-tree mst port summary active
This command displays settings for the ports within the specified multiple spanning tree
instance that are active links.
Format show spanning-tree mst port summary mstid active
Mode Privileged EXEC
User EXEC
Term Definition
MST Instance ID The ID of the existing MST instance.
Interface The interface.
STP Mode Indicates whether spanning tree is enabled or disabled on the port.
Switching Commands 414
