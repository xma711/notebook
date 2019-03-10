import tensorflow as tf

num_units = 200
num_layers = 3
dropout = tf.placeholder(tf.float32)

# create the architecture
cells = []

for _ in range(num_layers):
	cell = tf.contrib.rnn.GRUCell(num_units) # or LSTMCell(num_units)
	cell = tf.contrib.rnn.DropoutWrapper(
		cell, output_keep_prob = 1.0 - dropout)
	cells.append(cell)

cell = tf.contrib.rnn.MultiRNNCell(cells)

# batch size x time steps x features
data = tf.placeholder(tf.float32, [None, None, 28])
output, state = tf.nn.dynamic_rnn(cell, data, dtype=tf.float32)


# sequence classification
output, _ = tf.nn.dynamic_rnn(cell, data, dtype=tf.float32) # how come repeated?
output = tf.transpose(output, [1, 0, 2]) # what is the meaning of 2nd argument?
last = tf.gather(output, int(output.get_shape()[0]) - 1)

# add a softmax classifier
out_size = target.get_shape()[2].value
logit = tf.contrib.layers.fully_connected(
	last, out_size, activation_fn=None)
prediction = tf.nn.softmax(logit)
loss = tf.losses.softmax_cross_entropy(target, logit)

# sequence labelling
out_size = target.get_shape()[2].value
logit = tf.contrib.layers.fully_connected(
	output, out_size, activation_fn = None)
prediction = tf.nn.softmax(logit)

flat_target = tf.reshape(target, [-1] + target.shape.as_list()[2:])
flat_logit = tf.reshape(logit, [-1] + logit.shape.as_list()[2:])
loss = tf.losses.softmax_cross_entropy(flat_target, flat_logit)
loss = tf.reduce_mean(loss)
