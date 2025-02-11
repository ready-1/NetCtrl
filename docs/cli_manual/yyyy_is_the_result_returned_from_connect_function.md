# yyyy_is_the_result_returned_from_connect_function

Pages: 1115-1116

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 35. SSLT Log Messages
Component Message Cause
SSLT SSLT: Can't connect to unsecure server at XXXX, Failed to open connection to unsecure server.
result = YYYY, errno = ZZZZ XXXX is the unsecure server socket address.
YYYY is the result returned from connect function
and ZZZZ is the error code.
SSLT SSLT: Msg Queue is full, event= XXXX Failed to send the received message to the SSLT
message queue as message queue is full. XXXX
indicates the event to be sent.
SSLT SSLT: Unknown UI event in message, event= Failed to dispatch the received UI event to the
XXXX appropriate SSLT function as it’s an invalid event.
XXXX indicates the event to be dispatched.
SSLT ssltApiCnfgrCommand: Failed calling Failed to send the message to the SSLT
ssltIssueCmd. message queue.
SSLT SSLT: Error loading certificate from file XXXX Failed while loading the SSLcertificate from
specified file. XXXX indicates the file from where
the certificate is being read.
SSLT SSLT: Error loading private key from file Failed while loading private key for SSL
connection.
SSLT SSLT: Error setting cipher list (no valid ciphers) Failed while setting cipher list.
SSLT SSLT: Could not delete the SSL semaphores Failed to delete SSL semaphores during
cleanup.of all resources associated with the
OpenSSL Locking semaphores.
Table 36. User_Manager Log Messages
Component Message Cause
User_Manager User Login Failed for XXXX Failed to authenticate user login. XXXX indicates
the username to be authenticated.
User_Manager Access level for user XXXX could not be Invalid access level specified for the user. The
determined. Setting to READ_ONLY. access level is set to READ_ONLY. XXXX
indicates the username.
User_Manager Could not migrate config file XXXX from version Failed to migrate the config file. XXXX is the
YYYY to ZZZZ. Using defaults. config file name. YYYY is the old version number
and ZZZZ is the new version number.
Switch Software Log Messages 1115

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Switching
T able 37. Protected Ports Log Messages
Component Message Cause
Protected Ports Protected Port: failed to save configuration This appears when the protected port
configuration cannot be saved.
Protected Ports protectedPortCnfgrInitPhase1Process: Unable to This appears when protectedPortCfgRWLock
create r/w lock for protected Port Fails.
Protected Ports protectedPortCnfgrInitPhase2Process: Unable to This appears when nimRegisterIntfChange with
register for VLAN change callback VLAN fails.
Protected Ports Cannot add interface xxx to group yyy This appears when an interface could not be
added to a particular group.
Protected Ports unable to set protected port group This appears when a dtl call fails to add interface
mask at the driver level.
Protected Ports Cannot delete interface xxx from group yyy This appears when a dtl call to delete an
interface from a group fails.
Protected Ports Cannot update group YYY after deleting interface This message appears when an update group for
XXX a interface deletion fails.
Protected Ports Received an interface change callback while not This appears when an interface change call back
ready to receive it has come before the protected port component is
ready.
Table 38. IP Subnet VLANS Log Messages
Component Message Cause
IP subnet VLANs ERROR vlanIpSubnetSubnetValid:Invalid subnet This occurs when an invalid pair of subnet and
netmask has come from the CLI.
IP subnet VLANs IP Subnet Vlans: failed to save configuration This message appears when save configuration
of subnet vlans failed.
IP subnet VLANs vlanIpSubnetCnfgrInitPhase1Process: Unable to This appears when a read/write lock creations
create r/w lock for vlanIpSubnet fails.
IP subnet VLANs vlanIpSubnetCnfgrInitPhase2Process: Unable to This appears when this component unable to
register for VLAN change callback register for vlan change notifications.
IP subnet VLANs vlanIpSubnetCnfgrFiniPhase1Process: could not This appears when a semaphore deletion of this
delete avl semaphore component fails.
IP subnet VLANs vlanIpSubnetDtlVlanCreate: Failed This appears when a dtl call fails to add an entry
into the table.
Switch Software Log Messages 1116
