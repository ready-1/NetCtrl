# vlan_ids_that_do_not_match_the_vlan_membership_of_the_receiving_interface_are_admitted

Pages: 423-438

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default all
Format vlan acceptframe {admituntaggedonly | vlanonly | all}
Mode Interface Config
no vlan acceptframe
This command resets the frame acceptance mode for the interface or range of interfaces to
the default value.
Format no vlan acceptframe
Mode Interface Config
vlan ingressfilter
This command enables ingress filtering on an interface or range of interfaces. If ingress
filtering is disabled, frames received with VLAN IDs that do not match the VLAN membership
of the receiving interface are admitted and forwarded to ports that are members of that
VLAN.
Default Disabled
Format vlan ingressfilter
Mode Interface Config
no vlan ingressfilter
This command disables ingress filtering. If ingress filtering is disabled, frames received with
VLAN IDs that do not match the VLAN membership of the receiving interface are admitted
and forwarded to ports that are members of that VLAN.
Format no vlan ingressfilter
Mode Interface Config
vlan internal allocation
Use this command to configure which VLAN IDs to use for port-based routing interfaces.
When a port-based routing interface is created, an unused VLAN ID is assigned internally.
Format vlan internal allocation {base vlan-id | policy ascending | policy decending}
Mode Global Config
Switching Commands 423

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
base vlan-id The first VLAN ID to be assigned to a port-based routing interface.
policy ascending VLAN IDs assigned to port-based routing interfaces start at the base and increase in value
policy descending VLAN IDs assigned to port-based routing interfaces start at the base and decrease in value
vlan makestatic
This command changes a dynamically created VLAN (created by GVRP registration) to a
static VLAN (one that is permanently configured and defined). The ID is a valid VLAN
identification number. The VLAN number is in the range is 2–4093.
Format vlan makestatic number
Mode VLAN Config
vlan name
This command changes the name of a VLAN. The name is an alphanumeric string of up to 32
characters, and the number is a valid VLAN identification number. The number is in the range
1–4093.
Default VLAN ID 1 - default
other VLANS - blank string
Format vlan name number name
Mode VLAN Config
no vlan name
This command sets the name of a VLAN to a blank string.
Format no vlan name number
Mode VLAN Config
vlan participation
This command configures the degree of participation for a specific interface or range of
interfaces in a VLAN. The number is a valid VLAN identification number in the range 1-4093,
and the interface is a valid interface number.
Format vlan participation {exclude | include | auto} number
Mode Interface Config
Switching Commands 424

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Participation options are:
Options Definition
include The interface is always a member of this VLAN. This is equivalent to registration fixed.
exclude The interface is never a member of this VLAN. This is equivalent to registration forbidden.
auto The interface is dynamically registered in this VLAN by GVRP and will not participate in this VLAN unless
a join request is received on this interface. This is equivalent to registration normal.
vlan participation all
This command configures the degree of participation for all interfaces in a VLAN. The
number is a valid VLAN identification number in the range 1–4093.
Format vlan participation all {exclude | include | auto} number
Mode Global Config
You can use the following participation options:
Participation Definition
Options
include The interface is always a member of this VLAN. This is equivalent to registration fixed.
exclude The interface is never a member of this VLAN. This is equivalent to registration forbidden.
auto The interface is dynamically registered in this VLAN by GVRP. The interface will not participate in
this VLAN unless a join request is received on this interface. This is equivalent to registration normal.
vlan port acceptframe all
This command sets the frame acceptance mode for all interfaces.
For the all mode, untagged frames or priority frames that enter on an interface are accepted
and assigned the VLAN ID of the interface. With any of the three modes, VLAN-tagged
frames are forwarded in accordance with the IEEE 802.1Q VLAN specification.
Default all
Format vlan port acceptframe all {vlanonly | admituntaggedonly | all}
Mode Global Config
The modes are defined as follows:
Mode Definition
vlanonly VLAN-only mode. Untagged frames or priority frames received on this interface are discarded.
Switching Commands 425

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Mode Definition
admituntaggedonly Admit untagged-only mode. VLAN-tagged and priority tagged frames received on this interface
are discarded.
all Admit all mode. Untagged frames or priority frames received on this interface are accepted and
assigned the value of the interface VLAN ID for this port.
no vlan port acceptframe all
This command sets the frame acceptance mode to the default mode all.
Format no vlan port acceptframe all
Mode Global Config
vlan port ingressfilter all
This command enables ingress filtering for all ports. If ingress filtering is disabled, frames
received with VLAN IDs that do not match the VLAN membership of the receiving interface
are admitted and forwarded to ports that are members of that VLAN.
Default Disabled
Format vlan port ingressfilter all
Mode Global Config
no vlan port ingressfilter all
This command disables ingress filtering for all ports. If ingress filtering is disabled, frames
received with VLAN IDs that do not match the VLAN membership of the receiving interface
are admitted and forwarded to ports that are members of that VLAN.
Format no vlan port ingressfilter all
Mode Global Config
vlan port pvid all
This command changes the VLAN ID for all interfaces. The number is a valid VLAN
identification number in the range 1–4093.
Default 1
Format vlan port pvid all number
Mode Global Config
Switching Commands 426

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no vlan port pvid all
This command sets the VLAN ID for all interfaces to 1.
Format no vlan port pvid all
Mode Global Config
vlan port tagging all
This command configures the tagging behavior for all interfaces in a VLAN to enabled. If
tagging is enabled, traffic is transmitted as tagged frames. If tagging is disabled, traffic is
transmitted as untagged frames. The number is a valid VLAN identification number in the
range 1–4093.
Format vlan port tagging all number
Mode Global Config
no vlan port tagging all
This command configures the tagging behavior for all interfaces in a VLAN to disabled. If
tagging is disabled, traffic is transmitted as untagged frames. The number is a valid VLAN
identification number in the range 1–4093.
Format no vlan port tagging all number
Mode Global Config
vlan protocol group
This command adds protocol-based VLAN groups to the system. The groupid is a unique
number from 1–128 that is used to identify the group in subsequent commands.
Format vlan protocol group groupid
Mode Global Config
vlan protocol group name
This command assigns a name to a protocol-based VLAN group. The groupname variable
can be a character string of 0 to 16 characters.
Format vlan protocol group name groupid groupname
Mode Global Config
Switching Commands 427

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no vlan protocol group name
This command removes the name from the group identified by groupid.
Format no vlan protocol group name groupid
Mode Global Config
vlan protocol group add protocol
This command adds the protocol to the protocol-based VLAN identified by groupid. A group
may have more than one protocol associated with it. Each interface and protocol combination
can only be associated with one group. If adding a protocol to a group causes any conflicts
with interfaces currently associated with the group, this command fails and the protocol is not
added to the group. The possible values for protocol-list includes the keywords ip,
arp, and ipx and hexadecimal or decimal values ranging from 0x0600 (1536) to 0xFFFF
(65535). The protocol list can accept up to 16 protocols separated by a comma.
Default none
Format vlan protocol group add protocol groupid ethertype protocol-list
Mode Global Config
no vlan protocol group add protocol
This command removes the protocols specified in the protocol-list from this
protocol-based VLAN group that is identified by this groupid.
Format no vlan protocol group add protocol groupid ethertype protocol-list
Mode Global Config
protocol group
This command attaches a vlanid to the protocol-based VLAN identified by groupid. A
group can only be associated with one VLAN at a time, however the VLAN association can
be changed.
Default none
Format protocol group groupid vlanid
Mode VLAN Config
Switching Commands 428

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no protocol group
This command removes the vlanid from this protocol-based VLAN group that is identified
by this groupid.
Format no protocol group groupid vlanid
Mode VLAN Config
protocol vlan group
This command adds a physical interface or a range of interfaces to the protocol-based VLAN
identified by groupid. You can associate multiple interfaces with a group, but you can only
associate each interface and protocol combination with one group. If adding an interface to a
group causes any conflicts with protocols currently associated with the group, this command
fails and the interface or interfaces are not added to the group.
Default none
Format protocol vlan group groupid
Mode Interface Config
no protocol vlan group
This command removes the interface from this protocol-based VLAN group that is identified
by this groupid.
Format no protocol vlan group groupid
Mode Interface Config
protocol vlan group all
This command adds all physical interfaces to the protocol-based VLAN identified by
groupid. You can associate multiple interfaces with a group, but you can only associate
each interface and protocol combination with one group. If adding an interface to a group
causes any conflicts with protocols currently associated with the group, this command will fail
and the interface or interfaces are not added to the group.
Default none
Format protocol vlan group all groupid
Mode Global Config
Switching Commands 429

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no protocol vlan group all
This command removes all interfaces from this protocol-based VLAN group that is identified
by this groupid.
Format no protocol vlan group all groupid
Mode Global Config
show port protocol
This command displays the Protocol-Based VLAN information for either the entire system, or
for the indicated group.
Format show port protocol {groupid | all}
Mode Privileged EXEC
Term Definition
Group Name The group name of an entry in the Protocol-based VLAN table.
Group ID The group identifier of the protocol group.
VLAN The VLAN associated with this Protocol Group.
Protocol(s) The type of protocol(s) for this group.
Interface(s) Lists the unit/slot/port interface(s) that are associated with this Protocol Group.
vlan pvid
This command changes the VLAN ID on an interface or range of interfaces. The number is a
valid VLAN identification number in the range 1–4093.
Default 1
Format vlan pvid number
Mode Interface Config
Interface Range Config
no vlan pvid
This command sets the VLAN ID on an interface or range of interfaces to 1.
Format no vlan pvid
Mode Interface Config
Switching Commands 430

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
vlan tagging
This command configures the tagging behavior for a specific interface or range of interfaces
in a VLAN to enabled. If tagging is enabled, traffic is transmitted as tagged frames. If tagging
is disabled, traffic is transmitted as untagged frames. The number is a valid VLAN
identification number in the range 1–4093.
Format vlan tagging number
Mode Interface Config
no vlan tagging
This command configures the tagging behavior for a specific interface or range of interfaces
in a VLAN to disabled. If tagging is disabled, traffic is transmitted as untagged frames. The
number is a valid VLAN identification number in the range 1–4093.
Format no vlan tagging number
Mode Interface Config
vlan association subnet
This command associates a VLAN to a specific IP-subnet.
Format vlan association subnet ipaddr netmask vlanid
Mode VLAN Config
no vlan association subnet
This command removes association of a specific IP-subnet to a VLAN.
Format no vlan association subnet ipaddr netmask
Mode VLAN Config
vlan association mac
This command associates a MAC address to a VLAN.
Format vlan association mac macaddr vlanid
Mode VLAN database
Switching Commands 431

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no vlan association mac
This command removes the association of a MAC address to a VLAN.
Format no vlan association mac macaddr
Mode VLAN database
remote-span
This command identifies the VLAN as the RSPAN VLAN.
Default None
Format remote-span
Mode VLAN configuration
show vlan
This command displays information about the configured private VLANs, including primary
and secondary VLAN IDs, type (community, isolated, or primary) and the ports which belong
to a private VLAN.
Format show vlan {vlan-id | private-vlan [type]}
Mode Privileged EXEC
User EXEC
Term Definition
Primary Primary VLAN identifier. The range of the VLAN ID is 1 to 4093.
Secondary Secondary VLAN identifier.
Type Secondary VLAN type (community, isolated, or primary).
Ports Ports which are associated with a private VLAN.
VLAN ID The VLAN identifier (VID) associated with each VLAN. The range of the VLAN ID is 1 to 4093.
VLAN Name A string associated with this VLAN as a convenience. It can be up to 32 alphanumeric characters
long, including blanks. The default is blank. VLAN ID 1 always has a name of Default. This field is
optional.
VLAN Type Type of VLAN, which can be Default (VLAN ID = 1) or static (one that is configured and permanently
defined), or Dynamic. A dynamic VLAN can be created by GVRP registration or during the 802.1X
authentication process (DOT1X) if a RADIUS-assigned VLAN does not exist on the switch.
Interface unit/slot/port. It is possible to set the parameters for all ports by using the selectors on the top line.
Switching Commands 432

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Current The degree of participation of this port in this VLAN. The permissible values are:
• Include - This port is always a member of this VLAN. This is equivalent to registration fixed in
the IEEE 802.1Q standard.
• Exclude - This port is never a member of this VLAN. This is equivalent to registration forbidden
in the IEEE 802.1Q standard.
• Autodetect - To allow the port to be dynamically registered in this VLAN via GVRP. The port will
not participate in this VLAN unless a join request is received on this port. This is equivalent to
registration normal in the IEEE 802.1Q standard.
Configured The configured degree of participation of this port in this VLAN. The permissible values are:
• Include - This port is always a member of this VLAN. This is equivalent to registration fixed in
the IEEE 802.1Q standard.
• Exclude - This port is never a member of this VLAN. This is equivalent to registration forbidden
in the IEEE 802.1Q standard.
• Autodetect - To allow the port to be dynamically registered in this VLAN via GVRP. The port will
not participate in this VLAN unless a join request is received on this port. This is equivalent to
registration normal in the IEEE 802.1Q standard.
Tagging The tagging behavior for this port in this VLAN.
• Tagged - Transmit traffic for this VLAN as tagged frames.
• Untagged - Transmit traffic for this VLAN as untagged frames.
show vlan internal usage
This command displays information about the VLAN ID allocation on the switch.
Format show vlan internal usage
Mode Privileged EXEC
User EXEC
Term Definition
Base VLAN ID Identifies the base VLAN ID for Internal allocation of VLANs to the routing interface.
Allocation policy Identifies whether the system allocates VLAN IDs in ascending or descending order.
show vlan port
This command displays VLAN port information.
Format show vlan port {unit/slot/port | all}
Mode Privileged EXEC
User EXEC
Switching Commands 433

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Interface It is possible to set the parameters for all ports by using the selectors on the top line.
Port VLAN ID The VLAN ID that this port will assign to untagged frames or priority tagged frames received on this
port. The value must be for an existing VLAN. The factory default is 1.
Acceptable Frame The types of frames that may be received on this port. The options are 'VLAN only' and 'Admit All'.
Types When set to 'VLAN only', untagged frames or priority tagged frames received on this port are
discarded. When set to 'Admit All', untagged frames or priority tagged frames received on this port
are accepted and assigned the value of the Port VLAN ID for this port. With either option, VLAN
tagged frames are forwarded in accordance to the 802.1Q VLAN specification.
Ingress Filtering May be enabled or disabled. When enabled, the frame is discarded if this port is not a member of the
VLAN with which this frame is associated. In a tagged frame, the VLAN is identified by the VLAN ID
in the tag. In an untagged frame, the VLAN is the Port VLAN ID specified for the port that received
this frame. When disabled, all frames are forwarded in accordance with the 802.1Q VLAN bridge
specification. The factory default is disabled.
GVRP May be enabled or disabled.
Default Priority The 802.1p priority assigned to tagged packets arriving on the port.
show vlan association subnet
This command displays the VLAN associated with a specific configured IP-Address and net
mask. If no IP address and net mask are specified, the VLAN associations of all the
configured IP-subnets are displayed.
Format show vlan association subnet [ipaddr netmask]
Mode Privileged EXEC
Term Definition
IP Address The IP address assigned to each interface.
Net Mask The subnet mask.
VLAN ID There is a VLAN Identifier (VID) associated with each VLAN.
show vlan association mac
This command displays the VLAN associated with a specific configured MAC address. If no
MAC address is specified, the VLAN associations of all the configured MAC addresses are
displayed.
Format show vlan association mac [macaddr]
Mode Privileged EXEC
Switching Commands 434

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Mac Address A MAC address for which the switch has forwarding and or filtering information. The format is 6 or 8
two-digit hexadecimal numbers that are separated by colons, for example 01:23:45:67:89:AB. In an
IVL system the MAC address will be displayed as 8 bytes.
VLAN ID There is a VLAN Identifier (VID) associated with each VLAN.
Switch Port Commands
This section describes the commands used for switch port mode.
switchport mode
Use this command to configure the mode of a switch port as access, trunk, or general:
• Trunk mode. In trunk mode, the port becomes a member of all VLANs on the switch
unless specified in the allowed list in the switchport trunk allowed vlan
command. The PVID of the port is set to the native VLAN as specified in the
switchport trunk native vlan command. This means that trunk ports accept both
tagged and untagged packets. Untagged packets are processed on the native VLAN and
tagged packets are processed on the VLAN for which the ID is contained in the packet.
MAC learning is performed on both tagged and untagged packets. Tagged packets that
are received with a VLAN ID of which the port is not a member are discarded and MAC
learning is not performed.
The trunk ports always transmit packets untagged on a native VLAN.
• Access mode. In access mode, the port becomes a member of only one VLAN. The port
sends and receives untagged traffic. The port can also receive tagged traffic. Ingress
filtering is enabled on the port. This means that when the VLAN ID of a received packet is
not identical to the access VLAN ID, the packet is discarded.
• General mode. In general mode, you can perform custom configuration of the VLAN
membership, PVID, tagging, ingress filtering, and so on. The general mode is legacy
behavior of the switch port configuration and you use legacy CLI commands to configure
the port in general mode.
Default General mode
Format switchport mode {access | trunk | general}
Mode Interface Config
Switching Commands 435

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no switchport mode
This command resets the switch port mode to its default value.
Format no switchport mode
Mode Interface Config
switchport trunk allowed vlan
Use this command to configure the list of allowed VLANs that can receive and send traffic on
this interface in tagged format when in trunking mode. The default is all.
You can modify the VLAN list by using the add and remove options and replace the VLAN
list with another list by using the all or except options. If you use the all option, all VLANs
are added to the list of allowed VLANs. The except option provides an exclusion list.
Default all
Format switchport trunk allowed vlan {vlan-list | all | {add vlan-list} |
{remove vlan-list} | {except vlan-list}}
Mode Interface Config
Parameter Description
all Specifies all VLANs from 1 to 4093. This keyword is not allowed for commands that do not
permit all VLANs in the list to be set at the same time.
add Adds the defined list of VLANs to those currently set instead of replacing the list.
remove Removes the defined list of VLANs from those currently set instead of replacing the list.
Valid IDs are from 1 to 4093. Extended-range VLAN IDs of the form XY or X,Y,Z are valid in
this command
except Lists the VLANs that must be calculated by inverting the defined list of VLANs. (VLANs are
added except the ones specified.)
van-list Either a single VLAN number from 1 to 4093 or a continuous range of VLANs described by
two VLAN numbers, the lesser one first, separated by a hyphen.
no switchport trunk allowed vlan
This command resets the list of allowed VLANs on the trunk port to its default value.
Format no switchport trunk allowed vlan
Mode Interface Config
switchport trunk native vlan
Use this command to configure the trunk port native VLAN (PVID) parameter of the switch
port. Any ingress untagged packets on the port are tagged with the value of the native VLAN.
Switching Commands 436

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The native VLAN must be in the allowed VLAN list for tagging of received untagged packets.
Otherwise, untagged packets are discarded. Packets marked with the native VLAN are
transmitted untagged from the trunk port. The default ID is 1, the default VLAN.
Default 1 (default VLAN)
Format switchport trunk native vlan vlan-id
Mode Interface Config
no switchport trunk native vlan
Use this command to reset the trunk mode native VLAN of the switch port to its default value.
Format no switchport trunk native vlan
Mode Interface Config
switchport access vlan
Use this command to configure the VLAN on the access port. You can assign one VLAN only
to the access port. The access port is member of VLAN 1 by default. You can assign the
access port to a VLAN other than VLAN 1. If you remove the access VLAN on the switch, the
access port becomes a member of VLAN 1. If you configure the access port as a member of
a VLAN that does not exist, an error occurs and the configuration does not change.
Default 1 (default VLAN)
Format switchport access vlan vlan-id
Mode Interface Config
no switchport access vlan
This command resets the switch port access mode VLAN to its default value.
Format no switchport access vlan
Mode Interface Config
show interfaces switchport
Use this command to either display the switch port status for all interfaces, for a specific
interface, or for a specific mode (access, trunk, or general). If you select a mode but do not
specify the interface for the mode, the selected mode is displayed for all interfaces.
Format show interfaces switchport {[unit/slot/port] | {access | trunk |
general} [unit/slot/port]}
Mode Privileged EXEC
Switching Commands 437

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show interfaces switchport 1/0/1
Port: 1/0/1
VLAN Membership Mode: General
Access Mode VLAN: 1 (default)
General Mode PVID: 1 (default)
General Mode Ingress Filtering: Disabled
General Mode Acceptable Frame Type: Admit all
General Mode Dynamically Added VLANs:
General Mode Untagged VLANs: 1
General Mode Tagged VLANs:
General Mode Forbidden VLANs:
Trunking Mode Native VLAN: 1 (default)
Trunking Mode Native VLAN tagging: Disable
Trunking Mode VLANs Enabled: All
Protected Port: False
Command example:
(NETGEAR Switch) #show interfaces switchport access 1/0/1
I ntf PVID
--------- ----
1 /0/1 1
Command example:
(NETGEAR Switch) #show interfaces switchport trunk 1/0/6
I ntf P VID Allowed Vlans List
--------- ----- -------------------
1 /0/6 1 All
Command example:
(NETGEAR Switch) #show interfaces switchport general 1/0/5
I ntf P VID I ngress A cceptable U ntagged T agged Forbidden Dynamic
F iltering F rame Type V lans V lans V lans Vlans
- -------- ----- ---------- ----------- --------- --------- --------- ---------
1 /0/5 1 E nabled A dmit All 7 1 0-50,55 9 ,100-200 88,96
Switching Commands 438
