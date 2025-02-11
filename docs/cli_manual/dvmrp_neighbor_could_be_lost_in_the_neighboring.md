# dvmrp_neighbor_could_be_lost_in_the_neighboring

Pages: 1132-1133

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 66. DVMRP Log Messages (continued)
Component Message Cause
DVMRP DVMRP Prune Control message Send Failed; Neighbor - %s, SrcAddr - %s, GrpAddr - %s DVMRP
rtrIfNum – xxx. Prune control message send failed. This could
mostly be because of a Failure return status of the
socket call sendto(). As a result of this, the unwanted
multicast traffic is still received and forwarded.
DVMRP DVMRP Probe Control message Send Failed on DVMRP Probe control message send failed. This
rtrIfNum –xxx. could mostly be because of a Failure return status of
the socket call sendto(). As a result of this, the
DVMRP neighbor could be lost in the neighboring
DVMRP routers.
Stacking
Table 67. EDB Log Message
Component Message Cause
EDB EDB Callback: Unit Join: num. Unit num joined the stack.
Technologies
T able 68. Error Messages
Component Message Cause
OS I nvalid USP unit = x, slot = x, port =x A port was not able to be translated correctly
during the receive.
OS In hapiBroadSystemMacAddress call to Failed to add an L2 address to the MAC table.
'bcm_l2_addr_add' - FAILED : x This should only happen when a hash collision
occurs or the table is full.
OS Failed installing mirror action - rest of the policy A previously configured probe port is not being
applied successfully used in the policy. The release notes state that
only a single probe port can be configured.
OS Policy x does not contain rule x The rule was not added to the policy due to a
discrepancy in the rule count for this specific
policy. Additionally, the message can be
displayed when an old rule is being modified, but
the old rule is not in the policy.
Switch Software Log Messages 1132

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 68. Error Messages (continued)
Component Message Cause
OS ERROR: policy x, tmpPolicy x, size x, data x x x x An issue installing the policy due to a possible
x x x x duplicate hash.
OS ACL x not found in internal table Attempting to delete a non-existent ACL.
OS ACL internal table overflow Attempting to add an ACL to a full table.
OS In hapiBroadQosCosQueueConfig, Failed to Attempting to configure the bandwidth beyond it’s
configure minimum bandwidth. Available capabilities.
bandwidth x
OS USL: failed to put sync response on queue A response to a sync request was not enqueued.
This could indicate that a previous sync request
was received after it was timed out.
OS U SL: failed to sync ipmc table on unit= x Either the transport failed or the message was
dropped.
OS usl_task_ipmc_msg_send(): failed to send with x Either the transport failed or the message was
dropped.
OS USL: No available entries in the STG table The Spanning Tree Group table is full in USL.
OS U SL: failed to sync stg table on unit= x Could not synchronize unit x due to a transport
failure or API issue on remote unit. A
synchronization retry will be issued.
OS USL: A Trunk doesn't exist in USL Attempting to modify a Trunk that doesn’t exist.
OS USL: A Trunk being created by bcmx already Possible synchronization issue between the
existed in USL application, hardware, and sync layer.
OS USL: A Trunk being destroyed doesn't exist in Possible synchronization issue between the
USL application, hardware, and sync layer.
OS USL: A Trunk being set doesn't exist in USL Possible synchronization issue between the
application, hardware, and sync layer.
OS U SL: failed to sync trunk table on unit= x Could not synchronize unit x due to a transport
failure or API issue on remote unit. A
synchronization retry will be issued.
OS USL: Mcast entry not found on a join Possible synchronization issue between the
application, hardware, and sync layer.
OS USL: Mcast entry not found on a leave Possible synchronization issue between the
application, hardware, and sync layer.
OS U SL: failed to sync dVLAN data on unit= x Could not synchronize unit x due to a transport
failure or API issue on remote unit. A
synchronization retry will be issued.
OS U SL: failed to sync policy table on unit= x Could not synchronize unit x due to a transport
failure or API issue on remote unit. A
synchronization retry will be issued.
Switch Software Log Messages 1133
