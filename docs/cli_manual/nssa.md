# nssa

Pages: 893-896

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Area Border Router The total number of area border routers reachable within this area.
Count
Area LSA Count Total number of link-state advertisements in this area's link-state database, excluding AS External
LSAs.
Area LSA A number representing the Area LSA Checksum for the specified area ID excluding the external (LS
Checksum type 5) link-state advertisements.
Stub Mode Represents whether the specified Area is a stub area or not. The possible values are enabled and
disabled. This is a configured value.
Import Summary Shows whether to import summary LSAs (enabled).
LSAs
OSPF Stub Metric The metric value of the stub area. This field displays only if the area is a configured as a stub area.
Value
The following OSPF NSSA specific information displays only if the area is configured as an
NSSA.
Term Definition
Import Summary Shows whether to import summary LSAs into the NSSA.
LSAs
Redistribute into Shows whether to redistribute information into the NSSA.
NSSA
Default Information Shows whether to advertise a default route into the NSSA.
Originate
Default Metric The metric value for the default route advertised into the NSSA.
Default Metric Type The metric type for the default route advertised into the NSSA.
Translator Role The NSSA translator role of the ABR, which is always or candidate.
Translator Stability The amount of time that an elected translator continues to perform its duties after it determines that
Interval its translator status has been deposed by another router.
Translator State Shows whether the ABR translator state is disabled, always, or elected.
show ipv6 ospf asbr
This command displays the internal OSPFv3 routes to reach Autonomous System Boundary
Routers (ASBR). This command takes no options.
Format show ipv6 ospf asbr
Modes Privileged EXEC
User EXEC
IPv6 Commands 893

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Type The type of the route to the destination. It can be either:
• intra. Intra-area route
• inter. Inter-area route
Router ID Router ID of the destination.
Cost Cost of using this route.
Area ID The area ID of the area from which this route is learned.
Next Hop Next hop toward the destination.
Next Hop Intf The outgoing router interface to use when forwarding traffic to the next hop.
show ipv6 ospf database
This command displays information about the link state database when OSPFv3 is enabled.
If you do not enter any parameters, the command displays the LSA headers for all areas. Use
the optional area-id parameter to display database information about a specific area.
Use the other optional parameters to specify the type of link state advertisements to display:
• Use external to display the external LSAs.
• Use inter-area to display the inter-area LSAs.
• Use link to display the link LSAs.
• Use network to display the network LSAs.
• Use nssa-external to display NSSA external LSAs.
• Use prefix to display intra-area Prefix LSAs.
• Use router to display router LSAs.
• Use unknown area, unknown as, or link to display unknown area, AS or link-scope
LSAs, respectively.
• As an option, use lsid to specify the link state ID (LSID).
• Use adv-router to show the LSAs that are restricted by the advertising router. AS an
option, use rtrid to specify the router ID.
• Use self-originate to display the LSAs in that are self originated.
Information is displayed only if OSPF is enabled.
Format show ipv6 ospf [area-id] database [{external | inter-area {prefix | router} |
link | network | nssa-external | prefix | router | unknown {area | as |
link}}] [lsid] [{adv-router [rtrid] | self-originate}]
Modes Privileged EXEC
User EXEC
IPv6 Commands 894

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
For each link-type and area, the following information is displayed.
Term Definition
Link Id A number that uniquely identifies an LSA that a router originates from all other self originated LSAs
of the same LS type.
Adv Router The Advertising Router. Is a 32-bit dotted decimal number representing the LSDB interface.
Age A number representing the age of the link state advertisement in seconds.
Sequence A number that represents which LSA is more recent.
Checksum The total number LSA checksum.
Prefix The IPv6 prefix.
Interface The interface for the link.
Rtr Count The number of routers attached to the network.
show ipv6 ospf database database-summary
Use this command to display the number of each type of LSA in the database and the total
number of LSAs in the database.
Format show ipv6 ospf database database-summary
Modes Privileged EXEC
User EXEC
Term Definition
Router Total number of router LSAs in the OSPFv3 link state database.
Network Total number of network LSAs in the OSPFv3 link state database.
Inter-area Prefix Total number of inter-area prefix LSAs in the OSPFv3 link state database.
Inter-area Router Total number of inter-area router LSAs in the OSPFv3 link state database.
Type-7 Ext Total number of NSSA external LSAs in the OSPFv3 link state database.
Link Total number of link LSAs in the OSPFv3 link state database.
Intra-area Prefix Total number of intra-area prefix LSAs in the OSPFv3 link state database.
Link Unknown Total number of link-source unknown LSAs in the OSPFv3 link state database.
Area Unknown Total number of area unknown LSAs in the OSPFv3 link state database.
AS Unknown Total number of as unknown LSAs in the OSPFv3 link state database.
Type-5 Ext Total number of AS external LSAs in the OSPFv3 link state database.
IPv6 Commands 895

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Self-Originated Total number of self originated AS external LSAs in the OSPFv3 link state database.
Type-5
Total Total number of router LSAs in the OSPFv3 link state database.
show ipv6 ospf interface
This command displays the information for the physical interface or virtual interface tables.
The argument unit/slot/port corresponds to a physical routing interface or VLAN
routing interface. The vlan keyword and vlan-id parameter are used to specify the VLAN
ID of the routing VLAN directly instead of in a unit/slot/port format. The vlan-id can
be a number from 1–4093.
You can use the loopback keyword and loopback-id argument to specify a loopback
interface. You can use the tunnel keyword and tunnel-id argument to specify a tunnel
interface.
Format show ipv6 ospf interface {unit/slot/port | vlan vlan-id | loopback
loopback-id | tunnel tunnel-id}
Modes Privileged EXEC
User EXEC
Term Definition
IP Address The IPv6 address of the interface.
ifIndex The interface index number associated with the interface.
OSPF Admin Mode Shows whether the admin mode is enabled or disabled.
OSPF Area ID The area ID associated with this interface.
Router Priority The router priority. The router priority determines which router is the designated router.
Retransmit Interval The frequency, in seconds, at which the interface sends LSA.
Hello Interval The frequency, in seconds, at which the interface sends Hello packets.
Dead Interval The amount of time, in seconds, the interface waits before assuming a neighbor is down.
LSA Ack Interval The amount of time, in seconds, the interface waits before sending an LSA
acknowledgement after receiving an LSA.
Interface Transmit Delay The number of seconds the interface adds to the age of LSA packets before transmission.
Authentication Type The type of authentication the interface performs on LSAs it receives.
Metric Cost The priority of the path. Low costs have a higher priority than high costs.
Prefix-suppression Displays whether prefix-suppression is enabled, disabled, or unconfigured on the given
interface.
IPv6 Commands 896
