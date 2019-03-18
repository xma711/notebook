LDA
------------------

LDA stands for linear discriminant analysis.

Like naive bayes, LDA is a generative model.

Problem LDA tries to solve:  
binary classification with y={-1, +1} based on feature vector x = (x1, ..., xd)

the biggest assumption is that
P(X | Y) is gaussian with the same covariance matrix E but different means mu_(-1) and mu_(+1)

so P(X=x|Y=y) = 1/( (2pi)^(d/2) |E|^(1/2) ) * e^( -1/2 (x-mu_(y))^T E^(-1) (x-mu_(y)) )  
i.e. P(X=x|Y=y) = normal_distribution( mean = mu_(y), variance = E )

after the model is trained, then we can use it to do prediction.  
It is just to compare P(Y=1|X) and P(Y=0|X).  
P(Y|X) = P(Y)*P(X|Y)/CONST, where we know P(Y) and P(X|Y).  
Then we can obtain which Y leads to a larger probability.
