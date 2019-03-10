#include "hello_world.h"
#include <iostream>

int main() {
	HelloWorld hw;
	std::string msg = hw.get_greeting();
	std::cout << "greeting msg is: " << msg << std::endl;

	std::string new_greeting = "Hi there!";
	hw.set_greeting(new_greeting);
	std::string msg2 = hw.get_greeting();
	std::cout << "new greeting msg is: " << msg2 << std::endl;

	return 0;
}
