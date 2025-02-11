# ssh_dfltcmdauthlist_exec_authorization_list_method_-_----------------------_--------------_6a017333

Pages: 102-127

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #show authorization methods
Command Authorization List Method
- ------------------------- --------------------------------------
d fltCmdAuthList tacacs none
l ist2 none undefined
l ist4 tacacs undefined
L ine Command Method List
------------ ------------------------------
C onsole dfltCmdAuthList
Telnet dfltCmdAuthList
SSH dfltCmdAuthList
Exec Authorization List Method
- ---------------------- --------------------------------------
d fltExecAuthList tacacs none
l ist2 none undefined
l ist4 tacacs undefined
L ine Exec Method List
------------ ------------------------------
Console dfltExecAuthList
Telnet dfltExecAuthList
S SH dfltExecAuthList
enable authentication
Use this command to specify the authentication method list when accessing a higher
privilege level from a remote telnet or console.
Format enable authentication {default | list-name}
Mode Line Config
Parameter Description
default Uses the default list created with the aaa authentication enable command.
list-name Uses the indicated list created with the aaa authentication enable command.
Command example:
The following example specifies the default authentication method to access a higher
privilege level console:
(NETGEAR Switch)(config)# line console
Management Commands 102

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
(NETGEAR Switch)(config-line)# enable authentication default
no enable authentication
Use this command to return to the default specified by the enable authentication command.
Format no enable authentication
Mode Line Config
username (Global Config, with an encrypted password entered)
Use the username command in Global Config mode to add a new user with an encrypted
password to the local user database.
For a new user, the default (privilege) level is 1.
Using the encrypted keyword allows you to transfer local user passwords between devices
without knowing the passwords.
If you use the password parameter with the encrypted parameter, the password must be
exactly 128 hexadecimal characters in length. If the password strength feature is enabled,
this command checks for password strength and returns an appropriate error if it fails to meet
the password strength criteria.
The optional parameter override-complexity-check disables the validation of the
password strength.
Note: In software version 12.0.11.8 and later software versions, when you
configure a user password, the password does not display in clear text
but encrypted.
Format username name {password password [encryption-type encryption-type]
[encrypted [override-complexity-check] | level level [encrypted [override-
complexity-check]] | override-complexity-check]} | {level level [override-
complexity-check] password [encryption-type encryption-type]}
Mode Global Config
Parameter Description
name The name of the user. The range is from 1 to 32 characters.
password T he authentication password for the user ranges from 8 to 64characters. The
password must be entered in encrypted format (it cannot be plain text).
The special characters allowed in the password include the following:
! # $ % & ' ( ) * + , - . / : ; < = > @ [ \ ] ^ _ ` { | } ~.
The password length can be zero if the no passwords min-length command is
executed.
encryption-type The encryption algorithm type, which can be SHA-512 (the default) or SHA-256.
Management Commands 103

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Parameter Description
encrypted Specifies that the password that is entered or copied from another switch configuration
is already encrypted, and is shown in the configuration as it is without any further
encryption.
override-complexity-check Disables the validation of the password strength.
level The user level. Level 0 can be assigned by a level 15 user to another user to suspend
that user’s access. Range 0-15. Enter access level 1 for Read Access or 15 for Read/
Write Access. In a situation in which the level is optional and you do not specify it, the
level is set to 1.
Command example:
The following example configures a password for the user “bob” with encryption type
SHA-512, (privilege) level 1, and the encrypted keyword set:
(NETGEAR Switch)(Config)#username "bob" password
$6$p6eTphdakQA88tjm$Hwg72k7wbEc0d6z7DioCNa9ezCqEOI1BiheodqFOktx.WRJeasjDm3D5M.x4Z4DIvBE
drWFBc/l2i6hiWYz.30 encryption-type sha512 level 1 encrypted
Command example:
The following example configures a password for the user “tom” with encryption type
SHA-512, (privilege) level 1, and both the encrypted keyword and
override-complexity-check keyword set:
(NETGEAR Switch)(Config)#username "tom" password
$6$p6eTphdakQA88tjm$Hwg72k7wbEc0d6z7DioCNa9ezCqEOI1BiheodqFOktx.WRJeasjDm3D5M.x4Z4DIvBE
drWFBc/l2i6hiWYz.30 encryption-type sha512 level 1 encrypted override-complexity-check
username (Global Config, with a plain text password entered)
Use the username command in Global Config mode to add a new user to the local user
database, allowing the user to enter a password in plain text. The password is displayed as a
series of asterisks (*).
For a new user, the default (privilege) level is 1.
The optional parameter override-complexity-check disables the validation of the
password strength.
Note: In software version 12.0.11.8 and later software versions, when you
configure a user password, the password does not display in clear text
but encrypted.
Management Commands 104

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format username name {[[encryption-type encryption-type] password | override-
complexity-check password | level level [password | override-complexity-check
password]] | override-complexity-check password}
Mode Global Config
Parameter Description
name The name of the user. The range is from 1 to 32 characters.
encryption-type The encryption algorithm type, which can be SHA-512 (the default) or SHA-256.
password Indicates that the user must enter a plain text password.
T his password must range from 8 to 64characters. Even though the password is
entered in plain text, the password is shown as a series of asterisks (*).
The special characters allowed in the password include the following:
! # $ % & ' ( ) * + , - . / : ; < = > @ [ \ ] ^ _ ` { | } ~.
The password length can be zero if the no passwords min-length command is
executed.
override-complexity-check Disables the validation of the password strength.
level The user level. Level 0 can be assigned by a level 15 user to another user to suspend
that user’s access. Range 0-15. Enter access level 1 for Read Access or 15 for Read/
Write Access. In a situation in which the level is optional and you do not specify it, the
level is set to 1.
Command example:
The following example configures a password for the user “bob” with (privilege) level 15:
(NETGEAR Switch)(Config)#username bob level 15 password
Enter new password:*********
Confirm new password:*********
Command example:
The following example configures a password for the user “test123” with (privilege) level 15,
and the encryption set to SHA-512:
(NETGEAR Switch)(Config)#username test123 level 15 password encryption-type sha512
Enter new password:********
Confirm new password:********
Command example:
The following example configures a password for the user “test1234” with the
override-complexity-check password keyword set:
(NETGEAR Switch)(Config)#username test1234 override-complexity-check password
Management Commands 105

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Enter new password:********
Confirm new password:********
no username
Use this command to remove a user name.
Format no username name
Mode Global Config
username name nopassword
Use this command to remove an existing user’s password (NULL password).
Format username name nopassword [level level]
Mode Global Config
Parameter Description
name The name of the user. Range: 1-32 characters.
password The authentication password for the user. Range 8-64 characters.
level The user level. Level 0 can be assigned by a level 15 user to another user to suspend that user’s
access. Range 0-15.
username name unlock
Use this command to allows a locked user account to be unlocked. Only a user with
read/write access can reactivate a locked user account.
Format username name unlock
Mode Global Config
username snmpv3 accessmode
This command specifies the snmpv3 access privileges for the specified login user. The valid
access mode values are readonly and readwrite. The username is the login user name
for which the specified access mode applies. The default is readwrite for the admin user
and readonly for all other users. You must enter the username in the same case you used
when you added the user. To see the case of the user name, enter the show users
command.
Management Commands 106

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Defaults • admin - readwrite
• other - readonly
Format username snmpv3 accessmode username {readonly | readwrite}
Mode Global Config
no username snmpv3 accessmode
This command sets the snmpv3 access privileges for the specified user as readwrite for
the admin user and readonly for all other users. The username value is the user name for
which the specified access mode will apply.
Format no username snmpv3 accessmode username
Mode Global Config
username snmpv3 authentication
This command specifies the authentication protocol to be used for the specified user. The
valid authentication protocols are none, md5 or sha. If you specify md5 or sha, the login
password is also used as the SNMPv3 authentication password and therefore must be at
least eight characters in length. The username is the user name associated with the
authentication protocol. You must enter the username in the same case you used when you
added the user. To see the case of the user name, enter the show users command.
Default no authentication
Format username snmpv3 authentication username {none | md5 | sha}
Mode Global Config
no username snmpv3 authentication
This command sets the authentication protocol to be used for the specified user to none. The
username is the user name for which the specified authentication protocol is used.
Format no username snmpv3 authentication username
Mode Global Config
username snmpv3 encryption
This command specifies the encryption protocol used for the specified user. The valid
encryption protocols are des or none.
If you select des, you can specify the required key on the command line. The encryption key
must be 8 to 64 characters long. If you select the des protocol but do not provide a key, the
user is prompted for the key. When you use the des protocol, the login password is also used
Management Commands 107

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
as the snmpv3 encryption password, so it must be a minimum of eight characters. If you
select none, you do not need to provide a key.
The username value is the login user name associated with the specified encryption. You
must enter the username in the same case you used when you added the user. To see the
case of the user name, enter the show users command.
Default no encryption
Format username snmpv3 encryption username {none | des [key]}
Mode Global Config
no username snmpv3 encryption
This command sets the encryption protocol to none. The username is the login user name
for which the specified encryption protocol will be used.
Format no username snmpv3 encryption username
Mode Global Config
username snmpv3 encryption encrypted
This command specifies the des encryption protocol and the required encryption key for the
specified user. The encryption key must be 8 to 64 characters long.
Default no encryption
Format username snmpv3 encryption encrypted username des key
Mode Global Config
show users
This command displays the configured user names and their settings. The show users
command displays truncated user names. Use the show users long command to display
the complete usernames. The show users command is only available for users with
read/write privileges. The SNMPv3 fields are displayed only if SNMP is available on the
system.
Format show users
Mode Privileged EXEC
Term Definition
User Name The name the user enters to login using the serial port, Telnet or Web.
Access Mode Shows whether the user is able to change parameters on the switch (Read/Write) or is only
able to view them (Read Only). As a factory default, the “admin” user has Read/Write
access and the “guest” has Read Only access.
Management Commands 108

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
SNMPv3 Access Mode The SNMPv3 Access Mode. If the value is set to ReadWrite, the SNMPv3 user is able to
set and retrieve parameters on the system. If the value is set to ReadOnly, the SNMPv3
user is only able to retrieve parameter information. The SNMPv3 access mode may be
different than the CLI and Web access mode.
SNMPv3 Authentication The authentication protocol to be used for the specified login user.
SNMPv3 Encryption The encryption protocol to be used for the specified login user.
show users long
This command displays the complete user names of the configured users on the switch.
Format show users long
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show users long
User Name
------------
admin
guest
test1111test1111test1111test1111
show users accounts
This command displays the local user status with respect to user account lockout and
password aging.This command displays truncated user names. Use the show users long
command to display the complete user names.
Format show users accounts [detail]
Mode Privileged EXEC
Term Definition
User Name The local user account’s user name.
Access Level The user’s access level (1 for read-only or 15 for read/write).
Password Aging Number of days, since the password was configured, until the password expires.
Password Expiry The current password expiration date in date format.
Date
Lockout Indicates whether the user account is locked out (true or false).
Management Commands 109

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If the detail keyword is included, the following additional fields display.
Term Definition
Password Override Displays the user's Password override complexity check status. By default it is disabled.
Complexity Check
Password Strength Displays the user password's strength (Strong or Weak). This field is displayed only if the
Password Strength feature is enabled.
Command example:
The following example displays information about the local user database.
(NETGEAR Switch)#show users accounts
UserName Privilege Password Password Lockout
Aging Expiry date
------------------- --------- -------- ------------ -------
admin 15 --- --- False
guest 1 --- --- False
console#show users accounts detail
UserName....................................... admin
Privilege...................................... 15
Password Aging................................. ---
Password Expiry................................ ---
Lockout........................................ False
Override Complexity Check...................... Disable
Password Strength.............................. ---
UserName....................................... guest
Privilege...................................... 1
Password Aging................................. ---
Password Expiry................................ ---
Lockout........................................ False
Override Complexity Check...................... Disable
Password Strength.............................. ---
show users login-history [long]
Use this command to display information about the login history of users.
Format show users login-history [long]
Mode Privileged EXEC
Management Commands 110

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show users login-history [username]
Use this command to display information about the login history of users.
Format show users login-history [username name]
Mode Privileged EXEC
Parameter Description
name Name of the user. Range: 1-20 characters.
Command example:
The following example shows user login history outputs:
Console>show users login-history
L ogin Time U sername P rotocol Location
- ------------------- - -------- - -------- ---------------
J an 19 2005 08:23:48 B ob Serial
J an 19 2005 08:29:29 R obert H TTP 172.16.0.8
J an 19 2005 08:42:31 J ohn S SH 172.16.0.1
J an 19 2005 08:49:52 B etty T elnet 172.16.1.7
login authentication
Use this command to specify the login authentication method list for a line (console, telnet, or
SSH). The default configuration uses the default set with the command aaa
authentication login.
Format login authentication {default | list-name}
Mode Line Configuration
Parameter Description
default Uses the default list created with the aaa authentication login command.
list-name Uses the indicated list created with the aaa authentication login command.
Command example:
The following example specifies the default authentication method for a console:
(NETGEAR Switch) (config)# line console
(NETGEAR Switch) (config-line)# login authentication default
Management Commands 111

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no login authentication
Use this command to return to the default specified by the authentication login
command.
Format no login authentication {default | list-name}
Mode Line Configuration
password (Line Configuration)
Use the password command in Line Configuration mode to specify a password on a line, or
allow it to be copied from a script file or configuration file. The default configuration is that no
password is specified.
Script files or configuration files with password commands that include plain text passwords
do not work.
Format password [encryption-type encryption-type] | password [encryption-type
encryption-type] [encrypted]]
Mode Line Config
Parameter Definition
password The password in encrypted format.
encrypted The password that is entered or copied from another switch configuration is already encrypted. For
SHA-256 salted hash, the password must be 63 characters in length. For SHA-512 salted hash (the
default), the password must be 106 characters in length.
encryption-type The encryption algorithm type, which can be SHA-512 (the default) or SHA-256.
Command example:
The following example configures a plain text password with the SHA-256 encryption type on
a line:
(NETGEAR Switch)(Config-line)#password encryption-type sha256
Enter new password:********
Confirm new password:********
Command example:
The following example configures a plain text password with the SHA-512 encryption type on
a line:
(NETGEAR Switch)(Config-line)#password encryption-type sha512
Enter new password:********
Confirm new password:********
Management Commands 112

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
The following example configures an encrypted password with the SHA-256 encryption type
on a line:
(NETGEAR Switch)(Config-line)#password
$5$8XLN8qHQLKvx61X8$vsIiv0ZqnesHqX/F5yeche4laH4B9WChxyRh5b3vGPB encryption-type sha256
encrypted
Command example:
The following example configures an encrypted password with the SHA-512 encryption type
on a line:
(NETGEAR Switch)(Config-line)#password
$6$iiOcwxwa96ZKoa1F$P6NjilVODkH5suf8ic90gj2FJ34EgiK1skJGt3nLevA6C6HJSBxNVOgtz.4DktM/SmE
NiIGFzqkdvhBgX8EGF/ encryption-type sha512 encrypted
no password (Line Configuration)
Use this command to remove the password on a line.
Format no password
Mode Line Config
password (User EXEC)
This command allow a user to change the password. The user must enter this command
after the password has aged. The user is prompted to enter the old password and the new
password.
Format password
Mode User EXEC
Command example:
The following example shows the prompt sequence for executing the password command:
(NETGEAR Switch)>password
Enter old password:********
Enter new password:********
Confirm new password:********
enable password (Privileged EXEC)
Use the enable password configuration command to set a local password to control
access to the privileged EXEC mode.
Script files or configuration files with password commands that include plain text passwords
do not work.
Management Commands 113

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: In software version 12.0.11.8 and later software versions, when you
configure a user password, the password does not display in clear text.
Format enable password [encryption-type encryption-type] | [password [encryp-
tion-type encryption-type] [encrypted]]
Mode Privileged EXEC
Parameter Description
encryption-type The encryption algorithm type, which can be SHA-512 (the default) or SHA-256.
password The password in encrypted format.
encrypted The password that is entered or copied from another switch configuration is already encrypted.
For SHA-256 salted hash, the password must be 63 characters in length. For SHA-512 salted
hash (the default), the password must be 106 characters in length.
Command example:
The following example configures a plain text password with the SHA-256 encryption type:
(NETGEAR Switch)#enable password encryption-type sha256
Enter old password:********
Enter new password:********
Confirm new password:********
Command example:
The following example configures a plain text password with the SHA-512 encryption type:
(NETGEAR Switch)#enable password encryption-type sha512
Enter old password:********
Enter new password:********
Confirm new password:********
Command example:
The following example configures an encrypted password with the SHA-256 encryption:
(NETGEAR Switch)#enable password
$5$8XLN8qHQLKvx61X8$vsIiv0ZqnesHqX/F5yeche4laH4B9WChxyRh5b3vGPB encryption-type sha256
encrypted
Command example:
The following example configures an encrypted password with the SHA-512 encryption type:
(NETGEAR Switch)#enable password
$6$Zhe76BxSM7ZOh8/.$.acXOoNVZMbXJuG/L7Ilcfd5iLHL7dd8Gt79bpQacL6UBSdD4GvEudGgP/eaT/wW.Xu
wT3j0o9qKFgLhGZoXz/ encryption-type sha512 encrypted
Management Commands 114

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no enable password (Privileged EXEC)
Use the no enable password command to remove the password requirement.
Format no enable password
Mode Privileged EXEC
passwords min-length
Use this command to enforce a minimum password length for local users. The value also
applies to the enable password. The length argument is a number in the range 8–64.
Default 8
Format passwords min-length length
Mode Global Config
no passwords min-length
Use this command to set the minimum password length to the default value.
Format no passwords min-length
Mode Global Config
passwords history
Use this command to set the number of previous passwords that can be stored for each user
account. When a local user changes his or her password, the user is not be able to reuse any
password stored in password history. This ensures that users do not reuse their passwords
often. The number argument is a number in the range 0–10.
Default 0
Format passwords history number
Mode Global Config
no passwords history
Use this command to set the password history to the default value.
Format no passwords history
Mode Global Config
Management Commands 115

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
passwords aging
Use this command to implement aging on passwords for local users. When a user’s
password expires, the user is prompted to change it before logging in again. The days
argument is a number in the range 1–365 days. The default is 0, or no aging.
Default 0
Format passwords aging days
Mode Global Config
no passwords aging
Use this command to set the password aging to the default value.
Format no passwords aging
Mode Global Config
passwords lock-out
Use this command to strengthen the security of the switch by locking user accounts that have
failed login due to wrong passwords. When a lockout count is configured, a user that is
logged in must enter the correct password within that count. Otherwise the user will be locked
out from further switch access. Only a user with read/write access can reactivate a locked
user account. Password lockout does not apply to logins from the serial console. The
number argument is a number in the range 1–5. The default is 0, or no lockout count
enforced.
Default 0
Format passwords lock-out number
Mode Global Config
no passwords lock-out
Use this command to set the password lock-out count to the default value.
Format no passwords lock-out
Mode Global Config
Management Commands 116

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
passwords strength-check
Use this command to enable the password strength feature. It is used to verify the strength of
a password during configuration.
Default Disable
Format passwords strength-check
Mode Global Config
no passwords strength-check
Use this command to set the password strength checking to the default value.
Format no passwords strength-check
Mode Global Config
passwords strength maximum consecutive-characters
Use this command to set the maximum number of consecutive characters to be used in
password strength. The number argument is a number in the range 0–15. The default is 0.
Minimum of 0 means no restriction on that set of characters.
Default 0
Format passwords strength maximum consecutive-characters number
Mode Global Config
passwords strength maximum repeated-characters
Use this command to set the maximum number of repeated characters to be used in
password strength. The number argument is a number in the range 0–15. The default is 0.
Minimum of 0 means no restriction on that set of characters.
Default 0
Format passwords strength maximum repeated-characters number
Mode Global Config
passwords strength minimum uppercase-letters
Use this command to enforce a minimum number of uppercase letters that a password
should contain. The number argument is a number in the range 0–16. The default is 2.
Minimum of 0 means no restriction on that set of characters.
Management Commands 117

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default 2
Format passwords strength minimum uppercase-letters number
Mode Global Config
no passwords strength minimum uppercase-letters
Use this command to reset the minimum uppercase letters required in a password to the
default value.
Format no passwords minimum uppercase-letter
Mode Global Config
passwords strength minimum lowercase-letters
Use this command to enforce a minimum number of lowercase letters that a password should
contain. The number argument is a number in the range 0–16. The default is 2. Minimum of
0 means no restriction on that set of characters.
Default 2
Format passwords strength minimum lowercase-letters number
Mode Global Config
no passwords strength minimum lowercase-letters
Use this command to reset the minimum lower letters required in a password to the default
value.
Format no passwords minimum lowercase-letter
Mode Global Config
passwords strength minimum numeric-characters
Use this command to enforce a minimum number of numeric characters that a password
should contain. The number argument is a number in the range 0–16. T The default is 2.
Minimum of 0 means no restriction on that set of characters.
Default 2
Format passwords strength minimum numeric-characters number
Mode Global Config
Management Commands 118

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no passwords strength minimum numeric-characters
Use this command to reset the minimum numeric characters required in a password to the
default value.
Format no passwords minimum numeric-characters
Mode Global Config
passwords strength minimum special-characters
Use this command to enforce a minimum number of special characters that a password
should contain. The number argument is a number in the range 0–16. The default is 2.
Minimum of 0 means no restriction on that set of characters.
Default 2
Format passwords strength minimum special-characters number
Mode Global Config
no passwords strength minimum special-characters
Use this command to reset the minimum special characters required in a password to the
default value.
Format no passwords minimum special-characters
Mode Global Config
passwords strength minimum character-classes
Use this command to enforce a minimum number of characters classes that a password
should contain. Character classes are uppercase letters, lowercase letters, numeric
characters and special characters. The number argument is a number in the range 0–4. The
default is 4.
Default 4
Format passwords strength minimum character-classes number
Mode Global Config
Management Commands 119

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no passwords strength minimum character-classes
Use this command to reset the minimum number of character classes required in a password
to the default value.
Format no passwords minimum character-classes
Mode Global Config
passwords strength exclude-keyword
Use this command to exclude the specified keyword while configuring the password. The
password does not accept the keyword in any form (in between the string, case in-sensitive
and reverse) as a substring. You can configure up to a maximum of three keywords.
Format passwords strength exclude-keyword keyword
Mode Global Config
no passwords strength exclude-keyword
Use this command to reset the restriction for the specified keyword or all the keywords
configured.
Format no passwords exclude-keyword [keyword]
Mode Global Config
passwords unlock timer
Use this command to configure the time after which a locked user account is unlocked (that
is, the unlock time) and password authentication can be attempted again. By default, the
period for the minutes argument is 5 minutes and the range is from 1 to 60 minutes.
Default 5
Format passwords unlock timer minutes
Mode Global Config
no passwords unlock timer
Use this command to reset the unlock time to the default time.
Format no passwords unlock timer
Mode Global Config
Management Commands 120

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
passwords unlock timer mode
Use this command to configure the password unlock timer mode. If the user account is
locked, the timer mode is enabled (which it is by default), and the unlock time expires, the
user account is unlocked. If the timer mode is disabled and the unlock time expires, the user
account remains locked.
Default Enabled
Format passwords unlock timer mode {enabled | disabled}
Mode Global Config
no passwords unlock timer mode
Use this command to reset the unlock timer mode to its default.
Format no passwords unlock timer mode
Mode Global Config
show passwords configuration
Use this command to display the configured password management settings.
Format show passwords configuration
Mode Privileged EXEC
Term Definition
Minimum Password Length The minimum number of characters that the password must include.
Password Aging (day) The length in days that a password is valid.
Password History The number of passwords to store for reuse prevention.
Lockout Attempts The number of failed password login attempts allowed before lockout occurs.
Password Strength Check Indicates if the password strength check is enabled.
Minimum Password The minimum number of uppercase characters that the password must include.
Uppercase Letters
Minimum Password The minimum number of lowercase characters that the password must include.
Lowercase Letters
Minimum Password Numeric The minimum number of numeric characters that the password must include.
Characters
Minimum Password Special The minimum number of special characters that the password must include.
Characters
Maximum Password The maximum number of repeated characters that the password can include.
Repeated Characters
Management Commands 121

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Maximum Password The maximum number of consecutive repeated characters that the password can include.
Consecutive Characters
Minimum Password The minimum number of character classes (uppercase, lowercase, numeric and special)
Character Classes that the password must include.
Password Exclude-Keywords The set of keywords to be excluded from the configured password when strength checking
is enabled.
Unlock Timer Mode Indicates if the unlock timer mode is enabled.
Unlock Time (mins) The time after which a locked user account is unlocked
show passwords result
Use this command to display the last password set result information.
Format show passwords result
Mode Privileged EXEC
Term Definition
Last User Whose Password Shows the name of the user with the most recently set password.
Is Set
Password Strength Check Shows whether password strength checking is enabled.
Last Password Set Result Shows whether the attempt to set a password was successful. If the attempt failed, the
reason for the failure is included.
aaa ias-user username
The Internal Authentication Server (IAS) database is a dedicated internal database used for
local authentication of users for network access through the IEEE 802.1X feature.
Use the aaa ias-user username command in Global Config mode to add the specified
user to the internal user database. This command also changes the mode to AAA User
Config mode.
Format aaa ias-user username user
Mode Global Config
no aaa ias-user username
Use this command to remove the specified user from the internal user database.
Format no aaa ias-user username user
Mode Global Config
Management Commands 122

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
(NETGEAR Switch) #
(NETGEAR Switch) #configure
(NETGEAR Switch) (Config)#aaa ias-user username client-1
((NETGEAR Switch)(Config-aaa-ias-User)#exit
(NETGEAR Switch) (Config)#no aaa ias-user username client-1
(NETGEAR Switch) (Config)#
aaa session-id
Use this command in Global Config mode to specify if the same session-id is used for
Authentication, Authorization and Accounting service type within a session.
Default common
Format aaa session-id [common | unique]
Mode Global Config
Parameter Description
common Use the same session-id for all AAA Service types.
unique Use a unique session-id for all AAA Service types.
no aaa session-id
Use this command in Global Config mode to reset the aaa session-id behavior to the default.
Format no aaa session-id [unique]
Mode Global Config
aaa accounting
Use this command in Global Config mode to create an accounting method list for user EXEC
sessions, user-executed commands, or DOT1X. This list is identified by the default
keyword or by a user-specified list-name. Accounting records, when enabled for a
line-mode, can be sent at both the beginning and at the end (start-stop) or only at the end
(stop-only). If none is specified, accounting is disabled for the specified list. If tacacs is
specified as the accounting method, accounting records are notified to a TACACS+ server. If
radius is the specified accounting method, accounting records are notified to a RADIUS
server.
Note the following:
• A maximum of five Accounting Method lists can be created for each exec and commands
type.
• Only the default Accounting Method list can be created for DOT1X. There is no provision
to create more.
Management Commands 123

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
• The same list-name can be used for both exec and commands accounting type
• AAA Accounting for commands with RADIUS as the accounting method is not supported.
• Start-stop or None are the only supported record types for DOT1X accounting. Start-stop
enables accounting and None disables accounting.
• RADIUS is the only accounting method type supported for DOT1X accounting.
Format aaa accounting {exec | commands | dot1x} {default | list-name} {start-stop |
stop-only |none} method1 [method2…]
Mode Global Config
Parameter Description
exec Provides accounting for a user EXEC terminal sessions.
commands Provides accounting for all user executed commands.
dot1x Provides accounting for DOT1X user commands.
default The default list of methods for accounting services.
list-name Character string used to name the list of accounting methods.
start-stop Sends a start accounting notice at the beginning of a process and a stop accounting notice at the
beginning of a process and a stop accounting notice at the end of a process.
stop-only Sends a stop accounting notice at the end of the requested user process.
none Disables accounting services on this line.
method Use either TACACS or radius server for accounting purposes.
Command example:
(NETGEAR Switch) #
(NETGEAR Switch) #configure
(NETGEAR Switch) #aaa accounting commands default stop-only tacacs
(NETGEAR Switch) #aaa accounting exec default start-stop radius
(NETGEAR Switch) #aaa accounting dot1x default start-stop radius
(NETGEAR Switch) #aaa accounting dot1x default none
(NETGEAR Switch) #exit
Command example:
For the same set of accounting type and list name, the administrator can change the record
type, or the methods list, without having to first delete the previous configuration:
(NETGEAR Switch) #
(NETGEAR Switch) #configure
(NETGEAR Switch) #aaa accounting exec ExecList stop-only tacacs
(NETGEAR Switch) #aaa accounting exec ExecList start-stop tacacs
(NETGEAR Switch) #aaa accounting exec ExecList start-stop tacacs radius
Management Commands 124

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The first aaa command creates a method list for exec sessions with the name ExecList,
with record-type as stop-only and the method as tacacs. The second command changes
the record type from stop-only to start-stop for the same method list. The third
command, for the same list changes the methods list from tacacs to tacacs,radius.
no aaa accounting
This command deletes the accounting method list.
Format no aaa accounting {exec | commands | dot1x} {default | list-name}
Mode Global Config
Command example:
(NETGEAR Switch) #
(NETGEAR Switch) #configure
(NETGEAR Switch) #aaa accounting commands userCmdAudit stop-only tacacs radius
(NETGEAR Switch) #no aaa accounting commands userCmdAudit
(NETGEAR Switch) #exit
password (AAA IAS User Config)
Use this command to specify a password for a user in the IAS database. An optional
parameter encrypted is provided to indicate that the password given to the command is
already preencrypted.
Format password password [encrypted]
Mode AAA IAS User Config
Parameter Definition
password Password for this level. Range: 8-64 characters
encrypted Encrypted password to be entered, copied from another switch configuration.
Command example:
(NETGEAR Switch) #
(NETGEAR Switch) #configure
(NETGEAR Switch) (Config)#aaa ias-user username client-1
(NETGEAR Switch) (Config-aaa-ias-User)#password client123
(NETGEAR Switch) (Config-aaa-ias-User)#no password
Command example:
The following is an example of adding a MAB Client to the Internal user database:
(NETGEAR Switch) #
(NETGEAR Switch) #configure
Management Commands 125

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
(NETGEAR Switch) (Config)#aaa ias-user username 1f3ccb1157
(NETGEAR Switch) (Config-aaa-ias-User)#password 1f3ccb1157
(NETGEAR Switch) (Config-aaa-ias-User)#exit
(NETGEAR Switch) (Config)#
no password (AAA IAS User Config)
Use this command to clear the password of a user.
Format no password
Mode AAA IAS User Config
clear aaa ias-users
Use this command to remove all users from the IAS database.
Format clear aaa ias-users
Mode Privileged Exec
Command example:
(NETGEAR Switch) #clear aaa ias-users
show aaa ias-users
Use this command to display configured IAS users and their attributes. Passwords
configured are not shown in the show command output.
Format show aaa ias-users [username]
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show aaa ias-users
UserName
-------------------
Client-1
Client-2
Following are the IAS configuration commands shown in the output of show
running-config command. Passwords shown in the command output are always
encrypted.
aaa ias-user username client-1
password a45c74fdf50a558a2b5cf05573cd633bac2c6c598d54497ad4c46104918f2c encrypted
exit
Management Commands 126

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
accounting
Use this command in Line Configuration mode to apply the accounting method list to a line
config (console/telnet/ssh).
Format accounting {exec | commands} {default | list-name}
Mode Line Configuration
Parameter Description
exec Causes accounting for an EXEC session.
commands This causes accounting for each command execution attempt. If a user is enabling accounting for
exec mode for the current line-configuration type, the user will be logged out.
default The default Accounting List
listname Enter a string of not more than 15 characters.
Command example:
(NETGEAR Switch) #
(NETGEAR Switch) #configure
(NETGEAR Switch) (Config)#line telnet
(NETGEAR Switch)(Config-line)# accounting exec default
(NETGEAR Switch) #exit
no accounting
Use this command to remove accounting from a Line Configuration mode.
Format no accounting {exec | commands]
Mode Line Configuration
show accounting
Use this command to display ordered methods for accounting lists.
Format show accounting
Mode Privileged EXEC
Command example:
(NETGEAR Switch) #show accounting
Number of Accounting Notifications sent at beginning of an EXEC session: 0
Errors when sending Accounting Notifications beginning of an EXEC session: 0
Number of Accounting Notifications at end of an EXEC session: 0
Errors when sending Accounting Notifications at end of an EXEC session: 0
Number of Accounting Notifications sent at beginning of a command execution: 0
Management Commands 127
