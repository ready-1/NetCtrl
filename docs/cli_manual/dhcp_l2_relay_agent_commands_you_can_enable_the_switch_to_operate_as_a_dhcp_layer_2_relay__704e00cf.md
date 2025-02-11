# dhcp_l2_relay_agent_commands_you_can_enable_the_switch_to_operate_as_a_dhcp_layer_2_relay__704e00cf

Pages: 536-539

## Content

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
