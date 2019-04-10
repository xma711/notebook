# run this script with python2 or python3 from anaconda

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn import svm 
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
# from sklearn.tree import export_graphviz # for output tree image
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB 
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report

import time
import sys
import getopt
import os
import json

## global variables
classifier_chosen = None;

write_file = False

classifiers_supported_dict = {
	"vt": "voting with svm (5), rf (1), mlp (3)", 
	"svm": "svm", 
	"rf": "random forest", 
	"mlp": "multilayer perceptron",
	"lr": "logistic regression", 
	"nbg": "nb_gaussian", 
	"nbm": "nb_multinominal", 
	"nbb": "nb_bernoulli",
	"gb": "gradient_boosting_classifier",
	"xgb": "XGBClassifier",
}

classifiers_supported = classifiers_supported_dict.keys()

arguments_dict = {}
for c in classifiers_supported:
	arguments_dict[c] = {}

# default arguments
arguments_dict['rf'] = {
	'n_estimators': 128,
	'min_samples_split': 2,
	'min_samples_leaf': 1,
	'max_depth': None,
	'random_state': 1
}

arguments_dict['svm'] = {
	'gamma': 0.0252, # parameter for rbf
	'C': 10, # penalty for svm
	'cache_size': 500,
	'probability': True,
	'kernel': 'rbf', # other choices are: poly, linear, sigmoid and precomputed
}

arguments_dict['mlp'] = {
	'solver': 'adam', # {'lbfgs', 'sgd', 'adam'}
	'alpha': 1e-2,
	'random_state': 1,
	'max_iter': 2000,
	'hidden_layer_sizes': (200,100),
	'activation': 'logistic', # actvation: logistic, tanh, relu(default), identity
}

arguments_dict['lr'] = {
	'penalty': 'l2',
	'dual': False,
	'tol': 0.0001,
	'C': 1.0,
	'fit_intercept': True,
	'intercept_scaling': 1,
	'class_weight': None,
	'random_state': None,
	'solver': 'liblinear',
	'max_iter': 100,
	'multi_class': 'ovr',
	'verbose': 0,
	'warm_start': False,
	'n_jobs': 1,
}

arguments_dict['xgb'] = {
	'objective':"binary:logistic",
	'random_state': 42,
}


arg_inputs = []

# utility function
def print_with_time(msg):
	print ( time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) + ": " + msg);

def print_help():
	print ("The options include: ")
	print ("\t-h : print help")
	print ("\t-w : output results to file")
	print ("\t-c < classifier > : supported: " + json.dumps(classifiers_supported_dict, indent=12))
	print ("\t-a < general argument in the format of argumentName=value (auto interpreted) or argumentName=value=type; can be applied multiple times > : e.g. gamma=0.0252 or gamma=0.0252=float. The arguments apply to the chosen classifier")

############ use option to set parameters #################

# parse arguments	
argv=sys.argv[1:] # ignore the program name

try:
	opts, args = getopt.getopt(argv, "hwc:a:", [])

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
	elif opt in ("-w"):
		write_file = True
	elif opt in ("-a"):
		arg_inputs.append(arg)
	else:
		print ("No such option allowed. Please check the correct uages:")
		print_help()
		exit(1)

###########################################################

if classifier_chosen is None:
	print ("please choose a classifier.")
	print_help()
	exit(1)

if arg_inputs:
	for arg in arg_inputs:
		arg_info = arg.split('=')
		arg_name = arg_info[0]
		val = arg_info[1]
		if len(arg_info) >= 3:
			val_type = arg_info[2]
		else:
			val_type = 'auto'
		if val_type == 'auto' or val_type == 'float' or val_type == 'int' or val_type == 'bool' or val_type == 'none':
			val = eval(val)
		else:
			print ("Value type {} is not supported.".format(val_type))
			exit(1)
		
		arguments_dict[classifier_chosen][arg_name] = val

print ("classifier_chosen is : {} - {}".format(classifier_chosen, classifiers_supported_dict[classifier_chosen]) )
print ("classifier arguments are: {}".format(arguments_dict[classifier_chosen]))
print ("write to file: " + str(write_file))
print ("")

# create test dataset
n_samples = 10000

X, y = make_classification(	n_samples=n_samples,
				n_features=5,
				n_informative=2,
				n_redundant=1,
				n_repeated=0,
				n_classes=2,
				n_clusters_per_class=1,
				weights=[0.6, 0.4],
				flip_y=0.05,
				class_sep=1.8,
				random_state=2)

print ("X.shape = {}".format(X.shape))
print ("num data = {}, num of data in class 1 = {}".format(len(y), y.sum()))

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=7)
print ("num of training data = {}, num of training in class 1 = {}".format(len(y_test), y_test.sum()))

# for svm, a good combination of gamma and C can be determined by GridSearchCV
# example of GridSearchCV for svm; it can be very slow if there are too many choices; better do this offline
# parameters = {'gamma':[0.252,  0.256], 'C':[10, 13]}
# gs = GridSearchCV(svr, parameters) # auto get the best combinations

# the combined classifier
# the higher the accuracy of a classifier, the higher the weight it is assigned
if (classifier_chosen == 'vc'):
	classifier = VotingClassifier(estimators=[
			('rf', RandomForestClassifier( **arguments_dict['rf'] )),
			('mlp', MLPClassifier( **arguments_dict['mlp'] )),
			('sv', svm.SVC( **arguments_dict['svm'] ))], 
		voting='soft', n_jobs=2, weights=[1, 3, 5])
# svm
elif (classifier_chosen == 'svm'):
	classifier = svm.SVC( **arguments_dict[classifier_chosen] )
# MLPClassifier
elif (classifier_chosen == 'mlp'):
	classifier = MLPClassifier( **arguments_dict[classifier_chosen] )
### random forest
elif (classifier_chosen == 'rf'):
	classifier = RandomForestClassifier( **arguments_dict[classifier_chosen] ) 
### logistic regression
elif (classifier_chosen == 'lr'):
	classifier = LogisticRegression( **arguments_dict[classifier_chosen] )
# variants of naive bayes
elif (classifier_chosen == 'nbg'):
	classifier = GaussianNB( **arguments_dict[classifier_chosen] )
elif (classifier_chosen == 'nbm'):
	classifier = MultinomialNB( **arguments_dict[classifier_chosen] )
elif (classifier_chosen == 'nbb'):
	classifier = BernoulliNB( **arguments_dict[classifier_chosen] )
# gradient boosting classifier
elif (classifier_chosen == 'gb'):
	classifier = GradientBoostingClassifier( **arguments_dict[classifier_chosen] )
# xgboost
elif (classifier_chosen == 'xgb'):
	classifier = XGBClassifier( **arguments_dict[classifier_chosen] )

print ("classifer = " + str(classifier))

# training
print_with_time("start to fit the model...")
classifier.fit(X_train, y_train)
print_with_time("finish fitting the model.")

# get estimated results
print_with_time("predicting test data...")
y_estimated = classifier.predict(X_test) # for test data
print_with_time("predicting train data...")
results2 = classifier.predict(X_train) # for train data
print_with_time("finished the prediction.")

print (classification_report(y_test, y_estimated))

