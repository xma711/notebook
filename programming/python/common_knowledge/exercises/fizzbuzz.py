#!/usr/bin/python2

for i in range(100):
	num = i+1
	if (num % 3 == 0 and num % 5 == 0):
		# btw, a comma at the end avoids a newline being printed
		print "FizzBuzz",
	elif (num % 3 == 0):
		print "Fizz",
	elif (num % 5 == 0):
		print "Buzz",
	else:
		print num,
