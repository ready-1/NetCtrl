# dscp_value

Pages: 958-960

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Mark IP The mark/re-mark value used as the IP Precedence for traffic matching this class. This is not
Precedence displayed if mark ip precedence is not specified.
Mirror Copies a classified traffic stream to a specified egress port (physical port or LAG). This can occur in
addition to any marking or policing action. It may also be specified along with a QoS queue
assignment.
Non-Conform The current setting for the action taken on a packet considered to not conform to the policing
Action parameters. This is not displayed if policing not in use for the class under this policy.
Non-Conform COS The CoS mark value if the non-conform action is set-cos-transmit.
Non-Conform The DSCP mark value if the non-conform action is set-dscp-transmit.
DSCP Value
Non-Conform IP The IP Precedence mark value if the non-conform action is set-prec-transmit.
Precedence Value
Peak Rate Guarantees a committed rate for transmission, but also transmits excess traffic bursts up to a
user-specified peak rate, with the understanding that a downstream network element (such as the
next hop’s policer) might drop this excess traffic. Traffic is held in queue until it is transmitted or
dropped (per type of queue depth management.) Peak rate shaping can be configured for the
outgoing transmission stream for an AP traffic class (although average rate shaping could also be
used.)
Peak Burst Size (PBS). The network administrator can set the PBS as a means to limit the damage expedited
forwarding traffic could inflict on other traffic (e.g., a token bucket rate limiter) Traffic that exceeds
this limit is discarded.
Policing Style The style of policing, if any, used (simple).
Redirect Forces a classified traffic stream to a specified egress port (physical port or LAG). This can occur in
addition to any marking or policing action. It may also be specified along with a QoS queue
assignment.
If the Policy Name is not specified this command displays a list of all defined DiffServ policies.
The following fields are displayed.
Term Definition
Policy Name The name of this policy. (The order in which the policies are displayed is not necessarily the same
order in which they were created.)
Policy Type The policy type (Only inbound is supported).
Class Members List of all class names associated with this policy.
Command example:
The following example includes the mark-cos-as-sec-cos option that is specified in the policy
action.
(NETGEAR Switch) #show policy-map p1
Policy Name.................................... p1
Policy Type.................................... In
Quality of Service Commands 958

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Class Name..................................... c1
Mark CoS as Secondary CoS...................... Yes
Command example:
The following example includes the mark-cos-as-sec-cos action that is used in the policing
(simple-police, police-single-rate, police two-rate) command.
(NETGEAR Switch) #show policy-map p2
Policy Name....................... p2
Policy Type....................... In
Class Name........................ c2
Policing Style.................... Police Two Rate
Committed Rate.................... 1
Committed Burst Size.............. 1
Peak Rate......................... 1
Peak Burst Size................... 1
Conform Action.................... Mark CoS as Secondary CoS
Exceed Action..................... Mark CoS as Secondary CoS
Non-Conform Action................ Mark CoS as Secondary CoS
Conform Color Mode................ Blind
Exceed Color Mode................. Blind
show diffserv service
This command displays policy service information for the specified interface and direction.
The unit/slot/port parameter specifies a valid unit/slot/port number for the
system.
Format show diffserv service unit/slot/port in
Mode Privileged EXEC
Term Definition
DiffServ Admin The current setting of the DiffServ administrative mode. An attached policy is only in effect on an
Mode interface while DiffServ is in an enabled mode.
Interface unit/slot/port
Direction The traffic direction of this interface service.
Operational Status The current operational status of this DiffServ service interface.
Policy Name The name of the policy attached to the interface in the indicated direction.
Policy Details Attached policy details, whose content is identical to that described for the show policy-map
policymapname command (content not repeated here for brevity).
Quality of Service Commands 959

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show diffserv service brief
This command displays all interfaces in the system to which a DiffServ policy has been
attached. The inbound direction parameter is optional.
Format show diffserv service brief [in]
Mode Privileged EXEC
Term Definition
DiffServ Mode The current setting of the DiffServ administrative mode. An attached policy is only active on an
interface while DiffServ is in an enabled mode.
The following information is repeated for interface and direction (only those interfaces
configured with an attached policy are shown).
Term Definition
Interface unit/slot/port
Direction The traffic direction of this interface service.
OperStatus The current operational status of this DiffServ service interface.
Policy Name The name of the policy attached to the interface in the indicated direction.
show policy-map interface
This command displays policy-oriented statistics information for the specified interface and
direction. The unit/slot/port parameter specifies a valid interface for the system.
Instead of unit/slot/port, lag lag-intf-num can be used as an alternate way to
specify the LAG interface, in which lag-intf-num is the LAG port number.
Note: This command is only allowed while the DiffServ administrative mode
is enabled.
Format show policy-map interface unit/slot/port [in]
Mode Privileged EXEC
Term Definition
Interface unit/slot/port
Direction The traffic direction of this interface service.
Operational Status The current operational status of this DiffServ service interface.
Policy Name The name of the policy attached to the interface in the indicated direction.
Quality of Service Commands 960
