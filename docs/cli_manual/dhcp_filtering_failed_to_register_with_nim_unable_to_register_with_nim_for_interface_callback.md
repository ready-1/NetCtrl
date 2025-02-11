# dhcp_filtering_failed_to_register_with_nim_unable_to_register_with_nim_for_interface_callback

Pages: 1109-1111

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Utilities
Table 20. Trap Mgr Log Message
Component Message Cause
Trap Mgr Link Up/Down: unit/slot/port An interface changed link state.
Table 21. DHCP Filtering Log Messages
Component Message Cause
DHCP Filtering Unable to create r/w lock for DHCP Filtering Unable to create semaphore used for dhcp
filtering configuration structure.
DHCP Filtering Failed to register with nv Store. Unable to register save and restore functions for
configuration save.
DHCP Filtering Failed to register with NIM Unable to register with NIM for interface callback
functions.
DHCP Filtering Error on call to sysapiCfgFileWrite file Error on trying to save configuration.
Table 22. NVStore Log Messages
Component Message Cause
NVStore Building defaults for file XXX A component’s configuration file does not exist or
the file’s checksum is incorrect so the
component’s default configuration file is built.
NVStore Error on call to osapiFsWrite routine on file XXX Either the file cannot be opened or the OS’s file
I/O returned an error trying to write to the file.
NVStore File XXX corrupted from file system. Checksum The calculated checksum of a component’s
mismatch. configuration file in the file system did not match
the checksum of the file in memory.
NVStore Migrating config file XXX from version Y to Z A configuration file version mismatch was
detected so a configuration file migration has
started.
Switch Software Log Messages 1109

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
T able 23. RADIUS Log Messages
Component Message Cause
RADIUS RADIUS: Invalid data length - xxx The RADIUS Client received an invalid message
from the server.
RADIUS RADIUS: Failed to send the request A problem communicating with the RADIUS
server.
RADIUS RADIUS: Failed to send all of the request A problem communicating with the RADIUS
server during transmit.
RADIUS RADIUS: Could not get the Task Sync Resource issue with RADIUS Client service.
semaphore!
RADIUS RADIUS: Buffer is too small for response RADIUS Client attempted to build a response
processing larger than resources allow.
RADIUS RADIUS: Could not allocate accounting Resource issue with RADIUS Client service.
requestInfo
RADIUS RADIUS: Could not allocate requestInfo Resource issue with RADIUS Client service.
RADIUS RADIUS: osapiSocketRecvFrom returned error Error while attempting to read data from the
RADIUS server.
RADIUS RADIUS: Accounting-Response failed to The RADIUS Client received an invalid message
validate, id = xxx from the server.
RADIUS RADIUS: User (xxx) needs to respond for An unexpected challenge was received for a
challenge configured user.
RADIUS RADIUS: Could not allocate a buffer for the Resource issue with RADIUS Client service.
packet
RADIUS RADIUS: Access-Challenge failed to validate, The RADIUS Client received an invalid message
i d= xxx from the server.
RADIUS RADIUS: Failed to validate The RADIUS Client received an invalid message
Message-Authenticator, id = xxx from the server.
RADIUS RADIUS: Access-Accept failed to validate, id= The RADIUS Client received an invalid message
xxx from the server.
RADIUS RADIUS: Invalid packet length – xxx The RADIUS Client received an invalid message
from the server.
RADIUS RADIUS: Response is missing The RADIUS Client received an invalid message
Message-Authenticator, id= xxx from the server.
RADIUS RADIUS: Server address doesn't match RADIUS Client received a server response from
configured server an unconfigured server.
Switch Software Log Messages 1110

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 24. T ACACS+ Log Messages
Component Message Cause
TACACS+ TACACS+: authentication error, no server to TACACS+ request needed, but no servers are
contact configured.
TACACS+ TACACS+: connection failed to server x.x.x.x TACACS+ request sent to server x.x.x.x but no
response was received.
TACACS+ TACACS+: no key configured to encrypt packet No key configured for the specified server.
for server x.x.x.x
TACACS+ TACACS+: received invalid packet type from Received packet type that is not supported.
server.
TACACS+ TACACS+: invalid major version in received Major version mismatch.
packet.
TACACS+ TACACS+: invalid minor version in received Minor version mismatch.
packet.
Table 25. LLDP Log Message
Component Message Cause
LLDP lldpTask(): invalid message type:xx. xxxxxx:xx Unsupported LLDP packet received.
Table 26. SNTP Log Message
Component Message Cause
SNTP SNTP: system clock synchronized on %s UTC Indicates that SNTP has successfully
synchronized the time of the switch with the
server.
Table 27. DHCPv6 Client Log Messages
Component Message Cause
DHCP6 Client ip6Map dhcp add failed. This message appears when the update of a
DHCP leased IP address to IP6Map fails.
DHCP6 Client osapiNetAddrV6Add failed on interface xxx. This message appears when the update of a
DHCP leased IP address fails.
Switch Software Log Messages 1111
