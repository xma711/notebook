from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
import pandas as pd
from sklearn.svm import SVC
import numpy as np

class Remove_columns(BaseEstimator, TransformerMixin):
	def __init__(self, n_col_to_rm = 2):
		self.n_col_to_rm = n_col_to_rm
	def fit(self, X, y):
		s = X.sum().sort_values(ascending=True, inplace=False)
		print ("in fit(), s = {}".format(s))
		asc_important_cols = s.index
		print ("in fit(), asc_important_cols = {}".format(asc_important_cols))
		self.cols_remained = asc_important_cols[self.n_col_to_rm : len(asc_important_cols)]
		print ("in fit(), self.cols_remained = {}".format(self.cols_remained))
		return self

	def transform(self, x):
		print ("in transform(), self.cols_remained = {}".format(self.cols_remained))
		print ("x = {}".format(x))
		x_new = x[self.cols_remained]
		print ("x_new = {}".format(x_new))
		return x_new

m = Pipeline([
	('remove_columns', Remove_columns()),
	('classifier', SVC(kernel='linear'))
])


n = 25

d1 = np.array([
	range(0, n),
	range(n, 2*n),
	range(2*n, 3*n),
	range(3*n, 4*n)
])
print ("d1.shape = {}".format(d1.shape))

d1 = np.transpose(d1)
print ("d1.shape = {}".format(d1.shape))

X = pd.DataFrame(d1)

print ("X =\n{}".format(X))

y = pd.DataFrame( [ 'cat' if x%2 ==0 else 'dog' for x in range(n) ] )
print ("y =\n{}".format(y))

m.fit(X, y)

print ("finished fitting. \n\nstart to do prediction.")
X2 = pd.DataFrame(
	np.transpose(
		[[100,200,300],
        	[40,50,60],
        	[7,8,9],
		[10,11,12]]
	)
)

print ("X2 =\n{}".format(X2))

y_p = m.predict(X2)
print ("y predicted =\n{}".format(y_p))
