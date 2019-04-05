/* this example is to check the overriding methods in a child class;
 * when the parent uses virtual or not, it makes a big difference.
 * and also to see how to call the parent methods from child class even they have been overridden.
*/

#include <stdio.h>
#include <stdlib.h>

class parent {
public:
	// you don't need a 'virtual' to allow a child to overwrite the method
	// but once the child is casted to a parent class in the polymophism scenario, the parent method will be called; 
	// this is usually undesired.
	void print_something() {
		printf ("i'm the parent.\n");
	}

	virtual void print_again() {
		printf("virtual function: i'm the parent.\n");
	}
};

class child: public parent {
public:
	// try to override the same function in parent that has not virtual keyword
	void print_something () {
		printf("i'm the child.\n");
	}

	// this method has virtual keyword in parent
	virtual void print_again () {
		printf("virtual function: i'm the child\n");
	}

	// the results show that the child class can still call the parent class's methods even if they are overridden.
	void print_something_from_parent () {
		printf ("child: try to call parent's function:\n");
		parent::print_something();
	}

	// the result shows that we can call the parent function even if it is a virtual function
	void print_again_from_parent() {
		printf("child: try to call parent's virtual function:\n");
		parent::print_again();
	}
};


int main() {
	child* obj1 = new child;
	obj1->print_something();
	obj1->print_again();
	obj1->print_something_from_parent();
	obj1->print_again_from_parent();

	printf("\ntry to cast child obj to parent obj and call the functions:\n");
	parent* cast = (parent*) obj1;
	cast->print_something();
	cast->print_again(); // the results show that with the virtual keyword, this function will still execute the child function, which is usually more desired
	return 0;
}
