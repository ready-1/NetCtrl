# vlan_tagging_is_a_way_to_pass_vlan_traffic_from_one_customer_domain_to_another_through_a

Pages: 439-454

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show interfaces switchport general
I ntf P VID I ngress A cceptable U ntagged T agged Forbidden Dynamic
F iltering F rame Type V lans V lans V lans Vlans
--------- ----- ---------- ----------- --------- --------- --------- ---------
1 /0/1 1 E nabled A dmit All 1 ,4-7 3 0-40,55 3 ,100-200 88,96
1 /0/2 1 D isabled A dmit All 1 3 0-40,55 n one none
Double VLAN Commands
This section describes the commands you use to configure double VLAN (DVLAN). Double
VLAN tagging is a way to pass VLAN traffic from one customer domain to another through a
Metro Core in a simple and cost effective manner. The additional tag on the traffic helps
differentiate between customers in the MAN while preserving the VLAN identification of the
individual customers when they enter their own IEEE 802.1Q domain.
dvlan-tunnel ethertype (Interface Config)
This command configures the ethertype for the specified interface. The two-byte hex
ethertype is used as the first 16 bits of the DVLAN tag. The ethertype can have the values of
802.1Q, vman, or custom. If the ethertype has an optional value of custom, then it is a
custom tunnel value, and ethertype must be set to a value in the range of 1 to 65535.
Default vman
Format dvlan-tunnel ethertype {802.1Q | vman | custom value}
Mode Global Config
Parameter Description
802.1Q Configure the ethertype as 0x8100.
custom Configure the value of the custom tag in the range from 1 to 65535.
vman Represents the commonly used value of 0x88A8.
no dvlan-tunnel ethertype (Interface Config)
This command removes the ethertype value for the interface.
Format no dvlan-tunnel ethertype
Mode Global Config
Switching Commands 439

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
dvlan-tunnel ethertype primary-tpid
Use this command to create a new TPID and associate it with the next available TPID
register. If no TPID registers are empty, the system returns an error. Specifying the optional
keyword primary–tpid forces the TPID value to be configured as the default TPID at index
0. The ethertype can have the values of 802.1Q, vman, or custom. If the ethertype has an
optional value of custom, then it is a custom tunnel value, and ethertype must be set to a
value in the range of 1 to 65535.
Format dvlan-tunnel ethertype {802.1Q | vman | custom value} [primary-tpid]
Mode Global Config
Parameter Description
802.1Q Configure the ethertype as 0x8100.
custom value Configure the value of the custom tag in the range from 1 to 65535.
vman Represents the commonly used value of 0x88A8.
primary-tpid [Optional] Forces the TPID value to be configured as the default TPID at index 0.
no dvlan-tunnel ethertype primary–tpid
Use the no form of the command to reset the TPID register to 0. (At initialization, all TPID
registers will be set to their default values.)
Format no dvlan-tunnel ethertype {802.1Q | vman | custom 1–65535} [primary-tpid]
Mode Global Config
mode dot1q-tunnel
This command is used to enable Double VLAN Tunneling on the specified interface.
Default Disabled
Format mode dot1q-tunnel
Mode Interface Config
no mode dot1q-tunnel
This command is used to disable Double VLAN Tunneling on the specified interface. By
default, Double VLAN Tunneling is disabled.
Format no mode dot1q-tunnel
Mode Interface Config
Switching Commands 440

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
mode dvlan-tunnel
Use this command to enable Double VLAN Tunneling on the specified interface.
Note: When you use the mode dvlan-tunnel command on an interface, it
becomes a service provider port. Ports that do not have double VLAN
tunneling enabled are customer ports.
Default Disabled
Format mode dvlan-tunnel
Mode Interface Config
no mode dvlan-tunnel
This command is used to disable Double VLAN Tunneling on the specified interface. By
default, Double VLAN Tunneling is disabled.
Format no mode dvlan-tunnel
Mode Interface Config
show dot1q-tunnel
Use this command without the optional parameters to display all interfaces enabled for
Double VLAN Tunneling. Use the optional parameters to display detailed information about
Double VLAN Tunneling for the specified interface or all interfaces.
Format show dot1q-tunnel [interface {unit/slot/port | all}]
Mode Privileged EXEC
User EXEC
Term Definition
Interface The interface.
Mode The administrative mode through which Double VLAN Tunneling can be enabled or disabled. The
default value for this field is disabled.
EtherType A 2-byte hex EtherType to be used as the first 16 bits of the DVLAN tunnel. There are three different
EtherType tags. The first is 802.1Q, which represents the commonly used value of 0x8100. The
second is vMAN, which represents the commonly used value of 0x88A8. If EtherType is not one of
these two values, then it is a custom tunnel value, representing any value in the range of 1 to 65535.
Switching Commands 441

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show dvlan-tunnel
Use this command without the optional parameters to display all interfaces enabled for
Double VLAN Tunneling. Use the optional parameters to display detailed information about
Double VLAN Tunneling for the specified interface or all interfaces.
Format show dvlan-tunnel [interface {unit/slot/port | all | lag lag-intf-num}]
Mode Privileged EXEC
User EXEC
Term Definition
Interface The interface.
LAG Instead of unit/slot/port, lag lag-intf-num can be used as an alternate way to specify the
LAG interface, in which lag-intf-num is the LAG port number.
Mode The administrative mode through which Double VLAN Tunneling can be enabled or disabled. The
default value for this field is disabled.
EtherType A 2-byte hex EtherType to be used as the first 16 bits of the DVLAN tunnel. There are three different
EtherType tags. The first is 802.1Q, which represents the commonly used value of 0x8100. The
second is vMAN, which represents the commonly used value of 0x88A8. If EtherType is not one of
these two values, then it is a custom tunnel value, representing any value in the range of 1 to 65535.
Command example:
(NETGEAR Switch) #show dvlan-tunnel
TPIDs Configured............................... 0x88a8
Default TPID................................... 0x88a8
Interfaces Enabled for DVLAN Tunneling......... None
(NETGEAR Switch) #
(NETGEAR Switch) #show dvlan-tunnel interface 1/0/1
Interface Mode EtherType
--------- ------- ------------
1/0/1 Disable 0x88a8
Switching Commands 442

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Private VLAN Commands
This section describes the commands you use for private VLANs. Private VLANs provides
Layer 2 isolation between ports that share the same broadcast domain. In other words, it
allows a VLAN broadcast domain to be partitioned into smaller point-to-multipoint
subdomains. The ports participating in a private VLAN can be located anywhere in the
Layer 2 network.
switchport private-vlan
This command defines a private-VLAN association for an isolated or community port or a
mapping for a promiscuous port.
Format switchport private-vlan {host-association primary-vlan-id secondary-vlan-id
| mapping primary-vlan-id {add | remove} secondary-vlan-list}
Mode Interface Config
Parameter Description
host-association Defines the VLAN association for community or host ports.
mapping Defines the private VLAN mapping for promiscuous ports.
primary-vlan-id Primary VLAN ID of a private VLAN.
secondary-vlan-id Secondary (isolated or community) VLAN ID of a private VLAN.
add Associates the secondary VLAN with the primary one.
remove Deletes the secondary VLANs from the primary VLAN association.
secondary-vlan-list A list of secondary VLANs to be mapped to a primary VLAN.
no switchport private-vlan
This command removes the private-VLAN association or mapping from the port.
Format no switchport private-vlan {host-association | mapping}
Mode Interface Config
switchport mode private-vlan
This command configures a port as a promiscuous or host private VLAN port. Note that the
properties of each mode can be configured even when the switch is not in that mode.
However, they will only be applicable once the switch is in that particular mode.
Format switchport mode private-vlan {host | promiscuous}
Mode Interface Config
Switching Commands 443

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
host Configures an interface as a private VLAN host port. It can be either isolated or community port
depending on the secondary VLAN it is associated with.
promiscuous Configures an interface as a private VLAN promiscuous port. The promiscuous ports are members
of the primary VLAN.
no switchport mode private-vlan
This command removes the private-VLAN association or mapping from the port.
Format no switchport mode private-vlan
Mode Interface Config
private-vlan
This command configures the private VLANs and configures the association between the
primary private VLAN and secondary VLANs.
Format private-vlan {association [add | remove] secondary-vlan-list | community |
isolated | primary}
Mode VLAN Config
Parameter Description
association Associates the primary and secondary VLAN.
secondary-vlan-list A list of secondary VLANs to be mapped to a primary VLAN.
community Designates a VLAN as a community VLAN.
isolated Designates a VLAN as the isolated VLAN.
primary Designates a VLAN as the primary VLAN.
no private-vlan
This command restores normal VLAN configuration.
Format no private-vlan [association]
Mode VLAN Config
Switching Commands 444

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Voice VLAN Commands
This section describes the commands you use for Voice VLAN. Voice VLAN enables switch
ports to carry voice traffic with defined priority so as to enable separation of voice and data
traffic coming onto the port. The benefits of using Voice VLAN is to ensure that the sound
quality of an IP phone could be safeguarded from deteriorating when the data traffic on the
port is high.
Also the inherent isolation provided by VLANs ensures that inter-VLAN traffic is under
management control and that network- attached clients cannot initiate a direct attack on
voice components. QoS-based on IEEE 802.1P class of service (CoS) uses classification
and scheduling to sent network traffic from the switch in a predictable manner. The system
uses the source MAC of the traffic traveling through the port to identify the IP phone data
flow.
The switch can be configured to support voice VLAN on a port connecting to the VoIP phone.
When a VLAN is associated with the voice VLAN port, then the VLAN id info is passed onto
the VoIP phone using the LLDP-MED mechanism. The voice data coming from the VoIP
phone is tagged with the exchanged VLAN ID; thus, regular data arriving on the switch is
given the default PVID of the port, and the voice traffic is received on a predefined VLAN.
The two types of traffic are therefore segregated so that better service can be provided to the
voice traffic.
When a dot1p priority is associated with the voice VLAN port instead of VLAN ID, the priority
information is passed onto the VoIP phone using the LLDP-MED mechanism. Thus, the voice
data coming from the VoIP phone is tagged with VLAN 0 and with the exchanged priority.
Regular data arriving on the switch is given the default priority of the port (default 0), and the
voice traffic is received with higher priority, thus segregating both the traffic to provide better
service to the voice traffic.
The switch can be configured to override the data traffic CoS. This feature enables overriding
the 802.1P priority of the data traffic packets arriving at the port enabled for voice VLAN.
Thus, a rogue client that is also connected to the voice VLAN port does not deteriorate the
voice traffic.
When a VLAN ID is configured on the voice VLAN port, the VLAN ID information is passed
onto the VoIP phone using the LLDP-MED mechanism. The voice data coming from the VoIP
phone is tagged with the exchanged VLAN ID; thus, regular data arriving on the switch is
given the default PVID of the port, and the voice traffic is received on a predefined VLAN.
The two types of traffic are segregated so that better service can be provided to the voice
traffic.
Note: The IP phone must support LLDP-MED to accept the VLAN ID and
CoS information from the switch.
Switching Commands 445

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
voice vlan (Global Config)
Use this command to enable the Voice VLAN capability on the switch.
Default Disabled
Format voice vlan
Mode Global Config
no voice vlan (Global Config)
Use this command to disable the Voice VLAN capability on the switch.
Format no voice vlan
Mode Global Config
voice vlan (Interface Config)
Use this command to enable the Voice VLAN capability on the interface or range of
interfaces.
Default Disabled
Format voice vlan {vlan-id | dot1p priority | none | untagged}
Mode Interface Config
You can configure Voice VLAN in one of four different ways.
Parameter Description
vlan-id Configure the IP phone to forward all voice traffic through the specified VLAN. Valid VLAN ID’s are
from 1 to 4093 (the max supported by the platform).
dot1p Configure the IP phone to use 802.1p priority tagging for voice traffic and to use the default native
VLAN (VLAN 0) to carry all traffic. Valid priority range is 0 to 7.
none Allow the IP phone to use its own configuration to send untagged voice traffic.
untagged Configure the phone to send untagged voice traffic.
no voice vlan (Interface Config)
Use this command to disable the Voice VLAN capability on the interface.
Format no voice vlan
Mode Interface Config
Switching Commands 446

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
voice vlan auth
This command lets the switch accept or reject voice traffic when the port is in an
unauthorized state. By default, the switch rejects voice traffic when the port is in an
unauthorized state.
Default disable
Format voice vlan auth [disable | enable]
Mode Interface Config
voice vlan data priority
Use this command to either trust or untrust the data traffic arriving on the Voice VLAN
interface or range of interfaces being configured.
Default trust
Format voice vlan data priority {untrust | trust}
Mode Interface Config
show voice vlan
Use this command to display information about the voice VLAN.
Format show voice vlan [interface {unit/slot/port | all}]
Mode Privileged EXEC
When the interface parameter is not specified, only the global mode of the Voice VLAN is
displayed.
Term Definition
Administrative Mode The Global Voice VLAN mode.
When the interface parameter is specified..
Term Definition
Voice VLAN Mode The admin mode of the Voice VLAN on the interface.
Voice VLAN ID The Voice VLAN ID
Voice VLAN Priority The do1p priority for the Voice VLAN on the port.
Voice VLAN Untagged The tagging option for the Voice VLAN traffic.
Voice VLAN CoS Override The Override option for the voice traffic arriving on the port.
Voice VLAN Status The operational status of Voice VLAN on the port.
Switching Commands 447

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Precision Time Protocol Commands
This section describes the commands you use to configure the Precision Time Protocol
(PTP) end-to-end (E2E) transparent clock.
ptp clock e2e-transparent
This command enables the PTP E2E transparent clock at system level (that is, globaly) or for
an interface.
Default Enabled at system level and for all interfaces
Format ptp clock e2e-transparent
Mode Global Config
Interface Config
In Global Config mode, the command applies the PTP transparent clock configuration to all
physical ports and LAG on the switch. In Interface Config mode, the command provides a
next-level control so you can disable this feature selectively for an individual physical port or
LAG.
You can configure the PTP transparent clock for physical ports and LAGs, but not for a
VLAN. When you configure the PTP transparent clock on a LAG, the configuration is applied
to all member ports.
no ptp clock e2e-transparent
This command disables the PTP E2E transparent clock at system level or for an interface.
Format no ptp clock e2e-transparent
Mode Global Config
Interface Config
show ptp clock e2e-transparent
Use this command to display the operational and configuration status of the PTP E2E
transparent clock, both at system level and at interface level.
Format show ptp clock e2e-transparent
Mode Privileged Exec
Term Definition
Interface The interface on which the feature is configured.
Switching Commands 448

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Configured Mode The configuration status of the PTP E2E transparent clock on the interface
Operational Mode The operational status of the PTP E2E transparent clock on the interface.
Command example:
(NETGEAR Switch) #show ptp clock e2e-transparent
PTP TC mode.................................... Enabled
Interface Configured Mode Operational Mode
--------- --------------- ----------------
1/1/1 Enabled Disabled
1/1/2 Enabled Disabled
1/1/3 Enabled Disabled
1/1/4 Enabled Disabled
1/1/5 Enabled Disabled
1/1/6 Enabled Disabled
1/1/7 Enabled Disabled
1/1/8 Enabled Disabled
Provisioning (IEEE 802.1p) Commands
This section describes the commands you use to configure provisioning (IEEE 802.1p,)
which allows you to prioritize ports.
vlan port priority all
This command configures the port priority assigned for untagged packets for all ports
presently plugged into the device. The range for the priority is 0-7. Any subsequent per port
configuration will override this configuration setting.
Format vlan port priority all priority
Mode Global Config
vlan priority
This command configures the default 802.1p port priority assigned for untagged packets for a
specific interface. The range for the priority is 0–7.
Default 0
Format vlan priority priority
Mode Interface Config
Switching Commands 449

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Asymmetric Flow Control
When in asymmetric flow control mode, the switch responds to PAUSE frames received from
a peer by stopping packet transmission, but the switch does not initiate MAC control PAUSE
frames.
When you configure the switch in asymmetric flow control (or no flow control mode), the
device is placed in egress drop mode. Egress drop mode maximizes the throughput of the
system at the expense of packet loss in a heavily congested system, and this mode avoids
head-of-line blocking.
flowcontrol
Use this command to enable the symmetric or asymmetric flow control on the switch.
Asymmetric flow control means you can enable Rx Pause only but not Tx Pause.
Default Flow control is disabled.
Format flowcontrol {symmetric | asymmetric}
Mode Interface Config
no flowcontrol
This command disables flow control.
Format no flowcontrol
Mode Global Config
show flowcontrol
Use this command to display the IEEE 802.3 Annex 31B flow control settings and status for a
specific interface or all interfaces. The command also displays 802.3 Tx and Rx pause
counts. Priority Flow Control frames counts are not displayed. If the port is enabled for priority
flow control, operational flow control status is displayed as Inactive. Operational flow control
status for stacking ports is always displayed as N/A.
Format show flowcontrol [interface unit/slot/port]
Mode Privileged Exec
Switching Commands 450

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show flowcontrol
Admin Flow Control: Symmetric
Port Flow Control RxPause TxPause
Oper
------ ------------ -------- ---------
0/1 Active 310 611
0/2 Inactive 0 0
Command example:
(NETGEAR Switch) #show flowcontrol interface 0/1
Admin Flow Control: Symmetric
Port Flow Control RxPause TxPause
Oper
--------- ------- -------- -------
0/1 Active 310 611
Protected Ports Commands
This section describes commands you use to configure and view protected ports on a switch.
Protected ports do not forward traffic to each other, even if they are on the same VLAN.
However, protected ports can forward traffic to all unprotected ports in their group.
Unprotected ports can forward traffic to both protected and unprotected ports. Ports are
unprotected by default.
If an interface is configured as a protected port, and you add that interface to a Port Channel
or Link Aggregation Group (LAG), the protected port status becomes operationally disabled
on the interface, and the interface follows the configuration of the LAG port. However, the
protected port configuration for the interface remains unchanged. Once the interface is no
longer a member of a LAG, the current configuration for that interface automatically becomes
effective.
switchport protected (Global Config)
Use this command to create a protected port group. The groupid parameter identifies the
set of protected ports. Use the name parameter to assign a name to the protected port group.
The name can be up to 32 alphanumeric characters long, including blanks. The default is
blank.
Switching Commands 451

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: Port protection occurs within a single switch. Protected port
configuration does not affect traffic between ports on two different
switches. No traffic forwarding is possible between two protected
ports.
Default unprotected
Format switchport protected groupid name name
Mode Global Config
no switchport protected (Global Config)
Use this command to remove a protected port group. The groupid parameter identifies the
set of protected ports. The name parameter specifies the name to remove from the group.
Format no switchport protected groupid name name
Mode Global Config
switchport protected (Interface Config)
Use this command to add an interface to a protected port group. The groupid parameter
identifies the set of protected ports to which this interface is assigned. You can only configure
an interface as protected in one group.
Note: Port protection occurs within a single switch. Protected port
configuration does not affect traffic between ports on two different
switches. No traffic forwarding is possible between two protected
ports.
Default unprotected
Format switchport protected groupid
Mode Interface Config
no switchport protected (Interface Config)
Use this command to configure a port as unprotected. The groupid parameter identifies the
set of protected ports to which this interface is assigned.
Format no switchport protected groupid
Mode Interface Config
Switching Commands 452

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show switchport protected
This command displays the status of all the interfaces, including protected and unprotected
interfaces.
Format show switchport protected groupid
Mode Privileged EXEC
User EXEC
Term Definition
Group ID The number that identifies the protected port group.
Name An optional name of the protected port group. The name can be up to 32 alphanumeric characters
long, including blanks. The default is blank.
List of Physical List of ports, which are configured as protected for the group identified with groupid. If no port is
Ports configured as protected for this group, this field is blank.
show interfaces switchport (for a group ID)
This command displays the status of the interface (protected or unprotected) under the
groupid.
Format show interfaces switchport unit/slot/port groupid
Mode Privileged EXEC
User EXEC
Term Definition
Name A string associated with this group as a convenience. It can be up to 32 alphanumeric characters
long, including blanks. The default is blank. This field is optional.
Protected Indicates whether the interface is protected or not. It shows TRUE or FALSE. If the group is a
multiple groups then it shows TRUE in Group groupid.
Private Group Commands
This section describes commands that are used to configure a private group and view the
configuration information of a private group.
You can use a private group to create a group of ports that either can or cannot share traffic
with each other in the same VLAN group. The main purpose of a private group is to isolate a
group of users from another group of users without using a VLAN.
Switching Commands 453

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
switchport private-group
This command assigns one port or a range of ports to a private group. You specify the private
group by either its name or its identifier.
The ingress traffic from a port in a private group can be forwarded to other ports either in the
same private group or outside the private group but in the same VLAN.
By default, a port does not belong to any private group. A port cannot be in more than one
private group. To change the membership of a port in a private group, first remove the port
from the private group.
Format switchport private-group [privategroup-name | privategroup-id]
Mode Interface Config
no switchport private-group
This command removes a port from to a private group.
Format no switchport private-group [privategroup-name | privategroup-id]
Mode Interface Config
private-group name
This command creates a private group with a name or an identifier. The name string can be
up to 24 bytes of non-blank characters. A total number of 192 of private groups is supported.
Therefore, the group identifier can be from 1 to 192.
The private-group-id parameter is optional. If you do not specify a group identifier, the
identifier is assigned automatically.
The optional mode for the group can be either isolated or community. If the private group is in
isolated mode, the member port in the group cannot forward its egress traffic to any other
members in the same group. By default, the mode for the private group is community mode,
allowing each member port to forward traffic to other members in the same group, but not to
members in other groups.
Format private-group name privategroup-name [private-group-id] [mode {community |
isolated}]
Mode Global Config
no private-group name
This command removes a private group.
Format no private-group name privategroup-name
Mode Global Config
Switching Commands 454
