VC dimension
---------------------

Given a hypothesis class H, e.g. halfspace with d parameters (linear function with d terms wrapped by a sign function), 
how many points can it shatter?

The meaning of shatter is that for, m points, no matter how each point falls into which binary label {+1, -1}, 
we can always find a function from the hypothesis class to represent this mapping.

With m points, there are 2^m possible functions. 
(the m points are in the X domain, labels in the Y co-domain, 
and a function is something that maps each point in X to a label in Y. 
As each point can be mapped to 1 or -1, there are 2^m possible functions.)

Back to the question that "how many points can a hypothesis class shatter?". The answer to this question is the VC dimension of the hypothesis class.

E.g. the halfspace hypothesis class with d parameters has a vc dim of d when there is no bias and d+1 when there is a bias. (see BBSD chapter 9 for proof). 
(intuitively, for d=2, we can draw 4 points on the 2d plane: (0,0), (0,1), (1,0), (1,1). when (0,0) and (1,1) belong to the same label and the other 2 points belong to the other label, we cannot find a line that separate them. but with 3 points, we can always find a line that can separate any arrangements.)

Note that it is only meaningful to talk about VC dimension when the problem is a binary classification (maybe multiclass classifications too?) 

VC dim is kinda measuring the 'richness' of a hypothesis class.
However, it doesn't mean the a bigger VC dim is always good.
In fact, if vc dim is infinite, it is not learnable (no sample size is enough to get a good hypothesis from H).

One useful functionality to use VC dim is to calculate the possible number of functions that can be extracted from hypothesis class H when the input points m is more than VCdim. 
The possible number of functions from m points to {+1, -1} is 2^m.
But the possible number of functions that can be extracted from H to represent some of these 2^m functions is only (em/d)^d, where d is the vc dim of H. 
The formula (em/d)^d is called the Sauer's lemma. the result can be seen as an "effective size" of the hypothesis class, despite it may be an infinite class (halfspace is infinite).


Fundamental theory of statistical learning
--------------------------------------------

When a hypothesis class H has a finite VC dimension, then it is PAC learnable. else, it is not PAC learnable. 
The other way is also true (for binary classification): i.e. when a hypothesis class is PAC learnable, it must have a finite VC dimension.  

When H has a finite VC dimension, it means H is uniform convergence too. the other way is also true. 
This also mean that uniform convergence and PAC learnable is also equivalent.

The equation of m (sample size required) to achieve a maximum error between the population loss LD(h) and the best possible population loss (epsilon) with a probability of at least (1-delta) can be found in BBSD chapter 6. the equation of m is in terms of epsilon, delta, and the VC dim of the hypothesis class.

Note that statistical learning does not consider computational complexity. It only handles sample complexity, i.e. it handles the question of how many data points are needed to find (regardless computationally efficiently or inefficiently) a good hypothesis from a hypothesis class H.


PAC learnable
-------------------------------------------------

PAC learnable stands for "Probably Approximately Correct learnable".  

Let Z be the data. each zi is (xi, yi). The distribution of Z is D.

For a hypothesis class H, for any distribution of Z,
if there exists a learning algorithm (usually the ERM - empirical risk minimization) to find a h 
and a function to get m sample data (a function of epsilon and delta),
such that the population loss when applying this h (LD(h)) is within a desired error 'epsilon' compared to the lowest possible population loss when applying the best possible h from H (which is unknown most of the time) with a probability of at least (1-delta),
then we call this hypothesis class PAC learnable.

More specifically, when the lowest possible population loss is not 0, the H is is agnostic PAC learnable. else, i.e. when the realizability assumption holds, then H is PAC learnable. 

