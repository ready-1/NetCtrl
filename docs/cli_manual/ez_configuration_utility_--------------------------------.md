# ez_configuration_utility_--------------------------------

Pages: 54-56

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Configure the Switch Management CPU
To manage the switch over the web management interface or Telnet, you must assign an IP
address to the switch management CPU. You can accomplish this task through CLI
commands or you can use the ezconfig tool, which simplifies the task. The tool lets you
configure the following settings:
• The administrator user password and administrator-enable password
• The management CPU IP address and network mask
• The system name and location information
The tool is interactive and uses questions to guide you through the configuration steps. At the
end of the configuration session, the tool lets you save the information. To see which
information was changed by the ezconfig tool after a configuration session, issue the show
running-config command.
ezconfig
This command sets the IP address, subnet mask, and gateway of the switch. The IP address
and the gateway must be on the same subnet.
Format ezconfig
Mode Privileged EXEC
(NETGEAR Switch) #ezconfig
EZ Configuration Utility
--------------------------------
Hello and Welcome!
This utility will walk you thru assigning the IP address for the switch
management CPU. It will allow you to save the changes at the end. After
the session, simply use the newly assigned IP address to access the Web
GUI using any public domain Web browser.
Admin password is not defined.
D o y ou w ant t o a ssign t he a dmin p assword ( password l ength m ust b e i n r ange o f 8-64
characters) (Y/N/Q)? y
Enter new password:********
Confirm new password:********
The 'enable' password required for switch configuration via the command
line interface is currently not configured.
D o y ou w ant t o a ssign i t ( password l ength m ust b e i n r ange o f 8-64 characters) (Y/N/Q)?
y
Management Commands 54

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Enter new password:********
Confirm new password:********
Current IPv4 Management Interface: vlan 1
Do you want to set new Management VLAN ID (Y/N/Q)?y
VLAN ID: 1
Assigning an IPv4 address to your switch management
Current IPv4 Address Configuration
----------------------------------
Management VLAN ID: vlan 1
IPv4 Address Assignment Mode: None
IPv4 Address: 0.0.0.0
Subnet Mask: 0.0.0.0
Gateway: 0.0.0.0
Routing Mode: Enable
IPv4 address is not assigned. What do you want to do?
C - Configure IPv4 address manually.
D - Assign IPv4 address for the switch using DHCP Mode(current IPv4 address will be
lost).
N - Skip this option and go to the next question.
Q - Quit.
? - Help.
(C/D/N/Q/?)? c
IPv4 Address: 192.168.1.1
Network Mask: 255.255.255.0
Gateway: 192.168.254
Incorrect input! Gateway must be a valid IP address.
Try again (Y/N/Q)? y
Gateway: 192.168.1.254
Do you want to enable global routing (Y/N)?y
Current IPv6 Management Interface: (not configured)
Do you want to set new IPv6 Management VLAN ID (Y/N/Q)?y
VLAN ID: 1
Assigning management IPv6 address.
Current IPv6 Address Configuration
----------------------------------
IPv6 Address: fe80::abd:43ff:fe71:73c0/64
IPv6 Current state: TENT
Address DHCP Mode: Disabled
Address Autoconfigure Mode: Disabled
EUI64 : Enabled
Management Commands 55

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Routing Mode: Enable
IPv6 address has been assigned manually. What do you want to do?
C - Add IPv6 address.
D - Assign IPv6 address for the switch using DHCP Mode.
A - Assign IPv6 address for the switch using Auto Mode.
N - Skip this option and go to the next question.
Q - Quit.
? - Help.
(C/D/A/N/Q/?)? c
IPv6 Address: 2001:1::1
IPv6 Prefix-length: 64
IPv6 EUI64 flag (Y/N): n
IPv6 Gateway: 2001:1::fffe
Current Out of Band(service port) IPv4 Address Configuration
--------------------------------
IP Address Assignment Mode: DHCP
IP Address: 172.26.2.104
Subnet Mask: 255.255.255.0
Default Router: 172.26.2.1
IPv4 address will be assigned automatically by the DHCP server in your network. You
can disable DHCP mode and use static(fixed) IPv4 address. If fixed IPv4 Address Mode
is selected, DHCP Protocol Mode will be disabled, and you will be prompted to
set the values for the four fields above.
Do you want to assign IPv4 address manually? (Y/N/Q/?) y
IPv4 Address: 172.26.2.1
Network Mask: 255.255.255.0
Gateway: 172.26.2.254
Current Out of Band(Serviceport) IPv6 Address Configuration
--------------------------------
Service port IPv6 Address Mode: None
IPv6 Administrative Mode: Enabled
Service port IPv6 Address Mode autoconfigure: Disabled
IPv6 Address: fe80::abd:43ff:fe71:73be/64
Service port IPv6 address gateway:
EUI Flag: False
IPv6 address has been assigned manually. What do you want to do?
A - Assign IPv6 address for the switch using Auto Mode.
D - Assign IPv6 address for the switch using DHCP Mode.
Management Commands 56
