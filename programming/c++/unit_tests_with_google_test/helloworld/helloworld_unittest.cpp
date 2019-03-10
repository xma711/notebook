/* this is a test that use the google test to run unit tests for C++ codes */

#include "gtest/gtest.h"
#include <stdio.h>
#include <string.h>
#include "helloworld.h"

TEST(HelloworldTest, init) {
	char buf[50];

	HELLOWORLD hello_obj;

	// call the method that is being tested
	hello_obj.return_hello_world(buf);

	// make sure the returned str is the expected value
	EXPECT_STREQ("hello world", (char*)buf);

};

// the main function doesn't really have to anything but
int main(int argc, char **argv) {
        ::testing::InitGoogleTest(&argc, argv);

        printf("unit test for helloworld module.\n");

        return RUN_ALL_TESTS();
}

