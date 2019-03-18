Dmesg
------------------

Dmesg = display message or driver message

dmesg is a command which will show kernel ring buffers.  
These messages contain valuable information about device drivers loaded into the kernel at the time of booting  
as well as when we connect a hardware to the system on the fly.  

In other words, dmesg will give us details about hardware drivers connected to,  
disconnected from a machine and any errors when hardware driver is loaded into the kernel.
 
To use it, simply use 'dmesg' to see all device drivers loaded into kernel. or  
dmesg | grep -i eth0  
to see info about eth0

reference: http://www.linuxnix.com/2013/05/what-is-linuxunix-dmesg-command-and-how-to-use-it.html
