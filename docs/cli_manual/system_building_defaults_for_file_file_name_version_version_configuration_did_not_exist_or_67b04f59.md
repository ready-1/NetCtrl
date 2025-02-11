# system_building_defaults_for_file_file_name_version_version_configuration_did_not_exist_or_67b04f59

Pages: 1108-1108

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
T able 18. SIM Log Message
Component Message Cause
SIM IP address conflict on service port/network port This message appears when an address conflict
for IP address x.x.x.x. Conflicting host MAC is detected in the LAN for the service
address is xx:xx:xx:xx:xx:xx port/network port IP.
T able 19. System Log Messages
Component Message Cause
SYSTEM The size of the startup-config.cfg The configuration file could not be read. This
configuration file is 0 (zero) bytes message may occur on a system for which no
configuration has ever been saved or for which
configuration has been erased.
SYSTEM could not separate The configuration file could not be read. This
SYSAPI_CONFIG_FILENAME message may occur on a system for which no
configuration has ever been saved or for which
configuration has been erased.
SYSTEM Building defaults for file file name version version Configuration did not exist or could not be read
num for the specified feature or file. Default
configuration values will be used. The file name
and version are indicated.
SYSTEM File filename: same version (version num) but the The configuration file which was loaded was of a
sizes (version size – expected version size) differ different size than expected for the version
number. This message indicates the
configuration file needed to be migrated to the
version number appropriate for the code image.
This message may appear after upgrading the
code image to a more current release.
SYSTEM Migrating config file filename from version The configuration file identified was migrated
version num to version num from a previous version number. Both the old and
new version number are specified. This message
may appear after upgrading the code image to a
more current release.
SYSTEM Building Defaults Configuration did not exist or could not be read
for the specified feature. Default configuration
values will be used.
SYSTEM sysapiCfgFileGet failed size = expected size of Configuration did not exist or could not be read
file version = expected version for the specified feature. This message is usually
followed by a message indicating that default
configuration values will be used.
Switch Software Log Messages 1108
