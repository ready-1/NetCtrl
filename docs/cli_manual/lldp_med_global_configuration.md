# lldp_med_global_configuration

Pages: 621-621

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show lldp med
Use this command to display a summary of the current LLDP MED configuration.
Format show lldp med
Mode Privileged Exec
Command example:
(NETGEAR Switch) #show lldp med
LLDP MED Global Configuration
Fast Start Repeat Count: 3
Device Class: Network Connectivity
(NETGEAR Switch) #
show lldp med interface
Use this command to display a summary of the current LLDP MED configuration for a
specific interface. unit/slot/port indicates a specific physical interface; all indicates all
valid LLDP interfaces.
Format show lldp med interface {unit/slot/port | all}
Mode Privileged Exec
Command example:
(NETGEAR Switch) #show lldp med interface all
Interface Link configMED operMED ConfigNotify TLVsTx
--------- ------ --------- -------- ------------ -----------
1/0/1 Down Disabled Disabled Disabled 0,1
1/0/2 Up Disabled Disabled Disabled 0,1
1/0/3 Down Disabled Disabled Disabled 0,1
1/0/4 Down Disabled Disabled Disabled 0,1
1/0/5 Down Disabled Disabled Disabled 0,1
1/0/6 Down Disabled Disabled Disabled 0,1
1/0/7 Down Disabled Disabled Disabled 0,1
1/0/8 Down Disabled Disabled Disabled 0,1
1/0/9 Down Disabled Disabled Disabled 0,1
1/0/10 Down Disabled Disabled Disabled 0,1
1/0/11 Down Disabled Disabled Disabled 0,1
1/0/12 Down Disabled Disabled Disabled 0,1
1/0/13 Down Disabled Disabled Disabled 0,1
1/0/14 Down Disabled Disabled Disabled 0,1
Switching Commands 621
