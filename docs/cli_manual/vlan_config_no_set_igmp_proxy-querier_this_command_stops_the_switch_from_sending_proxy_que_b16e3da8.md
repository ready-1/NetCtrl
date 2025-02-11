# vlan_config_no_set_igmp_proxy-querier_this_command_stops_the_switch_from_sending_proxy_que_b16e3da8

Pages: 588-588

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
By default, the proxy querrier is enabled.
Default enabled
Format set igmp proxy-querier [vlan-id]
Mode Global Config
Interface Config
VLAN Config
no set igmp proxy-querier
This command stops the switch from sending proxy queries through different command
modes in the following ways:
• in Global Config mode, on the entire switch
• in Interface Config mode, on an interface
• in VLAN Config mode, on a particular VLAN and all interfaces participating in the VLAN.
This command is specific to IGMP.
Format no set igmp proxy-querier [vlan-id]
Mode Global Config
Interface Config
VLAN Config
show igmpsnooping proxy-querier
This command shows the global admin mode of the IGMP snooping proxy-querier and the
interface on which it is enabled.
Format show igmpsnooping proxy-querier
Mode Privileged EXEC
Command example:
(Netgear Switch) #show igmpsnooping proxy-querier
Admin Mode..................................... Enable
Interfaces Enabled for IGMP Proxy Querier...... 1/0/1
1/0/2
1/0/3
1/0/4
Switching Commands 588
