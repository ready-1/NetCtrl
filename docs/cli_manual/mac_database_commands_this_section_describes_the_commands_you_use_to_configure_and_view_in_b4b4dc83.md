# mac_database_commands_this_section_describes_the_commands_you_use_to_configure_and_view_in_b4b4dc83

Pages: 636-637

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no auto-dos
This command disables Auto-DoS on the switch.
Format no auto-dos
Mode Global Config
show auto-dos
The output of this command shows whether Auto-DoS is enabled on the switch.
Format show auto-dos
Mode Global Config
MAC Database Commands
This section describes the commands you use to configure and view information about the
MAC databases.
bridge aging-time
This command configures the forwarding database address aging time-out in seconds. The
seconds parameter must be within the range of 10 to 1,000,000 seconds. In an SVL
system, the [fdbid/all] parameter is not used and will be ignored if entered. In an SVL system,
the [fdbid/all] parameter is not used and will be ignored if entered.
Default 300
Format bridge aging-time seconds
Mode Global Config
no bridge aging-time
This command sets the forwarding database address aging time-out to the default value. In
an SVL system, the [fdbid/all] parameter is not used and will be ignored if entered.
Format no bridge aging-time
Mode Global Config
Switching Commands 636

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show forwardingdb agetime
This command displays the timeout for address aging.
Default all
Format show forwardingdb agetime
Mode Privileged EXEC
Term Definition
Address Aging Displays the system's address aging timeout value in seconds.
Timeout
show mac-address-table multicast
This command displays the Multicast Forwarding Database (MFDB) information. If you enter
the command with no parameter, the entire table is displayed. You can display the table entry
for one MAC Address by specifying the MAC address as an optional parameter.
Format show mac-address-table multicast macaddr
Mode Privileged EXEC
Term Definition
VLAN ID The VLAN in which the MAC address is learned.
MAC Address A multicast MAC address for which the switch has forwarding or filtering information. The format is 6
two-digit hexadecimal numbers that are separated by colons, for example 01:23:45:67:89:AB.
Source The component that is responsible for this entry in the Multicast Forwarding Database. The source
can be IGMP Snooping, GMRP, and Static Filtering.
Type The type of the entry. Static entries are those that are configured by the end user. Dynamic entries
are added to the table as a result of a learning process or protocol.
Description The text description of this multicast table entry.
Interfaces The list of interfaces that are designated for forwarding (Fwd:) and filtering (Flt:).
Fwd Interface The resultant forwarding list is derived from combining all the component’s forwarding interfaces and
removing the interfaces that are listed as the static filtering interfaces.
Switching Commands 637
