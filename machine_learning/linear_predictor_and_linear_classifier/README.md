linear predictor
----------------------------

actually, it is the same as linear regression (or linear fitting).  
i.e. f(x) = wT x + w0 (or simply wT x if x is considered to have one more dimension with the value of 1)

it is better to view this equation for one single point instead of the whole dataset.  
wT is 1xd and x is dx1 so the result from the RHS is a scalar.

this can be used to predict the output given a data point x, and the output is continuous.
(even if the labels are discrete, when we apply this linear predictor directly, the output won't be discrete.)

to allow the output to be discrete, i.e. classification, we need to add another function on the RHS of linear predictor, such as the sign function.  
sign function means that if the input to it is larger than 0, then it outputs 1; 
if the input to it is smaller than 0, then it outputs -1 (or 0, depending on convention).


linear classifier
-------------------------

linear classifier relies on linear predictor and one extra function.

linear predictor is like finding a hyperplane that best fits the training data (X~Y).  
linear classifier is like finding a hyperplane that best separates the training data (X) based on their labels (Y).

linear classifier may sound restrictive as it always has to stick to a hyperplane (which is linear).  
but in fact it is quite powerful. 
svm is one type of linear classifier that can do powerful classification.  
the trick is to map the raw data points (x) to high-dimension space to make them more linear.  
read "svm" README.md for more details.

assume that we do not know the trick and stick to the raw data points, 
then often it is quite restrictive.

e.g. in the 2d space, we have these 4 points: (0,0), (0,1), (1,0), (1,1) (each dimension is binary). 
each of these points has a label of 1 or -1 (i.e. 2 classes only).  
are we able to classify the case that (0,0) and (0,1) correspond to class 1 and the rest to class -1?   
the answer is yes. 
draw the 4 points on a 2d plane and it is not hard to draw a line that separate these 2 sets (in fact there are infinite choices).  
what about the case that (0,0) and (1,1) corresponding to class 1 and the rest to class -1?  
we can't..  
no matter how we draw a line to put (0,0) and (1,1) to the same side,  the line will also separate (0,1) and (1,0).

therefore if 2nd case is indeed the ground truth, by nature linear classifier on the 2d space cannot do the job.  
the solution is of course to map them to higher dimensional space.  
but the question we are more interested here is that given a linear classifier on the 2d space, 
what is the maximum of number of input points (each dimension takes binary value; just for simplicity) 
that the linear classifier is always able to separate them cleanly (i.e. shatter),
no matter what labels they are?

we can ask a more general question. given a linear classifier on the d dimensional space,
how many inputs points can be shattered by the linear classifier?

in fact, we can ask an even more general question. given a class of functions H (one example is the linear classifier), what is the number of points it can shatter?

all these questions can be answered by VC dimensions. 
read the VC dimension README for more details.
