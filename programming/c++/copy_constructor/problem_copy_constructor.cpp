#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

class Cat {
private:
	char* name;
public:
	// there is no customized copy constructor (only default copy constructor is hidden), 
	// so it will be a shallow copy if the value is passed into a function
	Cat( char* nameIn) {
		int len = strlen(nameIn);
		this->name = new char[len+1];
		strcpy(name, nameIn);
		printf("in constructor: cat's name is %s\n", this->name);
	};

	~Cat() {
		printf("in destructor. going to free name variable.\n");
		delete [] name;
	}

	void print_name() {
                printf("my name is %s\n", this->name);
	};
};


void get_name (Cat catcopy) {
	catcopy.print_name();
	// the catcopy will call the destructor and free the same pointer to the name variable, 
	// which then cause problem to the original cat object.
};

int main() {
	Cat cat1("meow1");
	get_name(cat1); // deliberately pass by value
	
	// this line will cause the program to crash because the variable name has been freed.
	cat1.print_name();
	return 0;
}
