# ip_multicast_commands_1031

Pages: 1031-1031

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip pim bsr-candidate
This command is used to configure the router to announce its candidacy as a bootstrap
router (BSR).
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vland-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in the unit/slot/port format. The vlan-id parameter
is a number in the range of 1–4093.
Note: This command takes effect only when PIM-SM is configured as the
PIM mode.
Default Disabled
Format ip pim bsr-candidate interface {unit/slot/port | vlan vlan-id}
hash-mask-length [bsr-priority] [interval interval]
Mode Global Config
Parameters Description
unit/slot/port Interface or VLAN number on this router from which the BSR address is derived, to make it a
candidate. This interface or VLAN must be enabled with PIM.
hash-mask-length Length of a mask (32 bits maximum) that is to be ANDed with the group address before the hash
function is called. All groups with the same seed hash correspond to the same RP. For example, if
this value is 24, only the first 24 bits of the group addresses matter. This allows you to get one RP for
multiple groups.
bsr-priority [Optional] Priority of the candidate BSR. The range is an integer from 0 to 255. The BSR with the
larger priority is preferred. If the priority values are the same, the router with the larger IP address is
the BSR. The default value is 0.
interval [Optional] Indicates the BSR candidate advertisement interval. The range is from 1 to 16383
seconds. The default value is 60 seconds.
Command example: The following shows examples of the command.
(NETGEAR) (Config) #ip pim bsr-candidate interface 1/0/1 32 5
(NETGEAR) (Config) #ip pim bsr-candidate interface 1/0/1 32 5 interval 100
no ip pim bsr-candidate
Use this command to remove the configured PIM Candidate BSR router.
Format no ip pim bsr-candidate interface {unit/slot/port | vlan vlan-id}
Mode Global Config
IP Multicast Commands 1031
