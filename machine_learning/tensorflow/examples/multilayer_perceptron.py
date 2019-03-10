# run with python3anaconda
# original codes: https://pythonprogramming.net/rnn-tensorflow-python-machine-learning-tutorial/

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data/", one_hot = True)

n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

n_classes = 10
batch_size = 100

x = tf.placeholder('float') #, [None, 784])
y = tf.placeholder('float')

def neural_network_model(data):
	hidden_1_layer = {'weights': tf.Variable(tf.random_normal([784, n_nodes_hl1])), # data is m x 784, weight is 784 x 500, result will be m x 500
			'biases': tf.Variable(tf.random_normal([n_nodes_hl1]))} # biases is a vector and it will be added to the each row of result

	hidden_2_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])), 
			'biases': tf.Variable(tf.random_normal([n_nodes_hl2]))}

	hidden_3_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])), 
			'biases': tf.Variable(tf.random_normal([n_nodes_hl3]))}

	output_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])), 
			'biases': tf.Variable(tf.random_normal([n_classes]))}


	l1 = tf.add(tf.matmul(data, hidden_1_layer['weights']), hidden_1_layer['biases'])
	l1 = tf.nn.relu(l1)

	l2 = tf.add(tf.matmul(l1, hidden_2_layer['weights']), hidden_2_layer['biases'])
	l2 = tf.nn.relu(l2)

	l3 = tf.add(tf.matmul(l2, hidden_3_layer['weights']), hidden_3_layer['biases'])
	l3 = tf.nn.relu(l3)

	output = tf.add(tf.matmul(l3, output_layer['weights']), output_layer['biases'])

	return output

# originally there is an input x.
# but i have a question: do we really need to input x here? x is already global..
# it turns out that it really doesn't need the x here. this way it is easier to be understood
def train_neural_network():
# maybe better this way:
# def train_neural_network(data): # and then set the train data and test data to the data input
	# now x is local
	prediction = neural_network_model(x) # the function linking prediction to input
	cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction,  labels=y)) # the cost function
	optimizer = tf.train.AdamOptimizer().minimize(cost) # the function to run optimization

	hm_epochs = 10
	with tf.Session() as sess:
		sess.run(tf.global_variables_initializer()) # make the virtual variables real (i think)

		for epoch in range(hm_epochs):
			epoch_loss = 0
			for _ in range( int(mnist.train.num_examples/batch_size) ):
				epoch_x, epoch_y = mnist.train.next_batch(batch_size)
				_, c = sess.run([optimizer, cost], feed_dict = {x:epoch_x, y: epoch_y})
				epoch_loss += c

			print ('Epoch', epoch, ' completed out of ', hm_epochs, ' loss: ', epoch_loss)

		correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))

		accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
		print('Accuracy: ', accuracy.eval({x: mnist.test.images, y:mnist.test.labels}))

train_neural_network()
