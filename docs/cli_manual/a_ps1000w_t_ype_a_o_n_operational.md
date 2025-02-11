# a_ps1000w_t_ype_a_o_n_operational

Pages: 1105-1107

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Use this command to display the information for a redundant power supply (RPS) that is
attached to the switch.
Format show power rps [unit-id]
Mode Privileged EXEC
User EXEC
Command example:
(NETGEAR Switch) #show power rps
Unit 1:
Model Name:……………………………………………..M4300-52G-POE+
RPS Name:……………………………………………..RPS4000v2
Total Available Power(W): ......................……………1440W
Power Module AC Input(V): ...................................... 220
Total RPS Interface Number ............................ 2
R PS Port Power Module Name Type CS Status
- ----------- - --------------- - ------- -------- --------------
1 A PS1000W T ype A O n Operational
2 A PS1000W T ype B O n Not present
Power over Ethernet Commands 1105

Switch Software Log Messages

This chapter lists common log messages that are provided by the switch, along with information
regarding the cause of each message. There is no specific action that can be taken per
message. When there is a problem being diagnosed, a set of these messages in the event log,
along with an understanding of the system configuration and details of the problem can assist
NETGEAR in determining the root cause of such a problem. The most recent log messages are
displayed first.
Note: This chapter is not a complete list of all syslog messages.
The chapter includes the following sections:
• Core
• Utilities
• Management
• Switching
• QoS
• Routing/IPv6 Routing
• Multicast
• Stacking
• Technologies
• O/S Support

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Core
T able 16. BSP Log Messages
Component Message Cause
BSP Event(0xaaaaaaaa) Switch has restarted.
BSP Starting code... BSP initialization complete, starting the switch.
T able 17. NIM Log Messages
Component Message Cause
NIM NIM: L7_ATTACH out of order for interface unit x Interface creation out of order.
slot x port x
NIM NIM: Failed to find interface at unit x slot x port x There is no mapping between the USP and
for event(x) Interface number.
NIM NIM: L7_DETACH out of order for interface unit x Interface creation out of order.
slot x port x
NIM NIM: L7_DELETE out of order for interface unit x Interface creation out of order.
slot x port x
NIM NIM: event(x),intf(x),component(x), in wrong An event was issued to NIM during the wrong
phase configuration phase (probably Phase 1, 2, or
WMU).
NIM NIM: Failed to notify users of interface change Event was not propagated to the system.
NIM NIM: failed to send message to NIM message NIM message queue full or non-existent.
Queue.
NIM NIM: Failed to notify the components of Interface not created.
L7_CREATE event
NIM NIM: Attempted event (x), on USP x.x.x before A component issued an interface event during
phase 3 the wrong initialization phase.
NIM NIM: incorrect phase for operation An API call was made during the wrong
initialization phase.
NIM NIM: Component(x) failed on event(x) for A component responded with a fail indication for
interface an interface event.
NIM NIM: Timeout event(x), interface remainingMask A component did not respond before the NIM
= xxxx timeout occurred.
Switch Software Log Messages 1107
