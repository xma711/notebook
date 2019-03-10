reference:  http://www.thegeekstuff.com/2012/07/system-calls-library-functions/

library function calls
--------------------

the functions which are a part of standard c library are known as library functions. (libray function may or may not further make system call.)

for examples, the standard string manipulation functions like strcmp() strlen() etc are all library functions.

there are library functions that do not make any system call.  
for example, the string manipulation functions.  

there are library functions that further make system calls,  
e.g. the fopen() function which is a standard library function but internally uses the open() system call.

(it seems system call is at a lower layer than library function calls. system call can be used by library function to achieve some goals in kernel mode.)

system calls
---------------------------

the functions which change the execution mode of the program from user mode to kernel mode are known as system calls.

for example, if we want to change the date and time of the system or if we want to create a network socket  
then these services can only be provided by kernel and hence these cases require system calls.   
for example, socket() is a system call.

system calls act as entry point to OS kernel.   
there are certain tasks that can only be done if a process is running in kernel mode.  
examples of these tasks can be interacting with hardware etc.  
so if a process wants to do such kind of task then it would require itself to be running in kernel mode   
which is made possible by system calls.


interactions
-----------------------

application code can interact with library functions or system calls. (but usefully application code won't use system call directly.)  
a library function can also call system function from within.  
only system calls have access to kernel which further can access computer hardware.


fopen() vs open()
--------------------------

fopen() is a library function which provides buffered I/O services for opening a file.  
open() is a system call that provides non-buffered I/O services.

if a library function corresponding to a systme call exists, then applications should use the library function because:
	- library functions are portable. system call may not be portable; it can vary from system to system.
	- sometimes the library function reduces the frequency to use system call. e.g. not every fread() (with buffered I/O) requires system call read(). 


is malloc() a system call
----------------------
no. it is a library function that further uses brk() or sbrk() systme call for memory allocation.


switching execution modes (user and kernel)
-------------------

today, the systenter/sysexit instructions are used for swithcing the execution mode.

traditionally, the mechanism of raising an interrupt of 'int $0x80' to kernel was used.  
after trapping the interrupt, kernel processes it and changes the exectution mode from user to kernel mode.


other differences
------------------

a library function is linked to the user program and executes in user space  
while a system call is not linked to a user program and executes in kernel space.

a library function execution time is counted in user level time   
while a system call execution time is counted as a part of system time.

library functions can be debugged easily using a debugger  
while system calls cannot be debugged as they are executed by the kernel.


intercept system calls
-----------------------------

reference: http://stackoverflow.com/questions/14415561/intercepting-a-system-call

seems that we can write a kernel module to replace one or some system calls.

the whole point is to change the function stored in the sys_call_table[].  
refer to hooking file too: repo/linux/hooking/README.md


trace system calls
----------------------

use a tool called "strace".

e.g. "strace sleep" will trace all the system calls by command "sleep".

refer to repo/linux/strace/README.md for more details.
