# ip_multicast_commands_1043

Pages: 1043-1043

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format show ip pim rp mapping [rp-address | candidate | static]
Modes Privileged EXEC
User EXEC
Term Definition
RP Address The IP address of the RP for the group specified.
Group Address The IP address of the multicast group.
Group Mask The subnet mask associated with the group.
Origin Indicates the mechanism (BSR or static) by which the RP was selected.
C-RP Indicates the configured C-RP Advertisement interval with which the router acting as a Candidate
Advertisement RP will periodically send the C-RP advertisement messages to the elected BSR.
Interval
Command example:
(NETGEAR) #show ip pim rp mapping 192.168.10.1
RP Address 192.168.10.1
Group Address 224.1.2.1
Group Mask 255.255.255.0
Origin Static
Command example:
(NETGEAR) #show ip pim rp mapping
R P Address 192.168.10.1
Group Address 224.1.2.1
Group Mask 255.255.255.0
Origin Static
RP Address 192.168.20.1
Group Address 229.2.0.0
Group Mask 255.255.0.0
Origin Static
Command example:
(NETGEAR) # show ip pim rp mapping candidate
RP Address.................................... 192.168.10.1
Group Address.............................. 224.1.2.1
Group Mask................................. 255.255.0.0
Origin..................................... BSR
IP Multicast Commands 1043
