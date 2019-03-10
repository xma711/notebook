# this example shows training on a 2d X vs Y;
# also shows how to plot some graphs

from sklearn import svm 
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import export_graphviz # for output tree image
from sklearn.linear_model import LogisticRegression

import numpy as np
import time
import sys
import getopt
import os

## global variables
# user can choose classifier: vc (voting), svm, rf (random forest), mlp (neural network), lr (logitstic regression)
classifier_chosen = None;

# other choices are: poly, linear, sigmoid and precomputed
kernel_svm = 'linear'; 

# parameter for rbf
gamma_svm = 0.0252

# penalty for svm
penalty_svm = 10

max_depth_rf = 3 
num_trees = 10

# utility function
def print_with_time(msg):
	print ( time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) + ": " + msg);

def print_help():
	print ("The options include: ")
	print ("\t-h : print help")
	print ("\t-w : output results to file")
	print ("\t-c < classifier > : supported: vt, svm, rf, mlp, lr")
	print ("\t-k < svm kernel > : supported: rbf, poly, linear, sigmoid and precomputed")
	print ("\t-g < svm gamma for rbf >")
	print ("\t-C < svm penalty value >")
	print ("\t-d < rf maximum depth >")
	print ("\t-t < num of trees for rf >")

############ use option to set parameters #################

# parse arguments	
argv=sys.argv[1:] # ignore the program name

try:
	opts, args = getopt.getopt(argv, "hc:k:g:C:d:t:", [])

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
		if (classifier_chosen != 'vc' and classifier_chosen != 'svm' and classifier_chosen != 'rf' and classifier_chosen != 'mlp' and classifier_chosen != 'lr'):
			print ("no such classifier: " + classifier_chosen)
			print ("the supported classifiers are vc, svm, rf and mlp")
			exit(1)
	elif opt in ("-k"):
		kernel_svm = arg
	elif opt in ("-g"):
		gamma_svm = float(arg)
	elif opt in ("-C"):
		penalty_svm = float(arg)
	elif opt in ("-d"):
		max_depth_rf = float(arg)
	elif opt in ("-t"):
		num_trees = int(arg)
	else:
		print ("No such option allowed. Please check the correct uages:")
		print_help()
		exit(1)

###########################################################

if not classifier_chosen:
	print ("you must choose one classifier.")
	print_help()
	exit(1)

print ("classifier_chosen is : " + classifier_chosen)
print ("")

data = np.genfromtxt("train.csv", delimiter=',', dtype=None)
print ("original train data shape: " + str(data.shape))

labels = data[:, 0]
print ("the length of labels = " + str(len(labels)))

training_data = data[:, 1:data.shape[1]] # include the position one-hot vector of the letter;
print ("training_data.shape: " + str(training_data.shape))

training_data = np.array(training_data, dtype = float)

testdata = np.genfromtxt("test.csv", delimiter=',', dtype=None)
test = testdata[:, 1:testdata.shape[1]]
print ("test data shape = " + str(test.shape))

test = np.array(test, dtype=float)


# create a svm classifier
sclf = svm.SVC(gamma=gamma_svm, C=penalty_svm, cache_size=500, probability=True, kernel=kernel_svm)  # a good combination of gamma and C can be determined by GridSearchCV

mlp = MLPClassifier(solver='adam', alpha=1e-2, random_state=1, max_iter=2000, hidden_layer_sizes=(200,100), activation='logistic') 
#{'lbfgs', 'sgd', 'adam'} alpha=1e-5; actvation: logistic, tanh, relu(default), identity

### random forest
# n_estimators is the number of trees in the forest
# max_depth is the maximum depth of a tree
forest = RandomForestClassifier( n_estimators=num_trees, min_samples_split=2, min_samples_leaf=1, max_depth=max_depth_rf, random_state=1) 

# the combined classifier
# the higher the accuracy of a classifier, the higher the weight it is assigned
vc = VotingClassifier(estimators=[('rf', forest), ('mlp', mlp), ('sv', sclf)], voting='soft', n_jobs=2, weights=[1, 3, 5])

### logistic regression
logistic_regression = LogisticRegression(penalty='l2', dual=False, 
tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver='liblinear', max_iter=100, multi_class='ovr', verbose=0, warm_start=False, n_jobs=1)

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
	print ("max_depth = " + str(max_depth_rf))
	print ("number of trees = " + str(num_trees))
elif (classifier_chosen == 'lr'):
	classifier = logistic_regression

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

test_truth = testdata[:, 0] # if the test data is not from train data, then this column is meaningless
train_truth = data[:, 0]

test_correct = 0
train_correct = 0

for i in range(len(train_truth)):
	if (results2[i] == train_truth[i]):
		train_correct = train_correct + 1 

for i in range(len(test_truth)):
	if (results[i] == test_truth[i]):
		test_correct = test_correct + 1 

print ("The prediction successful rate for train data = " + str( float(train_correct)/len(train_truth) ) )
print ("The prediction successful rate for test data (not meaningful if test data is not from the original train data) = " + str(float(test_correct)/len(test_truth) ) )
	
# print some weights
if (classifier_chosen == 'svm' and kernel_svm == "linear"):
	print ("coef = " + str(classifier.coef_))
	print ("intercept = " + str(classifier.intercept_))

if (classifier_chosen == 'lr'):
	print ("coef = " + str(classifier.coef_))
	print ("intercept = " + str(classifier.intercept_))
	print ("n_iter = " + str(classifier.n_iter_))
	results_proba = classifier.predict_proba(test)
	print ("the specific probabilities for different classes are:")
	for i in range(len(test)):
		print (str(test[i]) + "\t" + str(int(test_truth[i])) + ":\t" + str(int(results[i])) + "\t" + str(results_proba[i])  )

# plot some images
header_x=["x1", "x2"]
if (classifier_chosen == 'rf'):
	# plot the first tree
	# reference: https://stackoverflow.com/questions/40155128/plot-trees-for-a-random-forest-in-python-with-scikit-learn
	export_graphviz(classifier.estimators_[0],
		        feature_names=header_x,
		        filled=True,
		        rounded=True)
	
	# have to install graphviz: sudo apt-get install graphviz
	os.system('dot -Tpng tree.dot -o tree.png; rm tree.dot')
