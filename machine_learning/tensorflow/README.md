tensorflow
------------------------

tensorflow is somewhat similar to numpy.
but numpy is executed immediately, while tensorflow 'variables' need to be explicitly evaluated in a session.

i think i have to think of any tensor as a function.
even tf.constant(1.0) is a function, not a constant by its type.  
only after we run/eval the function, we can get the returned value.

the process is to create a tensor, then create a session, then evalute this tensor in the session.

example:  
```
a = tf.constant(5.0) # cannot see a as a constant or variable. have to see a as a function that will return a constant 5.0
b = tf.constant(6.0)
c = a * b # c is a function that will return a value from ret value of function a * ret value of function b
with tf.Session() as sess:
	print (sess.run(c))
	# or evaluate c using: 
	# print (c.eval())
	# c.eval() is just syntactic sugar for sess.run(c) in the current active session
```

tensorflow graph
----------------------------

tensorflow programs are usually structured into a construction phase that assembes a graph,
and an execution phase that uses a session to execute ops in the graph.

by default there is already a global default graph.
all computations add nodes to the global default graph.


tensor variables
----------------------------------

tensor variables are in-memory buffers containing tensors.
when you train a model you use variables to hold and update parameters.

example of tensor variables:  
```
# W1 is not a variable itself. it is a function that manages an internal variable that has a dimension of (2,2)
W1 = tf.ones((2,2)) # tensor constants. No need to explictly initialize the initial values
W2 = tf.Variable(tf.zeros((2,2)), name='weights') # a variable with initial values; but the init values are not really created yet
with tf.Session() as sess:
	print (sess.run(W1)) # evaluate W1
	sess.run(tf.initialize_all_variables()) # even initialization has to be evaluated explicitly
	print (sess.run(W2))
```

example 2 of tensor variables:  
```
W = tf.Variable(tf.zeros((2,2)), name='weights')
R = tf.Variable(tf.random_normal((2,2)), name='random_weights')
with tf.Session() as sess:
	# sess.run(tf.initialize_all_variables()) # old style
	sess.run(tf.global_variables_initializer())
	print (sess.run(W))
	print (sess.run(R))
```

example of updating variable state:   
```
state = tf.Variable(0, name = 'counter') # state is a function that manages an internal variable of name 'counter'
new_value = tf.add(state, tf.constant(1)) # new_value is a function that adds function state and function tf.constant()
update = tf.assign(state, new_value) # update is a function that assign ret value of new_value to the internal variable of state function
# 'update' function returns nothings. actually it is easier to understand if it is: update = state.assign(new_value)
# why cannot state = new_value? because then the function that holds the variable counter will be lost

with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	print (sess.run(state)) # state will return the initial value of counter
	for _ in range(3):
		sess.run(update) # update function will be executed, which triggers other needed functions to be executed
		print(sess.run(state))
```

fetching variable state / returned values:  
```
input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)
intermed = tf.add(input2, input3)
mul = tf.mul(input1, intermed)
with tf.Session() as sess:
	result = sess.run([mul, intermed])
	print (result)
```

thinking about it, one naive implementation of tensorflow is just to define many functions.
each tensor is one function.
function will not be executed until they are called.
the so-called state in each tensor is just the returned value of each function.  
if i imagine in this way, things will be much easier to understand.

to convert numpy array to tensor:  
```
a = np.zeros((3,3))
ta = tf.convert_to_tensor(a) # just imagine there is function wrapping around the numpy variable a. also note that ta is a tf constant, not tf variable
with tf.Session() as sess:
	print (sess.run(ta))
```

tensor placeholder
-----------------------------------------------

compared to tf.convert_to_tensor(), tf.placeholder is more flexible.
tf.placeholder is a dummy node that provides an entry point for data to computational graph.  
a feed_dict is a python dictionary mapping from tf.placeholder to data (numpy arrays, lists, etc)

example:  
```
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.mul(input1, input2)

with tf.Session() as sess:
	print (sess.run([output], feed_dict={input1:[7.], input2: [2.]}))
```

variable scope
----------------------------------------

tf.variable_scope() provides simple namespacing to avoid clashes.  
i.e. variable scope adds prefixes to variable names within scope.  
tf.get_variable() creates/accesses variables from within a variabe scope.  
example:  
```
with tf.variable_scope("foo"):
	with tf.variable_scope("bar"):
		v = tf.get_variable("v", [1]) # by default, it will keep creating v:x, x is an id
		# previously, we use: v = tf.Variable(1, name='foo/bar/v:0')
assert v.name == "foo/bar/v:0"
```
to reuse the variable with a name within a variable_scope:  
```
with tf.variable_scope("foo"):
	v = tf.get_variable("v", [1]) # btw this [1] is shape
	# need to do the following line in order to let subsequent codes retrieve the same tensor based on name
	tf.get_variable_scope().reuse_variables()
	v1 = tf.get_variable("v", [1])
assert v1 == v # btw v is a tensor variable
```

also, you can do u = tf.get_variable("u", [1,2]) without the "with tf.variable_scope()",
because by default there is a '' scope.

if reuse is set to false, tf.get_variable() creates and returns a new tf variable;  
if reuse is set to true, it searches for existing variable with given name. valueError exception is raised if not found.


linear regression implemented in tensorflow
-------------------------------------------------

refer to linear_regression_tensorflow.py
