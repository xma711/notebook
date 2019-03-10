strace
------------------

trace the system calls by a program.

e.g. strace ls, strace sleep


how does strace work
------------------------

reference: http://stackoverflow.com/questions/5494316/how-does-strace-work

internally it uses the ptrace() system call.  
when a system call is made, strace will be notified.  
it will stop the process, do some inspection and logging, and then let the process continue.  
and so on ..
