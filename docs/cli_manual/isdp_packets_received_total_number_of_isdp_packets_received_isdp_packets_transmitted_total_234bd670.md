# isdp_packets_received_total_number_of_isdp_packets_received_isdp_packets_transmitted_total_234bd670

Pages: 645-654

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
H oldtime 131
A dvertisement Version 2
E ntry last changed time 0 days 00:01:59
V ersion: 05.00.56
show isdp traffic
This command displays ISDP statistics.
Format show isdp traffic
Mode Privileged EXEC
Term Definition
ISDP Packets Received Total number of ISDP packets received
ISDP Packets Transmitted Total number of ISDP packets transmitted
ISDPv1 Packets Received Total number of ISDPv1 packets received
ISDPv1 Packets Transmitted Total number of ISDPv1 packets transmitted
ISDPv2 Packets Received Total number of ISDPv2 packets received
ISDPv2 Packets Transmitted Total number of ISDPv2 packets transmitted
ISDP Bad Header Number of packets received with a bad header
ISDP Checksum Error Number of packets received with a checksum error
ISDP Transmission Failure Number of packets which failed to transmit
ISDP Invalid Format Number of invalid packets received
ISDP Table Full Number of times a neighbor entry was not added to the table due to a full database
ISDP IP Address Table Full Displays the number of times a neighbor entry was added to the table without an IP
address.
Command example:
(NETGEAR Switch) #show isdp traffic
ISDP Packets Received.......................... 4253
ISDP Packets Transmitted....................... 127
ISDPv1 Packets Received........................ 0
ISDPv1 Packets Transmitted..................... 0
ISDPv2 Packets Received........................ 4253
ISDPv2 Packets Transmitted..................... 4351
ISDP Bad Header................................ 0
ISDP Checksum Error............................ 0
ISDP Transmission Failure...................... 0
ISDP Invalid Format............................ 0
Switching Commands 645

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ISDP Table Full................................ 392
ISDP IP Address Table Full..................... 737
debug isdp packet
This command enables tracing of ISDP packets processed by the switch. ISDP must be
enabled on both the device and the interface in order to monitor packets for a particular
interface.
Note: To display the debug trace, enable the debug console command.
Format debug isdp packet [receive | transmit]
Mode Privileged EXEC
no debug isdp packet
This command disables tracing of ISDP packets on the receive or the transmit sides or on
both sides.
Format no debug isdp packet [receive | transmit]
Mode Privileged EXEC
Interface Error Disabling and Auto Recovery
Commands
Interface error disabling automatically disables an interface when an error is detected. No
traffic is allowed until the interface is either manually reenabled or, if auto recovery is
configured, the configured auto recovery interval expires.
If an error condition is detected for an interface, the switch places the interface in an
error-disabled state (also referred to as a diagnostic-disabled state) by shutting down the
interface. The error-disabled interface does not allow any traffic until the interface is
reenabled. You can manually enable the error-disabled interface. Alternatively, you can
enable auto recovery, which automatically reenables the interface after the expiration of the
configured interval.
errdisable recovery cause
This command enables auto recovery for a specific cause or for all causes. If auto recovery is
enabled, interfaces in the error-disabled state are reenabled when the recovery interval
expires. If errors continue on the interface, the interface can be placed back in the
error-disabled state and disabled. You can manually reenable an interface in the
error-disabled state by entering the no shutdown command for the interface.
Switching Commands 646

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format errdisable recovery cause {all | arp-inspection | bpduguard | dhcp-rate-limit
| sfp-mismatch | udld | ucast-storm | bcast-storm | mcast-storm | bpdustorm |
mac-locking | denial-of-service | link-flap}
Mode Global Config
no errdisable recovery cause
Use this command to disable auto recovery for a specific cause or for all causes. When
disabled, interfaces that are in an error-disabled state do not recover automatically.
Format no errdisable recovery cause {all | arp-inspection | bpduguard |
dhcp-rate-limit | sfp-mismatch | udld | ucast-storm | bcast-storm |
mcast-storm | bpdustorm | mac-locking | denial-of-service | link-flap}
Mode Global Config
errdisable recovery interval
Use this command to configure the auto recovery period, which is used for all causes. The
period can be from 30 to 86400 seconds. When the recovery period expires, the switch
attempts to bring interfaces in the error-disabled state back into service.
Default 300 seconds
Format errdisable recovery interval period
Mode Global Config
no errdisable recovery interval
Use this command to reset the auto recovery period to the default period of 300 seconds.
Format no errdisable recovery interval
Mode Global Config
show errdisable recovery
Use this command to display whether auto recovery is enabled for the various features for
which it can be enabled.
Format show errdisable recovery
Mode Privileged EXEC
Switching Commands 647

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
dhcp-rate-limit Auto recovery is enabled or disabled for rate limiting of the DHCP Snooping feature.
arp-inspection Auto recovery is enabled or disabled for the ARP Inspection feature.
udld Auto recovery is enabled or disabled for the UDLD feature.
bpdguard Auto recovery is enabled or disabled for the BPDU Guard feature.
bpdustorm Auto recovery is enabled or disabled for BPDU storm conditions.
sfp-mismatch Auto recovery is enabled or disabled for SFP mismatch conditions.
time interval The period after which auto recovery occurs.
mac-locking Auto recovery is enabled or disabled for port MAC locking conditions.
denial-of-service Auto recovery is enabled or disabled for DoS conditions.
link-flap Auto recovery is enabled or disabled for the link-flap feature.
Command example:
(M4300-96X) #show errdisable recovery
Errdisable Reason Auto-recovery Status
------------------ ---------------------
dhcp-rate-limit Disabled
arp-inspection Disabled
udld Disabled
bcast-storm Disabled
mcast-storm Disabled
ucast-storm Disabled
bpduguard Disabled
bpdustorm Disabled
keepalive Disabled
mac-locking Disabled
denial-of-service Disabled
link-flap Disabled
Timeout for Auto-recovery from D-Disable state 300
show interfaces status err-disabled
Use this command to display the interfaces that are error-disabled, the reason they are
error-disabled, and the period remaining before auto recovery occurs.
Format show interfaces status err-disabled
Mode Privileged EXEC
Switching Commands 648

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
interface An interface that is error-disabled.
Errdisable Reason The reason the interface is error-disabled.
Auto-Recovery The period that is remaining before auto recovery occurs.
Time Left
Command example:
(NETGEAR Switch) #show interfaces status err-disabled
Interface Errdisable Reason Auto-Recovery Time Left(sec)
- --------- - ---------------- ------------------
0/1 udld 279
0/2 bpduguard 285
0/3 bpdustorm 291
0/4 keepalive 11
UniDirectional Link Detection Commands
The purpose of the UniDirectional Link Detection (UDLD) feature is to detect and avoid
unidirectional links. A unidirectional link is a forwarding anomaly in a Layer 2 communication
channel in which a bi-directional link stops passing traffic in one direction. Use the UDLD
commands to detect unidirectional links’ physical ports. UDLD must be enabled on both sides
of the link in order to detect a unidirectional link. The UDLD protocol operates by exchanging
packets containing information about neighboring devices.
udld enable (Global Config)
This command enables UDLD globally on the switch.
Default Disabled
Format udld enable
Mode Global Config
no udld enable (Global Config)
This command disables udld globally on the switch.
Format no udld enable
Mode Global Config
Switching Commands 649

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
udld message time
This command configures the interval between UDLD probe messages on ports that are in
the advertisement phase. The range is from 7 to 90 seconds.
Default 15 seconds
Format udld message time seconds
Mode Global Config
udld timeout interval
This command configures the time interval after which UDLD link is considered to be
unidirectional. The range is from 5 to 60 seconds.
Default 5 seconds
Format udld timeout interval seconds
Mode Global Config
udld reset
This command resets all interfaces that have been shutdown by UDLD.
Default None
Format udld reset
Mode Privileged EXEC
udld enable (Interface Config)
This command enables UDLD on the specified interface.
Default disable
Format udld enable
Mode Interface Config
no udld enable (Interface Config)
This command disables UDLD on the specified interface.
Format no udld enable
Mode Interface Config
Switching Commands 650

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
udld port
This command selects the UDLD mode operating on this interface. If the aggressive
keyword is not entered, the port operates in normal mode.
Default normal
Format udld port [aggressive]
Mode Interface Config
show udld
This command displays either the global settings of UDLD or the UDLD settings for the
specified unit/slot/port. If the all keyword is entered, the command displays information for
all ports.
Format show udld [unit/slot/port | all]
Mode User EXEC
Privileged EXEC
If you do not enter a value for the unit/slot/port parameter, the command output
displays the fields that are shown in the following table.
Parameter Description
Admin Mode The global administrative mode of UDLD.
Message Interval The time period (in seconds) between the transmission of UDLD probe packets.
Timeout Interval The time period (in seconds) before making a decision that the link is unidirectional.
If you enter a value for the unit/slot/port parameter or you use the all keyword, the
command output displays the fields that are shown in the following table.
Parameter Description
Port The identifying port of the interface.
Admin Mode The administrative mode of UDLD configured on this interface. This is either Enabled or Disabled.
UDLD Mode The UDLD mode configured on this interface. This is either Normal or Aggressive.
UDLD Status The status of the link as determined by UDLD. The options are:
• Undetermined. UDLD has not collected enough information to determine the state of the port.
• Not applicable. UDLD is disabled, either globally or on the port.
• Shutdown. UDLD has detected a unidirectional link and shutdown the port. That is, the port is
in an errDisabled state.
• Bidirectional. UDLD has detected a bidirectional link.
• Undetermined (Link Down). The port would transition into this state when the port link
physically goes down due to any reasons other than the port been put into D-Disable mode by
the UDLD protocol on the switch.
Switching Commands 651

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
The following output displays after you enable UDLD and configure nondefault interval
values:
(NETGEAR Switch) #show udld
Admin Mode..................................... Enabled
Message Interval............................... 13
Timeout Interval............................... 31
Command example:
(NETGEAR Switch) #show udld 0/1
Port Admin Mode UDLD Mode UDLD Status
----- ---------- ----------- --------------
0/1 Enabled Normal Not Applicable
Command example:
(NETGEAR Switch) #show udld all
Port Admin Mode UDLD Mode UDLD Status
----- ---------- ----------- --------------
0/1 Enabled Normal Shutdown
0/2 Enabled Normal Undetermined
0/3 Enabled Normal Bidirectional
0/4 Enabled Normal Not Applicable
0/5 Enabled Normal Not Applicable
0/6 Enabled Normal Not Applicable
0/7 Enabled Normal Not Applicable
0/8 Enabled Normal Shutdown
0/9 Enabled Normal Not Applicable
0/10 Enabled Normal Not Applicable
0/11 Enabled Normal Not Applicable
0/12 Enabled Normal Undetermined
0/13 Enabled Normal Bidirectional
0/14 Disabled Normal Not Applicable
0/15 Disabled Normal Not Applicable
0/16 Disabled Normal Not Applicable
0/17 Disabled Normal Not Applicable
0/18 Disabled Normal Not Applicable
0/19 Disabled Normal Not Applicable
0/20 Disabled Normal Not Applicable
Switching Commands 652

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Link Debounce Commands
Link debouncing functions on a per-port basis on physical interfaces. After you configure link
debouncing, if the switch receives a link-down notification, the switch starts monitoring the
link event by starting a timer with the configured debounce time. Any intermediate link-down
and link-up events are ignored hereafter. When the timer expires, link debounce checks if the
current state of the link is still down; if so, it forwards a link-down notification to the upper
layer applications.
You must explicitly enable link debounce per interface with an appropriate debounce timer
value, taking into consideration the network topology and the features enabled on the switch,
such as LAG or spanning tree.
Note: Link debouncing is disabled by default.
link debounce time
This command configures the debounce time. The possible values for the milliseconds
parameter are in the 100–5000 range.
Format link debounce time milliseconds
Mode Interface Config
no link debounce time
This command disables the debounce time.
Format no link debounce time
Mode Interface Config
show interface debounce
This command displays the flap counts for all interfaces.
Format show interface debounce
Mode Privileged EXEC
Switching Commands 653

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show interface debounce
Interface Debounce Time(ms) Flaps
--------- -------------- -------
1/0/1 0 0
1/0/2 0 0
1/0/3 0 0
1/0/4 0 0
1/0/5 0 0
1/0/6 0 0
Bonjour Commands
A Mac that supports Bonjour can discover the switch in the network so that you can find the
switch IP address and log in to the local browser user interface of the switch. Bonjour is
enabled by default on the switch. You can disable Bonjour for security reasons.
bonjour run
This command enables Bonjour on the switch.
Default Enabled
Format bonjour run
Mode Global Config
no bonjour run
This command disables Bonjour on the switch.
Format no bonjour run
Mode Global Config
show bonjour run
This command displays the Bonjour information and the published services.
Format show bonjour run
Mode Privileged EXEC
Switching Commands 654
