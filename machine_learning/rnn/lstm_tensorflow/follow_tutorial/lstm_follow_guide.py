#!/home/xma/anaconda2/bin/python

# follow: https://towardsdatascience.com/lstm-by-example-using-tensorflow-feb0c1968537

# btw this one is supposed to be not working because i just type along when i read the tutorial

import collections

story = 'long ago , the mice had a general council to consider what measures they could take to outwit their common enemy , the cat . some said this , and some said that but at last a young mouse got up and said he had a proposal to make , which he thought would meet the case . you will all agree , said he , that our chief danger consists in the sly and treacherous manner in which the enemy approaches us . now , if we could receive some signal of her approach , we could easily escape from her . i venture , therefore , to propose that a small bell be procured , and attached by a ribbon round the neck of the cat . by this means we should always know when she was about , and could easily retire while she was in the neighbourhood . this proposal met with general applause , until an old mouse got up and said that is all very well , but who is to bell the cat ? the mice looked at one another and nobody spoke . then the old mouse said it is easy to propose impossible remedies .'

# the input to this function should be a list of words, not a long string.
# a long string can work but it becomes a list of letters
def build_dataset(words):
	count = collections.Counter(words).most_common()
	dictionary = dict()
	for word, _ in count:
		# word to number
		dictionary[word] = len(dictionary)
	reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
	return dictionary, reverse_dictionary

def RNN(x, weights, biases):
	# reshape to [1, n_input]. n_input should be the number of words in x
	x = tf.reshape(x, [-1, n_input])

	# generate a n_input-element sequence of inputs
	# (e.g. [had] [a] [general] -> [20] [6] [33])
	x = tf.split(x, n_input, 1)

	# 1-layer LSTM with n_hidden units
	rnn_cell = rnn.BasicsLSTMCell(n_hidden)

	# generate prediction
	outputs, states = rnn.static_rnn(rnn_cell, x, dtype=tf.float32)

	# there are n_input outputs but
	# we only want the last output
	return tf.matmul(outputs[-1], weights['out']) + biases['out']


# the trickiest part is feeding the input in the correct format and sequence.
# in this example, the LSTM feeds on a sequence of 3 integers (e.g. 1x3 vector of int)

vocab_size = len(dictionary)
n_input = 3

3 number of units in RNN cell
n_hidden = 512 # isn't this too many considering there is so few examples??

# RNN output node weights and biases
weights = {
	'out': tf.Variable(tf.random_normal([n_hidden, vocab_size]))
}
biases = {
	'out': tf.Variable(tf.random_normal([vocab_size]))
}

# need to generate the training_data first -- should be a list of words
symbols_in_keys = [ [ dictionary[ str(training_data[i]) ] ] for i in range( offset, offset + n_input )]

symbols_out_onehot = np.zeros([vocab_size], dtype=float)
symbols_out_onehot[dictionary[str(training_data[offset + n_input])]] = 1.0

_, acc, loss, onehot_pred = session.run(
	[optimizer, accuracy, cost, pred],
	feed_dict = {x: symbols_in_keys, y: symbols_out_onehot}
)

pred = RNN(x, weights, biases)

# loss and optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))

optimizer = tf.train.RMSPropOptimizer(learning_rate=learning_rate).minimize(cost)

rnn_cell = rnn.MultiRNNCell([rnn.BasicLSTMCell(n_hidden), rnn.BasicLSTMCell(n_hidden)])

