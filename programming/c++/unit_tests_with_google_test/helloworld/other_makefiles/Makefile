#MAIN_DIR = ../../../..

BOARD = linux64

# GTEST_DIR is where the source codes for gtest is
# must use full path here!
GTEST_DIR = ${HOME}/github/knowledge/programming/c++/unit_tests_with_google_test/googletest/googletest

# the google_test folder is simply clone from github
# see https://github.com/google/googletest

# Where to find user code.
SRC_DIR = .
# QUEUE_DIR = $(MBIP_DIR)/data/src


# flags dependent on the CPU used
#ifeq "$(BOARD)" "linux32"
#LDFLAGS= -L$(MAIN_DIR)/libraries/networking/Mosquitto/arch/x86 -lmosquitto -lmosquittopp -lssl -lcrypto -lz
#CPPFLAGS += -I$(MBIP_SRC_DIR) -I$(MAIN_DIR)/libraries/networking/Mosquitto/arch/x86 -I$(MQTTCLIENT_DIR) -I$(QUEUE_DIR)  
#CXXFLAGS += -std=c++11 -D__maxPktSz=36 -DENCRYPTED_REGISTRATION -DDISABLE_MAIN_FOR_TESTING -DDEMUX_NOT_NEEDED
#endif

ifeq "$(BOARD)" "linux64"
LDFLAGS= -L$(SRC_DIR) # -lz ; use -L to point to where shared lib is, and -l to include the shared lib
CPPFLAGS += -I$(SRC_DIR) # point to where .h files are
CXXFLAGS += -std=c++11
endif

# Flags passed to the preprocessor.
# Set Google Test's header directory as a system directory, such that
# the compiler doesn't generate warnings in Google Test headers.
CPPFLAGS += -isystem $(GTEST_DIR)/include

# Flags passed to the C++ compiler.
CXXFLAGS += -g -Wall -Wextra -pthread

# All tests produced by this Makefile.  Remember to add new tests you
# created to the list.
TESTS = helloworld.test

# All Google Test headers.  Usually you shouldn't change this
# definition.
GTEST_HEADERS = $(GTEST_DIR)/include/gtest/*.h \
                $(GTEST_DIR)/include/gtest/internal/*.h


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

# Builds a test.  A test should link with either gtest.a or
# gtest_main.a, depending on whether it defines its own main()
# function.

helloworld.o : $(SRC_DIR)/helloworld.cpp $(SRC_DIR)/helloworld.h $(GTEST_HEADERS)
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c $(SRC_DIR)/helloworld.cpp -o $@

helloworld_unittest.o : $(SRC_DIR)/helloworld_unittest.cpp $(GTEST_HEADERS)
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c $(SRC_DIR)/helloworld_unittest.cpp -o $@

helloworld.test : helloworld.o helloworld_unittest.o gtest_main.a
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -lpthread $^ -o $@ $(LDFLAGS)
