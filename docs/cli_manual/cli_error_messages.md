# cli_error_messages

Pages: 24-37

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
CLI Error Messages
If you enter a command and the system is unable to execute it, an error message appears.
The following table describes the most common CLI error messages.
T able 7. CLI Error Messages
Message Text Description
% Invalid input detected at Indicates that you entered an incorrect or unavailable command. The
'^' marker. carat (^) shows where the invalid text is detected. This message also
appears if any of the parameters or values are not recognized.
Command not found / Incomplete Indicates that you did not enter the required keywords or values.
command. Use ? to list
commands.
Ambiguous command Indicates that you did not enter enough letters to uniquely identify the
command.
CLI Line-Editing Conventions
The following table describes the key combinations you can use to edit commands or
increase the speed of command entry. You can access this list from the CLI by entering help
from the User or Privileged EXEC modes.
T able 8. CLI Editing Conventions
Key Sequence Description
DEL or Backspace Delete previous character.
Ctrl-A Go to beginning of line.
Ctrl-E Go to end of line.
Ctrl-F Go forward one character.
Ctrl-B Go backward one character.
Ctrl-D Delete current character.
Ctrl-U, X Delete to beginning of line.
Ctrl-K Delete to end of line.
Ctrl-W Delete previous word.
Ctrl-T Transpose previous character.
Ctrl-P Go to previous line in history buffer.
Software Modules 24

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Table 8. CLI Editing Conventions (continued)
Key Sequence Description
Ctrl-R Rewrites or pastes the line.
Ctrl-N Go to next line in history buffer.
Ctrl-Y Prints last deleted character.
Ctrl-Q Enables serial flow.
Ctrl-S Disables serial flow.
Ctrl-Z Return to root command prompt.
Tab, <SPACE> Command-line completion.
Exit Go to next lower command prompt.
? List available commands, keywords, or parameters.
Using CLI Help
Enter a question mark (?) at the command prompt to display the commands available in the
current mode.
(NETGEAR Switch) >?
enable Enter into user privilege mode.
help Display help for various special keys.
logout Exit this session. Any unsaved changes are lost.
password Change an existing user’s password.
ping Send ICMP echo packets to a specified IP address.
quit Exit this session. Any unsaved changes are lost.
show Display Switch Options and Settings.
telnet Telnet to a remote host.
Enter a question mark (?) after each word you enter to display available command keywords
or parameters.
(NETGEAR Switch) #network ?
ipv6 Configure IPv6 parameters for system network.
javamode Enable/Disable.
mac-address Configure MAC Address.
mac-type Select the locally administered or burnedin MAC
address.
mgmt_vlan Configure the Management VLAN ID of the switch.
parms Configure Network Parameters of the device.
protocol Select DHCP, BootP, or None as the network config
protocol.
Software Modules 25

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If the help output shows a parameter in angle brackets, you must replace the parameter with
a value.
(NETGEAR Switch) #network parms ?
<ipaddr> Enter the IP Address.
none Reset IP address and gateway on management interface
If there are no additional command keywords or parameters, or if additional parameters are
optional, the following message appears in the output:
<cr> Press Enter to execute the command
You can also enter a question mark (?) after typing one or more characters of a word to list
the available command or parameters that begin with the letters, as shown in the following
example:
(NETGEAR Switch) #show m?
mac mac-addr-table mac-address-table
m ail-server mbuf monitor
Access the CLI
You can access the CLI by using a direct console connection or by using a telnet or SSH
connection from a remote management host.
For the initial connection, you must use a direct connection to the console port. You cannot
access the system remotely until the system has an IP address, subnet mask, and default
gateway. You can set the network configuration information manually, or you can configure
the system to accept these settings from a BootP or DHCP server on your network. For more
information, see Management Interface Commands on page58.
Software Modules 26

Stacking Commands

This chapter describes the stacking commands.
This chapter contains the following sections:
• Dedicated Port Stacking Commands
• Stack Port Commands
• Stack Firmware Synchronization Commands
• Nonstop Forwarding Commands for Stack Configuration
The commands in this chapter are in two functional groups:
• Show commands. Display switch settings, statistics, and other information.
• Configuration commands. Configure features and options of the switch. For every
configuration command, there is a show command that displays the configuration setting.
Note: The Primary Management Unit is the unit that controls the stack.

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Dedicated Port Stacking Commands
This section describes the commands you use to configure dedicated port stacking.
stack
Use this command to set the mode to Stack Global Config.
Default None
Format stack
Mode Global Config
member (Stack Global Config)
Use this command to add a switch to a stack. The unit is the switch identifier of the switch to
be added to the stack. The switchindex is the index into the database of the supported
switch types, indicating the type of the switch being preconfigured. The switchindex is a
32-bit integer. You issue this command on the Primary Management Unit.
Default None
Format member unit switchindex
Mode Stack Global Config
Note: You can obtain the switch index by issuing the show supported
switchtype command in User EXEC mode.
no member
Use this command to remove a switch from a stack. The unit is the switch identifier of the
switch to be removed from the stack. You issue this command on the Primary Management
Unit.
Format no member unit
Mode Stack Global Config
switch priority
Use this command to configure the ability of a switch to become the Primary Management
Unit. The unit is the switch identifier. The value is the preference parameter that lets you
specify the priority of one backup switch over another. The range for priority is 1 to 15. The
switch with the highest priority value becomes the Primary Management Unit if the active
Primary Management Unit fails. The switch priority defaults to the hardware management
Stacking Commands 28

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
preference value 1. Switches without the hardware capability to become the Primary
Management Unit are not eligible for management.
Default Enabled
Format switch unit priority value
Mode Global Config
switch renumber
Use this command to change the switch identifier for a switch in the stack. The oldunit is
the current switch identifier on the switch whose identifier is to be changed. The newunit is
the updated value of the switch identifier. When you issue the command, the switch is
configured with the configuration information for the new switch, if any. The old switch
configuration information is retained, however the old switch becomes operationally
unplugged. You issue this command on the Primary Management Unit.
Note: If the management unit is renumbered, the running configuration is no
longer applied (that is, the stack functions as if the running
configuration is cleared).
Default None
Format switch oldunit renumber newunit
Mode Global Config
movemanagement (Stack Global Config)
Use this command to move the Primary Management Unit functionality from one switch to
another. The fromunit is the switch identifier on the current Primary Management Unit. The
tounit is the switch identifier on the new Primary Management Unit. When you issue the
command, the entire stack (including all interfaces in the stack) is unconfigured and
reconfigured with the configuration on the new Primary Management Unit. After the reload is
complete, you must perform all stack management capability on the new Primary
Management Unit. To preserve the current configuration across a stack move, issue the
copy system:running-config nvram:startup-config command in Privileged
EXEC mode before performing the stack move. A stack move causes all routes and layer 2
addresses to be lost. You issue this command on the Primary Management Unit. The system
prompts you to confirm the management move.
Note: The movemanagement command does not perform nonstop
forwarding (NSF). To move the management unit to the backup unit,
issue the initiate failover command instead. For more
information, see initiate failover (for stack configuration) on p age51.
Stacking Commands 29

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Default None
Format movemanagement fromunit tounit
Mode Stack Global Config
standby
Use this command to configure a unit as a Standby Management Unit (STBY). The unit
number is the unit number that must become the Standby Management Unit. The unit
number must be a valid unit number.
Default None
Format standby unit number
Mode Stack Global Config
Note: The Standby Management Unit cannot be the current Management
Unit. The Standby unit must be a management-capable unit.
no standby
Use this command to let the switch run the auto Standby Management Unit.
Format no standby
Mode Stack Global Config
slot (for stack configuration)
Use this command to configure a slot in the system. The unit/slot is the slot identifier of
the slot. The cardindex is the index into the database of the supported card types,
indicating the type of the card that is being preconfigured in the specified slot. The
cardindex is a 32-bit integer. If a card is present in the slot that is unconfigured, the
configured information is deleted and the slot is reconfigured with default information for the
card.
Default None
Format slot unit/slot cardindex
Mode Global Config
Stacking Commands 30

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: You can obtain the card index by issuing the show supported
cardtype command in User EXEC mode.
no slot
Use this command to remove configured information from an existing slot in the system.
Format no slot unit/slot cardindex
Mode Global Config
Note: You can obtain the card index by issuing the show supported
cardtype command in User EXEC mode.
set slot disable (for stack configuration)
Use this command to configure the administrative mode for a specified slot or for all slots. If
you specify all, the command is applied to all slots, otherwise the command is applied to
the slot that is identified by unit/slot.
If a card or other module is present in the slot, the administrative mode is applied to the
contents of the slot. If the slot is empty, the administrative mode is applied to any module that
is inserted into the slot. If a card is disabled, all the ports on the device are operationally
disabled and shown as “unplugged” on management screens.
Default None
Format set slot disable [unit/slot | all]
Mode Global Config
no set slot disable
Use this command to remove the administrative mode for a specified slot or for all slots. If
you specify all, the command removes the administrative mode from all slots, otherwise the
command removes the administrative mode from the slot that is identified by unit/slot.
If a card or other module is present in the slot, the administrative mode removes the
configuration from the contents of the slot. If the slot is empty, the administrative mode
removes the configuration from any module inserted into the slot. If a card is disabled, all the
ports on the device are operationally disabled and shown as “unplugged” on management
screens.
Format no set slot disable [unit/slot | all]
Mode Global Config
Stacking Commands 31

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
set slot power (for stack configuration)
Use this command to configure the power mode for a specified slot or for all slots and allows
power to be supplied to the cards that are located in the slots. If you specify all, the
command is applied to all slots, otherwise the command is applied to the slot that is identified
by unit/slot.
Use this command when you install or remove cards. If a card or other module is present in
the slot, the power mode is applied to the contents of the slot. If the slot is empty, the power
mode is applied to any card inserted into the slot.
Default None
Format set slot power [unit/slot | all]
Mode Global Config
no set slot power
Use this command to remove the power mode for a specified slot or for all slots and prohibits
power from being supplied to the cards that are located in the slots. If you specify all, the
command prohibits power to all slots, otherwise the command prohibits power to the slot that
is identified by unit/slot.
Use this command when you install or remove cards. If a card or other module is present in
the slot, power is prohibited to the contents of the slot. If the slot is empty, power is prohibited
to any card inserted into the slot.
Format no set slot power [unit/slot | all]
Mode Global Config
reload (for stack configuration)
Use this command to reset the entire stack or the identified unit. The unit is the switch
identifier. The system prompts you to confirm that you want to reset the switch.
Default None
Format reload [unit]
Mode User EXEC
stack-status sample-mode
Use this command to configure the global status management mode and, as an option, the
sample size. The mode and sample size parameters are applied globally to all units in the
stack. The default sampling mode of the operation is cumulative, which tacks the sum of the
received time stamp offsets cumulatively. You can also select the history sampling mode,
which tracks the history of the received timestamps.
Stacking Commands 32

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
The sample size indicates the maximum number of samples that must be kept. The range for
the number value for max-samples is from 100 to 500.
Note: The stack-status sample-mode command is implemented as
part of a serviceability functionality and therefore not expected to be
persistent across reloads. The configuration is not visible in the
running configuration under any circumstances. When you issue the
command, the configuration is applied to all the members that are part
of the stack. After you issue the command, the configuration is not
applied to new members that you add to the stack.
Default The default for sampling mode is cumulative.
The default for max-samples is 300.
Format stack-status sample-mode {cumulative | history} [max-samples
number]
Mode Stack Global Config
The following command sets the sampling mode to cumulative:
(NETGEAR Switch) #configure
(NETGEAR Switch) (Config)#stack
(NETGEAR Switch) (Config-stack)# stack-status sample-mode cumulative
Command example:
The following command sets the sampling mode to history and the sample size to the default.
(NETGEAR Switch) #configure
(NETGEAR Switch) (Config)#stack
(NETGEAR Switch) (Config-stack)#stack-status sample-mode history
Command example:
The following command sets the sampling mode to history and sample size to 100.
(NETGEAR Switch) #configure
(NETGEAR Switch) (Config)#stack
(NETGEAR Switch) (Config-stack)#stack-status sample-mode history max-samples 100
Stacking Commands 33

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show slot
Use this command to display information about all the slots in the system or about a specific
slot.
Format show slot [unit/slot]
Mode User EXEC
Privileged EXEC
Term Definition
Slot The slot identifier in the unit/slot format.
Slot Status The slot is empty, full, or has encountered an error.
Admin State The slot administrative mode is enabled or disabled.
Power State The slot power mode is enabled or disabled.
Card Information Shows the card type pre-configured vs actual card installed in the chassis.
Configured/Actual
Vendor Name Card vendor name.
Seral Number Serial number of the card if present.
Power Down Indicates whether the slot can be powered down.
PoE Capable Indicates whether the card is PoE capable or not.
Command example:
This example shows the output of the show slot command:
(M4300-96X) #show slot
Admin Power Card Information Vendor Serial Power
Slot Status State State Configured/Actual Name Number Down PoE Capable
----- -------- ------- ------- -------------------- ------------- --------------- ----- -----------
1/1 Full Enable Enable APM408C/APM408C 57Y1847N8009E Yes Yes
1/2 Full Enable Enable APM408C/APM408C 57Y17C7D80015 Yes Yes
1/3 Full Enable Enable APM408F/APM408F 78 58117C7Y800B4 Yes Yes
1/4 Full Enable Enable APM408P/APM408P 58017C7H800B0 Yes Yes
1/5 Full Enable Enable TPM404H/TPM404H ZeeVee HZ80K800001A Yes Yes
1/6 Empty Enable Enable Yes Yes
1/7 Full Enable Enable APM408F/APM408F 58117C7E80041 Yes No
1/8 Full Enable Enable APM408P/APM408P 58017C7S800C6 Yes No
1/9 Full Enable Enable APM408C/APM408C 57Y17C79800E7 Yes No
1/10 Empty Enable Enable Yes No
1/11 Empty Enable Enable APM402XL/ Yes No
1/12 Full Enable Enable APM402XL/APM402XL 5EU1857L80139 Yes No
Stacking Commands 34

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Note: In the previous example for model M4300-96X, a third-party HDMI
port card is shown in slot 1/5. You can insert a third-party HDMI port
card in any of the upper slots (1–6), but not in the lower slots.
If you preconfigure a slot for a particular type of port card, install only that type of port card in
the slot. In the previous example for model M4300-96X, if you insert a port card other than
the APM408P in slot 1/8, the slot is not activated, the interfaces on the port card do no
become operational, and the switch generates a log message about a mismatch in the
configured port card and the inserted port card in the memory log. Therefore, if you
preconfigure a slot for a particular type of port card, insert only that type of port card in the
slot.
You can change the configuration for a slot from a set type of port card to a dynamic port card
by entering the no slot unit/slot command. For example, to remove the configuration
of slot 2 so that the slot can enter any of the supported port cards dynamically, enter the no
slot 1/2 command.
Note: The output of the show slot command shows only the port cards in
the slots that are populated or are configured for a particular type of
port card.
If you supply a value for unit/slot, the following additional information displays:
Term Definition
Inserted Card The model identifier of the card inserted in the slot. The model identifier is a
Model Identifier 32-character field used to identify a card. This field is displayed only if the slot is
populated.
Inserted Card The card description. This field is displayed only if the slot is populated.
Description
Configured Card The card description of the card preconfigured in the slot.
Description
show stack-status
Use this command to display the stack unit’s received heartbeat message timings and the
dropped or lost statistics for the specified unit.
Use the following optional keywords to specify the command output:
• number. The output displays for a specific unit in the stack. The value for number can be
from 1 to 8.
• all. The output displays for all units in the stack.
Use the optional keyword clear to remove the statistics of the stack heartbeat message.
Stacking Commands 35

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Format show stack stack-status [number | all] [clear]
Mode Privileged EXEC
Term Definition
Current The time at which the heartbeat message was received.
Average The average time of the heartbeat messages that were received.
Min The minimum time of the heartbeat messages that were received.
Max The maximum time of the heartbeat messages that were received.
Dropped The number of heartbeat messages that were dropped or lost.
Command example:
This example dumps the stack unit heartbeat status information of the specified unit:
(NETGEAR Switch) #show stack-status
Stack Unit 1 Status
Sampling Mode: Cumulative Summing
--------------------------------------
Unit Current Average Min Max Dropped
--------------------------------------
show supported cardtype (for stack configuration)
Use this command to display information about all card types or specific card types that are
supported in the switch.
Format show supported cardtype [cardindex]
Mode User EXEC
If you do not supply a value for cardindex, the following output displays:
Term Definition
Card Index (CID) The index in the database for the supported card types. This index is used when you
preconfigure a slot.
Card Model The model identifier for the supported card type.
Identifier
Stacking Commands 36

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If you supply a value for cardindex, the following output displays:
Term Definition
Card Type The 32-bit numeric card type for the supported card.
Model Identifier The model identifier for the supported card type.
Card Description The description for the supported card type.
show switch
Use this command to display information about all units in the stack or about a single unit if
you specify the unit value. For units that lack a matching stack template ID and can therefore
not join the stack, the switch status is shown as “STM Mismatch.”
Format show switch [unit]
Mode Privileged EXEC
Term Definition
Switch The unit identifier assigned to the switch.
If you do not specify a value for unit, the following information displays:
Term Definition
Management Indicates whether the switch is the Primary Management Unit, a stack member, or the
Status status is unassigned.
Preconfigured The model identifier of a preconfigured switch ready to join the stack. The model
Model Identifier identifier is a 32-character field that is assigned by the device manufacturer to identify
the device.
Plugged-In Model The model identifier of the switch in the stack. The model identifier is a 32-character
Identifier field that is assigned by the device manufacturer to identify the device.
Switch Status The switch status. Possible values for this state are: OK, Unsupported, Code
Mismatch, Config Mismatch, or Not Present.
A mismatch indicates that a stack unit is running a different firmware version, Switch
Database Management (SDM) template, or configuration than the management unit.
The SDM Mismatch status indicates that the unit joined the stack, but is running a
different SDM template than the management unit. This status is temporary; the stack
unit automatically reloads using the template that is running on the stack manager. If a
Stacking Firmware Synchronization operation is in progress, the status is shown as
Updating Code.
Code Version The detected version of code on the switch.
Stacking Commands 37
