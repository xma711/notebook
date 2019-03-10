#ifndef MOCK_CAT_H_
#define MOCK_CAT_H_

#include "gmock/gmock.h"
#include "animal.h"

#include <iostream>

class Mock_Cat: public Animal {
private:
	std::string name;	

public:
	// what about constructor?

	// mock the only meaningful method in Cat class
	MOCK_METHOD0(get_name, std::string() );

};

#endif
