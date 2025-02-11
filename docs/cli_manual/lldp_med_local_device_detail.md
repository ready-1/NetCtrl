# lldp_med_local_device_detail

Pages: 622-623

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
TLV Codes: 0- Capabilities, 1- Network Policy
2- Location, 3- Extended PSE
4- Extended Pd, 5- Inventory
--More-- or (q)uit
(NETGEAR Switch) #show lldp med interface 1/0/2
Interface Link configMED operMED ConfigNotify TLVsTx
--------- ------ --------- -------- ------------ -----------
1/0/2 Up Disabled Disabled Disabled 0,1
TLV Codes: 0- Capabilities, 1- Network Policy
2- Location, 3- Extended PSE
4- Extended Pd, 5- Inventory
show lldp med local-device detail
Use this command to display detailed information about the LLDP MED data that a specific
interface transmits. unit/slot/port indicates a specific physical interface.
Format show lldp med local-device detail unit/slot/port
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show lldp med local-device detail 1/0/8
LLDP MED Local Device Detail
Interface: 1/0/8
Network Policies
Media Policy Application Type : voice
Vlan ID: 10
Priority: 5
DSCP: 1
Unknown: False
Tagged: True
Media Policy Application Type : streamingvideo
Vlan ID: 20
Priority: 1
DSCP: 2
Unknown: False
Tagged: True
Switching Commands 622

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Inventory
Hardware Rev: xxx xxx xxx
Firmware Rev: xxx xxx xxx
Software Rev: xxx xxx xxx
Serial Num: xxx xxx xxx
Mfg Name: xxx xxx xxx
Model Name: xxx xxx xxx
Asset ID: xxx xxx xxx
Location
Subtype: elin
Info: xxx xxx xxx
Extended POE
Device Type: pseDevice
Extended POE PSE
Available: 0.3 Watts
Source: primary
Priority: critical
Extended POE PD
Required: 0.2 Watts
Source: local
Priority: low
show lldp med remote-device
Use this command to display the summary information about remote devices that transmit
current LLDP MED data to the system. You can show information about LLDP MED remote
data received on all valid LLDP interfaces or on a specific physical interface.
Format show lldp med remote-device {unit/slot/port | all}
Mode Privileged EXEC
Term Definition
Local Interface The interface that received the LLDPDU from the remote device.
Remote ID An internal identifier to the switch to mark each remote device to the system.
Device Class Device classification of the remote device.
Switching Commands 623
