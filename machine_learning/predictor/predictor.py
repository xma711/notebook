# this is the updated version on 02 Oct 2017

# run this using: python3 filename  (python3 can be installed by anaconda)
# to use a particular classifier, use: python3 filename vc/svm/rf/mlp

from sklearn import svm 
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
# from sklearn.tree import export_graphviz # for output tree image
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB 
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB

import numpy as np
import time
import sys
import getopt
import os
import json

## global variables
# user can choose classifier: vc (voting), svm, rf (random forest), mlp (neural network)
classifier_chosen = 'vc';

# other choices are: poly, linear, sigmoid and precomputed
kernel_svm = 'rbf'; 

# parameter for rbf
gamma_svm = 0.0252

# penalty for svm
penalty_svm = 10

write_file = False

classifiers_supported_dict = {
	"vt": "voting with svm (5), rf (1), mlp (3)", 
	"svm": "svm", 
	"rf": "random forest", 
	"mlp": "multilayer perceptron",
	"lr": "logistic regression", 
	"nbg": "nb_gaussian", 
	"nbm": "nb_multinominal", 
	"nbb": "nb_bernoulli"
}

classifiers_supported = classifiers_supported_dict.keys()

# utility function
def print_with_time(msg):
	print ( time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) + ": " + msg);

def print_help():
	print ("The options include: ")
	print ("\t-h : print help")
	print ("\t-w : output results to file")
	print ("\t-c < classifier > : supported: " + json.dumps(classifiers_supported_dict, indent=12))
	print ("\t-k < svm kernel > : supported: rbf, poly, linear, sigmoid and precomputed")
	print ("\t-g < svm gamma for rbf >")
	print ("\t-C < svm penalty value >")

############ use option to set parameters #################

# parse arguments	
argv=sys.argv[1:] # ignore the program name

try:
	opts, args = getopt.getopt(argv, "hwc:k:g:C:n:", [])

except getopt.GetoptError:
	print ("Error: the format or the input of options is wrong")
	print_help()	
	sys.exit(2)

if args:
	print ("unknown arguments are detected: " + str(args) + ".\nplease check correct usage: ")
	print_help()
	exit(1)

for opt, arg in opts:	
	if opt == '-h':
		print_help()
		sys.exit()
	elif opt in ("-c"):
		classifier_chosen = arg
		# choose the classifier
		if (not classifier_chosen in classifiers_supported):
			print ("no such classifier: " + classifier_chosen)
			print_help()
			exit(1)
	elif opt in ("-k"):
		kernel_svm = arg
	elif opt in ("-g"):
		gamma_svm = float(arg)
	elif opt in ("-C"):
		penalty_svm = float(arg)
	elif opt in ("-w"):
		write_file = True
	else:
		print ("No such option allowed. Please check the correct uages:")
		print_help()
		exit(1)

###########################################################

print ("classifier_chosen is : " + classifier_chosen)
print ("write to file: " + str(write_file))
print ("")

# read data
data = np.genfromtxt("train.csv", delimiter=',', dtype=None)
print ("original input data shape: " + str(data.shape) )

# keep the header
header = data[0, :]
header_x = header[3:]

data = data[1:data.shape[0] , :] # remove the header
print ("remove header. input data shape: " + str(data.shape) )

labels = data[: , 1]
print ("the length of labels = " + str(len(labels)) )

training_data = data[:, 3:data.shape[1]]; # include the position of the letter in a word
print ("training_data.shape: " + str(training_data.shape) );
assert (len(header_x) == training_data.shape[1])

training_data = np.array(training_data, dtype=float)

# get test data
testdata = np.genfromtxt("test.csv", delimiter=',', dtype=None)
print ("original input test data shape: " + str(testdata.shape) )
testdata = testdata[1:testdata.shape[0] , :] # remove the header
print ("remove header. input test data shape: " + str(testdata.shape) )
test = testdata[:, 3:testdata.shape[1]]
print ("test data .shape: " + str(test.shape) )

test = np.array(test, dtype=float)

# create a svm classifier
sclf = svm.SVC(gamma=gamma_svm, C=penalty_svm, cache_size=500, probability=True, kernel=kernel_svm)  # a good combination of gamma and C can be determined by GridSearchCV

## example of GridSearchCV for svm; it can be very slow if there are too many choices; better do this offline
## parameters = {'gamma':[0.252,  0.256], 'C':[10, 13]}
## svr = svm.SVC(cache_size=500)
## gs = GridSearchCV(svr, parameters) # auto get the best combinations

mlp = MLPClassifier(solver='adam', alpha=1e-2, random_state=1, max_iter=2000, hidden_layer_sizes=(200,100), activation='logistic') 
#{'lbfgs', 'sgd', 'adam'} alpha=1e-5; actvation: logistic, tanh, relu(default), identity

### random forest
forest = RandomForestClassifier( n_estimators=128, min_samples_split=2, min_samples_leaf=1, max_depth=None, random_state=1 ) 

# the combined classifier
# the higher the accuracy of a classifier, the higher the weight it is assigned
vc = VotingClassifier(estimators=[('rf', forest), ('mlp', mlp), ('sv', sclf)], voting='soft', n_jobs=2, weights=[1, 3, 5])

### logistic regression
logistic_regression = LogisticRegression(penalty='l2', dual=False, 
tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver='liblinear', max_iter=100, multi_class='ovr', verbose=0, warm_start=False, n_jobs=1)

# variants of naive bayes
nb_gaussian = GaussianNB()
nb_multinominal = MultinomialNB()
nb_bernoulli = BernoulliNB()

# choose the classifier
if (classifier_chosen == 'vc'):
	classifier = vc
elif (classifier_chosen == 'svm'):
	classifier = sclf
	print ("kernel function = " + str(kernel_svm))
	print ("gamma = " + str(gamma_svm))
	print ("penalty = " + str(penalty_svm))
elif (classifier_chosen == 'mlp'):
	classifier = mlp
elif (classifier_chosen == 'rf'):
	classifier = forest
elif (classifier_chosen == 'lr'):
	classifier = logistic_regression
elif (classifier_chosen == 'nbg'):
	classifier = nb_gaussian
elif (classifier_chosen == 'nbm'):
	classifier = nb_multinominal
elif (classifier_chosen == 'nbb'):
	classifier = nb_bernoulli

print ("classifer = " + str(classifier))

# training
print_with_time("start to fit the model...")
classifier.fit(training_data, labels)
print_with_time("finish fitting the model.")

# get estimated results
print_with_time("predicting test data...")
results = classifier.predict(test) # for test data
print_with_time("predicting train data...")
results2 = classifier.predict(training_data) # for train data
print_with_time("finished the prediction.")

test_ids = testdata[: , 0]
train_ids = data[: , 0]
test_truth = testdata[:, 1] # if the test data is not from train data, then this column is meaningless
train_truth = data[:, 1]

test_correct = 0
train_correct = 0

for i in range(len(train_ids)):
	if (results2[i] == train_truth[i]):
		train_correct = train_correct + 1 

for i in range(len(test_ids)):
	if (results[i] == test_truth[i]):
		test_correct = test_correct + 1 

print ("The prediction successful rate for train data = " + str( float(train_correct)/len(train_ids) ) )
# the successful rate on test data is not meaningful if test data is not from the original train data
print ("The prediction successful rate for test data  = " + str(float(test_correct)/len(test_ids) ) )

# write to file if so configured
if write_file == True:
	f2 = open("results.csv", "w")
	f2.write("Id,Prediction\n")

	# write estimated results for training data
	for i in range(len(train_ids)):
		f2.write( str(train_ids[i], 'utf-8') + "," + str(results2[i], 'utf-8') + "\n")

	# write estimated results for test data
	for i in range(len(test_ids)):
		f2.write( str(test_ids[i], 'utf-8') + "," + str(results[i], 'utf-8') + "\n")
	
if classifier_chosen == 'nbg':
	print "parameters obtained are: \nmean: {}\nvariance: {}".format(classifier.theta_, classifier.sigma_)
	print "classifier.theta_.shape = {}, classifier.sigma_.shape={}".format(classifier.theta_.shape, classifier.sigma_.shape)

# plot some images
# # (this works but the dimension is too large to be meaningful in viewing)
# if (classifier_chosen == 'rf'):
	# plot the first tree
	# reference: https://stackoverflow.com/questions/40155128/plot-trees-for-a-random-forest-in-python-with-scikit-learn
#	export_graphviz(classifier.estimators_[0],
#		        feature_names=header_x,
#		        filled=True,
#		        rounded=True)
	
#	# have to install graphviz: sudo apt-get install graphviz
#	os.system('dot -Tpng tree.dot -o tree.png')
