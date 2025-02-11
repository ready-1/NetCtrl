# cpu_queue_commands

Pages: 57-58

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
G - Assign IPv6 Gateway.
C - Add IPv6 address.
N - Skip this option and go to the next question.
Q - Quit.
? - Help.
(A/D/G/C/N/Q/?)? c
Current Management Interface Configuration
--------------------------------
Management Interface: L3 Management VLAN
Current management interface is L3 Management VLAN. What do you want to do?
O - Change to Out of Band port(service port).
V - Change to L3 Management VLAN.
N - Skip this option and go to the next question.
Q - Quit.
? - Help.
(O/V/N/Q/?)?n
Assigning System Name, System Location and System Contact to your switch management
Current Configuration
--------------------------------
System Name:
System Location:
System Contact:
Do you want to assign switch name and location information? (Y/N/Q)
CPU Queue Commands
You can send all packets with a specified destination address to a higher priority queue (5)
than the default queue for data packets and unicast packets to the CPU.
ip cpu-priority
This command sends all packets with a specified destination IPv4 address to a higher priority
queue (5) than the default queue for data packets and unicast packets to the CPU.
Format ip cpu-priority ip-address
Mode Privileged EXEC
Management Commands 57

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ip cpu-priority
This command removes all packets with a specified destination IPv4 address from the higher
priority queue.
Format no ip cpu-priority ip-address
Mode Privileged EXEC
ipv6 cpu-priority
The command allows all packets with a specified destination IPv6 address into a higher
priority queue (5) than the default queue for data packets and unicast packets to the CPU.
Format ip cpu-priority ipv6-address
Mode Privileged EXEC
no ipv6 cpu-priority
This command removes all packets with a specified destination IPv6 address from the higher
priority queue.
Format no ip cpu-priority ipv6-address
Mode Privileged EXEC
Management Interface Commands
This section describes the commands you use to configure a logical IPv4 interface for
management access.
enable (Privileged EXEC access)
This command gives you access to the Privileged EXEC mode. From the Privileged EXEC
mode, you can configure the network interface.
Format enable
Mode User EXEC
Management Commands 58
