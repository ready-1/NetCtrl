# dns_client_commands

Pages: 278-283

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Message Sent.
Message Definition
DHCP OFFER The number of DHCPOFFER messages the server sent.
DHCP ACK The number of DHCPACK messages the server sent.
DHCP NACK The number of DHCPNACK messages the server sent.
show ip dhcp conflict
This command displays address conflicts logged by the DHCP Server. If no IP address is
specified, all the conflicting addresses are displayed.
Format show ip dhcp conflict [ip-address]
Modes Privileged EXEC
User EXEC
Term Definition
IP address The IP address of the host as recorded on the DHCP server.
Detection Method The manner in which the IP address of the hosts were found on the DHCP Server.
Detection time The time when the conflict was found.
DNS Client Commands
These commands are used in the Domain Name System (DNS), an Internet directory
service. DNS is how domain names are translated into IP addresses. When enabled, the
DNS client provides a hostname lookup service to other components.
ip domain lookup
Use this command to enable the DNS client.
Default enabled
Format ip domain lookup
Mode Global Config
Utility Commands 278

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip domain lookup
Use this command to disable the DNS client.
Format no ip domain lookup
Mode Global Config
ip domain name
Use this command to define a default domain name that the switch uses to complete
unqualified host names (names with a domain name). By default, no default domain name is
configured in the system. name cannot be longer than 2 55 characters and cannot include an
initial period. name should be used only when the default domain name list, configured using
the ip domain list command, is empty.
Default none
Format ip domain name name
Mode Global Config
The CLI command ip domain name yahoo.com configures yahoo.com as a default
domain name. For an unqualified hostname xxx, a DNS query is made to find the IP address
corresponding to xxx.yahoo.com.
no ip domain name
Use this command to remove the default domain name configured using the ip domain name
command.
Format no ip domain name
Mode Global Config
ip domain list
Use this command to define a list of default domain names to complete unqualified names.
By default, the list is empty. Each name must be no more than 256 characters, and should
not include an initial period. The default domain name, configured using the ip domain
name command, is used only when the default domain name list is empty. A maximum of 32
names can be entered in to this list.
Default none
Format ip domain list name
Mode Global Config
Utility Commands 279

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip domain list
Use this command to delete a name from a list.
Format no ip domain list name
Mode Global Config
ip name server
Use this command to configure the available name servers. Up to eight servers can be
defined in one command or by using multiple commands. The parameter server-address
is a valid IPv4 or IPv6 address of the server. The preference of the servers is determined by
the order they were entered.
Format ip name-server server-address1 [server-address2...server-address8]
Mode Global Config
no ip name server
Use this command to remove a name server.
Format no ip name-server [server-address1...server-address8]
Mode Global Config
ip name source-interface
Use this command to specify the physical or logical interface to use as the DNS client (IP
name) source interface (source IP address) for the DNS client management application. If
configured, the address of source Interface is used for all DNS communications between the
DNS server and the DNS client. The selected source-interface IP address is used for filling
the IP header of management protocol packets. This allows security devices (firewalls) to
identify the source packets coming from the specific switch. If a source-interface is not
specified, the primary IP address of the originating (outbound) interface is used as the source
address. If the configured interface is down, the DNS client falls back to its default behavior.
Format ip name source-interface {unit/slot/port | loopback loopback-id | tunnel
tunnel-id | vlan vlan-id}
Mode Global Config
no ip name source-interface
Use this command to reset the DNS source interface to the default settings.
Format no ip name source-interface
Mode Global Config
Utility Commands 280

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip host
Use this command to define static host name-to-address mapping in the host cache. The
parameter name is host name and ipaddress is the IP address of the host. The host name
can include 1–255 alphanumeric characters, periods, hyphens, underscores, and
non-consecutive spaces. Hostnames that include one or more space must be enclosed in
quotation marks, for example “lab-pc 45”.
Default none
Format ip host name ipaddress
Mode Global Config
no ip host
Use this command to remove the name-to-address mapping.
Format no ip host name
Mode Global Config
ipv6 host
Use this command to define static host name-to-IPv6 address mapping in the host cache.
The parameter name is host name and v6 address is the IPv6 address of the host. The
host name can include 1–255 alphanumeric characters, periods, hyphens, and spaces. Host
names that include one or more space must be enclosed in quotation marks, for example
“lab-pc 45”.
Default none
Format ipv6 host name v6 address
Mode Global Config
no ipv6 host
Use this command to remove the static host name-to-IPv6 address mapping in the host
cache.
Format no ipv6 host name
Mode Global Config
Utility Commands 281

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip domain retry
Use this command to specify the number of times to retry sending Domain Name System
(DNS) queries. The number argument indicates the number of times to retry sending a DNS
query to the DNS server. This number is in the range from 0 to 100.
Default 2
Format ip domain retry number
Mode Global Config
no ip domain retry
Use this command to return to the default.
Format no ip domain retry
Mode Global Config
ip domain timeout
Use this command to specify the amount of time to wait for a response to a DNS query. The
parameter seconds specifies the time, in seconds, to wait for a response to a DNS query.
The parameter seconds ranges from 0 to 3600.
Default 3
Format ip domain timeout seconds
Mode Global Config
no ip domain timeout
Use this command to return to the default setting.
Format no ip domain timeout
Mode Global Config
clear host
Use this command to delete entries from the host name-to-address cache. This command
clears the entries from the DNS cache maintained by the software. This command clears
both IPv4 and IPv6 entries.
Format clear host {name | all}
Mode Privileged EXEC
Utility Commands 282

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Description
name A particular host entry to remove. The parameter name ranges from 1-255 characters.
all Removes all entries.
show hosts
Use this command to display the default domain name, a list of name server hosts, the static
and the cached list of host names and addresses. The parameter name ranges from 1-255
characters. This command displays both IPv4 and IPv6 entries.
Format show hosts [name]
Mode Privileged Exec
User EXEC
Field Description
Host Name Domain host name.
Default Domain Default domain name.
Default Domain List Default domain list.
Domain Name DNS client enabled/disabled.
Lookup
Number of Retries Number of time to retry sending Domain Name System (DNS) queries.
Retry Timeout Amount of time to wait for a response to a DNS query.
Period
Name Servers Configured name servers.
DNS Client Source Shows the configured source interface (source IP address) used for a DNS client. The IP address of
Interface the selected interface is used as source IP for all communications with the server.
Command example:
(NETGEAR Switch) show hosts
Host name......................... Device
Default domain.................... gm.com
Default domain list............... yahoo.com, Stanford.edu, rediff.com
Domain Name lookup................ Enabled
Number of retries................. 5
Retry timeout period.............. 1500
Name servers (Preference order)... 176.16.1.18 176.16.1.19
DNS Client Source Interface....... (not configured)
Utility Commands 283
