/proc/
-----------------

Reference: http://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/proc.html

the directory /proc/ stores the virtual files that 'store' the information of the system and processes.

E.g. each folder named by a number is a process.  
Cd into the process_id, we can see all the info related to this process.  
	- exe: the symbolic link to the binary  
	- cmdline: the command line that starts this process  
	- stack: the stack ..  
	- maps: the memory map  
	- environ: the environment variables  
	- status: human readable info  
	

there are other things about the system info in /proc/. e.g.  
	- cmdline: the command line that starts the kernel: in fact the file stores the familiar line: BOOT_IMAGE=/boot/vmlinuz-3.13.0-95-generic root=UUID=0661f1e1-bde6-4a3f-987d-e99489a80acd ro quiet splash  
	- cpuinfo: as explained by the filename  
	- uptime  
	- interrupts


