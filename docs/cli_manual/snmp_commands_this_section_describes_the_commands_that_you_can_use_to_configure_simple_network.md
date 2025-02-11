# snmp_commands_this_section_describes_the_commands_that_you_can_use_to_configure_simple_network

Pages: 129-139

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #
(NETGEAR Switch) #show domain-name
Domain : Enable
Domain-name :abc
SNMP Commands
This section describes the commands that you can use to configure Simple Network
Management Protocol (SNMP) on the switch. You can configure the switch to act as an
SNMP agent so that it can communicate with SNMP managers on your network.
snmp-server
This command sets the name and the physical location of the switch and the organization
responsible for the network. The range for the name, loc and con parameters is from 1 to 31
alphanumeric characters.
Default none
Format snmp-server {sysname name | location loc | contact con}
Mode Global Config
snmp-server community
This command adds (and names) a new SNMP community. A community name is associated
with the switch and with a set of SNMP managers that manage the community with a
specified privileged level. The length of the name parameter can be up to 16 case-sensitive
characters.
Note: Community names in the SNMP Community table must be unique. If
multiple entries are made using the same community name, the first
entry is kept and processed and all duplicate entries are ignored.
Format snmp-server community name
Mode Global Config
Management Commands 129

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no snmp-server community
This command removed a community name from the table. The name parameter is the
community name that must be deleted.
Format no snmp-server community name
Mode Global Config
snmp-server community ipaddr
This command sets a client IP address for an SNMP community. The SNMP community
sends SNMP packets from this address. The address along with the client IP mask value
denotes a range of IP addresses from which SNMP clients can use the community to access
the device. A value of 0.0.0.0 allows access from any IP address. Otherwise, this value is
ANDed with the mask to determine the range of allowed client IP addresses. The name is the
applicable community name.
Default 0.0.0.0
Format snmp-server community ipaddr ipaddr name
Mode Global Config
no snmp-server community ipaddr
This command sets a client IP address for an SNMP community to 0.0.0.0. The name is the
applicable community name.
Format no snmp-server community ipaddr name
Mode Global Config
snmp-server community ipmask
This command sets a client IP mask for an SNMP community. The SNMP community sends
SNMP packets from an address with this client IP mask. The address along with the client IP
mask value denotes a range of IP addresses from which SNMP clients can use the
community to access the device. A value of 255.255.255.255 allows access from only one
computer and specifies that computer’s IP address as the client IP address. A value of
0.0.0.0 allows access from any IP address. The name is the applicable community name.
Default 0.0.0.0
Format snmp-server community ipmask ipmask name
Mode Global Config
Management Commands 130

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no snmp-server community ipmask
This command sets a client IP mask for an SNMP community to 0.0.0.0. The name is the
applicable community name.
Format no snmp-server community ipmask name
Mode Global Config
snmp-server community mode
This command activates an SNMP community. If a community is enabled, an SNMP
manager that is associated with this community manages the switch according to its access
right. If the community is disabled, no SNMP requests using this community are accepted. In
this case, the SNMP manager that is associated with this community cannot manage the
switch until the status is changed back to enabled.
Default • private and public communities - enabled
• other four - disabled
Format snmp-server community mode name
Mode Global Config
no snmp-server community mode
This command deactivates an SNMP community. If the community is disabled, no SNMP
requests using this community are accepted. In this case, the SNMP manager that is
associated with this community cannot manage the switch until the status is changed back to
enabled.
Format no snmp-server community mode name
Mode Global Config
snmp-server community ro
This command restricts access to switch information. The access mode is read-only (also
called public).
Format snmp-server community ro name
Mode Global Config
Management Commands 131

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
snmp-server community rw
This command restricts access to switch information. The access mode is read/write (also
called private).
Format snmp-server community rw name
Mode Global Config
snmp-server user
This command creates an SNMPv3 user that can access the switch.
Default No default user
Format snmp-server user username groupname [remote engineid-string] [auth-sha512
authentication-password| auth-sha512-key sha512-key] {[priv-aes128 encryp-
tion-password| priv-aes128-key aes128-key]}
Mode Global Config
Parameter Description
username The name (from 1 to 30 characters) of the SNMPv3 user.
groupname The group name (from 1 to 30 characters) of which the SNMPv3 user is a member.
engineid-string The engine-id (from 6 to 32 characters) of the remote management station that this user will be
connecting from.
auth-sha512 Indicates that you must enter a password on the basis of which the switch can generate an SHA-512
key for authentication.
authentication- The actual password (from 1 to 32 characters) that lets the switch automatically generate an SHA-512
password key for authentication.
auth-sha512-key Indicates that you must enter (or copy) the SHA-512 key for authentication.
sha512-key The actual SHA-512 key for authentication. The key can be up to 128 characters. If you do not enter a
key, the switch automatically generates a key.
priv-aes128 Indicates that you must enter a password on the basis of which the switch can generate an AES-128
HMAC-MD5-96 key for encryption.
encryption- The actual password (from 1 to 32 characters) that lets the switch automatically generate an AES-128
password HMAC-MD5-96 key for encryption.
priv-aes128-key Indicates that you must enter (or copy) the AES-128 HMAC-MD5-96 key for encryption.
aes128-key The actual AES-128 HMAC-MD5-96 key for encryption. The key can be up to 128 characters. If you do
not enter a key, the switch automatically generates a key.
Management Commands 132

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch)(Config)#snmp-server user test grp1 auth-sha512 priv-aes128
Enter Authentication Password:********
Confirm Authentication Password:********
Enter Encryption Password:********
Confirm Encryption Password:********
Command example:
(NETGEAR Switch)(Config)#snmp-server user test DefaultWrite auth-sha512-key
6991313bb623241c8f6f967fa28dff0265b4b57dfd07301be41024a791df01f412d1ad8bd8cde6ae6d66da7
61987657afe36efd788d021012564cf8ed2718351 priv-aes128-key
6991313bb623241c8f6f967fa28dff0265b4b57dfd07301be41024a791df01f412d1ad8bd8cde6ae6d66da7
61987657afe36efd788d021012564cf8ed2718351
no snmp-server user
This command removes an SNMPv3 user.
Format no snmp-server user username
Mode Global Config
snmp-server enable traps violation
This command enables the switch to send violation traps. The switch sends a violation trap if
it receives a packet with a disallowed MAC address on a locked port.
Note: For information about port security commands, see Protected Ports
Commands on page451.
Default disabled
Format snmp-server enable traps violation
Mode Interface Config
no snmp-server enable traps violation
This command prevents the switch from sending violation traps.
Format no snmp-server enable traps violation
Mode Interface Config
Management Commands 133

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
snmp-server enable traps
This command enables the Authentication Flag.
Default enabled
Format snmp-server enable traps
Mode Global Config
no snmp-server enable traps
This command disables the Authentication Flag.
Format no snmp-server enable traps
Mode Global Config
snmp-server enable traps linkmode
This command enables Link Up/Down traps for the entire switch. If enabled, the switch sends
link traps only if the Link Trap flag setting that is associated with a port is enabled. For more
information, see snmp trap link-status on page138
Default enabled
Format snmp-server enable traps linkmode
Mode Global Config
no snmp-server enable traps linkmode
This command disables Link Up/Down traps for the entire switch.
Format no snmp-server enable traps linkmode
Mode Global Config
snmp-server enable traps multiusers
This command enables multiple user traps. If the traps are enabled, the switch sends a
multiple user trap if a user logs in to the terminal interface (EIA 232 or Telnet) while an
existing terminal interface session is already established.
Default enabled
Format snmp-server enable traps multiusers
Mode Global Config
Management Commands 134

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no snmp-server enable traps multiusers
This command disables multiple user traps.
Format no snmp-server enable traps multiusers
Mode Global Config
snmp-server enable traps stpmode
This command enables the switch to send new root traps and topology change notification
traps.
Default enabled
Format snmp-server enable traps stpmode
Mode Global Config
no snmp-server enable traps stpmode
This command prevents the switch from sending new root traps and topology change
notification traps.
Format no snmp-server enable traps stpmode
Mode Global Config
snmp-server port
This command modifies the port that the switch uses to detect SNMP messages. By default,
the switch uses UDP port 161 to detect SNMP messages.
Default 161
Format snmp-server port number
Mode User EXEC
no snmp-server port
This command resets the port that the switch uses to detect SNMP messages. After you
enter this command, the switch uses UDP port 161 to detect SNMP messages.
Format no snmp-server port
Mode User EXEC
Management Commands 135

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
snmp-server trapsend
Use this command to set the UDP port to which traps are sent by the SNMP server.
Default 50505
Format snmp-server trapsend number
Mode Global Config
no snmp-server trapsend
Use this command to reset the UDP port to which traps are sent by the SNMP server to the
default port of 50505.
Format no snmp-server trapsend
Mode Global Config
snmptrap
This command adds an SNMP trap receiver. The snmpversion parameter is the version of
SNMP. The version parameter option can be snmpv1 or snmpv2. You can set the SNMP trap
address as an IPv4 or IPv6 global address.
The name parameter does not need to be unique, however; the combination of name and
ipaddr or ip6addr must be unique. Multiple entries can exist with the same name as long
as they are associated with a different ipaddr or ip6addr. The reverse scenario is also
acceptable. The name is the community name used when sending the trap to the receiver,
but the name is not directly associated with the SNMP Community table (see snmp-server
community on page129).
Default snmpv2
Format snmptrap name {ipaddr ipaddr | ip6addr ip6addr} [snmpversion snmpversion]
Mode Global Config
Command example:
(NETGEAR Switch)# snmptrap mytrap ip6addr 3099::2
no snmptrap
This command delete trap receivers for a community.
Format no snmptrap name {ipaddr ipaddr | ip6addr ip6addr}
Mode Global Config
Management Commands 136

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
snmptrap snmpversion
This command modifies the SNMP version of a trap. The maximum length of the name
parameter is 16 case-sensitive alphanumeric characters. The snmpversion parameter
options are snmpv1 or snmpv2.
Note: This command does not support a no form.
Default snmpv2
Format snmptrap snmpversion name {ipaddr | ip6addr} {snmpv1 | snmpv2}
Mode Global Config
snmptrap ipaddr
This command assigns a new IP address or host name to a community name. The name can
use up to 16 case-sensitive alphanumeric characters.
Note: IP addresses in the SNMP trap receiver table must be unique. If you
make multiple entries using the same IP address, the first entry is
retained and processed. All duplicate entries are ignored.
Format snmptrap ipaddr name ipaddrold ipaddrnew
Mode Global Config
snmptrap mode
This command activates an SNMP trap. Enabled trap receivers are active (that is, able to
receive traps).
Format snmptrap mode name {ipaddr | ip6addr}
Mode Global Config
no snmptrap mode
This command deactivates an SNMP trap. Disabled trap receivers are inactive (that is, not
able to receive traps).
Format no snmptrap mode name {ipaddr | ip6addr}
Mode Global Config
Management Commands 137

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
snmptrap source-interface
This command configures the global source interface (that is, the source IP address) for all
SNMP communication between the SNMP client and the server.
Format snmptrap source-interface {unit/slot/port | loopback loopback-id | tunnel
tunnel-id | vlan vlan-id}
Mode Global Config
Parameter Description
unit/slot/port The unit identifier that is assigned to the switch.
loopback-id The loopback interface that you want to use as the source IP address. The range of the loopback ID is
from 0 to 7.
tunnel-id The tunnel interface that you want to use as the source IP address. The range of the tunnel ID is from
0 to 7.
vlan-id The VLAN interface that you want to use as the source IP address. The range of the VLAN ID is from
1 to 4093.
no snmptrap source-interface
This command removes the global source interface for all SNMP communication between
the SNMP client and the server.
Format no snmptrap source-interface
Mode Global Config
snmp trap link-status
This command enables link status traps for an interface or for all interfaces.
Format snmp trap link-status
Mode Interface Config
no snmp trap link-status
This command disables link status traps for an interface.
Format no snmp trap link-status
Mode Interface Config
Management Commands 138

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
snmp trap link-status all
This command enables link status traps for all interfaces.
Format snmp trap link-status all
Mode Global Config
no snmp trap link-status
This command disables link status traps for all interfaces.
Format no snmp trap link-status all
Mode Global Config
show snmp-server
This command shows the UDP port to which the SNMP server is connected and on which the
switch sends SNMP traps.
Format show snmp-server
Mode User EXEC
Command example:
(NETGEAR Switch)#show snmp-server
SNMP Server Port............................... 161
SNMP Trap Send Port............................ 162
show snmpcommunity
This command displays SNMP community information. Six communities are supported. You
can add, change, or delete communities. You do not need to reset the switch for changes to
take effect.
The SNMP agent of the switch complies with SNMP Versions 1, 2, and 3. For more
information about the SNMP specification, see the SNMP RFCs. The SNMP agent sends
traps through TCP/IP to an external SNMP manager based on the SNMP configuration (the
trap receiver and other SNMP community parameters).
Format show snmpcommunity
Mode Privileged EXEC
Management Commands 139
