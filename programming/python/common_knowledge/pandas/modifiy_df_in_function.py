#!/home/xma/anaconda2/bin/python

import pandas as pd
import numpy as np

def add_column(df):
	df['new_col'] = 999

a = np.array([[1,2,3],[4,5,6]])
print "a =\n{}".format(a)
df = pd.DataFrame(a)
print "df =\n{}".format(df)

add_column(df)
print "df =\n{}".format(df)

# conclusion is that no need for the function to return the df.
# once the df is modified in a function, the original df is modified.
# this means that df is like a pointer in C or C++.
