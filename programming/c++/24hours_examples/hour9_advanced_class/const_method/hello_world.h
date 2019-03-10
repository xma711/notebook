#ifndef HELLO_WORLD_H
#define HELLO_WORLD_H

#include <iostream>

class HelloWorld {

private:
	// in the 11 standard we can do the following; for compatibility, better not use
	std::string hello; // = "hello world!";

public:
	HelloWorld() {
		hello = "hello world!";
	}

	void set_greeting(std::string new_greeting);

	// this const makes sure this function will not change any data in the class
	std::string get_greeting() const;
};

#endif
