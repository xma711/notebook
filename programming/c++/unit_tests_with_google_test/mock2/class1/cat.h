#ifndef CAT_H_
#define CAT_H_

#include "animal.h"

#include <iostream>

class Cat: public Animal {
private:
	std::string name;	

public:
	// constructor
	Cat ( std::string name);

	// destructor
	~Cat() {};

	std::string get_name();	
};

#endif
