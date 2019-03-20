# run this script with ~/anaconda3/bin/python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# reference: http://pandas.pydata.org/pandas-docs/version/0.18.1/10min.html#min

# there is this "Series" variable type
s = pd.Series( [1, 2, 3, np.nan, 5] )
print ("An example pd.Series = \n", s)

# another (more commonly used) type is "DataFrame", which looks like a table;
# if index (row) and columns are not set, the defaults are 1,2,3,4 ...
df1 = pd.DataFrame( np.random.randn(6,4) ) # input is a 6x4 matrix
print ("The most direct generation of a dataframe results in:\n", df1);

# let's configure the index and columns
dates = pd.date_range('20161001', periods=6)
df = pd.DataFrame( np.random.randn(6,4), index=dates, columns=['A', 'B', 'C', 'D'] )
print ("After configure index and columns, the dataframe looks like:\n", df)

# btw, the input to the pd.DataFrame() can be a dictionary,
# with key as the column name, and values as an array or series of the same length;
# refer to the reference..

print ("To print the types of data for each column in a df, just use df.dtypes:\n", df.dtypes)

