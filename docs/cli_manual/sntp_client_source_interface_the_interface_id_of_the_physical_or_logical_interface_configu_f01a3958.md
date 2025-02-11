# sntp_client_source_interface_the_interface_id_of_the_physical_or_logical_interface_configu_f01a3958

Pages: 260-261

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
For each configured server.
Term Definition
IP Address / Hostname IP address or hostname of configured SNTP Server.
Address Type Address Type of configured SNTP server (IPv4, IPv6, or DNS).
Priority IP priority type of the configured server.
Version SNTP Version number of the server. The protocol version used to query the server in
unicast mode.
Port Server Port Number.
Last Attempt Time Last server attempt time for the specified server.
Last Update Status Last server attempt status for the server.
Total Unicast Requests Number of requests to the server.
Failed Unicast Requests Number of failed requests from server.
show sntp source-interface
Use this command to display the SNTP client source interface configured on the switch.
Format show sntp source-interface
Mode Privileged EXEC
Field Description
SNTP Client Source Interface The interface ID of the physical or logical interface configured as the SNTP client source
interface.
SNTP Client Source IPv4 The IP address of the interface configured as the SNTP client source interface.
Address
Command example:
(NETGEAR Switch) #show sntp source-interface
SNTP Client Source Interface................... (not configured)
Utility Commands 260

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Time Zone Commands
Use the Time Zone commands to configure system time and date, Time Zone and Summer
Time (that is, Daylight Saving Time). Summer time can be recurring or non-recurring.
clock set
This command sets the system time and date.
Format clock set hh:mm:ss
clock set mm/dd/yyyy
Mode Global Config
Parameter Description
hh:mm:ss Enter the current system time in 24-hour format in hours, minutes, and seconds. The range is hours:
0 to 23, minutes: 0 to 59, seconds: 0 to 59.
mm/dd/yyyy Enter the current system date the format month, day, year. The range for month is 1 to 12. The range
for the day of the month is 1 to 31. The range for year is 2010 to 2079.
Command example:
(NETGEAR Switch) (Config)# clock set 03:17:00
(NETGEAR Switch) (Config)# clock set 11/01/2011
clock summer-time date
Use the clock summer-time date command to set the summer-time offset to Coordinated
Universal Time (UTC). If the optional parameters are not specified, they are read as either 0
or \0, as appropriate.
Format clock summer-time date {date month year hh:mm date month year hh:mm}[offset
offset] [zone acronym]
Mode Global Config
Parameter Description
date Day of the month. Range is 1 to 31.
month Month. Range is the first three letters by name; jan, for example.
year Year. The range is 2000 to 2097.
hh:mm Time in 24-hour format in hours and minutes. The range is hours: 0 to 23, minutes: 0 to 59.
Utility Commands 261
