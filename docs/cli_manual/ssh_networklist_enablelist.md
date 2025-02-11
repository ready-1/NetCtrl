# ssh_networklist_enablelist

Pages: 474-475

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show authentication methods
Use this command to display information about the authentication methods.
Format show authentication methods
Mode Privileged EXEC
Term Definition
Authentication Login List The authentication login listname.
Method 1 The first method in the specified authentication login list, if any.
Method 2 The second method in the specified authentication login list, if any.
Method 3 The third method in the specified authentication login list, if any.
Command example:
(NETGEAR Switch)#show authentication methods
Login Authentication Method Lists
---------------------------------
defaultList : local
networkList : local
Enable Authentication Method Lists
----------------------------------
enableList : enable none
enableNetList : enable deny
Line Login Method List Enable Method List
------- ----------------- ------------------
Console defaultList enableList
Telnet networkList enableList
SSH networkList enableList
HTTPS :local
HTTP :local
DOT1X :
show authentication statistics
Use this command to display the authentication statistics for an interface.
Format show authentication statistics unit/slot/port
Mode Privileged EXEC
Switching Commands 474

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The following information is displayed for each interface.
Term Definition
Port The port for which information is displayed.
802.1X attempts The number of Dot1x authentication attempts for the port.
802.1X failed attempts The number of failed Dot1x authentication attempts for the port.
Mab attempts The number of MAB (MAC authentication bypass) authentication attempts for the port.
Mab failed attempts The number of failed MAB authentication attempts for the port.
Captive-portal attempts The number of captive portal (Web authorization) authentication attempts for the port.
Captive-portal failed attempts The number of failed captive portal authentication attempts for the port.
Command example:
(NETGEAR Switch) #show authentication statistics 1/0/1
Port........................................... 1/0/1
802.1X attempts................................ 0
802.1X failed attempts......................... 0
Mab attempts................................... 0
Mab failed attempts............................ 0
Captive-portal attempts........................ 0
Captive-Portal failed attempts................. 0
clear authentication statistics
Use this command to clear the authentication statistics on an interface.
Format clear authentication statistics {unit/slot/port] | all}
Mode Privileged EXEC
clear authentication authentication-history
Use this command to clear the authentication history log for an interface.
Format clear authentication authentication-history {unit/slot/port | all}
Mode Privileged EXEC
show dot1x
This command is used to show a summary of the global dot1x configuration, summary
information of the dot1x configuration for a specified port or all ports, the detailed dot1x
configuration for a specified port and the dot1x statistics for a specified port, depending on
the tokens used.
Switching Commands 475
