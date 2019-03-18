Hooking
----------------------

Hook is a place in code that allows you to tap in to a module
to either provide different behavior or to react when something happens.  
Reference: http://stackoverflow.com/questions/467557/what-is-meant-by-the-term-hook-in-programming

one method: wrapper library. 
Make your own version of library that an application loads,
and wrapper library can be designed to called any of the functionality from the original library,
or replace it with an entire new set of logic.

OS may provde means to insert event hooks at runtime.
If the process inserting the hook has enough permission to do so, it can be done.  
In fact, the linux firewall NetFilter use hooking mechanism to process network events.

One example of system call hooking: http://stackoverflow.com/questions/2103315/linux-kernel-system-call-hooking-example?noredirect=1&lq=1  
what this example does is that:  
	- get the original function: original_call = sys_call_table[__NR_open];  
	- set sys_call_table to read-write  
	- overwrite the system function: sys_call_table[__NR_open] = our_sys_open;


in lecture notes, hooks are explained as 
a set of functions to control operations on kernel objects and security fields in kernel data structures.
There are 2 types of hooks in linux (security module?):  
	- management hooks, used to manage security fields  
	- control hooks, used to perform access controls


