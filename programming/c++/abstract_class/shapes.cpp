#include <iostream>

// Shape will be an abstract data type (ADT)
class Shape {
public:
	Shape() {}
	virtual ~Shape(){}

	virtual double getArea() = 0;
	virtual double getPerim() = 0;
	virtual void draw() = 0;

	// this is not a virtual method
	void say_something() {std::cout << "Shape: i am a shape..\n";}

	//virtual void draw2() = 0; // if derived class doesn't override this method, compiler will give error
};

// and yet, we can still define the pure virtual method..
void Shape::draw() {
	std::cout << "Shape: Abstract drawing mechanism.\n";
}

// the following doesn't help; draw2() must be overridden by derived class
//void Shape::draw2() {
//	std::cout << "Shape: Abstract drawing mechanism 2.\n";
//}

class Circle: public Shape {
public:
	Circle(double radiusIn): radius(radiusIn) {}
	~Circle() {}

	double getArea();
	double getPerim();
	void draw();
private:
	double radius;
	double circumference; 
};

double Circle::getArea() {
	return 3.14 * radius * radius;	
}
double Circle::getPerim() {
	return 2 * 3.14 * radius;
}
void Circle::draw() {
	std::cout << "Circle drawing routine here.\n";
}

int main() {
	//Shape s; // this will lead to an error because Shape is abstract class

	Shape* s;
	s = new Circle(1.0);
	s->draw();
	s->say_something();

	return 0;
}
