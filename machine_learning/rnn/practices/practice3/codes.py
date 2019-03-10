# for batch size, just imagine there are two parallel training going on
words_in_dataset = tf.placeholder(tf.float32, [time_steps, batch_size, num_features])
lstm = tf.contrib.rnn.BasicLSTMCell(lstm_size)

# initial state of the LSTM memory
hidden_state = tf.zeros([batch_size, lstm.state_size]) # state_size should be a 1d vector that holds the memory
current_state = tf.zeros([batch_size, lstm.state_size])
state = hidden_state, current_state
probabilities = []
loss = 0.0
for current_batch_of_words in words_in_dataset:
	# the value of state is updated after processing each batch of words
	output, state = lstm(current_batch_of_words, state)

	# the lstm output can be used to make next word predictions
	logits = tf.matmul(output, softmax_w) + softmax_b
	probabilities.append(tf.nn.softmax(logits))
	loss += loss_function(probabilities, target_words)


# placeholder for the inputs in a given iteration
words = tf.placeholder(tf.int32, [batch_size, num_steps])

lstm = tf.contrib.rnn.BasicLSTMCell(lstm_size)

# initial state of the LSTM memory
initial_state = state = tf.zeros([batch_size, lstm.state_size])

for i in range(num_steps):
	output, state = lstm(words[:, i], state)
