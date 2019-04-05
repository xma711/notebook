#ifndef HELLOWORLD_H__
#define HELLOWORLD_H__
#include "helloworld_interface.h"

class HELLOWORLD : public HELLOWORLD_INTERFACE {

// this class has to be made inheritable so that it can be mocked by google mock
//class HELLOWORLD  : public HELLOWORLD_INTERFACE {
public:
	// constructor
	//HELLOWORLD () {;} // nothing in constructor

	// destructor
	//virtual ~HELLOWORLD () {;} // nothing in constructor

	// copy hello world to str
	void return_hello_world(char * str);

	void do_nothing();
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
