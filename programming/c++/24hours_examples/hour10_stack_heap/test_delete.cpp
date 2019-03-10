#include <iostream>

int main() {
	int* p = new int;

	*p = 10;

	delete p;

	//  set p to nullptr after delete.
	// then even we do a 2nd delete on p, there is no problem
	// p = NULL; // a less optimized choice because NULL is equivalent to 0
	p = nullptr; // a better choice; however, have to compile with flag" -std=c++11"

	delete p;

	return 0;
}
