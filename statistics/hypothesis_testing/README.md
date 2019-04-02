Usual scenario
-----------------------

There is a list of observed values xi,
and then we want to test a hypothesis (null hypothesis) such as:  
h0: population mean = 10

and there is always a alternative hypothesis:  
h1: population mean != 10

so how to proceed from here?

Firstly, we will be able to compute the sample mean x_bar_observed and sample variance S^2 (sample variance can be a surrogate for population variance)

if number of xi is large enough (> 30 e.g.), we can assume the sample mean x_bar itself follows a normal distribution.
What this means is that if we are able to get many samples with each sample having 30 observation,
the mean of the sample will follow a normal distribution.  
Why? central limit theorem!!!

Ok back to the problem.
Now we have the observed sample mean and the sample variance,
we can compute the variance for the x_bar:  
var(x_bar) = var(sum of xi / n) = sum of var(xi) / n^2 = var(xi) / n = S^2 / n

hypothesis testing is all about assume h0 is true until proven otherwise.

Ok let's assume hypothesis is true. then the x_bar should follow a normal distribution with mean=10 and variance of S^2 / n.

So what is the equivalent Z value on a N(0,1) distribution for the observed x_bar on the N(10, S^2) normal distribution?

The formula is Z = (x_bar_observed - 10)/ Sqr(S^2/n).  

After obtaining this Z value, we can compare it with the standard table and decide to not reject the null hypothesis based on some requirement.
E.g. if this Z value falls within the 95% central area, then we will not reject the null hypothesis.
From standard normal distribution table, we know that the area with 95% probability is -1.96<Z<1.96.
Therefore we just have to compare our computed Z value with -1.96 and 1.96.
If it is within this range, we will not reject H0. otherwise we reject H0.

Btw, at the end we can only say that we do not reject the null hypothesis,
which is not to say the null hypothesis is absolutely true.


What about p value
----------------------------

Instead of using Z value, equivalently we can use the p value.

P value is the area of the distribution such that the variable interested > the observation on the right side or variable interested < the observation on the left side (assumed h0 is true).

E.g. using the previous example,
the p value = Pr( x_bar > x_bar_observed) = Area of normal distribution N(10, S^2/n) when x_bar > x_bar_observed.
(again, note that x_bar here is a random variable while x_bar_observed is an observation)

when using p value, we also need a 'threshold'.
E.g. if we set our threshold to be 0.025,
then if p < 0.025, we have to reject the null hypothesis because the observed value is too 'far' away from the hypothesized mean.

As long as i understand the concept of p value, the whole process is exactly equivalent to the method when using z value.

In conclusion, a large p value favor the null hypothesis while a small p value may lead to rejection of the null hypothesis.

P value is good for reporting, because the number has a meaning - probability.

For easier visualizing this in the head, just imagine a normal distribution, and an observed value with a vertical line,
and then the p value is the area of the distribution from the nearest tail to the observed value.  
When the p value is large, it must mean the observed value is closer to the hypothesized mean (good thing if we want to not reject the null hypothesis).


What if n is not large enough
-------------------------------------

When the observed sample size is not large enough, the random variable x_bar will follow a Student's t distribution.
T distribution has its own lookup table.
We can use similar way to decide if we want to reject or not reject the null hypothesis.


More general case
-----------------------------------

I think as long as we have a null and an alternative hypothesis and has a way to reject or not reject the null hypothesis (assume the null hypothesis is correct in the first place),
it will be considered a hypothesis test.

One example is the test of goodness of fit.
There is also a null hypothesis saying that the distribution of a variable follows a hypothesized distribution.
Then use the chi-square test to test it.
