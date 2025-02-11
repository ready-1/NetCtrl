# dhcp_client_identifier_the_client_identifier_is_displayed_in_the_output_of_the_command_onl_16a86c65

Pages: 63-63

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
MAC Address Type The MAC address that must be used for in-band connectivity. The choices are the
burned in or the Locally Administered address. The factory default is to use the burned
in MAC address.
DHCPv6 Client DUID The DHCPv6 client’s unique client identifier. This row is displayed only when the
configured IPv6 protocol is DHCP.
IPv6 Autoconfig Mode Whether IPv6 Stateless address autoconfiguration is enabled or disabled.
DHCP Client Identifier The client identifier is displayed in the output of the command only if DHCP is enabled
with the client-id option on the management interface.
Command example:
(NETGEAR Switch) #show ip management
IPv4 Interface Status.......................... Up
IPv4 Management Interface...................... vlan 1
IP Address..................................... 169.254.100.100
Subnet Mask.................................... 255.255.255.0
Method......................................... DHCP
Routing Mode................................... Enable
Default Gateway................................ 0.0.0.0
Source Interface............................... vlan 1
Burned In MAC Address.......................... DC:EF:09:D3:2D:48
Locally Administered MAC address............... 00:00:00:00:00:00
MAC Address Type............................... Burned In
IPv6 Management Interface is not Configured.
show serviceport
This command displays service port configuration information.
Format show serviceport
Mode • Privileged EXEC
• User EXEC
Term Definition
Interface Status The network interface status. It is always considered to be up.
IP Address The IP address of the interface. The factory default value is 0.0.0.0.
Subnet Mask The IP subnet mask for this interface. The factory default value is 0.0.0.0.
Default Gateway The default gateway for this IP interface. The factory default value is 0.0.0.0.
Management Commands 63
