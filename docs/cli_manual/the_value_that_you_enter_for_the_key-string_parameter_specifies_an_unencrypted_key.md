# the_value_that_you_enter_for_the_key-string_parameter_specifies_an_unencrypted_key

Pages: 145-145

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no ignore session-key
Use this command to configure the switch not to ignore the session key. That is, this
command resets the ignore session key property on the switch.
Format no ignore session-key
Mode Dynamic Authorization
port
Use this command to specify the UDP port on which the switch can detect RADIUS requests
from the configured dynamic authorization clients. The supported range for the port number
is 1025–65535.
Default 3799
Format port port-number
Mode Dynamic Authorization
no port
Use this command to reset the configured UDP port on which the switch can detect RADIUS
requests from dynamic authorization clients to port number 3799, which is the default port.
Default 3799
Format no port
Mode Dynamic Authorization
server-key
Use this command to configure a global shared secret that is used for all dynamic
authorization clients on which no individual shared secret key is configured.
Format server-key [0 | 7] key-string
Mode Dynamic Authorization
Parameter Description
0 The value that you enter for the key-string parameter specifies an unencrypted key.
7 The value that you enter for the key-string parameter specifies an encrypted key.
key-string The shared secret string. For unencrypted key, the maximum length is 128 characters.
Management Commands 145
