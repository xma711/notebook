#ifndef ANIMAL_H_
#define ANIMAL_H_

#include <iostream>

// an abstract class
class Animal {

public:
	// constructor
	//virtual Animal( std::string name) = 0;

	// destructor
	virtual ~Animal() {};

	virtual std::string get_name() = 0; // this line makes this class an abstract data type
};

#endif
