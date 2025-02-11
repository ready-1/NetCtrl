# ecmp_retries_the_number_of_ecmp_routes_that_have_been_installed_in_the_forwarding_table_after

Pages: 855-856

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Term Definition
Unresolved Route Adds The number of route adds that failed because none of the route’s next hops were on a
local subnet. Note that static routes can fail to be added to the routing table at startup
because the routing interfaces are not yet up. This counter gets incremented in this
case. The static routes are added to the routing table when the routing interfaces come
up.
Invalid Route Adds The number of routes that failed to be added to the routing table because the route
was invalid. A log message is written for each of these failures.
Failed Route Adds The number of routes that failed to be added to the routing table because of a resource
limitation in the routing table.
Hardware Failed Route Adds The number of routes that failed to be inserted into the hardware because of a hash
error or a table-full condition.
Reserved Locals The number of routing table entries reserved for a local subnet on a routing interface
that is down. Space for local routes is always reserved so that local routes can be
installed when a routing interface bounces.
Unique Next Hops The number of distinct next hops used among all routes currently in the routing table.
These include local interfaces for local routes and neighbors for indirect routes.
Unique Next Hops High Water The highest count of unique next hops since counters were last cleared.
Next Hop Groups The current number of next hop groups in use by one or more routes. Each next hop
group includes one or more next hops.
Next Hop Groups High Water The highest count of next hop groups since counters were last cleared.
ECMP Groups The number of next hop groups with multiple next hops.
ECMP Routes The number of routes with multiple next hops currently in the routing table.
Truncated ECMP Routes The number of ECMP routes that are currently installed in the forwarding table with
just one next hop. The forwarding table may limit the number of ECMP routes or the
number of ECMP groups. When an ECMP route cannot be installed because such a
limit is reached, the route is installed with a single next hop.
ECMP Retries The number of ECMP routes that have been installed in the forwarding table after
initially being installed with a single next hop.
Routes with n Next Hops The current number of routes with each number of next hops.
Command example:
(NETGEAR Switch) #show ipv6 route summary
Connected Routes............................... 4
Static Routes.................................. 0
6To4 Routes.................................... 0
OSPF Routes.................................... 13
Intra Area Routes............................ 0
Inter Area Routes............................ 13
External Type-1 Routes....................... 0
External Type-2 Routes....................... 0
IPv6 Commands 855

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Reject Routes.................................. 0
Total routes................................... 17
Best Routes (High)............................. 17 (17)
Alternate Routes............................... 0
Route Adds..................................... 44
Route Deletes.................................. 27
Unresolved Route Adds.......................... 0
Invalid Route Adds............................. 0
Failed Route Adds.............................. 0
Reserved Locals................................ 0
Unique Next Hops (High)........................ 8 (8)
Next Hop Groups (High)......................... 8 (8)
ECMP Groups (High)............................. 3 (3)
ECMP Routes.................................... 12
Truncated ECMP Routes.......................... 0
ECMP Retries................................... 0
Routes with 1 Next Hop......................... 5
Routes with 2 Next Hops........................ 1
Routes with 3 Next Hops........................ 1
Routes with 4 Next Hops........................ 10
Number of Prefixes:
/64: 17
clear ipv6 route counters
The command resets to zero the IPv6 routing table counters reported in the command show
ipv6 route summary on page854. The command only resets event counters. Counters that
report the current state of the routing table, such as the number of routes of each type, are
not reset.
Format clear ipv6 route counters
Mode Privileged Exec
clear ipv6 snooping counters
This command clears the counters that are associated with the IPv6 RA guard host mode.
Format clear ipv6 snooping counters
Modes EXEC
Global Config
IPv6 Commands 856
