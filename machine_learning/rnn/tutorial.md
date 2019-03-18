Tutorial
--------------------------

Reference: https://www.tensorflow.org/tutorials/recurrent

the model: 
	consists of an LSTM cell that processes one word at a time 
	and compute the probabilities of the possible values for the next word in the sentence.

Will process data in mini-batches of size_batch_size.

Every word in a batch should correspond to a time t. (!!)  
Tensorflow will automatically sum the gradients of each batch for you. (???)

(it seems that the concept of batch here is not the same as that in stochastic gradient descent??)


Example.

Sentence1 = "the quick brown fox is quick"  
sentence2 = "the red fox jumped high"

```
 t=0	t=1	t=2	t=3	t=4  
[the	brown	fox	is 	quick]  
[the 	red	fox	jumped	high]  

words_in_dataset[0] = [the, the]  
words_in_dataset[1] = [brown, red]  
words_in_dataset[2] = [fox, fox]  
words_in_dataset[3] = [is, jumped]  
words_in_dataset[4] = [quick, high]  

num_batches = 4 (???)  
Batch_size = 2 (???)  
Time_steps = 5
```

question: why each batch does not consists of sequential words????


#### psedocode:

```
words_in_dataset = tf.placeholder(tf.float32, [num_batches, batch_size, num_features])

lstm = tf.contrib.rnn.BasicLSTMCell(lstm_sie) # what is lstm_size??

# initial state of the LSTM memory
hidden_state = tf.zeros([batch_size, lstm.state_size])
current_state = tf.zeros([batch_size, lstm.state_size])
state = hidden_state, current_state # this makes state a tuple

probabilities = []
loss = 0.0

for current_batch_of_words in words_in_dataset:
	# the value of state is updated after processing each batch of words.
	output, state = lstm(current_batch_of_words, state)

	# the lstm output can be used to make next word prediction
	logits = tf.matmul(output, softmax_w) + softmax_b
	probabilities.append(tf.nn.softmax(logits))
	loss += loss_function(probabilities, target_words)
```

by design, the output of a recurrent neural network (RNN) depends on arbitrarily distant inputs.  
Unfortunately, this makes backpropagation computation difficult.  
In order to make the learning process tractable, 
it is common to create an "unrolled" version of the network,
which contains a fixed number (num_steps) of LSTM inputs and outputs.  
The model is then trained on this finite approximation of the RNN.  
This can be implemented by feeding inputs of length num_steps at a time
and perform a backward pass after each such input block.

Simplified block of code for creating a graph which performs truncated backpropagation:  
```
words = tf.placeholder(tf.int32, [batch_size, num_steps])

lstm = tf.contrib.rnn.BasicLSTMCell(lstm_size)

# initial state of the LSTM memory
initial_state = state = tf.zeros([batch_size, lstm.state_size])

for i in range(num_steps):
	# the value of state is updated after processing each batch of words.
	output, state = lstm( words[:, i], state )

	# the rest of the code.
	# ...

Final_state = state

```

to implement an iteration over the whole dataset:  
```
# a numpy array holding the state of LSTM after each batch of words.
Numpy_state = initial_state.eval()
total_loss = 0.0
for current_batch_of_words in words_in_dataset:
	numpy_state, current_loss = session.run([final_state, loss],
		feed_dict = {initial_state: numpy_state, words: current_batch_of_words})

	total_loss += current_loss
```

#### inputs

the word IDs will be embedded into a dense representation before feeding to the LSTM. 
This allows the model to efficiently represent the knowledge about particular words.  
```
# embedding_matrix is a tensor of shape [vocabulary_size, embedding_size]
word_embeddings = tf.nn.embedding_lookup(embedding_matrix, word_ids)
```
the embedding matrix will be initialized randomly 
and the model will learn to differentiate the meaning of words just by looking at the data. (??)

#### loss function

we want to minimize the average negative log probability of the target words:  
loss = -1/N SUM( ln(p_target_i) )

#### stacking multiple LSTMs

the output of the first layer will become the input of the second and so on.

We have a class called MultiRNNCell that makes the implementation seamless.

```
def lstm_cell():
	return tf.contrib.rnn.BasicLSTMCell(lstm_size)

stacked_lstm = tf.contrib.rnn.MultiRNNCell(
	[lstm_cell() for _ in range(number_of_layers)]
)

initial_state = state = stacked_lstm.zero_state(batch_size, tf.float32)

for i in range(num_steps):
	# the value of state is updated after processing each batch of words.
	output, state = stacked_lstm(words[:, i], state)

	# the rest of the codes
	# ...

Final_state = state
```
