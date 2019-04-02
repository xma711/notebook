### This unit test file shows how to test the HelloWorld class;
### There will be a few test cases to test the 2 methods in the class;
### Note that it is not uncommon to have more than 1 tests cases for one single method.
### Also note that each test case is independent; in fact they can be run individually.

### To run this test, use: python3 -m unittest helloWorldUnittest

import unittest
import helloWorld # this is the class for testing
from unittest.mock import MagicMock # this is useful for creating stub or mock functions

class TestHelloWorld(unittest.TestCase):
	# this function will run before EACH test case;
	def setUp(self):
		# create a new object for every test case
		self.hwObj = helloWorld.HelloWorld(); 

	# this function will run after EACH test case
	def tearDown(self):
		# remove the object after every test case
		self.hwObj = None; 

	# 1st test case: test the greeting method
	def testGreetMethod(self):
		strHello = self.hwObj.greeting() # run the method
		# test to make sure the returned string is what you expect
		self.assertEqual(strHello, "Hello world!") 

	# 2nd test case: test the lengthGreeting method
	def testLengthGreeting(self):
		lenHello = self.hwObj.lengthGreeting() # run the method
		self.assertEqual(lenHello, len("Hello world!")) 

	# 3rd test case: test the lengthGreeting method with a stub (recommended)
	def testLengthGreetingUsingStub(self):
		localStr = "The quick brown fox jumps over the lazy dog";

		# before executing the method for testing, create a stub for its dependency
		mockGreeting = MagicMock(return_value = localStr) # create a stub function
		self.hwObj.greeting = mockGreeting # replace the function by our stub function
		lenHello = self.hwObj.lengthGreeting() # run the method

		# in this way we can make sure the logic of the method itself is correct
		self.assertEqual(lenHello, len(localStr)) 

# don't have to create a main function
# just use the unittest's main function
if __name__=='__main__':
	unittest.main()
