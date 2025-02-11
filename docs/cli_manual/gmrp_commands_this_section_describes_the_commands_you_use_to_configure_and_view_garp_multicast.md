# gmrp_commands_this_section_describes_the_commands_you_use_to_configure_and_view_garp_multicast

Pages: 459-473

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Interface unit/slot/port
Join Timer The interval between the transmission of GARP PDUs registering (or reregistering) membership for
an attribute. Current attributes are a VLAN or multicast group. There is an instance of this timer on a
per-Port, per-GARP participant basis. Permissible values are 10 to 100 centiseconds (0.1 to 1.0
seconds). The factory default is 20 centiseconds (0.2 seconds). The finest granularity of
specification is one centisecond (0.01 seconds).
Leave Timer The period of time to wait after receiving an unregister request for an attribute before deleting the
attribute. Current attributes are a VLAN or multicast group. This may be considered a buffer time for
another station to assert registration for the same attribute in order to maintain uninterrupted service.
There is an instance of this timer on a per-Port, per-GARP participant basis. Permissible values are
20 to 600 centiseconds (0.2 to 6.0 seconds). The factory default is 60 centiseconds (0.6 seconds).
LeaveAll Timer This Leave All Time controls how frequently LeaveAll PDUs are generated. A LeaveAll PDU
indicates that all registrations will shortly be deregistered. Participants will need to rejoin in order to
maintain registration. There is an instance of this timer on a per-Port, per-GARP participant basis.
The Leave All Period Timer is set to a random value in the range of LeaveAllTime to
1.5*LeaveAllTime. Permissible values are 200 to 6000 centiseconds (2 to 60 seconds). The factory
default is 1000 centiseconds (10 seconds).
Port GMRP Mode The GMRP administrative mode for the port, which is enabled or disabled (default). If this parameter
is disabled, Join Time, Leave Time and Leave All Time have no effect.
GMRP Commands
This section describes the commands you use to configure and view GARP Multicast
Registration Protocol (GMRP) information. Like IGMP snooping, GMRP helps control the
flooding of multicast packets.GMRP-enabled switches dynamically register and de-register
group membership information with the MAC networking devices attached to the same
segment. GMRP also allows group membership information to propagate across all
networking devices in the bridged LAN that support Extended Filtering Services.
Note: If GMRP is disabled, the system does not forward GMRP messages.
set gmrp adminmode
This command enables GARP Multicast Registration Protocol (GMRP) on the system.
Default Disabled
Format set gmrp adminmode
Mode Privileged EXEC
Switching Commands 459

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no set gmrp adminmode
This command disables GARP Multicast Registration Protocol (GMRP) on the system.
Format no set gmrp adminmode
Mode Privileged EXEC
set gmrp interfacemode
This command enables GARP Multicast Registration Protocol on a single interface (Interface
Config mode), a range of interfaces, or all interfaces (Global Config mode). If an interface
which has GARP enabled is enabled for routing or is enlisted as a member of a port-channel
(LAG), GARP functionality is disabled on that interface. GARP functionality is subsequently
re-enabled if routing is disabled and port-channel (LAG) membership is removed from an
interface that has GARP enabled.
Default Disabled
Format set gmrp interfacemode
Mode Interface Config
Global Config
no set gmrp interfacemode
This command disables GARP Multicast Registration Protocol on a single interface or all
interfaces. If an interface which has GARP enabled is enabled for routing or is enlisted as a
member of a port-channel (LAG), GARP functionality is disabled. GARP functionality is
subsequently re-enabled if routing is disabled and port-channel (LAG) membership is
removed from an interface that has GARP enabled.
Format no set gmrp interfacemode
Mode Interface Config
Global Config
show gmrp configuration
This command displays Generic Attributes Registration Protocol (GARP) information for one
or all interfaces.
Format show gmrp configuration {unit/slot/port | all}
Mode Privileged EXEC
User EXEC
Switching Commands 460

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Interface The unit/slot/port of the interface that this row in the table describes.
Join Timer The interval between the transmission of GARP PDUs registering (or reregistering) membership for
an attribute. Current attributes are a VLAN or multicast group. There is an instance of this timer on a
per-port, per-GARP participant basis. Permissible values are 10 to 100 centiseconds (0.1 to 1.0
seconds). The factory default is 20 centiseconds (0.2 seconds). The finest granularity of
specification is 1 centisecond (0.01 seconds).
Leave Timer The period of time to wait after receiving an unregister request for an attribute before deleting the
attribute. Current attributes are a VLAN or multicast group. This may be considered a buffer time for
another station to assert registration for the same attribute in order to maintain uninterrupted service.
There is an instance of this timer on a per-Port, per-GARP participant basis. Permissible values are
20 to 600 centiseconds (0.2 to 6.0 seconds). The factory default is 60 centiseconds (0.6 seconds).
LeaveAll Timer This Leave All Time controls how frequently LeaveAll PDUs are generated. A LeaveAll PDU
indicates that all registrations will shortly be deregistered. Participants will need to rejoin in order to
maintain registration. There is an instance of this timer on a per-Port, per-GARP participant basis.
The Leave All Period Timer is set to a random value in the range of LeaveAllTime to
1.5*LeaveAllTime. Permissible values are 200 to 6000 centiseconds (2 to 60 seconds). The factory
default is 1000 centiseconds (10 seconds).
Port GMRP Mode The GMRP administrative mode for the port. It may be enabled or disabled. If this parameter is
disabled, Join Time, Leave Time and Leave All Time have no effect.
show mac-address-table gmrp
This command displays the GMRP entries in the Multicast Forwarding Database (MFDB)
table.
Format show mac-address-table gmrp
Mode Privileged EXEC
Term Definition
VLAN ID The VLAN in which the MAC Address is learned.
MAC Address A unicast MAC address for which the switch has forwarding and or filtering information. The format is
6 two-digit hexadecimal numbers that are separated by colons, for example 01:23:45:67:89:AB.
Type The type of the entry. Static entries are those that are configured by the end user. Dynamic entries
are added to the table as a result of a learning process or protocol.
Description The text description of this multicast table entry.
Interfaces The list of interfaces that are designated for forwarding (Fwd:) and filtering (Flt:).
Switching Commands 461

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Port-Based Network Access Control
Commands
This section describes the commands you use to configure port-based network access
control (IEEE 802.1X). Port-based network access control allows you to permit access to
network services only to and devices that are authorized and authenticated.
aaa authentication dot1x default
Use this command to configure the authentication methods for port-based access to the
switch. The additional methods of authentication are used only if the previous method returns
an error, not if there is an authentication failure.
The possible methods are as follows:
• ias. Uses the internal authentication server users database for authentication.
• local. Uses the local user name database for authentication.
• none. Uses no authentication.
• radius. Uses the list of all RADIUS servers for authentication.
You can configure one method at the time.
Format aaa authentication dot1x default {ias | local | none | radius}
Mode Global Config
Command example:
(NETGEAR Switch) #
(NETGEAR Switch) #configure
(NETGEAR Switch) (Config)#aaa authentication dot1x default ias
(NETGEAR Switch) (Config)#aaa authentication dot1x default local
clear dot1x statistics
This command resets the 802.1X statistics for the specified port or for all ports.
Format clear dot1x statistics {unit/slot/port | all}
Mode Privileged EXEC
Switching Commands 462

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
clear dot1x authentication-history
This command clears the authentication history table captured during successful and
unsuccessful authentication on all interface or the specified interface.
Format clear dot1x authentication-history [unit/slot/port]
Mode Privileged EXEC
clear radius statistics
This command is used to clear all RADIUS statistics.
Format clear radius statistics
Mode Privileged EXEC
dot1x eapolflood
Use this command to enable EAPOL flood support on the switch.
Default Disabled
Format dot1x eapolflood
Mode Global Config
no dot1x eapolflood
This command disables EAPOL flooding on the switch.
Format no dot1x eapolflood
Mode Global Config
dot1x dynamic-vlan enable
Use this command to enable the switch to create VLANs dynamically when a
RADIUS-assigned VLAN does not exist in the switch.
Default Disabled
Format dot1x dynamic-vlan enable
Mode Global Config
Switching Commands 463

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dot1x dynamic-vlan enable
Use this command to prevent the switch from creating VLANs when a RADIUS-assigned
VLAN does not exist in the switch.
Format no dot1x dynamic-vlan enable
Mode Global Config
dot1x guest-vlan
This command configures VLAN as guest vlan on an interface or a range of interfaces. The
command specifies an active VLAN as an IEEE 802.1X guest VLAN. The range is 1 to the
maximum VLAN ID supported by the platform.
Default Disabled
Format dot1x guest-vlan vlan-id
Mode Interface Config
no dot1x guest-vlan
This command disables Guest VLAN on the interface.
Default Disabled
Format no dot1x guest-vlan
Mode Interface Config
dot1x initialize
This command begins the initialization sequence on the specified port. This command is only
valid if the control mode for the specified port is auto or mac-based. If the control mode is not
auto or mac-based, an error is returned.
Format dot1x initialize unit/slot/port
Mode Privileged EXEC
dot1x max-req
This command sets the maximum number of times the authenticator state machine on an
interface or range of interfaces will transmit an EAPOL EAP Request/Identity frame before
timing out the supplicant. The count parameter must be in the range 1–10.
Default 2
Switching Commands 464

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format dot1x max-req count
Mode Interface Config
no dot1x max-req
This command sets the maximum number of times the authenticator state machine on this
port will transmit an EAPOL EAP Request/Identity frame before timing out the supplicant.
Format no dot1x max-req
Mode Interface Config
dot1x max-users
Use this command to set the maximum number of clients supported on an interface or range
of interfaces when MAC-based dot1x authentication is enabled on the port. The maximum
users supported per port is dependent on the product. The count parameter must be in the
range 1–48.
Default 48
Format dot1x max-users count
Mode Interface Config
no dot1x max-users
This command resets the maximum number of clients allowed per port to its default value.
Format no dot1x max-users
Mode Interface Config
dot1x port-control
This command sets the authentication mode to use on the specified interface or range of
interfaces. Use the force-unauthorized parameter to specify that the authenticator PAE
unconditionally sets the controlled port to unauthorized. Use the force-authorized
parameter to specify that the authenticator PAE unconditionally sets the controlled port to
authorized. Use the auto parameter to specify that the authenticator PAE sets the controlled
port mode to reflect the outcome of the authentication exchanges between the supplicant,
authenticator and the authentication server. If the mac-based parameter is specified, then
MAC-based dot1x authentication is enabled on the port.
Default auto
Format dot1x port-control {force-unauthorized | force-authorized | auto | mac-based}
Mode Interface Config
Switching Commands 465

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dot1x port-control
This command sets the 802.1X port control mode on the specified port to the default value.
Format no dot1x port-control
Mode Interface Config
dot1x port-control all
This command sets the authentication mode to use on all ports. Select the
force-unauthorized parameter to specify that the authenticator PAE unconditionally sets
the controlled port to unauthorized. Select the force-authorized parameter to specify
that the authenticator PAE unconditionally sets the controlled port to authorized. Select the
auto parameter to specify that the authenticator PAE sets the controlled port mode to reflect
the outcome of the authentication exchanges between the supplicant, authenticator and the
authentication server. If the mac-based parameter is specified, then MAC-based dot1x
authentication is enabled on the port.
Default auto
Format dot1x port-control all {force-unauthorized | force-authorized | auto |
mac-based}
Mode Global Config
no dot1x port-control all
This command sets the authentication mode on all ports to the default value.
Format no dot1x port-control all
Mode Global Config
dot1x mac-auth-bypass
If the 802.1X mode on the interface is mac-based, you can optionally use this command to
enable MAC Authentication Bypass (MAB) on an interface. MAB is a supplemental
authentication mechanism that allows 802.1X unaware clients – such as printers, fax
machines, and some IP phones—to authenticate to the network using the client MAC
address as an identifier.
Default Disabled
Format dot1x mac-auth-bypass
Mode Interface Config
Switching Commands 466

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dot1x mac-auth-bypass
This command sets the MAB mode on the ports to the default value.
Format no dot1x mac-auth-bypass
Mode Interface Config
dot1x re-authenticate
This command begins the reauthentication sequence on the specified port. This command is
only valid if the control mode for the specified port is auto or mac-based. If the control mode
is not auto or mac-based, an error is returned.
Format dot1x re-authenticate unit/slot/port
Mode Privileged EXEC
dot1x re-authentication
This command enables reauthentication of the supplicant for the specified interface or range
of interfaces.
Default Disabled
Format dot1x re-authentication
Mode Interface Config
no dot1x re-authentication
This command disables reauthentication of the supplicant for the specified port.
Format no dot1x re-authentication
Mode Interface Config
dot1x system-auth-control
Use this command to enable the dot1x authentication support on the switch. While disabled,
the dot1x configuration is retained and can be changed, but is not activated.
Default Disabled
Format dot1x system-auth-control
Mode Global Config
Switching Commands 467

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dot1x system-auth-control
This command is used to disable the dot1x authentication support on the switch.
Format no dot1x system-auth-control
Mode Global Config
dot1x system-auth-control monitor
Use this command to enable the 802.1X monitor mode on the switch. The purpose of Monitor
mode is to help troubleshoot port-based authentication configuration issues without
disrupting network access for hosts connected to the switch. In Monitor mode, a host is
granted network access to an 802.1X-enabled port even if it fails the authentication process.
The results of the process are logged for diagnostic purposes.
Default Disabled
Format dot1x system-auth-control monitor
Mode Global Config
no dot1x system-auth-control monitor
This command disables the 802.1X Monitor mode on the switch.
Format no dot1x system-auth-control monitor
Mode Global Config
dot1x timeout
This command sets the value, in seconds, of the timer used by the authenticator state
machine on an interface or range of interfaces. Depending on the token used and the value
(in seconds) passed, various timeout configurable parameters are set.
The following tokens are supported:
Tokens Definition
guest-vlan-period The time, in seconds, for which the authenticator waits to see if any EAPOL packets are received on
a port before authorizing the port and placing the port in the guest vlan (if configured). The guest
vlan timer is only relevant when guest vlan has been configured on that specific port.
reauth-period The value, in seconds, of the timer used by the authenticator state machine on this port to determine
when reauthentication of the supplicant takes place. The reauth-period must be a value in the range
1 - 65535.
quiet-period The value, in seconds, of the timer used by the authenticator state machine on this port to define
periods of time in which it will not attempt to acquire a supplicant. The quiet-period must be a value
in the range 0 - 65535.
Switching Commands 468

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Tokens Definition
tx-period The value, in seconds, of the timer used by the authenticator state machine on this port to determine
when to send an EAPOL EAP Request/Identity frame to the supplicant. The quiet-period must be a
value in the range 1 - 65535.
supp-timeout The value, in seconds, of the timer used by the authenticator state machine on this port to timeout
the supplicant. The supp-timeout must be a value in the range 1 - 65535.
server-timeout The value, in seconds, of the timer used by the authenticator state machine on this port to timeout
the authentication server. The supp-timeout must be a value in the range 1 - 65535.
Default guest-vlan-period: 90 seconds
reauth-period: 3600 seconds
quiet-period: 60 seconds
tx-period: 30 seconds
supp-timeout: 30 seconds
server-timeout: 30 seconds
Format dot1x timeout {{guest-vlan-period seconds} |{reauth-period seconds} |
{quiet-period seconds} | {tx-period seconds} | {supp-timeout seconds} |
{server-timeout seconds}}
Mode Interface Config
no dot1x timeout
This command sets the value, in seconds, of the timer used by the authenticator state
machine on this port to the default values. Depending on the token used, the corresponding
default values are set.
Format no dot1x timeout {guest-vlan-period | reauth-period | quiet-period |
tx-period | supp-timeout | server-timeout}
Mode Interface Config
dot1x unauthenticated-vlan
Use this command to configure the unauthenticated VLAN associated with the specified
interface or range of interfaces. The unauthenticated VLAN ID can be a valid VLAN ID from
0 to 4093. The unauthenticated VLAN must be statically configured in the VLAN database to
be operational. By default, the unauthenticated VLAN is 0, that is, invalid and not operational.
Default 0
Format dot1x unauthenticated-vlan vlan-id
Mode Interface Config
Switching Commands 469

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dot1x unauthenticated-vlan
This command resets the unauthenticated-vlan associated with the port to its default value.
Format no dot1x unauthenticated-vlan
Mode Interface Config
dot1x user
This command adds the specified user to the list of users with access to the specified port or
all ports. The user argument must be a configured user.
Format dot1x user user {unit/slot/port | all}
Mode Global Config
no dot1x user
This command removes the user from the list of users with access to the specified port or all
ports.
Format no dot1x user user {unit/slot/port | all}
Mode Global Config
authentication enable
This command globally enables the Authentication Manager. Interface configuration takes
effect only if the Authentication Manager is enabled with this command.
Default Disabled
Format authentication enable
Mode Global Config
no authentication enable
This command disables the Authentication Manager.
Format no authentication enable
Mode Global Config
authentication order
This command sets the order of authentication methods used on a port. The available
authentication methods are Dot1x, MAB, and captive portal. Ordering sets the order of
methods that the switch attempts when trying to authenticate a new device connected to a
port. If one method is unsuccessful or timed out, the next method is attempted.
Switching Commands 470

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Each method can only be entered once. Ordering is only possible between 802.1x and MAB.
Captive portal can be configured either as a stand-alone method or as the last method in the
order.
Format authentication order {dot1x [mab [captive-portal] | captive-portal] | mab
[dot1x [captive-portal]| captive-portal] | captive-portal}
Mode Interface Config
no authentication order
This command returns the port to the default authentication order.
Format no authentication order
Mode Interface Config
authentication priority
This command sets the priority for the authentication methods used on a port. The available
authentication methods are Dot1x, MAB, and captive portal. The authentication priority
decides if a previously authenticated client is reauthenticated with a higher-priority method
when the same is received. Captive portal is always the last method in the list.
Default authentication order dot1x mab captive portal
Format authentication priority {dot1x [mab [captive portal] | captive portal] | mab
[dot1x [captive portal]| captive portal] | captive portal}
Mode Interface Config
no authentication priority
This command returns the port to the default order of priority for the authentication methods.
Format no authentication priority
Mode Interface Config
authentication restart
This command sets the time, in seconds, after which reauthentication starts. The range is
300–65535 seconds and the default time is 300 seconds. The timer restarts the
authentication only after all the authentication methods fail. At the expiration of this timer,
authentication is reinitiated for the port.
Format authentication restart seconds
Mode Interface Config
Switching Commands 471

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no authentication restart
This command sets the reauthentication value to the default value of 3600 seconds.
Format no authentication restart
Mode Interface Config
show authentication authentication-history
Use this command to display information about the authentication history for a specified
interface.
Format show authentication authentication-history unit/slot/port
Mode Privileged EXEC
Term Definition
Time Stamp The time of the authentication.
Interface The interface.
MAC-Address The MAC address for the interface.
Auth Status Method The authentication method and status for the interface.
Command example:
Time Stamp Interface MAC-Address Auth Status Method
--------------------- --------- ----------------- ------ ------------
Jul 21 1919 15:06:15 1/0/1 00:00:00:00:00:01 Authorized 802.1X
show authentication interface
Use this command to display authentication method information either for all interfaces or a
specified port.
Format show authentication interface {all | unit/slot/port}
Mode Privileged EXEC
The following information is displayed for each interface.
Term Definition
Interface The interface for which authentication configuration information is displayed.
Authentication Restart timer The time, in seconds, after which reauthentication starts.
Configured method order The order of authentication methods used on a port.
Switching Commands 472

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Enabled method order The order of authentication methods used on a port.
Configured method priority The priority for the authentication methods used on a port.
Enabled method priority The priority for the authentication methods used on a port.
Number of authenticated clients The number of authenticated clients.
Logical Interface The logical interface
Client MAC addr The MAC address for the client.
Authenticated Method The current authentication method.
Auth State If the authentication was successful.
Auth Status The current authentication status.
Command example:
(NETGEAR Switch) #show authentication interface all
Interface...................................... 1/0/1
Authentication Restart timer................... 300
Configured method order........................ dot1x mab captive-portal
Enabled method order........................... dot1x mab undefined
Configured method priority..................... undefined undefined undefined
Enabled method priority........................ undefined undefined undefined
Number of authenticated clients................ 0
Interface...................................... 1/0/2
Authentication Restart timer................... 300
Configured method order........................ dot1x mab captive-portal
Enabled method order........................... dot1x mab undefined
Configured method priority..................... undefined undefined undefined
Enabled method priority........................ undefined undefined undefined
Number of authenticated clients................ 0
Interface...................................... 1/0/3
Authentication Restart timer................... 300
Configured method order........................ dot1x mab captive-portal
Enabled method order........................... dot1x mab undefined
Configured method priority..................... undefined undefined undefined
Enabled method priority........................ undefined undefined undefined
Number of authenticated clients................ 0
Interface...................................... 1/0/4
Authentication Restart timer................... 300
Configured method order........................ dot1x mab captive-portal
Enabled method order........................... dot1x mab undefined
Configured method priority..................... undefined undefined undefined
Enabled method priority........................ undefined undefined undefined
Number of authenticated clients................ 0
Switching Commands 473
