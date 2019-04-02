References
--------------------------------

Reference 1: https://turkeyland.net/projects/overflow/crash.php

reference 1 explains what a RSP, RBP and RIP are. (x86)

RSP is the stack pointer.
It tracks the next available position in the stack.  
A stack grows from large addr to smaller address, 
so RSP should point to the top of the current stack (smallest addr in current stack.)

Stack frame is the section of the stack that is presently active (presently executing function).
It is pointed to by RBP, the base pointer.  
Question: where does the RBP point to? the top or the bottom of the stack frame?  
-- i think it should be the bottom of the stack frame, because the top is pointed to by the stack pointer,  RSP.

RIP is the instruction pointer.
It holds the address of the instruction that the CPU just loaded and is presently executing.

Note that stack is in the (virtual) memory.
Registers are in the CPU. 
We can read the values at registers to understand what memory addresses are used in the stack.

It also has an example to explain how the stack looks like when a function is called 
and when buffer overflow happens. 

When main() calls func1(), the stack will look in this way:  
```
argc, argv, envp
return address
main's frame pointer
main's automatic variables
func1's arguments
return address
func1's frame pointer
func1's automatic variables
...
```

ref1 also mentions that each process runs on its own virtual memory addresses.
This means two processes can use the same virtual addresses
because internally they are mapped to different physical addresses by the kernel.  
This also means that each process works as if it is the only process in the computer.


Reference 2: https://www.cs.umd.edu/class/sum2003/cmsc311/Notes/Mips/stack.html

ref2 explains what a stack is.


Reference 3: http://www.thegeekstuff.com/2012/03/linux-processes-memory-layout

this is given by the teacher.
It explains what a stack is too.


Understand the stack from teacher's sample.c example
----------------------------------------

Firstly, need to disable the address-space randomization:  
sudo sysctl -w kernel.randomize_va_space=0

secondly, need to compile the sample.c with -fno-stack-protector and -g (-g for gdb)

ok now run: gdb sample.elf

break at main function: break main

we can then see the main's codes in assembly language:  disassemble main  
(at this point, we can actually see the the assembly for sample_function too. 
This means all the instructions are placed inside the memory already)

in the current stack, the sample_function instruction is loaded at 0x4005fd in my case.  
The next instruction is at 0x400602. 
The address for the next instruction is important, because this is the location of the memory 
the sample_function should return to after it is done.  
(this value will be stored in the return_address in the stack before the sample_function() is called.)


Ok run the program: run

ok now let's take a look at the registers (info registers), 
which indirectly give us insights into the current stack in the memory.
The register values are what they are right before we enter the main() function.

Note down the current stack pointer (which is the top of the stack; the smallest number, coz stack grows from higher addr to smaller addr) 
(its name is esp or rsp or sth else, depending on machine used),
base pointer and instruction pointer.
In my own execution on a 64bit machine, the sp = 0x7fffffffdc30,
bp = 0x7fffffffdc40 (base of the current stack frame i think), 
ip = 0x4005e3

ok proceed: next  
the console should show "sample_function();",
which means we are right before entering the sample_function.

Now see the assembly codes for the sample function: disassemble sample_function,  
and we will see the top few lines like these:  
line1: addr_a push %rbp  
line2: addr_b mov %rsp, %rbp  
line3: addr_c sub $0x10,%rsp  
....

Line 1 means base pointer's current value is pushed to the stack.  
Line 2 means the current stack pointer value will become the base pointer value for the new stack frame for the sample_function.  
Line 3 subtracts current stack pointer by 10, which is to allocate some space for local variables.

Before we run the sample_function(), let's think about what will happen and verify later.  

Before line 1 is executed, 1 thing has happened: 
a return addr (the value of a memory addr) is pushed to the stack. the return addr is a value indicating where the next instruction is when sample_function() is done.
Of course it is the memory addr of the instruction after sample_function() in the main()'s assembly codes,
which is 0x400602 in my case.  
Because of this, the stack pointer has been minus away by 8 bytes (in 64bit machine; 4 bytes in 32bit machine).
So before line1, the stack pointer = 0x7fffffffdc30 - 8 = 0x7fffffffdc28.
This is also the memory addr of value of the return address (memory addr of a memory addr).

Ok assume that we run line 1. 
Then stack pointer will be decreased by 8 bytes again, because base pointer (rbp) is pushed to the stack.  
So stack pointer becomes 0x7fffffffdc28 - 8 =  0x7fffffffdc20.  
 
Line 2 tells us that base pointer register now stores 0x7fffffffdc20, which is the base of the sample_function stack frame.

Okay after line 3, the stack pointer will be decreased by 0x10.
Sp will become 0x7fffffffdc20 - 0x10 = 0x7fffffffdc10

in summary, we will check if sp becomes  0x7fffffffdc10,
bp becomes 0x7fffffffdc20,
and the value at the return addr (0x7fffffffdc28) is 0x400602.

Okay run into sample_function(): step

now print the registers' values again: info registers  
and what i have are:  
rsp: 0x7fffffffdc10  
rbp: 0x7fffffffdc20

and print value at 0x7fffffffdc28: x/xw 0x7fffffffdc28 (or x/xw $rbp+8).  
The value is 0x400602! 

These values are exactly what we expected.


Override the value at the returned address at the sample_function's stack frame
---------------------------------------------

Follow homework 1


further understanding of stack
-----------------------------------

Question: there are assembly codes (instructions) in the memory, and there is stack in the memory,
who is the boss?

Answer: the instructions in the memory is the boss!!!!  
A stack is created by the instructions.  
The change of the stack is also controlled by the instructions!!!

For example,
main() has some codes:  
sub1	$4, %esp  
mov1	$1, (%esp)  
cal1	foo  
mov1	$0, %eax  
add1	$4, %esp  
...

When main()'s codes are running, main() is in charge of the stack.  
Before it calls foo(), it has to explicitly changes the stack pointer (esp) (subtract 4 away in this case),
and move the argument for foo() (1) to the stack, (and also add the return address), before calling foo.

After calling foo(), the foo() is now in charge of the stack.
After foo() finishes its business, it has to return the control of stack to main().  
How?  
When main() calls foo(), it will set the return address (the address of the next instruction) in the stack before
calling foo().
After foo() is done, it will return the control to main() by returning to the instruction indicated by 
the address value inside the known return address location.
In fact, foo() is not aware of the existence of main().
It simply return the control to the instruction indicated by the return address.

All the variables to modify the stack are the registers!
And the instructions themselves explicitly use these registers to control the stack.

The way the stack grows and shrinks is not a myth!
It is simply controlled by the instructions who use the registers explicitly!!

Ok now here starts my speculation:

everything can be understood as within the control of the instructions.
But there are some hidden instructions that do not show up in the instructions list.
For example, the fact that foo() knows it has to return the control to main() can be considered as 
a hidden instruction associated with foo(). 
After foo()'s own stuff is done, it automatically runs a hidden instruction to jump to 
the instruction in main(), so that main() takes back of the control of stack.

Other register like eip, which stores the address of the current instruction, should be assigned by some instructions too.
But these instructions are considered hidden.

Now ends now speculation.

By hijacking the ret_address, we tricked the foo() function to return control to the instruction at the ret_address.

If the ret_address is a simple instruction (like mov sth), it will simply execute the instruction,
and the next instruction in the memory, until it hits the instruction "ret".  
When the 'ret' instruction is executed, like any function, it will return the control of the stack to the instruction right before the 
current stack frame. 

If the ret_address is a function, the function takes the control of the stack, and then start to
execute the instructions listed in the function.
And this function expects the return address and arguments are right below (higher address than) the 
bottom of the current stack frame, because these are not controlled by the function. 
At the end of this function, there is a 'ret' instruction too.

Function likes to push the old ebp to the first slot of its stack frame, but it is not special. 
It is simply the first instruction in a function, and is mostly likely created by c programming itself.
If a function is written in assembly codes directly, we don't have to write this instruction.  
This means that any instruction sequence (until ret) always assume the current value stored in the ebp register
is the bottom of the current stack frame.  
A 'ret' instruction will base on the ebp to deduce where ret_address is. 
After the 'ret' instruction is executed, ebp should be automatically shifted down (value increases).

Therefore, i think if the hijacked return address returns to a instruction that changes the value in the ebp register,
then next return address may be messed up.

One cleaner way is that after main() transfers control to foo(), the ebp is the stack bottom of foo(),
and we hijack the ret_address, and carefully select the instructions from the memory that do not have anything to do with ebp,
so ebp always increases by 4 after every ret.  
In this way, we can write a consecutive ret addresses into the overflown buffer and each ret address will execute a series of 
instructions in the memory (a gadget) until it hits 'ret'.
