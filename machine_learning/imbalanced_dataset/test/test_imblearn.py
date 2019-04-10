from sklearn.datasets import make_classification
from imblearn.pipeline import make_pipeline
from imblearn.over_sampling import SMOTE

from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline

n_samples = 1000

X, y = make_classification(	n_samples=n_samples,
				n_features=2,
				n_informative=2,
				n_redundant=0,
				n_repeated=0,
				n_classes=2,
				n_clusters_per_class=1,
				weights=[0.97, 0.03],
				flip_y=0.05,
				class_sep=1.8,
				random_state=2)

print ("X = {}".format(X))
# print ("y = {}".format(y))
print ("num points = {}, num of points in class 1 = {}".format(len(y), y.sum()))

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=7)

print ("len(X_train) = {}".format(len(X_train)))
print ("num of points in class 1 in training data = {}".format(y_train.sum()))

# Firstly try classification without over-sampling

clf1 = LinearSVC()
clf1.fit(X_train, y_train)

y_estimated = clf1.predict(X_test)

print ("\nResults from normal classification:")
print (classification_report(y_test, y_estimated))

# Then try classification with over-sampling
# Documentation for SMOTE: https://imbalanced-learn.readthedocs.io/en/stable/generated/imblearn.over_sampling.SMOTE.html#imblearn.over_sampling.SMOTE
clf = make_pipeline(SMOTE(), LinearSVC())

# unfortunately, it doesn't work with sklearn's native Pipeline;
# need to test if all sklearn's modules and self-customized modules work with imblearn.pipeline.Pipeline
# clf = Pipeline(steps=[
#	('oversampling', SMOTE()),
#	('classifier', LinearSVC()),
#])

clf.fit(X_train, y_train)

y_estimated = clf.predict(X_test)

print ("\nResults from classification after oversampling the training data:")
print (classification_report(y_test, y_estimated))
