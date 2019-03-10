#include <iostream>

// this function will change the input integer.
// actually is this really good?
// main function my think that the number will not be changed.
// need to be careful in such case.
void funct1 (int& i) {
	std::cout << "function: input number is " << i << std::endl;
	i = 10;
	std::cout << "function: change input number to " << i << std::endl;
}

// main function
int main() {
	int j = 30;
	int& rj = j;
	std::cout << "j = " << j <<", rj = "<< rj << std::endl;
	rj = -1;
	std::cout << "now set rj to -1.." << std::endl;
	std::cout << "j = " << j <<", rj = "<< rj << std::endl << std::endl;

	int i = -20;
	std::cout << "main: initially num = " << i << std::endl;

	std::cout << "main: now pass the reference to function.." << std::endl;
	// this function looks quite innocent;
	// but i will be changed by this function, which expects a reference;
	// then the function will change the same memory!
	funct1(i);

	std::cout << "main: after finishing the function, now num = " << i << std::endl;
	
	return 0;
}
