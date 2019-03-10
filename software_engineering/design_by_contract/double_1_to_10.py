#!/usr/bin/python3

import sys

# must be an integer
def double_1_to_10 (num):
	if not type(num) is int:
		sys.stderr.write("num input must be an integer. %s is not an integer.\n" % str(num));
		exit(1);

	if num < 1 or num > 10:
		sys.stderr.write('The number (%d) cannot be smaller than 1 or more than 10.\n' % num);
		exit(1);

	return num*2;


# define main function
# so that this file can be used as a lib too
def main():	
	num = 5;
	print("doubling num %d = %d" % ( num, double_1_to_10(num) ));
	exit(0);

if __name__ == "__main__":
	main();
