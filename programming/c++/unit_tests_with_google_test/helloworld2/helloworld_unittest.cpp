#include "helloworld.h"
#include "gtest/gtest.h"
#include <stdio.h>
#include <stdlib.h>

// reference: https://github.com/google/googletest/blob/master/googletest/docs/Primer.md

namespace{
/*************************************************************/
/* create test fixture, if needed */		
/*************************************************************/
	class HelloWorldTest: public ::testing::Test {
	 	protected:
		virtual void SetUp () {
			printf("setup function: create hw object.\n");
			hw = new HELLO_WORLD();
		}

		virtual void TearDown () {
			printf("teardown function: free hw object.\n");
			delete hw;
		}

		// objects declared here can be used by all tests in TEST_F
		HELLO_WORLD *hw;

	}; // end of class

/*************************************************************/
/* start the tests now */		
/*************************************************************/
	// the difference between TEST() and TEST_F() is that TEST() doesn't use test fixture while TEST_F() does.
	TEST_F(HelloWorldTest, MethodReturnHello) {
		// hw instance is created in test fixture
		char msg[20];
		hw->return_hello(msg);
		ASSERT_STREQ(msg, "hello world!");
	}

	TEST_F(HelloWorldTest, MethodReturn0) {
		int ret = hw->return0();
		ASSERT_EQ(ret, 0);
	}

} // end namespace

int main(int argc, char **argv) {
	::testing::InitGoogleTest(&argc, argv);
	return RUN_ALL_TESTS();
} 
