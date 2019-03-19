#!/home/xma/anaconda2/bin/python

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# define input data
x_data = np.arange(100, step=.1) # 1000 points
y_data = x_data + 20 * np.sin(x_data/10) # y_data is x_data with some extra stuff 

# plot input data
plt.scatter(x_data, y_data)

n_samples = 1000
batch_size = 100 # for SGD?

# tensorflow is finicky about shapes, so reshape
x_data = np.reshape(x_data, (n_samples, 1)) # a nx1 matrix
y_data = np.reshape(y_data, (n_samples, 1))

# define placeholders for input
X = tf.placeholder(tf.float32, shape=(batch_size, 1)) # fix the dimension
y = tf.placeholder(tf.float32, shape=(batch_size, 1))

# define variables to be learned
with tf.variable_scope("linear-regression"):
	W = tf.get_variable("weights", (1,1), initializer=tf.random_normal_initializer())
	b = tf.get_variable("bias", (1,), initializer=tf.constant_initializer(0.0))
	y_pred = tf.matmul(X, W) + b # nx1 * 1x1 + (1,)

loss = tf.reduce_sum( (y - y_pred)**2 / batch_size )
# next is to get gradients in order to do gradient descent, but we have existing optimizer to do this

# to run one step of gradient descent
opt = tf.train.AdamOptimizer()
opt_operation = opt.minimize(loss) 
# this is it! it knows W and b are something to be found;
# and it knows how to calculate it for one step: W = W - dL/dW and b = b - dL/db

# run on single step of gradient descent
with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	_, loss_val = sess.run([opt_operation, loss], feed_dict={X: x_data[0:batch_size], y: y_data[0:batch_size]})
	print ("current loss = {}".format(loss_val))

	for i in range(2000):
		# select random minibatch
		indices = np.random.choice(n_samples, batch_size)
		x_batch, y_batch = x_data[indices], y_data[indices]

		# do gradient descent step
		_, loss_val = sess.run([opt_operation, loss], feed_dict={X: x_batch, y: y_batch})

		if i%100 == 0:
			print "loss_val = {}".format(loss_val)

print "loss_val = {}".format(loss_val)

