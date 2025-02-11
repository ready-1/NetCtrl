# eu_the_system_clock_uses_the_standard_recurring_summer_time_settings_used_in_countries_in_the

Pages: 262-264

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
offset The number of minutes to add during the summertime. The range is 1 to 1440.
acronym The acronym for the summer-time to be displayed when summertime is in effect. The range is up to
four characters are allowed.
Command example:
(NETGEAR Switch) (Config)# clock summer-time date 1 nov 2011 3:18 2 nov 2011 3:18
(NETGEAR Switch) (Config)# clock summer-time date 1 nov 2011 3:18 2 nov 2011 3:18 offset
120 zone INDA
clock summer-time recurring
This command sets the summer-time recurring parameters.
Format clock summer-time recurring {week day month hh:mm week day month hh:mm}
[offset offset] [zone acronym]
Mode Global Config
Parameter Description
EU The system clock uses the standard recurring summer time settings used in countries in the
European Union.
USA The system clock uses the standard recurring daylight saving time settings used in the United
States.
week Week of the month. The range is 1 to 5, first, last.
day Day of the week. The range is the first three letters by name; sun, for example.
month Month. The range is the first three letters by name; jan, for example.
hh:mm Time in 24-hour format in hours and minutes. The range is hours: 0 to 23, minutes: 0 to 59.
offset The number of minutes to add during the summertime. The range is 1 to 1440.
acronym The acronym for the summertime to be displayed when summertime is in effect. Up to four
characters are allowed.
Command example:
(NETGEAR Switch) (Config)# clock summer-time recurring 2 sun nov 3:18 2 mon nov 3:18
(NETGEAR Switch) (Config)# clock summer-time recurring 2 sun nov 3:18 2 mon nov 3:18
offset 120 zone INDA
Utility Commands 262

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no clock summer-time
This command disables the summer time settings.
Format no clock summer-time
Mode Global Config
Command example:
(NETGEAR Switch) (Config)# no clock summer-time
clock timezone
Use this command to set the offset to Coordinated Universal Time (UTC). If the optional
parameters are not specified, they will be read as either 0 or \0 as appropriate.
Format clock timezone {hours} [minutes minutes] [zone acronym]
Mode Global Config
Parameter Description
hours Hours difference from UTC. The range is -12 to +13.
minutes Minutes difference from UTC. The range is 0 to 59.
acronym The acronym for the time zone. The range is up to four characters.
Command example:
(NETGEAR Switch) (Config)# clock timezone 5 minutes 30 zone INDA
no clock timezone
Use this command to reset the time zone settings.
Format no clock timezone
Mode Global Config
Command example:
(NETGEAR Switch) (Config)# no clock timezone
show clock
Use this command to display the time and date from the system clock.
Format show clock
Mode Privileged Exec
Utility Commands 263

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch)) # show clock
15:02:09 (UTC+0:00) Nov 1 2011
No time source
Command example:
(NETGEAR Switch) # show clock
10:55:40 INDA(UTC+7:30) Nov 1 2011
No time source
show clock detail
Use this command to display the detailed system time along with the time zone and the
summertime configuration.
Format show clock detail
Mode Privileged Exec
Command example:
(NETGEAR Switch) # show clock detail
15:05:24 (UTC+0:00) Nov 1 2011
No time source
Time zone:
Acronym not configured
Offset is UTC+0:00
Summertime:
Summer-time is disabled
Command example:
((NETGEAR Switch) # show clock detail
10:57:57 INDA(UTC+7:30) Nov 1 2011
No time source
Time zone:
Acronym is INDA
Offset is UTC+5:30
Summertime:
Acronym is INDA
Recurring every year
Utility Commands 264
