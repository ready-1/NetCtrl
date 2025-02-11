# radius_attribute_4_mode_a_global_parameter_to_indicate_whether_the_nas-ip-address_attribute_has_been

Pages: 153-153

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
RADIUS Attribute 4 Mode A global parameter to indicate whether the NAS-IP-Address attribute has been
enabled to use in RADIUS requests.
RADIUS Attribute 4 Value A global parameter that specifies the IP address to be used in the
NAS-IP-Address attribute to be used in RADIUS requests.
Command example:
(NETGEAR Switch) #show radius
Number of Configured Authentication Servers............. 32
Number of Configured Accounting Servers................. 32
Number of Named Authentication Server Groups............ 15
Number of Named Accounting Server Groups................ 3
Number of Retransmits................................... 4
Time Duration........................................... 10
RADIUS Accounting Mode.................................. Disable
RADIUS Attribute 4 Mode................................. Enable
RADIUS Attribute 4 Value ............................... 192.168.37.60
show radius servers
This command displays the summary and details of RADIUS authenticating servers
configured for the RADIUS client.
Format show radius servers [ipaddr | dnsname | name [servername]]
Mode Privileged EXEC
Field Description
ipaddr The IP address of the authenticating server.
dnsname The DNS name of the authenticating server.
servername The alias name to identify the server.
Current The * symbol preceding the server host address specifies that the server is currently active.
Host Address The IP address of the host.
Server Name The name of the authenticating server.
Port The port used for communication with the authenticating server.
Type Specifies whether this server is a primary or secondary type.
Current Host The IP address of the currently active authenticating server.
Address
Secret Configured Yes or No Boolean value that indicates whether this server is configured with a secret.
Management Commands 153
