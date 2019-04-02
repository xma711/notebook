// this example will print the order of the constructors and destructors that will be called

// note that parent's destructor will always be called after the child's destructor.

// if any of the function in your class are virtual, the destructor also should be virtual.
// why? 
// because when you pass the child object ptr to a function expecting the parent object, if this function needs to delete the object, it will call the child object's destructor (which will later call parent's destructor). if parent's destructor is not virtual, the parent's destructor will be called instead. this will cause problems.

#include <iostream>

class Parent {
public:
	Parent() {
		std::cout << "Parent class: in constructor" << std::endl;
	};
	virtual ~Parent() { // this is correct
	//~Parent() { // this is incorrect;
		std::cout << "Parent class: in destructor" << std::endl;
	};

	virtual void do_something() {
		std::cout << "Parent class: do something " << std::endl;
	}
};

class Child: public Parent {
public:
	Child() {
		std::cout << "Child class: in constructor" << std::endl;
		num = new int;
	};
	~Child() {
		std::cout << "Child class: in destructor" << std::endl;
		delete num;
	};

	void do_something() {
		std::cout << "Child class: do something " << std::endl;
	}
private:
	int *num;
};

void play_obj_and_delete (Parent * ptr) {
	ptr->do_something();
	delete ptr; // if parent's destructor is not virtual, this will call parent's destructor only!
}

int main() {
	Child *c = new Child;
	play_obj_and_delete(c);
	return 0;
}
