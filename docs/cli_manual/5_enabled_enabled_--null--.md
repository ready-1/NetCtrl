# 5 Enabled Enabled --NULL--

Pages: 543-558

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show dhcp l2relay agent-option vlan 5-10
DHCP L2 Relay is Enabled.
V LAN Id L 2 Relay C ircuitId RemoteId
--------- ---------- - ---------- ------------
5 Enabled Enabled --NULL--
6 Enabled Enabled NETGEAR
7 Enabled Disabled --NULL--
8 Enabled Disabled --NULL--
9 Enabled Disabled --NULL--
10 Enabled Disabled --NULL--
show dhcp l2relay vlan
This command displays DHCP vlan configuration.
Format show dhcp l2relay vlan vlan-list
Mode Privileged EXEC
Parameter Description
vlan-list Enter VLAN IDs in the range 1–4093. Use a dash (–) to specify a range or a comma (,) to separate
VLAN IDs in a list. Spaces and zeros are not permitted.
clear dhcp l2relay statistics interface
Use this command to reset the DHCP L2 relay counters to zero. Specify the port with the
counters to clear, or use the all keyword to clear the counters on all ports.
Format clear dhcp l2relay statistics interface {unit/slot/port | all}
Mode Privileged EXEC
DHCP Client Commands
The switch can include vendor and configuration information in DHCP client requests relayed
to a DHCP server. This information is included in DHCP Option 60, Vendor Class Identifier.
The information is a string of 128 octets.
Switching Commands 543

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
dhcp client vendor-id-option
This command enables the inclusion of DHCP Option-60, Vendor Class Identifier included in
the requests transmitted to the DHCP server by the DHCP client operating in the switch.
Format dhcp client vendor-id-option string
Mode Global Config
no dhcp client vendor-id-option
This command disables the inclusion of DHCP Option-60, Vendor Class Identifier included in
the requests transmitted to the DHCP server by the DHCP client operating in the switch.
Format no dhcp client vendor-id-option
Mode Global Config
dhcp client vendor-id-option-string
This parameter sets the DHCP Vendor Option-60 string to be included in the requests
transmitted to the DHCP server by the DHCP client operating in the switch.
Format dhcp client vendor-id-option-string string
Mode Global Config
no dhcp client vendor-id-option-string
This parameter clears the DHCP Vendor Option-60 string.
Format no dhcp client vendor-id-option-string
Mode Global Config
show dhcp client vendor-id-option
This command displays the configured administration mode of the vendor-id-option and the
vendor-id string to be included in Option-43 in DHCP requests.
Format show dhcp client vendor-id-option
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show dhcp client vendor-id-option
DHCP Client Vendor Identifier Option........... Enabled
DHCP Client Vendor Identifier Option String.... NetgearClient
Switching Commands 544

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
DHCP Snooping Configuration Commands
This section describes commands you use to configure DHCP Snooping.
ip dhcp snooping
Use this command to enable DHCP Snooping globally.
Default Disabled
Format ip dhcp snooping
Mode Global Config
no ip dhcp snooping
Use this command to disable DHCP Snooping globally.
Format no ip dhcp snooping
Mode Global Config
ip dhcp snooping vlan
Use this command to enable DHCP Snooping on a list of comma-separated VLAN ranges.
Default Disabled
Format ip dhcp snooping vlan vlan-list
Mode Global Config
no ip dhcp snooping vlan
Use this command to disable DHCP Snooping on VLANs.
Format no ip dhcp snooping vlan vlan-list
Mode Global Config
ip dhcp snooping verify mac-address
Use this command to enable verification of the source MAC address with the client hardware
address in the received DCHP message.
Default Enabled
Format ip dhcp snooping verify mac-address
Mode Global Config
Switching Commands 545

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip dhcp snooping verify mac-address
Use this command to disable verification of the source MAC address with the client hardware
address.
Format no ip dhcp snooping verify mac-address
Mode Global Config
ip dhcp snooping database
Use this command to configure the persistent location of the DHCP Snooping database. This
can be local or a remote file on a given IP machine.
Default Local
Format ip dhcp snooping database {local | tftp://hostIP/filename}
Mode Global Config
ip dhcp snooping database write-delay (DHCP)
Use this command to configure the interval in seconds at which the DHCP Snooping
database persists. The interval value ranges from 15 to 86400 seconds.
Default 300 seconds
Format ip dhcp snooping database write-delay seconds
Mode Global Config
no ip dhcp snooping database write-delay
Use this command to set the write delay value to the default value.
Format no ip dhcp snooping database write-delay
Mode Global Config
ip dhcp snooping binding
Use this command to configure static DHCP Snooping binding.
Format ip dhcp snooping binding mac-address vlan vlan-id ipaddress interface
interface-id
Mode Global Config
Switching Commands 546

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip dhcp snooping binding
Use this command to remove the DHCP static entry from the DHCP Snooping database.
Format no ip dhcp snooping binding mac-address
Mode Global Config
ip verify binding
Use this command to configure static IP source guard (IPSG) entries.
Format ip verify binding mac-address vlan vlan-id ipaddress interface interface-id
Mode Global Config
no ip verify binding
Use this command to remove the IPSG static entry from the IPSG database.
Format no ip verify binding mac-address vlan vlan-id ipaddress interface
interface-id
Mode Global Config
ip dhcp snooping limit
Use this command to control the rate at which the DHCP Snooping messages come on an
interface or range of interfaces. By default, rate limiting is disabled. When enabled, the rate
can range from 0 to 300 packets per second (pps). The burst level range is 1 to 15 seconds.
Default Disabled (no limit)
Format ip dhcp snooping limit {rate pps [burst interval seconds]}
Mode Interface Config
no ip dhcp snooping limit
Use this command to set the rate at which the DHCP Snooping messages come, and the
burst level, to the defaults.
Format no ip dhcp snooping limit
Mode Interface Config
Switching Commands 547

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip dhcp snooping log-invalid
Use this command to control the logging DHCP messages filtration by the DHCP Snooping
application. This command can be used to configure a single interface or a range of
interfaces.
Default Disabled
Format ip dhcp snooping log-invalid
Mode Interface Config
no ip dhcp snooping log-invalid
Use this command to disable the logging DHCP messages filtration by the DHCP Snooping
application.
Format no ip dhcp snooping log-invalid
Mode Interface Config
ip dhcp snooping trust
Use this command to configure an interface or range of interfaces as trusted.
Default Disabled
Format ip dhcp snooping trust
Mode Interface Config
no ip dhcp snooping trust
Use this command to configure the port as untrusted.
Format no ip dhcp snooping trust
Mode Interface Config
ip verify source
Use this command to configure the IPSG source ID attribute to filter the data traffic in the
hardware. Source ID is the combination of IP address and MAC address. Normal command
allows data traffic filtration based on the IP address. With the port-security option, the
data traffic will be filtered based on the IP and MAC addresses.
Switching Commands 548

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
This command can be used to configure a single interface or a range of interfaces.
Default The source ID is the IP address
Format ip verify source [port-security]
Mode Interface Config
no ip verify source
Use this command to disable the IPSG configuration in the hardware. You cannot disable
port-security alone if it is configured.
Format no ip verify source
Mode Interface Config
show ip dhcp snooping
Use this command to display the DHCP Snooping global configurations and per port
configurations.
Format show ip dhcp snooping
Mode Privileged EXEC
User EXEC
Term Definition
Interface The interface for which data is displayed.
Trusted If it is enabled, DHCP snooping considers the port as trusted. The factory default is disabled.
Log Invalid Pkts If it is enabled, DHCP snooping application logs invalid packets on the specified interface.
Command example:
(NETGEAR Switch) #show ip dhcp snooping
DHCP snooping is Disabled
DHCP snooping source MAC verification is enabled
DHCP snooping is enabled on the following VLANs:
11 - 30, 40
Interface Trusted Log Invalid Pkts
--------- -------- ----------------
0/1 Yes No
0 /2 No Yes
0 /3 No Yes
0/4 No No
0/6 No No
Switching Commands 549

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show ip dhcp snooping binding
Use this command to display the DHCP Snooping binding entries. To restrict the output, use
the following options:
• static. Restrict the output based on static entries.
• dynamic. Restrict the output based on DCHP snooping.
• interface unit/slot/port. Restrict the output based on a specific interface.
• vlan-id. Restrict the output based on a VLAN.
Format show ip dhcp snooping binding [static | dynamic] [interface unit/slot/port]
[vlan-id]
Mode Privileged EXEC
User EXEC
Term Definition
MAC Address Displays the MAC address for the binding that was added. The MAC address is the key to the
binding database.
IP Address Displays the valid IP address for the binding rule.
VLAN The VLAN for the binding rule.
Interface The interface to add a binding into the DHCP snooping interface.
Type Binding type; statically configured from the CLI or dynamically learned.
Lease (sec) The remaining lease time for the entry.
Command example:
(NETGEAR Switch) #show ip dhcp snooping binding
Total number of bindings: 2
MAC Address IP Address VLAN Interface Type Lease time (Secs)
------------------ ------------ ---- --------- ---- ------------------
00:02:B3:06:60:80 210.1.1.3 10 0/1 86400
00:0F:FE:00:13:04 210.1.1.4 10 0/1 86400
show ip dhcp snooping database
Use this command to display the DHCP Snooping configuration related to the database
persistency.
Format show ip dhcp snooping database
Mode Privileged EXEC
User EXEC
Switching Commands 550

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Agent URL Bindings database agent URL.
Write Delay The maximum write time to write the database into local or remote.
Command example:
(NETGEAR Switch) #show ip dhcp snooping database
agent url: /10.131.13.79:/sai1.txt
write-delay: 5000
show ip dhcp snooping interfaces
Use this command to show the DHCP Snooping status of the interfaces.
Format show ip dhcp snooping interfaces
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show ip dhcp snooping interfaces
Interface Trust State Rate Limit Burst Interval
(pps) (seconds)
----------- ---------- ---------- --------------
1/0/1 No 1 5 1
1 /0/2 No 1 5 1
1/0/3 N o 15 1
Command example:
(NETGEAR Switch) #show ip dhcp snooping interfaces ethernet 1/0/15
Interface Trust State Rate Limit Burst Interval
(pps) (seconds)
----------- ---------- ---------- --------------
1 /0/15 Yes 15 1
show ip dhcp snooping statistics
Use this command to list statistics for DHCP Snooping security violations on untrusted ports.
Format show ip dhcp snooping statistics
Mode Privileged EXEC
User EXEC
Switching Commands 551

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Interface The IP address of the interface in unit/slot/port format.
MAC Verify Represents the number of DHCP messages that were filtered on an untrusted interface because of
Failures source MAC address and client HW address mismatch.
Client Ifc Mismatch Represents the number of DHCP release and Deny messages received on the different ports than
learned previously.
DHCP Server Msgs Represents the number of DHCP server messages received on Untrusted ports.
Rec’d
Command example:
(NETGEAR Switch) #show ip dhcp snooping statistics
Interface MAC Verify Client Ifc DHCP Server
Failures Mismatch Msgs Rec'd
----------- ---------- ---------- -----------
1/0/2 0 0 0
1/0/3 0 0 0
1/0/4 0 0 0
1/0/5 0 0 0
1/0/6 0 0 0
1/0/7 0 0 0
1/0/8 0 0 0
1/0/9 0 0 0
1/0/10 0 0 0
1/0/11 0 0 0
1/0/12 0 0 0
1/0/13 0 0 0
1/0/14 0 0 0
1/0/15 0 0 0
1/0/16 0 0 0
1/0/17 0 0 0
1/0/18 0 0 0
1/0/19 0 0 0
1/0/20 0 0 0
clear ip dhcp snooping binding
Use this command to clear all DHCP Snooping bindings on all interfaces or on a specific
interface.
Format clear ip dhcp snooping binding [interface unit/slot/port]
Mode Privileged EXEC
User EXEC
Switching Commands 552

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
clear ip dhcp snooping statistics
Use this command to clear all DHCP Snooping statistics.
Format clear ip dhcp snooping statistics
Mode Privileged EXEC
User EXEC
show ip verify source
Use this command to display the IPSG configurations on all ports.
Format show ip verify source
Mode Privileged EXEC
User EXEC
Term Definition
Interface Interface address in unit/slot/port format.
Filter Type Is one of two values:
ip-mac: User has configured MAC address filtering on this interface.
ip: Only IP address filtering on this interface.
IP Address IP address of the interface
MAC Address If MAC address filtering is not configured on the interface, the MAC Address field is empty. If port
security is disabled on the interface, then the MAC Address field displays “permit-all.”
VLAN The VLAN for the binding rule.
Command example:
(NETGEAR Switch) #show ip verify source
Interface Filter Type IP Address MAC Address Vlan
--------- ----------- --------------- ----------------- -----
0/1 ip-mac 210.1.1.3 00:02:B3:06:60:80 10
0/1 ip-mac 210.1.1.4 00:0F:FE:00:13:04 10
show ip verify interface
Use this command to display the IPSG filter type for a specific interface.
Format show ip verify interface unit/slot/port
Mode Privileged EXEC
User EXEC
Switching Commands 553

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Interface Interface address in unit/slot/port format.
Filter Type Is one of two values:
ip-mac: User has configured MAC address filtering on this interface.
ip: Only IP address filtering on this interface.
show ip source binding
Use this command to display the IPSG bindings.
Format show ip source binding [dhcp-snooping | static] [interface unit/slot/port]
[vlan-id]
Mode Privileged EXEC
User EXEC
Term Definition
MAC Address The MAC address for the entry that is added.
IP Address The IP address of the entry that is added.
Type Entry type; statically configured from CLI or dynamically learned from DHCP Snooping.
VLAN VLAN for the entry.
Interface IP address of the interface in unit/slot/port format.
Command example:
(NETGEAR Switch) #show ip source binding
M AC Address IP Address Type V lan Interface
- ---------------- --------------- ------------- ----- -------------
0 0:00:00:00:00:08 1.2.3.4 dhcp-snooping 2 1/0/1
0 0:00:00:00:00:09 1.2.3.4 dhcp-snooping 3 1/0/1
0 0:00:00:00:00:0A 1.2.3.4 dhcp-snooping 4 1/0/1
Dynamic ARP Inspection Commands
Dynamic ARP Inspection (DAI) is a security feature that rejects invalid and malicious ARP
packets. DAI prevents a class of man-in-the-middle attacks, where an unfriendly station
intercepts traffic for other stations by poisoning the ARP caches of its unsuspecting
neighbors. The miscreant sends ARP requests or responses mapping another station’s IP
address to its own MAC address.
Switching Commands 554

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
DAI relies on DHCP snooping. DHCP snooping listens to DHCP message exchanges and
builds a binding database of valid MAC addresses, IP addresses, VLANs, and interfaces.
When DAI is enabled, the switch drops ARP packets whose sender MAC address and
sender IP address do not match an entry in the DHCP snooping bindings database. You can
optionally configure additional ARP packet validation.
ip arp inspection vlan
Use this command to enable Dynamic ARP Inspection on a list of comma-separated VLAN
ranges.
Default Disabled
Format ip arp inspection vlan vlan-list
Mode Global Config
no ip arp inspection vlan
Use this command to disable Dynamic ARP Inspection on a list of comma-separated VLAN
ranges.
Format no ip arp inspection vlan vlan-list
Mode Global Config
ip arp inspection validate
Use this command to enable additional validation checks like source-mac (src-mac)
validation, destination-mac (dst-mac) validation, and IP address validation on the received
ARP packets. Each command overrides the configuration of the previous command. For
example, if a command enables source-mac and destination-mac validations, and a second
command enables IP validation only, the source-mac and destination-mac validations are
disabled as a result of the second command.
Default Disabled
Format ip arp inspection validate {[src-mac] [dst-mac] [ip]}
Mode Global Config
no ip arp inspection validate
Use this command to disable the additional validation checks on the received ARP packets.
Format no ip arp inspection validate {[src-mac] [dst-mac] [ip]}
Mode Global Config
Switching Commands 555

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip arp inspection vlan logging
Use this command to enable logging of invalid ARP packets on a list of comma-separated
VLAN ranges.
Default Enabled
Format ip arp inspection vlan vlan-list logging
Mode Global Config
no ip arp inspection vlan logging
Use this command to disable logging of invalid ARP packets on a list of comma-separated
VLAN ranges.
Format no ip arp inspection vlan vlan-list logging
Mode Global Config
ip arp inspection trust
Use this command to configure an interface or range of interfaces as trusted for Dynamic
ARP Inspection.
Default Disabled
Format ip arp inspection trust
Mode Interface Config
no ip arp inspection trust
Use this command to configure an interface as untrusted for Dynamic ARP Inspection.
Format no ip arp inspection trust
Mode Interface Config
ip arp inspection limit
Use this command to configure the rate limit and burst interval values for an interface or
range of interfaces. Configuring none for the limit means the interface is not rate limited for
Dynamic ARP Inspections. The maximum pps value shown in the range for the rate option
might be more than the hardware allowable limit. Therefore you need to understand the
switch performance and configure the maximum rate pps accordingly.
Switching Commands 556

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: The user interface accepts a rate limit for a trusted interface, but the
limit is not enforced unless the interface is configured to be untrusted.
Default 15 pps for rate and 1 second for burst-interval.
Format ip arp inspection limit {rate pps [burst interval seconds] | none}
Mode Interface Config
no ip arp inspection limit
Use this command to set the rate limit and burst interval values for an interface to the default
values of 15 pps and 1 second, respectively.
Format no ip arp inspection limit
Mode Interface Config
ip arp inspection filter
Use this command to configure the ARP ACL used to filter invalid ARP packets on a list of
comma-separated VLAN ranges. If the static keyword is given, packets that do not match a
permit statement are dropped without consulting the DHCP snooping bindings.
Default No ARP ACL is configured on a VLAN.
Format ip arp inspection filter acl-name vlan vlan-list [static]
Mode Global Config
no ip arp inspection filter
Use this command to unconfigure the ARP ACL used to filter invalid ARP packets on a list of
comma-separated VLAN ranges.
Format no ip arp inspection filter acl-name vlan vlan-list [static]
Mode Global Config
arp access-list
Use this command to create an ARP ACL.
Format arp access-list acl-name
Mode Global Config
Switching Commands 557

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no arp access-list
Use this command to delete a configured ARP ACL.
Format no arp access-list acl-name
Mode Global Config
permit ip host mac host
Use this command to configure a rule for a valid IP address and MAC address combination
used in ARP packet validation.
Format permit ip host sender-ipaddress mac host sender-mac
Mode ARP Access-list Config
no permit ip host mac host
Use this command to delete a rule for a valid IP and MAC combination.
Format no permit ip host sender-ipaddress mac host sender-mac
Mode ARP Access-list Config
show ip arp inspection
Use this command to display the Dynamic ARP Inspection global configuration and
configuration on all the VLANs. With the vlan keyword and vlan-list argument (that is,
comma separated VLAN ranges), the command displays the global configuration and
configuration on all the VLANs in the given VLAN list. For the vlan-list argument, you
can enter a list of VLANs (for example, 12-18 or 12,14) to display the statistics on all
DAI-enabled VLANs in the list, or enter a single VLAN to display the statistics for only that
VLAN. The global configuration includes the source mac validation, destination mac
validation and invalid IP validation information.
Format show ip arp inspection [vlan vlan-list]
Mode Privileged EXEC
User EXEC
Term Definition
Source MAC Displays whether Source MAC Validation of ARP frame is enabled or disabled.
Validation
Destination MAC Displays whether Destination MAC Validation is enabled or disabled.
Validation
Switching Commands 558
