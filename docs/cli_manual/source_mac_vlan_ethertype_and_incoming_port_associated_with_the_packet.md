# source_mac_vlan_ethertype_and_incoming_port_associated_with_the_packet

Pages: 522-528

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
port-channel load-balance
This command selects the load-balancing option used on a port-channel (LAG). Traffic is
balanced on a port-channel (LAG) by selecting one of the links in the channel over which to
transmit specific packets. The link is selected by creating a binary pattern from selected fields
in a packet, and associating that pattern with a particular link.
Load-balancing is not supported on every device. The range of options for load-balancing
may vary per device.
This command can be configured for a single interface, a range of interfaces, or all interfaces.
Instead of unit/slot/port, lag lag-intf-num can be used as an alternate way to
specify the LAG interface, in which lag-intf-num is the LAG port number.
Default 3
Format port-channel load-balance {1 | 2 | 3 | 4 | 5 | 6 | 7} {unit/slot/port | all}
Mode Interface Config
Global Config
Term Definition
1 Source MAC, VLAN, EtherType, and incoming port associated with the packet
2 Destination MAC, VLAN, EtherType, and incoming port associated with the packet
3 Source/Destination MAC, VLAN, EtherType, and incoming port associated with the packet
4 Source IP and Source TCP/UDP fields of the packet
5 Destination IP and Destination TCP/UDP Port fields of the packet
6 Source/Destination IP and source/destination TCP/UDP Port fields of the packet
7 Enhanced hashing mode
unit/slot/port Global Config Mode only: The interface is a logical unit/slot/port number of a configured
port-channel.
all Global Config Mode only: all applies the command to all currently configured port-channels.
no port-channel load-balance
This command reverts to the default load balancing configuration.
Format no port-channel load-balance {unit/slot/port | all}
Mode Interface Config
Global Config
Switching Commands 522

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
unit/slot/port Global Config Mode only: The interface is a logical unit/slot/port number of a configured port-channel.
all Global Config Mode only: all applies the command to all currently configured port-channels.
port-channel local-preference
This command enables the local-preference mode on a port-channel (LAG) interface or
range of interfaces. By default, the local-preference mode for a port-channel is disabled. This
command can be used only on port-channel interfaces.
Default Disabled
Format port-channel local-preference
Mode Interface Config
no port-channel local-preference
This command disables the local-preference mode on a port-channel.
Format no port-channel local-preference
Mode Interface Config
port-channel min-links
This command configures the port-channel’s minimum links for lag interfaces. The number
parameter can be in the range 1–8. The default is 1.
Default 1
Format port-channel min-links number
Mode Interface Config
port-channel name
This command defines a name for the port-channel (LAG). The interface is a logical
unit/slot/port for a configured port-channel, and name is an alphanumeric string up to
15 characters. Instead of unit/slot/port, lag lag-intf-num can be used as an
alternate way to specify the LAG interface, in which lag-intf-num is the LAG port number.
Format port-channel name {logical unit/slot/port} name
Mode Global Config
Switching Commands 523

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
port-channel system priority
Use this command to configure port-channel system priority. The valid range of priority is
0-65535.
Default 0x8000
Format port-channel system priority priority
Mode Global Config
no port-channel system priority
Use this command to configure the default port-channel system priority value.
Format no port-channel system priority
Mode Global Config
show lacp actor
Use this command to display LACP actor attributes. Instead of unit/slot/port, lag
lag-intf-num can be used as an alternate way to specify the LAG interface, in which
lag-intf-num is the LAG port number.
Format show lacp actor {unit/slot/port | all}
Mode Global Config
The following output parameters are displayed.
Parameter Description
System Priority The administrative value of the Key.
Actor Admin Key The administrative value of the Key.
Port Priority The priority value assigned to the Aggregation Port.
Admin State The administrative values of the actor state as transmitted by the Actor in LACPDUs.
show lacp partner
Use this command to display LACP partner attributes. Instead of unit/slot/port, lag
lag-intf-num can be used as an alternate way to specify the LAG interface, in which
lag-intf-num is the LAG port number.
Format show lacp actor {unit/slot/port | all}
Mode Privileged EXEC
Switching Commands 524

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The following output parameters are displayed.
Parameter Description
System Priority The administrative value of priority associated with the Partner’s System ID.
System-ID Represents the administrative value of the Aggregation Port’s protocol Partner’s System ID.
Admin Key The administrative value of the Key for the protocol Partner.
Port Priority The administrative value of the Key for protocol Partner.
Port-ID The administrative value of the port number for the protocol Partner.
Admin State The administrative values of the actor state for the protocol Partner.
show port-channel brief
This command displays the static capability of all port-channel (LAG) interfaces on the device
as well as a summary of individual port-channel interfaces.
Format show port-channel brief
Mode User EXEC
For each port-channel the following information is displayed.
Term Definition
Logical Interface The unit/slot/port of the logical interface.
Port-channel Name The name of port-channel (LAG) interface.
Link-State Shows whether the link is up or down.
Trap Flag Shows whether trap flags are enabled or disabled.
Type Shows whether the port-channel is statically or dynamically maintained.
Mbr Ports The members of this port-channel.
Active Ports The ports that are actively participating in the port-channel.
show port-channel
This command displays an overview of all port-channels (LAGs) on the switch.
Format show port-channel
Mode Privileged EXEC
Switching Commands 525

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Logical Interface The valid unit/slot/port number.
Port-Channel The name of this port-channel (LAG). You may enter any string of up to 15 alphanumeric characters.
Name
Link State Indicates whether the Link is up or down.
Admin Mode May be enabled or disabled. The factory default is enabled.
Type The status designating whether a particular port-channel (LAG) is statically or dynamically
maintained.
• Static. The port-channel is statically maintained.
• Dynamic. The port-channel is dynamically maintained.
Load Balance The load balance option associated with this LAG. See port-channel load-balance on page522.
Option
Local Preference Indicates whether the local preference mode is enabled or disabled.
Mode
Mbr Ports A listing of the ports that are members of this port-channel (LAG), in unit/slot/port notation.
There can be a maximum of eight ports assigned to a given port-channel (LAG).
Device Timeout For each port, lists the timeout (long or short) for Device Type (actor or partner).
Port Speed Speed of the port-channel port.
Active Ports This field lists ports that are actively participating in the port-channel (LAG).
Command example:
(NETGEAR Switch) #show port-channel 0/3/1
Local Interface................................ 0/3/1
Channel Name................................... ch1
Link State..................................... Up
Admin Mode..................................... Enabled
Type........................................... Static
Load Balance Option............................ 3
(Src/Dest MAC, VLAN, EType, incoming port)
Local Preference Mode.......................... Enabled
Mbr Device/ Port Port
Ports Timeout Speed Active
------ ------------- --------- -------
1/0/1 actor/long Auto True
partner/long
1/0/2 actor/long Auto True
partner/long
1/0/3 actor/long Auto False
Switching Commands 526

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
partner/long
1/0/4 actor/long Auto False
partner/long
show port-channel system priority
Use this command to display the port-channel system priority.
Format show port-channel system priority
Mode Privileged EXEC
show port-channel counters
Use this command to display port-channel counters for the specified port.
Format show port-channel unit/slot/port counters
Mode Privileged EXEC
Term Definition
Local Interface The valid unit/slot/port number.
Channel Name The name of this port-channel (LAG).
Link State Indicates whether the Link is up or down.
Admin Mode May be enabled or disabled. The factory default is enabled.
Port Channel Flap The number of times the port-channel was inactive.
Count
Mbr Ports The slot/port for the port member.
Mbr Flap Counters The number of times a port member is inactive, either because the link is down, or the admin state is
disabled.
Command example:
(NETGEAR Switch) #show port-channel 3/1 counters
Local Interface................................ 3/1
Channel Name................................... ch1
Link State..................................... Down
Admin Mode..................................... Enabled
Port Channel Flap Count........................ 0
Mbr Mbr Flap
Ports Counters
------ ---------
0/1 0
Switching Commands 527

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
0/2 0
0/3 1
0/4 0
0/5 0
0/6 0
0/7 0
0/8 0
clear port-channel counters
Use this command to clear and reset specified port-channel and member flap counters for
the specified interface.
Format clear port-channel {lag-intf-num | unit/slot/port} counters
Mode Privileged EXEC
clear port-channel all counters
Use this command to clear and reset all port-channel and member flap counters for the
specified interface.
Format clear port-channel all counters
Mode Privileged EXEC
Port Mirroring Commands
Port mirroring, which is also known as port monitoring, selects network traffic that you can
analyze with a network analyzer, such as a SwitchProbe device or other Remote Monitoring
(RMON) probe.
monitor session source
This command adds a source interface for a port mirroring session that is identified by the
session-id argument (an integer value).
Use the source interface {unit/slot/port | cpu | lag lag-group-id}
parameters to specify the interface to monitor. You can also configure a VLAN as the source
for the session (all member ports of that VLAN are monitored).
Switching Commands 528
