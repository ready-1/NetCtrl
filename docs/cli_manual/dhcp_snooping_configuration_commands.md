# dhcp_snooping_configuration_commands

Pages: 545-548

## Content

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
