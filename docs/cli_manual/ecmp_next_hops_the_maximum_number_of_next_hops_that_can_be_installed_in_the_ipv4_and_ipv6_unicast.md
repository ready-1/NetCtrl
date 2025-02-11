# ecmp_next_hops_the_maximum_number_of_next_hops_that_can_be_installed_in_the_ipv4_and_ipv6_unicast

Pages: 336-340

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show sdm prefer
Use this command to view the currently active SDM template and its scaling parameters, or
to view the scaling parameters for an inactive template. When invoked with no optional
keywords, this command lists the currently active template and the template that will become
active on the next reboot, if it is different from the currently active template. If the system
boots with a non-default template, and you clear the template configuration, either using no
sdm prefer or by deleting the startup configuration, show sdm prefer lists the default
template as the next active template. To list the scaling parameters of a specific template,
use that template’s keyword as an argument to the command.
Use the optional keywords to list the scaling parameters of a specific template.
Format show sdm prefer [dual-ipv4-and-ipv6 {data-center-generic |
data-center-m4396only | data-center-mixed-native-m4396 | data-center-native}
| ipv4-routing data-center {plus-generic | plus-m4396only |
plus-mixed-native-m4396 | plus-native}]
Mode Privileged EXEC
Field Description
ARP Entries The maximum number of entries in the IPv4 Address Resolution Protocol (ARP) cache
for routing interfaces.
IPv4 Unicast Routes The maximum number of IPv4 unicast forwarding table entries.
IPv6 NDP Entries The maximum number of IPv6 Neighbor Discovery Protocol (NDP) cache entries.
IPv6 Unicast Routes The maximum number of IPv6 unicast forwarding table entries.
ECMP Next Hops The maximum number of next hops that can be installed in the IPv4 and IPv6 unicast
forwarding tables.
Command example:
The following example shows the SDM template when the next active SDM template is not
changed:
(NETGEAR Switch)#show sdm prefer
The current template is the 'dual ipv4 and ipv6 data center generic' template.
ARP Entries.................................... 1536
IPv4 Unicast Routes............................ 512
IPv6 NDP Entries............................... 512
IPv6 Unicast Routes............................ 256
ECMP Next Hops................................. 4
IPv4 Multicast Routes.......................... 96
IPv6 Multicast Routes.......................... 32
Maximum VLAN Entries........................... 4093
Utility Commands 336

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
The following example shows the SDM template when the next active SDM template is
configured:
(NETGEAR Switch) (Config)#sdm prefer ipv4-routing data-center plus-generic
Changes to the running SDM preferences have been stored, but cannot take effect until the
next reload.
Use 'show sdm prefer' to see what SDM preference is currently active.
(NETGEAR Switch)#show sdm prefer
The current template is the 'dual ipv4 and ipv6 data center generic' template.
ARP Entries.................................... 1536
IPv4 Unicast Routes............................ 512
IPv6 NDP Entries............................... 512
IPv6 Unicast Routes............................ 256
ECMP Next Hops................................. 4
IPv4 Multicast Routes.......................... 96
IPv6 Multicast Routes.......................... 32
Maximum VLAN Entries........................... 4093
On the next reload, the template will be the 'ipv4 data center plus generic' template.
Green Ethernet Commands
This section describes the commands you use to configure Green Ethernet modes on the
system. The purpose of the Green Ethernet features is to save power. The switch supports
the following Green Ethernet modes:
• Energy-detect mode
• Energy-efficient Ethernet (EEE) mode
Note: Only 1G copper ports support energy-detect mode.
green-mode energy-detect
Use this command to enable energy-detect mode on an interface or on a range of interfaces.
With this mode enabled, when the port link is down, the port automatically powers down for
short period of time and then wakes up to check link pulses. In energy-detect mode, the port
can perform auto-negotiation and consume less power when no link partner is present.
Utility Commands 337

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default disabled
Format green-mode energy-detect
Mode Interface Config
no green-mode energy-detect
Use this command to disable energy-detect mode on the interface(s).
Format no green-mode energy-detect
Mode Interface Config
green-mode eee
Use this command to enable EEE low-power idle mode on an interface or on a range of
interfaces. The EEE mode enables both send and receive sides of the link to disable some
functionality for power saving when lightly loaded. The transition to EEE low-power mode
does not change the port link status. Frames in transit are not dropped or corrupted in
transition to and from this mode.
Default disabled
Format green-mode eee
Mode Interface Config
no green-mode eee
Use this command to disable EEE mode on the interface(s).
Format no green-mode eee
Mode Interface Config
green-mode eee tx-idle-time
Use this command to configure the EEE mode transmit idle time for an interface or range of
interfaces. The idle time is in microseconds (0–4294977295). The transmit idle time is the
amount of time the port waits before moving to the MAC TX transitions to the LPI state.
Default 0
Format green-mode eee tx-idle-time microseconds
Mode Interface Config
Utility Commands 338

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no green-mode eee tx-idle-time
Use this command to return the EEE idle time to the default value.
Format no green-mode eee tx-idle-time
Mode Interface Config
green-mode eee tx-wake-time
Use this command to configure the EEE mode transmit wake time for an interface or range of
interfaces. The wake time is in microseconds (0–65535). The transmit wake time is the
amount of time the switch must wait to go back to the ACTIVE state from the LPI state when
it receives a packet for transmission.
Default 0
Format green-mode eee tx-wake-time microseconds
Mode Interface Config
no green-mode eee tx-wake-time
Use this command to return the EEE wake time to the default value.
Format no green-mode eee tx-wake-time
Mode Interface Config
green-mode eee-lpi-history sampling-interval
Use this command to configure global EEE LPI history collection interval for the system. The
value specified in this command is applied globally on all interfaces in the switch. The
s ampling interval unit is seconds (30– 36000).
Note: The sampling interval takes effect immediately; the current and future
samples are collected at this new sampling interval.
Default 3600 seconds
Format green-mode eee-lpi-history seconds
Mode Global Config
Utility Commands 339

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no green-mode eee-lpi-history sampling-interval
Use this command to return the global EEE LPI history collection interval to the default value.
Format no green-mode eee-lpi-history sampling-interval
Mode Global Config
green-mode eee-lpi-history max-samples
Use this command to configure global EEE LPI history collection buffer size for the system.
The size value ( 1– 168) specified in this command is applied globally on all interfaces in the
switch.
Default 168
Format green-mode eee-lpi-history max-samples size
Mode Global Config
no green-mode eee-lpi-history max samples
Use this command to return the global EEE LPI history collection buffer size to the default
value.
Format no green-mode eee-lpi-history max-samples
Mode Global Config
show green-mode
Use this command to display the green-mode configuration and operational status on all
ports or on the specified port.
Note: The fields that display in the show green-mode command output
depend on the Green Ethernet modes available on the hardware
platform.
Format show green-mode [unit/slot/port]
Mode Privileged EXEC
Utility Commands 340
