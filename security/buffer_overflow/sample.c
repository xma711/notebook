#include <stdio.h>
#include <stdlib.h>

void sample_function() 
{
	int i = 0xFFFFFFFF;
	char buffer[10];
	
	printf("In sample_function(), i is stored at 0x%08x.\n", (unsigned int) &i);
	printf("In sample_function(), buffer is stored at 0x%08x.\n", (unsigned int)&buffer);

	printf("Value of i before calling gets(): 0x%08x\n", (unsigned int)i);
	gets(buffer);
	printf("Value of i after calling gets() : 0x%08x\n", (unsigned int)i);
	return;
}

int main()
{
	int x;

	printf("In main(), x is stored at 0x%08x.\n", (unsigned int) &x);
	sample_function();
}
