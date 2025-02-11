# mac_address_of_the_hardware_platform_of_the_client_consisting_of_6_bytes_in_dotted

Pages: 267-277

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
dns-server
This command specifies the IP servers available to a DHCP client. Address parameters are
valid IP addresses; each made up of four decimal bytes ranging from 0 to 255. IP address
0.0.0.0 is invalid.
Default none
Format dns-server address1 [address2....address8]
Mode DHCP Pool Config
no dns-server
This command removes the DNS Server list.
Format no dns-server
Mode DHCP Pool Config
hardware-address
This command specifies the hardware address of a DHCP client. Hardware-address is the
MAC address of the hardware platform of the client consisting of 6 bytes in dotted
hexadecimal format. Type indicates the protocol of the hardware platform. It is 1 for 10 MB
Ethernet and 6 for IEEE 802.
Default ethernet
Format hardware-address hardwareaddress type
Mode DHCP Pool Config
no hardware-address
This command removes the hardware address of the DHCP client.
Format no hardware-address
Mode DHCP Pool Config
Utility Commands 267

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
host
This command specifies the IP address and network mask for a manual binding to a DHCP
client. Address and Mask are valid IP addresses; each made up of four decimal bytes ranging
from 0 to 255. IP address 0.0.0.0 is invalid. The prefix-length is an integer from 0 to 32.
Default none
Format host address [mask | prefix-length]
Mode DHCP Pool Config
no host
This command removes the IP address of the DHCP client.
Format no host
Mode DHCP Pool Config
lease
This command configures the duration of the lease for an IP address that is assigned from a
DHCP server to a DHCP client. The overall lease time must be between 1–-86400 minutes. If
you specify infinite, the lease is set for 60 days. You can also specify a lease duration:
days is an integer from 0 to 59; hours is an integer from 0 to 23; minutes is an integer from
0 to 59.
Default 1 (day)
Format lease [{days [hours] [minutes] | infinite}]
Mode DHCP Pool Config
no lease
This command restores the default value of the lease time for DHCP Server.
Format no lease
Mode DHCP Pool Config
network (DHCP Pool Config)
Use this command to configure the subnet number and mask for a DHCP address pool on
the server. Network-number is a valid IP address, made up of four decimal bytes ranging
from 0 to 255. IP address 0.0.0.0 is invalid. Mask is the IP subnet mask for the specified
address pool. The prefix-length is an integer from 0 to 32.
Utility Commands 268

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default none
Format network networknumber [mask | prefixlength]
Mode DHCP Pool Config
no network
This command removes the subnet number and mask.
Format no network
Mode DHCP Pool Config
bootfile
The command specifies the name of the default boot image for a DHCP client. The
filename specifies the boot image file.
Format bootfile filename
Mode DHCP Pool Config
no bootfile
This command deletes the boot image name.
Format no bootfile
Mode DHCP Pool Config
domain-name
This command specifies the domain name of a Domain Name System (DNS) server for a
DHCP client when the DHCP server allocates an IP address to the client. That is, the domain
name is issued to the DHCP client, not to the switch.
The domain specifies the domain name for the DHCP client.
Default none
Format domain-name domain
Mode DHCP Pool Config
Utility Commands 269

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no domain-name
This command removes the domain name of a DNS server for a DHCP client.
Format no domain-name
Mode DHCP Pool Config
domain-name name
This command specifies the domain name of a DNS server that the switch sends to the
RADIUS server for authentication. Use this command in combination with the domain-name
enable command.
The name argument specifies the domain name.
Default none
Format domain-name name name
Mode Global Config
no domain-name name
This command removes the domain name of a DNS server that the switch sends to the
RADIUS server.
Format no domain-name name name
Mode Global Config
domain-name enable
This command enables the switch to send the domain name of a DNS server that you specify
with the domain-name name command to a RADIUIS server. By default, the switch sends
only the domain name of the DNS server. If you specify a user name with the optional name
keyword and name argument, the switch also sends the user name along with the domain
name to a RADIUS server. (The switch sends this information in the format
domain-name\username.)
Default Disabled
Format domain-name enable [name name]
Mode Global Config
Command example:
(NETGEAR Switch) (Config)#domain-name enable
(NETGEAR Switch) (Config)#exit
Utility Commands 270

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no domain-name enable
This command disables sending of the domain name of a DNS server (and, if configured, a
user name) to a RADIUS server.
Format no domain-name enable
Mode Global Config
netbios-name-server
This command configures NetBIOS Windows Internet Naming Service (WINS) name servers
that are available to DHCP clients.
One IP address is required, although one can specify up to eight addresses in one command
line. Servers are listed in order of preference (address1 is the most preferred server,
address2 is the next most preferred server, and so on).
Default none
Format netbios-name-server address [address2...address8]
Mode DHCP Pool Config
no netbios-name-server
This command removes the NetBIOS name server list.
Format no netbios-name-server
Mode DHCP Pool Config
netbios-node-type
The command configures the NetBIOS node type for Microsoft Dynamic Host Configuration
Protocol (DHCP) clients.type Specifies the NetBIOS node type. Valid types are:
• b-node. Broadcast
• p-node. Peer-to-peer
• m-node. Mixed
• h-node. Hybrid (recommended)
Default none
Format netbios-node-type type
Mode DHCP Pool Config
Utility Commands 271

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no netbios-node-type
This command removes the NetBIOS node Type.
Format no netbios-node-type
Mode DHCP Pool Config
next-server
This command configures the next server in the boot process of a DHCP client.The address
parameter is the IP address of the next server in the boot process, which is typically a TFTP
server.
Default inbound interface helper addresses
Format next-server address
Mode DHCP Pool Config
no next-server
This command removes the boot server list.
Format no next-server
Mode DHCP Pool Config
option
The option command configures DHCP Server options. The code parameter specifies the
DHCP option code and ranges from 1-254. The ascii string parameter specifies an NVT
ASCII character string. ASCII character strings that contain white space must be delimited by
quotation marks. The hex string parameter specifies hexadecimal data. In hexadecimal,
character strings are two hexadecimal digits. You can separate each byte by a period (for
example, a3.4f.22.0c), colon (for example, a3:4f:22:0c), or white space (for example,
a3 4f 22 0c).
Default none
Format option code {ascii string | hex string1 [string2...string8] | ip address1
[address2...address8]}
Mode DHCP Pool Config
Utility Commands 272

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no option
This command removes the DHCP Server options. The code parameter specifies the DHCP
option code.
Format no option code
Mode DHCP Pool Config
ip dhcp excluded-address
This command specifies the IP addresses that a DHCP server should not assign to DHCP
clients. Low-address and high-address are valid IP addresses; each made up of four decimal
bytes ranging from 0 to 255. IP address 0.0.0.0 is invalid.
Default none
Format ip dhcp excluded-address lowaddress [highaddress]
Mode Global Config
no ip dhcp excluded-address
This command removes the excluded IP addresses for a DHCP client. Low-address and
high-address are valid IP addresses; each made up of four decimal bytes ranging from 0 to
255. IP address 0.0.0.0 is invalid.
Format no ip dhcp excluded-address lowaddress [highaddress]
Mode Global Config
ip dhcp ping packets
Use this command to specify the number, in a range from 2–10, of packets a DHCP server
sends to a pool address as part of a ping operation. By default the number of packets sent to
a pool address is 2, which is the smallest allowed number when sending packets. Setting the
number of packets to 0 disables this command.
Default 2
Format ip dhcp ping packets number
Mode Global Config
no ip dhcp ping packets
This command restores the number of ping packets to the default value.
Format no ip dhcp ping packets
Mode Global Config
Utility Commands 273

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
service dhcp
This command enables the DHCP server.
Default disabled
Format service dhcp
Mode Global Config
no service dhcp
This command disables the DHCP server.
Format no service dhcp
Mode Global Config
ip dhcp bootp automatic
This command enables the allocation of the addresses to the bootp client. The addresses are
from the automatic address pool.
Default disabled
Format ip dhcp bootp automatic
Mode Global Config
no ip dhcp bootp automatic
This command disables the allocation of the addresses to the bootp client. The address are
from the automatic address pool.
Format no ip dhcp bootp automatic
Mode Global Config
ip dhcp conflict logging
This command enables conflict logging on DHCP server.
Default enabled
Format ip dhcp conflict logging
Mode Global Config
Utility Commands 274

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip dhcp conflict logging
This command disables conflict logging on DHCP server.
Format no ip dhcp conflict logging
Mode Global Config
clear ip dhcp binding
This command deletes an automatic address binding from the DHCP server database. If *
(the asterisk character) is specified, the bindings corresponding to all the addresses are
deleted. address is a valid IP address made up of four decimal bytes ranging from 0 to 255.
IP address 0.0.0.0 is invalid.
Format clear ip dhcp binding {address | *}
Mode Privileged EXEC
clear ip dhcp server statistics
This command clears DHCP server statistics counters.
Format clear ip dhcp server statistics
Mode Privileged EXEC
clear ip dhcp conflict
The command is used to clear an address conflict from the DHCP Server database. The
server detects conflicts using a ping. DHCP server clears all conflicts If * (the asterisk
character) is used as the address parameter.
Default none
Format clear ip dhcp conflict {address | *}
Mode Privileged EXEC
show ip dhcp binding
This command displays address bindings for the specific IP address on the DHCP server. If
no IP address is specified, the bindings corresponding to all the addresses are displayed.
Format show ip dhcp binding [address]
Modes Privileged EXEC
User EXEC
Utility Commands 275

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
IP address The IP address of the client.
Hardware Address The MAC Address or the client identifier.
Lease expiration The lease expiration time of the IP address assigned to the client.
Type The manner in which IP address was assigned to the client.
show ip dhcp global configuration
This command displays address bindings for the specific IP address on the DHCP server. If
no IP address is specified, the bindings corresponding to all the addresses are displayed.
Format show ip dhcp global configuration
Modes Privileged EXEC
User EXEC
Term Definition
Service DHCP The field to display the status of dhcp protocol.
Number of Ping The maximum number of Ping Packets that will be sent to verify that an ip address id not already
Packets assigned.
Conflict Logging Shows whether conflict logging is enabled or disabled.
BootP Automatic Shows whether BootP for dynamic pools is enabled or disabled.
show ip dhcp pool configuration
This command displays pool configuration. If all is specified, configuration for all the pools
is displayed.
Format show ip dhcp pool configuration {name | all}
Modes Privileged EXEC
User EXEC
Field Definition
Pool Name The name of the configured pool.
Pool Type The pool type.
Lease Time The lease expiration time of the IP address assigned to the client.
DNS Servers The list of DNS servers available to the DHCP client.
Default Routers The list of the default routers available to the DHCP client
Utility Commands 276

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The following additional field is displayed for Dynamic pool type.
Field Definition
Network The network number and the mask for the DHCP address pool.
The following additional fields are displayed for Manual pool type.
Field Definition
Client Name The name of a DHCP client.
Client Identifier The unique identifier of a DHCP client.
Hardware Address The hardware address of a DHCP client.
Hardware Address The protocol of the hardware platform.
Type
Host The IP address and the mask for a manual binding to a DHCP client.
show ip dhcp server statistics
This command displays DHCP server statistics.
Format show ip dhcp server statistics
Modes Privileged EXEC
User EXEC
Field Definition
Automatic Bindings The number of IP addresses that have been automatically mapped to the MAC addresses of hosts
that are found in the DHCP database.
Expired Bindings The number of expired leases.
Malformed The number of truncated or corrupted messages that were received by the DHCP server.
Bindings
Message Received.
Message Definition
DHCP DISCOVER The number of DHCPDISCOVER messages the server has received.
DHCP REQUEST The number of DHCPREQUEST messages the server has received.
DHCP DECLINE The number of DHCPDECLINE messages the server has received.
DHCP RELEASE The number of DHCPRELEASE messages the server has received.
DHCP INFORM The number of DHCPINFORM messages the server has received.
Utility Commands 277
