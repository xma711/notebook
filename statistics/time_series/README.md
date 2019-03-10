stats and time series
----------------------

if yi = 2xi + e, e~N(0,1)

xi may have a complicated distribution, which makes yi have a complicated distribution too.

the correct way of looking at this is that (yi-2xi) = e,
which make (yi-2xi) follow the distribution of e!!!

now (yi-2xi) is 'stationary', because the distribution of (yi-2xi) is the same regardless of xi!!!


however, if we only know that yi = w xi + e, where w is an unknown, how do we get w?

as we alreay assumes that (yi-w xi) follows the normal distribution (or whatever distribution of e),
and we already know all the yi and xi, 
it means that we can have a list of points = {yi - w xi},
where w is still an unknown but stays the same across all points.

one unknown requires one equation to have a single answer, but we have multiple equations,
how to get the best w??

i think MLE can solve this (thinking about this later).

another way to get we is to minimize the sum of ei^2, which is the Least squares method.

anyway, the correct way to look at regression from statistics perspective is that 
we need to create a SINGLE variable (that may combine multiple variables and can have unknowns inside) that follows one single distribution.  
after that, use some methods like MLE or LSM to estimate the unknowns.

for time series, there is only one variable xt.  
if xt follows a fixed distribution regardless of t, then xt is just x.
there will be no such thing as predictiong xt+1 given xt
(or the more correct way to say is that predicting xt+1 is independent of xt)
because each xt is independent and simply follow the same distribution.

if xt has a trend, such as xt has a different mean for each t while having the same variance,
then the SINGLE variable we want to form could be (xt+1 - xt).  
e.g. if xt+1 = 2xt + e, then the mean of each xt+1 is actually 2xt.
we can get a single variable (xt+1 - xt) which follows the distribution of e.


in short, stats is about a variable that follows a distribution, which looks quite static.
for any dynamic data (each data at a different step/time have different distributions),
we need to transform the data for each step/time to a variable that has one single distribution.  
as a result, the dynamic data is transformed to data with a static distribution.


further thinking (incomplete)
------------------------

when (yi - w xi) follows the normal distribution of N(0,1),
what is the the conditional distribution of yi given xi?  
intuitively it should be: p(yi | xi) = p(y|xi) = N(w xi, 1)  
(p(yi | xi) = p(y|xi) because the expression N(w xi, 1) has nothing to do with yi),  
meaning each yi follows a normal distribution of mean = w xi, and variance = 1.

y itself is obvious not from a single distribution (the only exception is that all xt are the same).  
in short, p(y) is not the same as p(yi).

does it mean that these 2 cases are equivalent:  
1. we can form a variable of f(xi,yi) such that this variable follows a same distribution (hopefully very small variance) and  
2. we can find p(y | xi) (i.e. it can be represented by a single function of xi)

both cases do not really care about the distribution of xi.

point 2 seems to say that it doesn't matter if x is stationary;
what it matters is that the distribution of y given x (i.e. when we know the value of x) can be found.


time series and machine learning
-----------------------------------------

reference: https://www.datascience.com/blog/time-series-forecasting-machine-learning-differences


think again (wrong - ignore this section)
---------------------------------

if yi = 2xi + e, e~N(0,1)  
then p(yi | xi) = N(2xi, 1)

what this means is that given a xi, yi has a fixed distribution.
but for different xi, yi has a different distribution (in this example, mean is different but variance is the same)


but what about p(yi,xi) and p(yi)?

p(yi) = SUM_xi( p(yi|xi) * p(xi) ) = SUM_xi( N(2xi, 1) * p(xi) )





initial thinking (likely wrong - ignore this section)
---------------------

for a statistics probability distribution, i can plot the points of the variable x in any order.  
ultimately i can get the probability distribution.

for a linear regression, usually we can randomize the order of x and y pairs (as long as each xi and yi pair is together).  
the Least-square method will result in the same estimations of the parameters.

the reason that i can randomize the order of the pairs of (xi, yi) is that the joint probability of (xi, yi) is the same regardless of i.  
this reason is equivalent to say that (xi,yi) is stationary (i think).  
(or is it that p(yi|xi) is the same, not about p(xi, yi)??? )

if this assumption is not true, we cannot randomize the order of the pairs of (xi, yi).  


let's take a look at a time series xt.


if we do a linear regression of xt and xt+1 (autoregression),
we already assume (xt, xt+1) is stationary,
i.e. the joint probability distribution of (xt, xt+1) is the same regardless of t.  
in some sense, although the probability distribution of xt looks dynamic,
the probability distribution of (xt, xt+1) is static (if the stationary assumption holds.)

ultimately, what we need to do is to get (xi, yi) such that the joint probability of (xi, yi) is the same regardless of i.

if such assumpiton doesn't hold, we need to obtain new pair of (xi, yi) from the raw data 
to make this assumption valid.

e.g. yi = 2xi + e, where e follows normal distribution of (0,1),
it means that for each xi, yi follows a normal distribution of (2xi, 1).

p(xi, yi) = p (yi | xi) * p(xi) = N(2xi, 1) * p(xi)
