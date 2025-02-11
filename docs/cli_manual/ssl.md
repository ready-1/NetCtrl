# ssl

Pages: 170-173

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
address. If the switch does not include an interface with a matching IP address, OpenFlow is
operationally disabled.
If OpenFlow is enabled when you enter this command and you specify a static IP address
that is not the same as the IP address that is already in use, OpenFlow is automatically
disabled and reenabled.
Default 0.0.0.0
Format openflow static-ip ipv4-address
Mode Global Config
no openflow static-ip
This command sets the OpenFlow static IP address to 0.0.0.0. If you enter this command
when OpenFlow is enabled and is using a static IP address, OpenFlow becomes
operationally disabled.
Format no openflow static-ip
Mode Global Config
openflow controller
This command can specify up to 20 IP addresses with which the switch must establish an
OpenFlow controller connection. Each time that you enter the command, you can specify one
IP address and connection mode (TCP or SSL). If you do not specify a port number for the
ip-port parameter, the default IP port number 6633 is used. The default connection mode
is SSL. The switch uses the controller table that is created by this command only in
OpenFlow modes 1.0 and 1.3.
Default 6633
SSL
Format openflow controller ip-address [ip-port] [TCP | SSL]
Mode Global Config
no openflow controller
This command deletes a specific OpenFlow controller IP address or deletes all controller’s IP
addresses. If you do not specify a port number for the ip-port parameter, all entries for the
specified IP address are deleted.
Format no openflow controller {ip-address [ip-port] | all]
Mode Global Config
Management Commands 170

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
openflow default-table
This command configures the OpenFlow hardware table. This table is used as the target for
flows that are installed by an OpenFlow 1.0 controller that is not enhanced to handle multiple
hardware tables. The full-match and layer-2-match keywords are applicable only in
OpenFlow mode 1.0.
Default full-match
Format openflow default-table {full-match | layer-2-match}
Mode Global Config
openflow ip-mode
This command directs OpenFlow to use the configured IP address:
• auto. OpenFlow uses the IP address of the management interface.
• static. OpenFlow uses the static IP address that you can specify by entering the
openflow static-ip command.
• serviceport. OpenFlow uses the IP address of the service port.
Issuing this command when OpenFlow is already enabled causes the feature to be disabled
and reenabled with the new IP address.
Default auto
Format openflow ip-mode {auto | static | serviceport}
Mode Global Config
no openflow ip-mode
This command resets the OpenFlow IP mode to the default (auto).
Format no openflow ip-mode
Mode Global Config
openflow passive-mode
This command enables OpenFlow passive mode.
Format openflow passive-mode
Mode Global Config
Management Commands 171

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no openflow passive-mode
This command disables OpenFlow passive mode.
Format no openflow passive-mode
Mode Global Config
openflow variant
This command configures OpenFlow mode 1.0 or mode 1.3. (For OpenFlow, mode is also
referred to as variant.) By default, OpenFlow is configured for mode 1.3.
Default openflow1.3
Format openflow variant {openflow10 | openflow13}
Mode Global Config
clear openflow ca-certs
This command erases the certificate authority (CA) certificates that the switch uses to
validate the OpenFlow controllers. When you enter this command, OpenFlow is automatically
disabled and reenabled.
The first time that the switch connects to the OpenFlow controller, the SSL certificates are
reloaded from the OpenFlow controller. You can also manually load the SSL certificates by
using a copy command.
Format clear openflow controller-certs
Mode Privileged Exec
show openflow
This command displays the status and configuration information of OpenFlow.
Format show openflow
Mode Privileged Exec
Term Definition
Administrative Mode The OpenFlow administrative mode that is specified by the openflow enable command.
Administrative Status The operational status of OpenFlow. Although OpenFlow can be administratively enabled, it could
be operationally disabled.
Disable Reason If OpenFlow is operationally disabled, the reason why OpenFlow is disabled.
IP Address The IPv4 address that is assigned to OpenFlow. If no IP address is assigned, the status is None.
Management Commands 172

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
IP Mode The IP mode that is specified by the openflow ip-mode command. The IP mode can be Auto,
Static, or ServicePort IP.
Static IP Address The static IP address that is specified by the openflow static-ip command.
OpenFlow Variant The OpenFlow protocol variant (mode). The OpenFlow variant can be OpenFlow 1.0 or
OpenFlow1.3.
Default Table The hardware table that is used as the target for flows that are installed by an OpenFlow 1.0
controller that is not enhanced to handle multiple hardware tables.
Passive Mode The OpenFlow passive mode that is specified by the openflow passive-mode command.
Command example:
(NETGEAR Switch) #show openflow
Administrative Mode............................ Enable
Administrative Status.......................... Disabled
Disable Reason................................. No-Suitable-IP-Interface
IP Address..................................... None
IP Mode................................. Auto
Static IP Address.............................. 10.1.1.1
OpenFlow Variant............................... OpenFlow 1.0
Default Table.................................. layer-2-match
Passive Mode................................... Enable
Command example:
(NETGEAR Switch) #show openflow
Administrative Mode............................ Enable
Administrative Status.......................... Enabled
Disable Reason................................. None
IP Address..................................... 10.27.65.64
IP Mode................................. Auto
Static IP Address.............................. 10.1.1.1
OpenFlow Variant............................... OpenFlow 1.0
Passive Mode................................... Enable
show openflow configured controller
This command displays a list of configured OpenFlow controllers. The switch communicates
with these controllers only when the OpenFlow variant (mode) is 1.0 or 1.3.
Format show openflow configured controller
Mode Privileged Exec
Management Commands 173
