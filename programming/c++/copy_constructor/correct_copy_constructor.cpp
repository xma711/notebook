#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

class Cat {
private:
	char* name;
public:
	Cat( char* nameIn) {
		int len = strlen(nameIn);
		this->name = new char[len+1];
		strcpy(name, nameIn);
		printf("in constructor: cat's name is %s\n", this->name);
	};

	// this is a copy constructor, which creates its own memory for the name variable
	Cat (const Cat& origin) {
		int len = strlen(origin.get_name());
		name = new char[len + 1];
		strcpy(name, origin.get_name());
		printf("in copy constructor: copy cat's name is %s\n", name);
	}

	~Cat() {
		printf("in destructor. going to free name variable.\n");
		delete [] name;
	}

	void print_name() {
                printf("my name is %s\n", this->name);
	};

	// the const behind the function name is very important!!
	// it makes sure that the caller won't change the "this" pointer!
	char* get_name() const {
		return this->name;
	};


};


void get_name (Cat catcopy) {
	catcopy.print_name();
	// the catcopy will free its own "name" variable
};

int main() {
	Cat cat1("meow1");
	get_name(cat1); // deliberately pass by value
	
	// now there is no problem
	cat1.print_name();

	// printf("the cat's name is %s\n", cat1.get_name());
	return 0;
}
