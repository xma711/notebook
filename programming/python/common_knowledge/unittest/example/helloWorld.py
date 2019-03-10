#!/usr/bin/python3

### This example is to demo how to use Python Unittesting framework;
### Please check helloWorldUnittest.py for the unit tests.
### For more details, refer to: https://docs.python.org/2/library/unittest.html


# A hello world class, to be tested
class HelloWorld:
	# The first method is simply to return a hello world string
	def greeting(self):
		return "Hello world!"

	# The 2nd method is to return the length of the string returned by the 1st method;
	# This method depends on the 1st method; but in testing it is better to isolate its dependencies.
	def lengthGreeting(self):
		return len(self.greeting());




