// need to compile with flag to enable c++11:
// g++ -std=c++11 simpleLambda.cpp

#include <iostream>

int main() {
	auto func1 = [] () { std::cout << "Hello world!" << std::endl;};
	func1();
	return 0;
}
