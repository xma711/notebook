import numpy as np
import tensorflow as tf

# model parameters
# variables are trainable parameters
W = tf.Variable([.3], tf.float32) # set init value too
b = tf.Variable([-.3], tf.float32)

# model input and output
# placeholder is for the model to accept external inputs later
x = tf.placeholder(tf.float32)
linear_model = W*x + b # setup the model
y = tf.placeholder(tf.float32)

# loss function
loss = tf.reduce_sum(tf.square(linear_model - y))

# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# training data
x_train = [1,2,3,4]
y_train = [0,-1,-2,-3]

# training loop
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init) # reset values to wrong
for i in range(1000):
	sess.run(train, {x:x_train, y:y_train})

# evaluate training accuracy
# the first argument to sess.run function is to tell the model what to run, with the same inputs 
curr_W, curr_b, curr_loss = sess.run([W, b, loss], {x:x_train, y:y_train})

print ("W: %s, b: %s, loss: %s" % (curr_W, curr_b, curr_loss))
