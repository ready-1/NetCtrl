# mvr_group_ip_status_members_------------------_---------------_---------------------

Pages: 566-566

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
MVR Max Multicast Groups The maximum number of multicast groups supported by MVR.
MVR Current multicast groups The current number of MVR groups allocated.
MVR Query response time The current MVR query response time.
MVR Mode The current MVR mode. It can be compatible or dynamic.
Command example:
(NETGEAR Switch)#show mvr
MVR Running…........................... TRUE
MVR multicast VLAN….................... 1200
MVR Max Multicast Groups….............. 256
MVR Current multicast groups….......... 1
MVR Global query response time…........ 10 (tenths of sec)
MVR Mode….............................. compatible
show mvr members
This command displays the MVR membership groups allocated. A.B.C.D is a valid multicast
address in IPv4 dotted notation.
Format show mvr members [A.B.C.D]
Mode Privileged EXEC
The following table describes the output parameters.
Term Definition
MVR Group IP MVR group multicast IP address.
Status The status of the specific MVR group. It can be active or inactive.
Members The list of ports that participates in the specified MVR group.
Command example:
(NETGEAR Switch)#show mvr members
MVR Group IP Status Members
------------------ --------------- ---------------------
2 24.1.1.1 INACTIVE 0/1, 0/2, 0/3
(switch)#show mvr members 224.1.1.1
MVR Group IP Status Members
------------------ --------------- ---------------------
2 24.1.1.1 INACTIVE 0/1, 0/2, 0/3
Switching Commands 566
