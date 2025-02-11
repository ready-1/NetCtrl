# multicast_static_routes_source_ip_s_ource_mask_rpf_address_preference_---------------_----_499eeceb

Pages: 1021-1021

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
If you use the summary parameter, the command displays the following column headings in
the output table.
Term Definition
Source IP Addr The IP address of the multicast data source.
Group IP Addr The IP address of the destination of the multicast packet.
Protocol The multicast routing protocol by which this entry was created.
Incoming Interface The interface on which the packet for this source arrives.
Outgoing Interface The list of outgoing interfaces on which this packet is forwarded.
List
show ip mroute static
Use this command in Privileged EXEC or User EXEC mode to display all the static routes
configured in the static mcast table, if it is specified, or display the static route associated with
the particular sourceipaddr.
Format show ip mroute static [sourceipaddr]
Modes Privileged EXEC
User EXEC
Parameter Description
Source IP IP address of the multicast source network.
Source Mask The subnetwork mask pertaining to the sourceIP.
RPF Address The IP address of the RPF next-hop router toward the source.
Preference The administrative distance for this Static MRoute.
Command example:
console#show ip mroute static
MULTICAST STATIC ROUTES
Source IP S ource Mask RPF Address Preference
--------------- --------------- --------------- ----------
1.1.1.1 255.255.255.0 2.2.2.2 23
IP Multicast Commands 1021
