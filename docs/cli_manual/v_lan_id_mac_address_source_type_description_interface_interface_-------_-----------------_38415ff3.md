# v_lan_id_mac_address_source_type_description_interface_interface_-------_-----------------_38415ff3

Pages: 638-638

## Content

M4300 Intelligent Edge Series Fu llyManaged Stackable Switches
Command example:
If one or more entries exist in the multicast forwarding table, the output is similar to the
following:
(NETGEAR Switch) #show mac-address-table multicast
Fwd
V LAN ID MAC Address Source Type Description Interface Interface
------- ----------------- ------- ------- --------------- --------- ---------
1 01:00:5E:01:02:03 Filter Static Mgmt Config Fwd: Fwd:
1/0/1, 1/0/1,
1/0/2, 1/0/2,
1/0/3, 1/0/3,
1 /0/4, 1/0/4,
1/0/5, 1/0/5,
1/0/6, 1/0/6,
1 /0/7, 1/0/7,
1/0/8, 1/0/8,
1/0/9, 1/0/9,
1/0/10, 1/0/10,
show mac-address-table stats
This command displays the Multicast Forwarding Database (MFDB) statistics.
Format show mac-address-table stats
Mode Privileged EXEC
Term Definition
Total Entries The total number of entries that can possibly be in the Multicast Forwarding Database table.
Most MFDB Entries The largest number of entries that have been present in the Multicast Forwarding Database table.
Ever Used This value is also known as the MFDB high-water mark.
Current Entries The current number of entries in the MFDB.
Switching Commands 638
