import csv
import itertools
import operator
import numpy as np
import nltk
import sys
import os
import time
from datetime import datetime
from utils import *
from rnn_theano import RNNTheano

# nltk.download('book')

_VOCABULARY_SIZE = int(os.environ.get('VOCABULARY_SIZE', '8000'))
_HIDDEN_DIM = int(os.environ.get('HIDDEN_DIM', '80'))
_LEARNING_RATE = float(os.environ.get('LEARNING_RATE', '0.005'))
_NEPOCH = int(os.environ.get('NEPOCH', '100'))
_MODEL_FILE = os.environ.get('MODEL_FILE')

def train_with_sgd(model, X_train, y_train, learning_rate = 0.005, nepoch=1, evaluate_loss_after=5):
	# we keep track of the losses so we can plot them later
	losses = []
	num_examples_seen = 0
	for epoch in range(nepoch):
		# optionally evaluate the loss
		if (epoch % evaluate_loss_after == 0):
			loss = model.calculate_loss(X_train, y_train)
			losses.append((num_examples_seen, loss))
			time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
			print "%s: Loss after num_examples_seen=%d epoch=%d: %f" % (time, num_examples_seen, epoch, loss)
			# adjust the learning rate if loss increases
			if (len(losses) > 1 and losses[-1][1] > losses[-2][1]):
				learning_rate = learning_rate * 0.5
				print "setting learning rate to %f" % learning_rate
			sys.stdout.flush()
			# saving model parameters
			save_model_parameters_theano('./data/rnn-theano-%d-%d-%s.npz' % (model.hidden_dim, model.word_dim, time), model)

		# for each training example...
		for i in range(len(y_train)):
			# one sgd step
			model.sdg_step(X_train[i], y_train[i], learning_rate)
			num_examples_seen += 1
