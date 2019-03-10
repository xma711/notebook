#include "animal_house.h"
#include <iostream>
#include <sstream>

std::string Animal_House::get_summary() {
	std::stringstream ss;
	ss << this->resident->get_name() << " lives in an animal house with a size of " << this->house_size;
	std::string ret = ss.str();
	return ret;
}
