How to use two interfaces
--------------------------------

Reference: http://unix.stackexchange.com/questions/16057/use-ssh-with-a-specific-network-interface

"It's not the ssh client that decides through which interface TCP packets should go, it's the kernel. 
In short, SSH asks the kernel to open a connection to a certain IP address, and the kernel decides which interface is to be used by consulting the routing tables."

"You can display the kernel routing tables with the commands route -n and/or ip route show."

Example:

Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.30.0.1       0.0.0.0         UG    0      0        0 eth0
10.30.0.0       0.0.0.0         255.255.255.0   U     1      0        0 eth0
169.254.0.0     0.0.0.0         255.255.0.0     U     1000   0        0 eth0
192.168.122.0   0.0.0.0         255.255.255.0   U     0      0        0 virbr0


"This means that connections to hosts in the 192.168.122.0/24 (i.e., addresses 192.168.122.0 to 192.168.122.255 according to CIDR notation) network will be routed through interface virbr0; 
those to 169.254.0.0/16 and 10.30.0.0/24 will go through eth0, 
and anything else (the 0.0.0.0 line) will be routed through eth0 to the gateway host 10.30.0.1."

