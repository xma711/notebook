### run this script using python2 from anaconda. 
### also need to do a conda install theano after install.
### reference: http://deeplearning.net/software/theano/library/compile/function.html

import theano
import theano.tensor as tensor

print "simple example"
# create a tensor variable, which doesn't have to have a value yet
# x is a so-called symbolic variable
x = theano.tensor.dscalar('x'); 

# theano.function is the interface for compiling graphs into callable objects
f = theano.function([x], 2*x); # define a theano function
print f(4)

# the idea is that we've compiled the symbolic graph (2*x) into a function 
# that can be called on a number and will do some computations.

### reference: http://deeplearning.net/software/theano/tutorial/examples.html#basictutexamples

print "\nlogistic function"
x = tensor.dmatrix('x'); # define a tensor variable
s = 1 / (1 + tensor.exp(-x)); # define a function on x
logistic = theano.function([x], s); # actually this looks like a template
print logistic([ [0, 1], [-1, -2] ]);

# we want to apply function s elementwise on matrix of doubles.
# the reason logistic is performed elementwise is because all of its
# operations - division, addition, exponentiation and division  -
# are themselves elementwise operations.

## let's try compute more than one thing at a time
print "\ncompute more than 1 things"
a = tensor.dmatrix('a');
b = tensor.dmatrix('b');
diff = a - b; # first function; again, imagine this is a tempate only
# actually another way to imagine this is to think that we just define a function
abs_diff = abs(diff); # 2nd function; diff is a function argument to abs_diff
diff_squared = diff ** 2; # 3rd function
f = theano.function([a, b], [diff, abs_diff, diff_squared]);
print f([ [1,1], [1,1] ],   [ [0,1], [2,3] ]);


## use shared variable
print "\nuse shared variable"
state = theano.shared(0) # this is a shared variable; it is hybrid symbolic and non-symbolic variable
# its value may be shared between multiple functions.
# shared variables can be used in symbolic expressions just like the tensor variables,
# but they also have an internal value that defines the value taken by this symbokic variable in all the functions that use it.
# the value can be accessed and modified by the .get_value() and .set_value() methods.

# we also have to use updates parameter!
# updates must be supplied with a list of pairs of the form (shared_variable, new_expression).
# it can also be a dictionary whose keys are shared_variables and values are the new_expressions.
# it means "whenever the function runs, it will replace the .value of each shared variable with the result of the corresponding expression."

inc = tensor.iscalar('inc'); # define a tensor variable (int scalar)
updates = [(state, state + inc)]; # define an update list; 
# in this case there is only one pair of shared variable and expression inside the updates array;
# apparently shared variable can add with tensor variable.
# note that state is kinda initialized with a value. but tensor variable inc is not; 
# inc's value should be supplied by the user

accumulator = theano.function([inc], state, updates = updates);
# interestingly, in this case, the function argument to theano.function is state. previously it is a precise function variable;
# then we have to further supply a update list to handle the state;
# question: what if there are 2 shared variables? input shared variables in a list?
print state.get_value();
accumulator(1);
print state.get_value();
accumulator(300);
print state.get_value();

print "\nuse another function to update the same shared variable"
decrementor = theano.function([inc], state, updates = [(state, state - inc)])
decrementor(2)
print state.get_value();

print "\nnow it is regarding the givens parameter"
# givens replaces a particular node in a graph for the purpose of one particular function
function_of_state = state * 2 + inc;

# match foo's type with state's value type
print state.dtype
foo = tensor.scalar(dtype = state.dtype)

skip_shared = theano.function([inc, foo], function_of_state, givens = [(state, foo)]);
print skip_shared(1, 3); # seems taht we want to use 3 (i.e. foo) for the state this time. 
# the answer from this functions should be 7 (3 * 2 + 1).
print state.get_value(); # state's value is not changed

# in practice, a good way of thinking about the givens parameter
# is as a mechanism that allows you to replcae any part of your formula
# with a different expression that evaluates to a tensor of same shape and dtype


