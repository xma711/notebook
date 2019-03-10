; ref: http://www.csee.umbc.edu/portal/help/nasm/sample.shtml

	SECTION .data
msg:	db "Hello World", 10
len:	equ $-msg

	SECTION .text
	global main
main:
	mov	edx,	len
	mov	ecx,	msg
	mov	ebx,	1
	mov	eax,	4
	int	0x80

	mov	ebx,	0
	mov	eax,	1
	int	0x80
