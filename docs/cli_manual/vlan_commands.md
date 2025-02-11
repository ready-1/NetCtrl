# vlan_commands

Pages: 421-422

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
VLAN Commands
This section describes the commands you use to configure VLAN settings.
switchport mode auto
This command globally enables the Auto-Trunk feature. If enabled, the switch can
automatically configure a port as a trunk (that is, an Auto-Trunk) with an interconnected
partner device that supports the Auto-Trunk feature.
After a port or an Auto-LAG becomes an Auto-Trunk, all VLANs on the switch become part of
the trunk, allowing automatic configuration of all VLANs on the switch and partner device with
which the trunk is established.
Default Disabled
Format switchport mode auto
Mode Global Config
no switchport mode auto
This command globally disables the Auto-Trunk feature.
Format no switchport mode auto
Mode Global Config
show interfaces switchport trunk
This command displays information for all interfaces on which the Auto-Trunk feature is
enabled. As an option, you can display the information for a single interface only.
Format show interfaces switchport trunk [unit/port]
Mode Privileged EXEC
Command example:
(Switch)#show interfaces switchport trunk
Global Auto-Trunk Mode : Enabled
Intf PVID Allowed Vlans List Auto-Trunk
--------- ----- -------------------- ---------------
0/3 1 All Yes
0/15 1 All Yes
0/29 1 All Yes
Switching Commands 421

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(Switch)#show interfaces switchport trunk 0/15
Global Auto-Trunk Mode : Enabled
Intf PVID Allowed Vlans List Auto-Trunk
--------- ----- -------------------- ---------------
0/15 1 All Yes
vlan database
This command gives you access to the VLAN Config mode, which allows you to configure
VLAN characteristics.
Format vlan database
Mode Privileged EXEC
vlan
This command creates a new VLAN and assigns it an ID. The ID is a valid VLAN
identification number (ID 1 is reserved for the default VLAN). The VLAN number is in the
range 2–4093.
Format vlan number
Mode VLAN Config
no vlan
This command deletes an existing VLAN. The ID is a valid VLAN identification number (ID 1
is reserved for the default VLAN). The VLAN number is in the range 2–4093.
Format no vlan number
Mode VLAN Config
vlan acceptframe
This command sets the frame acceptance mode on an interface or range of interfaces. For
VLAN Only mode, untagged frames or priority frames received on this interface are
discarded. For Admit All mode, untagged frames or priority frames received on this interface
are accepted and assigned the value of the interface VLAN ID for this port. For
admituntaggedonly mode, only untagged frames are accepted on this interface; tagged
frames are discarded. With any option, VLAN tagged frames are forwarded in accordance
with the IEEE 802.1Q VLAN Specification.
Switching Commands 422
