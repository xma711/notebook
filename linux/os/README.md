How can the os act as the intermediary between the compiled application and the hardware
----------------------

Reference: http://stackoverflow.com/questions/12811359/how-does-a-compiled-program-interact-with-the-os

another question: how does the compiled application code (machine code) interact with the operating system  
in order to do things like getting input from the keyboard?


Answer:

the operating system acts as a level of abstraction between software and hardware.

The os communicates with the hardware through programs called drivers,  
and the os communicate with software through procedures called system calls.

When you make a system call, you are leaving the application program and  
entering codes of the operating system.

System calls are the only way programmers are allowed to communicate with resources.


All codes are just machine codes running on the cpu.  
No code is higher or lower than the other.  
So the question is: how can the OS possibly be in control?

Ther is a concept called an interrupt.  
This is a signal sent to the cpu that causes the currently running code 
to stop and get switched out with another piece of code, called an interrupt handler.

Examples of interrupts include the keyboard, the mouse, and most importantly, the clock.

The clock interrupt is raised on a regular basis,  
allowing the OS's clock interrupt handler to run. 

Within this clock interrupt handler is the OS's code that examines what code is currently running,
determining what code needs to run next.  
This can be either more operating system code or more user code.

Because the clock is always ticking,  
and because the OS always gets this periodic chance to run on the cpu,  
it is able to orchestrate everything within the computer,  
even though it runs using the same set of CPU commands as any normal program. 


From core to programming
------------------------------

Processor/cpu: execute direclty on machine code.   
Each machine code instruction performs a very specific task, such as load, a jump or an ALU operation on a unit of data in a CPU register or memory.  
Machine codes are different for differenc processors.

Processor/cpu: provides the instruction set (in assembly language format) to do calculation and branches etc.  
However, these instructions still need to be translated to machine code before processor really executes them.

Assembly language: a language that use the instruction set to do some tasks. this can be different for different processors (e.g. x86 vs arm)

all higher level programs: compiler translate these higher level programs to assembly language with the exact logics intact (is assembly a must intermediate step?)  
Higher level programs can be the same for different architectures. but they have to be translated/compiled to the right assembly language and thus the right machine codes for different processors.

Kernel in os: the program that manages all hardware resources and provide system call APIs to other programs to use the hardware resources.  
Note that kernel is just a program. it can be compiled for different processors. e.g. ubuntu can be compiled for linux64, linux32 and even ARM. 

User programs: programs that relies on the kernel to use the hardware resources if needed.  
User programs are usually portable, but needed to be compiled differently. 
However, if a library function uses a particular system call with functionality offered by this particular os only (other os doesn't have equivalent system call), this library function cannot be ported to other os.  
Then if a user program uses this library function, then it cannot be ported to other os. (my own understanding.)


Questions: 
	- where is machine code's place? -> cpu can only exectute machine code.
	- how can kernel keep all program in check?
	- the modern day os is not just the kernel right? seems many tools are included in the so called os.
	- the interaction between kernel and hardware? -> all hardware provides drivers. but how come the kernel knows what hardwares are there and how to run the drivers?

Reference: https://en.wikibooks.org/wiki/A-level_Computing/AQA/Computer_Components,_The_Stored_Program_Concept_and_the_Internet/Machine_Level_Architecture/Machine_code_and_processor_instruction_set#Machine_code_and_instruction_sets


kernel in linux
--------------------------
Reference: http://www.howtogeek.com/howto/31632/what-is-the-linux-kernel-and-what-does-it-do/

in /boot/ folder, one can find vmlinuz-xxx.
	- where vm is virtual memory, linu is linux, z means compression with zlib

there are other formats, such as zImage (compressed + virtual memory support), and bzImage (zImage compressed to the max)

other fles in /boot/:
	- initrd,img-version: used as as a small RAM disk that extracts and executes the actual kernel file.
	- system.map-version: used for memory management before the kernel fully loads
	- config-version: tells the kernel what options and modules to load into the kernel image when it is being compiled.

Because linux kernel is monolithic, it has the largest footprint and the most complexity over the other types of kernels. 

However, nowadays linux kernel modules could be loaded and unloaded at runtime. 

Linux kernel module
----------------------------

Linux has every driver available installed and one just have to turn on the drivers needed.

Linux kernel modules, aka a loadable kernel module (LKM), are essential to keep the kernel functioning with all the hardware without comsuming all the available memeory.

A module typically adds functionality to the base kernel for things like devices, file systems, and system calls.

LKMs have the file extension .ko and are typically stored in the /lib/modules directory.

Kernel can be customized by setting modules to load/not load during startup with the menuconfig or by editing /boot/config file. or load and unload modules on the fly with modprobe command.

Some third party provide closed kernel module in .ko for distribution, such as nVidia, ATI, etc.
