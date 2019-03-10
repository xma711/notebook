#ifndef COUNT_NUM_CHAR_H
#define COUNT_NUM_CHAR_H
#include "helloworld_interface.h"

class COUNT_NUM_CHAR {
private:
	HELLOWORLD_INTERFACE* hw;

public:
	// constructor
	COUNT_NUM_CHAR(HELLOWORLD_INTERFACE* hw_passed_in) {
		// use dependency injection for external object, which is also convenient for unit testing.
		// COUNT_NUM_CHAR class doesn't have to care about the implementation of HELLOWORLD_INTERFACE;
		// there could multiple implementation dependent on who uses COUNT_NUM_CHAR class;
		// This class has to know the APIs only.
		hw = hw_passed_in;
	}

	// a generic function to count the number of characters in a string
	int count_num_char_in_string(char* str);

	// count the number of characters in a string returned by the helloworld function
	int count_after_call_hello_world();

	int call_helloworld_do_nothing_and_return_1 ();
};
#endif
