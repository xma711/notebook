unix domain sockets
----------------------

reference: http://pymotw.com/2/socket/uds.html (using python)

similar to TCP/IP socket, but using a path on the filesystem as the address rather than servername and port.

the node created in the filesystem to represent the socket persists after the socket is closed, and needs to be removed each time the server starts up.

```
import socket
import sys
import os
server_address = './uds_socket'
# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
# Bind the socket to the port
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

```


concepts
------------------

reference: http://man7.org/linux/man-pages/man7/unix.7.html (using c)

```
       #include <sys/socket.h>
       #include <sys/un.h>

       unix_socket = socket(AF_UNIX, type, 0);
       error = socketpair(AF_UNIX, type, 0, int *sv);
```
(where the socket is not opened yet. need to specify the address and open the connection.)


the AF_UNIX socket family is used to communicate between processes on the same machine efficiently.

the valid socket types in the unix domain are:  
SOCK\_STREAM (stream oriented),  
SOCK\_DGRAM (datagram-oriented, preserve message boundaries, no reordering datagrams), and  
SOCK_SEQPACKET (connection-oriented socket, preserver message boundaries, delivers messages in order)


