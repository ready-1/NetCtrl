# vlan_config_no_set_mld_exclude-mrouter-intf

Pages: 594-595

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Enter the command in Global Config mode to globally apply the setting to all interfaces.
Enter the command in VLAN Config mode to apply the setting at interface level.
For the VLAN configuration to take effect, you must first enter the set mld
exclude-mrouter-intf command and then enter the same command for a specific
VLAN.
Default Enabled
Format set mld exclude-mrouter-intf [vlan-id]
Mode Global Config
VLAN Config
no set mld exclude-mrouter-intf
Use this command to let the switch pass unknown multicast data to an mrouter interface.
Enter the command in Global Config mode to globally apply the setting to all interfaces.
Enter the command in VLAN Config mode to apply the setting at interface level.
Format no set mld exclude-mrouter-intf [vlan-id]
Mode Global Config
VLAN Config
set mld-plus
This command enables both of the following global MLD Snooping configuration commands:
• set mld
• set mld exclude-mrouter-intf
Default Enabled
Format set mld-plus
Mode Global Config
no set mld-plus
This command disables both of the following global MLD Snooping configuration commands:
• set mld
• set mld exclude-mrouter-intf
Format no set mld-plus
Mode Global Config
Switching Commands 594

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
set mld-plus vlan
After you enable the set mld-plus command, you can enable the set mld-plus vlan
command to enable all of the following global MLD Snooping configuration commands at the
VLAN level for a particular VLAN:
• set mld vlan
• set mld exclude-mrouter-intf vlan
• set mld fast-leave vlan
The vlan argument in the set mld-plus vlan command can be a VLAN from 1 to 4093.
Default Enabled for VLAN 1
Format set mld-plus vlan
Mode VLAN Config
no set mld-plus vlan
This command disables all of the following global MLD Snooping configuration commands at
the VLAN level for a particular VLAN:
• set mld vlan
• set mld exclude-mrouter-intf vlan
• set mld fast-leave vlan
The vlan argument in the no set mld-plus vlan command can be a VLAN from 1 to
4093.
Format no set mld-plus vlan
Mode VLAN Config
show mldsnooping
Use this command to display MLD Snooping information. Configured information is displayed
whether or not MLD Snooping is enabled.
Format show mldsnooping [unit/slot/port | vlan-id]
Mode Privileged EXEC
When the optional arguments unit/slot/port or vlan-id are not used, the command
displays the following information.
Term Definition
Admin Mode Indicates whether or not MLD Snooping is active on the switch.
Interfaces Enabled Interfaces on which MLD Snooping is enabled.
for MLD Snooping
Switching Commands 595
