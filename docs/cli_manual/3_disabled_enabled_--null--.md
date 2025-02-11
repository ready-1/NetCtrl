# 3 Disabled Enabled --NULL--

Pages: 540-542

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dhcp l2relay vlan
Use this command to disable the DHCP L2 Relay agent for a set of VLANs.
Format no dhcp l2relay vlan vlan-list
Mode Global Config
show dhcp l2relay all
This command displays the summary of DHCP L2 Relay configuration.
Format show dhcp l2relay all
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show dhcp l2relay all
DHCP L2 Relay is Enabled.
Interface L2RelayMode TrustMode
---------- ----------- --------------
0/2 Enabled untrusted
0/4 Disabled trusted
VLAN Id L2 Relay CircuitId RemoteId
--------- ---------- ----------- ------------
3 Disabled Enabled --NULL--
5 Enabled Enabled --NULL--
6 Enabled Enabled NETGEAR
7 Enabled Disabled --NULL--
8 Enabled Disabled --NULL--
9 Enabled Disabled --NULL--
10 Enabled Disabled --NULL--
show dhcp l2relay circuit-id vlan
This command displays DHCP circuit-id vlan configuration.
Format show dhcp l2relay circuit-id vlan vlan-list
Mode Privileged EXEC
Switching Commands 540

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
vlan-list Enter VLAN IDs in the range 1–4093. Use a dash (–) to specify a range or a comma (,) to separate
VLAN IDs in a list. Spaces and zeros are not permitted.
show dhcp l2relay interface
This command displays DHCP L2 relay configuration specific to interfaces.
Format show dhcp l2relay interface {all | unit/slot/port}
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show dhcp l2relay interface all
DHCP L2 Relay is Enabled.
Interface L2RelayMode TrustMode
---------- ----------- --------------
0/2 Enabled untrusted
0/4 Disabled trusted
show dhcp l2relay remote-id vlan
This command displays DHCP Remote-id vlan configuration.
Format show dhcp l2relay remote-id vlan vlan-list
Mode Privileged EXEC
Parameter Description
vlan-list Enter VLAN IDs in the range 1–4093. Use a dash (–) to specify a range or a comma (,) to separate
VLAN IDs in a list. Spaces and zeros are not permitted.
show dhcp l2relay stats interface
This command displays statistics specific to DHCP L2 Relay configured interface.
Format show dhcp l2relay stats interface {all | unit/slot/port}
Mode Privileged EXEC
Switching Commands 541

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
((NETGEAR Switch)) #show dhcp l2relay stats interface all
DHCP L2 Relay is Enabled.
Interface UntrustedServer UntrustedClient TrustedServer TrustedClient
M sgsWithOpt82 M sgsWithOpt82 M sgsWithoutOpt82 MsgsWithoutOpt82
- -------- --------------- - -------------- ---------------- --------------
0/1 0 0 0 0
0/2 0 0 3 7
0/3 0 0 0 0
0/4 0 1 2 0 0
0/5 0 0 0 0
0/6 3 0 0 0
0/7 0 0 0 0
0/8 0 0 0 0
0/9 0 0 0 0
show dhcp l2relay subscription interface
This command displays DHCP L2 Relay configuration specific to a service subscription on an
interface.
Format show dhcp l2relay subscription interface {all | unit/slot/port}
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show dhcp l2relay subscription interface all
I nterface SubscriptionName L2Relay mode Circuit-Id mode Remote-Id mode
----------- ---------------- -------------- --------------- ----------------
0/1 sub1 Enabled Disabled --NULL--
0/2 sub3 Enabled Disabled EnterpriseSwitch
0/2 sub22 Disabled Enabled --NULL--
0/4 sub4 Enabled Enabled --NULL--
show dhcp l2relay agent-option vlan
This command displays the DHCP L2 Relay Option-82 configuration specific to VLAN.
Format show dhcp l2relay agent-option vlan vlan-range
Mode Privileged EXEC
Switching Commands 542
