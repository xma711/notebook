Basic
------------------

Let X be the input set, each xi belongs to R^2 (2 dimensions/features, each dimension is a real number).  
Let Y be the labels (outputs), and yi belong to {1,-1}^1.  (i think better to imagine 1 and -1 here are different categories, rather than numbers.)

The simplest neural network we can draw is that on the first layer, we have 2 nodes for the 2 dimensions of each xi and 1 additional node for value 1 (the so-called bias).  
And on the 2nd layer we have one single output node, which connects to both input nodes.    
With this simple architecture, the easiest equation we can have is  
yi = w1 x1 + w2 x2 + b * 1  (equation 1)

it is not hard to see that this is actually linear regression.  
In fact, from this, we can see that linear regression is the simplest form of a neural network.

We can also view this as something like: the input to the output node is (w1 x1 + w2 x2 + b * 1) while the output node applies an identity function on the input,
and so the output from this node is the same as the input to this node.

However, as we want to classify xi to either 1 or -1, it is better for us to have a function on the output such that the output is bounded by a range (such as [0,1] ) 
so that we know how to classify xi (if the output is more 1 than 0, we can say xi belongs to one category; otherwise it is another category.)

There are some such functions that can be used, such as sigmoid, logistic or tanh functions.  
Okay now we make equation 1 slightly more complicated:   
yi = sigmoid(w1 x1 + w2 x2 + b)  (equation 2)

when using an appropriate cost function (i.e. empirical risk function), we can try to find the values for w1 w2 and b that will minimize the cost function (usually through gradient descent).  
One such cost function is the logloss function, which essentially means that if the classification is wrong the cost is 1, and otherwise 0 cost.


More nodes
-----------------------

Let's say we want 2 hidden nodes (h1 and h2) and one bias node in the 2nd layer, we just add them and shift the output node to 3rd layer.  
H1 and the 2 input nodes and bias form something similar to the basic architecture: h1 = sigmoid (w1 x1 + w2 x2 + b1).  
Similarly for h2: h2 = sigmoid (w3 x1 + w4 x2 + b1).  
(we may need to name the weights in a more systematic way; but let's do it this way now for simplicity.)  
From hidden nodes to the output node, the equation is yi = sigmoid( w5 h1 + w6 h2 + b2), which can be unrolled to be a much longer equation linking up yi and xi.  
In fact, this is the pure math part of a neural network: it is just a (usually nonlinear) equation linking up outputs and inputs.  
And all we need to do is to find out the best weights that minimize the cost function of our choice.


Another perspective
------------------------- 

Using the 2 inputs nodes, 2 hidden nodes and 1 output node case (let's ignore the bias nodes for now), 
we can understand the network from another perspective.  
Each node (except input nodes) can be view as a neuron. 
If the input to a neuron reaches a threshold, it will be activated.  
The activation is controlled by the sigmoid function. in fact it is a continuous function, so the output is like a percentage of activation.  
If a neuron is activated, it will output a higher value to the neurons in the subsequent layer.  
The whole process mimic the neurons in a human brain.
