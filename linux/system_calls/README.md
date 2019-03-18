Reference:  http://www.thegeekstuff.com/2012/07/system-calls-library-functions/

library function calls
--------------------

The functions which are a part of standard c library are known as library functions. (libray function may or may not further make system call.)

For examples, the standard string manipulation functions like strcmp() strlen() etc are all library functions.

There are library functions that do not make any system call.  
For example, the string manipulation functions.  

There are library functions that further make system calls,  
e.g. the fopen() function which is a standard library function but internally uses the open() system call.

(it seems system call is at a lower layer than library function calls. system call can be used by library function to achieve some goals in kernel mode.)

System calls
---------------------------

The functions which change the execution mode of the program from user mode to kernel mode are known as system calls.

For example, if we want to change the date and time of the system or if we want to create a network socket  
then these services can only be provided by kernel and hence these cases require system calls.   
For example, socket() is a system call.

System calls act as entry point to OS kernel.   
There are certain tasks that can only be done if a process is running in kernel mode.  
Examples of these tasks can be interacting with hardware etc.  
So if a process wants to do such kind of task then it would require itself to be running in kernel mode   
which is made possible by system calls.


Interactions
-----------------------

Application code can interact with library functions or system calls. (but usefully application code won't use system call directly.)  
A library function can also call system function from within.  
Only system calls have access to kernel which further can access computer hardware.


Fopen() vs open()
--------------------------

Fopen() is a library function which provides buffered I/O services for opening a file.  
Open() is a system call that provides non-buffered I/O services.

If a library function corresponding to a systme call exists, then applications should use the library function because:
	- library functions are portable. system call may not be portable; it can vary from system to system.
	- sometimes the library function reduces the frequency to use system call. e.g. not every fread() (with buffered I/O) requires system call read(). 


Is malloc() a system call
----------------------
No. it is a library function that further uses brk() or sbrk() systme call for memory allocation.


Switching execution modes (user and kernel)
-------------------

Today, the systenter/sysexit instructions are used for swithcing the execution mode.

Traditionally, the mechanism of raising an interrupt of 'int $0x80' to kernel was used.  
After trapping the interrupt, kernel processes it and changes the exectution mode from user to kernel mode.


Other differences
------------------

A library function is linked to the user program and executes in user space  
while a system call is not linked to a user program and executes in kernel space.

A library function execution time is counted in user level time   
while a system call execution time is counted as a part of system time.

Library functions can be debugged easily using a debugger  
while system calls cannot be debugged as they are executed by the kernel.


Intercept system calls
-----------------------------

Reference: http://stackoverflow.com/questions/14415561/intercepting-a-system-call

seems that we can write a kernel module to replace one or some system calls.

The whole point is to change the function stored in the sys_call_table[].  
Refer to hooking file too: repo/linux/hooking/README.md


trace system calls
----------------------

Use a tool called "strace".

E.g. "strace sleep" will trace all the system calls by command "sleep".

Refer to repo/linux/strace/README.md for more details.
