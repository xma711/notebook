BOARD = linux64


# GTEST_DIR is where the source codes for gtest is
GTEST_DIR = ${HOME}/github/knowledge/programming/c++/unit_tests_with_google_test/googletest/googletest
GMOCK_DIR = ${HOME}/github/knowledge/programming/c++/unit_tests_with_google_test/googletest/googlemock

# Where to find user code.
SRC_DIR = .
HELLOWORLD_DIR = $(SRC_DIR)/../helloworld


ifeq "$(BOARD)" "linux64"
LDFLAGS= -L$(SRC_DIR) 
CPPFLAGS += -I$(SRC_DIR) -I$(HELLOWORLD_DIR) -I$(HELLOWORLD_DIR)/googlemock
CXXFLAGS += -std=c++11
endif

# Flags passed to the preprocessor.
# Set Google Test's header directory as a system directory, such that
# the compiler doesn't generate warnings in Google Test headers.
CPPFLAGS += -isystem $(GTEST_DIR)/include \
	    -isystem $(GMOCK_DIR)/include

# Flags passed to the C++ compiler.
CXXFLAGS += -g -Wall -Wextra -pthread

# All tests produced by this Makefile.  Remember to add new tests you
# created to the list.
TESTS = count_num_char.test

# All Google Test headers.  Usually you shouldn't change this
# definition.
GTEST_HEADERS = $(GTEST_DIR)/include/gtest/*.h \
                $(GTEST_DIR)/include/gtest/internal/*.h

GMOCK_HEADERS = $(GMOCK_DIR)/include/gmock/*.h \
                $(GMOCK_DIR)/include/gmock/internal/*.h

# House-keeping build targets.

all : $(TESTS)

clean :
	rm -f $(TESTS) gtest.a gtest_main.a *.o

# Builds gtest.a and gtest_main.a.

# Usually you shouldn't tweak such internal variables, indicated by a
# trailing _.
GTEST_SRCS_ = $(GTEST_DIR)/src/*.cc $(GTEST_DIR)/src/*.h $(GTEST_HEADERS)

# For simplicity and to avoid depending on Google Test's
# implementation details, the dependencies specified below are
# conservative and not optimized.  This is fine as Google Test
# compiles fast and for ordinary users its source rarely changes.
gtest-all.o : $(GTEST_SRCS_)
	$(CXX) $(CPPFLAGS) -I$(GTEST_DIR) $(CXXFLAGS) -c \
            $(GTEST_DIR)/src/gtest-all.cc

gtest_main.o : $(GTEST_SRCS_)
	$(CXX) $(CPPFLAGS) -I$(GTEST_DIR) $(CXXFLAGS) -c \
            $(GTEST_DIR)/src/gtest_main.cc

gtest.a : gtest-all.o
	$(AR) $(ARFLAGS) $@ $^

gtest_main.a : gtest-all.o gtest_main.o
	$(AR) $(ARFLAGS) $@ $^

# gmock stuff
GMOCK_SRCS_ = $(GMOCK_DIR)/src/*.cc $(GMOCK_HEADERS)

gmock-all.o : $(GMOCK_SRCS_)
	$(CXX) $(CPPFLAGS) -I$(GMOCK_DIR) $(CXXFLAGS) -c \
            $(GMOCK_DIR)/src/gmock-all.cc

gmock_main.o : $(GMOCK_SRCS_)
	$(CXX) $(CPPFLAGS) -I$(GMOCK_DIR) $(CXXFLAGS) -c \
            $(GMOCK_DIR)/src/gmock_main.cc

gmock.a : gmock-all.o
	$(AR) $(ARFLAGS) $@ $^

gmock_main.a : gmock-all.o gmock_main.o
	$(AR) $(ARFLAGS) $@ $^

# Builds a test.  A test should link with either gtest.a or
# gtest_main.a, depending on whether it defines its own main()
# function.
#helloworld.o : $(HELLOWORLD_DIR)/helloworld.cpp $(GTEST_HEADERS) $(GMOCK_HEADERS)
#	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c $(HELLOWORLD_DIR)/helloworld.cpp -o $@

count_num_char.o : $(SRC_DIR)/count_num_char.cpp $(GTEST_HEADERS) $(GMOCK_HEADERS)
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c $(SRC_DIR)/count_num_char.cpp -o $@

count_num_char_unittest.o : $(SRC_DIR)/count_num_char_unittest.cpp $(HELLOWORLD_DIR)/helloworld_interface.h $(HELLOWORLD_DIR)/googlemock/mock_helloworld.h $(GTEST_HEADERS) $(GMOCK_HEADERS)
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c $(SRC_DIR)/count_num_char_unittest.cpp -o $@

count_num_char.test : count_num_char.o count_num_char_unittest.o gtest_main.a gmock_main.a
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -lpthread $^ -o $@ $(LDFLAGS)
