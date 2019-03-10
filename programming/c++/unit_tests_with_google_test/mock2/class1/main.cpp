#include "cat.h"
#include <iostream>

int main() {
	std::string cat_name = "Tom";
	Cat* cat1 = new Cat(cat_name);
	std::cout << "The name of the cat is: ";
	std::cout << cat1->get_name() << std::endl;

	delete cat1;

	return 0;
}
