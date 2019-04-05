#!/usr/bin/python2.7

import unittest
import fibo # going to have a fibonacci module

# the fibo module has a method to let user input a number n, 
# and then it will return a list of fibonacci numbers starting from 1.
# the length of the list is n

# things to test:
# 1. when the input number is less than 1, it will complain
# 2. when the input number is n (1 or more), it will return a list of fibonacci number with length n

# Run this test: python -m unittest test_first (cannot have ./ or .py)

class TestFibonacci(unittest.TestCase):

	# 1st test case: test function
	def test_wrong_input(self):
		fb = fibo.FIBO();

		with self.assertRaises(fibo.InputError):
			num_err = 0;
			fb.get_fibo_list(num_err);

	# 2nd test case: test a method in a class
	def test_get_fibo_list(self):
		fb = fibo.FIBO();
		num = 10;
		list_expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
		list_fibo = fb.get_fibo_list(num);
		self.assertEqual(len(list_fibo), num);
		i = 0;
		for num_fibo in list_fibo:
			self.assertEqual(list_fibo[i], list_expected[i])
			i += 1;
	

# don't have to create a main function
# just use the unittest's main function
if __name__=='__main__':
	unittest.main()
