# mrp_commands

Pages: 498-498

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
no llpf
Use this command to unblock LLPF protocol(s) on a port.
Format no llpf {blockisdp | blockvtp | blockdtp | blockudld | blockpagp | blocksstp
| blockall }
Mode Interface Config
show llpf interface
Use this command to display the status of LLPF rules configured on a particular port or on all
ports..
Format show llpf interface [all | unit/slot/port]
Mode Privileged EXEC
Term Definition
Block ISDP Shows whether the port blocks ISDP PDUs.
Block VTP Shows whether the port blocks VTP PDUs.
Block DTP Shows whether the port blocks DTP PDUs.
Block UDLD Shows whether the port blocks UDLD PDUs.
Block PAGP Shows whether the port blocks PAgP PDUs.
Block SSTP Shows whether the port blocks SSTP PDUs.
Block All Shows whether the port blocks all proprietary PDUs available for the LLDP feature.
MRP Commands
Multicast Registration Protocol (MRP) replaces the Generic Attribute Registration Protocol
(GARP) functionality. MRP provides the same functionality as GARP. MRP is a generic
registration framework defined by the IEEE 802.1ak amendment to the IEEE 802.1Q
standard.
mrp
This command sets the MRP protocol timers on an interface.
Format mrp {jointime seconds | leavetime seconds | leavealltime seconds}
Mode Interface Config
Switching Commands 498
