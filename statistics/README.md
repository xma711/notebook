Random experiment
-----------------------------

Reference: cs5229 advanced computer networks module

consider a random experiment whose outcome cannot be determined in advance.

Sample space S: the set of all outcomes

Event E: a subset of the sample space (An event E occurs if the outcome s belongs to E)

probability function P(E): the probability that event E happens


Random Variable
----------------------------

A random variable X is a mapping *function* X:S -> R that assigns a real value to each outcome s (belongs to S).

There is nothing random in a random variable, because it is a deterministic function. what is random is the events.

Let A be a set in R (real numbers), P{X = A} = P( the events that result in outcome A, or X_Inverse(A) )


Distribution
----------------------------

The distribution function F of the random variable X is defined on any real number x by  
	F(x) = P{X <= x} = P(X_Inverse(-inf, x))

A random variable is continuous if there exists a probability density function f(x) such that  
	f(x) = d(F(x))/dx  

In a continuous random variable, P(X = x) = d(F(x)) = d(F(x))/dx * dx = f(x) * dx. (Sum all f(x)*dx = 1)
	- to get the average of something continuous, it is similar to the discrete case. E[X] = SUM {x * P(X=x)} = SUM (x * f(x) * delta x) = INTEGRATE(-inf, +inf) {x*f(x) dx}


Kurtosis
------------------------

Reference: https://en.wikipedia.org/wiki/Kurtosis

kurtosis is a measure of the "tailedness" of the probability distribution of a real-valued random variable.
It is a descriptor of the shape of a probability distribution.

The standard measure of kurtosis (there could be other ways of calculation) is based on a scaled version of the 4th moment of the data or population.
The number is related to the tails of the distribution, not its peak;
higher kurtosis is the result of infrequent extreme deviations (outliers), as opposed to frequent modestly sized deviations.

The kurtosis of any univariate normal distribution is 3.
It is common to compare the kurtosis of a distribution to this value.

Distributions with kurtosis less than 3 are said to be platykurtic.
It means the distribution produces fewer and less extreme outliers than does the normal distribution.

Distributions with kurtosis greater than 3 are said to be leptokurtic.
Such a distribution produces more outliers than the normal distribution.

It is common practice to use an adjusted version of Pearson's kurtosis, the excess kurtosis, which is the kurtosis minus 3.


Skewness
----------------

Reference: https://en.wikipedia.org/wiki/Skewness

skewness is a measure of the asymmetry of the probability distribution of a real
-valued random variable about its mean.
The skewness value can be positive or negative or undefined.

Skew does not refer to the direction the curve appears to be leaning;
in fact, the opposite is true.

For unimodal distribution, negative skew indicates that the tail on the left side of the probability density function is longer or fatter than the right side - it does not distinguish these 2 kinds of shape.  
Positive skew indicates that the tail on the right side is longer or fatter than the left side.

Btw in the reference there are graphs to show the skewness - easier to be understood.

Moments
-----------------

The expectation or mean or the 1st moment of a random variable X:  
	E[X] = Integrate(+inf to -inf) xf(x) dx or E[X] = Sum(+inf to -inf) xP(X=x)

the 2nd moment of a r.v. X:  
	E[X^2] = Integrate(+inf to -inf) x^2 f(x) dx or E[X] = Sum(+inf to -inf) x^2 P(X=x)

variance = Var[X] = E[(X-E[X])^2] = E[X^2] -E^2[X]


Conditional probability
--------------------------

P(Ei|Ej) = P(Ei Union Ej) / P(Ej)

Bayes' Rule: P(Ei|Ej) = P(Ej|Ei) * P(Ei) / P(Ej)

The same rules will hold for random variable. change () to {} using the format in this readme.


Independence
--------------------------
P(Ei Intersect Ej) = P(Ei) * P(Ej) or P(Ei|Ej) = P(Ei)


Pearson correlation
-------------------------

Pear so correlation is a measure of the linear correlation between 2 variables x and y.
It has a value between +1 and -1, 
where 1 is total positive linear correlation,
0 is no linear correlation
and -1 is total negative linear correlation.

It can be used to check if 2 features are highly linearly correlated (either positively or negatively).
If yes, using only one of the features is enough.

P(x,y), the Pearson correlation of vector x and vector y = cov(x, y) / (sd(x) * sd(y))
