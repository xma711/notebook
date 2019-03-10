#include <string.h>
#include <stdio.h>
#include "count_num_char.h"

int COUNT_NUM_CHAR::count_num_char_in_string(char* str) {
	return (int) strlen(str);
}

// make helloworld object an argument
// otherwise it is very hard to separate the helloworld object when doing unit testing
int COUNT_NUM_CHAR::count_after_call_hello_world() {
	char buf[50];

	printf("count_after_call_hello_world: buf originally = %s\n", buf);

	// hw is a private attribute
	// get the hello string and store to buf
	hw->return_hello_world(buf);

	printf("count_after_call_hello_world: buf returned = %s\n", buf);

	return count_num_char_in_string(buf);
}


int COUNT_NUM_CHAR::call_helloworld_do_nothing_and_return_1 () {
	hw->do_nothing();
	return 1;
}
