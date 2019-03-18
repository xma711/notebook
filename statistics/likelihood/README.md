Maximum likelihood estimation (MLE)
------------------

After collecting data, one may think that the model that can fit these data is normal distribution 
(or any other educated guesses).  
Now the question is: what is the values of the parameters of this model given these collected data?  
In the normal distribution case, the question is what are mean and variance?

One solution is the maximum likelihood,'
which is to maximize L(p ; x) or L(p | x) (which is not the same as P(p | X) ), where p is the parameters (sometimes we use theta) and x are the observed data.

Reference http://statgen.iop.kcl.ac.uk/bgim/mle/sslike_3.html says: 
the aim of maximum likelihood estimation is to find the parameter value(s) that
makes the observed data most likely.

Note that this is slightly different from probability.  
To get the probability of an event, it is before we have any data. 
And we have a model in mind with parameters known. 
Then we try to calculate what is the probability of an event (or a random variable).

Probability: knowing parameters -> prediction of outcome  
likelihood: observation of data -> estimation of parameters

application of MLE: estimate model parameters, 
test if the estimated parameter differs significantly from the expected parameter 
(e.g. flip a coin, we know that normally probability of head is 0.5. 
But from data, it may not be so, which may show that the coin is biased.)


Example: flip a coin
----------------------

Flip a coin 100 times.  
Outcome: head = 56, tail = 44.  
Model: Binomial distribution: P(k,n) = nCk p^k (1-p)^(n-k) 
where k = number of occurrence of a head, and n = total number of coin flipping, p is the probability of a head

before we try to estimate the maximum likelihood, let's try a number first.  
Say p = 0.5, what is the likelihood?  
L(p=0.5 ; data) = P(data | p=0.5) = 100C56 0.5^56 (1-0.5)^44 = 0.0389.  
What about p = 0.52, L(p=0.52 ; data) = 0.0581.  
In these two cases, p = 0.52 is more likely than p = 0.50.

However, we need to try many times in this way to get the maximum likelihood.  
Is there any short-cut? indeed yes.

L(p ; data) = L(p | data) = P(data | p) =100C56 p^56 (1-p)^44.  
So log(L) = log(100C56) + 56log(p) + 44log(1-p).  (log function is monotonous, which won't change the order of numbers)
d( log(L) )/d(p) = 56 * 1/p + 44 * 1/(1-p) * (-1) = 56/p - 44/(1-p)  
set this to 0, and solve p, we will have p = 0.56! 
This is the MLE for p such that the model with p=0.56 makes the observed data most likely.


Example: normal distribution
---------------------------

Model: the probability density function of normal distribution is  
f(xj) = (2 PI var^2)^(-1/2) exp(-1/2 (xj - mean)^2 / var^2 )  
and the parameters are mean and var (squre root of variance).

Now we have collected data x1 to xn. how to estimate mean and var?

Likelihood function L(mean, var^2 ; x1,....,xn ) = f(x1,...,xn | mean, var^2) = (2 PI var^2)^(-1/2) exp(-1/(2 var^2) SUM_j_1_to_n{ (xj - mean)^2 } )  
the function may look weird, but it is actually sum of individual likelihood values for each xj. 
Proof: http://www.statlect.com/fundamentals-of-statistics/normal-distribution-maximum-likelihood

the log-likelihood function is   
l(mean, var^2 ; x1,...,xn) = -n/2 ln(2PI) - n/2 ln(var^2) - 1/(2 var^2) SUM_j_1_to_n{ (xj - mean)^2 }

then solve for d(l)/d(mean) = 0 and d(l)/d(var^2) = 0 (both are partial differentiation), we will have  
mean_estimated = 1/n SUM_j_1_to_n{xj} and   
var^2_estimated = 1/n SUM_j_1_to_n{ (xj - mean_estimated)^2 }
