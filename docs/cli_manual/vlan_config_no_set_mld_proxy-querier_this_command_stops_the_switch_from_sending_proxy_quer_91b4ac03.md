# vlan_config_no_set_mld_proxy-querier_this_command_stops_the_switch_from_sending_proxy_quer_91b4ac03

Pages: 603-614

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
When the optional detail keyword is used, the command shows the global information and
the information for all Querier-enabled VLANs.
set mld proxy-querier
If a non-querier switch receives an MLD leave message, the non-querier switch can send
queries with 0::0 as the source IP addresses. This command enables the switch to send such
proxy queries through different command modes the following ways:
• in Global Config mode, on the entire switch
• in Interface Config mode, on an interface
• in VLAN Config mode, on a particular VLAN and all interfaces participating in the VLAN.
By default, the proxy-querier is enabled.
Default enabled
Format set mld proxy-querier [vlan-id]
Mode Global Config
Interface Config
VLAN Config
no set mld proxy-querier
This command stops the switch from sending proxy queries through different command
modes in the following ways:
• in Global Config mode, on the entire switch
• in Interface Config mode, on an interface
• in VLAN Config mode, on a particular VLAN and all interfaces participating in the VLAN.
This command is specific to MLD.
Format no set mld proxy-querier [vlan-id]
Mode Global Config
Interface Config
VLAN Config
show mldsnooping proxy-querier
This command shows the global admin mode of the MLD snooping proxy-querier and the
interface on which it is enabled.
Format show mldsnooping proxy-querier
Mode Privileged EXEC
Switching Commands 603

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(Netgear Switch) #show mldsnooping proxy-querier
Admin Mode..................................... Enable
Interfaces Enabled for MLD Proxy Querier....... 1/0/1
1/0/2
1/0/3
Port Security Commands
This section describes the command you use to configure Port Security on the switch. Port
security, which is also known as port MAC locking, allows you to secure the network by
locking allowable MAC addresses on a given port. Packets with a matching source MAC
address are forwarded normally, and all other packets are discarded.
Note: To enable the SNMP trap specific to port security, see snmp-server
enable traps violation on page133.
port-security
This command enables port locking on an interface, a range of interfaces, or at the system
level.
Default disabled
Format port-security
Mode Global Config (to enable port locking globally)
Interface Config (to enable port locking on an interface or range of interfaces)
no port-security
This command disables port locking for one (Interface Config) or all (Global Config) ports.
Format no port-security
Mode Global Config
Interface Config
Switching Commands 604

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
port-security max-dynamic
This command sets the maximum number of dynamically locked MAC addresses allowed on
a specific port. The valid range is 0–4096.
Default 4096
Format port-security max-dynamic maxvalue
Mode Interface Config
no port-security max-dynamic
This command resets the maximum number of dynamically locked MAC addresses allowed
on a specific port to its default value.
Format no port-security max-dynamic
Mode Interface Config
port-security max-static
This command sets the maximum number of statically locked MAC addresses allowed on a
port. The valid range is 0–20.
Default 1
Format port-security max-static maxvalue
Mode Interface Config
no port-security max-static
This command sets maximum number of statically locked MAC addresses to the default
value.
Format no port-security max-static
Mode Interface Config
port-security mac-address
This command adds a MAC address to the list of statically locked MAC addresses for an
interface or range of interfaces. The vid is the VLAN ID.
Format port-security mac-address mac-address vid
Mode Interface Config
Switching Commands 605

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no port-security mac-address
This command removes a MAC address from the list of statically locked MAC addresses.
Format no port-security mac-address mac-address vid
Mode Interface Config
port-security mac-address move
This command converts dynamically locked MAC addresses to statically locked addresses
for an interface or range of interfaces.
Format port-security mac-address move
Mode Interface Config
port-security mac-address sticky
This command enables sticky mode Port MAC Locking on a port. If accompanied by a MAC
address and a VLAN id (for interface config mode only), it adds a sticky MAC address to the
list of statically locked MAC addresses. These sticky addresses are converted back to
dynamically locked addresses if sticky mode is disabled on the port. The vid is the VLAN ID.
The Global command applies the sticky mode to all valid interfaces (physical and LAG).
There is no global sticky mode as such.
Sticky addresses that are dynamically learned display in the output of the show
running-config command as port-security mac-address sticky mac vid entries.
This distinguishes them from static entries.
Format port-security mac-address sticky [mac-address vid]
Mode Global Config
Interface Config
Command example:
(NETGEAR)(Config)# port-security mac-address sticky
(NETGEAR)(Interface)# port-security mac-address sticky
(NETGEAR)(Interface)# port-security mac-address sticky
00:00:00:00:00:01 2
no port-security mac-address sticky
Use this command to disable the sticky mode.
Format no port-security mac-address sticky [mac-address vid]
Mode Global Config
Interface Config
Switching Commands 606

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
port-security violation shutdown
This command allows an interface to be diagnostically disabled when a violation occurs for
port MAC locking.
Format port-security violation shutdown
Mode Interface Config
no port-security violation shutdown
This command prevents an interface from being diagnostically disabled when a violation
occurs for port MAC locking.
Format no port-security violation shutdown
Mode Interface Config
show port-security
This command displays the port-security settings for the port or ports. If you do not use a
parameter, the command displays the Port Security Administrative mode. Use the optional
parameters to display the settings on a specific interface or on all interfaces. Instead of
unit/slot/port, lag lag-intf-num can be used as an alternate way to specify the
LAG interface, in which lag-intf-num is the LAG port number.
Format show port-security [unit/slot/port | all]
Mode Privileged EXEC
Term Definition
Admin Mode Port Locking mode for the entire system. This field displays if you do not supply any parameters.
For each interface, or for the interface you specify, the following information displays.
Term Definition
Admin Mode Port Locking mode for the Interface.
Dynamic Limit Maximum dynamically allocated MAC Addresses.
Static Limit Maximum statically allocated MAC Addresses.
Violation Trap Whether violation traps are enabled.
Mode
Sticky Mode The administrative mode of the port security Sticky Mode feature on the interface.
Switching Commands 607

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show port-security 0/1
Admin Dynamic Static Violation Sticky
Intf Mode Limit Limit Trap Mode Mode
------ ------- ---------- --------- --------- --------
0 /1 Disabled 1 1 Disabled Enabled
show port-security dynamic
This command displays the dynamically locked MAC addresses for the port. Instead of
unit/slot/port, lag lag-intf-num can be used as an alternate way to specify the
LAG interface, in which lag-intf-num is the LAG port number.
Format show port-security dynamic unit/slot/port
Mode Privileged EXEC
Term Definition
MAC Address MAC Address of dynamically locked MAC.
show port-security static
This command displays the statically locked MAC addresses for a port. Instead of
unit/slot/port, lag lag-intf-num can be used as an alternate way to specify the
LAG interface, in which lag-intf-num is the LAG port number.
Format show port-security static {unit/slot/port | lag lag-intf-num}
Mode Privileged EXEC
Term Definition
Statically Configured MAC The statically configured MAC address.
Address
VLAN ID The ID of the VLAN that includes the host with the specified MAC address.
Sticky Indicates whether the static MAC address entry is added in sticky mode.
Command example:
(NETGEAR Switch) #show port-security static 1/0/1
Number of static MAC addresses configured: 2
Statically configured MAC Address VLAN ID Sticky
--------------------------------- ------- ------
00:00:00:00:00:01 2 Yes
00:00:00:00:00:02 2 No
Switching Commands 608

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show port-security violation
This command displays the source MAC address of the last packet discarded on a locked
port. Instead of unit/slot/port, lag lag-intf-num can be used as an alternate way to
specify the LAG interface, in which lag-intf-num is the LAG port number.
Format show port-security violation {unit/slot/port | lag lag-intf-num}
Mode Privileged EXEC
Term Definition
MAC Address The source MAC address of the last frame that was discarded at a locked port.
VLAN ID The VLAN ID, if applicable, associated with the MAC address of the last frame that was discarded at
a locked port.
LLDP (802.1AB) Commands
This section describes the command you use to configure Link Layer Discovery Protocol
(LLDP), which is defined in the IEEE 802.1AB specification. LLDP allows stations on an 802
LAN to advertise major capabilities and physical descriptions. The advertisements allow a
network management system (NMS) to access and display this information.
lldp transmit
Use this command to enable the LLDP advertise capability on an interface or a range of
interfaces.
Default disabled
Format lldp transmit
Mode Interface Config
no lldp transmit
Use this command to return the local data transmission capability to the default.
Format no lldp transmit
Mode Interface Config
Switching Commands 609

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
lldp receive
Use this command to enable the LLDP receive capability on an interface or a range of
interfaces.
Default disabled
Format lldp receive
Mode Interface Config
no lldp receive
Use this command to return the reception of LLDPDUs to the default value.
Format no lldp receive
Mode Interface Config
lldp timers
Use this command to set the timing parameters for local data transmission on ports enabled
for LLDP. The interval-seconds determines the number of seconds to wait between
transmitting local data LLDPDUs. The range is 1–32768 seconds. The hold-value is the
multiplier on the transmit interval that sets the TTL in local data LLDPDUs. The multiplier
range is 2–10. The reinit-seconds is the delay before reinitialization, and the range is
1–0 seconds.
Default interval—30 seconds
hold—4
reinit—2 seconds
Format lldp timers [interval interval-seconds] [hold hold-value] [reinit
reinit-seconds]
Mode Global Config
no lldp timers
Use this command to return any or all timing parameters for local data transmission on ports
enabled for LLDP to the default values.
Format no lldp timers [interval] [hold] [reinit]
Mode Global Config
lldp transmit-tlv
Use this command to specify which optional type length values (TLVs) in the 802.1AB basic
management set are transmitted in the LLDPDUs from an interface or range of interfaces.
Use sys-name to transmit the system name TLV.
Switching Commands 610

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
To configure the system name, see snmp-server on page129. Use sys-desc to transmit
the system description TLV. Use sys-cap to transmit the system capabilities TLV. Use
port-desc to transmit the port description TLV. To configure the port description, see
description (Interface Config) on page373
Default no optional TLVs are included
Format lldp transmit-tlv [sys-desc] [sys-name] [sys-cap] [port-desc]
Mode Interface Config
no lldp transmit-tlv
Use this command to remove an optional TLV from the LLDPDUs. Use the command without
parameters to remove all optional TLVs from the LLDPDU.
Format no lldp transmit-tlv [sys-desc] [sys-name] [sys-cap] [port-desc]
Mode Interface Config
lldp transmit-mgmt
Use this command to include transmission of the local system management address
information in the LLDPDUs. This command can be used to configure a single interface or a
range of interfaces.
Format lldp transmit-mgmt
Mode Interface Config
no lldp transmit-mgmt
Use this command to include transmission of the local system management address
information in the LLDPDUs. Use this command to cancel inclusion of the management
information in LLDPDUs.
Format no lldp transmit-mgmt
Mode Interface Config
lldp notification
Use this command to enable remote data change notifications on an interface or a range of
interfaces.
Default disabled
Format lldp notification
Mode Interface Config
Switching Commands 611

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no lldp notification
Use this command to disable notifications.
Default disabled
Format no lldp notification
Mode Interface Config
lldp notification-interval
Use this command to configure how frequently the system sends remote data change
notifications. The interval parameter is the number of seconds to wait between sending
notifications. The valid interval range is 5–3600 seconds.
Default 5
Format lldp notification-interval interval
Mode Global Config
no lldp notification-interval
Use this command to return the notification interval to the default value.
Format no lldp notification-interval
Mode Global Config
clear lldp statistics
Use this command to reset all LLDP statistics, including MED-related information.
Format clear lldp statistics
Mode Privileged Exec
clear lldp remote-data
Use this command to delete all information from the LLDP remote data table, including
MED-related information.
Format clear lldp remote-data
Mode Global Config
Switching Commands 612

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show lldp
Use this command to display a summary of the current LLDP configuration.
Format show lldp
Mode Privileged Exec
Term Definition
Transmit Interval How frequently the system transmits local data LLDPDUs, in seconds.
Transmit Hold The multiplier on the transmit interval that sets the TTL in local data LLDPDUs.
Multiplier
Re-initialization The delay before reinitialization, in seconds.
Delay
Notification Interval How frequently the system sends remote data change notifications, in seconds.
show lldp interface
Use this command to display a summary of the current LLDP configuration for a specific
interface or for all interfaces.
Format show lldp interface {unit/slot/port | all}
Mode Privileged Exec
Term Definition
Interface The interface in a unit/slot/port format.
Link Shows whether the link is up or down.
Transmit Shows whether the interface transmits LLDPDUs.
Receive Shows whether the interface receives LLDPDUs.
Notify Shows whether the interface sends remote data change notifications.
TLVs Shows whether the interface sends optional TLVs in the LLDPDUs. The TLV codes can be 0 (Port
Description), 1 (System Name), 2 (System Description), or 3 (System Capability).
Mgmt Shows whether the interface transmits system management address information in the LLDPDUs.
show lldp statistics
Use this command to display the current LLDP traffic and remote table statistics for a specific
interface or for all interfaces.
Format show lldp statistics {unit/slot/port | all}
Mode Privileged Exec
Switching Commands 613

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Last Update The amount of time since the last update to the remote table in days, hours, minutes, and seconds.
Total Inserts Total number of inserts to the remote data table.
Total Deletes Total number of deletes from the remote data table.
Total Drops Total number of times the complete remote data received was not inserted due to insufficient
resources.
Total Ageouts Total number of times a complete remote data entry was deleted because the Time to Live interval
expired.
The table contains the following column headings.
Term Definition
Interface The interface in unit/slot/port format.
TX Total Total number of LLDP packets transmitted on the port.
RX Total Total number of LLDP packets received on the port.
Discards Total number of LLDP frames discarded on the port for any reason.
Errors The number of invalid LLDP frames received on the port.
Ageouts Total number of times a complete remote data entry was deleted for the port because the Time to
Live interval expired.
TVL Discards The number of TLVs discarded.
TVL Unknowns Total number of LLDP TLVs received on the port where the type value is in the reserved range, and
not recognized.
TLV MED The total number of LLDP-MED TLVs received on the interface.
TLV 802.1 The total number of LLDP TLVs received on the interface which are of type 802.1.
TLV 802.3 The total number of LLDP TLVs received on the interface which are of type 802.3.
show lldp remote-device
Use this command to display summary information about remote devices that transmit
current LLDP data to the system. You can show information about LLDP remote data
received on all ports or on a specific port.
Format show lldp remote-device {unit/slot/port | all}
Mode Privileged EXEC
Switching Commands 614
