#include "helloworld.h"
#include <string.h>

void HELLO_WORLD:: return_hello( char* buf ) {
	const char *msg = "hello world!";
	strcpy(buf, msg);
}

int HELLO_WORLD:: return0 () {
	return 0;
}
