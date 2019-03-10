# reference: https://www.tensorflow.org/api_docs/python/tf/nn/dynamic_rnn

# create a basicRNNCell
rnn_cell = tf.nn.rnn_cell.BasicRNNCell(hidden_size)

# output is a tensor of shape [batch_size, max_time, cell_state_size]

# defining initial state
initial_state = rnn_cell.zero_state(batch_size, dtype=tf.float32)

######## example 1: single LSTM cell

# state is a tensor of shape [batch_size, cell_state_size]
outputs, state = tf.nn.dynamic_rnn(
	rnn_cell,
	input_data,
	initial_state=initial_state,
	dtype=tf.float32
)

######## example 2: double LSTM cells

# create 2 LSTMCells
rnn_layers = [tf.nn.rnn_cell.LSTMCell(size) for size in [128, 256]]

# create a RNN cell composed sequentially of a number of RNNCells
multi_rnn_cell = tf.nn.rnn_cell.MultiRNNCell(rnn_layers)

# outputs is a tensor of shape [batch_size, max_time, 256]
# state is a N-tuple where N is the number of LSTMCells containing a tf.contrib.rnn.LSTMStateTuple for each cell
outputs, state = tf.nn.dynamic_rnn(
	cell=multi_rnn_cell,
	inputs=data,
	dtype=tf.float32
)

# cell: an instance of RNNCell
# sequence_length: (optional) an int32/int64 vector sized [batch_size]. it is more for correctness than performance.
# time_major: the shape format of the inputs and outputs tensors.
	# if true, these tensors must be shaped [max_time, batch_size, depth].
	# if false, these tensors must be shaped [batch_size, max_time, depth]
# scope: VariableScope for the created subgraph; defaults to "rnn".
