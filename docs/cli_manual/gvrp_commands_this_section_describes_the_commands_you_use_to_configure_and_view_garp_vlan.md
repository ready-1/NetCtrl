# gvrp_commands_this_section_describes_the_commands_you_use_to_configure_and_view_garp_vlan

Pages: 457-458

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default 1000
Format set garp timer leaveall centiseconds
Mode Interface Config
Global Config
no set garp timer leaveall
This command sets how frequently Leave All PDUs are generated the default and only has
an effect when GVRP is enabled.
Format no set garp timer leaveall
Mode Interface Config
Global Config
show garp
This command displays GARP information.
Format show garp
Mode Privileged EXEC
User EXEC
Term Definition
GMRP Admin The administrative mode of GARP Multicast Registration Protocol (GMRP) for the system.
Mode
GVRP Admin Mode The administrative mode of GARP VLAN Registration Protocol (GVRP) for the system.
GVRP Commands
This section describes the commands you use to configure and view GARP VLAN
Registration Protocol (GVRP) information. GVRP-enabled switches exchange VLAN
configuration information, which allows GVRP to provide dynamic VLAN creation on trunk
ports and automatic VLAN pruning.
Note: If GVRP is disabled, the system does not forward GVRP messages.
Switching Commands 457

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
set gvrp adminmode
This command enables GVRP on the system.
Default Disabled
Format set gvrp adminmode
Mode Privileged EXEC
no set gvrp adminmode
This command disables GVRP.
Format no set gvrp adminmode
Mode Privileged EXEC
set gvrp interfacemode
This command enables GVRP on a single port (Interface Config mode), a range of ports
(Interface Range mode), or all ports (Global Config mode).
Default Disabled
Format set gvrp interfacemode
Mode Interface Config
Interface Range
Global Config
no set gvrp interfacemode
This command disables GVRP on a single port (Interface Config mode) or all ports (Global
Config mode). If GVRP is disabled, Join Time, Leave Time and Leave All Time have no
effect.
Format no set gvrp interfacemode
Mode Interface Config
Global Config
show gvrp configuration
This command displays Generic Attributes Registration Protocol (GARP) information for one
or all interfaces.
Format show gvrp configuration {unit/slot/port | all}
Mode Privileged EXEC
User EXEC
Switching Commands 458
