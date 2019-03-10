#ifndef ANIMAL_HOUSE_H
#define ANIMAL_HOUSE_H

#include "animal.h"
#include <iostream>

class Animal_House {
private:
	Animal *resident;
	double house_size;
public:
	Animal_House(Animal* animal, double size) {
		// dependency injection
		this->resident = animal;
		this->house_size = size;
	}

	std::string get_summary();	
};

#endif
