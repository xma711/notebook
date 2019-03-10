#!/usr/bin/python3

import unittest
import double_1_to_10


class TestDouble(unittest.TestCase):

	# 1st test case: test function
	def test_basic_function(self):
		num = 5;
		result = double_1_to_10.double_1_to_10(num);
		self.assertEqual(2 * num, result);

	# make sure it only accepts int
	def test_input_type(self):
		num = 5.5;
		failure = False;
		try:
			result = double_1_to_10.double_1_to_10(num);
			failure = False;
		except:
			failure = True;

		# expect failure to happen
		self.assertEqual(failure, True);
	
	# make sure lower bound is correct
	def test_lower_bound(self):
		num = 0;
		failure = False;
		try:
			result = double_1_to_10.double_1_to_10(num);
			failure = False;
		except:
			failure = True;

		# expect failure to happen
		self.assertEqual(failure, True);

	# make sure upper bound is correct
	def test_upper_bound(self):
		num = 11;
		failure = False;
		try:
			result = double_1_to_10.double_1_to_10(num);
			failure = False;
		except:
			failure = True;

		# expect failure to happen
		self.assertEqual(failure, True);

# don't have to create a main function
# just use the unittest's main function
if __name__=='__main__':
	unittest.main()
