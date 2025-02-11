# lldp_remote_device_detail

Pages: 616-620

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Local Interface The interface that received the LLDPDU from the remote device.
Remote Identifier An internal identifier to the switch to mark each remote device to the system.
Chassis ID The type of identification used in the Chassis ID field.
Subtype
Chassis ID The chassis of the remote device.
Port ID Subtype The type of port on the remote device.
Port ID The port number that transmitted the LLDPDU.
System Name The system name of the remote device.
System Description Describes the remote system by identifying the system name and versions of hardware, operating
system, and networking software supported in the device.
Port Description Describes the port in an alpha-numeric format. The port description is configurable.
System Indicates the primary function(s) of the device.
Capabilities
Supported
System Shows which of the supported system capabilities are enabled.
Capabilities
Enabled
Management For each interface on the remote device with an LLDP agent, lists the type of address the remote
Address LLDP agent uses and specifies the address used to obtain information related to the device.
Time To Live The amount of time (in seconds) the remote device's information received in the LLDPDU should be
treated as valid information.
Command example:
(NETGEAR switch) #show lldp remote-device detail 0/7
LLDP Remote Device Detail
Local Interface: 0/7
Remote Identifier: 2
Chassis ID Subtype: MAC Address
Chassis ID: 00:FC:E3:90:01:0F
Port ID Subtype: MAC Address
Port ID: 00:FC:E3:90:01:11
System Name:
System Description:
Port Description:
System Capabilities Supported:
System Capabilities Enabled:
Time to Live: 24 seconds
Switching Commands 616

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show lldp local-device
Use this command to display summary information about the advertised LLDP local data.
This command can display summary information or detail for each interface.
Format show lldp local-device {unit/slot/port | all}
Mode Privileged EXEC
Term Definition
Interface The interface in a unit/slot/port format.
Port ID The port ID associated with this interface.
Port Description The port description associated with the interface.
show lldp local-device detail
Use this command to display detailed information about the LLDP data a specific interface
transmits.
Format show lldp local-device detail unit/slot/port
Mode Privileged EXEC
Term Definition
Interface The interface that sends the LLDPDU.
Chassis ID The type of identification used in the Chassis ID field.
Subtype
Chassis ID The chassis of the local device.
Port ID Subtype The type of port on the local device.
Port ID The port number that transmitted the LLDPDU.
System Name The system name of the local device.
System Description Describes the local system by identifying the system name and versions of hardware, operating
system, and networking software supported in the device.
Port Description Describes the port in an alpha-numeric format.
System Indicates the primary function(s) of the device.
Capabilities
Supported
System Shows which of the supported system capabilities are enabled.
Capabilities
Enabled
Management The type of address and the specific address the local LLDP agent uses to send and receive
Address information.
Switching Commands 617

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
LLDP-MED Commands
Link Layer Discovery Protocol - Media Endpoint Discovery (LLDP-MED) (ANSI-TIA-1057)
provides an extension to the LLDP standard. Specifically, LLDP-MED provides extensions for
network configuration and policy, device location, Power over Ethernet (PoE) management
and inventory management.
lldp med
Use this command to enable MED on an interface or a range of interfaces. By enabling MED,
you will be effectively enabling the transmit and receive function of LLDP.
Default disabled
Format lldp med
Mode Interface Config
no lldp med
Use this command to disable MED.
Format no lldp med
Mode Interface Config
lldp med confignotification
Use this command to configure an interface or a range of interfaces to send the topology
change notification.
Default disabled
Format lldp med confignotification
Mode Interface Config
no ldp med confignotification
Use this command to disable notifications.
Format no lldp med confignotification
Mode Interface Config
Switching Commands 618

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
lldp med transmit-tlv
Use this command to specify which optional Type Length Values (TLVs) in the LLDP MED
set will be transmitted in the Link Layer Discovery Protocol Data Units (LLDPDUs) from this
interface or a range of interfaces.
Default By default, the capabilities and network policy TLVs are included.
Format lldp med transmit-tlv [capabilities] [ex-pd] [ex-pse] [inventory] [location]
[network-policy]
Mode Interface Config
Parameter Definition
capabilities Transmit the LLDP capabilities TLV.
ex-pd Transmit the LLDP extended PD TLV.
ex-pse Transmit the LLDP extended PSE TLV.
inventory Transmit the LLDP inventory TLV.
location Transmit the LLDP location TLV.
network-policy Transmit the LLDP network policy TLV.
no lldp med transmit-tlv
Use this command to remove a TLV.
Format no lldp med transmit-tlv [capabilities] [network-policy] [ex-pse] [ex-pd]
[location] [inventory]
Mode Interface Config
lldp med all
Use this command to configure LLDP-MED on all the ports.
Format lldp med all
Mode Global Config
lldp med confignotification all
Use this command to configure all the ports to send the topology change notification.
Format lldp med confignotification all
Mode Global Config
Switching Commands 619

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
lldp med faststartrepeatcount
Use this command to set the value of the fast start repeat count. count is the number of
LLDP PDUs that are transmitted when the product is enabled. The range is 1 to 10.
Default 3
Format lldp med faststartrepeatcount [count]
Mode Global Config
no lldp med faststartrepeatcount
Use this command to return to the factory default value.
Format no lldp med faststartrepeatcount
Mode Global Config
lldp med transmit-tlv all
Use this command to specify which optional Type Length Values (TLVs) in the LLDP MED
set will be transmitted in the Link Layer Discovery Protocol Data Units (LLDPDUs).
Default By default, the capabilities and network policy TLVs are included.
Format lldp med transmit-tlv all [capabilities] [ex-pd] [ex-pse] [inventory]
[location] [network-policy]
Mode Global Config
Term Definition
capabilities Transmit the LLDP capabilities TLV.
ex-pd Transmit the LLDP extended PD TLV.
ex-pse Transmit the LLDP extended PSE TLV.
inventory Transmit the LLDP inventory TLV.
location Transmit the LLDP location TLV.
network-policy Transmit the LLDP network policy TLV.
no lldp med transmit-tlv
Use this command to remove a TLV.
Format no lldp med transmit-tlv [capabilities] [network-policy] [ex-pse] [ex-pd]
[location] [inventory]
Mode Global Config
Switching Commands 620
