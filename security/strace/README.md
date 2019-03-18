Strace
------------------

Trace the system calls by a program.

E.g. strace ls, strace sleep


how does strace work
------------------------

Reference: http://stackoverflow.com/questions/5494316/how-does-strace-work

internally it uses the ptrace() system call.  
When a system call is made, strace will be notified.  
It will stop the process, do some inspection and logging, and then let the process continue.  
And so on ..
