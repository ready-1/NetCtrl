# eapol_logoff_frames_received_displays_the_number_of_eapol_log_off_frames_that_have_been_re_b1650479

Pages: 485-497

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
EAPOL Start Frames Transmitted Displays the number of EAPOL Start frames transmitted via the port.
EAPOL Logoff Frames Received Displays the number of EAPOL Log off frames that have been received on the
port.
EAP Resp/ID Frames Received Displays the number of EAP Respond ID frames that have been received on the
port.
EAP Response Frames Received Displays the number of valid EAP Respond frames received on the port.
EAP Req/ID Frames Transmitted Displays the number of EAP Requested ID frames transmitted via the port.
EAP Req Frames Transmitted Displays the number of EAP Request frames transmitted via the port.
Invalid EAPOL Frames Received Displays the number of unrecognized EAPOL frames received on this port.
EAP Length Error Frames Received Displays the number of EAPOL frames with an invalid Packet Body Length
received on this port.
Last EAPOL Frames Version Displays the protocol version number attached to the most recently received
EAPOL frame.
Last EAPOL Frames Source Displays the source MAC Address attached to the most recently received
EAPOL frame.
Command example:
(NETGEAR Switch) #show dot1x statistics 0/1
Port........................................... 0/1
EAPOL Frames Received.......................... 0
EAPOL Frames Transmitted....................... 0
EAPOL Start Frames Transmitted................. 3
EAPOL Logoff Frames Received................... 0
EAP Resp/Id frames transmitted................. 0
EAP Response frames transmitted................ 0
EAP Req/Id frames transmitted.................. 0
EAP Req frames transmitted..................... 0
Invalid EAPOL frames received.................. 0
EAP length error frames received............... 0
Last EAPOL Frame Version....................... 0
Last EAPOL Frame Source........................ 00:00:00:00:02:01
Switching Commands 485

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Storm-Control Commands
This section describes commands you use to configure storm-control and view storm-control
configuration information. A traffic storm is a condition that occurs when incoming packets
flood the LAN, which creates performance degradation in the network. The Storm-Control
feature protects against this condition.
The switch provides broadcast, multicast, and unicast story recovery for individual interfaces.
Unicast Storm-Control protects against traffic whose MAC addresses are not known by the
system. For broadcast, multicast, and unicast storm-control, if the rate of traffic ingressing on
an interface increases beyond the configured threshold for that type, the traffic is dropped.
To configure storm-control, you will enable the feature for all interfaces or for individual
interfaces, and you will set the threshold (storm-control level) beyond which the broadcast,
multicast, or unicast traffic will be dropped. The Storm-Control feature allows you to limit the
rate of specific types of packets through the switch on a per-port, per-type, basis.
Configuring a storm-control level also enables that form of storm-control. Disabling a
storm-control level (using the no version of the command) sets the storm-control level back to
the default value and disables that form of storm-control. Using the no version of a
storm-control command (not stating a level) disables that form of storm-control but maintains
the configured level (to be active the next time that form of storm-control is enabled.)
Note: The actual rate of ingress traffic required to activate storm-control is
based on the size of incoming packets and the hard-coded average
packet size of 512 bytes - used to calculate a packet-per-second (pps)
rate - as the forwarding-plane requires pps versus an absolute rate
kbps. For example, if the configured limit is 10 percent, this is
converted to ~25000 pps, and this pps limit is set in forwarding plane
(hardware). You get the approximate desired output when 512bytes
packets are used.
storm-control broadcast
Use this command to enable broadcast storm recovery mode for all interfaces (Global Config
mode) or one or more interfaces (Interface Config mode). If the mode is enabled, broadcast
storm recovery is active and, if the rate of L2 broadcast traffic ingressing on an interface
increases beyond the configured threshold, the traffic will be dropped. Therefore, the rate of
broadcast traffic will be limited to the configured threshold.
Default Enabled
Format storm-control broadcast
Mode Global Config
Interface Config
Switching Commands 486

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no storm-control broadcast
Use this command to disable broadcast storm recovery mode for all interfaces (Global Config
mode) or one or more interfaces (Interface Config mode).
Format no storm-control broadcast
Mode Global Config
Interface Config
storm-control broadcast action
This command configures the broadcast storm recovery action to either shut down or send
traps for one, several, or all interfaces. If you enter the command in Global Config mode, the
action applies to all interfaces. If you enter the command in Interface Config mode, the action
applies to or one or more interfaces.
If you specify the shutdown keyword, the interface that receives the broadcast packets at a
rate above the threshold is diagnostically disabled. If you specify the trap keyword, the
interface sends trap messages approximately every 30 seconds until broadcast storm control
recovers.
Format storm-control broadcast action {shutdown | trap}
Mode Global Config
Interface Config
no storm-control broadcast action
This command sets the broadcast storm recovery action to the default value for one, several,
or all interfaces. If you enter the command in Global Config mode, the action applies to all
interfaces. If you enter the command in Interface Config mode, the action applies to or one or
more interfaces.
Format no storm-control broadcast action
Mode Global Config
Interface Config
storm-control broadcast level
Use this command to configure the broadcast storm recovery threshold for all interfaces
(Global Config mode) or one or more interfaces (Interface Config mode) as a percentage of
link speed and enable broadcast storm recovery. If the mode is enabled, broadcast storm
recovery is active, and if the rate of L2 broadcast traffic ingressing on an interface increases
beyond the configured threshold, the traffic is dropped. Therefore, the rate of broadcast traffic
is limited to the configured threshold. The threshold level can be in the range from 0–100.
The default is 5.
Switching Commands 487

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default 5
Format storm-control broadcast level threshold
Mode Global Config
Interface Config
no storm-control broadcast level
This command sets the broadcast storm recovery threshold to the default value for all
interfaces (Global Config mode) or one or more interfaces (Interface Config mode) and
disables broadcast storm recovery.
Format no storm-control broadcast level
Mode Global Config
Interface Config
storm-control broadcast rate
Use this command to configure the broadcast storm recovery threshold for all interfaces
(Global Config mode) or one or more interfaces (Interface Config mode) in packets per
second. If the mode is enabled, broadcast storm recovery is active, and if the rate of L2
broadcast traffic ingressing on an interface increases beyond the configured threshold, the
traffic is dropped. Therefore, the rate of broadcast traffic is limited to the configured threshold.
The threshold rate can be in the range from 0–14880000. The default is 0.
Default 0
Format storm-control broadcast rate threshold
Mode Global Config
Interface Config
no storm-control broadcast rate
This command sets the broadcast storm recovery threshold to the default value for all
interfaces (Global Config mode) or one or more interfaces (Interface Config mode) and
disables broadcast storm recovery.
Format no storm-control broadcast rate
Mode Global Config
Interface Config
storm-control multicast
This command enables multicast storm recovery mode for all interfaces (Global Config
mode) or one or more interfaces (Interface Config mode). If the mode is enabled, multicast
Switching Commands 488

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
storm recovery is active, and if the rate of L2 multicast traffic ingressing on an interface
increases beyond the configured threshold, the traffic will be dropped. Therefore, the rate of
multicast traffic will be limited to the configured threshold.
Default Disabled
Format storm-control multicast
Mode Global Config
Interface Config
no storm-control multicast
This command disables multicast storm recovery mode for all interfaces (Global Config
mode) or one or more interfaces (Interface Config mode).
Format no storm-control multicast
Mode Global Config
Interface Config
storm-control multicast action
This command configures the multicast storm recovery action to either shut down or send
traps for one, several, or all interfaces. If you enter the command in Global Config mode, the
action applies to all interfaces. If you enter the command in Interface Config mode, the action
applies to or one or more interfaces.
If you specify the shutdown keyword, the interface that receives the multicast packets at a
rate above the threshold is diagnostically disabled. If you specify the trap keyword, the
interface sends trap messages approximately every 30 seconds until multicast storm control
recovers.
Format storm-control multicast action {shutdown | trap}
Mode Global Config
Interface Config
no storm-control multicast action
This command sets the multicast storm recovery action to the default value for one, several,
or all interfaces. If you enter the command in Global Config mode, the action applies to all
interfaces. If you enter the command in Interface Config mode, the action applies to or one or
more interfaces.
Format no storm-control multicast action
Mode Global Config
Interface Config
Switching Commands 489

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
storm-control multicast level
This command configures the multicast storm recovery threshold for all interfaces (Global
Config mode) or one or more interfaces (Interface Config mode) as a percentage of link
speed and enables multicast storm recovery mode. If the mode is enabled, multicast storm
recovery is active, and if the rate of L2 multicast traffic ingressing on an interface increases
beyond the configured threshold, the traffic will be dropped. Therefore, the rate of multicast
traffic will be limited to the configured threshold. The threshold level can be in the range from
0–100. The default is 5.
Default 5
Format storm-control multicast level 0-100
Mode Global Config
Interface Config
no storm-control multicast level
This command sets the multicast storm recovery threshold to the default value for all
interfaces (Global Config mode) or one or more interfaces (Interface Config mode) and
disables multicast storm recovery.
Format no storm-control multicast level
Mode Global Config
Interface Config
storm-control multicast rate
Use this command to configure the multicast storm recovery threshold for all interfaces
(Global Config mode) or one or more interfaces (Interface Config mode) in packets per
second. If the mode is enabled, multicast storm recovery is active, and if the rate of L2
broadcast traffic ingressing on an interface increases beyond the configured threshold, the
traffic is dropped. Therefore, the rate of multicast traffic is limited to the configured threshold.
The threshold rate can be in the range from 0–14880000. The default is 0.
Default 0
Format storm-control multicast rate threshold
Mode Global Config
Interface Config
Switching Commands 490

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no storm-control multicast rate
This command sets the multicast storm recovery threshold to the default value for all
interfaces (Global Config mode) or one or more interfaces (Interface Config mode) and
disables multicast storm recovery.
Format no storm-control multicast rate
Mode Global Config
Interface Config
storm-control unicast
This command enables unicast storm recovery mode for all interfaces (Global Config mode)
or one or more interfaces (Interface Config mode). If the mode is enabled, unicast storm
recovery is active, and if the rate of unknown L2 unicast (destination lookup failure) traffic
ingressing on an interface increases beyond the configured threshold, the traffic will be
dropped. Therefore, the rate of unknown unicast traffic will be limited to the configured
threshold.
Default Disabled
Format storm-control unicast
Mode Global Config
Interface Config
no storm-control unicast
This command disables unicast storm recovery mode for all interfaces (Global Config mode)
or one or more interfaces (Interface Config mode).
Format no storm-control unicast
Mode Global Config
Interface Config
storm-control unicast action
This command configures the unicast storm recovery action to either shut down or send traps
for one, several, or all interfaces. If you enter the command in Global Config mode, the action
applies to all interfaces. If you enter the command in Interface Config mode, the action
applies to or one or more interfaces.
If you specify the shutdown keyword, the interface that receives the unicast packets at a
rate above the threshold is diagnostically disabled. If you specify the trap keyword, the
interface sends trap messages approximately every 30 seconds until unicast storm control
recovers.
Switching Commands 491

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format storm-control unicast action {shutdown | trap}
Mode Global Config
Interface Config
no storm-control unicast action
This command sets the unicast storm recovery action to the default value for one, several, or
all interfaces. If you enter the command in Global Config mode, the action applies to all
interfaces. If you enter the command in Interface Config mode, the action applies to or one or
more interfaces.
Format no storm-control unicast action
Mode Global Config
Interface Config
storm-control unicast level
This command configures the unicast storm recovery threshold for all interfaces (Global
Config mode) or one or more interfaces (Interface Config mode) as a percentage of link
speed, and enables unicast storm recovery. If the mode is enabled, unicast storm recovery is
active, and if the rate of unknown L2 unicast (destination lookup failure) traffic ingressing on
an interface increases beyond the configured threshold, the traffic will be dropped. Therefore,
the rate of unknown unicast traffic will be limited to the configured threshold. This command
also enables unicast storm recovery mode for an interface. The threshold level can be in the
range from 0–100. The default is 5.
Default 5
Format storm-control unicast level threshold
Mode Global Config
Interface Config
no storm-control unicast level
This command sets the unicast storm recovery threshold to the default value for all interfaces
(Global Config mode) or one or more interfaces (Interface Config mode) and disables unicast
storm recovery.
Format no storm-control unicast level
Mode Global Config
Interface Config
Switching Commands 492

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
storm-control unicast rate
Use this command to configure the unicast storm recovery threshold for all interfaces (Global
Config mode) or one or more interfaces (Interface Config mode) in packets per second. If the
mode is enabled, unicast storm recovery is active, and if the rate of L2 broadcast traffic
ingressing on an interface increases beyond the configured threshold, the traffic is dropped.
Therefore, the rate of unicast traffic is limited to the configured threshold. The threshold rate
can be in the range from 0–14880000. The default is 0.
Default 0
Format storm-control unicast rate threshold
Mode Global Config
Interface Config
no storm-control unicast rate
This command sets the unicast storm recovery threshold to the default value for all interfaces
(Global Config mode) or one or more interfaces (Interface Config mode) and disables unicast
storm recovery.
Format no storm-control unicast rate
Mode Global Config
Interface Config
show storm-control
This command displays switch configuration information. If you do not use any of the optional
parameters, this command displays global storm control configuration parameters:
• Broadcast Storm Recovery Mode may be enabled or disabled. The factory default is
disabled.
• 802.3x Flow Control Mode may be enabled or disabled. The factory default is disabled.
Use the all keyword to display the per-port configuration parameters for all interfaces, or
specify the unit/slot/port to display information about a specific interface.
Format show storm-control [all | unit/slot/port]
Mode Privileged EXEC
Parameter Definition
Bcast Mode Shows whether the broadcast storm control mode is enabled or disabled. The factory default is
disabled.
Bcast Level The broadcast storm control level.
Bcast Action The broadcast storm recovery acton.
Switching Commands 493

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Definition
Mcast Mode Shows whether the multicast storm control mode is enabled or disabled.
Mcast Level The multicast storm control level.
Mcast Action The multicast storm recovery acton.
Ucast Mode Shows whether the Unknown Unicast or DLF (Destination Lookup Failure) storm control mode is
enabled or disabled.
Ucast Level The Unknown Unicast or DLF (Destination Lookup Failure) storm control level.
Ucast Action The unicast storm recovery acton.
Command example:
(NETGEAR Switch) #show storm-control
Broadcast Storm Control Mode................... Enable
Broadcast Storm Control Level.................. 5 percent
Broadcast Storm Control Action................. None
Multicast Storm Control Mode................... Disable
Multicast Storm Control Level.................. 5 percent
Multicast Storm Control Action................. None
Unicast Storm Control Mode..................... Disable
Unicast Storm Control Level.................... 5 percent
Unicast Storm Control Action................... None
Command example:
(NETGEAR Switch) #show storm-control 1/0/1
B cast B cast B cast M cast M cast M cast U cast U cast U cast F low Mode
I ntf M ode L evel A ction M ode L evel A ction M ode L evel Action
- ---- - ----- - ---- - ----- - ------ - ---- - ----- - ------ - ---- - ----- -------
1 /0/1 E nable 5 % N one D isable 5 % N one D isable 5 % N one Disable
Command example:
(NETGEAR Switch) #show storm-control all
B cast B cast B cast M cast M cast M cast U cast U cast U cast F low Mode
I ntf M ode L evel A ction M ode L evel A ction M ode L evel Action
- ---- - ----- - ---- - ----- - ------ - ---- - ----- - ------ - ---- - ----- -------
1 /0/1 E nable 5 % N one D isable 5 % N one D isable 5 % N one Disable
1 /0/2 E nable 5 % N one D isable 5 % N one D isable 5 % N one Disable
1 /0/3 E nable 5 % N one D isable 5 % N one D isable 5 % N one Disable
1 /0/4 E nable 5 % N one D isable 5 % N one D isable 5 % N one Disable
1 /0/5 E nable 5 % N one D isable 5 % N one D isable 5 % N one Disable
Switching Commands 494

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Link Dependency Commands
Link dependency allows the link status of specified ports to be dependent on the link status of
one port or many ports. Consequently, if a port on which other ports depend loses a link, the
dependent ports either become administratively disabled and are brought down or become
administratively enabled and are brought up.
link state group
Use this command to indicate if the downstream interfaces of a specified group must mirror
or invert the status of the upstream interfaces. The default configuration for a group is down.
That is, the downstream interfaces mirror the upstream link status by going down when all
upstream interfaces are down. Specifying the up keyword allows the downstream interfaces
to come up when all upstream interfaces are down.
Default down
Format link state group group-id action {up | down}
Mode Global Config
link state group downstream
Use this command to add a group of interfaces to the downstream interface list. Adding an
interface to a downstream list brings the interface down until an upstream interface is added
to the group. The link status then follows the interface that is specified in the link state
group upstream command. To prevent interfaces from being brought down, enter the
link state group upstream command before you enter the link state group
downstream command.
Format link state group group-id downstream
Mode Interface Config
no link state group downstream
Use this command to remove a group of interfaces from the downstream list.
Format no link state group group-id downstream
Mode Interface Config
Switching Commands 495

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
link state group upstream
Use this command to add a group of interfaces to the upstream interface list.
An interface that is defined as an upstream interface cannot also be defined as a downstream
interface in the same link state group or as a downstream interface in a different link state
group if either configuration creates a circular dependency between groups.
Format link state group group-id upstream
Mode Interface Config
no link state group upstream
Use this command to remove a group of interfaces from the upstream list.
Format no link state group group-id upstream
Mode Interface Config
show link state group
Use this command to display information about all configured link-dependency groups or a
specific link-dependency group.
Format show link state group [group-id]
Mode Privileged EXEC
Command example:
This example displays information about all configured link-dependency groups.
(Switching) #show link-state group
G roupId D ownstream Interfaces U pstream Interfaces L ink Action Group State
- ------ - ------------------------- - ------------------- - ---------- -----------
1 2 /0/3-2/0/7,2/0/12-2/0/17 2 /0/12-2/0/32,0/3/5 L ink Up Up
4 2 /0/18,2/0/27 2 /0/22-2/0/33,0/3/1 L ink Up Down
Command example:
This example displays information about a specific link-dependency group.
(Switching) #show link state group 1
G roupId D ownstream Interfaces U pstream Interfaces L ink Action Group State
- ------ - ------------------------- - ------------------- - ---------- -----------
1 2 /0/3-2/0/7,2/0/12-2/0/17 2 /0/12-2/0/32,0/3/5 L ink Up Up
Switching Commands 496

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show link state group detail
Use this command to display detailed information about the state of upstream and
downstream interfaces for a selected link-dependency group. The Group Transitions field
shows a count of the number of times that the downstream interface went into its action state
as a result of the upstream interfaces link state.
Format show link state group group-id detail
Mode Privileged EXEC
Command example:
(Switching) #show link state group 1 detail
GroupId: 1
Link Action: Up
Group State: Up
Downstream Interface State:
Link Up: 2/0/3
Link Down: 2/0/4-2/0/7,2/0/12-2/0/17
Upstream Interface State:
Link Up: -
Link Down: 2/0/12-2/0/32,0/3/5
Group Transitions: 0
Last Transition Time: 00:52:35 (UTC+0:00) Nov 3 2015
Link Local Protocol Filtering Commands
Link Local Protocol Filtering (LLPF) allows the switch to filter out multiple proprietary protocol
PDUs, such as Port Aggregation Protocol (PAgP), if the problems occur with proprietary
protocols running on standards-based switches. If certain protocol PDUs cause unexpected
results, LLPF can be enabled to prevent those protocol PDUs from being processed by the
switch.
llpf
Use this command to block LLPF protocol(s) on a port.
Default disable
Format llpf {blockisdp | blockvtp | blockdtp | blockudld | blockpagp | blocksstp |
blockall}
Mode Interface Config
Switching Commands 497
