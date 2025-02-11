# ip_multicast_commands_1056

Pages: 1056-1056

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Older Version 2 The interval used to timeout the older version 2 queriers.
Querier Timeout
Proxy Start The number of times the IGMP Proxy has been stopped and started.
Frequency
Command example:
(NETGEAR Switch) #show ip igmp-proxy
Interface Index............................................. 1/0/1
Admin Mode................................................ Enable
Operational Mode......................................... Enable
Version......................................................... 3
Num of Multicast Groups............................. 0
Unsolicited Report Interval.......................... 1
Querier IP Address on Proxy Interface........ 5.5.5.50
Older Version 1 Querier Timeout................ 0
Older Version 2 Querier Timeout................ 00::00:00
Proxy Start Frequency................................. 1
show ip igmp-proxy interface
This command displays a detailed list of the host interface status parameters. It displays the
following parameters only when you enable IGMP Proxy.
Format show ip igmp-proxy interface
Modes Privileged EXEC
User EXEC
Term Definition
Interface Index The unit/slot/port of the IGMP proxy.
The column headings of the table associated with the interface are as follows.
Term Definition
Ver The IGMP version.
Query Rcvd Number of IGMP queries received.
Report Rcvd Number of IGMP reports received.
Report Sent Number of IGMP reports sent.
IP Multicast Commands 1056
