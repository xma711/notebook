from __future__ import print_function

import numpy as np
import tensorflow as tf
from tensorflow.contrib import rnn
import random
import collections
import time


class LSTM_RNN:
	def __init__(self, n_hidden, vocab_size, learning_rate):
		self.n_hidden = n_hidden
		self.vocab_size = vocab_size
		self.learning_rate = learning_rate

		# RNN output node weights and biases
		self.weights = {
			'out': tf.Variable(tf.random_normal([n_hidden, vocab_size]))
		}
		self.biases = {
			'out': tf.Variable(tf.random_normal([vocab_size]))
		}

#		self.build_graph()

	# create the necessary functions here
#	def build_graph(self):

	# actually, this function is to add nodes to the tensorflow graph
	# def predict(self, x, n_input_tf):
	def predict(self, x, n_input):
		# reshape to [1, n_input_tf]
		# x = tf.reshape(x, [-1, n_input_tf])
		# n_input_tf = tf.shape(x)[1]
		x1 = tf.reshape(x, [-1, n_input, self.vocab_size])

		# Generate a n_input-element sequence of inputs
		# (eg. [had] [a] [general] -> [20] [6] [33])
		# returns a list of sub-tensors
		# split(value, num_or_size_splits, axis=0, ... )
		
		# print ("in predict. n_input_tf = {}".format(n_input_tf))
		x1 = tf.split(x1, n_input, 1)
		#x = tf.split(x, [1,self.vocab_size], 0)

		# possible to pass the full x1 array into the graph?
		i = 0
		for xi in x1:
			x1[i] = tf.reshape(x1[i], [1,self.vocab_size])
			i += 1

		# 2-layer LSTM, each layer has n_hidden units.
		# Average Accuracy= 95.20% at 50k iter
		rnn_cell = rnn.MultiRNNCell([rnn.BasicLSTMCell(self.n_hidden),rnn.BasicLSTMCell(self.n_hidden)])

		# 1-layer LSTM with n_hidden units but with lower accuracy.
		# Average Accuracy= 90.60% 50k iter
		# Uncomment line below to test but comment out the 2-layer rnn.MultiRNNCell above
		# rnn_cell = rnn.BasicLSTMCell(self.n_hidden)

		# generate prediction
		# 2nd argument is 'inputs': A length T list of inputs, each a Tensor of shape [batch_size, input_size], or a nested tuple of such elements.
		outputs, states = rnn.static_rnn(rnn_cell, x1, dtype=tf.float32)

		# there are n_input outputs but
		# we only want the last output
		return tf.matmul(outputs[-1], self.weights['out']) + self.biases['out']

#	def build_rnn_graph(self, x, n_input_tf, y):
	def build_rnn_graph(self, x, n_input, y):
		# both x and n_input_tf are tensors
		pred = self.predict(x, n_input)
		# pred = self.predict(x)

		# Loss and optimizer
		cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
		optimizer = tf.train.RMSPropOptimizer(learning_rate=self.learning_rate).minimize(cost)
		return pred, cost, optimizer

