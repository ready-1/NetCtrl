# vlan_egress_tagging_on_the_port_that_is_connected_to_the_destination

Pages: 530-535

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
VLAN. At the destination switch, you must specify the source as the RSPAN VLAN. You
cannot configure the source and destination as remote on the same switch.
Note: If an interface is a member of both a VLAN and a LAG, you cannot
assign the VLAN as a destination VLAN for a monitor session.
However, if an interface is a member of a VLAN and you assign the
VLAN as a destination VLAN for a monitor session, afterwards you
can add the interface as a member to a LAG.
Note: On an intermediate switch, you must create an RSPAN VLAN, make
sure that the ports that are connected to the source and destination
switches are members of the RSPAN VLAN, and enable RSPAN
VLAN egress tagging on the port that is connected to the destination
switch.
If you specify an RSPAN VLAN ID, you must also specify the reflector port at the source
switch. The reflector port, which must be a member of the RSPAN VLAN, forwards the
mirrored traffic to the destination switch. You specify the reflector port by entering the
reflector-port keyword and the unit/slot/port argument.
Format monitor session session-id destination {interface {unit/slot/port} | remote vlan vlan-id reflector-port
unit/slot/port}
Mode Global Config
no monitor session destination
This command removes a destination interface for a port mirroring session that is identified
by the session-id argument (an integer value).
Format no monitor session session-id destination {interface | remote vlan unit/slot/port}
Mode Global Config
no monitor
This command removes all the source ports and a destination port for the and restores the
default value for mirroring session mode for all the configured sessions.
Note: This is a stand-alone no command. This command does not have a
normal form.
Switching Commands 530

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format no monitor
Mode Global Config
show monitor session
This command displays the port monitoring information for a particular mirroring session.
Note: The session-id parameter is an integer value used to identify the
session. In the current version of the software, the session-id
parameter is a number from 1 to 4.
Format show monitor session session-id
Mode Privileged EXEC
Term Definition
Session ID An integer value used to identify the session. Its value can be anything between 1 and the maximum
number of mirroring sessions allowed on the platform.
Monitor Session Indicates whether the Port Mirroring feature is enabled or disabled for the session identified with
Mode session-id. The possible values are Enabled and Disabled.
Probe Port Probe port (destination port) for the session identified with session-id. If probe port is not set then
this field is blank.
Source Port The port, which is configured as mirrored port (source port) for the session identified with
session-id. If no source port is configured for the session then this field is blank.
Type Direction in which source port configured for port mirroring.Types are tx for transmitted packets and
rx for receiving packets.
Src VLAN All member ports of this VLAN are mirrored. If the source VLAN is not configured, this field is blank.
Ref. Port This port carries all the mirrored traffic at the source switch.
Src Remote VLAN The source VLAN is configured at the destination switch. If the remote VLAN is not configured, this
field is blank.
Dst Remote VLAN The destination VLAN is configured at the source switch. If the remote VLAN is not configured, this
field is blank.
IP ACL The IP access-list id or name attached to the port mirroring session.
MAC ACL The MAC access-list name attached to the port mirroring session.
Switching Commands 531

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show vlan remote-span
This command displays the configured RSPAN VLAN.
Format show vlan remote-span
Mode Privileged Exec Mode
Command example:
(NETGEAR Switch)# show vlan remote-span
Remote SPAN VLAN
------------------------------------------------------------------------

Static MAC Filtering Commands
The commands in this section describe how to configure static MAC filtering. Static MAC
filtering allows you to configure destination ports for a static multicast MAC filter irrespective
of the platform.
macfilter
This command adds a static MAC filter entry for the MAC address macaddr on the VLAN
vlanid. A packet with a specific destination MAC address in a specific VLAN is admitted
only if the ingress port is defined in the set of source ports, otherwise the packet is dropped.
On the egress side, a packet that was admitted is sent through all ports that are defined in the
set of destination ports.
The value of the macaddr parameter is a 6-byte hexadecimal number in the format of
b1:b2:b3:b4:b5:b6. The restricted MAC Addresses are: 00:00:00:00:00:00,
01:80:C2:00:00:00 to 01:80:C2:00:00:0F, 01:80:C2:00:00:20 to 01:80:C2:00:00:21, and
FF:FF:FF:FF:FF:FF. The vlanid parameter must identify a valid VLAN.
The number of static mac filters supported on the system is different for MAC filters where
source ports are configured and MAC filters where destination ports are configured.
• For unicast MAC address filters and multicast MAC address filters with source port lists,
the maximum number of static MAC filters supported is 20.
• For multicast MAC address filters with destination ports configured, the maximum number
of static filters supported is 256.
For example, you can configure the following combinations:
• Unicast MAC and source port (max = 20)
• Multicast MAC and source port (max = 20)
Switching Commands 532

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
• Multicast MAC and destination port (only) (max = 256)
• Multicast MAC and source ports and destination ports (max = 20)
Format macfilter macaddr vlanid
Mode Global Config
no macfilter
This command removes all filtering restrictions and the static MAC filter entry for the MAC
address macaddr on the VLAN vlanid. The macaddr parameter must be specified as a
6-byte hexadecimal number in the format of b1:b2:b3:b4:b5:b6.
The vlanid parameter must identify a valid VLAN.
Format no macfilter macaddr vlanid
Mode Global Config
macfilter adddest
Use this command to add the interface or range of interfaces to the destination filter set for
the MAC filter with the given macaddr and VLAN of vlanid. The macaddr parameter must
be specified as a 6-byte hexadecimal number in the format of b1:b2:b3:b4:b5:b6. The
vlanid parameter must identify a valid VLAN.
Note: Configuring a destination port list is only valid for multicast MAC
addresses.
Format macfilter adddest macaddr vlanid
Mode Interface Config
no macfilter adddest
This command removes a port from the destination filter set for the MAC filter with the given
macaddr and VLAN of vlanid. The macaddr parameter must be specified as a 6-byte
hexadecimal number in the format of b1:b2:b3:b4:b5:b6. The vlanid parameter must
identify a valid VLAN.
Format no macfilter adddest macaddr vlanid
Mode Interface Config
Switching Commands 533

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
macfilter adddest all
This command adds all interfaces to the destination filter set for the MAC filter with the given
macaddr and VLAN of vlanid. The macaddr parameter must be specified as a 6-byte
hexadecimal number in the format of b1:b2:b3:b4:b5:b6. The vlanid parameter must
identify a valid VLAN.
Note: Configuring a destination port list is only valid for multicast MAC
addresses.
Format macfilter adddest all macaddr vlanid
Mode Global Config
no macfilter adddest all
This command removes all ports from the destination filter set for the MAC filter with the
given macaddr and VLAN of vlanid. The macaddr parameter must be specified as a
6-byte hexadecimal number in the format of b1:b2:b3:b4:b5:b6. The vlanid parameter must
identify a valid VLAN.
Format no macfilter adddest all macaddr vlanid
Mode Global Config
macfilter addsrc
This command adds the interface or range of interfaces to the source filter set for the MAC
filter with the MAC filter with the given macaddr and VLAN of vlanid. The macaddr
parameter must be specified as a 6-byte hexadecimal number in the format of
b1:b2:b3:b4:b5:b6. The vlanid parameter must identify a valid VLAN.
Format macfilter addsrc macaddr vlanid
Mode Interface Config
no macfilter addsrc
This command removes a port from the source filter set for the MAC filter with the given
macaddr and VLAN of vlanid. The macaddr parameter must be specified as a 6-byte
hexadecimal number in the format of b1:b2:b3:b4:b5:b6. The vlanid parameter must
identify a valid VLAN.
Format no macfilter addsrc macaddr vlanid
Mode Interface Config
Switching Commands 534

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
macfilter addsrc all
This command adds all interfaces to the source filter set for the MAC filter with the MAC filter
with the given macaddr and VLAN of vlanid. The macaddr parameter must be specified
as a 6-byte hexadecimal number in the format of b1:b2:b3:b4:b5:b6. The vlanid parameter
must identify a valid VLAN.
Format macfilter addsrc all macaddr vlanid
Mode Global Config
no macfilter addsrc all
This command removes all interfaces to the source filter set for the MAC filter with the given
macaddr and VLAN of vlanid. The macaddr parameter must be specified as a 6-byte
hexadecimal number in the format of b1:b2:b3:b4:b5:b6. The vlanid parameter must
identify a valid VLAN.
Format no macfilter addsrc all macaddr vlanid
Mode Global Config
show mac-address-table static
This command displays the Static MAC Filtering information for all Static MAC Filters. If you
specify all, all the static MAC filters in the system are displayed. If you supply a value for
macaddr, you must also enter a value for vlanid, and the system displays static MAC filter
information only for that MAC address and VLAN.
Format show mac-address-table static {macaddr vlanid | all}
Mode Privileged EXEC
Term Definition
MAC Address The MAC Address of the static MAC filter entry.
VLAN ID The VLAN ID of the static MAC filter entry.
Source Ports The source port filter set slot and ports.
Note: Only multicast address filters can have destination port lists.
Switching Commands 535
