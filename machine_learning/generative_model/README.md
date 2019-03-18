Generative model
----------------------

I.e. how to solve the classification problem using pure stats?

Ultimately it is this problem: h(y) = argmax_over_y P(Y=y | X=x)

The direct way is to find out the distribution of p(x, y) which allows us to solve the problem directly 
(i.e. p(y|x) = p(x,y) / p(x) = p(x,y) / INTEGRATE(p(x,y)dy) )  
or   
the distribution of p(x | y) and p(y) which allows us to solve the problem using bayes' rule  
(i.e. p(y|x) = p(y)*p(x|y) / p(x) = p(y)*p(x|y) / INTEGRATE(p(x,y)dy) = p(y)*p(x|y) / INTEGRATE(p(x|y)p(y)dy)  )


compare generative and discriminative models
--------------------------------------------------

Reference: https://medium.com/@mlengineer/generative-and-discriminative-models-af5637a66a3

both of them is predicting the conditional probability p(y|x).
But both models learn different probabilities.

A generative model learns the joint probability distribution p(x,y).
It predicts the conditional probability with the help of Bayes Theorem.

A discriminative model learns the conditional probability distribution p(y|x).


If x is univariate
--------------------------

If x is univariate, i.e. only one random variable, the problem is easier.  
We just have to collect enough data to compute p(x|y).  
I.e. when y is {cat, dog} while x is the first pixel of the image (unrealistic; just for illustration purpose),
we are trying to find out which of p(y=cat | x) and p(y=dog | x) is larger. 
Then pick the y that has a larger probability value given x.

Now the question is how to estimate p(x | y)?  
One way is that we have to set a distribution for p(x|y) with some unknown parameters,
then we can use MLE or MAP to solve the unknowns.  
E.g. we can assume p(x|y) is normal distribution (i.e. 2 different normal distribution, as y can be cat or dog).  
When p(x|y) is known, and p(y) is known, we can solve the problem.

The next question is how to check if the sample size is large enough?  

(need to correct this part using knowledge learnt from Simulation module) for normal distribution, we know that x_mean follows normal distribution of mu and S^2/N, where mu is the true mean and N is the sample size.  
We can solve the problem of 
```
p(|(x_mean - mu)| / (S/sqrt(N)) < epsilon) = sigma
```
to get an expression for N.
Assume the result is N = f(epsilon, sigma), then we can an expression for the sample size given the error bound epsilon and the probability sigma we want.  
This should be similar to the PAC theory.


If x is multivariate
-----------------------------

E.g. when x has 2 pixels, how to find out p(y|x)?

Intuitively, if we have a lot of images, we can plot out the distribution of y when x=x1, x=x2, x=x3....  
E.g. let's say x can only be 0 and 1. then x has 4 choices.
If for each choice of x, we have a lot of images. 
Then we can find out p(y | x = xi) for each xi.  
Then the answer of p(y | x=xi) is already solved.

In this case, for each xi, we need to have enough images to estimate the distribution of y.  
Similarly we can find out the sample complexity for this particular distribution.

For each xi, we have a set of parameters for p(y | x=xi).  
Therefore we need O(K^L) parameters, where L is the length of x and K is a constant.

For each parameter, we need certain number of images.
This turns out to be problematic because we need O(K^L) data to do the estimation.

One solution is to use Naive Bayes, which assumes that each element in x is independent.  
Then we can express p(x | y) = PRODUCTS( p(xi | y) ) where xi is an element in x (not each data point in this case).

However, in reality, the elements are usually not independent.  
Then how?  
One way is to use graphic model to solve this.
