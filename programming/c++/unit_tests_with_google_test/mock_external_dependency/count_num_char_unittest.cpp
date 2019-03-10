/* this is a test that use the google test to run unit tests for C++ codes */
// reference: https://github.com/google/googletest/blob/master/googlemock/docs/ForDummies.md

#include "gtest/gtest.h"
#include "gmock/gmock.h"
#include <stdio.h>
#include <string.h>
#include "count_num_char.h" // the class to be tested
#include "mock_helloworld.h" // the external dependency class that is mocked
//#include "helloworld.h"

using ::testing::AtLeast; 

// this test requires no googlemock, because it has no external dependency
TEST(CountNumCharMethodTest, init) {

	MOCK_HELLOWORLD mock_hw; // in this test this dependency is not used at all

	COUNT_NUM_CHAR count(&mock_hw);

	char str[] = "doing unit testing!!"; // 20 characters

	// call the method that is being tested
	int num = count.count_num_char_in_string(str);

	// make sure the returned str is the expected value
	EXPECT_EQ(20, num);

};

// the simplest test with an external dependency;
// do_nothing() is in hello world and it has no argument needed
TEST(DoNothingTest, init) {
	MOCK_HELLOWORLD mock_hw;

	EXPECT_CALL(mock_hw, do_nothing())             // #3
	.Times(AtLeast(1));

	COUNT_NUM_CHAR count(&mock_hw);

	int num = count.call_helloworld_do_nothing_and_return_1 ();

	EXPECT_EQ(1, num);

};


// try to mock the external HELLOWORLD class
// return_hello_world() function has an argument
// this seems to make things more complicated
TEST(CountHelloworldMethodTest, init) {
	MOCK_HELLOWORLD mock_hw;

	// "::testing::_" means anything matches
	// because count_after_call_hello_world() will generate its own char*buf to be passed into return_hello_world(),
	// i can't exactly know what the pointer to the buf is.
	// so it is better to just check if the function is called
	EXPECT_CALL(mock_hw, return_hello_world(::testing::_)).Times(AtLeast(1));             // #3

	COUNT_NUM_CHAR count(&mock_hw);

	int num = count.count_after_call_hello_world();

	printf("check: num = %d\n", num);

//	EXPECT_EQ(11, num);

};

// example:
/*
  MockTurtle mock_turtle;                          // #2
  EXPECT_CALL(mock_turtle, PenDown())              // #3
      .Times(AtLeast(1));

  Painter painter(&mock_turtle);                   // #4

  EXPECT_TRUE(painter.DrawCircle(0, 0, 10));
*/

// the main function doesn't really have to anything but
int main(int argc, char **argv) {
	::testing::InitGoogleMock(&argc, argv);
        ::testing::InitGoogleTest(&argc, argv);

        printf("unit test for count_num_char module.\n");

        return RUN_ALL_TESTS();
}

