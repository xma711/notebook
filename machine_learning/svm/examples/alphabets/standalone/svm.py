from sklearn import svm

import numpy as np
import time
import sys

kernel_function = "rbf" # by default use rbf as kernel function
# other choices are: poly, linear, sigmoid and precomputed
if ( len(sys.argv) > 1 ):
	kernel_function = sys.argv[1]
print ("kernel_function is : " + kernel_function)

data = np.genfromtxt("train.csv", delimiter=',', dtype=None)
print ("original train data shape: " + str(data.shape))
data = data[1:data.shape[0], :] # remove header
print ("remove header, train data shape: " + str(data.shape))

labels = data[:, 1]
print ("the length of labels = " + str(len(labels)))

training_data = data[:, 3:data.shape[1]] # include the position one-hot vector of the letter;
print ("training_data.shape: " + str(training_data.shape))

training_data = np.array(training_data, dtype = float)

testdata = np.genfromtxt("test.csv", delimiter=',', dtype=None)
testdata = testdata[1:testdata.shape[0], :]
test = testdata[:, 3:testdata.shape[1]]
print ("test data shape = " + str(test.shape))

test = np.array(test, dtype=float)

sclf = svm.SVC(gamma = 0.0252, C=10, cache_size = 500, probability = True, kernel = kernel_function)
# Question: what exactly is C? which parameter in the svm formula does C refer to?

classifier = sclf

print (time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print ("start to fit the model...")
print ( classifier.fit(training_data, labels) )
print (time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print ("finished fitting the model")

print (time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print ("start to predict both test and training data...")
results_test = classifier.predict(test)
results_train = classifier.predict(training_data)
print (time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print ("finished predicting the data")

test_ids = testdata[:, 0]
train_ids = data[:, 0]
test_truth = testdata[:, 1]
train_truth = data[:,1]

#f2 = open("results.csv", "w")
#f2.write("Id,Prediction\n")

test_correct = 0
train_correct = 0

for i in range(len(train_ids)):
	if (results_train[i] == train_truth[i]):
		train_correct = train_correct + 1

for i in range(len(test_ids)):
	if (results_test[i] == test_truth[i]):
		test_correct = test_correct + 1

print ("The prediction successful rate for train data = " + str(float(train_correct)/len(train_ids)))

print ("The prediction successful rate for test data = " + str( float(test_correct)/len(test_ids) ))

# write estimated results for training data
#for i in range(len(train_ids)):
#	f2.write( str(train_ids[i], 'utf-8') + "," + str(results_train[i], 'utf-8') + "\n" )

# write estimated results for test data
#for i in range(len(test_ids)):
#	f2.write( str(test_ids[i], 'utf-8') + "," + str(results_test[i], 'utf-8') + "\n" )
