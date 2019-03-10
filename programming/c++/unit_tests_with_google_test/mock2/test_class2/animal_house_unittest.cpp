// reference: https://github.com/google/googletest/blob/master/googlemock/docs/ForDummies.md

#include "mock_cat.h"
#include "animal_house.h"
#include "gtest/gtest.h"
#include "gmock/gmock.h"
#include <iostream>

using ::testing::AtLeast; // not using in this case
using ::testing::Return;

// use a simple test
TEST(AnimalHouseTest, getSummary) {
	Mock_Cat cat;
	double size = 101;
	std::string cat_name = "MockCat";
	// the get_name() function will be exactly call once
	EXPECT_CALL(cat, get_name())
		.Times(1)
		.WillRepeatedly(Return(cat_name)); // allows setting return value!

	Animal_House house(&cat, size);
	std::string summary = house.get_summary(); // in order to make get_name() called

	std::cout<< "The summary string returned is: " << summary << std::endl;

	// something else later
	std::string summary_expected = "MockCat lives in an animal house with a size of 101";

	// ASSERT_EQ can be used for comparing std::string
	// while ASSERT_STREQ is used for comparing c strings
	ASSERT_EQ(summary, summary_expected);
}

int main(int argc, char** argv) {
	::testing::InitGoogleMock(&argc, argv);
        ::testing::InitGoogleTest(&argc, argv);

	return RUN_ALL_TESTS();
}
