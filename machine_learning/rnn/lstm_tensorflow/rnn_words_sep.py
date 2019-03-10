'''
A Recurrent Neural Network (LSTM) implementation example using TensorFlow..
Next word prediction after n_input words learned from text file.
A story is automatically generated if the predicted word is fed back as input.

Author: Rowel Atienza
Project: https://github.com/roatienza/Deep-Learning-Experiments
'''

from __future__ import print_function

import numpy as np
import tensorflow as tf
from tensorflow.contrib import rnn
import random
import collections
import time
from lstm_rnn import LSTM_RNN

start_time = time.time()
def elapsed(sec):
	if sec<60:
		return str(sec) + " sec"
	elif sec<(60*60):
		return str(sec/60) + " min"
	else:
		return str(sec/(60*60)) + " hr"


# Target log path
logs_path = '/tmp/tensorflow/rnn_words'
writer = tf.summary.FileWriter(logs_path)

# Text file containing words for training
training_file = 'belling_the_cat.txt'

def read_data(fname):
	with open(fname) as f:
		content = f.readlines()
	content = [x.strip() for x in content]
	content = [content[i].split() for i in range(len(content))]
	content = np.array(content)
	content = np.reshape(content, [-1, ])
	return content

training_data = read_data(training_file)
print("Loaded training data...")

def build_dataset(words):
	count = collections.Counter(words).most_common()
	dictionary = dict()
	for word, _ in count:
		dictionary[word] = len(dictionary)
	reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
	return dictionary, reverse_dictionary

dictionary, reverse_dictionary = build_dataset(training_data)
vocab_size = len(dictionary)

# Parameters
learning_rate = 0.001
training_iters = 3000 #5000 # 50000
display_step = 1000
n_input = 3

# number of units in RNN cell
n_hidden = 512

# tf Graph input
# x = tf.placeholder("float", [None, n_input, 1]) # each xi is a n_input x 1 matrix. why is it not a n_input x vocab_size matrix?
# x = tf.placeholder("float", [None, n_input, vocab_size])
x = tf.placeholder("float", [None, None, vocab_size])
y = tf.placeholder("float", [None, vocab_size]) # each yi is a vocab_size vector
n_input_tf = tf.placeholder("int32", shape=()) # a scalar to be updated

RNN = LSTM_RNN(n_hidden, vocab_size, learning_rate)
pred, cost, optimizer = RNN.build_rnn_graph(x, n_input, y)
#pred, cost, optimizer = RNN.build_rnn_graph(x, y)

# Model evaluation
correct_pred = tf.equal(tf.argmax(pred,1), tf.argmax(y,1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# Initializing the variables
init = tf.global_variables_initializer()

def index_to_onehot_vector(s):
	s_onehot = np.zeros([vocab_size], dtype=float)
	s_onehot[s] = 1.0
	return s_onehot

# set to reuse variables
tf.get_variable_scope().reuse_variables()

# Launch the graph
with tf.Session() as session:
	session.run(init)
	step = 0
	offset = random.randint(0,n_input+1)
	end_offset = n_input + 1
	acc_total = 0
	loss_total = 0

	writer.add_graph(session.graph)

	while step < training_iters:
		# Generate a minibatch. Add some randomness on selection process.
		if offset > (len(training_data)-end_offset):
			offset = random.randint(0, n_input+1)

		symbols_in_keys = [ [dictionary[ str(training_data[i])]] for i in range(offset, offset+n_input) ]
		symbols_in_keys_onehot = [ index_to_onehot_vector(s) for s in symbols_in_keys]

		# this shape is to match the x placeholder
		# symbols_in_keys = np.reshape(np.array(symbols_in_keys), [-1, n_input, 1])
		symbols_in_keys = np.reshape(np.array(symbols_in_keys_onehot), [-1, n_input, vocab_size])

		symbols_out_onehot = index_to_onehot_vector(dictionary[str(training_data[offset+n_input])])
		symbols_out_onehot = np.reshape(symbols_out_onehot,[1,-1])

		_, acc, loss, onehot_pred = session.run([optimizer, accuracy, cost, pred], \
												feed_dict={x: symbols_in_keys, y: symbols_out_onehot})
		loss_total += loss
		acc_total += acc

		if (step+1) % display_step == 0:
			print("Iter= " + str(step+1) + ", Average Loss= " + \
				  "{:.6f}".format(loss_total/display_step) + ", Average Accuracy= " + \
				  "{:.2f}%".format(100*acc_total/display_step))
			acc_total = 0
			loss_total = 0
			symbols_in = [training_data[i] for i in range(offset, offset + n_input)]
			symbols_out = training_data[offset + n_input]
			symbols_out_pred = reverse_dictionary[int(tf.argmax(onehot_pred, 1).eval())]
			print("%s - [%s] vs [%s]" % (symbols_in,symbols_out,symbols_out_pred))
		step += 1
		offset += (n_input+1)

	print("Optimization Finished!")
	print("Elapsed time: ", elapsed(time.time() - start_time))
	print("Run on command line.")
	print("\ttensorboard --logdir=%s" % (logs_path))
	print("Point your web browser to: http://localhost:6006/")

	while True:
		prompt = "%s words (need to have \" before and after the words): " % (n_input)
		try:
			sentence = input(prompt)
			sentence = sentence.strip()
			words = sentence.split(' ')
		except Exception as e:
			print ("exception: {}".format(e))
			print ("need to put \" before and after the 3 words")
			continue
		if len(words) != n_input:
			continue
		try:
			symbols_in_keys = [dictionary[str(words[i])] for i in range(len(words))]
			symbols_in_keys_onehot = [ index_to_onehot_vector(s) for s in symbols_in_keys ]

			# current limitation: have to use fixed length!!
			for i in range(64):
				# keys = np.reshape(np.array(symbols_in_keys), [-1, n_input, 1])
				n_input_new = len(symbols_in_keys_onehot)
				# print ("len(symbols_in_keys_onehot) = {}".format(n_input_new))
				# -1 in np.reshape means: let np to infer the dimension
				keys = np.reshape(np.array(symbols_in_keys_onehot), [-1, n_input_new, vocab_size])
				# print ("keys.shape = {}".format(keys.shape))
				# need to re-obtain the follows because need to recreate the graph due to static n_input..
#				pred, cost, optimizer = RNN.build_rnn_graph(x, n_input_new, y)

#				onehot_pred = session.run(pred, feed_dict={x: keys, n_input_tf: n_input_new})
				onehot_pred = session.run(pred, feed_dict={x: keys})
				onehot_pred_index = int(tf.argmax(onehot_pred, 1).eval())
				sentence = "%s %s" % (sentence,reverse_dictionary[onehot_pred_index])
				# symbols_in_keys = symbols_in_keys[1:]
				# symbols_in_keys.append(onehot_pred_index)
				symbols_in_keys_onehot = symbols_in_keys_onehot[1:]
				symbols_in_keys_onehot.append(index_to_onehot_vector(onehot_pred_index))
			print(sentence)
		except Exception as e:
			print ("exception: {}".format(e))
			print("Word not in dictionary")

