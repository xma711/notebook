
# reference: https://danijar.com/variable-sequence-lengths-in-tensorflow/

# notes:
# for variable length, paddling seems needed.
# tf.nn.dynamic_rnn uses a tf.While loop to dynamically construct the graph when it is executed.
# static run should be creating an unrolled graph for a fixed RNN length.


# assume that the sequences are padded with 0 vectors to fill up the remaining time steps in the batch.
# compute the length of a sequence in the tensorflow graph
def length(sequence):
	# collapse the frame vectors (3rd dimension of a batch) into scalars using maximum;
	# each sequence is now a vector of scalars that will be 0 for the padded frames at the end;
	# use tf.sign() to convert the actual frames from their maximum values to values of one;
	# this gives us a binary mask of ones for used frames and 0s for unused frames that we can just sum to get the sequence length
	used = tf.sign(tf.reduce_max(tf.abs(sequence), 2))
	length = tf.reduce_sum(used, 1)
	length = tf.cast(length, tf.int32)
	return length


max_length = 100
frame_size = 64
num_hidden = 200

sequence = tf.placeholder(
	tf.float32,
	[None, max_length, frame_size]
)

# now that we have a vector holding the sequence lenghts, we can pass it to dynamic_rnn(),
# the function that unfolds our network, using the optional sequence_length parameter.
# when running the model later, tensorflow will return 0 vectors for states that outputs after these sequence lengths.
# therefore, weights will not affect those outputs and don't get trained on them.
output, state = tf.nn.dynamic_run(
	tf.contrib.rnn.GRUCell(num_hidden),
	sequence,
	dtype=tf.float32,
	sequence_length=length(sequence),
)

# output will still be of size batch_size x max_length x out_size, but with the last being zero vectors for sequences shorter than the maximum length.
# when you use the outputs at each time step, as in sequence labelling, we don't want to consider them in our cost function.
# we mask out the unused frames and compute the mean error over the sequence length by dividing by the actual length.
# using tf.reduce_mean() does not work here because it would divide by the maximum sequence length.

def cost(output, target):
	# compute cross entropy for each frame
	cross_entropy = target * tf.log(output)
	cross_entropy = -tf.reduce_sum(cross_entropy, 2)
	mask = tf.sign(tf.reduce_max(tf.abs(target), 2))
	cross_entropy *= mask

	# average over actual sequence lengths
	cross_entropy = tf.reduce_sum(cross_entropy, 1)
	cross_entropy /= tf.reduce_sum(mask, 1)
	return tf.reduce_mean(cross_entropy)

# we flatten the output tensor to shape (frames in all examples x output size).
# then we construct an index into that by creating a tensor with the start indices for each example tf.range(0, batch_size) * max_length
# and add the individual sequence lengths to it.
# tf.gather() then performs the actual indexing.
def last_relevant(output, length):
	batch_size = tf.shape(output)[0]
	max_length = tf.shape(output)[1]
	out_size = int(output.get_shape()[2])
	index = tf.range(0, batch_size) * max_length + (length - 1)
	flat = tf.reshape(output, [-1, out_size])
	relevant = tf.gather(flat, index)
	return relevant

# we got the last relevant output and can feed that into a simple softmax layer to predict the class of each sequence.
num_classes = 10
last = last_relevant(output)
weight = tf.Variable(
	tf.truncated_normal([num_hidden, num_classes], stddev=0.1)
)
bias = tf.Variable(tf.constant(0.1, shape=[num_classes]))
prediction = tf.nn.softmax(tf.matmul(last, weight) + bias)
