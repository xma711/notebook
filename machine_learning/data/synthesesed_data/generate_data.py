# to generate X (R2) and Y ( {+1, -1} ) based on a linear function y = w1 x1 + w2 x2 + b

import sys
import numpy as np
import random 
import matplotlib.pyplot as plt

random.seed(a=10) # make it deterministic so that it is repeatable

# note that don't key in "," in the arguments!
if ( len(sys.argv) < 5 ):
	print ("please input number data points wanted, w1, w2 and b.")
	exit(1)

print (sys.argv)

num = int(sys.argv[1])
num_test = num / 3

w1 = float(sys.argv[2])
w2 = float(sys.argv[3])
b = float(sys.argv[4])

print ("The true equation is: y = (" + str(w1) + ")*x1 + (" + str(w2) + ")*x2 + (" + str(b) + ")")

print ("number of data points that will be generated = " + str(num) )

data = np.zeros( (num, 3) )

def generate_data (num_wanted, data_ptr):
	num_positive = 0
	num_negative = 0
	for i in range(num_wanted):
		# from 0 to 10
		x1 = (random.random() - 0.5) * 100
		x2 = (random.random() - 0.5) * 100
		y = w1 * x1 + w2 * x2 + b
		y_label = 1
		if y < 0:
			y_label = -1
			num_negative += 1
		else:
			num_positive += 1
		data_ptr[i] = [y_label, x1, x2]
		print ( str(x1) + " " + str(x2) + " " + str(y) + " " + str(y_label))

	print ("number of positive examples = " + str(num_positive))
	print ("number of negative examples = " + str(num_negative))

generate_data(num, data)
# print (data)
print ("data.shape = " + str(data.shape))

data_test = np.zeros( (num_test, 3) )
generate_data(num_test, data_test)
print ("data_test.shape = " + str(data_test.shape))

# save to file
with open("data_synthesed_train.csv", "w") as f:
	np.savetxt(f, data, delimiter=',', fmt="%s")

# save to file
with open("data_synthesed_test.csv", "w") as f1:
	np.savetxt(f1, data_test, delimiter=',', fmt="%s")

# save ground truth to file
with open("equation.csv", "w") as f2:
	f2.write("The true equation is: y = (" + str(w1) + ")*x1 + (" + str(w2) + ")*x2 + (" + str(b) + ")\n");
	f2.write("w1 = " + str(w1))
	f2.write("w2 = " + str(w2))
	f2.write("b = " + str(b))

plt.title("Train data")
plt.subplot(321)
plt.scatter(data[:, 1], data[:, 2], marker='o', c=data[:, 0], s=25, edgecolor='k')

plt.subplot(322)
plt.title("Test data")
plt.scatter(data_test[:, 1], data_test[:, 2], marker='o', c=data_test[:, 0], s=25, edgecolor='k')

plt.show()
