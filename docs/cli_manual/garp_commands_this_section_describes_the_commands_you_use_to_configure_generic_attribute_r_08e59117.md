# garp_commands_this_section_describes_the_commands_you_use_to_configure_generic_attribute_r_08e59117

Pages: 455-456

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show private-group
This command displays information about a private group. If you do not specify a group
name, group identifier, or port, the command displays information about all private groups.
Format show private-group [private-group-name | private-group-id | port
unit/slot/port]
Mode Privileged EXEC
Term Description
Interface A valid slot and port number separated by forward slashes.
Port VLANID The VLAN ID that is associated with the port.
Private Group ID The identifier of the private group (from 1 to 192).
Private Group The name of the private group. The name string can be up to 24 bytes of non-blank characters.
Name
Private Group The mode of the private group. The mode can be either isolated or community.
Mode
GARP Commands
This section describes the commands you use to configure Generic Attribute Registration
Protocol (GARP) and view GARP status. The commands in this section affect both GARP
VLAN Registration Protocol (GVRP) and GARP Multicast Registration Protocol (GMRP).
GARP is a protocol that allows client stations to register with the switch for membership in
VLANS (by using GVMP) or multicast groups (by using GVMP).
set garp timer join
This command sets the GVRP join time per GARP for one interface, a range of interfaces, or
all interfaces. Join time is the interval between the transmission of GARP Protocol Data Units
(PDUs) registering (or reregistering) membership for a VLAN or multicast group. This
command has an effect only when GVRP is enabled. The time is from 10 to 100
centiseconds. The value 20 centiseconds is 0.2 seconds.
Default 20
Format set garp timer join centiseconds
Mode Interface Config
Global Config
Switching Commands 455

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no set garp timer join
This command sets the GVRP join time to the default and only has an effect when GVRP is
enabled.
Format no set garp timer join
Mode Interface Config
Global Config
set garp timer leave
This command sets the GVRP leave time for one interface, a range of interfaces, or all
interfaces or all ports and only has an effect when GVRP is enabled. Leave time is the time to
wait after receiving an unregister request for a VLAN or a multicast group before deleting the
VLAN entry. This can be considered a buffer time for another station to assert registration for
the same attribute in order to maintain uninterrupted service. The leave time is 20 to 600
centiseconds. The value 60 centiseconds is 0.6 seconds. The leave time must be greater
than or equal to three times the join time.
Default 60
Format set garp timer leave centiseconds
Mode Interface Config
Global Config
no set garp timer leave
This command sets the GVRP leave time on all ports or a single port to the default and only
has an effect when GVRP is enabled.
Format no set garp timer leave
Mode Interface Config
Global Config
set garp timer leaveall
This command sets how frequently Leave All PDUs are generated. A Leave All PDU
indicates that all registrations will be unregistered. Participants would need to rejoin in order
to maintain registration. The value applies per port and per GARP participation. The time may
range from 200 to 6000 centiseconds. The value 1000 centiseconds is 10 seconds. You can
use this command on all ports (Global Config mode), or on a single port or a range of ports
(Interface Config mode) and it only has an effect only when GVRP is enabled. The leave all
time must be greater than the leave time.
Switching Commands 456
