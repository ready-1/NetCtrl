# m4300-96x_172_26_2_114_http_tcp_local_80_path

Pages: 655-663

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Service Name The Bonjour service name on the switch.
Type The Bonjour service type name on the switch.
Domain The Bonjour service domain name on the switch.
Port The Bonjour service port number on the switch.
TXT data The Bonjour service text on the switch.
Command example:
(Netgear Switch) #show bonjour
Bonjour Administration Mode: Enabled
Published Services:
# S ervice Name Type Domain Port TXT data
- -- ----------------------- - ------------ - --------- - ---- ----------
1 M4300-96X.172.26.2.114 _http._tcp. local. 80 path=/
2 M4300-96X.172.26.2.114 _telnet._tcp. local. 23
Switching Commands 655

Routing Commands

This chapter describes the routing commands.
The chapter contains the following sections:
• Address Resolution Protocol Commands
• IP Routing Commands
• Routing Policy Commands
• Router Discovery Protocol Commands
• Virtual LAN Routing Commands
• Virtual Router Redundancy Protocol Commands
• DHCP and BootP Relay Commands
• IP Helper Commands
• Open Shortest Path First Commands
• OSPF Graceful Restart Commands
• Routing Information Protocol Commands
• ICMP Throttling Commands
The commands in this chapter are in one of three functional groups:
• Show commands. Display switch settings, statistics, and other information.
• Configuration commands. Configure features and options of the switch. For every
configuration command, there is a show command that displays the configuration setting.
• Clear commands. Clear some or all of the settings to factory defaults.

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Address Resolution Protocol Commands
This section describes the commands you use to configure Address Resolution Protocol
(ARP) and to view ARP information on the switch. ARP associates IP addresses with MAC
addresses and stores the information as ARP entries in the ARP cache.
arp
This command creates an ARP entry. The value for ipaddress is the IP address of a device
on a subnet attached to an existing routing interface. The parameter macaddr is a unicast
MAC address for that device. The interface parameter specifies the next hop interface.
The format of the MAC address is 6 two-digit hexadecimal numbers that are separated by
colons, for example 00:06:29:32:81:40
Format arp ipaddress macaddr interface {unit/slot/port | vlan id}
Mode Global Config
no arp
This command deletes an ARP entry. The value for ipaddress is the IP address of a device
on a subnet attached to an existing routing interface. The parameter macaddr is a unicast
MAC address for that device. The interface parameter specifies the next hop interface.
Format arp ipaddress macaddr interface {unit/slot/port}
Mode Global Config
ip proxy-arp
This command enables proxy ARP on a router interface or range of interfaces. Without proxy
ARP, a device only responds to an ARP request if the target IP address is an address
configured on the interface where the ARP request arrived. With proxy ARP, the device may
also respond if the target IP address is reachable. The device only responds if all next hops
in its route to the destination are through interfaces other than the interface that received the
ARP request.
Default enabled
Format ip proxy-arp
Mode Interface Config
Routing Commands 657

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip proxy-arp
This command disables proxy ARP on a router interface.
Format no ip proxy-arp
Mode Interface Config
ip local-proxy-arp
Use this command to allow an interface to respond to ARP requests for IP addresses within
the subnet and to forward traffic between hosts in the subnet.
Default disabled
Format ip local-proxy-arp
Mode Interface Config
no ip local-proxy-arp
This command resets the local proxy ARP mode on the interface to the default value.
Format no ip local-proxy-arp
Mode Interface Config
arp cachesize
This command configures the ARP cache size. The ARP cache size value is a platform
specific integer value. The default size also varies depending on the platform.
Format arp cachesize platform-specific-integer-value
Mode Global Config
no arp cachesize
This command configures the default ARP cache size.
Format no arp cachesize
Mode Global Config
arp dynamicrenew
This command enables the ARP component to automatically renew dynamic ARP entries
when they age out. When an ARP entry reaches its maximum age, the system must decide
whether to retain or delete the entry. If the entry has recently been used to forward data
packets, the system will renew the entry by sending an ARP request to the neighbor. If the
neighbor responds, the age of the ARP cache entry is reset to 0 without removing the entry
Routing Commands 658

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
from the hardware. Traffic to the host continues to be forwarded in hardware without
interruption. If the entry is not being used to forward data packets, then the entry is deleted
from the ARP cache, unless the dynamic renew option is enabled. If the dynamic renew
option is enabled, the system sends an ARP request to renew the entry. When an entry is not
renewed, it is removed from the hardware and subsequent data packets to the host trigger an
ARP request. Traffic to the host may be lost until the router receives an ARP reply from the
host. Gateway entries, entries for a neighbor router, are always renewed. The dynamic renew
option applies only to host entries.
The disadvantage of enabling dynamic renew is that once an ARP cache entry is created,
that cache entry continues to take space in the ARP cache as long as the neighbor continues
to respond to ARP requests, even if no traffic is being forwarded to the neighbor. In a network
where the number of potential neighbors is greater than the ARP cache capacity, enabling
dynamic renew could prevent some neighbors from communicating because the ARP cache
is full.
Default disabled
Format arp dynamicrenew
Mode Privileged EXEC
no arp dynamicrenew
This command prevents dynamic ARP entries from renewing when they age out.
Format no arp dynamicrenew
Mode Privileged EXEC
arp purge
This command causes the specified IP address to be removed from the ARP cache. Only
entries of type dynamic or gateway are affected by this command.
The ipaddr parameter is the IP address that must be removed from the ARP cache.
The optional interface keyword and its associated parameters specify the interface from
which the IP address must be removed.
Format arp purge ipaddr [interface {unit/slot/port | vlan-id}]
Mode Privileged EXEC
Routing Commands 659

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
arp resptime
This command configures the ARP request response time-out.
The value for seconds is a valid positive integer, which represents the IP ARP entry response
time-out time in seconds. The range for seconds is between 1-10 seconds.
Default 1
Format arp resptime seconds
Mode Global Config
no arp resptime
This command configures the default ARP request response timeout.
Format no arp resptime
Mode Global Config
arp retries
This command configures the ARP count of maximum request for retries.
The value for retries is an integer, which represents the maximum number of request for
retries. The range for retries is an integer between 0-10 retries.
Default 4
Format arp retries retries
Mode Global Config
no arp retries
This command configures the default ARP count of maximum request for retries.
Format no arp retries
Mode Global Config
arp timeout
This command configures the ARP entry ageout time.
The value for seconds is a valid positive integer, which represents the IP ARP entry ageout
time in seconds. The range for seconds is between 15-21600 seconds.
Routing Commands 660

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default 1200
Format arp timeout seconds
Mode Global Config
no arp timeout
This command configures the default ARP entry ageout time.
Format no arp timeout
Mode Global Config
clear arp-cache
This command causes all ARP entries of type dynamic to be removed from the ARP cache. If
the gateway keyword is specified, the dynamic entries of type gateway are purged as well.
Format clear arp-cache [gateway]
Mode Privileged EXEC
load-interval
This command changes the length of time for which data is used to compute load statistics.
You must enter the time in seconds, and the time must be a multiple of 30, in a range from
30–600 seconds. The smaller the value of the load interval, the more accurate the
instantaneous rate of the load statistics. However, a small value can affect the performance
of the switch.
Default 300 seconds
Format load-interval interval
Mode Interface Config
no load-interval
This command resets the load interval on the interface to the default value.
Format no load-interval
Mode Interface Config
Routing Commands 661

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
clear arp-switch
Use this command to clear the contents of the switch’s Address Resolution Protocol (ARP)
table that contains entries learned through the Management port. To observe whether this
command is successful, ping from the remote system to the switch. Issue the show arp
switch command to see the ARP entries. Then issue the clear arp-switch command
and check the show arp switch entries: ARP entries are no longer shown.
Format clear arp-switch
Mode Privileged EXEC
show arp
This command displays the Address Resolution Protocol (ARP) cache. The displayed results
are not the total ARP entries. To view the total ARP entries, the view the output of the show
arp command in conjunction with the output of the show arp switch command.
Format show arp
Mode Privileged EXEC
Term Definition
Age Time (seconds) The time it takes for an ARP entry to age out. This is configurable. Age time is measured in
seconds.
Response Time The time it takes for an ARP request timeout. This value is configurable. Response time is
(seconds) measured in seconds.
Retries The maximum number of times an ARP request is retried. This value is configurable.
Cache Size The maximum number of entries in the ARP table. This value is configurable.
Dynamic Renew Displays whether the ARP component automatically attempts to renew dynamic ARP entries when
Mode they age out.
Total Entry Count The total entries in the ARP table and the peak entry count in the ARP table.
Current / Peak
Static Entry Count The static entry count in the ARP table and maximum static entry count in the ARP table.
Current / Max
The following are displayed for each ARP entry:
Term Definition
IP Address The IP address of a device on a subnet attached to an existing routing interface.
MAC Address The hardware MAC address of that device.
Interface The routing unit/slot/port associated with the device ARP entry.
Routing Commands 662

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Type The type that is configurable. The possible values are Local, Gateway, Dynamic and Static.
Age The current age of the ARP entry since last refresh (in hh:mm:ss format)
show arp brief
This command displays the brief Address Resolution Protocol (ARP) table information.
Format show arp brief
Mode Privileged EXEC
Term Definition
Age Time The time it takes for an ARP entry to age out. This value is configurable. Age time is measured in
(seconds) seconds.
Response Time The time it takes for an ARP request timeout. This value is configurable. Response time is measured
(seconds) in seconds.
Retries The maximum number of times an ARP request is retried. This value is configurable.
Cache Size The maximum number of entries in the ARP table. This value is configurable.
Dynamic Renew Displays whether the ARP component automatically attempts to renew dynamic ARP entries when
Mode they age out.
Total Entry Count The total entries in the ARP table and the peak entry count in the ARP table.
Current / Peak
Static Entry Count The static entry count in the ARP table and maximum static entry count in the ARP table.
Current / Max
show arp switch (Address Resolution Protocol commands)
This command displays the contents of the switch’s Address Resolution Protocol (ARP)
table.
Format show arp switch
Mode Privileged EXEC
Term Definition
IP Address The IP address of a device on a subnet attached to the switch.
MAC Address The hardware MAC address of that device.
Interface The routing unit/slot/port associated with the device’s ARP entry.
Routing Commands 663
