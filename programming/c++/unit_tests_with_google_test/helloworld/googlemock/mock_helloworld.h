#ifndef MOCK_HELLOWORLD_H__
#define MOCK_HELLOWORLD_H__

#include "gmock/gmock.h"
#include "helloworld_interface.h"

// this mock class of helloworld_interface can be used for unit testing in other modules

class MOCK_HELLOWORLD : public HELLOWORLD_INTERFACE {

public:
	// no need an explicit destructor?
	//MOCK_METHOD0(HELLOWORLD, ~() ); 

	// original function: void return_hello_world(char * str);
	// remember to put a void in front of (char* str)
	MOCK_METHOD1(return_hello_world, void(char* str));

	MOCK_METHOD0(do_nothing, void());
};
#endif

// example of a mocked class
// reference: https://github.com/google/googletest/blob/master/googlemock/docs/ForDummies.md
/*
#include "gmock/gmock.h"  // Brings in Google Mock.
class MockTurtle : public Turtle {
 public:
  ...
  MOCK_METHOD0(PenUp, void());
  MOCK_METHOD0(PenDown, void());
  MOCK_METHOD1(Forward, void(int distance));
  MOCK_METHOD1(Turn, void(int degrees));
  MOCK_METHOD2(GoTo, void(int x, int y));
  MOCK_CONST_METHOD0(GetX, int());
  MOCK_CONST_METHOD0(GetY, int());
};
*/
