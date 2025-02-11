# octets_total_number_of_packets_which_are_64_octets_in_length_excluding_framing_bits_including

Pages: 358-358

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
show rmon statistics interfaces
This command displays the RMON statistics for the given interfaces.
Format show rmon statistics interfaces unit/slot/port
Mode Privileged Exec
Term Description
Port unit/slot/port
Dropped Total number of dropped events on the interface.
Octets Total number of octets received on the interface.
Packets Total number of packets received (including error packets) on the interface.
Broadcast Total number of good broadcast packets received on the interface.
Multicast Total number of good multicast packets received on the interface.
CRC Align Errors Total number of packets received have a length (excluding framing bits, including FCS
octets) of between 64 and 1518 octets inclusive.
Collisions Total number of collisions on the interface.
Undersize Pkts Total number of undersize packets. Packets are less than 64 octets long (excluding
framing bits, including FCS octets).
Oversize Pkts Total number of oversize packets. Packets are longer than 1518 octets (excluding
framing bits, including FCS octets).
Fragments Total number of fragment packets. Packets are not an integral number of octets in
length or had a bad Frame Check Sequence (FCS), and are less than 64 octets in
length (excluding framing bits, including FCS octets).
Jabbers Total number of jabber packets. Packets are longer than 1518 octets (excluding
framing bits, including FCS octets), and are not an integral number of octets in length
or had a bad Frame Check Sequence (FCS).
64 Octets Total number of packets which are 64 octets in length (excluding framing bits, including
FCS octets).
65-127 Octets Total number of packets which are between 65 and 127 octets in length (excluding
framing bits, including FCS octets).
128-255 Octets Total number of packets which are between 128 and 255 octets in length (excluding
framing bits, including FCS octets).
256-511 Octets Total number of packets which are between 256 and 511 octets in length (excluding
framing bits, including FCS octets).
512-1023 Octets Total number of packets which are between 512 and 1023 octets in length (excluding
framing bits, including FCS octets).
1024-1518 Octets Total number of packets which are between 1024 and 1518 octets in length (excluding
framing bits, including FCS octets).
Utility Commands 358
