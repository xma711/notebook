Generative model
----------------------

i.e. how to solve the classification problem using pure stats?

ultimately it is this problem: h(y) = argmax_over_y P(Y=y | X=x)

The direct way is to find out the distribution of p(x, y) which allows us to solve the problem directly 
(i.e. p(y|x) = p(x,y) / p(x) = p(x,y) / INTEGRATE(p(x,y)dy) )  
or   
the distribution of p(x | y) and p(y) which allows us to solve the problem using bayes' rule  
(i.e. p(y|x) = p(y)*p(x|y) / p(x) = p(y)*p(x|y) / INTEGRATE(p(x,y)dy) = p(y)*p(x|y) / INTEGRATE(p(x|y)p(y)dy)  )


compare generative and discriminative models
--------------------------------------------------

reference: https://medium.com/@mlengineer/generative-and-discriminative-models-af5637a66a3

both of them is predicting the conditional probability p(y|x).
but both models learn different probabilities.

a generative model learns the joint probability distribution p(x,y).
it predicts the conditional probability with the help of Bayes Theorem.

a discriminative model learns the conditional probability distribution p(y|x).


if x is univariate
--------------------------

if x is univariate, i.e. only one random variable, the problem is easier.  
we just have to collect enough data to compute p(x|y).  
i.e. when y is {cat, dog} while x is the first pixel of the image (unrealistic; just for illustration purpose),
we are trying to find out which of p(y=cat | x) and p(y=dog | x) is larger. 
then pick the y that has a larger probability value given x.

now the question is how to estimate p(x | y)?  
one way is that we have to set a distribution for p(x|y) with some unknown parameters,
then we can use MLE or MAP to solve the unknowns.  
e.g. we can assume p(x|y) is normal distribution (i.e. 2 different normal distribution, as y can be cat or dog).  
when p(x|y) is known, and p(y) is known, we can solve the problem.

the next question is how to check if the sample size is large enough?  

(need to correct this part using knowledge learnt from Simulation module) for normal distribution, we know that x_mean follows normal distribution of mu and S^2/N, where mu is the true mean and N is the sample size.  
we can solve the problem of 
```
p(|(x_mean - mu)| / (S/sqrt(N)) < epsilon) = sigma
```
to get an expression for N.
Assume the result is N = f(epsilon, sigma), then we can an expression for the sample size given the error bound epsilon and the probability sigma we want.  
this should be similar to the PAC theory.


if x is multivariate
-----------------------------

e.g. when x has 2 pixels, how to find out p(y|x)?

intuitively, if we have a lot of images, we can plot out the distribution of y when x=x1, x=x2, x=x3....  
e.g. let's say x can only be 0 and 1. then x has 4 choices.
if for each choice of x, we have a lot of images. 
then we can find out p(y | x = xi) for each xi.  
then the answer of p(y | x=xi) is already solved.

in this case, for each xi, we need to have enough images to estimate the distribution of y.  
similarly we can find out the sample complexity for this particular distribution.

for each xi, we have a set of parameters for p(y | x=xi).  
therefore we need O(K^L) parameters, where L is the length of x and K is a constant.

for each parameter, we need certain number of images.
this turns out to be problematic because we need O(K^L) data to do the estimation.

one solution is to use Naive Bayes, which assumes that each element in x is independent.  
then we can express p(x | y) = PRODUCTS( p(xi | y) ) where xi is an element in x (not each data point in this case).

however, in reality, the elements are usually not independent.  
then how?  
one way is to use graphic model to solve this.
