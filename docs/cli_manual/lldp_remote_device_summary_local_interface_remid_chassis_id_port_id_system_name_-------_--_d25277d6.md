# lldp_remote_device_summary_local_interface_remid_chassis_id_port_id_system_name_-------_--_d25277d6

Pages: 615-615

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Local Interface The interface that received the LLDPDU from the remote device.
RemID An internal identifier to the switch to mark each remote device to the system.
Chassis ID The ID that is sent by a remote device as part of the LLDP message, it is usually a MAC address of
the device.
Port ID The port number that transmitted the LLDPDU.
System Name The system name of the remote device.
Command example:
(NETGEAR switch) #show lldp remote-device all
LLDP Remote Device Summary
Local
Interface RemID Chassis ID Port ID System Name
------- ------- -------------------- ------------------ ------------------
0/1
0/2
0/3
0/4
0/5
0/6
0/7 2 00:FC:E3:90:01:0F 00:FC:E3:90:01:11
0/7 3 00:FC:E3:90:01:0F 00:FC:E3:90:01:12
0/7 4 00:FC:E3:90:01:0F 00:FC:E3:90:01:13
0/7 5 00:FC:E3:90:01:0F 00:FC:E3:90:01:14
0/7 1 00:FC:E3:90:01:0F 00:FC:E3:90:03:11
0/7 6 00:FC:E3:90:01:0F 00:FC:E3:90:04:11
0/8
0/9
0/10
0/11
0/12
show lldp remote-device detail
Use this command to display detailed information about remote devices that transmit current
LLDP data to an interface on the system.
Format show lldp remote-device detail unit/slot/port
Mode Privileged EXEC
Switching Commands 615
