/sys/
--------------------------------------
Sysfs is a virtual file system provided by the Linux kernel that exports information about various kernel subsystems, hardware devices, 
and associated device drivers from the kernel's device model to user space through virtual files. 
In addition to providing information about various devices and kernel subsystems, exported virtual files are also used for their configuring.

Sysfs privides an interface between kernelspace and userspace.

Reference: http://www.linux.org/threads/sysfs-and-configfs.4956/


/sys/class/
------------------
This directory contains folders named by device type like "printers", "mem", "leds", "input", etc.  
The subdirectories then contain shortcuts to the sysfs files pertaining to the selected device.


/sys/devices/
---------------------
Most of the symbolic links in the sysfs system link to devices and files here


/sys/module/
----------------------
All of the loaded modules can be seen here.  
Each folder contains information and settings for that particular module.


/sys/firmware/
----------------------
Files containing information and settings for the system's firmware resides here.


/sys/kernel
-------------------
The folder contains settings, information, and security policies


/sys/bus/
-------------------
The directory contains the sysfs files and data for the different buses on the system.


/sys/power/
------------------
The directory contains files with information on the power state, the number of times the system hibernated/slept, etc

