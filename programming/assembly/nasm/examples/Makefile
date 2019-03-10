all:
	nasm -f elf -l hello.lst  hello.asm
	ld -m elf_i386 -s -o hello.elf hello.o

clean:
	rm hello.elf hello.lst hello.o
