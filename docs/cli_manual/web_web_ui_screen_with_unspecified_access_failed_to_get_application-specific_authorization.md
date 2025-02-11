# web_web_ui_screen_with_unspecified_access_failed_to_get_application-specific_authorization

Pages: 1114-1114

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 32. WEB Log Messages
Component Message Cause
WEB # (XXXX) Form Submission Failed. No Action The form submission failed and no action is
Taken. taken. XXXX indicates the file under
consideration.
WEB ewaFormServe_file_download() - WEB Unknown Unknown error returned while downloading file
return code from tftp download result using TFTP from web interface.
WEB ewaFormServe_file_upload() - Unknown return Unknown error returned while uploading file
code from tftp upload result using TFTP from web interface.
WEB Web UI Screen with unspecified access Failed to get application-specific authorization
attempted to be brought up handle provided to EmWeb/Server by the
application in ewsAuthRegister(). The specified
web page will be served in read-only mode.
Table 33. CLI_WEB_MGR Log Messages
Component Message Cause
CLI_WEB_MGR File size is greater than 2K The banner file size is greater than 2K bytes.
CLI_WEB_MGR No. of rows greater than allowed maximum of When the number of rows exceeds the maximum
XXXX allowed rows.
Table 34. SSHD Log Messages
Component Message Cause
SSHD SSHD: Unable to create the global (data) Failed to create semaphore for global data
semaphore protection.
SSHD SSHD: Msg Queue is full, event = XXXX Failed to send the message to the SSHD
message queue as message queue is full. XXXX
indicates the event to be sent.
SSHD S SHD: Unknown UI event in message, event= Failed to dispatch the UI event to the appropriate
XXXX SSHD function as it’s an invalid event. XXXX
indicates the event to be dispatched.
SSHD sshdApiCnfgrCommand: Failed calling Failed to send the message to the SSHD
sshdIssueCmd. message queue.
Table 35. SSLT Log Messages
Component Message Cause
SSLT SSLT: Exceeded maximum, ssltConnectionTask Exceeded maximum allowed SSLT connections.
SSLT SSLT: Error creating Secure server socket6 Failed to create secure server socket for IPV6.
Switch Software Log Messages 1114
