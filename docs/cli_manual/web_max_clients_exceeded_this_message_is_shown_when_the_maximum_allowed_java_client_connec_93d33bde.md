# web_max_clients_exceeded_this_message_is_shown_when_the_maximum_allowed_java_client_connec_93d33bde

Pages: 1113-1113

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 30. EmW eb Log Messages
Component Message Cause
EmWeb EMWEB (Telnet): Max number of Telnet login A user attempted to connect via telnet when the
sessions exceeded maximum number of telnet sessions were
already active.
EmWeb EMWEB (SSH): Max number of SSH login A user attempted to connect via SSH when the
sessions exceeded maximum number of SSH sessions were already
active.
EmWeb Handle table overflow All the available EmWeb connection handles are
being used and the connection could not be
made.
EmWeb ConnectionType EmWeb socket accept() failed: Socket accept failure for the specified connection
errno type.
EmWeb ewsNetHTTPReceive failure in Socket receive failure.
NetReceiveLoop() - closing connection.
EmWeb EmWeb: connection allocation failed Memory allocation failure for the new connection.
EmWeb EMWEB TransmitPending: EWOULDBLOCK Socket error on send.
error sending data
EmWeb ewaNetHTTPEnd: internal error - handle not in EmWeb handle index not valid.
Handle table
EmWeb ewsNetHTTPReceive:recvBufCnt exceeds The receive buffer limit has been reached. Bad
MAX_QUEUED_RECV_BUFS! request or DoS attack.
EmWeb EmWeb accept: XXXX Accept function for new SSH connection failed.
XXXX indicates the error info.
Table 31. CLI_UTIL Log Messages
Component Message Cause
CLI_UTIL Telnet Send Failed errno = 0x%x Failed to send text string to the telnet client.
CLI_UTIL osapiFsDir failed Failed to obtain the directory information from a
volume's directory.
Table 32. WEB Log Messages
Component Message Cause
WEB Max clients exceeded This message is shown when the maximum
allowed java client connections to the switch is
exceeded.
WEB Error on send to sockfd XXXX, closing Failed to send data to the java clients through the
connection socket.
Switch Software Log Messages 1113
