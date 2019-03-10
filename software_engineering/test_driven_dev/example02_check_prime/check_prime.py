import math

# the main class
class CHECK_PRIME():
	def it_is_a_prime(self, num):

		# check if num has the right range and is a integer
		if ( num < 2 or type(num) != int ):
			raise InputError("Input number cannot be smaller than 2, and input number must be an integer.");

		# special case. 2 is a prime.
		if num == 2:
			return True;

		# definitly not a prime when it can be divided by 2 - half of the cases are handled
		if num % 2 == 0:
			return False

		num_sqrt = int( math.ceil( math.sqrt(num) ) )

		# as long as it can be divided by a number, it must not be a prime
		for element in range(3, num_sqrt+1):
			if num % element == 0:
				return False

		# at this point, it must be a prime number
		return True 

# exception to be raised/thrown
class InputError(Exception):
    """Exception raised for errors in the input.

    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = msg
