# compile the program without stack protector
all:
	gcc -fno-stack-protector -o sample.elf -g sample.c

clean:
	rm sample.elf

# turn off the address-space randomization
setup:
	sudo sysctl -w kernel.randomize_va_space=0
