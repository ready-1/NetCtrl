# dhcp_relay_request_hops_field_more_than_config_value_the_dhcp_relay_agent_has_processed_a__6779f942

Pages: 1124-1125

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 54. DiffServ Log Messages
Component Message Cause
DiffServ diffserv.c 165: diffServRestore Failed to reset While attempting to clear the running
DiffServ. Recommend resetting device configuration an error was encountered in
removing the current settings. This may lead to
an inconsistent state in the system and resetting
is advised.
DiffServ Policy invalid for service intf: policy name, The DiffServ policy definition is not compatible
interface x, direction y with the capabilities of the interface specified.
Check the platform release notes for information
on configuration limitations.
Routing/IPv6 Routing
Table 55. DHCP Relay Log Messages
Component Message Cause
DHCP relay REQUEST hops field more than config value The DHCP relay agent has processed a DHCP
request whose HOPS field is larger than the
maximum value allowed. The relay agent will not
forward a message with a hop count greater than
4.
DHCP relay Request's seconds field less than the config The DHCP relay agent has processed a DHCP
value request whose SECS field is larger than the
configured minimum wait time allowed.
DHCP relay processDhcpPacket: invalid DHCP packet type: The DHCP relay agent has processed an invalid
%u\n DHCP packet. Such packets are discarded by
the relay agent.
Table 56. OSPFv2 Log Messages
Component Message Cause
OSPFv2 Best route client deregistration failed for OSPF OSPFv2 registers with the IPv4 routing table
Redist manager (“RTO”) to be notified of best route
changes. There are cases where OSPFv2
deregisters more than once, causing the second
deregistration to fail. The failure is harmless.
OSPFv2 XX_Call() failure in _checkTimers for thread An OSPFv2 timer has fired but the message
0x869bcc0 queue that holds the event has filled up. This is
normally a fatal error.
Switch Software Log Messages 1124

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 56. OSPFv2 Log Messages (continued)
Component Message Cause
OSPFv2 Warning: OSPF LSDB is 90% full (22648 LSAs). OSPFv2 limits the number of Link State
Advertisements (LSAs) that can be stored in the
link state database (LSDB). When the database
becomes 90 or 95 percent full, OSPFv2 logs this
warning. The warning includes the current size of
the database.
OSPFv2 The number of LSAs, 25165, in the OSPF LSDB When the OSPFv2 LSDB becomes full, OSPFv2
has exceeded the LSDB memory allocation. logs this message. OSPFv2 reoriginates its
router LSAs with the metric of all non-stub links
set to the maximum value to encourage other
routers to not compute routes through the
overloaded router.
OSPFv2 Dropping the DD packet because of MTU OSPFv2 ignored a Database Description packet
mismatch whose MTU is greater than the IP MTU on the
interface where the DD was received.
OSPFv2 LSA Checksum error in LsUpdate, dropping LSID OSPFv2 ignored a received link state
1.2.3.4 checksum 0x1234. advertisement (LSA) whose checksum was
incorrect.
Table 57. OSPFv3 Log Messages
Component Message Cause
OSPFv3 Best route client deregistration failed for OSPFv3 OSPFv3 registers with the IPv6 routing table
Redist manager (“RTO6”) to be notified of best route
changes. There are cases where OSPFv3
deregisters more than once, causing the second
deregistration to fail. The failure is harmless.
OSPFv3 Warning: OSPF LSDB is 90% full (15292 LSAs). OSPFv3 limits the number of Link State
Advertisements (LSAs) that can be stored in the
link state database (LSDB). When the database
becomes 90 or 95 percent full, OSPFv3 logs this
warning. The warning includes the current size of
the database.
OSPFv3 The number of LSAs, 16992, in the OSPF LSDB When the OSPFv3 LSDB becomes full, OSPFv3
has exceeded the LSDB memory allocation. logs this message. OSPFv3 reoriginates its
router LSAs with the R-bit clear indicating that
OSPFv3 is overloaded.
OSPFv3 LSA Checksum error detected for LSID 1.2.3.4 OSPFv3 periodically verifies the checksum of
checksum 0x34f5. OSPFv3 Database may be each LSA in memory. OSPFv3 logs this.
corrupted.
Switch Software Log Messages 1125
