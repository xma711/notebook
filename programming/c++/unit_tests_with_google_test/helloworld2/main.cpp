#include "helloworld.h"
#include <stdio.h>
#include <stdlib.h>

int main() {
	HELLO_WORLD* hw = new HELLO_WORLD();
	char msg[20];
	hw->return_hello(msg);
	printf("returned from function: %s\n", msg);
	delete hw; // btw, end of function will not automatically free a 'new' object so it is always better to free it by ourselves 

	HELLO_WORLD hw2; 
	// cannot put a () in the above line; 
	// ref: https://stackoverflow.com/questions/877523/error-request-for-member-in-which-is-of-non-class-type

	char msg2[20];
	hw2.return_hello(msg2);
	printf("returned from function from 2nd object: %s\n", msg2);

	return 0;
}
