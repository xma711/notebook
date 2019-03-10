import numpy as np

# this preprocess program is to convert the position int to a one-hot vector;
# and then outputs a new file to contain the modified dataset

# read data from file
data = np.genfromtxt("train_very_ori.csv", delimiter=',', dtype=None)
print ("original input data shape: ", str(data.shape))
header = data[0, :] # keep the header
data = data[1:data.shape[0], :] # remove header
print ("remove header, input data shape: ", str(data.shape))

# get the position vector
position_vector = data[:, 3].astype(np.int)
len_rows = len(position_vector)
print ("position_vector.shape = ", position_vector.shape)

# get the maximum number, which determines the length of the one-hot vector
max_position = np.max(position_vector)
print ("max_position = ", max_position)

# create an empty 2d arrays to store the array of one-hot vectors
position_one_hot_arr = np.zeros( (len_rows, max_position) )
print ("position_one_hot_arr.shape = ", position_one_hot_arr.shape)

# transform the position_vector to an array of one-hot vectors!
# in this case, the one-hot vector length is 14.
# we need to minus 1 from position_vector because element 0 in the one-hot vector to be 1 if position = 1, and so on
position_one_hot_arr[np.arange(len_rows), position_vector - 1] = 1
print ("check the first 10 elements")
print (position_vector[0:10])
print (position_one_hot_arr[0:10, :])

data_modified = np.concatenate([data[:, 0:3], position_one_hot_arr, data[:, 4:]], 1) # concatenate horizontally
print ("data_modified.shape = ", data_modified.shape)
print ("first row in data:")
print (data[0])
print ("first row in data_modified:")
print (data_modified[0])
assert (data_modified.shape[0] == len_rows)
assert (data_modified.shape[1] == len(data[0, :]) - 1 + max_position)

position_header = []
for i in range(max_position):
	position_header.append("pos_elem_" + str(i+1))
print (position_header)
print (position_header)
new_header = []
new_header.extend(header[0:3])
new_header.extend(position_header)
new_header.extend(header[4:])
print (new_header)
assert (len(new_header) == data_modified.shape[1])

# make new_header to 1 x len 2d array
new_header = np.array(new_header).reshape((1, len(new_header)))
data_modified = np.concatenate([new_header, data_modified])
print ("data_modified.shape = ", data_modified.shape)
assert (data_modified.shape[0] == len_rows+1)
assert (data_modified.shape[1] == len(data[0, :]) - 1 + max_position)

# need to save the array as strings in file
with open("train_preprocessed.csv", "w") as f:
	np.savetxt(f, data_modified, delimiter=',', fmt="%s")
