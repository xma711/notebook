#!/home/xma/anaconda2/bin/python

import dask.dataframe as dd

filename = 'test.csv'
df = dd.read_csv(filename)
sum_x = df.x.sum().compute()
print("sum_x = {}".format(sum_x))

# the feeling is that those panda-like actions are just 'actions yet to be carried out'.
# then the 'compute()' function will carry out these actions
print ("df.x.compute() = {}".format(df.x.compute()))
