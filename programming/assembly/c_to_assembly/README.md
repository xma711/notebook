C and c++ can be translated to assembly using -S option in gcc or g++.

E.g. gcc -S helloworld.c -o hello_world_asm.s

Another exmaple (in linux 32bit) from generating assembly to compile the assembly code to link it and run it (segfault..)

Simple.c:
```
int main(){
	int i=1;
	return 0;
}

```

gcc -S simple.c -o simple.s
```
	.file	"simple.c"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	subl	$16, %esp
	movl	$1, -4(%ebp)
	movl	$0, %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 4.9.2-10ubuntu13) 4.9.2"
	.section	.note.GNU-stack,"",@progbits

```

compile assembly: as -o simple.o simple.s

link: ld -e main -o simple -s -Os simple.o

however, when run ./simple it gives a segfault.

To do
------------

Find a good way to compile assembly codes in linux and run it.

Nasm seems a promising tool.
