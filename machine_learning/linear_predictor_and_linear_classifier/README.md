Linear predictor
----------------------------

Actually, it is the same as linear regression (or linear fitting).  
I.e. f(x) = wT x + w0 (or simply wT x if x is considered to have one more dimension with the value of 1)

it is better to view this equation for one single point instead of the whole dataset.  
WT is 1xd and x is dx1 so the result from the RHS is a scalar.

This can be used to predict the output given a data point x, and the output is continuous.
(even if the labels are discrete, when we apply this linear predictor directly, the output won't be discrete.)

To allow the output to be discrete, i.e. classification, we need to add another function on the RHS of linear predictor, such as the sign function.  
Sign function means that if the input to it is larger than 0, then it outputs 1; 
if the input to it is smaller than 0, then it outputs -1 (or 0, depending on convention).


Linear classifier
-------------------------

Linear classifier relies on linear predictor and one extra function.

Linear predictor is like finding a hyperplane that best fits the training data (X~Y).  
Linear classifier is like finding a hyperplane that best separates the training data (X) based on their labels (Y).

Linear classifier may sound restrictive as it always has to stick to a hyperplane (which is linear).  
But in fact it is quite powerful. 
Svm is one type of linear classifier that can do powerful classification.  
The trick is to map the raw data points (x) to high-dimension space to make them more linear.  
Read "svm" README.md for more details.

Assume that we do not know the trick and stick to the raw data points, 
then often it is quite restrictive.

E.g. in the 2d space, we have these 4 points: (0,0), (0,1), (1,0), (1,1) (each dimension is binary). 
Each of these points has a label of 1 or -1 (i.e. 2 classes only).  
Are we able to classify the case that (0,0) and (0,1) correspond to class 1 and the rest to class -1?   
The answer is yes. 
Draw the 4 points on a 2d plane and it is not hard to draw a line that separate these 2 sets (in fact there are infinite choices).  
What about the case that (0,0) and (1,1) corresponding to class 1 and the rest to class -1?  
We can't..  
No matter how we draw a line to put (0,0) and (1,1) to the same side,  the line will also separate (0,1) and (1,0).

Therefore if 2nd case is indeed the ground truth, by nature linear classifier on the 2d space cannot do the job.  
The solution is of course to map them to higher dimensional space.  
But the question we are more interested here is that given a linear classifier on the 2d space, 
what is the maximum of number of input points (each dimension takes binary value; just for simplicity) 
that the linear classifier is always able to separate them cleanly (i.e. shatter),
no matter what labels they are?

We can ask a more general question. given a linear classifier on the d dimensional space,
how many inputs points can be shattered by the linear classifier?

In fact, we can ask an even more general question. given a class of functions H (one example is the linear classifier), what is the number of points it can shatter?

All these questions can be answered by VC dimensions. 
Read the VC dimension README for more details.
