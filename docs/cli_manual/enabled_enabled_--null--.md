# enabled_enabled_--null--

Pages: 543-544

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show dhcp l2relay agent-option vlan 5-10
DHCP L2 Relay is Enabled.
V LAN Id L 2 Relay C ircuitId RemoteId
--------- ---------- - ---------- ------------
5 Enabled Enabled --NULL--
6 Enabled Enabled NETGEAR
7 Enabled Disabled --NULL--
8 Enabled Disabled --NULL--
9 Enabled Disabled --NULL--
10 Enabled Disabled --NULL--
show dhcp l2relay vlan
This command displays DHCP vlan configuration.
Format show dhcp l2relay vlan vlan-list
Mode Privileged EXEC
Parameter Description
vlan-list Enter VLAN IDs in the range 1–4093. Use a dash (–) to specify a range or a comma (,) to separate
VLAN IDs in a list. Spaces and zeros are not permitted.
clear dhcp l2relay statistics interface
Use this command to reset the DHCP L2 relay counters to zero. Specify the port with the
counters to clear, or use the all keyword to clear the counters on all ports.
Format clear dhcp l2relay statistics interface {unit/slot/port | all}
Mode Privileged EXEC
DHCP Client Commands
The switch can include vendor and configuration information in DHCP client requests relayed
to a DHCP server. This information is included in DHCP Option 60, Vendor Class Identifier.
The information is a string of 128 octets.
Switching Commands 543

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
dhcp client vendor-id-option
This command enables the inclusion of DHCP Option-60, Vendor Class Identifier included in
the requests transmitted to the DHCP server by the DHCP client operating in the switch.
Format dhcp client vendor-id-option string
Mode Global Config
no dhcp client vendor-id-option
This command disables the inclusion of DHCP Option-60, Vendor Class Identifier included in
the requests transmitted to the DHCP server by the DHCP client operating in the switch.
Format no dhcp client vendor-id-option
Mode Global Config
dhcp client vendor-id-option-string
This parameter sets the DHCP Vendor Option-60 string to be included in the requests
transmitted to the DHCP server by the DHCP client operating in the switch.
Format dhcp client vendor-id-option-string string
Mode Global Config
no dhcp client vendor-id-option-string
This parameter clears the DHCP Vendor Option-60 string.
Format no dhcp client vendor-id-option-string
Mode Global Config
show dhcp client vendor-id-option
This command displays the configured administration mode of the vendor-id-option and the
vendor-id string to be included in Option-43 in DHCP requests.
Format show dhcp client vendor-id-option
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show dhcp client vendor-id-option
DHCP Client Vendor Identifier Option........... Enabled
DHCP Client Vendor Identifier Option String.... NetgearClient
Switching Commands 544
