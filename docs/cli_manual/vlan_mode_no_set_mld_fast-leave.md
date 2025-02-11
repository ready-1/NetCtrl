# vlan_mode_no_set_mld_fast-leave

Pages: 591-591

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default Enabled for VLAN 1; Disabled for other VLANs.
Format set mld fast-leave vlan-id
Mode Interface Config
VLAN Mode
no set mld fast-leave
Use this command to disable MLD Snooping fast-leave admin mode on a selected interface.
Format no set mld fast-leave vlan-id
Mode Interface Config
VLAN Mode
set mld groupmembership-interval
Use this command to set the MLD Group Membership Interval time on a VLAN, one interface
or all interfaces. The Group Membership Interval time is the amount of time in seconds that a
switch waits for a report from a particular group on a particular interface before deleting the
interface from the entry. This value must be greater than the MLDv2 maximum response time
value. The range is 2 to 3600 seconds.
Default 260 seconds
Format set mld groupmembership-interval vlan-id seconds
Mode Interface Config
Global Config
VLAN Mode
no set groupmembership-interval
Use this command to set the MLDv2 group membership Interval time to the default value.
Format no set mld groupmembership-interval
Mode Interface Config
Global Config
VLAN Mode
set mld maxresponse
Use this command to set the MLD maximum response time for the system, on a particular
interface or VLAN. The maximum response time is the amount of time in seconds that a
switch will wait after sending a query on an interface because it did not receive a report for a
particular group in that interface. This value must be less than the MLD query interval time
value. The range is 1 to 65 seconds.
Switching Commands 591
