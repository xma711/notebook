/* create an interface so that it is easier to be mocked by other modules */

#ifndef HELLOWORLD_INTERFACE_H__
#define HELLOWORLD_INTERFACE_H__

// this interface allows different implementation based on inheritance.
// other classes should not use the child classes directly.
// they should use this interface class,
// and use dependency injection (pass of parameter to the constructor e.g.) to use this class.
// all the child classes should maintain the same APIs so that usages of different child classes won't be problematic.
class HELLOWORLD_INTERFACE {

public:
	// constructor
	//HELLOWORLD_INTERFACE () {;} // nothing in constructor

	// destructor must be virtual
	virtual ~HELLOWORLD_INTERFACE() {};

	// copy hello world to str
	// must init it to 0
	virtual void return_hello_world(char * str) = 0;

	// just a function that does nothing
        virtual void do_nothing() = 0;

};
#endif

// example of an interface.
// reference: https://github.com/google/googletest/blob/master/googlemock/docs/ForDummies.md
/*
class Turtle {
  ...
  virtual ~Turtle() {}
  virtual void PenUp() = 0;
  virtual void PenDown() = 0;
  virtual void Forward(int distance) = 0;
  virtual void Turn(int degrees) = 0;
  virtual void GoTo(int x, int y) = 0;
  virtual int GetX() const = 0;
  virtual int GetY() const = 0;
};
*/
