# failed

Pages: 325-335

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show power redundancy
This command displays the power redundancy status.
Format show power redundancy
Mode Privileged EXEC
Command example:
(NETGEAR Switch)# show power redundancy
N+1 configuration: ............................ Disable
N+1 Active: ................................... No
Number of PSU: ................................ 1
Effective Number of PSU: ...................... 1
show power
This command displays the switch power usage.
The unit-number argument specifies the PSU in the switch.
Format show power [unit-number]
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show power
Unit : 1
Model Name:.................................... M4300-52G-PoE+
Total Available power(W): ..................... 1440
Total Power Module Slot Number:................ 2
Power Power
Modules Module Module
Slot Name Status AC Input(V)
------- ------------ ---------------- -----------
1 Failed
2 Not Present
USB commands
If a USB flash device is installed in the USB slot, the USB commands display the device
status and content.
Utility Commands 325

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show usb device
This command displays USB flash device details.
Format show USB device
Mode Privileged EXEC
Term Description
Device Status This field specifies the current status of device. Following are possible device status states:
• Active. Device is plugged in and the device is recognized if device is not mounted.
• Inactive. Device is not mounted.
• Invalid. Device is not present or invalid device is plugged in.
Command example:
(NETGEAR Switch) #show USB device
Device Status………………………………………………… Active
dir usb
This command displays USB device contents and memory statistics.
Format dir usb
Mode Privileged EXEC
Term Description
Filename File name
Filesize File size
Total Size USB flash device storage size
Bytes Used Indicates size of memory used on the device.
Bytes Free Indicates size of memory free on the device
Command example:
(NETGEAR Switch) #dir USB:
Filename Filesize Modification Time
F1.cfg 256 4/22/2009 8:00:12
Total Size: xxxx
Bytes Used: yyyy
Bytes Free: zzzz
Utility Commands 326

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
sFlow Commands
sFlow is the standard for monitoring high-speed switched and routed networks. sFlow
technology is built into network equipment and gives complete visibility into network activity,
enabling effective management and control of network resources.
sflow receiver
Use this command to configure the sFlow collector parameters (owner string, receiver
time-out, max datagram size, IP address, and port).
Format sflow receiver rcvr_idx {owner owner-string {timeout rcvr_timeout |
notimeout} | maxdatagram size | ip ip | port port}
Mode Global Config
Parameter Description
Receiver Owner The identity string for the receiver, the entity making use of this sFlowRcvrTable entry. The range is
127 characters. The default is a null string. The empty string indicates that the entry is currently
unclaimed and the receiver configuration is reset to the default values. An entity wishing to claim an
sFlowRcvrTable entry must ensure that the entry is unclaimed before trying to claim it. The entry is
claimed by setting the owner string to a non-null value. The entry must be claimed before assigning
a receiver to a sampler or poller.
Receiver Timeout The time, in seconds, remaining before the sampler or poller is released and stops sending samples
to receiver. A management entity wanting to maintain control of the sampler is responsible for setting
a new value before the old one expires. The allowed range is 0-2147483647 seconds. The default is
zero (0).
No Timeout The configured entry will be in the config until you explicitly removes the entry.
Receiver Max The maximum number of data bytes that can be sent in a single sample datagram. The
Datagram Size management entity should set this value to avoid fragmentation of the sFlow datagrams. The
allowed range is 200 to 9116). The default is 1400.
Receiver IP The sFlow receiver IP address. If set to 0.0.0.0, no sFlow datagrams will be sent. The default is
0.0.0.0.
Receiver Port The destination Layer4 UDP port for sFlow datagrams. The range is 1-65535. The default is 6343.
no sflow receiver
Use this command to set the sFlow collector parameters back to the defaults.
Format no sflow receiver rcvr_idx [owner | maxdatagram | ip | port]
Mode Global Config
Utility Commands 327

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
sflow receiver owner timeout
Use this command to configure a receiver as a timeout entry. As the sFlow receiver is
configured as a timeout entry, information related to sampler and pollers are also shown in
the running-config and are retained after reboot.
If a receiver is configured with a specific value, these configurations are not shown in the
running-config file. Samplers and pollers information related to this receiver are also not
shown in the running-config file.
Format sflow receiver index owner owner-string timeout
Mode Global Config
Field Description
index Receiver index identifier. The range is 1 to 8.
Receiver Owner The owner name corresponds to the receiver name. The identity string for the receiver, the entity
making use of this sFlowRcvrTable entry. The range is 127 characters. The default is a null string.
The empty string indicates that the entry is currently unclaimed and the receiver configuration is
reset to the default values. An entity wishing to claim an sFlowRcvrTable entry must ensure that the
entry is unclaimed before trying to claim it. The entry is claimed by setting the owner string to a
non-null value. The entry must be claimed before assigning a receiver to a sampler or poller.
sflow receiver owner notimeout
Use this command to configure a receiver as a non-timeout entry. Unlike entries configured
with a specific timeout value, this command will be shown in show running-config and
retained after reboot. As the sFlow receiver is configured as a non-timeout entry, information
related to sampler and pollers will also be shown in the running-config and will be retained
after reboot.
If a receiver is configured with a specific value, these configurations are not shown in the
running-config file. Samplers and pollers information related to this receiver are also not
shown in the running-config file.
Format sflow receiver index owner owner-string notimeout
Mode Global Config
Field Description
index Receiver index identifier. The range is 1 to 8.
Receiver Owner The owner name corresponds to the receiver name. The identity string for the receiver, the entity
making use of this sFlowRcvrTable entry. The range is 127 characters. The default is a null string.
The empty string indicates that the entry is currently unclaimed and the receiver configuration is
reset to the default values. An entity wishing to claim an sFlowRcvrTable entry must ensure that the
entry is unclaimed before trying to claim it. The entry is claimed by setting the owner string to a
non-null value. The entry must be claimed before assigning a receiver to a sampler or poller.
Utility Commands 328

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
sflow sampler
A data source configured to collect flow samples is called a poller. Use this command to
configure a new sFlow sampler instance on an interface or range of interfaces for this data
source if rcvr_indx is valid.
Format sflow sampler {rcvr-indx | rate sampling-rate | maxheadersize size}
Mode Interface Config
Field Description
Receiver Index The sFlow Receiver for this sFlow sampler to which flow samples are to be sent. A value of zero (0)
means that no receiver is configured, no packets will be sampled. Only active receivers can be set. If
a receiver expires, then all samplers associated with the receiver will also expire. Possible values
are 1-8. The default is 0.
Maxheadersize The maximum number of bytes that should be copied from the sampler packet. The range is 20-256.
The default is 128. When set to zero (0), all the sampler parameters are set to their corresponding
default value.
Sampling Rate The statistical sampling rate for packet sampling from this source. A value of zero (0) disables
sampling. A value of N means that out of N incoming packets, 1 packet will be sampled. The range is
1024-65536 and 0. The default is 0.
When you issue a show command for the sampling rate, the configured sampling rate on an
interface changes. Each time that you configure a sampling rate, a threshold value is calculated.
This threshold value is configured in the hardware register. When you issue a show command for
the sampling rate, the threshold value is queried from the hardware and the sampling rate is
calculated in the following way:
threshold value = 2^24/ (sampling rate)
Because only an integer operation is supported, the sampling rate is not the same as the configured
value.
The following is an example:
configured sampling rate is 60000
threshold value = 2^24/ (60000) = 279 (from integer division)
recalculated sampling rate = 2^24/ (279) = 60133
no sflow sampler
Use this command to reset the sFlow sampler instance to the default settings.
Format no sflow sampler {rcvr-indx | rate sampling-rate | maxheadersize size}
Mode Interface Config
Utility Commands 329

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
sflow poller
A data source configured to collect counter samples is called a poller. Use this command to
enable a new sFlow poller instance on an interface or range of interfaces for this data source
if rcvr_indx is valid.
Format sflow poller {rcvr-indx | interval poll-interval}
Mode Interface Config
Field Description
Receiver Index Enter the sFlow Receiver associated with the sampler/poller. A value of zero (0) means that no
receiver is configured. The range is 1-8. The default is 0.
Poll Interval Enter the sFlow instance polling interval. A poll interval of zero (0) disables counter sampling. When
set to zero (0), all the poller parameters are set to their corresponding default value. The range is
0-86400. The default is 0. A value of N means once in N seconds a counter sample is generated.
The sFlow task is heavily loaded when the sFlow polling interval is configured at the minimum
value (i.e., one second for all the sFlow supported interfaces). In this case, the sFlow task is
always busy collecting the counters on all the configured interfaces. This can cause the
device to hang for some time when the user tries to configure or issue show sFlow
commands.
To overcome this situation, sFlow polling interval configuration on an interface or range of
interfaces is controlled as mentioned below:
1. The maximum number of allowed interfaces for the polling intervals max (1, (interval –
10)) to min ((interval + 10), 86400) is:
interval * 5
2. For every one second increment in the polling interval that is configured, the number of
allowed interfaces that can be configured increases by 5.
no sflow poller
Use this command to reset the sFlow poller instance to the default settings.
Format no sflow poller [interval]
Mode Interface Config
sflow source-interface
Use this command to specify the physical or logical interface to use as the sFlow client
source interface. If configured, the address of source Interface is used for all sFlow
communications between the sFlow receiver and the sFlow client. Otherwise there is no
Utility Commands 330

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
change in behavior. If the configured interface is down, the sFlow client falls back to normal
behavior.
Format sflow source-interface {unit/slot/port | loopback loopback-id | tunnel
tunnel-id | vlan vlan-id}
Mode Global Config
Parameter Description
unit/slot/port VLAN or port-based routing interface.
loopback-id Configures the loopback interface to use as the source IP address. The range of the loopback ID is
0 to 7.
tunnel-id Configures the tunnel interface to use as the source IP address. The range of the tunnel ID is 0 to 7.
vlan-id Configures the VLAN interface to use as the source IP address. The range of the VLAN ID is 1 to
4093.
no sflow source-interface
Use this command to reset the sFlow source interface to the default settings.
Format no sflow source-interface
Mode Global Config
show sflow agent
The sFlow agent collects time-based sampling of network interface statistics and flow-based
samples. These are sent to the configured sFlow receivers. Use this command to display the
sFlow agent information.
Format show sflow agent
Mode Privileged EXEC
Field Description
sFlow Version Uniquely identifies the version and implementation of this MIB. The version string must have the
following structure: MIB Version; Organization; Software Revision where:
MIB Version: 1.3, the version of this MIB.
Organization: NETGEAR Corp.
Revision: 1.0
IP Address The IP address associated with this agent.
Command example:
(NETGEAR Switch) #show sflow agent
sFlow Version.................................. 1.3;NETGEAR Corp;1.0
Utility Commands 331

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
IP Address..................................... 10.131.12.66
show sflow pollers
Use this command to display the sFlow polling instances created on the switch. Use “-” for
range.
Format show sflow pollers
Mode Privileged EXEC
Field Description
Poller Data Source The sFlowDataSource (slot/port) for this sFlow sampler. This agent will support Physical ports only.
Receiver Index The sFlowReceiver associated with this sFlow counter poller.
Poller Interval The number of seconds between successive samples of the counters associated with this data
source.
show sflow receivers
Use this command to display configuration information related to the sFlow receivers.
Format show sflow receivers [index]
Mode Privileged EXEC
Parameter Description
Receiver Index The sFlow Receiver associated with the sampler/poller.
Owner String The identity string for receiver, the entity making use of this sFlowRcvrTable entry.
Time Out The time (in seconds) remaining before the receiver is released and stops sending samples
to sFlow receiver. The no timeout value of this parameter means that the sFlow receiver is
configured as a non-timeout entry.
Max Datagram Size The maximum number of bytes that can be sent in a single sFlow datagram.
Port The destination Layer4 UDP port for sFlow datagrams.
IP Address The sFlow receiver IP address.
Address Type The sFlow receiver IP address type. For an IPv4 address, the value is 1 and for an IPv6
address, the value is 2.
Datagram Version The sFlow protocol version to be used while sending samples to sFlow receiver.
Command example:
(NETGEAR Switch) #show sflow receivers 1
Receiver Index................................. 1
Owner String................................... tulasi
Utility Commands 332

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Time out....................................... 0
IP Address:.................................... 0.0.0.0
Address Type................................... 1
Port........................................... 6343
Datagram Version............................... 5
Maximum Datagram Size.......................... 1400
Command example:
The following example shows that a receiver is configured as a non-time-out entry:
(NETGEAR Switch) #show sflow receivers
Rcvr Owner Timeout Max Dgram Port IP Address
Indx String Size
---- -------------------------------- ---------- --------- ----- ---------------
1 tulasi No Timeout 1400 6343 0.0.0.0 <= No Timeout
string
2 0 1400 6343 0.0.0.0
3 0 1400 6343 0.0.0.0
4 0 1400 6343 0.0.0.0
5 0 1400 6343 0.0.0.0
6 0 1400 6343 0.0.0.0
7 0 1400 6343 0.0.0.0
8 0 1400 6343 0.0.0.0
Command example:
The following example also shows that a receiver is configured as a non-time-out entry:
(NETGEAR Switch) #show sflow receivers 1
Receiver Index................................. 1
Owner String................................... tulasi
Time out....................................... No Timeout < = No Timeout string
is added
IP Address:.................................... 0.0.0.0
Address Type................................... 1
Port........................................... 6343
Datagram Version............................... 5
Maximum Datagram Size.......................... 1400
show sflow samplers
Use this command to display the sFlow sampling instances created on the switch.
Format show sflow samplers
Mode Privileged EXEC
Utility Commands 333

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Field Description
Sampler Data Source The sFlowDataSource (slot/port) for this sFlow sampler. This agent will support Physical
ports only.
Receiver Index The sFlowReceiver configured for this sFlow sampler.
Packet Sampling Rate The statistical sampling rate for packet sampling from this source.
Max Header Size The maximum number of bytes that should be copied from a sampled packet to form a
flow sample.
show sflow source-interface
Use this command to display the sFlow source interface configured on the switch.
Format show sflow source-interface
Mode Privileged EXEC
Field Description
sFlow Client Source Interface The interface ID of the physical or logical interface configured as the sFlow client source
interface.
sFlow Client Source IPv4 The IP address of the interface configured as the sFlow client source interface.
Address
Command example:
(NETGEAR Switch) #show sflow source-interface
sFlow Client Source Interface.................. (not configured)
Switch Database Management Template
Commands
A Switch Database Management (SDM) template is a description of the maximum resources
a switch or router can use for various features. Different SDM templates allow different
combinations of scaling factors, enabling different allocations of resources depending on how
the device is used. In other words, SDM templates enable you to reallocate system resources
to support a different mix of features based on your network requirements.
Utility Commands 334

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: If you insert a unit in a stack and its template does not match the
template of the stack, the unit reboots automatically using the
template that is used by other stack members. To avoid the automatic
reboot, first set the template to the template that is used by existing
members of the stack. Then power off the new unit, insert it in the
stack, and power on the unit.
sdm prefer
Use this command to change the template that must be active after the next reboot. The
keywords are as follows:
• dual-ipv4-and-ipv6 data-center-generic. The common template that supports both IPv4
and IPv6 on M4300 series switches.
• dual-ipv4-and-ipv6 data-center-native. The template that supports both IPv4 and IPv6
on model M4300-24X24F only.
• sdm prefer ipv4-routing data-center plus-m4396only. the template that supports IPv4
on model M4300-96X only.
• ipv4 routing data-center plus-generic. The common template that supports IPv4 only
on M4300 series switches.
• ipv4 routing data-center plus-native. The template that supports IPv4 on model
M4300-24X24F only.
• sdm prefer ipv4-routing data-center plus-mixed-native-m4396. The template that
supports IPv4 on models M4300-48X, M4300-24X24F, and M4300-96X.
Note: After setting the template, you must reboot in order for the
configuration change to take effect.
Default dual-ipv4-and-ipv6 data-center-generic
Format sdm prefer {dual-ipv4-and-ipv6 {data-center-generic | data-center-m4396only
| data-center-mixed-native-m4396 | data-center-native} | ipv4-routing
data-center {plus-generic | plus-m4396only | plus-mixed-native-m4396 |
plus-native}}
Mode Global Config
no sdm prefer
Use this command to revert to the default template after the next reboot.
Format no sdm prefer
Mode Global Config
Utility Commands 335
