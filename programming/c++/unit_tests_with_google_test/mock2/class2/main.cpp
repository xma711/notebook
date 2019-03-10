#include "cat.h"
#include "animal_house.h"

int main() {
	std::string cat_name = "Tom";
	double house_size = 100;
	Cat* cat1 = new Cat (cat_name);
	Animal_House* house = new Animal_House (cat1, house_size);

	std::cout << house->get_summary() << std::endl;
	return 0;
}
