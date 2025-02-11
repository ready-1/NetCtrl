# network2_radius_server_1813_secondary

Pages: 154-154

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Description
Number of The configured value of the maximum number of times a request packet is retransmitted.
Retransmits
Message A global parameter to indicate whether the Message Authenticator attribute is enabled or disabled.
Authenticator
Time Duration The configured timeout value, in seconds, for request retransmissions.
RADIUS A global parameter to indicate whether the accounting mode for all the servers is enabled or not.
Accounting Mode
RADIUS Attribute 4 A global parameter to indicate whether the NAS-IP-Address attribute has been enabled to use in
Mode RADIUS requests.
RADIUS Attribute 4 A global parameter that specifies the IP address to be used in NAS-IP-Address attribute used in
Value RADIUS requests.
Command example:
(NETGEAR Switch) #show radius servers
Current Host Address Server Name Port Type
---- ------------------------ --------------------------------- ----- ----------
* 192.168.37.200 Network1_RADIUS_Server 1813 Primary
192.168.37.201 Network2_RADIUS_Server 1813 Secondary
192.168.37.202 Network3_RADIUS_Server 1813 Primary
192.168.37.203 Network4_RADIUS_Server 1813 Secondary
Command example:
(NETGEAR Switch) #show radius servers name
Current Host Address Server Name Type
------------------------ --------------------------------- ----------
192.168.37.200 Network1_RADIUS_Server Secondary
192.168.37.201 Network2_RADIUS_Server Primary
192.168.37.202 Network3_RADIUS_Server Secondary
192.168.37.203 Network4_RADIUS_Server Primary
Command example:
(NETGEAR Switch) #show radius servers name Default_RADIUS_Server
Server Name............................ Default_RADIUS_Server
Host Address........................... 192.168.37.58
Secret Configured...................... No
Message Authenticator ................. Enable
Number of Retransmits.................. 4
Time Duration.......................... 10
RADIUS Accounting Mode................. Disable
RADIUS Attribute 4 Mode................ Enable
RADIUS Attribute 4 Value .............. 192.168.37.60
Management Commands 154
