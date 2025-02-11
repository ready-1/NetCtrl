# mmrp_messages_received_with_total_number_of_mmrp_frames_with_bad_headers_received_bad_head_0b7276e8

Pages: 502-502

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
0/6 Disabled
0/7 Disabled
0/8 Disabled
0/9 Disabled
0/10 Disabled
0/11 Disabled
0/12 Disabled
0/13 Disabled
0/14 Disabled
0/15 Disabled
0/16 Disabled
0/17 Disabled
show mmrp statistics
Use this command in Privileged EXEC mode to display statistical information about the
MMRP PDUs sent and received on the interface.
Format show mmrp statistics {summary | [unit/slot/port | all]}
Mode Privileged EXEC
The following statistics display when the summary keyword or unit/slot/port parameter
is used. Using the summary keyword displays global statistics. The unit/slot/port
parameter displays per-interface statistics.
Parameter Description
MMRP messages received Total number of MMRP messages received.
MMRP messages received with Total number of MMRP frames with bad headers received
bad header
MMRP messages received with Total number of MMRP frames with bad PDUs body formats received
bad format
MMRP messages transmitted Total number of MMRP frames that sent
MMRP messages failed to Total number of MMRP frames that failed to be transmitted
transmit
The following statistics display when the all keyword is used.
Parameter Description
Intf The interface associated with the rest of the data in the row.
Rx Total number of MMRP messages received.
Bad Header Total number of MMRP frames with bad headers received
Switching Commands 502
