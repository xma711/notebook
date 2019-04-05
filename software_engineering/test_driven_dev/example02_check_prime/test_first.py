#!/usr/bin/python2.7

import unittest
import check_prime # going to have a check_primenacci module

# the check_prime module has a method to let user input a number n, 
# and then it will return a list of check_primenacci numbers starting from 1.
# the length of the list is n

# things to test:
# 1. when input number is less than 1, it will complain
# 2. when input number is n (1 or more), it will return a list of check_primenacci number with length n

# Run this test: python -m unittest test_first (cannot have ./ or .py)

class TestCheckPrime(unittest.TestCase):

	# 1st test case: test function
	def test_wrong_input(self):
		check_prime_obj = check_prime.CHECK_PRIME();

		with self.assertRaises(check_prime.InputError):
			num_err = 1;
			check_prime_obj.it_is_a_prime(num_err);

		with self.assertRaises(check_prime.InputError):
			num_err = 0;
			check_prime_obj.it_is_a_prime(num_err);

		with self.assertRaises(check_prime.InputError):
			num_err = -1;
			check_prime_obj.it_is_a_prime(num_err);

		# only integer is allowed
		with self.assertRaises(check_prime.InputError):
			num_err = 2.5;
			check_prime_obj.it_is_a_prime(num_err);

	# 2nd test case: test a method in a class
	def test_get_check_prime_list(self):
		check_prime_obj = check_prime.CHECK_PRIME();
		self.assertEqual(check_prime_obj.it_is_a_prime(2), True)
		self.assertEqual(check_prime_obj.it_is_a_prime(31), True)
		self.assertEqual(check_prime_obj.it_is_a_prime(7901), True)
		self.assertEqual(check_prime_obj.it_is_a_prime(4), False)
		self.assertEqual(check_prime_obj.it_is_a_prime(4653), False)
		self.assertEqual(check_prime_obj.it_is_a_prime(7719), False)

	

# don't have to create a main function
# just use the unittest's main function
if __name__=='__main__':
	unittest.main()
