#include "cat.h"
#include <iostream>

Cat::Cat( std::string name) {
	std::cout << "Set cat name to " << name << std::endl;
	this->name = name;
}

std::string Cat::get_name() {
	return this->name;
}	
