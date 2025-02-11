# m_ac_address_ip_address_type_v_lan_interface_-_----------------_---------------_----------_d56b350b

Pages: 554-558

## Content

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
