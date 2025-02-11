# dhcp_server_commands_this_section_describes_the_commands_you_to_configure_the_dhcp_server__9c767f3a

Pages: 265-266

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Begins on second Sunday of Nov at 03:18
Ends on second Monday of Nov at 03:18
Offset is 120 minutes
Summer-time is in effect.
DHCP Server Commands
This section describes the commands you to configure the DHCP server settings for the
switch. DHCP uses UDP as its transport protocol and supports a number of features that
facilitate in administration address allocations.
ip dhcp pool
This command configures a DHCP address pool name on a DHCP server and enters DHCP
pool configuration mode.
Default none
Format ip dhcp pool name
Mode Global Config
no ip dhcp pool
This command removes the DHCP address pool. The name should be previously configured
pool name.
Format no ip dhcp pool name
Mode Global Config
client-identifier
This command specifies the unique identifier for a DHCP client. Unique-identifier is a valid
notation in hexadecimal format. In some systems, such as Microsoft® DHCP clients, the
client identifier is required instead of hardware addresses. The unique-identifier is a
concatenation of the media type and the MAC address. For example, the Microsoft client
identifier for Ethernet address c819.2488.f177 is 01c8.1924.88f1.77 where 01 represents the
Ethernet media type. For more information, refer to the “Address Resolution Protocol
Parameters” section of RFC 1700, Assigned Numbers for a list of media type codes.
Default none
Format client-identifier uniqueidentifier
Mode DHCP Pool Config
Utility Commands 265

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no client-identifier
This command deletes the client identifier.
Format no client-identifier
Mode DHCP Pool Config
client-name
This command specifies the name for a DHCP client. Name is a string consisting of standard
ASCII characters.
Default none
Format client-name name
Mode DHCP Pool Config
no client-name
This command removes the client name.
Format no client-name
Mode DHCP Pool Config
default-router
This command specifies the default router list for a DHCP client. address1, address2…
address8 are valid IP addresses, each made up of four decimal bytes ranging from 0 to
255. IP address 0.0.0.0 is invalid.
Default none
Format default-router address1 [address2....address8]
Mode DHCP Pool Config
no default-router
This command removes the default router list.
Format no default-router
Mode DHCP Pool Config
Utility Commands 266
