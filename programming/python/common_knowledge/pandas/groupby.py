#!/home/xma/anaconda2/bin/python

import pandas as pd

# all of the elements become string if using numpy;
# in this case using simple list is better
b = [ ['cat1', 2, 3], ['cat2', 5, 6], ['cat1', 3, 3], ['cat2', 2, 2], ['cat1', 7, 8], ] 

print "b = {}".format(b)

bp = pd.DataFrame(b)
bp.columns = ['category', 'metric1', 'metric2']

# it is important to convert the strings to floats if numpy array is used for b
# bp['metric1'] = bp['metric1'].astype(float)
# bp['metric2'] = bp['metric2'].astype(float)

print "bp = {}".format(bp)

group_by_b1 = bp.groupby(['category'])

print "group_by_b1.get_group('cat1') = {}\n".format(group_by_b1.get_group('cat1'))

print "group_by_b1 = {}\n".format(group_by_b1)

print "group_by_b1.count() = {}\n".format(group_by_b1.count())
print "group_by_b1.sum() = {}\n".format(group_by_b1.sum())
print "group_by_b1.mean() = {}\n".format(group_by_b1.mean())
