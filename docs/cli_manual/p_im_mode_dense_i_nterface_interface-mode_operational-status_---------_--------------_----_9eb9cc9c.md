# p_im_mode_dense_i_nterface_interface-mode_operational-status_---------_--------------_----_9eb9cc9c

Pages: 1037-1037

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Current multicast IPv4 protocol................ PIMSM
Current multicast IPv6 protocol................ No protocol enabled.
Total software forwarded packets .............. 0
Source address: 192.168.10.5
Group address: 225.1.1.1
Packets forwarded in software for this entry: 0 Protocol: PIM-SM
Expiry Time (secs): 206 Up Time (secs): 4
Incoming interface: 1/0/10 Outgoing interface list: None
show ip pim
This command displays the system-wide information for PIM-DM or PIM-SM.
Format show ip pim
Modes Privileged EXEC
User EXEC
Note: If the PIM mode is PIM-DM (dense), some of the fields in the following
table do not display in the command output because they are
applicable only to PIM-SM.
Term Definition
PIM Mode Indicates the configured mode of the PIM protocol as dense (PIM-DM) or sparse
(PIM-SM)
Interface unit/slot/port
Interface Mode Indicates whether PIM is enabled or disabled on this interface.
Operational Status The current state of PIM on this interface: Operational or Non-Operational.
The following example shows PIM Mode - Dense:
(NETGEAR) #show ip pim
P IM Mode Dense
I nterface Interface-Mode Operational-Status
--------- -------------- ------------------
1/0/1 Enabled Operational
1/0/3 Disabled Non-Operational
Command example:
The following example shows PIM Mode - Sparse
(NETGEAR) #show ip pim
IP Multicast Commands 1037
