Linux security modules (LSM)
--------------------------------

Reference: https://en.wikipedia.org/wiki/Linux_Security_Modules

LSM is a framework that allows the Linux kernel to support a variety of computer security models.  
LSM inserts hooks (upcalls to the module) at every point in the kernel where
a user-level system call is about to result in access to an important internal kernel object
such as inodes and task control blocks.

LSM's access control goal is closely related to system audit, but is subtly different.  
Auditing requires that every attempt at access to be recorded,
but LSM cannot deliver that as it doesn't have enough hooks.


Btw upcall is a call from a lower-level subsystem, such as a kernel, 
to a higher-level subsystem, such as user code.


LSM adds security fields to kernel,
and provides interface to manage these fields.
