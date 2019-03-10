// this example shows how a derived class (child class) calls its parent class' constructor

#include <iostream>

class Parent {
// use protected so derived class is able to access the attributes too
protected:
	std::string name;
	int age;
public:
	// in this sense, we know that constructor doesn't have to be virtual,
	// because a child class can write a new constructor;
	// and unlike other normal method, this constructor will never be called again when the child object is passed into any other function in any way
	Parent(std::string name, int age){
		std::cout << "Parent class: in constructor" << std::endl;
		this->name = name;
		this->age = age;
	}

	virtual void get_summary() {
		std::cout << "Parent class: the age of " << this->name << " is " << this->age << std::endl; 
	}

	// however, destructor has to be virtual; 
	// otherwise in the polymophism scenario the parent's destructor may be called instead of child's destructor
	virtual ~Parent() {
		std::cout << "Parent class: in destructor" << std::endl;
	};
};

class Child: public Parent {
private:
	std::string nationality;

public:
	// this is how a child class calls its parent class' constructor
	// ref: https://stackoverflow.com/questions/120876/what-are-the-rules-for-calling-the-superclass-constructor
	Child(std::string name, int age, std::string nationality) : Parent(name, age) {
		std::cout << "Child class: in constructor" << std::endl;
		this->nationality = nationality;
	}
	
	void get_summary() {
		std::cout << "Parent class: the age of " << this->name << " is " << this->age << ", and he/she is from " << this->nationality << std::endl; 
	}

	~Child() {
		std::cout << "Child class: in destructor" << std::endl;
	};


};

int main() {
	Child * c = new Child("Tom", 20, "USA");
	c-> get_summary();
	delete c;

	return 0;
}
