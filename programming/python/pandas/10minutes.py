# run with python2 from anaconda

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Series seems a type that it will automatically have a default integer index
s = pd.Series( [ 1, 3, 5, np.nan, 6, 8 ] )
print "type(s) = {}".format(type(s))
print "series s = \n{}\n".format(s)
print "s[0] = \n{}\n".format(s[0])
print "s[0:2] = \n{}\n".format(s[0:2])

# dataframe seems more commonly used

# this dates has a type of "pandas.core.indexes.datetimes.DatetimeIndex".
# is this dataframe? No.. it is just index in time. (as the type implies)
dates = pd.date_range('20170101', periods=6)
print "type(dates) = {}".format(type(dates))
print "dates = \n{}\n".format(dates)

# now dataframe's turn
# see. dates becomes the index.. more meaningful than just 0,1,2,3..
np_data = np.random.randn(6,4)
df = pd.DataFrame(np_data, index=dates, columns=list('ABCD'))
print "type(df) = {}".format(type(df))
print "df = \n{}\n".format(df)

# let's see if we don't set the dates as index, what will happen?
# there will be index 0,1,2...
df__ = pd.DataFrame(np_data, columns = list('ABCD'))
print "df__ = \n{}\n".format(df__)

# we can also pass a dictionary into Dataframe()
# however, i think this is a bad idea..
# unless you understand exactly how dataframe will manipulate the dictionary, it can be hard to predict what dataframe will be created
dict1 = {
	'A': 1,
	'B': pd.Timestamp('20170101'),
	'C': pd.Series(1, index=list(range(4)), dtype='float32'),
	'D': np.array([3]*4, dtype='int32'),
	'E': pd.Categorical(['test', 'train', 'test', 'train']),
	'F': 'foo'
}

print "dict1 = \n{}\n".format(dict1)
df2 = pd.DataFrame(dict1)
print "df2 = \n{}\n".format(df2)

print "df2.dtypes = \n{}\n".format(df2.dtypes)

print "df.head() = \n{}\n".format(df.head())
print "df.tail(3) = \n{}\n".format(df.tail(3))

print "df.index = \n{}\n".format(df.index)
print "df.columns = \n{}\n".format(df.columns)
print "df.values = \n{}\n".format(df.values)
print "type(df.values) = {}".format(type(df.values))
