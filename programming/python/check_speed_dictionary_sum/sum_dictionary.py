from datetime import datetime
import pandas as pd

n = 100000
print ("there are {} items.".format(n))

d1 = {}

for i in range(n):
	d1[i] = i

df = pd.DataFrame([ [x, d1[x]] for x in d1.keys()])
df.columns = ['id', 'count']
print ("df.shape = {}".format(df.shape))
# print ("df.head = {}".format(df.head))

t1 = datetime.now()
print ("{}: start adding 2 dictionary by using set".format(t1))

def whatever(grid_coords):
	return grid_coords[0]

df['new_id'] = df[['id', 'count']].apply(lambda grid_coords: whatever( grid_coords ), axis=1)
# print ("after adding new id, df.head = {}".format(df.head))

d2 = df.set_index('id')['count'].to_dict()

d3 = { k: d1.get(k, 0) + d2.get(k, 0) for k in set(d1) | set(d2) }

t2 = datetime.now() 
print ("{}: end adding 2 dictionary by using set".format(t2))
print ("the time taken is {}".format(t2-t1))


t1 = datetime.now()
print ("{}: start adding 2 dictionary one by one".format(t1))

for i in range(df.shape[0]):
	row = df.iloc[i]
	k = row['id']
	value = row['count']
	if k in d2:
		d2[k] += value
	else:
		d2[k] = value

t2 = datetime.now() 
print ("{}: end adding 2 dictionary one by one".format(t2))
print ("the time taken is {}".format(t2-t1))
