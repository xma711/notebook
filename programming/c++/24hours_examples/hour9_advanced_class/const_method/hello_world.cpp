
#include "hello_world.h"
#include <iostream>


void HelloWorld::set_greeting(std::string new_greeting) {
	this->hello = new_greeting;
}


std::string HelloWorld::get_greeting() const {
	// change local variable is okay
	int i = 2;
	i = 3;

	// the following line will cause an error, because it changes the private data while this method is supposed to be const
	// this->hello = "try change the greeting msg";

	return this->hello;
}

