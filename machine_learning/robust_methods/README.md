robust methods
------------------

if a model-fitting method (like linear fitting) can be easily affected by outliers, it is not robust.

however, there are ways to make them robust.

first method is called winsorizing (or M-estimator).
this is to defines an error function that suppresses the effect of outliers.  
e.g. error function of each point = r^2/(a^2 + r^2), where r is the difference between the estimated result from the model given an input and the real result.  
even if r goes to infinity, the error function outputs 1!  
this means that as long as outlier are not more than half, they can be supressed quite well.

specially for least squares (linear fitting), we can introduce a weight matrix W to make each r^2 multiplied by a wi.  
the effect is that E(a) = SUM{ wi * ri(a)^2 }, instead of the usual E(a) = SUM{ ri(a)^2 } .  
the estimated results for a = (XT W X)^(-1) XT W y.  
in fact, this is one way of winsorizing.

another powerful method is trimming.  
just use all points to estimate the model, and then remove k points with largest misfit from the points;
then compute M again with remaining points. 
the steps can be repeated.

one more powerful method is RANSAC (Random Sample Consensus).  
just randomly select the minimum number of points to compute the model.  
then identify a subset that has error smaller than a threshold with this model.  
if this subset has a large enough size, keep it and label it.  
do this k times so we have some subsets identified.  
just pick the subset with the biggest size to compute the model.

RANSAC is useful when the number of points is not many.

another variant of RANSAC is that after finding the model,
check each point and keep the points that agree with the model and keep it as a set.  
at the end also pick the set with the maximum number and then compute the model.
