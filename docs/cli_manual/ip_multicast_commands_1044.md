# ip_multicast_commands_1044

Pages: 1044-1044

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
C-RP Advertisement Interval (secs)......... 60
Next Candidate RP Advertisement (hh:mm:ss). 00:00:15
Command example:
If no RP Group mapping exist on the router, the following message is displayed:
No RP-Group mappings exist on this router.
show ip pim statistics
This command displays statistics for the received PIM control packets per interface. This
command displays statistics only if PIM sparse mode is enabled.
Format show ip pim statistics
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
(NETGEAR) #show ip pim statistics
=====================================================================
Interface Stat Hello Register Reg-Stop Join/Pru BSR Assert CRP
=====================================================================
Vl10 Rx 0 0 0 0 0 0 0
Tx 2 0 0 0 0 0 0
Invalid Packets Received - 0
---------------------------------------------------------------------
Vl20 Rx 0 0 0 5 0 0 0
Tx 8 7 0 0 0 0 0
IP Multicast Commands 1044
