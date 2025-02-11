# sftp_and_scp_are_available_as_additional_transfer_methods_if_the_software_package_supports

Pages: 250-251

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
configuration
This command gracefully reloads the configuration. If you do not specify a script name, the
switch reloads the existing startup-config file. If you specify a script name, you must include
the extension.
Format configuration [scriptname]
Mode Privileged EXEC
copy
The copy command uploads and downloads files to and from the switch. You can also use
the copy command to manage the dual images (image 1 and image 2) on the file system.
Upload and download files from a server using FTP, TFTP, Xmodem, Ymodem, or Zmodem.
SFTP and SCP are available as additional transfer methods if the software package supports
secure management. If FTP is used, a password is required.
Format copy source destination {verify | noverify}
Mode Privileged EXEC
Replace the source and destination parameters with the options in the table on page
251 or the url source and destination arguments that are listed in the table on page 251,
use one of the following values:
• xmodem
• ymodem
• zmodem
• tftp://{ipaddress | hostname}/filepath/filename
• ftp://{user@ipaddr | hostname}/path/filename
• scp://{user@ipaddr | hostname}/path/filename
• sftp://{user@ipaddr | hostname}/path/filename
• usb://filepath/filename
The verify and noverify keywords are available only if the image/configuration verify
options feature is enabled (see file verify on page254); verify specifies that digital
signature verification will be performed for the specified downloaded image or configuration
file. noverify specifies that no verification will be performed.
The keyword ias-users supports the downloading of the IAS user database file. When the
IAS users file is downloaded, the switch IAS user’s database is replaced with the users and
its attributes available in the downloaded file. In the command copy url ias-users, for
url one of the following is used for IAS users file:
{{tftp://<ipaddr> | <ipv6address> | <hostname>/<filepath>/<filename>} |
{sftp | scp://<username>@<ipaddress>/<filepath>/<filename>}}
Utility Commands 250

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: The maximum length for the file path is 160 characters, and the
maximum length for the file name is 31 characters.
For FTP, TFTP, SFTP and SCP, the ipaddr or hostname parameter is the IP address or
host name of the server, filepath is the path to the file, and filename is the name of the
file you want to upload or download. For SFTP and SCP, the username parameter is the
user name for logging into the remote server via SSH.
Note: ip6address is also a valid parameter for routing packages that
support IPv6.
To copy OpenFlow SSL certificates to the switch using TFTP or XMODEM, using only the
following options pertinent to the OpenFlow SSL certificates.
Format copy [mode/file] nvram:{openflow-ssl-ca-cert | openflow-ssl-cert |
openflow-ssl-priv-key}
Mode Privileged Exec
CAUTION:
Before you load a new release image to make a backup, upload the
existing startup-config.cfg file to the server.
Source Destination Description
nvram:backup-config nvram:startup-config Copies the backup configuration to the startup
configuration.
nvram:clibanner url Copies the CLI banner to a server.
nvram:cpupktcapture.pcap url Uploads CPU packets capture file.
nvram:crash-log url Copies the crash log to a server.
nvram:errorlog url Copies the error log file to a server.
nvram:factory-defaults url Uploads factory defaults file.
nvram:log url Copies the log file to a server.
nvram:script scriptname url Copies a specified configuration script file to a
server.
nvram:startup-config nvram:backup-config Copies the startup configuration to the backup
configuration.
nvram:startup-config url Copies the startup configuration to a server.
Utility Commands 251
