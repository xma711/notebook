
# Show how to pass the onehot encoding from training data to test data

# Reference: http://fastml.com/how-to-use-pd-dot-get-dummies-with-the-test-set/

import pandas as pd

car1 = 'car1'
car2 = 'car2'
car3 = 'car3'
car4 = 'car4'
car5 = 'car5'

data = [
	[car1, 2],
	[car2, 1],
	[car3, 5],
	[car4, 7],
	[car2, 3],
	[car4, 1]
]

df = pd.DataFrame(data)
df.columns = [ 'type', 'num']
print ("\ndf =\n{}".format(df))

# save this object_cols for df_test
object_cols = [x for x in list(df.select_dtypes(include=['object']).columns)]
print ("\nobject_cols = {}".format(object_cols))

df = pd.get_dummies(df, columns=object_cols)

print ("\nafter onehot encoding, df =\n{}".format(df))

# save the full column for df_test
df_columns = df.columns
print ("\ndf_columns = {}".format(df_columns))

data_test = [
	[car1, 2],
	[car2, 1],
	[car2, 3],
	[car1, 1],
	[car5, 2]
]

df_test = pd.DataFrame(data_test)
df_test.columns = [ 'type', 'num']
print("\ndf_test =\n{}".format(df_test))

df_test = pd.get_dummies(df_test, columns=object_cols)
print("\nafter onehot encoding, df_test =\n{}".format(df_test))

# add missing columns
missing_cols = set( df_columns ) - set( df_test.columns )
for c in missing_cols:
	df_test[c] = 0

print("\nafter adding missing columns, df_test =\n{}".format(df_test))

# also need to remove extra columns
extra_cols = set( df_test.columns ) - set( df_columns )
if extra_cols:
	print "extra columns:", extra_cols

df_test = df_test[ df_columns ]
print("\nafter removing extra columns, df_test =\n{}".format(df_test))
