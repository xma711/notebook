#!/usr/bin/python2.7

import unittest
import hello_world


class TestStringMethods(unittest.TestCase):

	# 1st test case: test function
	def test_hello_world(self):
		str1 = hello_world.hello_world()
		print "Test 1: string returned from function = \'%s\'" % (str1)
		self.assertEqual(str1, 'hello world')

	# 2nd test case: test a method in a class
	def test_hello_world_class(self):
		hello_world_object = hello_world.hello_world_class()
		str1 = hello_world_object.hello_world()
		print "\nTest 2: string returned from a method in a class = \'%s\'" % (str1)
		self.assertEqual(str1, 'hello world')

	

# don't have to create a main function
# just use the unittest's main function
if __name__=='__main__':
	unittest.main()
