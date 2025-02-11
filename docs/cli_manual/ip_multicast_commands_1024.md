# ip_multicast_commands_1024

Pages: 1024-1024

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
ip dvmrp metric
This command configures the metric for an interface or range of interfaces. This value is used
in the DVMRP messages as the cost to reach this network. The metric argument is a value
in the range 1 to 31.
Default 1
Format ip dvmrp metric metric
Mode Interface Config
no ip dvmrp metric
This command resets the metric for an interface to the default value. This value is used in the
DVMRP messages as the cost to reach this network.
Format no ip dvmrp metric
Mode Interface Config
ip dvmrp trapflags
This command enables the DVMRP trap mode.
Default disabled
Format ip dvmrp trapflags
Mode Global Config
no ip dvmrp trapflags
This command disables the DVMRP trap mode.
Format no ip dvmrp trapflags
Mode Global Config
ip dvmrp (Interface Config)
This command sets the administrative mode of DVMRP on an interface or range of interfaces
to active.
Default disabled
Format ip dvmrp
Mode Interface Config
IP Multicast Commands 1024
