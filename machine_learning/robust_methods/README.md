Robust methods
------------------

If a model-fitting method (like linear fitting) can be easily affected by outliers, it is not robust.

However, there are ways to make them robust.

First method is called winsorizing (or M-estimator).
This is to defines an error function that suppresses the effect of outliers.  
E.g. error function of each point = r^2/(a^2 + r^2), where r is the difference between the estimated result from the model given an input and the real result.  
Even if r goes to infinity, the error function outputs 1!  
This means that as long as outlier are not more than half, they can be supressed quite well.

Specially for least squares (linear fitting), we can introduce a weight matrix W to make each r^2 multiplied by a wi.  
The effect is that E(a) = SUM{ wi * ri(a)^2 }, instead of the usual E(a) = SUM{ ri(a)^2 } .  
The estimated results for a = (XT W X)^(-1) XT W y.  
In fact, this is one way of winsorizing.

Another powerful method is trimming.  
Just use all points to estimate the model, and then remove k points with largest misfit from the points;
then compute M again with remaining points. 
The steps can be repeated.

One more powerful method is RANSAC (Random Sample Consensus).  
Just randomly select the minimum number of points to compute the model.  
Then identify a subset that has error smaller than a threshold with this model.  
If this subset has a large enough size, keep it and label it.  
Do this k times so we have some subsets identified.  
Just pick the subset with the biggest size to compute the model.

RANSAC is useful when the number of points is not many.

Another variant of RANSAC is that after finding the model,
check each point and keep the points that agree with the model and keep it as a set.  
At the end also pick the set with the maximum number and then compute the model.
