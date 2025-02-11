# igmp_snooping_failed_to_set_global_igmp_snooping_mode_to_xxx_failed_to_set_global_igmp_sno_adab7b3f

Pages: 1118-1123

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 40. 802.1X Log Messages
Component Message Cause
802.1X dot1xApplyConfigData: Unable to enable/disable DTL call failed enabling/disabling 802.1X.
dot1x in driver
802.1X dot1xSendRespToServer: Failed sending message to RADIUS server.
dot1xRadiusAccessRequestSend failed
802.1X dot1xRadiusAcceptProcess: error calling Failed sending accounting start to RADIUS
r adiusAccountingStart, ifIndex= xxx server.
802.1X function: failed sending terminate cause, intf xxx Failed sending accounting stop to RADIUS
server.
T able 41. IGMP Snooping Log Messages
Component Message Cause
IGMP Snooping function: osapiMessageSend failed IGMP Snooping message queue is full.
IGMP Snooping Failed to set global igmp snooping mode to xxx Failed to set global IGMP Snooping mode due to
message queue being full.
IGMP Snooping Failed to set igmp snooping mode xxx for Failed to set interface IGMP Snooping mode due
interface yyy to message queue being full.
IGMP Snooping Failed to set igmp mrouter mode xxx for interface Failed to set interface multicast router mode due
yyy to IGMP Snooping message queue being full.
IGMP Snooping Failed to set igmp snooping mode xxx for vlan Failed to set VLAN IGM Snooping mode due to
yyy message queue being full.
IGMP Snooping Failed to set igmp mrouter mode%d for interface Failed to set VLAN multicast router mode due to
xxx on Vlan yyy IGMP Snooping message queue being full.
IGMP Snooping snoopCnfgrInitPhase1Process: Error allocating Could not allocate buffers for small IGMP
small buffers packets.
IGMP Snooping snoopCnfgrInitPhase1Process: Error allocating Could not allocate buffers for large IGMP
large buffers packets.
Table 42. GARP/GVRP/GMRP Log Messages
Component Message Cause
GARP/GVRP/ garpSpanState, garpIfStateChange, The garpQueue is full, logs specifics of the
GMRP GarpIssueCmd, garpDot1sChangeCallBack, message content like internal interface number,
garpApiCnfgrCommand, type of message, etc.
garpLeaveAllTimerCallback, garpTimerCallback:
QUEUE SEND FAILURE:
GARP/GVRP/ GarpSendPDU: QUEUE SEND FAILURE The garpPduQueue is full, logs specific of the
GMRP GPDU, internal interface number, vlan id, buffer
handle, etc.
Switch Software Log Messages 1118

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 42. GARP/GVRP/GMRP Log Messages
Component Message Cause
GARP/GVRP/ garpMapIntfIsConfigurable, A default configuration does not exist for this
GMRP gmrpMapIntfIsConfigurable: Error accessing interface. Typically a case when a new interface
GARP/GMRP config data for interface %d in is created and has no preconfiguration.
garpMapIntfIsConfigurable.
GARP/GVRP/ garpTraceMsgQueueUsage: garpQueue usage Traces the build up of message queue. Helpful in
GMRP has exceeded fifty/eighty/ninety percent determining the load on GARP.
GARP/GVRP/ gid_destroy_port: Error Removing port %d Mismatch between the gmd (gmrp database) and
GMRP registration for vlan-mac %d - MFDB.
%02X:%02X:%02X:%02X:%02X:%02X
GARP/GVRP/ gmd_create_entry: GMRP failure adding MFDB MFDB table is full.
GMRP entry: vlan %d and address %s
Table 43. 802.3ad Log Messages
Component Message Cause
802.3ad dot3adReceiveMachine: received default event Received a LAG PDU and the RX state machine
%x is ignoring this LAGPDU.
802.3ad dot3adNimEventCompletionCallback, The event sent to NIM was not completed
dot3adNimEventCreateCompletionCallback: successfully.
DOT3AD: notification failed for event(%d),
intf(%d), reason(%d)
Table 44. FDB Log Message
Component Message Cause
FDB fdbSetAddressAgingTimeOut: Failure setting fid Unable to set the age time in the hardware.
%d address aging timeout to %d
Table 45. Double VLAN Tag Log Message
Component Message Cause
Double Vlan Tag dvlantagIntfIsConfigurable: Error accessing A default configuration does not exist for this
dvlantag config data for interface %d interface. Typically a case when a new interface
is created and has no preconfiguration.
Switch Software Log Messages 1119

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 46. IPv6 Provisioning Log Message
Component Message Cause
IPV6 Provisioning ipv6ProvIntfIsConfigurable: Error accessing IPv6 A default configuration does not exist for this
Provisioning config data for interface %d interface. Typically a case when a new interface
is created and has no preconfiguration.
Table 47. MFDB Log Message
Component Message Cause
MFDB mfdbTreeEntryUpdate: entry does not exist Trying to update a non existing entry.
T able 48. 802.1Q Log Messages
Component Message Cause
802.1Q dot1qIssueCmd: Unable to send message %d to dot1qMsgQueue is full.
dot1qMsgQueue for vlan %d - %d msgs in queue
802.1Q dot1qVlanCreateProcess: Attempt to create a vlan This accommodates for reserved vlan ids. i.e.
with an invalid vlan id %d ; 4094 - x.
VLAN %d not in range,
802.1Q dot1qMapIntfIsConfigurable: Error accessing A default configuration does not exist for this
DOT1Q config data for interface %d in interface. Typically a case when a new interface
dot1qMapIntfIsConfigurable. is created and has no preconfiguration.
802.1Q dot1qVlanDeleteProcess: Deleting the default VLAN Typically encountered during clear Vlan and clear
config.
802.1Q dot1qVlanMemberSetModify, If this vlan is a learnt via GVRP then we cannot
dot1qVlanTaggedMemberSetModify: Dynamic entry modify its member set via management.
%d can only be modified after it is converted to static
802.1Q dtl failure when adding ports to vlan id %d - Failed to add the ports to VLAN entry in
portMask = %s hardware.
802.1Q dtl failure when deleting ports from vlan id %d - Failed to delete the ports for a VLAN entry from
portMask = %s the hardware.
802.1Q dtl failure when adding ports to tagged list for vlan id Failed to add the port to the tagged list in
%d - portMask = %s hardware.
802.1Q dtl failure when deleting ports from tagged list for Failed to delete the port to the tagged list from
vlan id %d - portMask = %s" the hardware.
802.1Q dot1qTask: unsuccessful return code on receive Failed to receive the dot1q message from dot1q
from dot1qMsgQueue: %08x" message queue.
802.1Q Unable to apply VLAN creation request for VLAN ID Failed to create VLAN ID, VLAN Database
%d, Database reached MAX VLAN count! reached maximum values.
Switch Software Log Messages 1120

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 48. 802.1Q Log Messages (continued)
Component Message Cause
802.1Q Attempt to create a vlan (%d) that already exists Creation of the existing Dynamic VLAN ID from
the CLI.
802.1Q DTL call to create VLAN %d failed with rc %d" Failed to create VLAN ID in hardware.
802.1Q Problem unrolling data for VLAN %d Failed to delete VLAN from the VLAN database
after failure of VLAN hardware creation.
802.1Q VLan %d does not exist Failed to delete VLAN entry.
802.1Q VLan %d requestor type %d does not exist Failed to delete dynamic VLAN ID if the given
requestor is not valid.
802.1Q Can not delete the VLAN, Some unknown Failed to delete, as some unknown component
component has taken the ownership! has taken the ownership.
802.1Q Not valid permission to delete the VLAN %d Failed to delete the VLAN ID as the given
requestor %d requestor and VLAN entry status are not same.
802.1Q VLAN Delete Call failed in driver for vlan %d Failed to delete VLAN ID from the hardware.
802.1Q Problem deleting data for VLAN %d Failed to delete VLAN ID from the VLAN
database.
802.1Q Dynamic entry %d can only be modified after it is Failed to modify the VLAN group filter
converted to static
802.1Q Cannot find vlan %d to convert it to static Failed to convert Dynamic VLAN to static VLAN.
VLAN ID not exists.
802.1Q Only Dynamically created VLANs can be converted Error while trying to convert the static created
VLAN ID to static.
802.1Q Cannot modify tagging of interface %s to non Error for a given interface sets the tagging
existence vlan %d" property for all the VLANs in the vlan mask.
802.1Q Error in updating data for VLAN %d in VLAN Failed to add VLAN entry into VLAN database.
database
802.1Q DTL call to create VLAN %d failed with rc %d Failed to add VLAN entry in hardware.
802.1Q Not valid permission to delete the VLAN %d Failed to delete static VLAN ID. Invalid requestor.
802.1Q Attempt to set access vlan with an invalid vlan id %d Invalid VLAN ID.
802.1Q Attempt to set access vlan with (%d) that does not VLAN ID not exists.
exist
802.1Q VLAN create currently underway for VLAN ID %d Creating a VLAN which is already under process
of creation.
802.1Q VLAN ID %d is already exists as static VLAN Trying to create already existing static VLAN ID.
802.1Q Cannot put a message on dot1q msg Queue, Failed to send Dot1q message on Dot1q
Returns:%d message Queue.
802.1Q Invalid dot1q Interface: %s Failed to add VLAN to a member of port.
Switch Software Log Messages 1121

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 48. 802.1Q Log Messages (continued)
Component Message Cause
802.1Q Cannot set membership for user interface %s on Failed to add VLAN to a member of port.
management vlan %d
802.1Q Incorrect tagmode for vlan tagging. tagmode: %d Incorrect tagmode for VLAN tagging.
Interface: %s
802.1Q Cannot set tagging for interface %d on non existent The VLAN ID does not exist.
VLAN %d"
802.1Q Cannot set tagging for interface %d which is not a Failure in Setting the tagging configuration for a
member of VLAN %d interface on a range of VLAN.
802.1Q VLAN create currently underway for VLAN ID %d" Trying to create the VLAN ID which is already
under process of creation.
802.1Q VLAN ID %d already exists Trying to create the VLAN ID which is already
exists.
802.1Q Failed to delete, Default VLAN %d cannot be Trying to delete Default VLAN ID.
deleted
802.1Q Failed to delete, VLAN ID %d is not a static VLAN Trying to delete Dynamic VLAN ID from CLI.
802.1Q Requestor %d attempted to release internal VLAN -
%d: owned by %d
Table 49. 802.1S Log Messages
Component Message Cause
802.1S dot1sIssueCmd: Dot1s Msg Queue is The message Queue is full.
full!!!!Event: %u, on interface: %u, for instance:
%u
802.1S dot1sStateMachineRxBpdu(): Rcvd BPDU The current conditions, like port is not enabled or
Discarded we are currently not finished processing another
BPDU on the same interface, does not allow us
to process this BPDU.
802.1S dot1sBpduTransmit(): could not get a buffer Out of system buffers.
T able 50. Port Mac Locking Log Message
Component Message Cause
Port Mac Locking pmlMapIntfIsConfigurable: Error accessing PML A default configuration does not exist for this
config data for interface %d in interface. Typically a case when a new interface
pmlMapIntfIsConfigurable. is created and has no preconfiguration.
Switch Software Log Messages 1122

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 51. Protocol-based VLANs Log Messages
Component Message Cause
Protocol Based pbVlanCnfgrInitPhase2Process: Unable to Appears when nimRegisterIntfChange fails to
VLANs register NIM callback register pbVlan for link state changes.
Protocol Based pbVlanCnfgrInitPhase2Process: Unable to Appears when VLANRegisterForChange fails to
VLANs register pbVlan callback with VLANs register pbVlan for VLAN changes.
Protocol Based pbVlanCnfgrInitPhase2Process: Unable to Appears when nvStoreRegister fails to register
VLANs register pbVlan callback with nvStore save and restore functions for configuration save.
QoS
Table 52. ACL Log Messages
Component Message Cause
ACL Total number of ACL rules (x) exceeds max (y) The combination of all ACLs applied to an
on intf i. interface has resulted in requiring more rules
than the platform supports.
ACL ACL name, rule x: This rule is not being logged The ACL configuration has resulted in a
requirement for more logging rules than the
platform supports. The specified rule is
functioning normally except for the logging
action.
ACL aclLogTask: error logging ACL rule trap for The system was unable to send an SNMP trap
correlator number for this ACL rule which contains a logging
attribute.
ACL IP ACL number: Forced truncation of one or While processing the saved configuration, the
more rules during config migration system encountered an ACL with more rules than
is supported by the current version. This may
happen when code is updated to a version
supporting fewer rules per ACL than the previous
version.
Table 53. CoS Log Message
Component Message Cause
COS cosCnfgrInitPhase3Process: Unable to apply The COS component was unable to apply the
saved config -- using factory defaults saved configuration and has initialized to the
factory default settings.
Switch Software Log Messages 1123
