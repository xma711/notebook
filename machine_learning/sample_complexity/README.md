Sample complexity
---------------------

Reference: https://en.wikipedia.org/wiki/Sample_complexity

the right question to ask is:  
what is the sample complexity of a machine learning algorithm?

E.g. what is the sample complexity of the "empirical risk minimization" algorithm (ERM)?

Note that "algorithm" in this case can be as general as "empirical risk minimization".  
(other examples of "algos" include structural risk minimization (SRM) and regularized loss minimization (RLM) )
we don't really have to care about how exactly this ERM is performed, 
and we only have to know that ERM will be performed and the hypothesis with the minmium risk will be selected.

The whole point of sample complexity is not to calculate a sample size in order to
get a hypothesis that results in a very small risk (error) for population.  
The correct thinking should be, given a hypothesis class, 
what is the sample size with which we can find a hypothesis whose pupulation risk is not too larger than the population risk of the best possible hypothesis from this hypothesis class.

This implies that when sample complexity is low, it does not mean we can find a good solution when sample size is large. 
It only means that we are able to find a solution that is not too bad compared to the best solution in this hypothesis class.  
If the best solution in the hypothesis class is already very bad, 
then no matter how easily achivable the sample complexity is, we can't get a globally good solution.

Also, what exactly is the meaning of risk?  
(reference: textbook chapter 2)  
the risk to be calculated actually depends on the loss function.  
With different loss function, the risk will be calculated differently.  
However, whatever loss function is used, conceptually there is a risk for population given a h and an empirical risk for the sample given a h.  
Therefore, we can still claim that sample complexity of an algo is about calculating a sample size such that the algo will be able to obtain a h that has risk not much more than the best possible risk on population, no matter what loss function is used.  
(actually, this means that, when different loss function is used, 
the sample size required to achieve a certain error bound can be different. correct??)


No free lunch theorem (NFL)
---------------------------

NFL means that if we allow any distribution for X and Y, then given an algorithm (e.g. ERM),
we can always find a distributiion of X and Y such that the learning algorithm will fail to learn the globally optimal function, 
no matter how large the sample is.

E.g. given a hypothesis class that contains all possible functions (functions from SVM, random forest, neural network and more),
and a learning algorithm being the ERM,
there is not finite sample size to learn the target function for all distributions of X and Y.

However, if we limit the "size" of the hypothesis class (this size can be represent by the VC dimension of the hypothesis class),
then the sample complexity is finite, even if the distribution of the X and Y is not restricted.

This implies the importance of prior knowledge.  
If we don't even know which hypothesis class is the better one, 
what we can do are: 
randomly pick one --> this may lead to a bad best possible hypothesis,  
or  
pick a very general class --> this leads to a high requirement on the sample size.  
(both ways have some issues.)
 
Overall, if we want to have a finite sample complexity, we can do either:  
	- limit the hypothesis class without limiting the distribtuion of X and Y (discrimative methods???) OR
	- limit the space of distribution for X and Y. (e.g. via a parametric approach)


the whole story recapped
----------------------------------

Reference: https://en.wikipedia.org/wiki/Sample_complexity

sample complexity of an algo is the sample needed for the algo
to find a good solution for the population 
compared to the best possible solution for the population.

Given an algo, if we allow any distribtuions for X and Y,
is there a finite sample size such that the algo will be able to learn a good solution for population compared to the best possible solution for population?

The answer is No, due to the no-free-lunch theorem (NFL).

NFL says taht for an algo, given any sample size, we can always find a distribtuion of X and Y
such that the algo fails to learn a good solution for the population.

Then what can we do?  
1. limit the probability distribution space for X and Y. e.g. we can assume the distribution is parameterized and learn the parameters using methods like MLE.  
2. limit the hypothesis class while allowing any distributions for X and Y.  
E.g. we can set the hypothesis class to linear functions. 
Then the sample complexity is finite, because linear-functions class has a finite VC dimension.

Good solution and overfitting
-------------------

Reference: textbook chapter 2

just now when we mention "good solution" or "good hypothesis",
we are talking about general risk/error, not sample risk/error.

Interesting, so far we have not talked about test data yet.

This means that, when the vc dimension of the hypothesis class is finite
and when the sample size is large enough,
the ERM algorithm is able to find a solution that is not overfitting!!

I think the intuition is that, when there is enough sample,
the sample starts to represent the population well. 
Then there is less likely for ERM to find a solution that does not fit the population.

One natural question is that, then what is the use of the test dataset?  
Refer to section "test dataset" for answer.


Uniform convergence
-------------------------

Intuitively given a hypothesis class, if this condition holdes:  
	"when sample size > a certain number  
	each h from the hypothesis class results in a sample risk that is close to the population risk",  
then we can this hypothesis class has the uniform convergence property.

It follows that if H has unifrom convergence property,
the ERM algo is a agnostic PAC learner for H.
I.e. ERM is able to find a good h for population compared to the best possible h for population.


Approximation error and estimation error
--------------------------------------------

Let hs be the h learnt by ERM based on sample s.  
LD(hs) is the population error.

We can decompose LD(hs) to LD(hs) = appr_error + est_error,  
where appr_error = min{over H} LD(h) 
and est_error = LD(hs) - appr_error

the approximation error is the minimum risk achivable by a predictor in the hypothesis class, 
which does not depend on the sample size.  
Enlarging the hypothesis class can decrease the appr_error.

The estimation error results because the empirical risk is only an estimate of the true risk.  
The quality of this estimation depends on the training set size and
on the complexity of the hypothesis class.

We face a tradeoff, the bias-complexity tradeoff.  
In many cases, the empirical research focuses on designing good hypothesis classes for a certain domain.

Note that by now we are always talking about one single set of training data (there is no test data).  
Will the existence of the test data change the bias-complexity tradeoff? (the answer is no. read the next section.)


Is it possible to reduce approximation error while maintaining estimation error?
---------------------------------------------

Firstly, let's look at training error along.

If we get the best h1 from H1 using ERM and the best h2 from H2 using ERM,
and then pick the better h from {h1, h2} in terms of training error as the overall choice of hypothesis h (this is exactly the same as pick h from H = {h1, h2} using ERM), 
will this h better than either h1 or h2 in terms of population error?

The answer is not necessarily.  
Because this h may be overfitting the training data (large estimation error).  
If the sample size is not enough for the full H, the h chosen in this case is very likely overfitting the training data.

Therefore, looking at training error alone, this does not violate the bias-complexity tradeoff.  
Even if we run EMR on 2 different hypothesis classes, such as SVM and logistic regression, the best ERM h is not necessarily the better one compared to the best ERM h from either SVM or logistic regression.

To ensure the EMR h from {H1, H2} is better than h1 or h2 in terms of population error, we do need more data to do the training.

On the other hand, if we look at the test error and pick the h from {h1, h2} such that h has a smaller test error, 
is h better than either h1 or h2?

The answer seems yes but it is wrong when we do this on many Hi!!

This time, the h chosen is not necessarily the same as the EMR h from the full H.

Does this mean that the existence of test data makes the bias-complexity tradeoff invalid?  
In another words, with the test data, can we reduce the bias (approximation error) and also reduce the estimation error?  

One example is that: we run ERM on different hypothesis classes with the sample,
and then pick the h that leads to the smallest test error.  
Does this violate the bias-complexity trade-off?

Another thing is that if we know the sample size is not enough for the full H, can we chop H up and then run EMR on each Hi, 
and at the end we choose the hi that results in a smallest test error?  
This method should be nicknamed "Test risk minimization"..  

The h that results in a smallest test error is no longer the best for the population, because this h could be overfitting the test data!!  
This means that the Test Risk Minimization algo has a limit itself.  
When the number of hypothesis classes increases to a certain limit, the population error actually increases, because the overall estimation error increases.

Therefore, it seems that with a test dataset, the bias-complexity tradeoff is still there!  
Because while we are pushing the approximation error to 0, the estimation error starts to increases when the number of hypothesis classes reaches certain number.

To reduce the estimation error further, there is no way but to increase the sample size.


Test dataset
------------------------

Reference: textbook chapter 11

so, for the PAC learnable case, since we are able to get the sample complexity for the ERM algo,
why do we still want to use a test dataset in practice?

A few reasons:  
1. the sample bound we obtain from the VC dimension is for all hypothesis in the class and for all distributions of X and Y,
so the bound can be quite hard to achieve.  
2. the difference between the test dataset risk and the true risk has a smaller bound

therefore, using a test dataset (i.e. validation set) is easier for us to estimate the true risk in practice.

When the test error is large,
we have to rely on both the training error and the test error to 
deduce which component of the sample error is large:  
is it the approximation error or the estimation error?

If it is the approximation error being too large, 
then we should consider expand the hypothesis class (e.g. increase the degrees in the polynomial function) 
or completely change a hypothesis class.

If it is due to a large estimation error, 
then we can increase the sample size if possible.  
We can also consider reduce the hypothesis class complexity.  
(any other ways? check testbook chapter 11)

again, estimation error is the difference between the sample error and the true best possible error.  
Again, when the hypothesis class becomes richer, the approximation error will drop while the estimation error increases (given the same sample size).


Boosting
-------------------------

Is there a way to tune the approximation error and estimation error smoothly?

Answer: yes.  
Example: adaboost.

Check chapter 10 for the details of adaboost algorithm.

The idea behind boosting is that  
given a weak learner (e.g. it is a simple hypothesis class and the ERM returns a h that only performs slightly better than random guess),  
theoretically and practically there is a way to boost it to a strong learner.  
How?

One way is adaboost.  
Give each example a weight.  
The weights will be changed in the next round. the example that has a wrong prediction will have a higher weight.  
Each round the weak learner will return a ht.  
Ultimately the hs = linear combination of ht

the number of rounds = T.  
It can be shown that T is the single parameter to tune the appr_error and est_error tradeoff.  
When T is large, appr_error is smaller while est_error is larger.  
Using model selection method to find a good T


compuational complexity
--------------------------------

Reference: chapter 8

from stat's point of view, when the sample complexity of an algo (e.g. ERM) is 'okay',
we say the problem is learnable using this algo (e.g. ERM)..

However, from computational efficiency's point of view, this may not be true. 

E.g. for the finite class, the class size can be huge, 
and an exhaustive search (ERM) is computationally inefficient.

Therefore in practice we have to consider both sample complexity and computational complexity.

For many hypothesis classes and the loss function,
the ERM is very hard to learn, even when the sample size is large enough. (see chapter 8 for some examples)

the linear predictor hypothesis class is popular because it is usually computationally efficient to perform ERM over this class. (not all)

e.g. for logistic regression (with log loss function) and linear regression (with square loss function), it is computationally efficient to learn.

For halfspace with the realizability assumption (0-1 loss), it is also computationally efficient to learn.  
However, for halfspace without the realizability assumption (0-1 loss), it is NP-hard to learn. (ultimately we will use SVM to 'solve' this)


convex function and RLM
--------------------

Reference: chapter 12 and 13

convex-Lipschitz-bounded and convex-smooth-bounded are 2 families of learning problems that are learnable.

Question: by what algorithm? ERM?  
Answer: the 2 families of learning problems are learnable by ERM to a certain extend only; not true for all.

Then by what algorithm?  
Regularized loss minimizaation is able to learn all convex-lipschitz-bounded and convex-smooth-bounded learning problems.

Intuitively, the complexity of the hypothesis is measured by the value of the regularizaton function, and the algorithm balances between low empirical risk and simpler or less complex hypothesis.

One of the most simple regularization function is lambda * ||w||^2, where ||w|| is l2 norm. this type is called Tikhonov regularization.

A usual linear regression + a l2 norm regularization is called ridge regression.  
It can be shown that ridge regression is pac learnable.

