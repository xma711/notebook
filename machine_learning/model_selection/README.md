Understand training error and test error
----------------------------------------------

All the possible combinations can be found in the document "find_appr_error_and_est_error.odt".

If test error is small, we directly conclude it is a good hypotheses for the population.


IMPORTANT: the following cases are all when the test error is large!

If training error is large, it means approximation error is large, regardless the sample size is large or small.  
A rational solution is to try another hypothesis class.

If training error is small, this case is very tricky.  
It is because there are 2 possible causes:  
	1. sample size is large enough (relative to vc dimension), approximation error is small but estimation error is large.  
	2. sample size is small (relative to vc dimension), approximation error is large

to find out which is the case, we need to draw a learning curve,
which is a graph of error (both training and testing) vs sample size.

If it is case 1, we should observe training error changes from very small to small (increases a bit due to harder to fit all data; but may not obvious),
and test error from larger to large (i.e. noticeably decreasing) and then stays at a certain value.

If it is case 2, we should observer training error stays very small all the way (because the maximum sample size is still not enough),
and the test error stays large (because we don't really learn anything)..  
However, from the observation, we only know that the sample size is definitely not enough; 
but cannot say if the approximation error is really large.  
If we can afford to get more data, then we should observe the test error starts to drop at some point 
but the training error will increase to reflect the approximation error.

Therefore, from the test error vs sample size curve, it is easier to tell whether it is because approximation error is large or simply sample size is not enough.  
If test error behaves 'normally' when sample size increases, it is due to estimation error;  
if test error stays large when sample size increases, it is because sample size is not enough.


More info
----------------------

If the vc dimension is finite, when the sample size goes to infinity,
the test and train errors converge to the approximation error.  
Therefore, by extrapolating the training and validation curves 
we can try to guess the value of the approximation error.

Anyway, if we observer training error low while test error high,
it is always good to get more data and plot the learning curve.  
Then we can estimate the approximation error by the intersection of train curve and test curve.  
Then we can obtain both the approx error and estimation error and act accordingly.

If we cannot get more data, then chop up the existing data and plot the learning curve still.  
At least in the case that the sample data is enough, we can see if the test curve behaves normally.
If it is the case, we know it is because estimation error is too large.  
Otherwise, we know at least sample size too small is definitely one of the problems.


More advice
----------------------

Check the last part of chapter 11.
