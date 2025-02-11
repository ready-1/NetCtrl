# ip_multicast_commands_1059

Pages: 1059-1071

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show ip igmp-proxy groups
Interface Index................................ 1/0/1
G roup Address Last Reporter Up Time Member State F ilter Mode Sources
------------- - ------------- - ---------- - ----------- - ----------- ---------
2 25.4.4.4 5 .5.5.48 0 0:02:21 D ELAY_MEMBER I nclude 3
G roup Source List Expiry Time
----------------- -----------------
5.1.2.3 00:02:21
6 .1.2.3 00:02:21
7.1.2.3 00:02:21
2 26.4.4.4 5 .5.5.48 0 0:02:21 D ELAY_MEMBER I nclude 3
Group Source List Expiry Time
----------------- -----------------
2.1.2.3 00:02:21
6 .1.2.3 00:01:44
8 .1.2.3 00:01:44
2 27.4.4.4 5 .5.5.48 0 0:02:21 D ELAY_MEMBER E xclude 0
2 28.4.4.4 5 .5.5.48 0 0:03:21 D ELAY_MEMBER I nclude 3
Group Source List Expiry Time
----------------- -----------------
9 .1.2.3 00:03:21
6 .1.2.3 00:03:21
7 .1.2.3 00:03:21
IP Multicast Commands 1059

IPv6 Multicast Commands

This chapter describes the IPv6 multicast commands.
The chapter contains the following sections:
• IPv6 Multicast Forwarder
• IPv6 PIM Commands
• IPv6 MLD Commands
• IPv6 MLD-Proxy Commands
Note: No specific command exists to enable multicast for IPv6. If you enable
multicast with a global config command, multicast is enabled for both
IPv4 and IPv6.
The commands in this chapter are in one of three functional groups:
• Show commands. Display switch settings, statistics, and other information.
• Configuration commands. Configure features and options of the switch. For every
configuration command, there is a show command that displays the configuration setting.
• Clear commands. Clear some or all of the settings to factory defaults.

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
IPv6 Multicast Forwarder
ipv6 mroute
This command configures an IPv6 Multicast Static Route for a source.
Default No MRoute is configured on the system.
Format ipv6 mroute src-ip-addr src-mask rpf-addr [interface] preference
Mode Global Config
Parameter Description
src-ip-addr The IP address of the multicast source network.
src-mask The IP mask of the multicast data source.
rpf-ip-addr The IP address of the RPF next-hop router toward the source.
interface [Optional] Specify the interface if the RPF Address is a link-local address.
preference The administrative distance for this Static MRoute, that is, the preference value. The range is 1 to
255.
no ipv6 mroute
This command removes the configured IPv6 Multicast Static Route.
Format no ip mroute src-ip-addr
Mode Global Config
Note: There is no specific IP multicast enable for IPv6. Enabling of multicast
at global config is common for both IPv4 and IPv6.
show ipv6 mroute
Use this command to show the mroute entries that are specific to IPv6. (This command is the
IPv6 equivalent of the IPv4 show ip mroute command.)
Format show ipv6 mroute [detail | summary]
Modes Privileged EXEC
User EXEC
IPv6 Multicast Commands 1061

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If you use the detail parameter, the command displays the following Multicast Route Table
fields.
Term Definition
Source IP Addr The IP address of the multicast data source.
Group IP Addr The IP address of the destination of the multicast packet.
Expiry Time The time of expiry of this entry in seconds.
Up Time The time elapsed since the entry was created in seconds.
RPF Neighbor The IP address of the RPF neighbor.
Flags The flags associated with this entry.
If you use the summary parameter, the command displays the following fields.
Term Definition
Source IP Addr The IP address of the multicast data source.
Group IP Addr The IP address of the destination of the multicast packet.
Protocol The multicast routing protocol by which the entry was created.
Incoming Interface The interface on which the packet for the source/group arrives.
Outgoing Interface List The list of outgoing interfaces on which the packet is forwarded.
show ipv6 mroute group
This command displays the multicast configuration settings specific to IPv6 such as flags,
timer settings, incoming and outgoing interfaces, RPF neighboring routers, and expiration
times of all the entries in the multicast route table containing the given group IPv6 address
group-address.
Format show ipv6 mroute group group-address {detail | summary}
Modes Privileged EXEC
User EXEC
Term Definition
Source IP Addr The IP address of the multicast data source.
Group IP Addr The IP address of the destination of the multicast packet.
Protocol The multicast routing protocol by which this entry was created.
Incoming Interface The interface on which the packet for this group arrives.
Outgoing Interface List The list of outgoing interfaces on which this packet is forwarded.
IPv6 Multicast Commands 1062

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ipv6 mroute source
This command displays the multicast configuration settings that are specific to IPv6 such as
flags, timer settings, incoming and outgoing interfaces, RPF neighboring routers, and
expiration times of all the entries in the multicast route table for the specified source IP
address (source-address).
Format show ipv6 mroute source source-address {detail | summary}
Modes Privileged EXEC
User EXEC
If you use the detail keyword, the command displays the following column headings in the
output table.
Term Definition
Source IP Addr The IP address of the multicast data source.
Group IP Addr The IP address of the destination of the multicast packet.
Expiry Time The time of expiry of this entry in seconds.
Up Time The time elapsed since the entry was created in seconds.
RPF Neighbor The IP address of the RPF neighbor.
Flags The flags associated with this entry.
If you use the summary keyword, the command displays the following column headings in
the output table.
Term Definition
Source IP Addr The IP address of the multicast data source.
Group IP Addr The IP address of the destination of the multicast packet.
Protocol The multicast routing protocol by which this entry was created.
Incoming Interface The interface on which the packet for this source arrives.
Outgoing Interface List The list of outgoing interfaces on which this packet is forwarded.
show ipv6 mroute static
Use the show ipv6 mroute static command in Privileged EXEC or User EXEC mode
to display all the configured IPv6 multicast static routes.
Format show ipv6 mroute static [source-address]
Modes Privileged EXEC
User EXEC
IPv6 Multicast Commands 1063

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
Source Address IP address of the multicast source network.
Source Mask The subnetwork mask pertaining to the sourceIP.
RPF Address The IP address of the RPF next-hop router toward the source.
Interface The interface that is used to reach the RPF next-hop. This is valid if the RPF address is a link-local
address.
Preference The administrative distance for this Static MRoute.
clear ipv6 mroute
This command deletes all or the specified IPv6 multicast route entries.
Note: This command clears only dynamic mroute entries. It does not clear
static mroutes.
Format clear ipv6 mroute {* | group-address [source-address]}
Modes Privileged EXEC
Parameter Description
* Deletes all IPv6 entries from the IPv6 multicast routing table.
group-address IPv6 address of the multicast group.
source-address The IPv6 address of a multicast source that is sending multicast traffic to the group.
The following example deletes all entries from the IPv6 multicast routing table:
(NETGEAR Switch) # clear ipv6 mroute *
Command example:
The following example deletes all entries from the IPv6 multicast routing table that match the
multicast group address (FF4E::1), irrespective of which source is sending for this group:
(NETGEAR Switch) # clear ipv6 mroute FF4E::1
Command example:
The following example deletes all entries from the IPv6 multicast routing table that match the
multicast group address (FF4E::1) and the multicast source address (2001::2):
(NETGEAR Switch) # clear ipv6 mroute FF4E::1 2001::2
IPv6 Multicast Commands 1064

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
IPv6 PIM Commands
This section describes the commands you use to configure Protocol Independent Multicast
-Dense Mode (PIM-DM) and Protocol Independent Multicast - Sparse Mode (PIM-SM) for
IPv6 multicast routing. PIM-DM and PIM-SM are multicast routing protocols that provides
scalable inter-domain multicast routing across the Internet, independent of the mechanisms
provided by any particular unicast routing protocol. Only one PIM mode can be operational at
a time.
ipv6 pim dense
This command enables the administrative mode of PIM-DM in the router.
Default disabled
Format ipv6 pim dense
Mode Global Config
Command example:
(NETGEAR) (Config) #ipv6 pim dense
no ipv6 pim dense
This command disables the administrative mode of PIM-DM in the router.
Format no ipv6 pim dense
Mode Global Config
ipv6 pim sparse
This command enables the administrative mode of PIM-SM in the router.
Default disabled
Format ipv6 pim sparse
Mode Global Config
Command example:
(NETGEAR) (Config) #ipv6 pim sparse
IPv6 Multicast Commands 1065

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ipv6 pim sparse
This command disables the administrative mode of PIM-SM in the router.
Format no ipv6 pim sparse
Mode Global Config
ipv6 pim
This command administratively enables PIM on an interface or range of interfaces.
Default disabled
Format ipv6 pim
Mode Interface Config
Command example:
(NETGEAR) (Interface 1/0/1) #ipv6 pim
no ipv6 pim
This command sets the administrative mode of PIM on an interface to disabled.
Format no ipv6 pim
Mode Interface Config
ipv6 pim hello-interval
Use this command to configure the PIM hello interval for the specified router interface or
range of interfaces. The seconds argument is the hello-interval, specified in the range
0–18000 seconds.
Default 30
Format ipv6 pim hello-interval seconds
Mode Interface Config
Command example:
(NETGEAR) (Interface 1/0/1) #ipv6 pim hello-interval 50
IPv6 Multicast Commands 1066

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ipv6 pim hello-interval
Use this command to set the PIM hello interval to the default value.
Format no ipv6 pim hello-interval
Mode Interface Config
ipv6 pim bsr-border
Use this command to prevent bootstrap router (BSR) messages from being sent or received
on the specified interface.
Note: This command takes effect only when PIM-SM is enabled in the
Global mode.
Default disabled
Format ipv6 pim bsr-border
Mode Interface Config
(NETGEAR) (Interface 1/0/1) #ipv6 pim bsr-border
no ipv6 pim bsr-border
Use this command to disable the setting of BSR border on the specified interface.
Format no ipv6 pim bsr-border
Mode Interface Config
ipv6 pim bsr-candidate
This command is used to configure the router to announce its candidacy as a bootstrap
router (BSR).
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
Note: This command takes effect only when PIM-SM is configured as the
PIM mode.
IPv6 Multicast Commands 1067

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default Disabled
Format ipv6 pim bsr-candidate interface {unit/slot/port | vlan vland-id}
hash-mask-length [bsr-priority] [interval interval]
Mode Global Config
Parameters Description
unit/slot/port Interface or VLAN number on this router from which the BSR address is derived, to make it a
candidate. This interface or VLAN must be enabled with PIM.
hash-mask-length Length of a mask (32 bits maximum) that is to be ANDed with the group address before the hash
function is called. All groups with the same seed hash correspond to the same RP. For example, if
this value was 24, only the first 24 bits of the group addresses matter. This allows you to get one RP
for multiple groups.
bsr-priority [Optional] Priority of the candidate BSR. The range is an integer from 0 to 255. The BSR with the
larger priority is preferred. If the priority values are the same, the router with the larger IPv6 address
is the BSR. The default value is 0.
interval [Optional] Indicates the BSR candidate advertisement interval. The range is from 1 to 16383
seconds. The default value is 60 seconds.
Command example:
(NETGEAR) (Config) #ipv6 pim bsr-candidate interface 1/0/1 32 5
(NETGEAR) (Config) #ipv6 pim bsr-candidate interface 1/0/1 32 5 interval 100
no ipv6 pim bsr-candidate
This command is used to remove the configured PIM Candidate BSR router.
Format no ipv6 pim bsr-candidate interface {unit/slot/port | vlan vland-id}
Mode Global Config
ipv6 pim dr-priority
Use this command to set the priority value for which a router is elected as the designated
router (DR). The priority argument is a value in the range of 0–2147483647.
Note: This command takes effect only when PIM-SM is enabled in the
Global mode.
IPv6 Multicast Commands 1068

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default 1
Format ipv6 pim dr-priority priority
Mode Interface Config
Command example:
(NETGEAR) (Interface 1/0/1) #ipv6 pim dr-priority 10
no ipv6 pim dr-priority
Use this command to return the DR Priority on the specified interface to its default value.
Format no ipv6 pim dr-priority
Mode Interface Config
ipv6 pim join-prune-interval
This command is used to configure the join/prune interval for the PIM-SM router on an
interface or range of interfaces. The join/prune interval is specified in seconds. The seconds
argument can be configured as a value from 0 to 18000 seconds.
Note: This command takes effect only when PIM-SM is enabled in the
Global mode.
Default 60
Format ipv6 pim join-prune-interval seconds
Mode Interface Config
Command example: The following shows examples of the command.
(NETGEAR) (Interface 1/0/1) #ipv6 pim join-prune-interval 90
no ipv6 pim join-prune-interval
Use this command to set the join/prune interval on the specified interface to the default value.
Format no ipv6 pim join-prune-interval
Mode Interface Config
IPv6 Multicast Commands 1069

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ipv6 pim rp-address
This command defines the address of a PIM Rendezvous point (RP) for a specific multicast
group range.
Note: This command takes effect only when PIM-SM is configured as the
PIM mode.
Default 0
Format ipv6 pim rp-address rp-address group-address/prefix-length [override]
Mode Global Config
Parameter Description
rp-address The IPv6 address of the RP.
group-address/ The group address and prefix length supported by the RP.
prefix-length
override [Optional] Indicates that if there is a conflict, the RP configured with this command prevails over the
RP learned by BSR.
no ipv6 pim rp-address
This command is used to remove the address of the configured PIM Rendezvous point (RP)
for the specified multicast group range.
Format no ipv6 pim rp-address rp-address group-address/prefix-length [override]
Mode Global Config
ipv6 pim rp-candidate
This command is used to configure the router to advertise itself as a PIM candidate
rendezvous point (RP) to the bootstrap router (BSR) for a specific multicast group range.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
Note: This command takes effect only when PIM-SM is configured as the
PIM mode.
IPv6 Multicast Commands 1070

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default Disabled
Format ipv6 pim rp-candidate interface {unit/slot/port | vlan vland-id}
group-address group-mask [interval interval]
Mode Global Config
Parameter Description
unit/slot/port or The interface type in the unit/slot/port format or the VLAN ID is advertised as a candidate RP
vland-id address. This interface or VLAN must be enabled with PIM.
group-address The multicast group address that is advertised in association with the RP address.
group-mask The multicast group prefix that is advertised in association with the RP address.
interval [Optional] Indicates the RP candidate advertisement interval. The range is from 1 to 16383 seconds.
The default value is 60 seconds.
no ipv6 pim rp-candidate
This command is used to disable the router to advertise itself as a PIM candidate rendezvous
point (RP) to the bootstrap router (BSR).
Format no ipv6 pim rp-candidate interface {unit/slot/port | vlan vlan-id}
group-address group-mask
Mode Global Config
ipv6 pim ssm
Use this command to define the Source Specific Multicast (SSM) range of IPv6 multicast
addresses on the router.
Note: This command takes effect only when PIM-SM is configured as the
PIM mode.
Note: Some platforms do not support a non-zero data threshold rate. For
these platforms, only a “Switch on First Packet” policy is supported.
Default disabled
Format ipv6 pim ssm {default | group-address group-mask}
Mode Global Config
IPv6 Multicast Commands 1071
