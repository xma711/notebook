// try lamda function
// need to compile with the -std=c++11 flag!

#include <iostream>
#include <vector>
#include <algorithm> // need to include this lib to use for_each function

int main() {

	// prepare a vector
	std::vector<int> v1;
	int i;
	for (i=0; i<10; i++) {
		v1.push_back(i);
	}
	
	// use for_each and a lambda function to do something on each element
	std::for_each (v1.begin(), v1.end(), [](int ele) { std::cout << ele << std::endl; } );

	return 0;
}
