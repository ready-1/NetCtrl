# 1 Energy-Detect EEE LPI-History LLDP-Cap-Exchg Pwr-Usg-Est

Pages: 341-341

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If you do not specify a port, the command displays the information in the following table.
Term Definition
Global
Cumulative Energy Saving per Estimated cumulative energy saved in the stack in (watts * hours) due to all green
Stack modes enabled.
Current Power Consumption per Power consumption by all ports in the stack in mWatts.
Stack
Power Saving Estimated percentage power saved on all ports in the stack due to Green mode(s)
enabled.
Unit Unit Index of the stack member.
Green Ethernet Features supported List of Green Features supported on the given unit which could be one or more of
the following: Energy-Detect (Energy Detect), EEE (Energy Efficient Ethernet),
LPI-History (EEE Low Power Idle History), LLDP-Cap-Exchg (EEE LLDP Capability
Exchange), Pwr-Usg-Est (Power Usage Estimates).
Energy Detect
Energy-detect Config Energy-detect Admin mode is enabled or disabled
Energy-detect Opr Energy detect mode is currently active or inactive. The energy detect mode may be
administratively enabled, but the operational status may be inactive.
EEE
EEE Config EEE Admin Mode is enabled or disabled.
Command example:
The following example shows that the system supports all green Ethernet features:
(NETGEAR Switch) (Config)#show green-mode
Current Power Consumption /Stack (mW).......... 12259
Percentage Power Saving /Stack (%)............. 0
Cumulative Energy Saving /Stack (W * H)........ 0
Unit Green Ethernet Features Supported
---- ---------------------------------
1 Energy-Detect EEE LPI-History LLDP-Cap-Exchg Pwr-Usg-Est
Interface Energy-Detect EEE
Config Opr Config
--------- --------- --------- --------
1/0/1 Disabled Inactive Disabled
1/0/2 Disabled Inactive Disabled
1/0/3 Disabled Inactive Disabled
Utility Commands 341
