# static_active

Pages: 567-567

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show mvr interface
This command displays the MVR-enabled interfaces configuration.
Format show mvr interface [interface-id [members [vlan vid]]]
Mode Privileged EXEC
The following table explains the output parameters.
Term Description
Port Interface number
Type The MVR port type. It can be none, receiver, or source type.
Status The interface status. It consists of two characteristics:
• active or inactive indicates whether the port is forwarding.
• inVLAN or notInVLAN indicates whether the port is part of any VLAN.
Immediate Leave The state of immediate mode. It can be enabled or disabled.
Command example:
(NETGEAR Switch)#show mvr interface
Port Type Status Immediate Leave
--------- --------------- --------------------- --------------------
0/9 RECEIVER ACTIVE/inVLAN DISABLED
(switch)#show mvr interface 0/9
Type: RECEIVER Status: ACTIVE Immediate Leave: DISABLED
(switch)#show mvr interface 0/23 members
235.0.0.1 STATIC ACTIVE
(switch)#show mvr interface 0/23 members vlan 12
235.0.0.1 STATIC ACTIVE
235.1.1.1 STATIC ACTIVE
show mvr traffic
This command displays global MVR statistics.
Format show mvr traffic
Mode Privileged EXEC
Switching Commands 567
