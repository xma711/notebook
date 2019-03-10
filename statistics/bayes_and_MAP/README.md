Bayes' theorem
------------------------

in math, it is P(A | B) = P(B | A) * P(A) / P(B)

in words, it means the posterior distribution of A ( P(A | B) ) equals to result of the likelihood of B given the prior distribution of A ( P(B | A) ) multiplying the prior distribution of A ( P(A) ), 
normalized by the probability of B without any conditions.

in some sense, this means that we have some prior belief in the distribution of A, 
and later given some observation B, we can improve on our belief on the distribution of A. 
in fact, this is the bayesian interpretation of the Bayes' theorem.


MAP (maximum a posteriori estimation)
-------------------------------------- 

we know that maximum likelihood estimation (MLE) is that imagining a distribution with some parameters (the parameters don't have to be the traditional mean or variance, it can be anything inside),
we form an equation to calculate the probability of the observations given this distribution (the equation will be expressed in terms of the parameters),
and then we maximize this equation to obtain the optimal values of the parameters. (usually we take log on the equation before maximize it for easier calculation)

MAP is slightly different.  
we need to have a prior belief on the distributions of the parameters themselves (e.g. normal distribution with 0 means).  
we form an equation to describe the posterior distribution of the parameters given the observations, 
which (using Bayes' theorem) equals to the probability of the observations given the distribution of the parameters and other information (?) 
mutiplied by the probability of the parameters (prior), normalized by a P(observations) that can be negelected (because it is not a function of the parameters.)  
again, this equation is expressed in terms of the parameters.  
we then maximize this function to obtained the optimal values of the parameters. (again we usually do a log on it before maximizing it.)

one example is that let yi = wT xi + noise; wT is the parameter array we try to find.  
let the distribution of the noise be normal distribtuion with 0 mean and sigma^2 variance.  
the distribtuion of each yi is normal distribtuion with (wT xi) mean and sigma^2 variance.  
using MLE, we form an likelihood function on the observations yi, so li = P(yi | wT) = sub y = yi into the normal distribtuion function = C exp(-(yi - wT xi)^2/C2), 
and the total likelihood = l1 * l2 * l3 ...  
taking a log, we have L = log(l1) + log(l2) + log(l3) + ... = sum of (- (yi - wT xi)^2)  (neglected the constants).  
then we can do a dL/dw = 0 to obtain the optimal values for w.  
(btw this is exactly the same as using the normal square error function when we try to find out the optimal values for wT using matrix differentiation directly.)  

when using MAP, we form the equation for the posterior distribution of wT,
which equals to probability of (all yi) given the distribution of yi mutiplied by the probability of wT (based on its own distribution)  (constants are ignored)
which equals to (l1*l2*l3...) * P(wT).  
taking log, we have L = sum of log(li) + log(P(wT)).  
sum of log(li) have the same equations as MLE. now we have one extra part: log(P(wT)).  
assume each wi in wT follows a normal distribution of 0 mean (prior belief), 
log(P(wT)) = log(P(w1)) + log(P(w2)) + ...   
each log(P(wi)) can be expressed as log (sub w = wi into the normal distribution function of w) = -wi^2/C.  
so log(P(wT)) = -1/C (w1^2 + w2^2 + ...) = lambda * ||w||^2.  
therefore the overall MAP equation can be written as sum of log(li) + log(P(wT)) = sum of (- (yi - wT xi)^2) + lambda * ||w||^2, which is purely in terms of w.  
we can do a dL/dw = 0 to obtain the optimal values for w.

compared with MLE, MAP has an extra term: lambda * ||w||^2.
therefore, MAP can be viewed as a regularized version of MLE.
