VC Dimension
-----------------

main question: given a class function H, how many points can H shatter? 
The answer is the VC dimensions of H.

first thing first, what is the meaning of "shatter"?  
let's say we have a domain set X, which has exactly 4 points {(0,0), (0,1), (1,0), (1,1)}. Each dimension can only take 0 or 1 as the value.  
we also have a label set Y, which has 2 choices only: {1, -1}.   
As the number of points in X is finite and the number of labels is finite,
we have finite number of functions that map any combinations of X to Y.  
in fact, in this example, the number of functions are 2^4. 
the reason is that each point is either mapped to 1 or -1, so there are 2^4 combinations of X -> Y.  
given any combination as a training set, if a function class is able to be trained to represent the function effect exactly, 
we say this function class shatters the this set of data.

however, more often than not, a function class is unable to shatter the whole set of X.  
then we will ask, maximumly how many points can this function class shatter?

e.g. given the X set above, a linear classifier ( i.e. sign(wt x + b) ) (which is a function class) is unable to shatter the 4 points.  
why? because if (0,0) and (1,1) are in the same group, there is no any single line that can separate (0,0) and (1,1) from the other 2 points.  
then what is the maximum number that a linear classifier can shatter? 
the answer is 3. 
and 3 is the VC dimension of the linear classifier.

in fact, there is a theorem saying that a linear classifier with a bias that map R^d -> {1, -1} can shatter at most d+1 points.  
(when there is no bias, i.e the hyperplane will pass through 0, the maximum number that it can shatter is d points).  
i.e. the vc dimension of the linear classifier with a bias is d+1.

other questions about vc dimension that we can ask are:  
	- what is the vc dimension of a decision tree?  
	- what is the vc dimension of a neural network with n hidden nodes?

these questions do have some answers. (TODO: write the answers down somewhere...)

another important question to ask is that, 
if we know that a function class H has a vm dimension of d,
then given m input data points, how many functions can be obtained from H to map the m input data points to some {1, -1}?  
or can we have some upper bound? this question can be answered by Sauer's Lemma.

before we move on the Sauer's lemma, we can know that if the answer to the question is 2^m,
then the function class H is able to shatter the all m points, 
which is the best case, meaning function class H is good choice to be used as a model to map these input points to the labels.  
more often, this is unlikely. 
so knowing a upper bound is an good indicator of how good this function class is to be used for training this data set.


Sauer's Lemma
---------------------

Sauer's Lemma says that when the vc dimension of a function class H <= d (and d is a finite number),
then for any choice of number of input points (m), 
the largest number of functions that can be obtained (tH(m)) is less than or equal to (mC0 + mC1 + mC2 + ... + mCd).

why? i don't understand it yet but one explanation is offered here: https://en.wikipedia.org/wiki/Sauer%E2%80%93Shelah_lemma

(
try to think of an intuition but failed:  
	at the best case, any d points from the m-points set can be shattered by H,
	then we can partition the m points to m/d sets. 
	each set has 2^d functions. then what????
)

in particular, if m > d+1 (which is usually the case), tH(m) <= (em/d)^d  (where e is the exponential constant).

what does this mean?  
if H is able to shatter the m points, the number of functions is 2^m, which is a big number if m is big.  
but if m >> d, the number of functions is only at most (e/d)^d * m^d, which is much smaller than 2^m. 
and it is just the upper bound; the true number may be much less than this number.   
e.g. if d=5, m=20, 2^m = 1,048,576 while (e/d)^d * m^d = 0.0475 * 3200000 = 151,968 which is a fraction of 2^20.

example of not-learnablity with hypothesis class with infinite vc dimension
-----------------------------------------------------

decision tree has infinite vc dimension.

without limiting decision tree's size, it can always construct a perfect tree to explain every single training data (0 empirical risk).

but clearly, the tree will be overfitting (high general risk).

once we limit the size of the tree, the empirical risk increases, but the general risk will drop.

when we don't limit the decision tree, the approximation error is the optimal bayesion error (0 if each x will correspond to a particular y) because it can explain everything.

when we reduce the size of decision tree, we increase the approximation error but reduce the estimation error.  
as long as the magnitude of the increase of the appr error is smaller than the magnitude of the reduction in the estimation error, it is worth to do.
