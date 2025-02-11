# p_im_mode_sparse_interface_interface-mode_operational-status_---------_--------------_----_79c2df9b

Pages: 1073-1079

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
The following example displays PIM Mode - Sparse:
(NETGEAR) #show ipv6 pim
P IM Mode Sparse
Interface Interface-Mode Operational-Status
--------- -------------- ------------------
1/0/1 Enabled Operational
1/0/3 Disabled Non-Operational
Command example:
The following example shows that PIM is not configured:
(NETGEAR) #show ipv6 pim
PIM Mode None
None of the routing interfaces are enabled for PIM.
show ipv6 pim ssm
This command displays the configured source specific IPv6 multicast addresses. If no SSM
Group range is configured, the command output show the following message:
No SSM address range is configured.
Format show ipv6 pim ssm
Modes Privileged EXEC
User EXEC
Term Definition
Group Address The IPv6 multicast address of the SSM group.
Prefix Length The network prefix length.
show ipv6 pim interface
This command displays the interface information for PIM on the specified interface.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
IPv6 Multicast Commands 1073

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If no interface is specified, the command displays the status parameters for all PIM-enabled
interfaces.
Format show ipv6 pim interface [unit/slot/port | vlan vland-id]
Modes Privileged EXEC
User EXEC
Term Definition
Interface unit/slot/port
Mode Indicates whether the PIM mode enabled on the interface is dense or sparse.
Hello Interval The frequency at which PIM hello messages are transmitted on this interface. By default, the value is
30 seconds.
Join Prune Interval The join/prune interval for the PIM router. The interval is in seconds.
DR Priority The priority of the Designated Router configured on the interface. This field is not applicable if the
interface mode is Dense
BSR Border Identifies whether this interface is configured as a bootstrap router border interface.
Neighbor Count The number of PIM neighbors learned on this interface. This is a dynamic value and is shown only
when a PIM interface is operational.
Designated Router The IP address of the elected Designated Router for this interface. This is a dynamic value and will
only be shown when a PIM interface is operational. This field is not applicable if the interface mode
is Dense
Command example:
(NETGEAR) #show ipv6 pim interface
Interface.........................................1/0/1
Mode............................................Sparse
Hello Interval (secs)...........................30
Join Prune Interval (secs)......................60
DR Priority.....................................1
BSR Border......................................Disabled
Neighbor Count..................................1
Designated Router...............................192.168.10.1
Interface.........................................1/0/2
Mode............................................Sparse
Hello Interval (secs)...........................30
Join Prune Interval (secs)......................60
DR Priority.....................................1
BSR Border......................................Disabled
Neighbor Count..................................1
Designated Router...............................192.168.10.1
IPv6 Multicast Commands 1074

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
If none of the interfaces are enabled for PIM, the following message is displayed:
None of the routing interfaces are enabled for PIM.
show ipv6 pim neighbor
This command displays PIM neighbors discovered by PIMv2 Hello messages.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
If the interface number is not specified, this command displays the neighbors discovered on
all the PIM-enabled interfaces.
Format show ipv6 pim neighbor [{unit/slot/port | vlan vland-id]
Modes Privileged EXEC
User EXEC
Term Definition
Neighbor Address The IPv6 address of the PIM neighbor on an interface.
Interface unit/slot/port
Up Time The time since this neighbor has become active on this interface.
Expiry Time Time remaining for the neighbor to expire.
DR Priority The DR Priority configured on this Interface (PIM-SM only).
Note: DR Priority is applicable only when sparse-mode configured routers are neighbors.
Otherwise, NA is displayed in this field.
Command example:
(NETGEAR) #show ipv6 pim neighbor
Neighbor Addr I nterface Uptime Expiry Time
( HH:MM::SS) (HH:MM::SS)
- ---------------- - -------- ----------- -----------
2001:DB8:39::/32 1/0/1 00:02:55 00:01:15
2 001:DB8:A3::/32 1/0/2 00:03:50 00:02:10
Command example:
If no neighbors were learned on any of the interfaces, the following message is displayed:
No neighbors are learnt on any interface.
IPv6 Multicast Commands 1075

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ipv6 pim bsr-router
This command displays the bootstrap router (BSR) information.
Format show ipv6 pim bsr-router {candidate | elected}
Mode Privileged EXEC
User EXEC
Term Definition
BSR Address IPv6 address of the BSR.
BSR Priority Priority as configured in the ipv6 pim bsr-candidate command.
BSR Hash Mask Length Length of a mask (maximum 32 bits) that is to be ANDed with the group address before the
hash function is called. This value is configured in the ipv6 pim bsr-candidate command.
C-BSR Advertisement Indicates the configured C-BSR Advertisement interval with which the router, acting as a
Interval C-BSR, will periodically send the C-BSR advertisement messages.
Next Bootstrap Time (in hours, minutes, and seconds) in which the next bootstrap message is due from this
Message BSR.
Command example:
(NETGEAR) #show ipv6 pim bsr-router elected
BSR Address................................... 192.168.10.1
BSR Priority................................ 0
BSR Hash Mask Length........................ 30
Next Bootstrap message (hh:mm:ss)........... 00:00:24
Command example:
(NETGEAR) #show ipv6 pim bsr-router candidate
BSR Address................................... 192.168.10.1
BSR Priority................................ 0
BSR Hash Mask Length........................ 30
C-BSR Advertisement Interval (secs)......... 60
Next Bootstrap message (hh:mm:ss)........... NA
Command example:
If no configured or elected BSRs exist on the router, the following message is displayed:
No BSR's exist/learned on this router.
IPv6 Multicast Commands 1076

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ipv6 pim rp-hash
This command displays which rendezvous point (RP) is being used for a specified group that
you must specify with the group-address argument.
Format show ipv6 pim rp-hash group-address
Modes Privileged EXEC
User EXEC
Term Definition
RP Address The IPv6 address of the RP for the group specified.
Type Indicates the mechanism (BSR or static) by which the RP was selected.
Command example:
(NETGEAR) #show ipv6 pim rp-hash 224.1.2.0
RP Address192.168.10.1
Type Static
Command example:
If no RP Group mapping exists on the router, the following message is displayed:
No RP-Group mappings exist/learned on this router.
show ipv6 pim rp mapping
Use this command to display the mapping for the PIM group to the active Rendezvous points
(RP) of which the router is a aware (either configured or learned from the bootstrap router
[BSR]). Use the optional parameters to limit the display to a specific RP address
(rp-address) or to view group-to-candidate RP (candidate) or group to Static RP
mapping information (static).
Format show ipv6 pim rp mapping [rp-address | candidate | static]
Modes Privileged EXEC
User EXEC
Term Definition
RP Address The IPv6 address of the RP for the group specified.
Group Address The IPv6 address and prefix length of the multicast group.
IPv6 Multicast Commands 1077

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Origin Indicates the mechanism (BSR or static) by which the RP was selected.
C-RP Indicates the configured C-RP Advertisement interval with which the router acting as a Candidate
Advertisement RP will periodically send the C-RP advertisement messages to the elected BSR.
Interval
Command example:
(NETGEAR) #show ipv6 pim rp mapping 192.168.10.1
R P Address 192.168.10.1
Group Address 224.1.2.1
Group Mask 255.255.255.0
Origin Static
Command example:
(NETGEAR) #show ipv6 pim rp mapping
RP Address 192.168.10.1
Group Address 224.1.2.1
Group Mask 255.255.255.0
Origin Static
R P Address 192.168.20.1
Group Address 229.2.0.0
Group Mask 255.255.0.0
Origin Static
Command example:
(NETGEAR) # show ipv6 pim rp mapping candidate
RP Address.................................... 192.168.10.1
Group Address.............................. 224.1.2.1
Group Mask................................. 255.255.0.0
Origin..................................... BSR
C-RP Advertisement Interval (secs)......... 60
Next Candidate RP Advertisement (hh:mm:ss). 00:00:15
Command example:
If no RP Group mapping exist on the router, the following message is displayed:
No RP-Group mappings exist on this router.
IPv6 Multicast Commands 1078

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ipv6 pim statistics
This command displays statistics for the received PIM control packets per interface. This
command displays statistics only if PIM sparse mode is enabled.
Format show ipv6 pim statistics
Modes Privileged EXEC
User EXEC
Term Definition
Stat • Rx packets received.
• Tx packets transmitted.
Interface The PIM-enabled routing interface.
Hello The number of PIM Hello messages.
Register The number of PIM Register messages.
Reg-Stop The number of PIM Register-stop messages.
Join/Pru The number of PIM Join/Prune messages.
BSR The number of PIM Boot Strap messages.
Assert The number of PIM Assert messages.
CRP The number of PIM Candidate RP Advertisement messages.
Command example:
(NETGEAR) #show ipv6 pim statistics
=====================================================================
Interface Stat Hello Register Reg-Stop Join/Pru BSR Assert CRP
=====================================================================
Vl10 Rx 0 0 0 0 0 0 0
Tx 2 0 0 0 0 0 0
Invalid Packets Received - 0
---------------------------------------------------------------------
Vl20 Rx 0 0 0 5 0 0 0
Tx 8 7 0 0 0 0 0
Invalid Packets Received - 0
---------------------------------------------------------------------
1/0/5 Rx 0 0 6 5 0 0 0
Tx 10 9 0 0 0 0 0
Invalid Packets Received - 0
---------------------------------------------------------------------
IPv6 Multicast Commands 1079
