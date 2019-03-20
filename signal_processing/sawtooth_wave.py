# run this with ~/anaconda2/bin/python

# this example is to show that an and bn are computed from the -pi to pi (period of 2pi),
# but the resultant fourier series can be applied to the whole -inf < x < inf.

import math
import sys


if len(sys.argv) < 2:
	raise Exception("please input the float number for the sawtooth wave function.")

input=float(sys.argv[1])
print "input is {}".format(input)

def compute_direct(x):
	if x > -1 * math.pi and x < math.pi:
		return x/math.pi

	if x > math.pi:
		n = int( (x - math.pi)/(2*math.pi) ) + 1
		x2 = x - n*2*math.pi
		return x2/math.pi

	if x < -1*math.pi:
		n = int( (x + math.pi)/(-2*math.pi) ) + 1
		x2 = x + n*2*math.pi
		return x2/math.pi

	return 0


def compute_thru_fourier(x):
	N = 1000
	sum = 0
	for i in range(1,N):
		# importantly, need to use float
		# the reason that there is no 2pi in the following function is that the period is 2pi too, so it cancel away mathematically
		comp = ( (-1.)**(i+1) ) / i * math.sin(i*x)
		sum += comp
#		if i < 100:
#			print "i={},comp={},sum={}".format(i, comp, sum)
	sum = sum*2/math.pi
	return sum


print "for function sawtooth wave, when x = {}, the direct result is {}, and the result from fourier series is {}".format(input, compute_direct(input), compute_thru_fourier(input))
