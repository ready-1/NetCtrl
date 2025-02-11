# vlan_assignment_indicates_whether_assignment_of_an_authorized_port_to_a_radius-assigned_vl_d11f7a4e

Pages: 476-479

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format show dot1x [{summary {unit/slot/port | all} | detail unit/slot/port |
statistics unit/slot/port}]
Mode Privileged EXEC
If you do not use the optional parameters unit/slot/port, the command displays the
global dot1x mode, the VLAN Assignment mode, and the Dynamic VLAN Creation mode.
Term Definition
Administrative Indicates whether authentication control on the switch is enabled or disabled.
Mode
VLAN Assignment Indicates whether assignment of an authorized port to a RADIUS-assigned VLAN is allowed
Mode (enabled) or not (disabled).
Dynamic VLAN Indicates whether the switch can dynamically create a RADIUS-assigned VLAN if it does not
Creation Mode currently exist on the switch.
Monitor Mode Indicates whether the Dot1x Monitor mode on the switch is enabled or disabled.
If you use the optional parameter summary {unit/slot/port | all}, the dot1x
configuration for the specified port or all ports are displayed.
Term Definition
Interface The interface whose configuration is displayed.
Control Mode The configured control mode for this port. Possible values are force-unauthorized, force-authorized,
auto, mac-based, authorized, and unauthorized.
Operating Control The control mode under which this port is operating. Possible values are authorized and
Mode unauthorized.
Reauthentication Indicates whether reauthentication is enabled on this port.
Enabled
Port Status Indicates whether the port is authorized or unauthorized. Possible values are authorized and
unauthorized.
Command example:
(NETGEAR Switch) #show dot1x summary 0/1
Operating
Interface Control Mode Control Mode Port Status
- -------- ------------ - ---------- ------------
0/1 a uto a uto Authorized
Switching Commands 476

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If you use the optional parameter detail unit/slot/port, the detailed dot1x
configuration for the specified port is displayed.
Term Definition
Port The interface whose configuration is displayed.
Protocol Version The protocol version associated with this port. The only possible value is 1, corresponding to the first
version of the dot1x specification.
PAE Capabilities The port access entity (PAE) functionality of this port. Possible values are Authenticator or
Supplicant.
Control Mode The configured control mode for this port. Possible values are force-unauthorized, force-authorized,
auto, and mac-based.
Authenticator PAE Current state of the authenticator PAE state machine. Possible values are Initialize, Disconnected,
State Connecting, Authenticating, Authenticated, Aborting, Held, ForceAuthorized, and
ForceUnauthorized. When MAC-based authentication is enabled on the port, this parameter is
deprecated.
Backend Current state of the backend authentication state machine. Possible values are Request, Response,
Authentication Success, Fail, Timeout, Idle, and Initialize. When MAC-based authentication is enabled on the port,
State this parameter is deprecated.
Quiet Period The timer used by the authenticator state machine on this port to define periods of time in which it
will not attempt to acquire a supplicant. The value is expressed in seconds and will be in the range 0
and 65535.
Transmit Period The timer used by the authenticator state machine on the specified port to determine when to send
an EAPOL EAP Request/Identity frame to the supplicant. The value is expressed in seconds and will
be in the range of 1 and 65535.
Guest-VLAN ID The guest VLAN identifier configured on the interface.
Guest VLAN Period The time in seconds for which the authenticator waits before authorizing and placing the port in the
Guest VLAN, if no EAPOL packets are detected on that port.
Supplicant Timeout The timer used by the authenticator state machine on this port to timeout the supplicant. The value is
expressed in seconds and will be in the range of 1 and 65535.
Server Timeout The timer used by the authenticator on this port to timeout the authentication server. The value is
expressed in seconds and will be in the range of 1 and 65535.
Maximum The maximum number of times the authenticator state machine on this port will retransmit an
Requests EAPOL EAP Request/Identity before timing out the supplicant. The value will be in the range of 1
and 10.
Configured MAB The administrative mode of the MAC authentication bypass feature on the switch.
Mode
Operational MAB The operational mode of the MAC authentication bypass feature on the switch. MAB might be
Mode administratively enabled but not operational if the control mode is not MAC based.
Vlan-ID The VLAN assigned to the port by the radius server. This is only valid when the port control mode is
not Mac-based.
Switching Commands 477

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
VLAN Assigned The reason the VLAN identified in the VLAN-assigned field has been assigned to the port. Possible
Reason values are RADIUS, Unauthenticated VLAN, Guest VLAN, default, and Not Assigned. When the
VLAN Assigned Reason is Not Assigned, it means that the port has not been assigned to any VLAN
by dot1x. This only valid when the port control mode is not MAC-based.
Reauthentication The timer used by the authenticator state machine on this port to determine when reauthentication of
Period the supplicant takes place. The value is expressed in seconds and will be in the range of 1 and
65535.
Reauthentication Indicates if reauthentication is enabled on this port. Possible values are True and False.
Enabled
Key Transmission Indicates if the key is transmitted to the supplicant for the specified port. Possible values are True or
Enabled False.
EAPOL Flood Indicates whether the EAPOL flood support is enabled on the switch. Possible values are True and
Mode Enabled False.
Control Direction The control direction for the specified port or ports. Possible values are both and in.
Maximum Users The maximum number of clients that can get authenticated on the port in the MAC-based dot1x
authentication mode. This value is used only when the port control mode is not MAC-based.
Unauthenticated Indicates the unauthenticated VLAN configured for this port. This value is valid for the port only when
VLAN ID the port control mode is not MAC-based.
Session Timeout Indicates the time for which the given session is valid. The time period in seconds is returned by the
RADIUS server on authentication of the port. This value is valid for the port only when the port
control mode is not MAC-based.
Session This value indicates the action to be taken once the session timeout expires. Possible values are
Termination Action Default, Radius-Request. If the value is Default, the session is terminated the port goes into
unauthorized state. If the value is Radius-Request, then a reauthentication of the client
authenticated on the port is performed. This value is valid for the port only when the port control
mode is not MAC-based.
Command example:
(NETGEAR Switch) #show dot1x detail 1/0/3
Port........................................... 1/0/1
Protocol Version............................... 1
PAE Capabilities............................... Authenticator
Control Mode................................... auto
Authenticator PAE State........................ Initialize
Backend Authentication State................... Initialize
Quiet Period (secs)............................ 60
Transmit Period (secs)......................... 30
Guest VLAN ID.................................. 0
Guest VLAN Period (secs)....................... 90
Supplicant Timeout (secs)...................... 30
Server Timeout (secs).......................... 30
Maximum Requests............................... 2
Switching Commands 478

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Configured MAB Mode............................ Enabled
Operational MAB Mode........................... Disabled
VLAN Id........................................ 0
VLAN Assigned Reason........................... Not Assigned
Reauthentication Period (secs)................. 3600
Reauthentication Enabled....................... FALSE
Key Transmission Enabled....................... FALSE
EAPOL flood Mode Enabled....................... FALSE
Control Direction.............................. both
Maximum Users.................................. 16
Unauthenticated VLAN ID........................ 0
Session Timeout................................ 0
Session Termination Action..................... Default
For each client authenticated on the port, the show dot1x detail unit/slot/port
command displays the following MAC-based dot1x parameters if the port-control mode for
that specific port is MAC-based.
Term Definition
Supplicant The MAC-address of the supplicant.
MAC-Address
Authenticator PAE Current state of the authenticator PAE state machine. Possible values are Initialize, Disconnected,
State Connecting, Authenticating, Authenticated, Aborting, Held, ForceAuthorized, and
ForceUnauthorized.
Backend Current state of the backend authentication state machine. Possible values are Request, Response,
Authentication Success, Fail, Timeout, Idle, and Initialize.
State
VLAN-Assigned The VLAN assigned to the client by the radius server.
Logical Port The logical port number associated with the client.
If you use the optional parameter statistics unit/slot/port, the following dot1x
statistics for the specified port appear.
Term Definition
Port The interface whose statistics are displayed.
EAPOL Frames The number of valid EAPOL frames of any type that have been received by this authenticator.
Received
EAPOL Frames The number of EAPOL frames of any type that have been transmitted by this authenticator.
Transmitted
EAPOL Start The number of EAPOL start frames that have been received by this authenticator.
Frames Received
EAPOL Logoff The number of EAPOL logoff frames that have been received by this authenticator.
Frames Received
Switching Commands 479
