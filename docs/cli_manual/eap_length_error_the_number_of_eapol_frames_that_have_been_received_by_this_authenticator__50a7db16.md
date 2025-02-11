# eap_length_error_the_number_of_eapol_frames_that_have_been_received_by_this_authenticator__50a7db16

Pages: 480-484

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Last EAPOL Frame The protocol version number carried in the most recently received EAPOL frame.
Version
Last EAPOL Frame The source MAC address carried in the most recently received EAPOL frame.
Source
EAP Response/Id The number of EAP response/identity frames that have been received by this authenticator.
Frames Received
EAP Response The number of valid EAP response frames (other than resp/id frames) that have been received by
Frames Received this authenticator.
EAP Request/Id The number of EAP request/identity frames that have been transmitted by this authenticator.
Frames
Transmitted
EAP Request The number of EAP request frames (other than request/identity frames) that have been transmitted
Frames by this authenticator.
Transmitted
Invalid EAPOL The number of EAPOL frames that have been received by this authenticator in which the frame type
Frames Received is not recognized.
EAP Length Error The number of EAPOL frames that have been received by this authenticator in which the frame type
Frames Received is not recognized.
show dot1x authentication-history
This command displays 802.1X authentication events and information during successful and
unsuccessful Dot1x authentication process for all interfaces or the specified interface. Use
the optional keywords to display only failure authentication events in summary or in detail.
Format show dot1x authentication-history {unit/slot/port | all} [failed-auth-only]
[detail]
Mode Privileged EXEC
Term Definition
Time Stamp The exact time at which the event occurs.
Interface Physical Port on which the event occurs.
Mac-Address The supplicant/client MAC address.
VLAN assigned The VLAN assigned to the client/port on authentication.
VLAN assigned The type of VLAN ID assigned, which can be Guest VLAN, Unauth, Default, RADIUS Assigned, or
Reason Monitor Mode VLAN ID.
Auth Status The authentication status.
Reason The actual reason behind the successful or failed authentication.
Switching Commands 480

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show dot1x clients
This command displays 802.1X client information. This command also displays information
about the number of clients that are authenticated using Monitor mode and using 802.1X.
Format show dot1x clients {unit/slot/port | all}
Mode Privileged EXEC
Term Definition
Clients Authenticated Indicates the number of the Dot1x clients authenticated using Monitor mode.
using Monitor Mode
Clients Authenticated Indicates the number of Dot1x clients authenticated using 802.1x authentication process.
using Dot1x
Logical Interface The logical port number associated with a client.
Interface The physical port to which the supplicant is associated.
User Name The user name used by the client to authenticate to the server.
Supplicant MAC The supplicant device MAC address.
Address
Session Time The time since the supplicant is logged on.
Filter ID Identifies the Filter ID returned by the RADIUS server when the client was authenticated. This
is a configured DiffServ policy name on the switch.
VLAN ID The VLAN assigned to the port.
VLAN Assigned The reason the VLAN identified in the VLAN ID field has been assigned to the port. Possible
values are RADIUS, Unauthenticated VLAN, Monitor Mode, or Default. When the VLAN
Assigned reason is Default, it means that the VLAN was assigned to the port because the
P-VID of the port was that VLAN ID.
Session Timeout This value indicates the time for which the given session is valid. The time period in seconds is
returned by the RADIUS server on authentication of the port. This value is valid for the port
only when the port-control mode is not MAC-based.
Session Termination This value indicates the action to be taken once the session timeout expires. Possible values
Action are Default and Radius-Request. If the value is Default, the session is terminated and client
details are cleared. If the value is Radius-Request, then a reauthentication of the client is
performed.
show dot1x users
This command displays 802.1X port security user information for locally configured users.
Format show dot1x users unit/slot/port
Mode Privileged EXEC
Switching Commands 481

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Users Users configured locally to have access to the specified port.
802.1X Supplicant Commands
The switch supports 802.1X (dot1x) supplicant functionality on point-to-point ports. The
administrator can configure the user name and password used in authentication and
capabilities of the supplicant port.
dot1x pae
This command sets the port’s dot1x role. The port can serve as either a supplicant or an
authenticator.
Format dot1x pae {supplicant | authenticator}
Mode Interface Config
dot1x supplicant port-control
This command sets the ports authorization state (Authorized or Unauthorized) either
manually or by setting the port to auto-authorize upon startup. By default all the ports are
authenticators. If the port’s attribute needs to be moved from authenticator to supplicant or
from supplicant to authenticator, use this command.
Format dot1x supplicant port-control {auto | force-authorized | force-unauthorized}
Mode Interface Config
Parameter Description
auto The port is in the Unauthorized state until it presents its user name and password credentials to an
authenticator. If the authenticator authorizes the port, then it is placed in the Authorized state.
force-authorized Sets the authorization state of the port to Authorized, bypassing the authentication process.
force-unauthorized Sets the authorization state of the port to Unauthorized, bypassing the authentication process.
no dot1x supplicant port-control
This command sets the port-control mode to the default, auto.
Default auto
Format no dot1x supplicant port-control
Mode Interface Config
Switching Commands 482

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
dot1x supplicant max-start
This command configures the number of attempts that the supplicant makes to find the
authenticator before the supplicant assumes that there is no authenticator. The number of
attempts can be in a range from 1–10. The default is 3 attempts.
Default 3
Format dot1x supplicant max-start number
Mode Interface Config
no dot1x supplicant max-start
This command sets the max-start value to the default.
Format no dot1x supplicant max-start
Mode Interface Config
dot1x supplicant timeout start-period
This command configures the start period timer interval to wait for the EAP identity request
from the authenticator. The interval can be in a range from 1–65535 seconds. The default is
30 seconds.
Default 30 seconds
Format dot1x supplicant timeout start-period seconds
Mode Interface Config
no dot1x supplicant timeout start-period
This command sets the start-period value to the default.
Format no dot1x supplicant timeout start-period
Mode Interface Config
dot1x supplicant timeout held-period
This command configures the held period timer interval to wait for the next authentication on
previous authentication fail. The interval can be in a range from 1–65535 seconds. The
default is 30 seconds.
Default 60 seconds
Format dot1x supplicant timeout held-period seconds
Mode Interface Config
Switching Commands 483

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no dot1x supplicant timeout held-period
This command sets the held-period value to the default value.
Format no dot1x supplicant timeout held-period
Mode Interface Config
dot1x supplicant timeout auth-period
This command configures the authentication period timer interval to wait for the next EAP
request challenge from the authenticator. The interval can be in a range from 1–65535
seconds. The default is 30 seconds.
Default 30 seconds
Format dot1x supplicant timeout auth-period seconds
Mode Interface Config
no dot1x supplicant timeout auth-period
This command sets the auth-period value to the default value.
Format no dot1x supplicant timeout auth-period
Mode Interface Config
dot1x supplicant user
Use this command to map the given user to the port.
Format dot1x supplicant user
Mode Interface Config
show dot1x statistics
This command displays the dot1x port statistics in detail.
Format show dot1x statistics unit/slot/port
Mode Privileged EXEC
User EXEC
Term Definition
EAPOL Frames Received Displays the number of valid EAPOL frames received on the port.
EAPOL Frames Transmitted Displays the number of EAPOL frames transmitted via the port.
Switching Commands 484
