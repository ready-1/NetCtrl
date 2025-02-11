# dhcp_and_bootp_relay_commands

Pages: 715-716

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Accept Mode.................................... Enable
State.......................................... Initialized
T rack Interface State DecrementPriority
- -------------- - ----- ------------------
< 1/0/1> d own 10
T rackRoute (pfx/len) S tate DecrementPriority
- ----------------------- ------ ------------------
1 0.10.10.1/255.255.255.0 d own 10
show ip vrrp interface brief
This command displays information about each virtual router configured on the switch. This
command takes no options. It displays information about each virtual router.
Format show ip vrrp interface brief
Modes Privileged EXEC
User EXEC
Term Definition
Interface unit/slot/port
VRID The router ID of the virtual router.
IP Address The virtual router IP address.
Mode Indicates whether the virtual router is enabled or disabled.
State The state (Master/backup) of the virtual router.
clear ip vrrp interface stats
This command clears VRRP statistical information from an interface or a VLAN. The virtual
router ID, vrid, is an integer value that ranges from 1 to 255.
Format clear ip vrrp interface stats {unit/slot/port vrid} | {vlan vlan-id vrid}
Modes Interface Config
DHCP and BootP Relay Commands
This section describes the commands you use to configure BootP/DHCP Relay on the
switch. A DHCP relay agent operates at Layer 3 and forwards DHCP requests and replies
between clients and servers when they are not on the same physical subnet.
Routing Commands 715

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
bootpdhcprelay cidoptmode
This command enables the circuit ID option mode for BootP/DHCP Relay on the system.
Default disabled
Format bootpdhcprelay cidoptmode
Mode Global Config
no bootpdhcprelay cidoptmode
This command disables the circuit ID option mode for BootP/DHCP Relay on the system.
Format no bootpdhcprelay cidoptmode
Mode Global Config
bootpdhcprelay maxhopcount
This command configures the maximum allowable relay agent hops for BootP/DHCP Relay
on the system. The hops parameter has a range of 1 to 16.
Default 4
Format bootpdhcprelay maxhopcount hops
Mode Global Config
no bootpdhcprelay maxhopcount
This command configures the default maximum allowable relay agent hops for BootP/DHCP
Relay on the system.
Format no bootpdhcprelay maxhopcount
Mode Global Config
bootpdhcprelay minwaittime
This command configures the minimum wait time in seconds for BootP/DHCP Relay on the
system. When the BootP relay agent receives a BOOTREQUEST message, it can use the
seconds-since-client-began-booting field of the request as a factor in deciding whether to
relay the request or not. The minwaittime seconds parameter has a range of 0 to 100
seconds.
Default 0
Format bootpdhcprelay minwaittime seconds
Mode Global Config
Routing Commands 716
