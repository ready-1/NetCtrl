# cpu_ports_cpu_ports_are_handled_by_the_driver_as_one_or_more_physical_entities_located

Pages: 16-23

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 4. Types of ports
Port Type Description
Logical Interfaces Port-channel or Link Aggregation Group (LAG) interfaces are logical
interfaces that are only used for bridging functions.
VLAN routing interfaces are only used for routing functions.
Loopback interfaces are logical interfaces that are always up.
Tunnel interfaces are logical point-to-point links that carry encapsulated
packets.
CPU ports CPU ports are handled by the driver as one or more physical entities located
on physical slots.
Note: In the CLI, loopback and tunnel interfaces do not use the
unit/slot/port format. To specify a loopback interface, you use
the loopback ID. To specify a tunnel interface, you use the tunnel ID.
Using the No Form of a Command
The no keyword is a specific form of an existing command and does not represent a new or
distinct command. Almost every configuration command has a no form. In general, use the
no form to reverse the action of a command or reset a value back to the default. For example,
the no shutdown configuration command reverses the shutdown of an interface. Use the
command without the keyword no to reenable a disabled feature or to enable a feature that is
disabled by default. Only the configuration commands are available in the no form.
Executing Show Commands
All show commands can be issued from any configuration mode (Global Configuration,
Interface Configuration, VLAN Configuration, etc.). The show commands provide information
about system and feature-specific configuration, status, and statistics. Previously, show
commands could be issued only in User EXEC or Privileged EXEC modes.
CLI Output Filtering
Many CLI show commands include considerable content to display to the user. This can
make output confusing and cumbersome to parse through to find the information of desired
importance. The CLI Output Filtering feature allows the user, when executing CLI show
display commands, to optionally specify arguments to filter the CLI output to display only
desired information. The result is to simplify the display and make it easier for the user to find
the information the user is interested in.
Using the Command-Line Interface 16

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The main functions of the CLI Output Filtering feature are:
• Pagination Control
- Supports enabling/disabling paginated output for all show CLI commands. When
disabled, output is displayed in its entirety. When enabled, output is displayed
page-by-page such that content does not scroll off the terminal screen until the user
presses a key to continue. --More-- or (q)uit is displayed at the end of each page.
- When pagination is enabled, press the return key to advance a single line, press q or
Q to stop pagination, or press any other key to advance a whole page. These keys
are not configurable.
Note: Although some switch show commands already support pagination,
the implementation is unique per command and not generic to all
commands.
• Output Filtering
- “Grep”-like control for modifying the displayed output to only show the user-desired
content.
- Filter displayed output to only include lines containing a specified string match.
- Filter displayed output to exclude lines containing a specified string match.
- Filter displayed output to only include lines including and following a specified string
match.
- Filter displayed output to only include a specified section of the content (for example,
“interface 0/1”) with a configurable end-of-section delimiter.
- String matching should be case insensitive.
- Pagination, when enabled, also applies to filtered output.
The following shows an example of the extensions made to the CLI show commands for
the Output Filtering feature.
(NETGEAR Switch) #show running-config ?
<cr> Press enter to execute the command.
| Output filter options.
<scriptname> Script file name for writing active configuration.
all Show all the running configuration on the switch.
i nterface Display the running configuration for specificed interface
on the switch.
(NETGEAR Switch) #show running-config | ?
begin Begin with the line that matches
exclude Exclude lines that matches
include Include lines that matches
section Display portion of lines
For new commands for the feature, see CLI Output Filtering Commands on page192.
Using the Command-Line Interface 17

Software Modules

The switch software consists of flexible modules that can be applied in various combinations to
develop advanced Layer 2/3/4+ products. The commands and command modes available on
your switch depend on the installed modules. Additionally, for some show commands, the output
fields might change based on the modules included in the switch software.
The switch software suite that is supported for the M4300 and M4300-96X series switches
includes the following modules:
• Switching (Layer 2)
• Routing (Layer 3)
• IPv6 routing
• Multicast
• Quality of Service
• Management (CLI, Web UI, and SNMP)
• IPv6 Management
Allows management of the switch through an IPv6 address without requiring the IPv6
Routing package in the system. The management address can be associated with the
network port (a front-panel switch port), a router interface (a port or VLAN), and the
service port.
• Secure Management

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command Modes
The CLI groups commands into modes according to the command function. Each of the
command modes supports specific commands. The commands in one mode are not
available until you switch to that particular mode, with the exception of the User EXEC mode
commands. You can execute the User EXEC mode commands in the Privileged EXEC
mode.
The command prompt changes in each command mode to help you identify the current
mode. The following table describes the command modes and the prompts visible in that
mode.
Note: The command modes available on your switch depend on the
software modules that are installed.
T able 5. CLI Command Modes
Command Mode Prompt Mode Description
User EXEC Switch> Contains a limited set of commands to view
basic system information.
Privileged EXEC Switch# Allows you to issue any EXEC command,
enter the VLAN mode, or enter the Global
Configuration mode.
Global Config Switch (Config)# Groups general setup commands and
permits you to make modifications to the
running configuration.
VLAN Config Switch (Vlan)# Groups all the VLAN commands.
Interface Config Switch (Interface Manages the operation of an interface and
unit/slot/port)# provides access to the router interface
configuration commands.
Switch (Interface Loopback id)#
Use this mode to set up a physical port for a
specific logical connection operation.
Switch (Interface Tunnel id)#
Switch (Interface unit/slot/port Use this mode to manage the operation of a
(startrange)-unit/slot/port range of interfaces. For example the prompt
(endrange)# may display as follows:
Switch (Interface 1/0/1-1/0/4) #
Switch (Interface lag Enters LAG Interface configuration mode for
lag-intf-num)# the specified LAG.
Switch (Interface vlan vlan-id)# Enters VLAN routing interface configuration
mode for the specified VLAN ID.
Software Modules 19

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 5. CLI Command Modes (continued)
Command Mode Prompt Mode Description
Line Console Switch (config-line)# Contains commands to configure outbound
telnet settings and console interface
settings, as well as to configure console
login/enable authentication.
Line SSH Switch (config-ssh)# Contains commands to configure SSH
login/enable authentication.
Line Telnet Switch (config-telnet)# Contains commands to configure telnet
login/enable authentication.
AAA IAS User Switch (Config-IAS-User)# Allows password configuration for a user in
Config the IAS database.
Mail Server Config Switch (Mail-Server)# Allows configuration of the email server.
Policy Map Config Switch (Config-policy-map)# Contains the QoS Policy-Map configuration
commands.
Policy Class Config Switch(Config-policy-class-map)# Consists of class creation, deletion, and
matching commands. The class match
commands specify Layer 2, Layer 3, and
general match criteria.
Class Map Config Switch (Config-class-map)# Contains the QoS class map configuration
commands for IPv4.
Ipv6_Class-Map Switch (Config-class-map)# Contains the QoS class map configuration
Config commands for IPv6.
Router OSPF Switch (Config-router)# Contains the OSPF configuration
Config commands.
Router OSPFv3 Switch (Config rtr)# Contains the OSPFv3 configuration
Config commands.
Router RIP Config Switch (Config-router)# Contains the RIP configuration commands.
Route Map Config Switch (config-route-map)# Contains the route map configuration
commands.
IPv6 Address Switch (Config-router-af)# Contains the IPv6 address family
Family Config configuration commands.
MAC Access-list Switch (Config-mac-access-list)# Allows you to create a MAC Access-List and
Config to enter the mode containing MAC
Access-List configuration commands.
TACACS Config Switch (Tacacs)# Contains commands to configure properties
for the TACACS servers.
DHCP Pool Switch (Config dhcp-pool)# Contains the DHCP server IP address pool
Config configuration commands.
Software Modules 20

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 5. CLI Command Modes (continued)
Command Mode Prompt Mode Description
DHCPv6 Pool Switch (Config dhcp6-pool)# Contains the DHCPv6 server IPv6 address
Config pool configuration commands.
Stack Global Switch (Config stack)# Allows you to access the Stack Global
Config Mode Config Mode.
ARP Access-List Switch (Config-arp-access-list)# Contains commands to add ARP ACL rules
Config Mode in an ARP Access List.
Support Mode Switch (Support)# Allows access to the support commands,
which should only be used by the
manufacturer's technical support personnel
as improper use could cause unexpected
system behavior and/or invalidate product
warranty.
The following table explains how to enter or exit each mode.
Table 6. CLI Mode Access and Exit
Command Mode Access Method Exit or Access Previous Mode
User EXEC This is the first level of access. To exit, enter logout.
Privileged EXEC From the User EXEC mode, enter To exit to the User EXEC mode, enter exit or
enable. press Ctrl-Z.
Global Config From the Privileged EXEC mode, enter To exit to the Privileged EXEC mode, enter
configure. exit, or press Ctrl-Z.
VLAN Config From the Privileged EXEC mode, enter To exit to the Privileged EXEC mode, enter
vlan database. exit, or press Ctrl-Z.
Interface Config From the Global Config mode, enter:
interface unit/slot/port
From the Global Config mode, enter:
interface loopback id
From the Global Config mode, enter:
interface tunnel id
To exit to the Global Config mode, enter exit.
From the Global Config mode, enter: To return to the Privileged EXEC mode, enter
interface
Ctrl-Z.
unit/slot/port(startrange)-
unit/slot/port(endrange)
From the Global Config mode, enter:
interface lag lag-intf-num
From the Global Config mode, enter:
interface vlan vlan-id
Software Modules 21

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 6. CLI Mode Access and Exit (continued)
Command Mode Access Method Exit or Access Previous Mode
Line Console From the Global Config mode, enter To exit to the Global Config mode, enter exit.
line console. To return to the Privileged EXEC mode, enter
Ctrl-Z.
Line SSH From the Global Config mode, enter To exit to the Global Config mode, enter exit.
line ssh. To return to the Privileged EXEC mode, enter
Ctrl-Z.
Line Telnet From the Global Config mode, enter To exit to the Global Config mode, enter exit.
line telnet. To return to the Privileged EXEC mode, enter
Ctrl-Z.
AAA IAS User From the Global Config mode, enter To exit to the Global Config mode, enter exit.
Config aaa ias-user username name. To return to the Privileged EXEC mode, enter
Ctrl-Z.
Mail Server Config From the Global Config mode, enter To exit to the Global Config mode, enter exit.
mail-server address. To return to the Privileged EXEC mode, enter
Ctrl-Z.
Policy-Map From the Global Config mode, enter To exit to the Global Config mode, enter exit.
Config policy-map. To return to the Privileged EXEC mode, enter
Ctrl-Z.
Policy-Class-Map From the Policy Map mode enter class. To exit to the Policy Map mode, enter exit. To
Config return to the Privileged EXEC mode, enter
Ctrl-Z.
Class-Map From the Global Config mode, enter To exit to the Global Config mode, enter exit.
Config class-map, and specify the optional To return to the Privileged EXEC mode, enter
keyword ipv4 to specify the Layer 3 Ctrl-Z.
protocol for this class. See class-map on
p age939 for more information.
VPC From Global Config mode, enter vpc. To exit to the Global Config mode, enter exit.
To return to the Privileged EXEC mode, enter
Ctrl-Z.
Ipv6-Class-Map From the Global Config mode, enter To exit to the Global Config mode, enter exit.
Config class-map and specify the optional To return to the Privileged EXEC mode, enter
keyword ipv6 to specify the Layer 3 Ctrl-Z.
protocol for this class. See class-map on
p age939 for more information.
Router OSPF From the Global Config mode, enter To exit to the Global Config mode, enter exit.
Config router ospf. To return to the Privileged EXEC mode, enter
Ctrl-Z.
Router OSPFv3 From the Global Config mode, enter To exit to the Global Config mode, enter exit.
Config ipv6 router ospf. To return to the Privileged EXEC mode, enter
Ctrl-Z.
Software Modules 22

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 6. CLI Mode Access and Exit (continued)
Command Mode Access Method Exit or Access Previous Mode
Router RIP From the Global Config mode, enter To exit to the Global Config mode, enter exit.
Config router rip. To return to the Privileged EXEC mode, enter
Ctrl-Z.
Route Map Config From the Global Config mode, enter To exit to the Global Config mode, enter exit.
route-map map-tag. To return to the Privileged EXEC mode, enter
Ctrl-Z.
MAC Access-list From the Global Config mode, enter To exit to the Global Config mode, enter exit.
Config mac access-list extended name. To return to the Privileged EXEC mode, enter
Ctrl-Z.
TACACS Config From the Global Config mode, enter To exit to the Global Config mode, enter exit.
tacacs-server host ip-addr, To return to the Privileged EXEC mode, enter
where ip-addr is the IP address of the Ctrl-Z.
TACACS server on your network.
DHCP Pool From the Global Config mode, enter To exit to the Global Config mode, enter exit.
Config ip dhcp pool pool-name. To return to the Privileged EXEC mode, enter
Ctrl-Z.
DHCPv6 Pool From the Global Config mode, enter To exit to the Global Config mode, enter exit.
Config ip dhcpv6 pool pool-name. To return to the Privileged EXEC mode, enter
Ctrl-Z.
Stack Global From the Global Config mode, enter To exit to the Global Config mode, enter the
Config Mode stack. exit command. To return to the Privileged
EXEC mode, enter Ctrl-Z.
ARP Access-List From the Global Config mode, enter arp To exit to the Global Config mode, enter the
Config Mode access-list. exit command. To return to the Privileged
EXEC mode, enter Ctrl-Z.
Support Mode From the Privileged EXEC mode, enter To exit to the Privileged EXEC mode, enter
support. exit, or press Ctrl-Z.
Note: The support command is
available only after you issued the
techsupport enable command.
Command Completion and Abbreviation
Command completion finishes spelling the command when you type enough letters of a
command to uniquely identify the command keyword. Once you have entered enough letters,
press the SPACEBAR or TAB key to complete the word.
Command abbreviation allows you to execute a command when you have entered there are
enough letters to uniquely identify the command. You must enter all of the required keywords
and parameters before you enter the command.
Software Modules 23
