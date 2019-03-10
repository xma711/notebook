#include <iostream>
#include <vector> // need to include this lib to use vector
#include <algorithm> // need to include this lib to use for_each
int main() {
	// this looks exactly like the function declaration in Node.js
	auto func1 = [] (int age) {
		std::cout << "The age is " << age << std::endl;
	};
	
	func1(10);

	// another usage of lambda function is to use with std::for_each() function, which reminds me of Node.js function also.
	
	// create a vector
	std::vector<int> v;
	for (int i = 0; i < 10; i++) {
		v.push_back(i);
	}
	// there are 3 arguments to for_each() function: the beginning of vector, the end of vector, and the lambda function.
	auto func_handle_ele = [](int e) {
		std::cout << e << std::endl;
	};

	// this is easier to understand, 
	// because the lambda function is just an argument and can be defined outside the for_each() function 
	std::for_each( v.begin(), v.end(), func_handle_ele );

	return 0;
}
