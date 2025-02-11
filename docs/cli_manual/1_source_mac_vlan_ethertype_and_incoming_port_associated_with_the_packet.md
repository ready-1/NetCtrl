# 1 Source MAC, VLAN, EtherType, and incoming port associated with the packet

Pages: 522-539

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
port-channel load-balance
This command selects the load-balancing option used on a port-channel (LAG). Traffic is
balanced on a port-channel (LAG) by selecting one of the links in the channel over which to
transmit specific packets. The link is selected by creating a binary pattern from selected fields
in a packet, and associating that pattern with a particular link.
Load-balancing is not supported on every device. The range of options for load-balancing
may vary per device.
This command can be configured for a single interface, a range of interfaces, or all interfaces.
Instead of unit/slot/port, lag lag-intf-num can be used as an alternate way to
specify the LAG interface, in which lag-intf-num is the LAG port number.
Default 3
Format port-channel load-balance {1 | 2 | 3 | 4 | 5 | 6 | 7} {unit/slot/port | all}
Mode Interface Config
Global Config
Term Definition
1 Source MAC, VLAN, EtherType, and incoming port associated with the packet
2 Destination MAC, VLAN, EtherType, and incoming port associated with the packet
3 Source/Destination MAC, VLAN, EtherType, and incoming port associated with the packet
4 Source IP and Source TCP/UDP fields of the packet
5 Destination IP and Destination TCP/UDP Port fields of the packet
6 Source/Destination IP and source/destination TCP/UDP Port fields of the packet
7 Enhanced hashing mode
unit/slot/port Global Config Mode only: The interface is a logical unit/slot/port number of a configured
port-channel.
all Global Config Mode only: all applies the command to all currently configured port-channels.
no port-channel load-balance
This command reverts to the default load balancing configuration.
Format no port-channel load-balance {unit/slot/port | all}
Mode Interface Config
Global Config
Switching Commands 522

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
unit/slot/port Global Config Mode only: The interface is a logical unit/slot/port number of a configured port-channel.
all Global Config Mode only: all applies the command to all currently configured port-channels.
port-channel local-preference
This command enables the local-preference mode on a port-channel (LAG) interface or
range of interfaces. By default, the local-preference mode for a port-channel is disabled. This
command can be used only on port-channel interfaces.
Default Disabled
Format port-channel local-preference
Mode Interface Config
no port-channel local-preference
This command disables the local-preference mode on a port-channel.
Format no port-channel local-preference
Mode Interface Config
port-channel min-links
This command configures the port-channel’s minimum links for lag interfaces. The number
parameter can be in the range 1–8. The default is 1.
Default 1
Format port-channel min-links number
Mode Interface Config
port-channel name
This command defines a name for the port-channel (LAG). The interface is a logical
unit/slot/port for a configured port-channel, and name is an alphanumeric string up to
15 characters. Instead of unit/slot/port, lag lag-intf-num can be used as an
alternate way to specify the LAG interface, in which lag-intf-num is the LAG port number.
Format port-channel name {logical unit/slot/port} name
Mode Global Config
Switching Commands 523

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
port-channel system priority
Use this command to configure port-channel system priority. The valid range of priority is
0-65535.
Default 0x8000
Format port-channel system priority priority
Mode Global Config
no port-channel system priority
Use this command to configure the default port-channel system priority value.
Format no port-channel system priority
Mode Global Config
show lacp actor
Use this command to display LACP actor attributes. Instead of unit/slot/port, lag
lag-intf-num can be used as an alternate way to specify the LAG interface, in which
lag-intf-num is the LAG port number.
Format show lacp actor {unit/slot/port | all}
Mode Global Config
The following output parameters are displayed.
Parameter Description
System Priority The administrative value of the Key.
Actor Admin Key The administrative value of the Key.
Port Priority The priority value assigned to the Aggregation Port.
Admin State The administrative values of the actor state as transmitted by the Actor in LACPDUs.
show lacp partner
Use this command to display LACP partner attributes. Instead of unit/slot/port, lag
lag-intf-num can be used as an alternate way to specify the LAG interface, in which
lag-intf-num is the LAG port number.
Format show lacp actor {unit/slot/port | all}
Mode Privileged EXEC
Switching Commands 524

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The following output parameters are displayed.
Parameter Description
System Priority The administrative value of priority associated with the Partner’s System ID.
System-ID Represents the administrative value of the Aggregation Port’s protocol Partner’s System ID.
Admin Key The administrative value of the Key for the protocol Partner.
Port Priority The administrative value of the Key for protocol Partner.
Port-ID The administrative value of the port number for the protocol Partner.
Admin State The administrative values of the actor state for the protocol Partner.
show port-channel brief
This command displays the static capability of all port-channel (LAG) interfaces on the device
as well as a summary of individual port-channel interfaces.
Format show port-channel brief
Mode User EXEC
For each port-channel the following information is displayed.
Term Definition
Logical Interface The unit/slot/port of the logical interface.
Port-channel Name The name of port-channel (LAG) interface.
Link-State Shows whether the link is up or down.
Trap Flag Shows whether trap flags are enabled or disabled.
Type Shows whether the port-channel is statically or dynamically maintained.
Mbr Ports The members of this port-channel.
Active Ports The ports that are actively participating in the port-channel.
show port-channel
This command displays an overview of all port-channels (LAGs) on the switch.
Format show port-channel
Mode Privileged EXEC
Switching Commands 525

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Logical Interface The valid unit/slot/port number.
Port-Channel The name of this port-channel (LAG). You may enter any string of up to 15 alphanumeric characters.
Name
Link State Indicates whether the Link is up or down.
Admin Mode May be enabled or disabled. The factory default is enabled.
Type The status designating whether a particular port-channel (LAG) is statically or dynamically
maintained.
• Static. The port-channel is statically maintained.
• Dynamic. The port-channel is dynamically maintained.
Load Balance The load balance option associated with this LAG. See port-channel load-balance on page522.
Option
Local Preference Indicates whether the local preference mode is enabled or disabled.
Mode
Mbr Ports A listing of the ports that are members of this port-channel (LAG), in unit/slot/port notation.
There can be a maximum of eight ports assigned to a given port-channel (LAG).
Device Timeout For each port, lists the timeout (long or short) for Device Type (actor or partner).
Port Speed Speed of the port-channel port.
Active Ports This field lists ports that are actively participating in the port-channel (LAG).
Command example:
(NETGEAR Switch) #show port-channel 0/3/1
Local Interface................................ 0/3/1
Channel Name................................... ch1
Link State..................................... Up
Admin Mode..................................... Enabled
Type........................................... Static
Load Balance Option............................ 3
(Src/Dest MAC, VLAN, EType, incoming port)
Local Preference Mode.......................... Enabled
Mbr Device/ Port Port
Ports Timeout Speed Active
------ ------------- --------- -------
1/0/1 actor/long Auto True
partner/long
1/0/2 actor/long Auto True
partner/long
1/0/3 actor/long Auto False
Switching Commands 526

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
partner/long
1/0/4 actor/long Auto False
partner/long
show port-channel system priority
Use this command to display the port-channel system priority.
Format show port-channel system priority
Mode Privileged EXEC
show port-channel counters
Use this command to display port-channel counters for the specified port.
Format show port-channel unit/slot/port counters
Mode Privileged EXEC
Term Definition
Local Interface The valid unit/slot/port number.
Channel Name The name of this port-channel (LAG).
Link State Indicates whether the Link is up or down.
Admin Mode May be enabled or disabled. The factory default is enabled.
Port Channel Flap The number of times the port-channel was inactive.
Count
Mbr Ports The slot/port for the port member.
Mbr Flap Counters The number of times a port member is inactive, either because the link is down, or the admin state is
disabled.
Command example:
(NETGEAR Switch) #show port-channel 3/1 counters
Local Interface................................ 3/1
Channel Name................................... ch1
Link State..................................... Down
Admin Mode..................................... Enabled
Port Channel Flap Count........................ 0
Mbr Mbr Flap
Ports Counters
------ ---------
0/1 0
Switching Commands 527

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
0/2 0
0/3 1
0/4 0
0/5 0
0/6 0
0/7 0
0/8 0
clear port-channel counters
Use this command to clear and reset specified port-channel and member flap counters for
the specified interface.
Format clear port-channel {lag-intf-num | unit/slot/port} counters
Mode Privileged EXEC
clear port-channel all counters
Use this command to clear and reset all port-channel and member flap counters for the
specified interface.
Format clear port-channel all counters
Mode Privileged EXEC
Port Mirroring Commands
Port mirroring, which is also known as port monitoring, selects network traffic that you can
analyze with a network analyzer, such as a SwitchProbe device or other Remote Monitoring
(RMON) probe.
monitor session source
This command adds a source interface for a port mirroring session that is identified by the
session-id argument (an integer value).
Use the source interface {unit/slot/port | cpu | lag lag-group-id}
parameters to specify the interface to monitor. You can also configure a VLAN as the source
for the session (all member ports of that VLAN are monitored).
Switching Commands 528

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: If an interface is a member of both a VLAN and a LAG, you cannot
assign the VLAN as a source VLAN for a monitor session. However, if
an interface is a member of a VLAN and you assign the VLAN as a
source VLAN for a monitor session, afterwards you can add the
interface as a member to a LAG.
You can configure remote port mirroring by specifying the remote vlan keywords and an
RSPAN VLAN ID. At the source switch, you must specify the destination as the RSPAN
VLAN. At the destination switch, you must specify the source as the RSPAN VLAN. You
cannot configure the source and destination as remote on the same switch.
Note: On an intermediate switch, you must create an RSPAN VLAN, make
sure that the ports that are connected to the source and destination
switches are members of the RSPAN VLAN, and enable RSPAN
VLAN egress tagging on the port that is connected to the destination
switch.
Use rx to monitor only ingress packets or use tx to monitor only egress packets. If you do
not specify an rx or tx option, the destination port monitors both ingress and egress
packets.
Format monitor session session-id source {interface {unit/slot/port | cpu | lag} | vlan vlan-id | remote vlan vlan-id}
[rx | tx]
Mode Global Config
no monitor session source
This command removes a source interface for a port mirroring session that is identified by the
session-id argument (an integer value).
Format monitor session session-id source {interface {unit/slot/port | cpu | lag} | vlan vlan-id | remote vlan vlan-id}
Mode Global Config
monitor session destination
This command adds a destination interface for a port mirroring session that is identified by
the session-id argument (an integer value).
Use the destination interface unit/slot/port parameter to specify the interface
to monitor.
You can configure remote port mirroring by specifying the remote vlan keywords and an
RSPAN VLAN ID. At the source switch, you must specify the destination as the RSPAN
Switching Commands 529

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
VLAN. At the destination switch, you must specify the source as the RSPAN VLAN. You
cannot configure the source and destination as remote on the same switch.
Note: If an interface is a member of both a VLAN and a LAG, you cannot
assign the VLAN as a destination VLAN for a monitor session.
However, if an interface is a member of a VLAN and you assign the
VLAN as a destination VLAN for a monitor session, afterwards you
can add the interface as a member to a LAG.
Note: On an intermediate switch, you must create an RSPAN VLAN, make
sure that the ports that are connected to the source and destination
switches are members of the RSPAN VLAN, and enable RSPAN
VLAN egress tagging on the port that is connected to the destination
switch.
If you specify an RSPAN VLAN ID, you must also specify the reflector port at the source
switch. The reflector port, which must be a member of the RSPAN VLAN, forwards the
mirrored traffic to the destination switch. You specify the reflector port by entering the
reflector-port keyword and the unit/slot/port argument.
Format monitor session session-id destination {interface {unit/slot/port} | remote vlan vlan-id reflector-port
unit/slot/port}
Mode Global Config
no monitor session destination
This command removes a destination interface for a port mirroring session that is identified
by the session-id argument (an integer value).
Format no monitor session session-id destination {interface | remote vlan unit/slot/port}
Mode Global Config
no monitor
This command removes all the source ports and a destination port for the and restores the
default value for mirroring session mode for all the configured sessions.
Note: This is a stand-alone no command. This command does not have a
normal form.
Switching Commands 530

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format no monitor
Mode Global Config
show monitor session
This command displays the port monitoring information for a particular mirroring session.
Note: The session-id parameter is an integer value used to identify the
session. In the current version of the software, the session-id
parameter is a number from 1 to 4.
Format show monitor session session-id
Mode Privileged EXEC
Term Definition
Session ID An integer value used to identify the session. Its value can be anything between 1 and the maximum
number of mirroring sessions allowed on the platform.
Monitor Session Indicates whether the Port Mirroring feature is enabled or disabled for the session identified with
Mode session-id. The possible values are Enabled and Disabled.
Probe Port Probe port (destination port) for the session identified with session-id. If probe port is not set then
this field is blank.
Source Port The port, which is configured as mirrored port (source port) for the session identified with
session-id. If no source port is configured for the session then this field is blank.
Type Direction in which source port configured for port mirroring.Types are tx for transmitted packets and
rx for receiving packets.
Src VLAN All member ports of this VLAN are mirrored. If the source VLAN is not configured, this field is blank.
Ref. Port This port carries all the mirrored traffic at the source switch.
Src Remote VLAN The source VLAN is configured at the destination switch. If the remote VLAN is not configured, this
field is blank.
Dst Remote VLAN The destination VLAN is configured at the source switch. If the remote VLAN is not configured, this
field is blank.
IP ACL The IP access-list id or name attached to the port mirroring session.
MAC ACL The MAC access-list name attached to the port mirroring session.
Switching Commands 531

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show vlan remote-span
This command displays the configured RSPAN VLAN.
Format show vlan remote-span
Mode Privileged Exec Mode
Command example:
(NETGEAR Switch)# show vlan remote-span
Remote SPAN VLAN
------------------------------------------------------------------------

Static MAC Filtering Commands
The commands in this section describe how to configure static MAC filtering. Static MAC
filtering allows you to configure destination ports for a static multicast MAC filter irrespective
of the platform.
macfilter
This command adds a static MAC filter entry for the MAC address macaddr on the VLAN
vlanid. A packet with a specific destination MAC address in a specific VLAN is admitted
only if the ingress port is defined in the set of source ports, otherwise the packet is dropped.
On the egress side, a packet that was admitted is sent through all ports that are defined in the
set of destination ports.
The value of the macaddr parameter is a 6-byte hexadecimal number in the format of
b1:b2:b3:b4:b5:b6. The restricted MAC Addresses are: 00:00:00:00:00:00,
01:80:C2:00:00:00 to 01:80:C2:00:00:0F, 01:80:C2:00:00:20 to 01:80:C2:00:00:21, and
FF:FF:FF:FF:FF:FF. The vlanid parameter must identify a valid VLAN.
The number of static mac filters supported on the system is different for MAC filters where
source ports are configured and MAC filters where destination ports are configured.
• For unicast MAC address filters and multicast MAC address filters with source port lists,
the maximum number of static MAC filters supported is 20.
• For multicast MAC address filters with destination ports configured, the maximum number
of static filters supported is 256.
For example, you can configure the following combinations:
• Unicast MAC and source port (max = 20)
• Multicast MAC and source port (max = 20)
Switching Commands 532

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
• Multicast MAC and destination port (only) (max = 256)
• Multicast MAC and source ports and destination ports (max = 20)
Format macfilter macaddr vlanid
Mode Global Config
no macfilter
This command removes all filtering restrictions and the static MAC filter entry for the MAC
address macaddr on the VLAN vlanid. The macaddr parameter must be specified as a
6-byte hexadecimal number in the format of b1:b2:b3:b4:b5:b6.
The vlanid parameter must identify a valid VLAN.
Format no macfilter macaddr vlanid
Mode Global Config
macfilter adddest
Use this command to add the interface or range of interfaces to the destination filter set for
the MAC filter with the given macaddr and VLAN of vlanid. The macaddr parameter must
be specified as a 6-byte hexadecimal number in the format of b1:b2:b3:b4:b5:b6. The
vlanid parameter must identify a valid VLAN.
Note: Configuring a destination port list is only valid for multicast MAC
addresses.
Format macfilter adddest macaddr vlanid
Mode Interface Config
no macfilter adddest
This command removes a port from the destination filter set for the MAC filter with the given
macaddr and VLAN of vlanid. The macaddr parameter must be specified as a 6-byte
hexadecimal number in the format of b1:b2:b3:b4:b5:b6. The vlanid parameter must
identify a valid VLAN.
Format no macfilter adddest macaddr vlanid
Mode Interface Config
Switching Commands 533

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
macfilter adddest all
This command adds all interfaces to the destination filter set for the MAC filter with the given
macaddr and VLAN of vlanid. The macaddr parameter must be specified as a 6-byte
hexadecimal number in the format of b1:b2:b3:b4:b5:b6. The vlanid parameter must
identify a valid VLAN.
Note: Configuring a destination port list is only valid for multicast MAC
addresses.
Format macfilter adddest all macaddr vlanid
Mode Global Config
no macfilter adddest all
This command removes all ports from the destination filter set for the MAC filter with the
given macaddr and VLAN of vlanid. The macaddr parameter must be specified as a
6-byte hexadecimal number in the format of b1:b2:b3:b4:b5:b6. The vlanid parameter must
identify a valid VLAN.
Format no macfilter adddest all macaddr vlanid
Mode Global Config
macfilter addsrc
This command adds the interface or range of interfaces to the source filter set for the MAC
filter with the MAC filter with the given macaddr and VLAN of vlanid. The macaddr
parameter must be specified as a 6-byte hexadecimal number in the format of
b1:b2:b3:b4:b5:b6. The vlanid parameter must identify a valid VLAN.
Format macfilter addsrc macaddr vlanid
Mode Interface Config
no macfilter addsrc
This command removes a port from the source filter set for the MAC filter with the given
macaddr and VLAN of vlanid. The macaddr parameter must be specified as a 6-byte
hexadecimal number in the format of b1:b2:b3:b4:b5:b6. The vlanid parameter must
identify a valid VLAN.
Format no macfilter addsrc macaddr vlanid
Mode Interface Config
Switching Commands 534

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
macfilter addsrc all
This command adds all interfaces to the source filter set for the MAC filter with the MAC filter
with the given macaddr and VLAN of vlanid. The macaddr parameter must be specified
as a 6-byte hexadecimal number in the format of b1:b2:b3:b4:b5:b6. The vlanid parameter
must identify a valid VLAN.
Format macfilter addsrc all macaddr vlanid
Mode Global Config
no macfilter addsrc all
This command removes all interfaces to the source filter set for the MAC filter with the given
macaddr and VLAN of vlanid. The macaddr parameter must be specified as a 6-byte
hexadecimal number in the format of b1:b2:b3:b4:b5:b6. The vlanid parameter must
identify a valid VLAN.
Format no macfilter addsrc all macaddr vlanid
Mode Global Config
show mac-address-table static
This command displays the Static MAC Filtering information for all Static MAC Filters. If you
specify all, all the static MAC filters in the system are displayed. If you supply a value for
macaddr, you must also enter a value for vlanid, and the system displays static MAC filter
information only for that MAC address and VLAN.
Format show mac-address-table static {macaddr vlanid | all}
Mode Privileged EXEC
Term Definition
MAC Address The MAC Address of the static MAC filter entry.
VLAN ID The VLAN ID of the static MAC filter entry.
Source Ports The source port filter set slot and ports.
Note: Only multicast address filters can have destination port lists.
Switching Commands 535

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show mac-address-table staticfiltering
This command displays the Static Filtering entries in the Multicast Forwarding Database
(MFDB) table.
Format show mac-address-table staticfiltering
Mode Privileged EXEC
Term Definition
VLAN ID The VLAN in which the MAC Address is learned.
MAC Address A unicast MAC address for which the switch has forwarding and or filtering information. As the data
is gleaned from the MFDB, the address will be a multicast address. The format is 6 two-digit
hexadecimal numbers that are separated by colons, for example 01:23:45:67:89:AB.
Type The type of the entry. Static entries are those that are configured by the end user. Dynamic entries
are added to the table as a result of a learning process or protocol.
Description The text description of this multicast table entry.
Interfaces The list of interfaces that are designated for forwarding (Fwd:) and filtering (Flt:).
DHCP L2 Relay Agent Commands
You can enable the switch to operate as a DHCP Layer 2 relay agent to relay DHCP requests
from clients to a Layer 3 relay agent or server. The Circuit ID and Remote ID can be added to
DHCP requests relayed from clients to a DHCP server. This information is included in DHCP
Option 82, as specified in sections 3.1 and 3.2 of RFC3046.
dhcp l2relay
This command enables the DHCP Layer 2 Relay agent for an interface a range of interfaces
in, or all interfaces. The subsequent commands mentioned in this section can only be used
when the DHCP L2 relay is enabled.
Format dhcp l2relay
Mode Global Config
Interface Config
Switching Commands 536

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dhcp l2relay
This command disables DHCP Layer 2 relay agent for an interface or range of interfaces.
Format no dhcp l2relay
Mode Global Config
Interface Config
dhcp l2relay circuit-id vlan
This parameter sets the DHCP Option-82 Circuit ID for a VLAN. When enabled, the interface
number is added as the Circuit ID in DHCP option 82.
Format dhcp l2relay circuit-id vlan vlan-list
Mode Global Config
Parameter Description
vlan–list The VLAN ID. The range is 1–4093. Separate nonconsecutive IDs with a comma (,) no spaces and
no zeros in between the range. Use a dash (–) for the range.
no dhcp l2relay circuit-id vlan
This parameter clears the DHCP Option-82 Circuit ID for a VLAN.
Format no dhcp l2relay circuit-id vlan vlan-list
Mode Global Config
dhcp l2relay remote-id subscription
This command sets the Option-82 Remote-ID string for a given service subscription identified
by subscription-string on a given interface or range of interfaces. The
subscription-string is a character string which needs to be matched with a configured
DOT1AD subscription string for correct operation. The remoteid-string is a character
string. When remote-id string is set using this command, all Client DHCP requests that fall
under this service subscription are added with Option-82 Remote-id as the configured
remote-id string.
Default empty string
Format dhcp l2relay remote-id remoteid-string subscription-name subscription-string
Mode Interface Config
no dhcp l2relay remote-id subscription
This command resets the Option-82 Remote-ID string for a given service subscription
identified by subscription-string on a given interface. The subscription-string is
Switching Commands 537

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
a character string which needs to be matched with a configured DOT1AD subscription string
for correct operation. When remote-id string is reset using this command, the Client DHCP
requests that fall under this service subscription are not added with Option-82 Remote-id.
Format no dhcp l2relay remote-id remoteid-string subscription-name
subscription-string
Mode Interface Config
dhcp l2relay remote-id vlan
This parameter sets the DHCP Option-82 Remote ID for a VLAN and subscribed service
(based on subscription-name).
Format dhcp l2relay remote-id remote-id-string vlan vlan-list
Mode Global Config
Parameter Description
vlan–list The VLAN ID. The range is 1–4093. Separate nonconsecutive IDs with a comma (,) no spaces and
no zeros in between the range. Use a dash (–) for the range.
no dhcp l2relay remote-id vlan
This parameter clears the DHCP Option-82 Remote ID for a VLAN and subscribed service
(based on subscription-name).
Format no dhcp l2relay remote-id vlan vlan-list
Mode Global Config
dhcp l2relay subscription
This command enables relaying DHCP packets on an interface or range of interfaces that fall
under the specified service subscription. The subscription-string is a character string
that must be matched with the configured DOT1AD subscription-string for correct operation.
Default Disabled (that is, no DHCP packets are relayed)
Format dhcp l2relay subscription-name subscription-string
Mode Interface Config
Switching Commands 538

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dhcp l2relay subscription
This command disables relaying DHCP packets that fall under the specified service
subscription. The subscription-string is a character string that must be matched with
the configured DOT1AD subscription string for correct operation.
Format no dhcp l2relay subscription-name subscription-string
Mode Interface Config
dhcp l2relay trust
Use this command to configure an interface or range of interfaces as trusted for Option-82
reception.
Default Untrusted
Format dhcp l2relay trust
Mode Interface Config
no dhcp l2relay trust
Use this command to configure an interface to the default untrusted for Option-82 reception.
Format no dhcp l2relay trust
Mode Interface Config
dhcp l2relay vlan
Use this command to enable the DHCP L2 Relay agent for a set of VLANs. All DHCP packets
which arrive on interfaces in the configured VLAN are subject to L2 Relay processing.
Default Disabled
Format dhcp l2relay vlan vlan-list
Mode Global Config
Parameter Description
vlan–list The VLAN ID. The range is 1–4093. Separate nonconsecutive IDs with a comma (,) no spaces and
no zeros in between the range. Use a dash (–) for the range.
Switching Commands 539
